# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utilities for parsing arguments to `gcloud tasks` commands."""

from apitools.base.py import encoding
from googlecloudsdk.command_lib.tasks import app
from googlecloudsdk.command_lib.tasks import constants
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.util import files


_PROJECT = properties.VALUES.core.project.GetOrFail


class NoFieldsSpecifiedError(exceptions.Error):
  """Error for when calling an update method with no fields specified."""


def ParseProject():
  return resources.REGISTRY.Parse(
      _PROJECT(),
      collection=constants.PROJECTS_COLLECTION)


def ParseLocation(location):
  return resources.REGISTRY.Parse(
      location,
      params={'projectsId': _PROJECT},
      collection=constants.LOCATIONS_COLLECTION)


def ParseQueue(queue, location=None):
  """Parses an id or uri for a queue.

  Args:
    queue: An id, self-link, or relative path of a queue resource.
    location: The location of the app associated with the active project.

  Returns:
    A queue resource reference, or None if passed-in queue is Falsy.
  """
  if not queue:
    return None

  queue_ref = None
  try:
    queue_ref = resources.REGISTRY.Parse(queue,
                                         collection=constants.QUEUES_COLLECTION)
  except resources.RequiredFieldOmittedException:
    app_location = location or app.ResolveAppLocation()
    location_ref = ParseLocation(app_location)
    queue_ref = resources.REGISTRY.Parse(
        queue, params={'projectsId': location_ref.projectsId,
                       'locationsId': location_ref.locationsId},
        collection=constants.QUEUES_COLLECTION)
  return queue_ref


def ParseTask(task, queue_ref=None):
  """Parses an id or uri for a task."""
  params = queue_ref.AsDict() if queue_ref else None
  task_ref = resources.REGISTRY.Parse(task,
                                      collection=constants.TASKS_COLLECTION,
                                      params=params)
  return task_ref


def ExtractLocationRefFromQueueRef(queue_ref):
  params = queue_ref.AsDict()
  del params['queuesId']
  location_ref = resources.REGISTRY.Parse(
      None, params=params, collection=constants.LOCATIONS_COLLECTION)
  return location_ref


def ParseCreateOrUpdateQueueArgs(args, queue_type, messages, is_update=False):
  return messages.Queue(
      retryConfig=_ParseRetryConfigArgs(args, queue_type, messages, is_update),
      rateLimits=_ParseRateLimitsArgs(args, queue_type, messages, is_update),
      pullTarget=_ParsePullTargetArgs(args, queue_type, messages, is_update),
      appEngineHttpTarget=_ParseAppEngineHttpTargetArgs(args, queue_type,
                                                        messages, is_update))


def ParseCreateTaskArgs(args, task_type, messages):
  return messages.Task(
      scheduleTime=args.schedule_time,
      pullMessage=_ParsePullMessageArgs(args, task_type, messages),
      appEngineHttpRequest=_ParseAppEngineHttpRequestArgs(args, task_type,
                                                          messages))


def CheckUpdateArgsSpecified(args, queue_type):
  if queue_type == constants.PULL_QUEUE:
    if not _AnyArgsSpecified(args, ['max_attempts', 'max_retry_duration'],
                             clear_args=True):
      raise NoFieldsSpecifiedError('Must specify at least one field to update.')
  if queue_type == constants.APP_ENGINE_QUEUE:
    if not _AnyArgsSpecified(args, [
        'max_attempts', 'max_retry_duration', 'max_doublings', 'min_backoff',
        'max_backoff', 'max_tasks_dispatched_per_second',
        'max_concurrent_tasks', 'routing_override'], clear_args=True):
      raise NoFieldsSpecifiedError('Must specify at least one field to update.')


def _AnyArgsSpecified(specified_args_object, args_list, clear_args=False):
  clear_args_list = []
  if clear_args:
    clear_args_list = [_EquivalentClearArg(a) for a in args_list]
  return any(
      filter(specified_args_object.IsSpecified, args_list + clear_args_list))


def _EquivalentClearArg(arg):
  return 'clear_{}'.format(arg)


def _ParseRetryConfigArgs(args, queue_type, messages, is_update):
  """Parses the attributes of 'args' for Queue.retryConfig."""
  if (queue_type == constants.PULL_QUEUE and
      _AnyArgsSpecified(args, ['max_attempts', 'max_retry_duration'],
                        clear_args=is_update)):
    retry_config = messages.RetryConfig(
        maxRetryDuration=args.max_retry_duration)
    _AddMaxAttemptsFieldsFromArgs(args, retry_config)
    return retry_config

  if (queue_type == constants.APP_ENGINE_QUEUE and
      _AnyArgsSpecified(args, ['max_attempts', 'max_retry_duration',
                               'max_doublings', 'min_backoff', 'max_backoff'],
                        clear_args=is_update)):
    retry_config = messages.RetryConfig(
        maxRetryDuration=args.max_retry_duration,
        maxDoublings=args.max_doublings, minBackoff=args.min_backoff,
        maxBackoff=args.max_backoff)
    _AddMaxAttemptsFieldsFromArgs(args, retry_config)
    return retry_config


def _AddMaxAttemptsFieldsFromArgs(args, config_object):
  if args.IsSpecified('max_attempts'):
    # args.max_attempts is a BoundedInt and so None means unlimited
    if args.max_attempts is None:
      config_object.unlimitedAttempts = True
    else:
      config_object.maxAttempts = args.max_attempts


def _ParseRateLimitsArgs(args, queue_type, messages, is_update):
  """Parses the attributes of 'args' for Queue.rateLimits."""
  if (queue_type == constants.APP_ENGINE_QUEUE and
      _AnyArgsSpecified(args, ['max_tasks_dispatched_per_second',
                               'max_concurrent_tasks'],
                        clear_args=is_update)):
    return messages.RateLimits(
        maxTasksDispatchedPerSecond=args.max_tasks_dispatched_per_second,
        maxConcurrentTasks=args.max_concurrent_tasks)


def _ParsePullTargetArgs(unused_args, queue_type, messages, is_update):
  """Parses the attributes of 'args' for Queue.pullTarget."""
  if queue_type == constants.PULL_QUEUE and not is_update:
    return messages.PullTarget()


def _ParseAppEngineHttpTargetArgs(args, queue_type, messages, is_update):
  """Parses the attributes of 'args' for Queue.appEngineHttpTarget."""
  if queue_type == constants.APP_ENGINE_QUEUE:
    routing_override = None
    if args.IsSpecified('routing_override'):
      routing_override = messages.AppEngineRouting(**args.routing_override)
    elif is_update and args.IsSpecified('clear_routing_override'):
      routing_override = messages.AppEngineRouting()
    return messages.AppEngineHttpTarget(
        appEngineRoutingOverride=routing_override)


def _ParsePullMessageArgs(args, task_type, messages):
  if task_type == constants.PULL_QUEUE:
    return messages.PullMessage(payload=_ParsePayloadArgs(args), tag=args.tag)


def _ParseAppEngineHttpRequestArgs(args, task_type, messages):
  """Parses the attributes of 'args' for Task.appEngineHttpRequest."""
  if task_type == constants.APP_ENGINE_QUEUE:
    routing = (
        messages.AppEngineRouting(**args.routing) if args.routing else None)
    http_method = (messages.AppEngineHttpRequest.HttpMethodValueValuesEnum(
        args.method.upper()) if args.IsSpecified('method') else None)
    return messages.AppEngineHttpRequest(
        appEngineRouting=routing, headers=_ParseHeaderArg(args, messages),
        httpMethod=http_method, payload=_ParsePayloadArgs(args),
        relativeUrl=args.url)


def _ParsePayloadArgs(args):
  if args.IsSpecified('payload_file'):
    return files.GetFileOrStdinContents(args.payload_file, binary=False)
  elif args.IsSpecified('payload_content'):
    return args.payload_content


def _ParseHeaderArg(args, messages):
  if args.header:
    headers_dict = {k: v for k, v in map(_SplitHeaderArgValue, args.header)}
    return encoding.DictToAdditionalPropertyMessage(
        headers_dict, messages.AppEngineHttpRequest.HeadersValue)


def _SplitHeaderArgValue(header_arg_value):
  key, value = header_arg_value.split(':', 1)
  return key, value.lstrip()


def FormatLeaseDuration(lease_duration):
  return '{}s'.format(lease_duration)


def ParseTasksPullFilterFlags(args):
  if args.oldest_tag:
    return 'tag_function=oldest_tag()'
  if args.IsSpecified('tag'):
    return 'tag="{}"'.format(args.tag)


def QueuesUriFunc(queue):
  return resources.REGISTRY.Parse(
      queue.name,
      params={'projectsId': _PROJECT},
      collection=constants.QUEUES_COLLECTION).SelfLink()


def TasksUriFunc(task):
  return resources.REGISTRY.Parse(
      task.name,
      params={'projectsId': _PROJECT},
      collection=constants.TASKS_COLLECTION).SelfLink()


def LocationsUriFunc(task):
  return resources.REGISTRY.Parse(
      task.name,
      params={'projectsId': _PROJECT},
      collection=constants.LOCATIONS_COLLECTION).SelfLink()

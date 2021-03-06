"""Generated client library for cloudtasks version v2beta2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudtasks.v2beta2 import cloudtasks_v2beta2_messages as messages


class CloudtasksV2beta2(base_api.BaseApiClient):
  """Generated client library for service cloudtasks version v2beta2."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudtasks.googleapis.com/'

  _PACKAGE = u'cloudtasks'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v2beta2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudtasksV2beta2'
  _URL_VERSION = u'v2beta2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudtasks handle."""
    url = url or self.BASE_URL
    super(CloudtasksV2beta2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_locations_queues_tasks = self.ProjectsLocationsQueuesTasksService(self)
    self.projects_locations_queues = self.ProjectsLocationsQueuesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsQueuesTasksService(base_api.BaseApiService):
    """Service class for the projects_locations_queues_tasks resource."""

    _NAME = u'projects_locations_queues_tasks'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsQueuesTasksService, self).__init__(client)
      self._upload_configs = {
          }

    def Acknowledge(self, request, global_params=None):
      """Acknowledges a pull task.

The lease holder, that is, the entity that received this task in
a PullTasksResponse, must call this method to indicate that
the work associated with the task has finished.

The lease holder must acknowledge a task within the
PullTasksRequest.lease_duration or the lease will expire and
the task will become ready to be returned in a different
PullTasksResponse. After the task is acknowledged, it will
not be returned by a later CloudTasks.PullTasks,
CloudTasks.GetTask, or CloudTasks.ListTasks.

To acknowledge multiple tasks at the same time, use
[HTTP batching](/storage/docs/json_api/v1/how-tos/batch)
or the batching documentation for your client library, for example
https://developers.google.com/api-client-library/python/guide/batch.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksAcknowledgeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Acknowledge')
      return self._RunMethod(
          config, request, global_params=global_params)

    Acknowledge.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:acknowledge',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.acknowledge',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:acknowledge',
        request_field=u'acknowledgeTaskRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksAcknowledgeRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def CancelLease(self, request, global_params=None):
      """Cancel a pull task's lease.

The lease holder can use this method to cancel a task's lease
by setting Task.schedule_time to now. This will make the task
available to be leased to the next caller of CloudTasks.PullTasks.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksCancelLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('CancelLease')
      return self._RunMethod(
          config, request, global_params=global_params)

    CancelLease.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:cancelLease',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.cancelLease',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:cancelLease',
        request_field=u'cancelLeaseRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksCancelLeaseRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Creates a task and adds it to a queue.

To add multiple tasks at the same time, use
[HTTP batching](/storage/docs/json_api/v1/how-tos/batch)
or the batching documentation for your client library, for example
https://developers.google.com/api-client-library/python/guide/batch.

Tasks cannot be updated after creation; there is no UpdateTask command.

* For [App Engine queues](google.cloud.tasks.v2beta2.AppEngineHttpTarget),
  the maximum task size is 100KB.
* For [pull queues](google.cloud.tasks.v2beta2.PullTarget), this
  the maximum task size is 1MB.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v2beta2/{+parent}/tasks',
        request_field=u'createTaskRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksCreateRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task
cannot be deleted if it has completed successfully or permanently
failed.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}',
        http_method=u'DELETE',
        method_id=u'cloudtasks.projects.locations.queues.tasks.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a task.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.tasks.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'responseView'],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksGetRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the tasks in a queue.

By default response_view is Task.View.BASIC; not all
information is retrieved by default due to performance
considerations; ListTasksRequest.response_view controls the
subset of information which is returned.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTasksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.tasks.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'orderBy', u'pageSize', u'pageToken', u'responseView'],
        relative_path=u'v2beta2/{+parent}/tasks',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksListRequest',
        response_type_name=u'ListTasksResponse',
        supports_download=False,
    )

    def Pull(self, request, global_params=None):
      """Pulls tasks from a pull queue and acquires a lease on them for a.
specified PullTasksRequest.lease_duration.

This method is invoked by the lease holder to obtain the
lease. The lease holder must acknowledge the task via
CloudTasks.AcknowledgeTask after they have performed the work
associated with the task.

The payload is intended to store data that the lease holder needs
to perform the work associated with the task. To return the
payloads in the PullTasksResponse, set
PullTasksRequest.response_view to Task.View.FULL.

A maximum of 10 qps of CloudTasks.PullTasks requests are allowed per
queue. google.rpc.Code.RESOURCE_EXHAUSTED is returned when this limit
is exceeded. google.rpc.Code.RESOURCE_EXHAUSTED is also returned when
RateLimits.max_tasks_dispatched_per_second is exceeded.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksPullRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PullTasksResponse) The response message.
      """
      config = self.GetMethodConfig('Pull')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pull.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks:pull',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.pull',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}/tasks:pull',
        request_field=u'pullTasksRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksPullRequest',
        response_type_name=u'PullTasksResponse',
        supports_download=False,
    )

    def RenewLease(self, request, global_params=None):
      """Renew the current lease of a pull task.

The lease holder can use this method to extend the lease by a new
duration, starting from now. The new task lease will be
returned in Task.schedule_time.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksRenewLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('RenewLease')
      return self._RunMethod(
          config, request, global_params=global_params)

    RenewLease.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:renewLease',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.renewLease',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:renewLease',
        request_field=u'renewLeaseRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksRenewLeaseRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      """Forces a task to run now.

This command is meant to be used for manual debugging. For
example, CloudTasks.RunTask can be used to retry a failed
task after a fix has been made or to manually force a task to be
dispatched now.

When this method is called, Cloud Tasks will dispatch the task to its
target, even if the queue is Queue.State.PAUSED.

The dispatched task is returned. That is, the task that is returned
contains the Task.task_status after the task is dispatched but
before the task is received by its target.

If Cloud Tasks receives a successful response from the task's
handler, then the task will be deleted; otherwise the task's
Task.schedule_time will be reset to the time that
CloudTasks.RunTask was called plus the retry delay specified
in the queue and task's RetryConfig.

CloudTasks.RunTask returns google.rpc.Code.NOT_FOUND when
it is called on a task that has already succeeded or permanently
failed. google.rpc.Code.FAILED_PRECONDITION is returned when
CloudTasks.RunTask is called on task that is dispatched or
already running.

CloudTasks.RunTask cannot be called on pull tasks.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTasksRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Task) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}/tasks/{tasksId}:run',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.tasks.run',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:run',
        request_field=u'runTaskRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTasksRunRequest',
        response_type_name=u'Task',
        supports_download=False,
    )

  class ProjectsLocationsQueuesService(base_api.BaseApiService):
    """Service class for the projects_locations_queues resource."""

    _NAME = u'projects_locations_queues'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsQueuesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a queue.

WARNING: Using this method may have unintended side effects if you are
using an App Engine `queue.yaml` or `queue.xml` file to manage your queues.
Read
[Overview of Queue Management and queue.yaml](/cloud-tasks/docs/queue-yaml)
carefully before using this method.

      Args:
        request: (CloudtasksProjectsLocationsQueuesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v2beta2/{+parent}/queues',
        request_field=u'queue',
        request_type_name=u'CloudtasksProjectsLocationsQueuesCreateRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, a queue with the same name can't be created
for 7 days.

WARNING: Using this method may have unintended side effects if you are
using an App Engine `queue.yaml` or `queue.xml` file to manage your queues.
Read
[Overview of Queue Management and queue.yaml](/cloud-tasks/docs/queue-yaml)
carefully before using this method.

      Args:
        request: (CloudtasksProjectsLocationsQueuesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}',
        http_method=u'DELETE',
        method_id=u'cloudtasks.projects.locations.queues.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a queue.

      Args:
        request: (CloudtasksProjectsLocationsQueuesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesGetRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a Queue.
Returns an empty policy if the resource exists and does not have a policy
set.

Authorization requires the following [Google IAM](/iam) permission on the
specified resource parent:

* `cloudtasks.queues.getIamPolicy`

      Args:
        request: (CloudtasksProjectsLocationsQueuesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v2beta2/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists queues.

Queues are returned in lexicographical order.

      Args:
        request: (CloudtasksProjectsLocationsQueuesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListQueuesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.queues.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v2beta2/{+parent}/queues',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsQueuesListRequest',
        response_type_name=u'ListQueuesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a queue.

This method creates the queue if it does not exist and updates
the queue if it does exist.

WARNING: Using this method may have unintended side effects if you are
using an App Engine `queue.yaml` or `queue.xml` file to manage your queues.
Read
[Overview of Queue Management and queue.yaml](/cloud-tasks/docs/queue-yaml)
carefully before using this method.

      Args:
        request: (CloudtasksProjectsLocationsQueuesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}',
        http_method=u'PATCH',
        method_id=u'cloudtasks.projects.locations.queues.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v2beta2/{+name}',
        request_field=u'queue',
        request_type_name=u'CloudtasksProjectsLocationsQueuesPatchRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def Pause(self, request, global_params=None):
      """Pauses the queue.

If a queue is paused then the system will stop executing the
tasks in the queue until it is resumed via
CloudTasks.ResumeQueue. Tasks can still be added when the
queue is paused. The state of the queue is stored in
Queue.state; if paused it will be set to
Queue.State.PAUSED.

      Args:
        request: (CloudtasksProjectsLocationsQueuesPauseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Pause')
      return self._RunMethod(
          config, request, global_params=global_params)

    Pause.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:pause',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.pause',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:pause',
        request_field=u'pauseQueueRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesPauseRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def Purge(self, request, global_params=None):
      """Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks
might be dispatched before the purge takes effect. A purge is irreversible.

      Args:
        request: (CloudtasksProjectsLocationsQueuesPurgeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Purge')
      return self._RunMethod(
          config, request, global_params=global_params)

    Purge.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:purge',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.purge',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:purge',
        request_field=u'purgeQueueRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesPurgeRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def Resume(self, request, global_params=None):
      """Resume a queue.

This method resumes a queue after it has been
Queue.State.PAUSED or Queue.State.DISABLED. The state of
a queue is stored in Queue.state; after calling this method it
will be set to Queue.State.RUNNING.

WARNING: Resuming many high-QPS queues at the same time can
lead to target overloading. If you are resuming high-QPS
queues, follow the 500/50/5 pattern described in
[Managing Cloud Tasks Scaling Risks](/cloud-tasks/pdfs/managing-cloud-tasks-scaling-risks-2017-06-05.pdf).

      Args:
        request: (CloudtasksProjectsLocationsQueuesResumeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Queue) The response message.
      """
      config = self.GetMethodConfig('Resume')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resume.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:resume',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.resume',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}:resume',
        request_field=u'resumeQueueRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesResumeRequest',
        response_type_name=u'Queue',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy for a Queue. Replaces any existing.
policy.

Note: The Cloud Console does not check queue-level IAM permissions yet.
Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](/iam) permission on the
specified resource parent:

* `cloudtasks.queues.setIamPolicy`

      Args:
        request: (CloudtasksProjectsLocationsQueuesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v2beta2/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on a Queue.
If the resource does not exist, this will return an empty set of
permissions, not a google.rpc.Code.NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (CloudtasksProjectsLocationsQueuesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}/queues/{queuesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'cloudtasks.projects.locations.queues.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v2beta2/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'CloudtasksProjectsLocationsQueuesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Get information about a location.

      Args:
        request: (CloudtasksProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2beta2/{+name}',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about the supported locations for this service.

      Args:
        request: (CloudtasksProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2beta2/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'cloudtasks.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v2beta2/{+name}/locations',
        request_field='',
        request_type_name=u'CloudtasksProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudtasksV2beta2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

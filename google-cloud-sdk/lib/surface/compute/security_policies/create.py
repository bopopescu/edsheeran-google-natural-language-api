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

"""Command for creating security policies."""
from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute.security_policies import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import completers
from googlecloudsdk.command_lib.compute.security_policies import flags


class Create(base.CreateCommand):
  """Create a Google Compute Engine security policy.

  *{command}* is used to create security policies. A security policy policy is a
  set of rules that controls access to various resources.
  """

  SECURITY_POLICY_ARG = None

  @classmethod
  def Args(cls, parser):
    cls.SECURITY_POLICY_ARG = flags.SecurityPolicyArgument()
    cls.SECURITY_POLICY_ARG.AddArgument(parser, operation_type='create')

    parser.add_argument(
        '--description',
        help='An optional, textual description for the security policy.')

    parser.display_info.AddCacheUpdater(completers.RoutesCompleter)

  def Collection(self):
    return 'compute.securityPolicies'

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    ref = self.SECURITY_POLICY_ARG.ResolveAsResource(args, holder.resources)
    security_policy = client.SecurityPolicy(ref, compute_client=holder.client)

    return security_policy.Create(description=args.description)

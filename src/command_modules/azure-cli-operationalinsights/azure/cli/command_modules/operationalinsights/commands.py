# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

#pylint: disable=line-too-long


def load_command_table(self, _):

    from azure.cli.core.commands import CliCommandType
    from azure.cli.command_modules.operationalinsights._client_factory import operationalinsights_data_plane_client

    operationalinsights_sdk = CliCommandType(
        operations_tmpl='azure.cli.command_modules.operationalinsights.custom#{}',
        client_factory=operationalinsights_data_plane_client
    )

    with self.command_group('operationalinsights', operationalinsights_sdk) as g:
        g.command('query', 'execute_query')

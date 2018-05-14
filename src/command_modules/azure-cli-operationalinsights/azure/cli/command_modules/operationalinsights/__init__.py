# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

# from azure.cli.command_modules.operationalinsights._help import helps  # pylint: disable=unused-import


class OperationalInsightsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.command_modules.operationalinsights._client_factory import operationalinsights_data_plane_client

        operationalinsights_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.operationalinsights.custom#{}',
            client_factory=operationalinsights_data_plane_client
        )

        super(OperationalInsightsCommandsLoader, self).__init__(
            cli_ctx=cli_ctx,
            custom_command_type=operationalinsights_custom
        )

    def load_command_table(self, args):
        from azure.cli.command_modules.operationalinsights.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        # super(OperationalInsightsCommandsLoader, self).load_arguments(command)
        from azure.cli.command_modules.operationalinsights._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = OperationalInsightsCommandsLoader

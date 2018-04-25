# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.profiles import ResourceType

class AppInsightsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from ._client_factory import appinsights_data_plane_client
        appinsights_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.appinsights.custom#{}')
        super(AppInsightsCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                    custom_command_type=appinsights_custom)

    def load_command_table(self, args):
        from azure.cli.command_modules.appinsights.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.appinsights._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = AppInsightsCommandsLoader
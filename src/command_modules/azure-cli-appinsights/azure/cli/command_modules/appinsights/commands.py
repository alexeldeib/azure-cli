def load_command_table(self, _):
    from azure.cli.core.commands import CliCommandType

    ai_data_sdk = CliCommandType(
        operations_tmpl='azure.cli.command_modules.appinsights.custom#{}')

    with self.command_group('appinsights', ai_data_sdk) as g:
        g.command('query', 'query')
        
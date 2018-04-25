def load_arguments(self, _):
    with self.argument_context('appinsights') as c:
        c.argument('app_id', help="The GUID representing an App Insights application", required=True)
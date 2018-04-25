
def appinsights_data_plane_client(appId):
    import sys
    import os
    from msrestazure.azure_active_directory import ServicePrincipalCredentials
    sys.path.append(os.path.abspath("C:\\Users\\alexe\\azure-sdk-for-python\\azure-applicationinsights"))
    from azure.applicationinsights.application_insights_data_client import ApplicationInsightsDataClient

    client_id = '0a7e0680-9fb9-443c-87e3-2f8e2a707de2'
    client_secret = 'ZwsaEYWSrE8Ich2cg5Ly6zrEqhiNNFja4q9XxeDnMOo='
    kwargs = {
        'tenant': '72f988bf-86f1-41af-91ab-2d7cd011db47',
        'resource': 'https://api.applicationinsights.io/',
    }
    creds = ServicePrincipalCredentials(client_id, client_secret, **kwargs)
    return ApplicationInsightsDataClient(creds, appId)

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def operationalinsights_data_plane_client(cli_ctx, _):
    from azure.operationalinsights import OperationalInsightsDataClient
    from azure.cli.core._profile import Profile
    profile = Profile(cli_ctx=cli_ctx)
    cred, _, _ = profile.get_login_credentials(resource='https://api.loganalytics.io')
    return OperationalInsightsDataClient(cred)

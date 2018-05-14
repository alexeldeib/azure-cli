# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

logger = get_logger(__name__)


def execute_query(client, workspace, kql):
    from azure.operationalinsights.models import QueryBody
    return client.query(workspace, QueryBody(kql))

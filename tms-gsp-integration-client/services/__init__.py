# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

"""
This package contains the service layer for the TMS GSP Integration addon.
It follows the principles of Clean Architecture by separating the core business logic
and external service interactions from the Odoo models.

- aws_secrets_manager.py: A client for securely fetching credentials from AWS.
- gsp_api_client.py: A low-level client responsible for direct HTTP communication with the GSP API.
- gsp_request_mapper.py: A transformer that converts Odoo invoice records into the GSP API's required format.
- gsp_service.py: The main orchestrator service that implements the sync/async fallback logic.
"""

from . import aws_secrets_manager
from . import gsp_api_client
from . import gsp_request_mapper
from . import gsp_service
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import requests
from odoo import models
from odoo.exceptions import UserError

from .aws_secrets_manager import AwsSecretsManager

_logger = logging.getLogger(__name__)


class GspApiClientError(Exception):
    """Base exception for GSP API client errors."""
    pass


class GspApiConnectionError(GspApiClientError):
    """Raised for network-level errors (e.g., DNS failure, refused connection)."""
    pass


class GspApiTimeoutError(GspApiClientError):
    """Raised when a request to the GSP API times out."""
    pass


class GspApiDataError(GspApiClientError):
    """Raised for 4xx HTTP client errors, indicating an issue with the sent data."""
    pass


class GspApiServerError(GspApiClientError):
    """Raised for 5xx HTTP server errors, indicating a problem with the GSP's servers."""
    pass


class GspApiClient:
    """
    Client class responsible for direct HTTP communication with the external
    GST Suvidha Provider (GSP) API.

    This class encapsulates all details of the HTTP communication, including
    endpoint construction, authentication, timeout handling, and error parsing.
    It uses the AwsSecretsManager to securely fetch API credentials at runtime.
    """

    def __init__(self, env: models.api.Environment):
        """
        Initializes the API client.

        :param env: The Odoo environment object, used for accessing configuration.
        """
        self.env = env
        self.secrets_manager = AwsSecretsManager()

    def send_invoice_data(self, payload: dict) -> dict:
        """
        Sends the e-invoice payload to the GSP API and returns the response.

        :param payload: A JSON-serializable dictionary conforming to the GSP API schema.
        :return: A dictionary parsed from the GSP's JSON response.
        :raises GspApiConnectionError: If a network connection error occurs.
        :raises GspApiTimeoutError: If the request times out.
        :raises GspApiDataError: If the GSP returns a 4xx client error.
        :raises GspApiServerError: If the GSP returns a 5xx server error.
        :raises GspApiClientError: For other unexpected request errors.
        :raises UserError: If essential configuration is missing.
        """
        config_param = self.env['ir.config_parameter'].sudo()
        api_url = config_param.get_param('tms_gsp.api_url')
        timeout_str = config_param.get_param('tms_gsp.timeout_seconds', '15')
        secret_name = config_param.get_param('tms_gsp.aws_secret_name')
        aws_region = config_param.get_param('tms_gsp.aws_region', 'ap-south-1')

        if not all([api_url, secret_name, aws_region]):
            _logger.error("GSP integration is not fully configured. Check system parameters.")
            raise UserError("GSP integration is not configured. Please contact the administrator.")

        try:
            timeout = int(timeout_str)
        except (ValueError, TypeError):
            _logger.warning("Invalid GSP timeout value '%s', defaulting to 15 seconds.", timeout_str)
            timeout = 15

        try:
            _logger.info("Fetching GSP API key from AWS Secrets Manager.")
            api_key = self.secrets_manager.get_secret(secret_name, aws_region)
        except Exception as e:
            _logger.critical("Failed to retrieve GSP API key from AWS Secrets Manager: %s", e)
            raise UserError(f"Could not retrieve API credentials. Error: {e}")

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        try:
            _logger.info("Sending e-invoice data to GSP endpoint: %s", api_url)
            response = requests.post(
                api_url,
                data=json.dumps(payload),
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
            _logger.info("Received successful response from GSP API. Status: %s", response.status_code)
            return response.json()

        except requests.exceptions.Timeout as e:
            _logger.warning("Request to GSP API timed out after %s seconds.", timeout)
            raise GspApiTimeoutError(f"Request timed out: {e}") from e

        except requests.exceptions.ConnectionError as e:
            _logger.error("GSP API connection error: %s", e)
            raise GspApiConnectionError(f"Connection error: {e}") from e

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_content = e.response.text
            _logger.error(
                "GSP API returned an HTTP error. Status: %s, Response: %s",
                status_code, error_content
            )
            if 400 <= status_code < 500:
                raise GspApiDataError(f"Client Error {status_code}: {error_content}") from e
            if 500 <= status_code < 600:
                raise GspApiServerError(f"Server Error {status_code}: {error_content}") from e
            raise GspApiClientError(f"Unhandled HTTP Error {status_code}: {error_content}") from e

        except requests.exceptions.RequestException as e:
            _logger.error("An unexpected error occurred during the GSP API request: %s", e)
            raise GspApiClientError(f"An unexpected request error occurred: {e}") from e

        except json.JSONDecodeError as e:
            _logger.error("Failed to decode JSON response from GSP API: %s", e)
            raise GspApiClientError(f"Invalid JSON response from server: {e}") from e
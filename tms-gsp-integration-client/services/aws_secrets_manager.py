# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import time
from typing import Dict, Any

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    boto3 = None
    ClientError = None
    NoCredentialsError = None

_logger = logging.getLogger(__name__)


class SecretManagerError(Exception):
    """Base exception for AWS Secrets Manager related errors."""
    pass


class SecretNotFoundError(SecretManagerError):
    """Exception raised when a secret is not found in AWS Secrets Manager."""
    pass


class SecretAccessDeniedError(SecretManagerError):
    """Exception raised when access to a secret is denied."""
    pass


class AwsSecretsManager:
    """
    A reusable service to fetch, cache, and manage secrets from AWS Secrets Manager.

    This class provides a simple interface to retrieve secrets while handling
    caching, error management, and the complexities of the boto3 SDK. It is
    designed to be a self-contained infrastructure component.
    """
    _cache: Dict[str, Dict[str, Any]] = {}

    def __init__(self, cache_ttl_seconds: int = 300):
        """
        Initializes the AWS Secrets Manager service.

        Args:
            cache_ttl_seconds (int): The Time-To-Live for cached secrets in seconds.
                                     Defaults to 300 (5 minutes).
        """
        if boto3 is None:
            _logger.error("The 'boto3' library is required to use AwsSecretsManager. Please install it.")
            raise ImportError("boto3 is not installed.")

        self.cache_ttl_seconds = cache_ttl_seconds
        self._clients: Dict[str, Any] = {}

    def _get_client(self, region_name: str) -> Any:
        """
        Gets a boto3 secretsmanager client for a specific region, caching the client instance.
        """
        if region_name not in self._clients:
            try:
                self._clients[region_name] = boto3.client(
                    service_name='secretsmanager',
                    region_name=region_name
                )
            except NoCredentialsError as e:
                _logger.error(
                    "AWS credentials not found. Ensure the Odoo instance has a "
                    "properly configured IAM role or environment variables."
                )
                raise SecretAccessDeniedError("AWS credentials are not configured.") from e
            except Exception as e:
                _logger.error("Failed to create boto3 client for region %s: %s", region_name, e)
                raise SecretManagerError(f"Could not initialize AWS client for region {region_name}") from e
        return self._clients[region_name]

    def get_secret(self, secret_name: str, region_name: str) -> str:
        """
        Retrieves a secret from AWS Secrets Manager, utilizing an in-memory cache.

        First, it checks for a valid, non-expired cached version of the secret.
        If not found or expired, it fetches the secret from AWS, caches it,
        and then returns it.

        Args:
            secret_name (str): The name or ARN of the secret to retrieve.
            region_name (str): The AWS region where the secret is stored.

        Returns:
            str: The value of the secret as a string.

        Raises:
            SecretNotFoundError: If the secret does not exist.
            SecretAccessDeniedError: If permissions are insufficient to access the secret.
            SecretManagerError: For other AWS-related errors.
        """
        if not secret_name or not region_name:
            raise ValueError("secret_name and region_name must be provided.")

        cache_key = f"{region_name}:{secret_name}"
        current_time = time.time()

        if cache_key in self._cache:
            cached_item = self._cache[cache_key]
            if (current_time - cached_item['timestamp']) < self.cache_ttl_seconds:
                _logger.info("Cache hit for secret '%s' in region '%s'.", secret_name, region_name)
                return cached_item['value']
            else:
                _logger.info("Cache expired for secret '%s' in region '%s'.", secret_name, region_name)

        _logger.info("Cache miss for secret '%s'. Fetching from AWS Secrets Manager.", secret_name)
        secret_value = self._fetch_from_aws(secret_name, region_name)

        self._cache[cache_key] = {
            'value': secret_value,
            'timestamp': current_time,
        }

        return secret_value

    def _fetch_from_aws(self, secret_name: str, region_name: str) -> str:
        """
        Performs the actual API call to AWS Secrets Manager to retrieve a secret.

        Args:
            secret_name (str): The name or ARN of the secret.
            region_name (str): The AWS region.

        Returns:
            str: The secret value.

        Raises:
            SecretNotFoundError: If the secret does not exist.
            SecretAccessDeniedError: If permissions are insufficient.
            SecretManagerError: For other AWS errors.
        """
        client = self._get_client(region_name)
        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            error_code = e.response.get("Error", {}).get("Code")
            _logger.error(
                "Failed to fetch secret '%s' from AWS. Error code: %s",
                secret_name,
                error_code,
                exc_info=True
            )
            if error_code == 'ResourceNotFoundException':
                raise SecretNotFoundError(f"Secret '{secret_name}' not found in region '{region_name}'.") from e
            elif error_code == 'AccessDeniedException':
                raise SecretAccessDeniedError(
                    f"Access denied when trying to fetch secret '{secret_name}'. "
                    "Check IAM permissions for the Odoo instance."
                ) from e
            else:
                raise SecretManagerError(f"An AWS error occurred while fetching secret '{secret_name}'.") from e
        except NoCredentialsError as e:
             _logger.error(
                "AWS credentials not found while fetching secret '%s'. "
                "Ensure the environment is configured correctly.", secret_name
             )
             raise SecretAccessDeniedError("AWS credentials are not configured.") from e
        except Exception as e:
            _logger.error("An unexpected error occurred while fetching secret '%s'.", secret_name, exc_info=True)
            raise SecretManagerError("An unexpected error occurred.") from e

        # Secrets can be stored as a string or binary. We primarily expect strings.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            # Some secrets might be JSON strings themselves, so we return the raw string
            # and let the consumer parse it if needed.
            return secret
        else:
            # Handle binary secrets if necessary, though less common for API keys.
            # For now, we'll treat this as an unsupported format.
            _logger.warning("Secret '%s' is a binary secret, which is not directly supported as a string.", secret_name)
            raise SecretManagerError(f"Secret '{secret_name}' is in a binary format and cannot be returned as a string.")
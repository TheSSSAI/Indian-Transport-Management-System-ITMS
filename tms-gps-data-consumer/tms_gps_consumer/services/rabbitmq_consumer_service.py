# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import json
from datetime import datetime
import pika
import pika.exceptions
import boto3
from botocore.exceptions import ClientError

from odoo.exceptions import UserError

from .vehicle_location_updater import VehicleLocationUpdater

_logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception for message payload validation errors."""
    pass


class RabbitMQConsumerService:
    """
    A service to connect to RabbitMQ, consume vehicle location messages,
    and orchestrate their processing and persistence in Odoo.

    This service encapsulates all AMQP-related logic, including connection
    management, message fetching, payload validation, and message lifecycle
    (ACK/NACK for DLQ routing), adhering to REQ-1-301 and REQ-1-501.
    """

    def __init__(self, env):
        """
        Initializes the service.

        :param env: The Odoo Environment object, used for accessing system
                    parameters and instantiating other services.
        """
        if not env:
            raise ValueError("Odoo environment (env) is required.")
        self.env = env
        self.vehicle_updater = VehicleLocationUpdater(env)
        self._cached_credentials = None

    def _get_config(self):
        """
        Retrieves all necessary configuration from Odoo's system parameters.

        :return: A dictionary of configuration values.
        :raises: UserError if a required parameter is missing.
        """
        get_param = self.env['ir.config_parameter'].sudo().get_param
        config = {
            'host': get_param('tms_gps_consumer.rabbitmq.host', 'rabbitmq'),
            'port': int(get_param('tms_gps_consumer.rabbitmq.port', '5672')),
            'vhost': get_param('tms_gps_consumer.rabbitmq.vhost', '/'),
            'queue': get_param('tms_gps_consumer.rabbitmq.queue', 'q.tms.location_updates'),
            'secret_name': get_param('tms_gps_consumer.aws.secretsmanager.secret_name'),
            'aws_region': get_param('tms_gps_consumer.aws.region'),
            'batch_size': int(get_param('tms_gps_consumer.consumer.batch_size', '100')),
        }
        if not all([config['secret_name'], config['aws_region']]):
            raise UserError("AWS Secrets Manager configuration (secret name and region) is missing in system parameters.")
        return config

    def _get_credentials(self, secret_name, region):
        """
        Fetches RabbitMQ credentials securely from AWS Secrets Manager.
        Caches credentials for the lifetime of the service instance to reduce API calls.

        :param secret_name: The name of the secret in AWS Secrets Manager.
        :param region: The AWS region where the secret is stored.
        :return: A dictionary containing 'username' and 'password'.
        :raises: UserError on failure to retrieve credentials.
        """
        if self._cached_credentials:
            return self._cached_credentials

        _logger.info("Fetching RabbitMQ credentials from AWS Secrets Manager.")
        try:
            session = boto3.session.Session()
            client = session.client(service_name='secretsmanager', region_name=region)
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)
            secret = json.loads(get_secret_value_response['SecretString'])
            
            if 'username' not in secret or 'password' not in secret:
                raise KeyError("Secret must contain 'username' and 'password' keys.")

            self._cached_credentials = secret
            return self._cached_credentials
        except ClientError as e:
            _logger.error("Failed to retrieve credentials from AWS Secrets Manager: %s", e)
            raise UserError(f"AWS Secrets Manager error: Could not retrieve secret '{secret_name}'. Check permissions and configuration. Error: {e}")
        except (json.JSONDecodeError, KeyError) as e:
            _logger.error("Failed to parse credentials from AWS secret: %s", e)
            raise UserError(f"Invalid secret format for '{secret_name}'. Ensure it is a valid JSON with 'username' and 'password'. Error: {e}")

    def _get_connection(self, config, credentials):
        """Establishes and returns a connection to the RabbitMQ broker."""
        creds = pika.PlainCredentials(credentials['username'], credentials['password'])
        params = pika.ConnectionParameters(
            host=config['host'],
            port=config['port'],
            virtual_host=config['vhost'],
            credentials=creds,
            heartbeat=600,
            blocked_connection_timeout=300
        )
        return pika.BlockingConnection(params)

    def consume_batch(self):
        """
        Main entry point for the consumer. Connects to RabbitMQ and processes
        a batch of messages from the configured queue.
        """
        _logger.info("Starting GPS data consumption batch.")
        try:
            config = self._get_config()
            credentials = self._get_credentials(config['secret_name'], config['aws_region'])
        except UserError as e:
            _logger.error("Configuration or credential error: %s", e)
            return

        connection = None
        processed_count = 0
        try:
            connection = self._get_connection(config, credentials)
            channel = connection.channel()
            # Ensure queue exists without creating it if it doesn't.
            # The producer/infra setup is responsible for queue creation.
            channel.queue_declare(queue=config['queue'], durable=True, passive=True)

            for _ in range(config['batch_size']):
                method_frame, properties, body = channel.basic_get(queue=config['queue'], auto_ack=False)
                if method_frame is None:
                    _logger.info("No more messages in queue. Ending batch.")
                    break
                
                self._process_message(channel, method_frame, properties, body)
                processed_count += 1

        except pika.exceptions.AMQPConnectionError as e:
            _logger.error("RabbitMQ connection failed: %s", e)
        except pika.exceptions.ChannelClosedByBroker as e:
            _logger.error("RabbitMQ channel closed by broker (check queue existence/permissions): %s", e)
        except Exception as e:
            _logger.error("An unexpected error occurred during message consumption: %s", e, exc_info=True)
        finally:
            if connection and not connection.is_closed:
                connection.close()
                _logger.info("RabbitMQ connection closed.")
        
        _logger.info("Finished GPS data consumption batch. Processed %d messages.", processed_count)

    def _process_message(self, channel, method_frame, properties, body):
        """
        Processes a single message: validation, persistence, and acknowledgement.
        Implements DLQ routing for poison-pill messages via NACK.
        """
        delivery_tag = method_frame.delivery_tag
        try:
            payload_str = body.decode('utf-8')
            payload = json.loads(payload_str)

            # --- Payload Validation (as per REQ-1-301) ---
            required_keys = ['vehicle_identifier', 'latitude', 'longitude', 'timestamp']
            if not all(key in payload for key in required_keys):
                raise ValidationError(f"Message missing required keys. Required: {required_keys}")

            if not isinstance(payload['vehicle_identifier'], str) or not payload['vehicle_identifier']:
                raise ValidationError("'vehicle_identifier' must be a non-empty string.")
            if not isinstance(payload['latitude'], (int, float)):
                raise ValidationError("'latitude' must be a number.")
            if not isinstance(payload['longitude'], (int, float)):
                raise ValidationError("'longitude' must be a number.")
            
            # Validate timestamp format
            try:
                datetime.fromisoformat(payload['timestamp'].replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                raise ValidationError("'timestamp' must be a valid ISO 8601 string.")
            
            # --- Delegate to Updater Service ---
            self.vehicle_updater.update_location(payload)

            # --- Acknowledge Success ---
            channel.basic_ack(delivery_tag)
            _logger.debug("Successfully processed and ACKed message for vehicle %s", payload.get('vehicle_identifier'))

        except (json.JSONDecodeError, ValidationError) as e:
            _logger.warning(
                "Malformed message payload. Rejecting and sending to DLQ. Error: %s. Body: %s",
                e, body
            )
            channel.basic_nack(delivery_tag, requeue=False)
        except Exception as e:
            _logger.error(
                "Unexpected error processing message. Rejecting and sending to DLQ. Error: %s. Body: %s",
                e, body, exc_info=True
            )
            # NACK to DLQ to prevent retry loops on persistent errors.
            channel.basic_nack(delivery_tag, requeue=False)
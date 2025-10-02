# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch, call

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger

_logger = logging.getLogger(__name__)

# Mock pika classes and exceptions for tests without a running RabbitMQ server
try:
    import pika
    from pika.exceptions import AMQPConnectionError
except ImportError:
    pika = MagicMock()
    AMQPConnectionError = ConnectionError


class TestGpsConsumer(TransactionCase):
    """
    Test suite for the TMS GPS Consumer cron job.
    These are integration tests that verify the interaction between the Odoo
    cron trigger, the consumer service, and the vehicle location updater service.
    External dependencies (RabbitMQ, AWS Secrets Manager) are mocked.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create test vehicles. Assumes 'tms_management' addon is a dependency
        # and has added the necessary location fields to 'tms.vehicle'.
        cls.Vehicle = cls.env["tms.vehicle"]
        cls.vehicle_1 = cls.Vehicle.create(
            {
                "name": "Test Truck 01",
                "truck_number": "KA-01-AB-1234",
                "latitude": 12.9716,
                "longitude": 77.5946,
                "last_gps_update": datetime(2023, 1, 1, 10, 0, 0),
            }
        )
        cls.vehicle_2 = cls.Vehicle.create(
            {
                "name": "Test Truck 02",
                "truck_number": "MH-12-CD-5678",
            }
        )
        cls.consumer_cron = cls.env["tms.gps.consumer.cron"].create({})

    def _create_mock_message(self, delivery_tag, payload):
        """Helper to create a mock RabbitMQ message tuple."""
        method_frame = MagicMock(spec=pika.spec.Basic.GetOk)
        method_frame.delivery_tag = delivery_tag
        body = json.dumps(payload).encode("utf-8")
        return (method_frame, None, body)

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_successful_consumption_and_location_update(self, mock_pika, mock_boto3):
        """
        Verify that a valid message is consumed, processed, ACK'd, and the
        vehicle's location is updated in the database.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_connection = MagicMock()
        mock_connection.channel.return_value = mock_channel
        mock_pika.BlockingConnection.return_value = mock_connection

        now = datetime.utcnow()
        payload = {
            "vehicle_identifier": "KA-01-AB-1234",
            "latitude": 13.0000,
            "longitude": 77.6000,
            "timestamp": now.isoformat(),
        }
        mock_message = self._create_mock_message(1, payload)
        mock_channel.basic_get.side_effect = [mock_message, (None, None, None)]

        # Act
        self.consumer_cron._run_consumer()

        # Assert
        self.vehicle_1.invalidate_recordset()
        self.assertEqual(self.vehicle_1.latitude, 13.0000)
        self.assertEqual(self.vehicle_1.longitude, 77.6000)
        # Odoo's datetime fields lose microseconds, so we compare without them
        self.assertEqual(
            self.vehicle_1.last_gps_update.replace(microsecond=0),
            now.replace(microsecond=0),
        )
        mock_channel.basic_ack.assert_called_once_with(delivery_tag=1)
        mock_channel.basic_nack.assert_not_called()
        mock_connection.close.assert_called_once()

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_poison_pill_message_is_nacked_to_dlq(self, mock_pika, mock_boto3):
        """
        Verify that a message with malformed JSON (a poison pill) is
        negatively acknowledged (NACK'd) to be routed to the DLQ.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_connection = MagicMock()
        mock_connection.channel.return_value = mock_channel
        mock_pika.BlockingConnection.return_value = mock_connection

        method_frame = MagicMock()
        method_frame.delivery_tag = 2
        # Malformed JSON
        body = b'{"vehicle_identifier": "KA-01-AB-1234", "latitude": 13.0000,'
        mock_channel.basic_get.side_effect = [(method_frame, None, body), (None, None, None)]

        initial_lat = self.vehicle_1.latitude
        initial_lon = self.vehicle_1.longitude

        # Act
        with mute_logger("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service"):
            self.consumer_cron._run_consumer()

        # Assert
        self.vehicle_1.invalidate_recordset()
        self.assertEqual(self.vehicle_1.latitude, initial_lat)
        self.assertEqual(self.vehicle_1.longitude, initial_lon)

        mock_channel.basic_ack.assert_not_called()
        mock_channel.basic_nack.assert_called_once_with(delivery_tag=2, requeue=False)
        mock_connection.close.assert_called_once()
        
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_message_with_invalid_payload_schema_is_nacked(self, mock_pika, mock_boto3):
        """
        Verify that a message with a valid JSON but missing required fields
        is NACK'd to the DLQ.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_pika.BlockingConnection.return_value.channel.return_value = mock_channel
        
        # Payload missing 'latitude'
        payload = {
            "vehicle_identifier": "KA-01-AB-1234",
            "longitude": 77.6000,
            "timestamp": datetime.utcnow().isoformat(),
        }
        mock_message = self._create_mock_message(3, payload)
        mock_channel.basic_get.side_effect = [mock_message, (None, None, None)]
        
        initial_lat = self.vehicle_1.latitude
        
        # Act
        with mute_logger("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service"):
            self.consumer_cron._run_consumer()
            
        # Assert
        self.vehicle_1.invalidate_recordset()
        self.assertEqual(self.vehicle_1.latitude, initial_lat)
        mock_channel.basic_ack.assert_not_called()
        mock_channel.basic_nack.assert_called_once_with(delivery_tag=3, requeue=False)

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_idempotency_check_prevents_update_from_old_message(self, mock_pika, mock_boto3):
        """
        Verify that if a message has a timestamp older than the last update on
        the vehicle, the message is ACK'd but no DB update occurs.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_pika.BlockingConnection.return_value.channel.return_value = mock_channel
        
        # This timestamp is older than the one set in setUpClass
        old_timestamp = datetime(2023, 1, 1, 9, 59, 59)
        payload = {
            "vehicle_identifier": "KA-01-AB-1234",
            "latitude": 99.9999,
            "longitude": 99.9999,
            "timestamp": old_timestamp.isoformat(),
        }
        mock_message = self._create_mock_message(4, payload)
        mock_channel.basic_get.side_effect = [mock_message, (None, None, None)]
        
        initial_lat = self.vehicle_1.latitude
        
        # Act
        self.consumer_cron._run_consumer()
        
        # Assert
        self.vehicle_1.invalidate_recordset()
        self.assertEqual(self.vehicle_1.latitude, initial_lat)
        mock_channel.basic_ack.assert_called_once_with(delivery_tag=4)
        mock_channel.basic_nack.assert_not_called()

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_vehicle_not_found_is_acked_and_logged(self, mock_pika, mock_boto3):
        """
        Verify that a message for a non-existent vehicle is safely handled by
        ACK'ing the message and logging a warning, without causing an error.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_pika.BlockingConnection.return_value.channel.return_value = mock_channel
        
        payload = {
            "vehicle_identifier": "XX-99-ZZ-9999",  # This vehicle does not exist
            "latitude": 15.0,
            "longitude": 75.0,
            "timestamp": datetime.utcnow().isoformat(),
        }
        mock_message = self._create_mock_message(5, payload)
        mock_channel.basic_get.side_effect = [mock_message, (None, None, None)]
        
        # Act
        with self.assertLogs(
            "odoo.addons.tms_gps_consumer.services.vehicle_location_updater",
            level="WARNING"
        ) as cm:
            self.consumer_cron._run_consumer()
            self.assertIn("Vehicle with identifier 'XX-99-ZZ-9999' not found.", cm.output[0])
            
        # Assert
        mock_channel.basic_ack.assert_called_once_with(delivery_tag=5)
        mock_channel.basic_nack.assert_not_called()

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.boto3")
    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.pika")
    def test_batch_processing_handles_mixed_messages(self, mock_pika, mock_boto3):
        """
        Verify that the consumer can process a batch of messages, correctly
        handling valid, invalid, and poison-pill messages in a single run.
        """
        # Arrange
        mock_channel = MagicMock()
        mock_pika.BlockingConnection.return_value.channel.return_value = mock_channel
        
        now = datetime.utcnow()
        # Message 1: Valid for vehicle 1
        valid_payload_1 = {
            "vehicle_identifier": "KA-01-AB-1234",
            "latitude": 14.0, "longitude": 78.0, "timestamp": now.isoformat()
        }
        msg1 = self._create_mock_message(10, valid_payload_1)
        
        # Message 2: Poison pill (malformed JSON)
        msg2_method = MagicMock(); msg2_method.delivery_tag = 11
        msg2 = (msg2_method, None, b'{"invalid_json":,}')
        
        # Message 3: Valid for vehicle 2
        valid_payload_2 = {
            "vehicle_identifier": "MH-12-CD-5678",
            "latitude": 18.0, "longitude": 74.0, "timestamp": now.isoformat()
        }
        msg3 = self._create_mock_message(12, valid_payload_2)
        
        # Message 4: Invalid schema (missing data)
        invalid_payload = {"vehicle_identifier": "KA-01-AB-1234"}
        msg4 = self._create_mock_message(13, invalid_payload)
        
        mock_channel.basic_get.side_effect = [msg1, msg2, msg3, msg4, (None, None, None)]
        
        # Act
        with mute_logger("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service"):
            self.consumer_cron._run_consumer()
            
        # Assert
        # Check vehicle 1 was updated
        self.vehicle_1.invalidate_recordset()
        self.assertEqual(self.vehicle_1.latitude, 14.0)
        self.assertEqual(self.vehicle_1.longitude, 78.0)
        
        # Check vehicle 2 was updated
        self.vehicle_2.invalidate_recordset()
        self.assertEqual(self.vehicle_2.latitude, 18.0)
        self.assertEqual(self.vehicle_2.longitude, 74.0)
        
        # Check ACK calls for valid messages
        self.assertIn(call(delivery_tag=10), mock_channel.basic_ack.call_args_list)
        self.assertIn(call(delivery_tag=12), mock_channel.basic_ack.call_args_list)
        self.assertEqual(mock_channel.basic_ack.call_count, 2)
        
        # Check NACK calls for invalid messages
        self.assertIn(call(delivery_tag=11, requeue=False), mock_channel.basic_nack.call_args_list)
        self.assertIn(call(delivery_tag=13, requeue=False), mock_channel.basic_nack.call_args_list)
        self.assertEqual(mock_channel.basic_nack.call_count, 2)

    @patch("odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service.RabbitMQConsumerService")
    def test_cron_job_handles_service_connection_error(self, MockConsumerService):
        """
        Verify that the top-level cron job method catches exceptions from the
        service layer (e.g., connection failure) and logs them without crashing.
        """
        # Arrange
        MockConsumerService.side_effect = AMQPConnectionError("Connection refused")

        # Act & Assert
        with self.assertLogs('odoo.addons.tms_gps_consumer.models.consumer_cron', level='ERROR') as cm:
            self.consumer_cron._run_consumer()
            self.assertIn("Failed to run GPS consumer due to connection error: Connection refused", cm.output[0])

        # Verify that the exception did not propagate and crash the cron runner
        # (This is implicitly tested by the test completing without an unhandled exception)
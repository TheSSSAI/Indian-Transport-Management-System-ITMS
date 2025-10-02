# -*- coding: utf-8 -*-
# Copyright (C) 2024 - All Rights Reserved
#
# This software is proprietary and confidential. Unauthorized copying of
# this file, via any medium is strictly prohibited.
#
# Written by the Master Software Architect <architect@tms.com>, 2024

import logging
from datetime import datetime
from typing import Dict, Any

from odoo import api
from odoo.tools import misc

_logger = logging.getLogger(__name__)


class VehicleLocationUpdater:
    """
    Service class responsible for updating vehicle location data in the Odoo database.

    This class encapsulates the specific business logic for finding a vehicle,
    performing an idempotency check to prevent processing stale or duplicate data,
    and writing the new location information to the `tms.vehicle` model.
    It is designed to be called by a consumer service (like RabbitMQConsumerService)
    after the initial message payload has been deserialized and structurally validated.
    """

    def __init__(self, env: api.Environment):
        """
        Initializes the VehicleLocationUpdater service.

        Args:
            env: The Odoo Environment object, providing access to the ORM.
        """
        if not env:
            raise ValueError("Odoo Environment must be provided.")
        self.env = env

    def update_location(self, payload: Dict[str, Any]) -> None:
        """
        Processes a single validated location update payload and persists it to the database.

        This method implements the core logic for the GPS data consumer:
        1.  Searches for the vehicle using the provided identifier.
        2.  Performs an idempotency check by comparing the payload timestamp with the
            vehicle's last known update timestamp.
        3.  Updates the vehicle's `latitude`, `longitude`, and `last_gps_update` fields
            if the new data is more recent.

        This method is designed to let database exceptions bubble up to the calling
        service, which is responsible for handling message acknowledgements (e.g., NACKing
        a message to a DLQ) in case of persistence failures.

        Args:
            payload (Dict[str, Any]): A validated dictionary containing the location
                update data. Expected keys are 'vehicle_identifier', 'latitude',
                'longitude', and 'timestamp'.

        Raises:
            KeyError: If the payload is missing a required key.
            ValueError: If the timestamp format is invalid.
        """
        _logger.debug("Processing vehicle location update payload: %s", payload)

        try:
            vehicle_identifier = payload['vehicle_identifier']
            new_latitude = payload['latitude']
            new_longitude = payload['longitude']
            new_timestamp_str = payload['timestamp']
        except KeyError as e:
            _logger.error("Payload is missing required key: %s. Payload: %s", e, payload)
            # Let the exception bubble up to be caught by the consumer,
            # which will NACK the message.
            raise

        # Find the vehicle record.
        # This relies on 'truck_number' being an indexed field for performance.
        vehicle = self.env['tms.vehicle'].search([
            ('truck_number', '=', vehicle_identifier)
        ], limit=1)

        if not vehicle:
            _logger.warning(
                "Vehicle with identifier '%s' not found in the database. "
                "Skipping location update.",
                vehicle_identifier
            )
            return

        # Perform idempotency check.
        try:
            # Odoo's misc.str_to_datetime handles ISO 8601 format with timezone awareness.
            new_timestamp = misc.str_to_datetime(new_timestamp_str)
            if not new_timestamp:
                raise ValueError("Timestamp could not be parsed.")
        except (ValueError, TypeError) as e:
            _logger.error(
                "Invalid timestamp format '%s' for vehicle '%s'. Error: %s",
                new_timestamp_str, vehicle_identifier, e
            )
            # Raise ValueError to indicate a poison pill message.
            raise ValueError(f"Invalid timestamp format: {new_timestamp_str}") from e

        # The 'last_gps_update' field is expected to be on the 'tms.vehicle' model.
        # This check is critical to handle message redeliveries or out-of-order processing.
        if vehicle.last_gps_update and new_timestamp <= vehicle.last_gps_update:
            _logger.info(
                "Stale or duplicate location update for vehicle '%s'. "
                "Incoming: %s, Existing: %s. Skipping.",
                vehicle_identifier,
                new_timestamp,
                vehicle.last_gps_update
            )
            return

        # Prepare the data for the write operation.
        update_vals = {
            'latitude': new_latitude,
            'longitude': new_longitude,
            'last_gps_update': new_timestamp,
        }

        try:
            # Perform the ORM write operation.
            # This is a transactional operation within Odoo.
            vehicle.write(update_vals)
            _logger.info(
                "Successfully updated location for vehicle '%s' to (%f, %f) at %s.",
                vehicle_identifier,
                new_latitude,
                new_longitude,
                new_timestamp_str
            )
            # The calling service should commit the transaction if it's managing it.
            # In a standard Odoo cron, the transaction is committed automatically
            # upon successful completion of the method.
        except Exception as e:
            _logger.error(
                "Failed to write location update for vehicle '%s'. Error: %s",
                vehicle_identifier, e, exc_info=True
            )
            # Re-raise the exception to allow the consumer service to NACK the message,
            # ensuring the failed message is sent to the DLQ and the transaction is rolled back.
            raise
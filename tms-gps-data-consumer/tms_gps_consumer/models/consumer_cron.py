# -*- coding: utf-8 -*-
"""
This module defines the Odoo model that acts as the entry point for the
RabbitMQ GPS data consumer scheduled action.
"""

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)

# As this is an Odoo addon, we need to handle the case where the dependent
# service layer might not be importable during server startup or in certain
# test environments. We use a try-except block for robustness.
try:
    from odoo.addons.tms_gps_consumer.services.rabbitmq_consumer_service import (
        RabbitMQConsumerService,
    )
except ImportError:
    _logger.warning(
        "Could not import RabbitMQConsumerService. "
        "The tms_gps_consumer addon may not be fully functional."
    )
    RabbitMQConsumerService = None


class ConsumerCron(models.Model):
    """
    Odoo model to host the scheduled action method for consuming GPS data.

    This model is not intended to be persistent. It serves as a hook for the
    Odoo cron scheduler to trigger the application service layer responsible
    for handling the RabbitMQ message consumption.
    """

    _name = "tms.gps.consumer.cron"
    _description = "GPS Consumer Cron Trigger"
    _transient = True  # This model does not need to be stored in the database.

    @api.model
    def _run_consumer(self):
        """
        Scheduled method to run the RabbitMQ GPS data consumer.

        This method is the target of the 'ir.cron' record. It instantiates the
        RabbitMQConsumerService and initiates the batch consumption process.
        It includes a top-level exception handler to ensure that any failure
        during the consumption process (e.g., connection errors, processing
        errors) is logged without causing the Odoo cron job itself to fail
        and be disabled by the scheduler.
        """
        if not RabbitMQConsumerService:
            _logger.error(
                "RabbitMQConsumerService is not available. "
                "Cannot run GPS consumer cron."
            )
            return

        _logger.info("Starting GPS consumer cron job...")
        try:
            # Instantiate the service layer, passing the Odoo environment.
            # The environment (self.env) provides access to the ORM and system parameters.
            consumer_service = RabbitMQConsumerService(self.env)

            # Delegate the entire consumption logic to the service layer.
            # This keeps the Odoo model thin and focused on its role as a trigger.
            consumer_service.consume_batch()

        except Exception:
            # This is a critical top-level exception handler.
            # REQ-1-301 and its resilience requirements imply that the cron job
            # should be robust and not be disabled by Odoo on repeated failures.
            # Logging with `exception` includes the full traceback for debugging.
            _logger.exception(
                "An unexpected error occurred during the GPS consumer cron job execution. "
                "The job will continue on its next scheduled run."
            )
        finally:
            _logger.info("Finished GPS consumer cron job.")
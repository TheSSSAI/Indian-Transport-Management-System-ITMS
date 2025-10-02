# -*- coding: utf-8 -*-
{
    "name": "TMS :: GPS Data Consumer",
    "summary": """
        Consumes vehicle location data from a message queue and updates vehicle records.
    """,
    "description": """
        This Odoo addon is responsible for consuming 'VehicleLocationUpdated' events from
        a RabbitMQ message queue. It implements the AMQP consumer logic as an Odoo
        scheduled action.

        Key Features:
        - Implements a scheduled action (ir.cron) to poll RabbitMQ.
        - Fetches messages in batches for performance.
        - Validates incoming message payloads.
        - Updates corresponding vehicle records with new location data.
        - Handles message acknowledgements (ACK/NACK) for reliable processing.
        - Routes persistently un-processable messages to a Dead-Letter Queue (DLQ).
        - Securely fetches connection credentials from external configuration.

        This module acts as the bridge between the asynchronous, high-volume GPS data
        stream and the transactional Odoo monolith, ensuring real-time tracking
        capabilities without compromising the core application's performance.
    """,
    "author": "Enterprise Software Architects",
    "website": "https://www.yourcompany.com",
    "category": "Technical",
    "version": "18.0.1.0.0",
    "license": "OEEL-1",
    # Odoo Dependencies
    "depends": [
        "base",
        "tms_core_business_logic",  # Depends on the core TMS addon for the tms.vehicle model
    ],
    # Data files which are always installed
    "data": [
        "data/ir_cron_data.xml",
    ],
    # External Python dependencies
    "external_dependencies": {
        "python": [
            "pika",
            "boto3", # For AWS Secrets Manager integration
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
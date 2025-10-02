sequenceDiagram
    participant "Odoo GPS Consumer" as OdooGPSConsumer
    participant "RabbitMQ Broker" as RabbitMQBroker
    participant "Prometheus" as Prometheus
    participant "Alertmanager" as Alertmanager
    participant "SRE On-Call Platform" as SREOnCallPlatform

    activate OdooGPSConsumer
    RabbitMQBroker->>OdooGPSConsumer: 1. 1. Deliver Malformed Message from 'q.tms.location_updates'
    OdooGPSConsumer->>OdooGPSConsumer: 2. 2. [Loop: Retry Logic (3 attempts)] Attempt to process message
    OdooGPSConsumer-->>OdooGPSConsumer: Raise ValidationError('Invalid latitude format')
    activate RabbitMQBroker
    OdooGPSConsumer->>RabbitMQBroker: 3. 3. Send Negative Acknowledgement (NACK)
    RabbitMQBroker->>RabbitMQBroker: 4. 4. Route message to Dead-Letter Queue (DLQ)
    RabbitMQBroker-->>RabbitMQBroker: Message moved to 'q.tms.location_updates.dlq'
    Prometheus->>RabbitMQBroker: 5. 5. Scrape RabbitMQ Exporter for metrics
    RabbitMQBroker-->>Prometheus: Return Metric Value: {queue='q.tms.location_updates.dlq', value=1}
    Prometheus->>Prometheus: 6. 6. Evaluate Alerting Rule: 'GpsDlqNotEmpty'
    Prometheus-->>Prometheus: Rule condition met, alert state changes to 'Firing'
    Prometheus->>Alertmanager: 7. 7. Fire Alert
    Alertmanager->>SREOnCallPlatform: 8. 8. Route Critical Notification

    note over OdooGPSConsumer: The requeue: false parameter in the NACK call is critical. If set to true, it would create an inf...
    note over Prometheus: The for: 1m clause in the alerting rule prevents flapping alerts if a message enters and is quick...

    deactivate RabbitMQBroker
    deactivate OdooGPSConsumer

sequenceDiagram
    participant "Scheduler (Timer)" as SchedulerTimer
    participant "External GPS Provider API" as ExternalGPSProviderAPI
    participant "GPS Ingestion Microservice" as GPSIngestionMicroservice
    participant "RabbitMQ Message Broker" as RabbitMQMessageBroker
    participant "Odoo Consumer" as OdooConsumer

    activate GPSIngestionMicroservice
    SchedulerTimer->>GPSIngestionMicroservice: 1. 1. Trigger Polling Job
    GPSIngestionMicroservice->>ExternalGPSProviderAPI: 2. 2. Poll for Vehicle Locations
    ExternalGPSProviderAPI-->>GPSIngestionMicroservice: 2.1. [Success] 200 OK with JSON Payload | [Failure] 4xx/5xx Error
    GPSIngestionMicroservice->>GPSIngestionMicroservice: 3. 3. Validate and Transform Payload
    GPSIngestionMicroservice->>RabbitMQMessageBroker: 4. 4. Publish 'VehicleLocationUpdated' Event
    activate RabbitMQMessageBroker
    OdooConsumer->>RabbitMQMessageBroker: 5. 5. Consume Batch of Location Events
    RabbitMQMessageBroker-->>OdooConsumer: 5.1. Batch of messages (up to configured limit)
    OdooConsumer->>OdooConsumer: 6. 6. Process Event Batch
    OdooConsumer->>OdooConsumer: 7. 7. Batch Update Vehicle Locations in DB
    OdooConsumer-->>OdooConsumer: 7.1. Transaction Commit/Rollback
    OdooConsumer->>RabbitMQMessageBroker: 8. 8. Acknowledge/Reject Messages

    note over OdooConsumer: Idempotency Check: The logic in step 6 is crucial to handle potential message redeliveries from R...
    note over RabbitMQMessageBroker: Dead-Letter Queue (DLQ): The 'q.tms.location_updates' queue is configured with a dead-letter-exch...

    deactivate RabbitMQMessageBroker
    deactivate GPSIngestionMicroservice

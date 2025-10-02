# 1 System Overview

## 1.1 Analysis Date

2025-06-13

## 1.2 Architecture Type

Hybrid (Modular Monolith with a Decoupled Microservice)

## 1.3 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- RabbitMQ (Amazon MQ)
- Docker
- Amazon EKS

## 1.4 Bounded Contexts

- Transport Management (Monolith)
- GPS Data Ingestion (Microservice)

# 2.0 Project Specific Events

- {'eventId': 'EVT-GPS-001', 'eventName': 'VehicleLocationUpdated', 'eventType': 'integration', 'category': 'Vehicle Tracking', 'description': "Published by the GPS Ingestion Microservice when a new location data point is received from the third-party provider. This event informs the core TMS application of a vehicle's current position.", 'triggerCondition': 'Successful polling and validation of new data from the third-party GPS API.', 'sourceContext': 'GPS Data Ingestion (Microservice)', 'targetContexts': ['Transport Management (Monolith)'], 'payload': {'schema': {'type': 'object', 'properties': {'vehicle_identifier': {'type': 'string', 'description': 'Unique identifier for the vehicle, e.g., truck number.'}, 'latitude': {'type': 'number', 'format': 'float'}, 'longitude': {'type': 'number', 'format': 'float'}, 'timestamp': {'type': 'string', 'format': 'date-time', 'description': 'ISO 8601 formatted timestamp of the location capture.'}, 'eventVersion': {'type': 'string', 'description': "Schema version, e.g., '1.0'."}, 'correlationId': {'type': 'string', 'format': 'uuid', 'description': 'Unique ID to trace the event through the system.'}}, 'required': ['vehicle_identifier', 'latitude', 'longitude', 'timestamp', 'eventVersion', 'correlationId']}, 'requiredFields': ['vehicle_identifier', 'latitude', 'longitude', 'timestamp'], 'optionalFields': []}, 'frequency': 'high', 'businessCriticality': 'important', 'dataSource': {'database': 'Third-Party GPS Provider', 'table': 'N/A (API Endpoint)', 'operation': 'read'}, 'routing': {'routingKey': 'location.update.v1', 'exchange': 'tms.gps.events', 'queue': 'q.tms.location_updates'}, 'consumers': [{'service': 'Odoo Monolith', 'handler': 'Scheduled Action consuming from RabbitMQ', 'processingType': 'async'}], 'dependencies': ['REQ-1-301', 'REQ-1-013'], 'errorHandling': {'retryStrategy': 'Consumer-side retry limit (e.g., 3 times) before moving to DLQ.', 'deadLetterQueue': 'q.tms.location_updates.dlq', 'timeoutMs': 10000}}

# 3.0 Event Types And Schema Design

## 3.1 Essential Event Types

- {'eventName': 'VehicleLocationUpdated', 'category': 'integration', 'description': 'The sole event required for inter-service communication between the GPS microservice and the Odoo monolith, as defined in REQ-1-301.', 'priority': 'high'}

## 3.2 Schema Design

| Property | Value |
|----------|-------|
| Format | JSON |
| Reasoning | JSON is lightweight, human-readable, and natively ... |
| Consistency Approach | A single, strictly defined schema for the 'Vehicle... |

## 3.3 Schema Evolution

| Property | Value |
|----------|-------|
| Backward Compatibility | ✅ |
| Forward Compatibility | ❌ |
| Strategy | Additive changes only (new optional fields). The O... |

## 3.4 Event Structure

### 3.4.1 Standard Fields

- eventVersion
- correlationId
- timestamp

### 3.4.2 Metadata Requirements

- The event payload itself contains all necessary metadata. RabbitMQ message headers will not be used for business-level metadata to keep the contract within the message body.

# 4.0.0 Event Routing And Processing

## 4.1.0 Routing Mechanisms

- {'type': 'RabbitMQ Topic Exchange', 'description': "A topic exchange named 'tms.gps.events' will be used. This provides flexibility for future consumers, though the initial implementation only has one queue.", 'useCase': "Routing 'VehicleLocationUpdated' events to the Odoo consumer queue based on a routing key like 'location.update.v1'."}

## 4.2.0 Processing Patterns

- {'pattern': 'sequential', 'applicableScenarios': ["The Odoo scheduled job will consume messages from the 'q.tms.location_updates' queue. While it may fetch a batch of messages, processing will be sequential to update the database records for vehicle locations."], 'implementation': 'An Odoo scheduled action (cron job) that runs at a high frequency (e.g., every minute) to poll the queue for new messages and process them.'}

## 4.3.0 Filtering And Subscription

### 4.3.1 Filtering Mechanism

Routing Key Matching

### 4.3.2 Subscription Model

A single, durable queue ('q.tms.location_updates') is bound to the topic exchange with a specific routing key to subscribe to location updates.

### 4.3.3 Routing Keys

- location.update.v1

## 4.4.0 Handler Isolation

| Property | Value |
|----------|-------|
| Required | ✅ |
| Approach | The Odoo consumer logic is isolated within its own... |
| Reasoning | This aligns with the architecture's goal of isolat... |

## 4.5.0 Delivery Guarantees

| Property | Value |
|----------|-------|
| Level | at-least-once |
| Justification | For GPS tracking, a small chance of processing a l... |
| Implementation | RabbitMQ message acknowledgements will be sent by ... |

# 5.0.0 Event Storage And Replay

## 5.1.0 Persistence Requirements

| Property | Value |
|----------|-------|
| Required | ❌ |
| Duration | N/A |
| Reasoning | Events are transient and do not need to be stored ... |

## 5.2.0 Event Sourcing

### 5.2.1 Necessary

❌ No

### 5.2.2 Justification

Event sourcing is not required. The system uses a state-oriented persistence model where the latest state is stored in the database. The 'VehicleLocation' table serves as a historical log of locations, but not as an event source.

### 5.2.3 Scope

*No items available*

## 5.3.0 Technology Options

*No items available*

## 5.4.0 Replay Capabilities

### 5.4.1 Required

❌ No

### 5.4.2 Scenarios

*No items available*

### 5.4.3 Implementation

Recovery is handled by the microservice continuing to poll the source GPS API, not by replaying old messages.

## 5.5.0 Retention Policy

| Property | Value |
|----------|-------|
| Strategy | No Retention in Broker |
| Duration | N/A |
| Archiving Approach | Events are discarded from the queue upon successfu... |

# 6.0.0 Dead Letter Queue And Error Handling

## 6.1.0 Dead Letter Strategy

| Property | Value |
|----------|-------|
| Approach | A dedicated Dead Letter Queue (DLQ) named 'q.tms.l... |
| Queue Configuration | The DLQ will have a long message TTL (e.g., 14 day... |
| Processing Logic | Messages in the DLQ will trigger a high-severity a... |

## 6.2.0 Retry Policies

### 6.2.1 Error Type

#### 6.2.1.1 Error Type

Message Processing Failure (Odoo Consumer)

#### 6.2.1.2 Max Retries

3

#### 6.2.1.3 Backoff Strategy

fixed

#### 6.2.1.4 Delay Configuration

A short delay (e.g., 5 seconds) between retries within the consumer logic. If all retries fail, the message is NACK'd (negative acknowledgement) and sent to the DLQ.

### 6.2.2.0 Error Type

#### 6.2.2.1 Error Type

API Polling Failure (GPS Microservice)

#### 6.2.2.2 Max Retries

5

#### 6.2.2.3 Backoff Strategy

exponential

#### 6.2.2.4 Delay Configuration

As specified in REQ-1-301, the microservice will use exponential backoff when polling the external GPS API.

## 6.3.0.0 Poison Message Handling

| Property | Value |
|----------|-------|
| Detection Mechanism | A message is considered poison after exceeding the... |
| Handling Strategy | The message is rejected without requeue, causing R... |
| Alerting Required | ✅ |

## 6.4.0.0 Error Notification

### 6.4.1.0 Channels

- Alertmanager
- Grafana Dashboard

### 6.4.2.0 Severity

critical

### 6.4.3.0 Recipients

- On-call DevOps/SRE Team

## 6.5.0.0 Recovery Procedures

- {'scenario': 'Poison message in DLQ due to malformed data.', 'procedure': '1. Alert triggers investigation. 2. Operator inspects message in DLQ. 3. If fixable, manually edit and redrive the message. 4. If not, discard the message and address the root cause in the producer microservice.', 'automationLevel': 'manual'}

# 7.0.0.0 Event Versioning Strategy

## 7.1.0.0 Schema Evolution Approach

| Property | Value |
|----------|-------|
| Strategy | Additive Changes with Version Identifier |
| Versioning Scheme | Semantic Versioning (e.g., 1.0, 1.1) is sufficient... |
| Migration Strategy | Consumers must be updated to support new versions ... |

## 7.2.0.0 Compatibility Requirements

| Property | Value |
|----------|-------|
| Backward Compatible | ✅ |
| Forward Compatible | ❌ |
| Reasoning | The consumer (Odoo) must be able to process older ... |

## 7.3.0.0 Version Identification

| Property | Value |
|----------|-------|
| Mechanism | Version number included in the event payload. |
| Location | payload |
| Format | string (e.g., 'eventVersion': '1.0') |

## 7.4.0.0 Consumer Upgrade Strategy

| Property | Value |
|----------|-------|
| Approach | Upgrade the consumer (Odoo module) first to handle... |
| Rollout Strategy | Standard deployment process for the Odoo addon. |
| Rollback Procedure | Roll back the producer microservice to the previou... |

## 7.5.0.0 Schema Registry

| Property | Value |
|----------|-------|
| Required | ❌ |
| Technology | N/A |
| Governance | The event schema is simple and singular. It will b... |

# 8.0.0.0 Event Monitoring And Observability

## 8.1.0.0 Monitoring Capabilities

### 8.1.1.0 Capability

#### 8.1.1.1 Capability

Queue Metrics Monitoring

#### 8.1.1.2 Justification

Essential for understanding the health and throughput of the event pipeline.

#### 8.1.1.3 Implementation

Prometheus scraping RabbitMQ exporter metrics (queue depth, message rates, consumer count).

### 8.1.2.0 Capability

#### 8.1.2.1 Capability

DLQ Monitoring

#### 8.1.2.2 Justification

Crucial for detecting persistent processing failures.

#### 8.1.2.3 Implementation

Alertmanager alert configured in Prometheus for any message count > 0 in the DLQ.

### 8.1.3.0 Capability

#### 8.1.3.1 Capability

End-to-End Latency Measurement

#### 8.1.3.2 Justification

Required to validate the performance SLO defined in REQ-1-501 (<10 seconds).

#### 8.1.3.3 Implementation

Calculated by comparing the event's capture timestamp with the processing timestamp in Odoo consumer logs, visualized in Grafana.

## 8.2.0.0 Tracing And Correlation

| Property | Value |
|----------|-------|
| Tracing Required | ✅ |
| Correlation Strategy | A unique 'correlationId' will be generated by the ... |
| Trace Id Propagation | The 'correlationId' will be logged at every stage ... |

## 8.3.0.0 Performance Metrics

### 8.3.1.0 Metric

#### 8.3.1.1 Metric

Message Queue Depth

#### 8.3.1.2 Threshold

> 1000 messages for 5 minutes

#### 8.3.1.3 Alerting

✅ Yes

### 8.3.2.0 Metric

#### 8.3.2.1 Metric

End-to-End Processing Latency (p95)

#### 8.3.2.2 Threshold

> 10 seconds

#### 8.3.2.3 Alerting

✅ Yes

### 8.3.3.0 Metric

#### 8.3.3.1 Metric

Messages in DLQ

#### 8.3.3.2 Threshold

> 0

#### 8.3.3.3 Alerting

✅ Yes

## 8.4.0.0 Event Flow Visualization

| Property | Value |
|----------|-------|
| Required | ❌ |
| Tooling | N/A |
| Scope | The event flow is simple (Producer -> Queue -> Con... |

## 8.5.0.0 Alerting Requirements

### 8.5.1.0 Condition

#### 8.5.1.1 Condition

Messages present in the Dead Letter Queue.

#### 8.5.1.2 Severity

critical

#### 8.5.1.3 Response Time

Immediate investigation required.

#### 8.5.1.4 Escalation Path

- On-call SRE

### 8.5.2.0 Condition

#### 8.5.2.1 Condition

Message queue depth exceeds threshold, indicating a slow or failed consumer.

#### 8.5.2.2 Severity

warning

#### 8.5.2.3 Response Time

Investigate within 1 hour.

#### 8.5.2.4 Escalation Path

- On-call SRE

# 9.0.0.0 Implementation Priority

## 9.1.0.0 Component

### 9.1.1.0 Component

RabbitMQ Setup (Exchange, Queues, DLQ)

### 9.1.2.0 Priority

🔴 high

### 9.1.3.0 Dependencies

*No items available*

### 9.1.4.0 Estimated Effort

Low

## 9.2.0.0 Component

### 9.2.1.0 Component

GPS Microservice Publisher Logic

### 9.2.2.0 Priority

🔴 high

### 9.2.3.0 Dependencies

- RabbitMQ Setup

### 9.2.4.0 Estimated Effort

Medium

## 9.3.0.0 Component

### 9.3.1.0 Component

Odoo Consumer (Scheduled Action)

### 9.3.2.0 Priority

🔴 high

### 9.3.3.0 Dependencies

- RabbitMQ Setup

### 9.3.4.0 Estimated Effort

Medium

## 9.4.0.0 Component

### 9.4.1.0 Component

Monitoring & Alerting Configuration

### 9.4.2.0 Priority

🔴 high

### 9.4.3.0 Dependencies

- RabbitMQ Setup
- Odoo Consumer

### 9.4.4.0 Estimated Effort

Medium

# 10.0.0.0 Risk Assessment

## 10.1.0.0 Risk

### 10.1.1.0 Risk

Third-party GPS API is unavailable or slow, causing data staleness.

### 10.1.2.0 Impact

medium

### 10.1.3.0 Probability

medium

### 10.1.4.0 Mitigation

The microservice implements an exponential backoff retry strategy (REQ-1-301). Monitoring on API error rates will provide visibility.

## 10.2.0.0 Risk

### 10.2.1.0 Risk

Odoo consumer fails or is too slow, causing a large backlog in the RabbitMQ queue.

### 10.2.2.0 Impact

high

### 10.2.3.0 Probability

low

### 10.2.4.0 Mitigation

Alerting on queue depth allows for rapid detection. The system is designed to be resilient to temporary consumer downtime.

## 10.3.0.0 Risk

### 10.3.1.0 Risk

Un-processable 'poison' messages fill the DLQ and cause loss of location data.

### 10.3.2.0 Impact

low

### 10.3.3.0 Probability

low

### 10.3.4.0 Mitigation

DLQ alerting ensures visibility. The low impact is due to the transient nature of single GPS data points.

# 11.0.0.0 Recommendations

## 11.1.0.0 Category

### 11.1.1.0 Category

🔹 Reliability

### 11.1.2.0 Recommendation

Implement idempotent logic in the Odoo consumer by checking the incoming event's timestamp against the last recorded timestamp for the vehicle to safely handle message redelivery.

### 11.1.3.0 Justification

This prevents duplicate data entries and ensures data integrity under an 'at-least-once' delivery guarantee.

### 11.1.4.0 Priority

🔴 high

## 11.2.0.0 Category

### 11.2.1.0 Category

🔹 Observability

### 11.2.2.0 Recommendation

Ensure the 'correlationId' is logged consistently in a structured (JSON) format across both the FastAPI microservice and the Odoo application logs.

### 11.2.3.0 Justification

This is critical for debugging and tracing the flow of a specific data point from ingestion to persistence, fulfilling the requirements of REQ-1-602.

### 11.2.4.0 Priority

🔴 high

## 11.3.0.0 Category

### 11.3.1.0 Category

🔹 Simplicity

### 11.3.2.0 Recommendation

Avoid implementing a schema registry for the initial release. The single, simple event schema does not justify the added complexity and operational overhead.

### 11.3.3.0 Justification

Adhering to the project's scope and prioritizing simplicity. The current versioning strategy (field in payload) is sufficient.

### 11.3.4.0 Priority

🔴 high


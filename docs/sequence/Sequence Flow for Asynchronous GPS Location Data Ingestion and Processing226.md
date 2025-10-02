# 1 Overview

## 1.1 Diagram Id

SEQ-EP-003

## 1.2 Name

Asynchronous GPS Location Data Ingestion and Processing

## 1.3 Description

Illustrates the complete event-driven flow for ingesting real-time vehicle location data. A decoupled microservice polls an external provider and publishes standardized events to a message queue. A consumer within the core Odoo application then processes these events asynchronously to update vehicle locations, ensuring high throughput and resilience.

## 1.4 Type

🔹 EventProcessing

## 1.5 Purpose

To provide near real-time vehicle tracking functionality without impacting the performance or stability of the core transactional TMS application.

## 1.6 Complexity

High

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

Hourly

## 1.9 Participants

- REPO-GPS-CON
- REPO-TMS-CORE

## 1.10 Key Interactions

- REPO-GPS-CON (FastAPI microservice) polls the external GPS Provider's REST API on a schedule.
- The microservice validates the received JSON payload against its predefined data contract.
- Upon successful validation, the microservice publishes a standardized 'VehicleLocationUpdated' event to a RabbitMQ topic.
- A REPO-TMS-CORE scheduled job (consumer) retrieves a batch of events from the subscribed message queue.
- The consumer logic in REPO-TMS-CORE parses the events and performs a batch update of the corresponding vehicle locations in the PostgreSQL database.

## 1.11 Triggers

- A scheduled polling timer fires within the GPS Ingestion Microservice.

## 1.12 Outcomes

- Vehicle location is updated in the database, meeting the end-to-end latency SLO of under 10 seconds.
- Users can view the updated vehicle location on the map UI with a data latency of no more than 60 seconds.

## 1.13 Business Rules

- REQ-INT-003: Location data ingested by the microservice must match the specified JSON contract.
- REQ-NFR-001: End-to-end latency for processing a GPS data point must be under 10 seconds.

## 1.14 Error Scenarios

- The external GPS API is unavailable; the microservice logs the error and retries with exponential backoff.
- Received GPS data is malformed; the microservice drops the message and logs a validation error.
- The Odoo consumer fails to process a message after several retries; the message is routed to a Dead-Letter Queue (DLQ) for manual investigation.

## 1.15 Integration Points

- External: Third-Party GPS Provider API
- Middleware: Amazon MQ for RabbitMQ

# 2.0 Details

## 2.1 Diagram Id

SEQ-EP-003-IMPL

## 2.2 Name

Technical Sequence: Asynchronous GPS Event Ingestion and Processing Pipeline

## 2.3 Description

Provides a complete, implementation-ready technical specification for the event-driven ingestion of real-time vehicle location data. The sequence details how a decoupled FastAPI microservice polls an external REST API, validates and transforms the data into a canonical event, and publishes it to a RabbitMQ message broker. It then specifies how a consumer within the Odoo application retrieves these events in batches, processes them idempotently, and updates the PostgreSQL database, all while adhering to strict performance and resilience requirements, including a Dead-Letter Queue (DLQ) for failed messages.

## 2.4 Participants

### 2.4.1 System Trigger

#### 2.4.1.1 Repository Id

Scheduler

#### 2.4.1.2 Display Name

Scheduler (Timer)

#### 2.4.1.3 Type

🔹 System Trigger

#### 2.4.1.4 Technology

Kubernetes CronJob / Internal Scheduler

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | «Trigger» |

### 2.4.2.0 External System

#### 2.4.2.1 Repository Id

External-GPS-Provider-API

#### 2.4.2.2 Display Name

External GPS Provider API

#### 2.4.2.3 Type

🔹 External System

#### 2.4.2.4 Technology

REST API (JSON)

#### 2.4.2.5 Order

3

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | boundary |
| Color | #777777 |
| Stereotype | «External» |

### 2.4.3.0 Microservice

#### 2.4.3.1 Repository Id

REPO-GPS-CON

#### 2.4.3.2 Display Name

GPS Ingestion Microservice

#### 2.4.3.3 Type

🔹 Microservice

#### 2.4.3.4 Technology

FastAPI, Python 3.11

#### 2.4.3.5 Order

2

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #1f77b4 |
| Stereotype | «Producer» |

### 2.4.4.0 Middleware

#### 2.4.4.1 Repository Id

RabbitMQ-Message-Broker

#### 2.4.4.2 Display Name

RabbitMQ Message Broker

#### 2.4.4.3 Type

🔹 Middleware

#### 2.4.4.4 Technology

Amazon MQ for RabbitMQ

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | queue |
| Color | #ff7f0e |
| Stereotype | «MessageBus» |

### 2.4.5.0 Monolith Module

#### 2.4.5.1 Repository Id

REPO-TMS-CORE

#### 2.4.5.2 Display Name

Odoo Consumer

#### 2.4.5.3 Type

🔹 Monolith Module

#### 2.4.5.4 Technology

Odoo 18, Python 3.11

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #2ca02c |
| Stereotype | «Consumer» |

## 2.5.0.0 Interactions

### 2.5.1.0 Scheduled Trigger

#### 2.5.1.1 Source Id

Scheduler

#### 2.5.1.2 Target Id

REPO-GPS-CON

#### 2.5.1.3 Message

1. Trigger Polling Job

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Scheduled Trigger

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Invocation |
| Method | execute_polling_cycle() |
| Parameters | None |
| Authentication | N/A (Internal) |
| Error Handling | Logs job execution errors. |
| Performance | Fires every 30-60 seconds, configurable via enviro... |

### 2.5.2.0 API Call

#### 2.5.2.1 Source Id

REPO-GPS-CON

#### 2.5.2.2 Target Id

External-GPS-Provider-API

#### 2.5.2.3 Message

2. Poll for Vehicle Locations

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 API Call

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

2.1. [Success] 200 OK with JSON Payload | [Failure] 4xx/5xx Error

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/1.1 |
| Method | GET /api/v2/locations |
| Parameters | query: { since: last_timestamp } |
| Authentication | HTTP Header 'Authorization: Bearer <API_TOKEN_FROM... |
| Error Handling | Implements retry with exponential backoff for 5xx ... |
| Performance | Request timeout set to 5 seconds. |

### 2.5.3.0 Internal Processing

#### 2.5.3.1 Source Id

REPO-GPS-CON

#### 2.5.3.2 Target Id

REPO-GPS-CON

#### 2.5.3.3 Message

3. Validate and Transform Payload

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 Internal Processing

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message



#### 2.5.3.8 Has Return

❌ No

#### 2.5.3.9 Is Activation

❌ No

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Function Call |
| Method | process_raw_data(payload) |
| Parameters | JSON data from API response. |
| Authentication | N/A |
| Error Handling | Uses Pydantic model for validation. If validation ... |
| Performance | Processing must be highly efficient to not delay t... |

#### 2.5.3.11 Nested Interactions

*No items available*

### 2.5.4.0 Message Publication

#### 2.5.4.1 Source Id

REPO-GPS-CON

#### 2.5.4.2 Target Id

RabbitMQ-Message-Broker

#### 2.5.4.3 Message

4. Publish 'VehicleLocationUpdated' Event

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 Message Publication

#### 2.5.4.6 Is Synchronous

❌ No

#### 2.5.4.7 Return Message



#### 2.5.4.8 Has Return

❌ No

#### 2.5.4.9 Is Activation

❌ No

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AMQP 0.9.1 |
| Method | basic.publish |
| Parameters | exchange: 'tms.gps.events', routing_key: 'location... |
| Authentication | Uses username/password credentials from AWS Secret... |
| Error Handling | Handles connection failures to the broker with a r... |
| Performance | Publishes messages for each valid location record ... |

### 2.5.5.0 Message Consumption

#### 2.5.5.1 Source Id

REPO-TMS-CORE

#### 2.5.5.2 Target Id

RabbitMQ-Message-Broker

#### 2.5.5.3 Message

5. Consume Batch of Location Events

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 Message Consumption

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message

5.1. Batch of messages (up to configured limit)

#### 2.5.5.8 Has Return

✅ Yes

#### 2.5.5.9 Is Activation

✅ Yes

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AMQP 0.9.1 |
| Method | basic.get (in a loop) or basic.consume |
| Parameters | queue: 'q.tms.location_updates', no_ack=false |
| Authentication | Uses username/password credentials. |
| Error Handling | Triggered by Odoo scheduled job (`ir.cron`) runnin... |
| Performance | Fetches a configurable batch of messages (e.g., 10... |

### 2.5.6.0 Internal Processing

#### 2.5.6.1 Source Id

REPO-TMS-CORE

#### 2.5.6.2 Target Id

REPO-TMS-CORE

#### 2.5.6.3 Message

6. Process Event Batch

#### 2.5.6.4 Sequence Number

6

#### 2.5.6.5 Type

🔹 Internal Processing

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Return Message



#### 2.5.6.8 Has Return

❌ No

#### 2.5.6.9 Is Activation

❌ No

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Function Call |
| Method | process_location_batch(messages) |
| Parameters | List of AMQP message objects. |
| Authentication | N/A |
| Error Handling | Iterates through each message. For any message tha... |
| Performance | Includes an idempotency check: for each event, ver... |

### 2.5.7.0 Database Transaction

#### 2.5.7.1 Source Id

REPO-TMS-CORE

#### 2.5.7.2 Target Id

REPO-TMS-CORE

#### 2.5.7.3 Message

7. Batch Update Vehicle Locations in DB

#### 2.5.7.4 Sequence Number

7

#### 2.5.7.5 Type

🔹 Database Transaction

#### 2.5.7.6 Is Synchronous

✅ Yes

#### 2.5.7.7 Return Message

7.1. Transaction Commit/Rollback

#### 2.5.7.8 Has Return

✅ Yes

#### 2.5.7.9 Is Activation

❌ No

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | vehicle_model.browse(ids).write(vals_list) |
| Parameters | A list of dictionaries containing updated location... |
| Authentication | Via Odoo's PostgreSQL connection pool. |
| Error Handling | The entire batch update is performed within a sing... |
| Performance | Using a single `write` call for the batch is criti... |

### 2.5.8.0 Message Acknowledgement

#### 2.5.8.1 Source Id

REPO-TMS-CORE

#### 2.5.8.2 Target Id

RabbitMQ-Message-Broker

#### 2.5.8.3 Message

8. Acknowledge/Reject Messages

#### 2.5.8.4 Sequence Number

8

#### 2.5.8.5 Type

🔹 Message Acknowledgement

#### 2.5.8.6 Is Synchronous

❌ No

#### 2.5.8.7 Return Message



#### 2.5.8.8 Has Return

❌ No

#### 2.5.8.9 Is Activation

❌ No

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AMQP 0.9.1 |
| Method | basic.ack (for successfully processed messages) an... |
| Parameters | ack: delivery_tag, multiple=true. nack: delivery_t... |
| Authentication | N/A |
| Error Handling | NACKing a message with `requeue=false` will cause ... |
| Performance | ACKs are sent after the database transaction is su... |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

REQ-NFR-001 Compliance: The total time from step 2 to step 7 must be less than 10 seconds for 95% of events. This is measured by comparing the event timestamp with the database update timestamp.

#### 2.6.1.2 Position

TopRight

#### 2.6.1.3 Participant Id

*Not specified*

#### 2.6.1.4 Sequence Number

0

### 2.6.2.0 Content

#### 2.6.2.1 Content

Idempotency Check: The logic in step 6 is crucial to handle potential message redeliveries from RabbitMQ, ensuring that an older location update does not overwrite a newer one.

#### 2.6.2.2 Position

Right

#### 2.6.2.3 Participant Id

REPO-TMS-CORE

#### 2.6.2.4 Sequence Number

6

### 2.6.3.0 Content

#### 2.6.3.1 Content

Dead-Letter Queue (DLQ): The 'q.tms.location_updates' queue is configured with a dead-letter-exchange pointing to a DLQ. Any message NACKed in step 8 triggers an immediate high-severity alert.

#### 2.6.3.2 Position

BottomRight

#### 2.6.3.3 Participant Id

RabbitMQ-Message-Broker

#### 2.6.3.4 Sequence Number

8

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | All communication must use TLS. API tokens for the... |
| Performance Targets | End-to-end event processing latency (p95) must be ... |
| Error Handling Strategy | Producer (`REPO-GPS-CON`): Implements an exponenti... |
| Testing Considerations | Unit tests for data validation/transformation logi... |
| Monitoring Requirements | Prometheus must monitor: 1) External API error rat... |
| Deployment Considerations | Both the producer and consumer are deployed as sep... |


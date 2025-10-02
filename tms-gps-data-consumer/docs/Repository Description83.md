# 1 Id

REPO-GPS-CON

# 2 Name

tms-gps-data-consumer

# 3 Description

This repository contains a focused Odoo addon, extracted from the 'tms-odoo-addon' monolith, whose single responsibility is to consume 'VehicleLocationUpdated' events from the RabbitMQ message queue. It implements the AMQP consumer logic as an Odoo scheduled action. Upon receiving a message, it validates the payload, finds the corresponding vehicle in the database, and updates its location. By isolating this consumer, we separate the concerns of asynchronous message processing and its specific dependency (pika library) from the core business logic, improving the maintainability and clarity of the main application. It depends on 'tms-core-business-logic' to perform the vehicle data updates.

# 4 Type

🔹 Infrastructure

# 5 Namespace

odoo.addons.tms_gps_consumer

# 6 Output Path

addons/tms_gps_consumer

# 7 Framework

Odoo 18

# 8 Language

Python

# 9 Technology

Python 3.11, RabbitMQ

# 10 Thirdparty Libraries

- pika

# 11 Layer Ids

- integration-messaging-layer

# 12 Dependencies

- REPO-TMS-CORE

# 13 Requirements

- {'requirementId': 'REQ-1-301'}

# 14 Generate Tests

✅ Yes

# 15 Generate Documentation

✅ Yes

# 16 Architecture Style

Event Consumer

# 17 Architecture Map

- Integration & Messaging Layer

# 18 Components Map

- integration-gateway-003

# 19 Requirements Map

- REQ-1-301

# 20 Decomposition Rationale

## 20.1 Operation Type

NEW_DECOMPOSED

## 20.2 Source Repository

tms-odoo-addon

## 20.3 Decomposition Reasoning

Extracted to isolate the asynchronous message consumer logic. This separates the AMQP protocol handling and its dependencies from the core application. It creates a clear boundary for the data ingestion endpoint within the monolith, making the data flow easier to understand and maintain.

## 20.4 Extracted Responsibilities

- RabbitMQ queue connection and consumption
- Event payload validation and deserialization
- Updating vehicle records based on events

## 20.5 Reusability Scope

- Specific to consuming GPS events for the TMS; not generally reusable.

## 20.6 Development Benefits

- The logic for handling incoming events is co-located and easy to find.
- Decouples the core business logic from the specifics of the messaging infrastructure.

# 21.0 Dependency Contracts

## 21.1 Repo-Tms-Core

### 21.1.1 Required Interfaces

- {'interface': 'Odoo ORM API (tms.vehicle)', 'methods': ["search([('truck_number', '=', vehicle_identifier)])", "write({'latitude': lat, 'longitude': lon})"], 'events': [], 'properties': []}

### 21.1.2 Integration Pattern

Direct ORM calls to update vehicle state.

### 21.1.3 Communication Protocol

Internal method calls

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

*No items available*

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | N/A |
| Event Communication | Acts as the consumer endpoint for the Event-Driven... |
| Data Flow | Receives data from RabbitMQ and writes it to the P... |
| Error Handling | Implements logic to handle un-processable messages... |
| Async Patterns | The entire component is asynchronous, triggered by... |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | The consumer must be idempotent, handling potentia... |
| Performance Considerations | Should process messages in batches to reduce datab... |
| Security Considerations | Connects to RabbitMQ using credentials securely in... |
| Testing Approach | Integration tests that simulate message delivery f... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- Connection to RabbitMQ.
- Consumption and acknowledgement of messages.
- Logic to handle poison messages.

## 25.2.0 Must Not Implement

- Any business logic beyond updating vehicle location.
- Publishing messages to any queue.

## 25.3.0 Extension Points

*No items available*

## 25.4.0 Validation Rules

- Must validate the incoming event payload against the expected schema before processing.


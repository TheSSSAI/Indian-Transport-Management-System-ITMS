# 1 Id

REPO-GPS-SVC

# 2 Name

tms-gps-ingestion-service

# 3 Description

This repository contains the standalone, decoupled microservice responsible for ingesting real-time GPS data. Built with FastAPI for high performance, its function is to poll the third-party GPS provider's API, validate the received data against a strict contract, and publish it as a standardized 'VehicleLocationUpdated' event to a RabbitMQ message queue. This service is a critical component of the system's real-time tracking feature, designed for high throughput and resilience. Its isolation from the core monolith is a key architectural decision to prevent performance degradation of the main application from high-frequency I/O operations.

# 4 Type

🔹 Application Services

# 5 Namespace

tms.gps_ingestion

# 6 Output Path

services/gps_ingestion

# 7 Framework

FastAPI

# 8 Language

Python

# 9 Technology

FastAPI, Python 3.11, Docker

# 10 Thirdparty Libraries

- pydantic
- pika
- requests

# 11 Layer Ids

- gps-microservice

# 12 Dependencies

*No items available*

# 13 Requirements

## 13.1 Requirement Id

### 13.1.1 Requirement Id

REQ-1-013

## 13.2.0 Requirement Id

### 13.2.1 Requirement Id

REQ-1-301

## 13.3.0 Requirement Id

### 13.3.1 Requirement Id

REQ-1-401

# 14.0.0 Generate Tests

✅ Yes

# 15.0.0 Generate Documentation

✅ Yes

# 16.0.0 Architecture Style

Microservice

# 17.0.0 Architecture Map

- GPS Ingestion Microservice

# 18.0.0 Components Map

- gps-ingestion-service-002

# 19.0.0 Requirements Map

- REQ-1-013
- REQ-1-301
- REQ-1-401

# 20.0.0 Decomposition Rationale

## 20.1.0 Operation Type

PRESERVED

## 20.2.0 Source Repository

tms-gps-ingestion-service

## 20.3.0 Decomposition Reasoning

This repository was preserved in its original form as it already represents a well-defined, single-responsibility component (microservice) that is architecturally decoupled from the monolith, aligning perfectly with the decomposition goals.

## 20.4.0 Extracted Responsibilities

*No items available*

## 20.5.0 Reusability Scope

- The pattern is reusable, but the implementation is specific to the chosen GPS provider.

## 20.6.0 Development Benefits

- Allows a specialist team to own and optimize the real-time data pipeline.
- Independent scaling and deployment based on telemetry volume.

# 21.0.0 Dependency Contracts

*No data available*

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

- {'interface': 'AMQP Publisher', 'methods': [], 'events': ['VehicleLocationUpdated'], 'properties': [], 'consumers': ['REPO-GPS-CON']}

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | FastAPI's dependency injection is used for managin... |
| Event Communication | Acts as the producer in an Event-Driven pattern, p... |
| Data Flow | Polls external HTTP API, transforms data, and publ... |
| Error Handling | Uses exponential backoff for API polling failures. |
| Async Patterns | Leverages Python's asyncio and FastAPI's async cap... |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | Utilize Pydantic for strict data validation of the... |
| Performance Considerations | The service is designed for high-throughput and sh... |
| Security Considerations | API keys and other secrets must be loaded from the... |
| Testing Approach | Unit tests for transformation logic and integratio... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- Polling the GPS provider API.
- Publishing the canonical 'VehicleLocationUpdated' event.
- A '/health' endpoint for monitoring.

## 25.2.0 Must Not Implement

- Any direct communication with the core application database.
- Any business logic related to trips or drivers.

## 25.3.0 Extension Points

*No items available*

## 25.4.0 Validation Rules

- Must enforce the data contract for all incoming data before publishing.


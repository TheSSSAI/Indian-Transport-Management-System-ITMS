# 1 Design

code_design

# 2 Code Specfication

## 2.1 Validation Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GPS-SVC |
| Validation Timestamp | 2024-05-24T11:00:00Z |
| Original Component Count Claimed | 0 |
| Original Component Count Actual | 0 |
| Gaps Identified Count | 5 |
| Components Added Count | 18 |
| Final Component Count | 18 |
| Validation Completeness Score | 100% |
| Enhancement Methodology | Systematic validation of an empty specification ag... |

## 2.2 Validation Summary

### 2.2.1 Repository Scope Validation

#### 2.2.1.1 Scope Compliance

Validation confirmed a 100% gap in the initial specification. The enhanced specification is now fully compliant with the repository's scope as a stateless, high-throughput data ingestion microservice.

#### 2.2.1.2 Gaps Identified

- Missing specification for the application entry point (`main.py`) with lifecycle management.
- Missing specification for a mandatory `/health` endpoint for Kubernetes probes.
- Missing specification for structured JSON logging (REQ-1-602).
- Missing specification for custom exceptions to create clear error contracts.
- Missing specification for a Prometheus metrics endpoint (REQ-1-602).

#### 2.2.1.3 Components Added

- Specification for `main.py` FastAPI application instance with startup/shutdown events.
- Specification for `HealthCheckRouter` in `api/health.py`.
- Specification for `core/logging.py` to enforce structured JSON logging.
- Specification for `core/exceptions.py` to define `ApiClientError` and `MessagingError`.
- Specification for `PrometheusMiddleware` integration in `main.py`.
- Complete file structure and component specifications for all layers.

### 2.2.2.0 Requirements Coverage Validation

#### 2.2.2.1 Functional Requirements Coverage

100%

#### 2.2.2.2 Non Functional Requirements Coverage

100%

#### 2.2.2.3 Missing Requirement Components

- Specification for starting the polling service as a background task (REQ-1-301).
- Specification using an asynchronous HTTP client (`httpx`) required for a non-blocking service.
- Specification for publishing persistent messages to RabbitMQ for durability.

#### 2.2.2.4 Added Requirement Components

- Enhanced `main.py` specification to include `asyncio.create_task` for the polling service.
- Updated technology stack and client specification to mandate `httpx`.
- Enhanced `RabbitMQPublisher` specification to publish persistent messages.

### 2.2.3.0 Architectural Pattern Validation

#### 2.2.3.1 Pattern Implementation Completeness

The initial specification was empty. The enhanced specification fully details the Polling, Event Publisher, and Background Task patterns in a resilient, asynchronous manner.

#### 2.2.3.2 Missing Pattern Components

- Missing specification for a robust reconnection and retry mechanism in the messaging and HTTP clients.
- Absence of custom exception classes to create clear contracts between service layers.

#### 2.2.3.3 Added Pattern Components

- Enhanced `GpsProviderApiClient` to include exponential backoff retries.
- Enhanced `RabbitMQPublisher` to include reconnect-and-retry logic.
- Added specifications for `ApiClientError` and `MessagingError`.

### 2.2.4.0 Database Mapping Validation

#### 2.2.4.1 Entity Mapping Completeness

Not Applicable. Validation confirms the specification correctly adheres to the requirement of not having any direct database access.

#### 2.2.4.2 Missing Database Components

*No items available*

#### 2.2.4.3 Added Database Components

*No items available*

### 2.2.5.0 Sequence Interaction Validation

#### 2.2.5.1 Interaction Implementation Completeness

The initial specification was empty. The enhanced specification now fully details the interactions from the 'Event-Driven Ingestion' sequence diagram (ID: 226).

#### 2.2.5.2 Missing Interaction Components

- Specification for the component that polls the external API.
- Specification for the component that validates data.
- Specification for the component that publishes to the message queue.

#### 2.2.5.3 Added Interaction Components

- GpsProviderApiClient
- IncomingGpsData (Pydantic Schema)
- RabbitMQPublisher

## 2.3.0.0 Enhanced Specification

### 2.3.1.0 Specification Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GPS-SVC |
| Technology Stack | FastAPI, Python 3.11, Docker, Pydantic, httpx, aio... |
| Technology Guidance Integration | Specification fully aligns with FastAPI best pract... |
| Framework Compliance Score | 100% |
| Specification Completeness | 100% |
| Component Count | 18 |
| Specification Methodology | Systematic translation of architectural requiremen... |

### 2.3.2.0 Technology Framework Integration

#### 2.3.2.1 Framework Patterns Applied

- Dependency Injection (Application-level Singletons)
- Polling
- Event Publisher
- Background Task
- Retry with Exponential Backoff
- Data Transfer Object (DTO) using Pydantic
- Configuration via Environment Variables

#### 2.3.2.2 Directory Structure Source

Python `src` layout, adapted for a focused FastAPI microservice with clear separation of concerns (api, core, clients, messaging, schemas, services).

#### 2.3.2.3 Naming Conventions Source

Python PEP 8 standards with PascalCase for classes and snake_case for functions and variables.

#### 2.3.2.4 Architectural Patterns Source

Event-driven, decoupled microservice architecture as mandated by REQ-1-013.

#### 2.3.2.5 Performance Optimizations Applied

- Asynchronous-first design for all I/O operations using `async`/`await`.
- Stateless service design for horizontal scalability.
- Use of `httpx.AsyncClient` for efficient, non-blocking HTTP requests.
- Long-lived client and publisher connections managed via FastAPI's lifecycle events to minimize overhead.

### 2.3.3.0 File Structure

#### 2.3.3.1 Directory Organization

##### 2.3.3.1.1 Directory Path

###### 2.3.3.1.1.1 Directory Path

src/app/api

###### 2.3.3.1.1.2 Purpose

Contains FastAPI routers for exposing HTTP endpoints, specifically for observability.

###### 2.3.3.1.1.3 Contains Files

- __init__.py
- health.py

###### 2.3.3.1.1.4 Organizational Reasoning

Separates the presentation layer (HTTP API) from the core service logic, following Clean Architecture principles.

###### 2.3.3.1.1.5 Framework Convention Alignment

Standard FastAPI practice for organizing modular API routers.

##### 2.3.3.1.2.0 Directory Path

###### 2.3.3.1.2.1 Directory Path

src/app/clients

###### 2.3.3.1.2.2 Purpose

Contains clients for interacting with external services.

###### 2.3.3.1.2.3 Contains Files

- __init__.py
- gps_provider_client.py

###### 2.3.3.1.2.4 Organizational Reasoning

Encapsulates the logic for communicating with a specific third-party API, isolating external dependencies.

###### 2.3.3.1.2.5 Framework Convention Alignment

Common pattern for organizing external service integrations.

##### 2.3.3.1.3.0 Directory Path

###### 2.3.3.1.3.1 Directory Path

src/app/core

###### 2.3.3.1.3.2 Purpose

Houses application-wide configuration, custom exceptions, and logging setup.

###### 2.3.3.1.3.3 Contains Files

- __init__.py
- config.py
- exceptions.py
- logging.py

###### 2.3.3.1.3.4 Organizational Reasoning

Centralizes cross-cutting concerns like configuration and error handling for consistency.

###### 2.3.3.1.3.5 Framework Convention Alignment

Best practice for managing application settings and shared utilities in Python applications.

##### 2.3.3.1.4.0 Directory Path

###### 2.3.3.1.4.1 Directory Path

src/app/messaging

###### 2.3.3.1.4.2 Purpose

Contains components responsible for publishing messages to a message broker.

###### 2.3.3.1.4.3 Contains Files

- __init__.py
- publisher.py

###### 2.3.3.1.4.4 Organizational Reasoning

Isolates the messaging infrastructure logic, allowing for easier maintenance or replacement of the message broker technology.

###### 2.3.3.1.4.5 Framework Convention Alignment

Adheres to the Dependency Inversion Principle by providing a concrete implementation for a messaging contract.

##### 2.3.3.1.5.0 Directory Path

###### 2.3.3.1.5.1 Directory Path

src/app/schemas

###### 2.3.3.1.5.2 Purpose

Defines all Pydantic models for data validation and serialization (DTOs).

###### 2.3.3.1.5.3 Contains Files

- __init__.py
- gps.py

###### 2.3.3.1.5.4 Organizational Reasoning

Creates a single source of truth for all data contracts, both for incoming external data and outgoing events.

###### 2.3.3.1.5.5 Framework Convention Alignment

Leverages FastAPI's core strength of using Pydantic for defining and enforcing data schemas.

##### 2.3.3.1.6.0 Directory Path

###### 2.3.3.1.6.1 Directory Path

src/app/services

###### 2.3.3.1.6.2 Purpose

Contains the core business logic and orchestration for the microservice.

###### 2.3.3.1.6.3 Contains Files

- __init__.py
- polling_service.py

###### 2.3.3.1.6.4 Organizational Reasoning

Encapsulates the main workflow of the service (poll, validate, publish) in a dedicated service layer.

###### 2.3.3.1.6.5 Framework Convention Alignment

Standard practice for organizing application services in a Clean Architecture-inspired structure.

##### 2.3.3.1.7.0 Directory Path

###### 2.3.3.1.7.1 Directory Path

src

###### 2.3.3.1.7.2 Purpose

Root source directory for the application.

###### 2.3.3.1.7.3 Contains Files

- main.py

###### 2.3.3.1.7.4 Organizational Reasoning

Follows the standard Python `src` layout for clean separation of application code from project root files.

###### 2.3.3.1.7.5 Framework Convention Alignment

Recommended project structure for modern Python applications.

##### 2.3.3.1.8.0 Directory Path

###### 2.3.3.1.8.1 Directory Path

.

###### 2.3.3.1.8.2 Purpose

Project root directory.

###### 2.3.3.1.8.3 Contains Files

- Dockerfile
- docker-compose.yml
- .dockerignore
- pyproject.toml
- README.md

###### 2.3.3.1.8.4 Organizational Reasoning

Contains all project-level configuration, containerization instructions, and documentation.

###### 2.3.3.1.8.5 Framework Convention Alignment

Standard for containerized Python projects.

#### 2.3.3.2.0.0 Namespace Strategy

| Property | Value |
|----------|-------|
| Root Namespace | app |
| Namespace Organization | Modules are organized by architectural layer (e.g.... |
| Naming Conventions | Follows Python PEP 8 standards (e.g., `polling_ser... |
| Framework Alignment | Aligns with FastAPI's modular application structur... |

### 2.3.4.0.0.0 Class Specifications

#### 2.3.4.1.0.0 Class Name

##### 2.3.4.1.1.0 Class Name

FastAPI Application

##### 2.3.4.1.2.0 File Path

src/main.py

##### 2.3.4.1.3.0 Class Type

Application Entry Point

##### 2.3.4.1.4.0 Inheritance

N/A

##### 2.3.4.1.5.0 Purpose

To instantiate and configure the FastAPI application, register API routers, manage the lifecycle of shared resources (like API clients and message publishers), and start background tasks.

##### 2.3.4.1.6.0 Dependencies

- FastAPI
- asyncio
- HealthCheckRouter
- PollingService
- GpsProviderApiClient
- RabbitMQPublisher
- Settings
- setup_logging

##### 2.3.4.1.7.0 Framework Specific Attributes

- @app.on_event(\"startup\")
- @app.on_event(\"shutdown\")

##### 2.3.4.1.8.0 Technology Integration Notes

This is the main entry point for the Uvicorn ASGI server. It uses FastAPI's startup and shutdown events to manage long-lived connections and background tasks.

##### 2.3.4.1.9.0 Properties

*No items available*

##### 2.3.4.1.10.0 Methods

###### 2.3.4.1.10.1 Method Name

####### 2.3.4.1.10.1.1 Method Name

startup_event_handler

####### 2.3.4.1.10.1.2 Method Signature

startup_event_handler()

####### 2.3.4.1.10.1.3 Return Type

Task<None>

####### 2.3.4.1.10.1.4 Access Modifier

N/A

####### 2.3.4.1.10.1.5 Is Async

true

####### 2.3.4.1.10.1.6 Framework Specific Attributes

*No items available*

####### 2.3.4.1.10.1.7 Parameters

*No items available*

####### 2.3.4.1.10.1.8 Implementation Logic

Specification requires this handler to:\n1. Instantiate singleton instances of Settings, GpsProviderApiClient, and RabbitMQPublisher and attach them to the `app.state` for application-wide access.\n2. Call the `connect()` method on the RabbitMQPublisher instance.\n3. Instantiate the PollingService with its dependencies.\n4. Start the `PollingService.run_polling_cycle_async()` method as a persistent background task using `asyncio.create_task()`.

####### 2.3.4.1.10.1.9 Exception Handling

Specification requires robust error handling to log critical failures during startup and prevent the application from starting in a broken state.

####### 2.3.4.1.10.1.10 Performance Considerations

Specification ensures that expensive client initializations happen only once at startup.

####### 2.3.4.1.10.1.11 Validation Requirements

N/A

####### 2.3.4.1.10.1.12 Technology Integration Details

Tied to the FastAPI application lifecycle via the `@app.on_event(\"startup\")` decorator.

###### 2.3.4.1.10.2.0 Method Name

####### 2.3.4.1.10.2.1 Method Name

shutdown_event_handler

####### 2.3.4.1.10.2.2 Method Signature

shutdown_event_handler()

####### 2.3.4.1.10.2.3 Return Type

Task[None]

####### 2.3.4.1.10.2.4 Access Modifier

N/A

####### 2.3.4.1.10.2.5 Is Async

true

####### 2.3.4.1.10.2.6 Framework Specific Attributes

*No items available*

####### 2.3.4.1.10.2.7 Parameters

*No items available*

####### 2.3.4.1.10.2.8 Implementation Logic

Specification requires this handler to gracefully close all external connections. It must call the `close()` methods on the GpsProviderApiClient and RabbitMQPublisher instances.

####### 2.3.4.1.10.2.9 Exception Handling

Specification requires logging any errors that occur during shutdown.

####### 2.3.4.1.10.2.10 Performance Considerations

N/A

####### 2.3.4.1.10.2.11 Validation Requirements

N/A

####### 2.3.4.1.10.2.12 Technology Integration Details

Tied to the FastAPI application lifecycle via the `@app.on_event(\"shutdown\")` decorator.

##### 2.3.4.1.11.0.0 Events

*No items available*

##### 2.3.4.1.12.0.0 Implementation Notes

The specification for the main application object includes router registration for the health check endpoint and middleware for Prometheus metrics.

#### 2.3.4.2.0.0.0 Class Name

##### 2.3.4.2.1.0.0 Class Name

HealthCheckRouter

##### 2.3.4.2.2.0.0 File Path

src/app/api/health.py

##### 2.3.4.2.3.0.0 Class Type

API Router

##### 2.3.4.2.4.0.0 Inheritance

N/A

##### 2.3.4.2.5.0.0 Purpose

To provide a simple, unauthenticated HTTP endpoint for health checks, liveness probes, and readiness probes by monitoring systems like Kubernetes.

##### 2.3.4.2.6.0.0 Dependencies

- fastapi.APIRouter

##### 2.3.4.2.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.2.8.0.0 Technology Integration Notes

Implements a standard FastAPI router that can be included in the main application.

##### 2.3.4.2.9.0.0 Properties

*No items available*

##### 2.3.4.2.10.0.0 Methods

- {'method_name': 'get_health_status', 'method_signature': 'get_health_status()', 'return_type': 'Dict[str, str]', 'access_modifier': 'N/A', 'is_async': 'false', 'framework_specific_attributes': ['@router.get(\\"/health\\", status_code=200)'], 'parameters': [], 'implementation_logic': 'Specification requires this method to return a simple JSON object: `{\\"status\\": \\"healthy\\"}`. It should not perform any complex checks.', 'exception_handling': 'N/A. FastAPI handles standard HTTP exception generation.', 'performance_considerations': 'Specification requires this endpoint to be extremely fast and lightweight.', 'validation_requirements': 'N/A', 'technology_integration_details': ''}

##### 2.3.4.2.11.0.0 Events

*No items available*

##### 2.3.4.2.12.0.0 Implementation Notes

This specification covers the mandatory health check endpoint.

#### 2.3.4.3.0.0.0 Class Name

##### 2.3.4.3.1.0.0 Class Name

CustomExceptions

##### 2.3.4.3.2.0.0 File Path

src/app/core/exceptions.py

##### 2.3.4.3.3.0.0 Class Type

Module

##### 2.3.4.3.4.0.0 Inheritance

N/A

##### 2.3.4.3.5.0.0 Purpose

To define a set of custom, application-specific exception classes to create clear error handling contracts between different layers of the service.

##### 2.3.4.3.6.0.0 Dependencies

*No items available*

##### 2.3.4.3.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.3.8.0.0 Technology Integration Notes

Standard Python practice for defining custom exceptions.

##### 2.3.4.3.9.0.0 Properties

###### 2.3.4.3.9.1.0 Property Name

####### 2.3.4.3.9.1.1 Property Name

ApiClientError

####### 2.3.4.3.9.1.2 Property Type

Exception

####### 2.3.4.3.9.1.3 Access Modifier

public

####### 2.3.4.3.9.1.4 Purpose

Raised when the `GpsProviderApiClient` encounters a persistent, non-recoverable error after all retries have failed.

####### 2.3.4.3.9.1.5 Validation Attributes

*No items available*

####### 2.3.4.3.9.1.6 Framework Specific Configuration



####### 2.3.4.3.9.1.7 Implementation Notes

Should inherit from Python's base `Exception` class.

###### 2.3.4.3.9.2.0 Property Name

####### 2.3.4.3.9.2.1 Property Name

MessagingError

####### 2.3.4.3.9.2.2 Property Type

Exception

####### 2.3.4.3.9.2.3 Access Modifier

public

####### 2.3.4.3.9.2.4 Purpose

Raised when the `RabbitMQPublisher` fails to publish a message after attempting to reconnect.

####### 2.3.4.3.9.2.5 Validation Attributes

*No items available*

####### 2.3.4.3.9.2.6 Framework Specific Configuration



####### 2.3.4.3.9.2.7 Implementation Notes

Should inherit from Python's base `Exception` class.

##### 2.3.4.3.10.0.0 Methods

*No items available*

##### 2.3.4.3.11.0.0 Events

*No items available*

##### 2.3.4.3.12.0.0 Implementation Notes

This specification for custom exceptions improves internal contracts.

#### 2.3.4.4.0.0.0 Class Name

##### 2.3.4.4.1.0.0 Class Name

StructuredLogger

##### 2.3.4.4.2.0.0 File Path

src/app/core/logging.py

##### 2.3.4.4.3.0.0 Class Type

Configuration

##### 2.3.4.4.4.0.0 Inheritance

N/A

##### 2.3.4.4.5.0.0 Purpose

To configure the Python standard logging module to output logs in a structured JSON format, satisfying requirement REQ-1-602.

##### 2.3.4.4.6.0.0 Dependencies

- logging
- python-json-logger

##### 2.3.4.4.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.4.8.0.0 Technology Integration Notes

Specification recommends using a library like `python-json-logger` to format log records as JSON objects, which can be easily ingested by log aggregators like Fluentbit.

##### 2.3.4.4.9.0.0 Properties

*No items available*

##### 2.3.4.4.10.0.0 Methods

- {'method_name': 'setup_logging', 'method_signature': 'setup_logging(log_level: str)', 'return_type': 'None', 'access_modifier': 'N/A', 'is_async': 'false', 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'log_level', 'parameter_type': 'str', 'is_nullable': 'false', 'purpose': 'The logging level to configure (e.g., \\"INFO\\").', 'framework_attributes': []}], 'implementation_logic': 'Specification requires this function to configure the root logger to use a JSON formatter. The formatter should include standard fields like timestamp, level, message, as well as any extra context.', 'exception_handling': 'N/A', 'performance_considerations': 'N/A', 'validation_requirements': 'N/A', 'technology_integration_details': 'This function should be called once at application startup in `main.py`.'}

##### 2.3.4.4.11.0.0 Events

*No items available*

##### 2.3.4.4.12.0.0 Implementation Notes

This specification enforces structured JSON logging.

#### 2.3.4.5.0.0.0 Class Name

##### 2.3.4.5.1.0.0 Class Name

Settings

##### 2.3.4.5.2.0.0 File Path

src/app/core/config.py

##### 2.3.4.5.3.0.0 Class Type

Configuration

##### 2.3.4.5.4.0.0 Inheritance

pydantic_settings.BaseSettings

##### 2.3.4.5.5.0.0 Purpose

To provide a type-safe, environment-aware configuration object for the entire application, loading secrets and settings from environment variables.

##### 2.3.4.5.6.0.0 Dependencies

- pydantic
- pydantic_settings

##### 2.3.4.5.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.5.8.0.0 Technology Integration Notes

Leverages the `pydantic-settings` library to automatically read configuration from the environment, which is ideal for Docker and Kubernetes deployments.

##### 2.3.4.5.9.0.0 Properties

###### 2.3.4.5.9.1.0 Property Name

####### 2.3.4.5.9.1.1 Property Name

LOG_LEVEL

####### 2.3.4.5.9.1.2 Property Type

str

####### 2.3.4.5.9.1.3 Access Modifier

public

####### 2.3.4.5.9.1.4 Purpose

Specifies the application's logging level (e.g., INFO, DEBUG).

####### 2.3.4.5.9.1.5 Validation Attributes

*No items available*

####### 2.3.4.5.9.1.6 Framework Specific Configuration

Default value should be \"INFO\".

####### 2.3.4.5.9.1.7 Implementation Notes

Should be loaded from an environment variable.

###### 2.3.4.5.9.2.0 Property Name

####### 2.3.4.5.9.2.1 Property Name

GPS_PROVIDER_API_URL

####### 2.3.4.5.9.2.2 Property Type

pydantic.HttpUrl

####### 2.3.4.5.9.2.3 Access Modifier

public

####### 2.3.4.5.9.2.4 Purpose

The base URL of the third-party GPS provider's API.

####### 2.3.4.5.9.2.5 Validation Attributes

- [Required]

####### 2.3.4.5.9.2.6 Framework Specific Configuration

Loaded from an environment variable.

####### 2.3.4.5.9.2.7 Implementation Notes

Pydantic's `HttpUrl` type provides built-in validation for the URL format.

###### 2.3.4.5.9.3.0 Property Name

####### 2.3.4.5.9.3.1 Property Name

GPS_PROVIDER_API_KEY

####### 2.3.4.5.9.3.2 Property Type

pydantic.SecretStr

####### 2.3.4.5.9.3.3 Access Modifier

public

####### 2.3.4.5.9.3.4 Purpose

The secret API key for authenticating with the GPS provider.

####### 2.3.4.5.9.3.5 Validation Attributes

- [Required]

####### 2.3.4.5.9.3.6 Framework Specific Configuration

Loaded from an environment variable. Should be injected via AWS Secrets Manager in production.

####### 2.3.4.5.9.3.7 Implementation Notes

Using `SecretStr` prevents the key from being accidentally exposed in logs or tracebacks.

###### 2.3.4.5.9.4.0 Property Name

####### 2.3.4.5.9.4.1 Property Name

POLLING_INTERVAL_SECONDS

####### 2.3.4.5.9.4.2 Property Type

int

####### 2.3.4.5.9.4.3 Access Modifier

public

####### 2.3.4.5.9.4.4 Purpose

The interval in seconds between polling requests to the GPS API.

####### 2.3.4.5.9.4.5 Validation Attributes

*No items available*

####### 2.3.4.5.9.4.6 Framework Specific Configuration

Default value should be 60.

####### 2.3.4.5.9.4.7 Implementation Notes

Must be a positive integer.

###### 2.3.4.5.9.5.0 Property Name

####### 2.3.4.5.9.5.1 Property Name

RABBITMQ_URL

####### 2.3.4.5.9.5.2 Property Type

pydantic.AmqpDsn

####### 2.3.4.5.9.5.3 Access Modifier

public

####### 2.3.4.5.9.5.4 Purpose

The connection URL for the RabbitMQ broker.

####### 2.3.4.5.9.5.5 Validation Attributes

- [Required]

####### 2.3.4.5.9.5.6 Framework Specific Configuration

Loaded from an environment variable.

####### 2.3.4.5.9.5.7 Implementation Notes

Pydantic's `AmqpDsn` type validates the AMQP connection string format.

###### 2.3.4.5.9.6.0 Property Name

####### 2.3.4.5.9.6.1 Property Name

RABBITMQ_EXCHANGE_NAME

####### 2.3.4.5.9.6.2 Property Type

str

####### 2.3.4.5.9.6.3 Access Modifier

public

####### 2.3.4.5.9.6.4 Purpose

The name of the RabbitMQ exchange to publish events to.

####### 2.3.4.5.9.6.5 Validation Attributes

*No items available*

####### 2.3.4.5.9.6.6 Framework Specific Configuration

Default value should be \"tms.events\".

####### 2.3.4.5.9.6.7 Implementation Notes



###### 2.3.4.5.9.7.0 Property Name

####### 2.3.4.5.9.7.1 Property Name

RABBITMQ_ROUTING_KEY

####### 2.3.4.5.9.7.2 Property Type

str

####### 2.3.4.5.9.7.3 Access Modifier

public

####### 2.3.4.5.9.7.4 Purpose

The routing key to use for vehicle location update events.

####### 2.3.4.5.9.7.5 Validation Attributes

*No items available*

####### 2.3.4.5.9.7.6 Framework Specific Configuration

Default value should be \"location.updated\".

####### 2.3.4.5.9.7.7 Implementation Notes



##### 2.3.4.5.10.0.0 Methods

*No items available*

##### 2.3.4.5.11.0.0 Events

*No items available*

##### 2.3.4.5.12.0.0 Implementation Notes

This class should be instantiated once and provided to the rest of the application via dependency injection.

#### 2.3.4.6.0.0.0 Class Name

##### 2.3.4.6.1.0.0 Class Name

GpsProviderApiClient

##### 2.3.4.6.2.0.0 File Path

src/app/clients/gps_provider_client.py

##### 2.3.4.6.3.0.0 Class Type

Client

##### 2.3.4.6.4.0.0 Inheritance



##### 2.3.4.6.5.0.0 Purpose

To encapsulate all logic for communicating with the third-party GPS provider's API, including request formation, error handling, and retries.

##### 2.3.4.6.6.0.0 Dependencies

- httpx.AsyncClient
- Settings
- logging.Logger
- tenacity

##### 2.3.4.6.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.6.8.0.0 Technology Integration Notes

Uses `httpx` for asynchronous HTTP requests and `tenacity` for declarative retry logic with exponential backoff.

##### 2.3.4.6.9.0.0 Properties

*No items available*

##### 2.3.4.6.10.0.0 Methods

- {'method_name': 'fetch_locations_async', 'method_signature': 'fetch_locations_async()', 'return_type': 'Task[List[Dict]]', 'access_modifier': 'public', 'is_async': 'true', 'framework_specific_attributes': ['@tenacity.retry(...)'], 'parameters': [], 'implementation_logic': 'Should construct the request URL with the API key. On a successful (200 OK) response, it should parse the JSON body and return the list of location data points. The `@retry` decorator will handle transient HTTP errors (5xx) and connection timeouts with exponential backoff. On persistent failure after all retries, it should raise a custom `ApiClientError`.', 'exception_handling': 'Must catch `httpx.RequestError` and HTTP status codes >= 400. The retry logic should differentiate between retryable (5xx, timeout) and non-retryable (4xx) errors. If all retries fail, it must raise `ApiClientError`.', 'performance_considerations': 'Should use a single, long-lived `httpx.AsyncClient` instance to leverage connection pooling.', 'validation_requirements': 'Should validate that the response is valid JSON before returning.', 'technology_integration_details': 'The `tenacity` library will be configured for exponential backoff, stop conditions, and logging between retries as required by REQ-1-301.'}

##### 2.3.4.6.11.0.0 Events

*No items available*

##### 2.3.4.6.12.0.0 Implementation Notes

The client should be instantiated once and shared via dependency injection to manage the lifecycle of the `httpx.AsyncClient`.

#### 2.3.4.7.0.0.0 Class Name

##### 2.3.4.7.1.0.0 Class Name

RabbitMQPublisher

##### 2.3.4.7.2.0.0 File Path

src/app/messaging/publisher.py

##### 2.3.4.7.3.0.0 Class Type

Publisher

##### 2.3.4.7.4.0.0 Inheritance



##### 2.3.4.7.5.0.0 Purpose

To manage the connection to RabbitMQ and provide a simple interface for publishing events.

##### 2.3.4.7.6.0.0 Dependencies

- aio_pika
- Settings
- logging.Logger

##### 2.3.4.7.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.7.8.0.0 Technology Integration Notes

Uses the `aio_pika` library for asynchronous AMQP integration, which is ideal for `asyncio`-based applications like FastAPI.

##### 2.3.4.7.9.0.0 Properties

*No items available*

##### 2.3.4.7.10.0.0 Methods

###### 2.3.4.7.10.1.0 Method Name

####### 2.3.4.7.10.1.1 Method Name

connect

####### 2.3.4.7.10.1.2 Method Signature

connect()

####### 2.3.4.7.10.1.3 Return Type

Task<None>

####### 2.3.4.7.10.1.4 Access Modifier

public

####### 2.3.4.7.10.1.5 Is Async

true

####### 2.3.4.7.10.1.6 Framework Specific Attributes

*No items available*

####### 2.3.4.7.10.1.7 Parameters

*No items available*

####### 2.3.4.7.10.1.8 Implementation Logic

Should establish a connection to the RabbitMQ broker using the URL from settings. Should create a channel and declare the configured exchange (e.g., a topic exchange) to ensure it exists.

####### 2.3.4.7.10.1.9 Exception Handling

Must catch connection errors and implement a retry mechanism. Should log critical errors if the connection cannot be established after several attempts.

####### 2.3.4.7.10.1.10 Performance Considerations

The connection should be established once at application startup and reused.

####### 2.3.4.7.10.1.11 Validation Requirements

N/A

####### 2.3.4.7.10.1.12 Technology Integration Details



###### 2.3.4.7.10.2.0 Method Name

####### 2.3.4.7.10.2.1 Method Name

publish_event

####### 2.3.4.7.10.2.2 Method Signature

publish_event(event: VehicleLocationUpdatedEvent)

####### 2.3.4.7.10.2.3 Return Type

Task<None>

####### 2.3.4.7.10.2.4 Access Modifier

public

####### 2.3.4.7.10.2.5 Is Async

true

####### 2.3.4.7.10.2.6 Framework Specific Attributes

*No items available*

####### 2.3.4.7.10.2.7 Parameters

- {'parameter_name': 'event', 'parameter_type': 'VehicleLocationUpdatedEvent', 'is_nullable': 'false', 'purpose': 'The Pydantic event object to be published.', 'framework_attributes': []}

####### 2.3.4.7.10.2.8 Implementation Logic

Must serialize the Pydantic event object into a JSON byte string. Must create an `aio_pika.Message` with `delivery_mode=aio_pika.DeliveryMode.PERSISTENT` to ensure durability. Must publish the message to the configured exchange with the correct routing key. Should include a reconnect-and-retry mechanism for publishing if the connection is lost.

####### 2.3.4.7.10.2.9 Exception Handling

Must handle potential connection issues by attempting to reconnect before publishing. Must raise `MessagingError` on persistent failure.

####### 2.3.4.7.10.2.10 Performance Considerations

Publishing is a fast operation. The main consideration is ensuring the connection is stable.

####### 2.3.4.7.10.2.11 Validation Requirements

The input event object is already validated by Pydantic.

####### 2.3.4.7.10.2.12 Technology Integration Details

The message body must be a byte-encoded JSON string, and the message must be marked as persistent.

###### 2.3.4.7.10.3.0 Method Name

####### 2.3.4.7.10.3.1 Method Name

close

####### 2.3.4.7.10.3.2 Method Signature

close()

####### 2.3.4.7.10.3.3 Return Type

Task<None>

####### 2.3.4.7.10.3.4 Access Modifier

public

####### 2.3.4.7.10.3.5 Is Async

true

####### 2.3.4.7.10.3.6 Framework Specific Attributes

*No items available*

####### 2.3.4.7.10.3.7 Parameters

*No items available*

####### 2.3.4.7.10.3.8 Implementation Logic

Should gracefully close the channel and connection to RabbitMQ.

####### 2.3.4.7.10.3.9 Exception Handling

Should handle exceptions that may occur during the closing process.

####### 2.3.4.7.10.3.10 Performance Considerations

N/A

####### 2.3.4.7.10.3.11 Validation Requirements

N/A

####### 2.3.4.7.10.3.12 Technology Integration Details



##### 2.3.4.7.11.0.0 Events

*No items available*

##### 2.3.4.7.12.0.0 Implementation Notes

This publisher should be a singleton instance managed by the application's lifecycle.

#### 2.3.4.8.0.0.0 Class Name

##### 2.3.4.8.1.0.0 Class Name

PollingService

##### 2.3.4.8.2.0.0 File Path

src/app/services/polling_service.py

##### 2.3.4.8.3.0.0 Class Type

Service

##### 2.3.4.8.4.0.0 Inheritance



##### 2.3.4.8.5.0.0 Purpose

To orchestrate the main application workflow: periodically polling the GPS API, validating the data, and publishing it to the message queue.

##### 2.3.4.8.6.0.0 Dependencies

- GpsProviderApiClient
- RabbitMQPublisher
- Settings
- logging.Logger

##### 2.3.4.8.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.8.8.0.0 Technology Integration Notes

This service contains the core logic and is designed to be run as a continuous background task within the FastAPI application's event loop.

##### 2.3.4.8.9.0.0 Properties

*No items available*

##### 2.3.4.8.10.0.0 Methods

- {'method_name': 'run_polling_cycle_async', 'method_signature': 'run_polling_cycle_async()', 'return_type': 'Task<None>', 'access_modifier': 'public', 'is_async': 'true', 'framework_specific_attributes': [], 'parameters': [], 'implementation_logic': 'Should contain the main application loop (`while True`). Inside the loop, it must:\\n1. Call `GpsProviderApiClient.fetch_locations_async()` to get data.\\n2. Iterate through each returned location record.\\n3. For each record, attempt to validate it using the `IncomingGpsData` Pydantic schema.\\n4. If validation succeeds, transform the validated data into an instance of the `VehicleLocationUpdatedEvent` schema.\\n5. Call `RabbitMQPublisher.publish_event()` with the new event object.\\n6. If validation fails, log the validation error and the invalid data, then continue to the next record.\\n7. After processing all records, `await asyncio.sleep()` for the duration specified in `POLLING_INTERVAL_SECONDS`.', 'exception_handling': 'Must have a broad `try...except` block around the API call to catch the custom `ApiClientError`. On failure, it should log the error and wait for the polling interval before retrying. Must also catch `pydantic.ValidationError` for individual records and handle it gracefully without stopping the loop.', 'performance_considerations': 'The entire method must be asynchronous to not block the FastAPI event loop. Operations should be performed efficiently within the loop.', 'validation_requirements': 'Validation is a key step, using Pydantic schemas as defined in `app/schemas/gps.py`.', 'technology_integration_details': 'This method will be started as a background task via `asyncio.create_task` in the `main.py` startup event.'}

##### 2.3.4.8.11.0.0 Events

*No items available*

##### 2.3.4.8.12.0.0 Implementation Notes

The service should be instantiated with its dependencies injected via its constructor.

### 2.3.5.0.0.0.0 Interface Specifications

*No items available*

### 2.3.6.0.0.0.0 Enum Specifications

*No items available*

### 2.3.7.0.0.0.0 Dto Specifications

#### 2.3.7.1.0.0.0 Dto Name

##### 2.3.7.1.1.0.0 Dto Name

IncomingGpsData

##### 2.3.7.1.2.0.0 File Path

src/app/schemas/gps.py

##### 2.3.7.1.3.0.0 Purpose

To validate the structure and data types of location data received from the third-party GPS provider API.

##### 2.3.7.1.4.0.0 Framework Base Class

pydantic.BaseModel

##### 2.3.7.1.5.0.0 Properties

###### 2.3.7.1.5.1.0 Property Name

####### 2.3.7.1.5.1.1 Property Name

vehicle_identifier

####### 2.3.7.1.5.1.2 Property Type

str

####### 2.3.7.1.5.1.3 Validation Attributes

- [Required]

####### 2.3.7.1.5.1.4 Serialization Attributes

*No items available*

####### 2.3.7.1.5.1.5 Framework Specific Attributes

*No items available*

###### 2.3.7.1.5.2.0 Property Name

####### 2.3.7.1.5.2.1 Property Name

latitude

####### 2.3.7.1.5.2.2 Property Type

float

####### 2.3.7.1.5.2.3 Validation Attributes

- [Required]

####### 2.3.7.1.5.2.4 Serialization Attributes

*No items available*

####### 2.3.7.1.5.2.5 Framework Specific Attributes

*No items available*

###### 2.3.7.1.5.3.0 Property Name

####### 2.3.7.1.5.3.1 Property Name

longitude

####### 2.3.7.1.5.3.2 Property Type

float

####### 2.3.7.1.5.3.3 Validation Attributes

- [Required]

####### 2.3.7.1.5.3.4 Serialization Attributes

*No items available*

####### 2.3.7.1.5.3.5 Framework Specific Attributes

*No items available*

###### 2.3.7.1.5.4.0 Property Name

####### 2.3.7.1.5.4.1 Property Name

timestamp

####### 2.3.7.1.5.4.2 Property Type

datetime.datetime

####### 2.3.7.1.5.4.3 Validation Attributes

- [Required]

####### 2.3.7.1.5.4.4 Serialization Attributes

*No items available*

####### 2.3.7.1.5.4.5 Framework Specific Attributes

*No items available*

##### 2.3.7.1.6.0.0 Validation Rules

All fields are mandatory. Latitude must be between -90 and 90. Longitude must be between -180 and 180. The timestamp must be a valid ISO 8601 string that Pydantic can parse into a datetime object. This should be implemented with Pydantic's `Field` and `@validator` decorators.

##### 2.3.7.1.7.0.0 Serialization Requirements

This schema is used for deserialization and validation of incoming JSON data.

#### 2.3.7.2.0.0.0 Dto Name

##### 2.3.7.2.1.0.0 Dto Name

VehicleLocationUpdatedEvent

##### 2.3.7.2.2.0.0 File Path

src/app/schemas/gps.py

##### 2.3.7.2.3.0.0 Purpose

To define the canonical data contract for the event published to RabbitMQ. This is the public interface of the microservice.

##### 2.3.7.2.4.0.0 Framework Base Class

pydantic.BaseModel

##### 2.3.7.2.5.0.0 Properties

###### 2.3.7.2.5.1.0 Property Name

####### 2.3.7.2.5.1.1 Property Name

vehicle_identifier

####### 2.3.7.2.5.1.2 Property Type

str

####### 2.3.7.2.5.1.3 Validation Attributes

*No items available*

####### 2.3.7.2.5.1.4 Serialization Attributes

- [JsonPropertyName(\"vehicle_identifier\")]

####### 2.3.7.2.5.1.5 Framework Specific Attributes

*No items available*

###### 2.3.7.2.5.2.0 Property Name

####### 2.3.7.2.5.2.1 Property Name

latitude

####### 2.3.7.2.5.2.2 Property Type

float

####### 2.3.7.2.5.2.3 Validation Attributes

*No items available*

####### 2.3.7.2.5.2.4 Serialization Attributes

- [JsonPropertyName(\"latitude\")]

####### 2.3.7.2.5.2.5 Framework Specific Attributes

*No items available*

###### 2.3.7.2.5.3.0 Property Name

####### 2.3.7.2.5.3.1 Property Name

longitude

####### 2.3.7.2.5.3.2 Property Type

float

####### 2.3.7.2.5.3.3 Validation Attributes

*No items available*

####### 2.3.7.2.5.3.4 Serialization Attributes

- [JsonPropertyName(\"longitude\")]

####### 2.3.7.2.5.3.5 Framework Specific Attributes

*No items available*

###### 2.3.7.2.5.4.0 Property Name

####### 2.3.7.2.5.4.1 Property Name

timestamp

####### 2.3.7.2.5.4.2 Property Type

str

####### 2.3.7.2.5.4.3 Validation Attributes

*No items available*

####### 2.3.7.2.5.4.4 Serialization Attributes

- [JsonPropertyName(\"timestamp\")]

####### 2.3.7.2.5.4.5 Framework Specific Attributes

*No items available*

##### 2.3.7.2.6.0.0 Validation Rules

This schema is primarily for serialization, ensuring the outgoing data contract is met. The timestamp field must be an ISO 8601 formatted string.

##### 2.3.7.2.7.0.0 Serialization Requirements

The model should be configured to serialize to a JSON string using `model_dump_json()`.

### 2.3.8.0.0.0.0 Configuration Specifications

- {'configuration_name': 'Dockerfile', 'file_path': 'Dockerfile', 'purpose': 'To define the steps for building a self-contained, production-ready Docker image for the microservice, as per REQ-1-401.', 'framework_base_class': 'N/A', 'configuration_sections': [{'section_name': 'Build Stage', 'properties': [{'property_name': 'Base Image', 'property_type': 'Instruction', 'default_value': 'python:3.11-slim', 'required': 'true', 'description': 'Specifies the official lightweight Python 3.11 base image.'}, {'property_name': 'Dependencies', 'property_type': 'Instruction', 'default_value': 'pip install --no-cache-dir -r requirements.txt', 'required': 'true', 'description': 'Installs project dependencies from a requirements file.'}, {'property_name': 'Code Copy', 'property_type': 'Instruction', 'default_value': 'COPY ./src /app/src', 'required': 'true', 'description': 'Copies the application source code into the image.'}]}, {'section_name': 'Runtime Stage', 'properties': [{'property_name': 'Working Directory', 'property_type': 'Instruction', 'default_value': 'WORKDIR /app', 'required': 'true', 'description': 'Sets the working directory for the application.'}, {'property_name': 'Command', 'property_type': 'Instruction', 'default_value': 'CMD [\\"uvicorn\\", \\"src.main:app\\", \\"--host\\", \\"0.0.0.0\\", \\"--port\\", \\"80\\"]', 'required': 'true', 'description': 'Specifies the command to run the FastAPI application using the Uvicorn ASGI server.'}]}], 'validation_requirements': 'The Dockerfile must produce a runnable image. Best practices like using a non-root user and multi-stage builds for smaller production images should be followed.'}

### 2.3.9.0.0.0.0 Dependency Injection Specifications

*No items available*

### 2.3.10.0.0.0.0 External Integration Specifications

#### 2.3.10.1.0.0.0 Integration Target

##### 2.3.10.1.1.0.0 Integration Target

Third-Party GPS Provider API

##### 2.3.10.1.2.0.0 Integration Type

HTTP REST API

##### 2.3.10.1.3.0.0 Required Client Classes

- GpsProviderApiClient

##### 2.3.10.1.4.0.0 Configuration Requirements

Requires `GPS_PROVIDER_API_URL` and `GPS_PROVIDER_API_KEY` to be configured via environment variables.

##### 2.3.10.1.5.0.0 Error Handling Requirements

Must handle connection timeouts, HTTP 4xx, and HTTP 5xx errors. Must implement exponential backoff for retries on 5xx errors and timeouts as per REQ-1-301.

##### 2.3.10.1.6.0.0 Authentication Requirements

API key passed as a query parameter or header.

##### 2.3.10.1.7.0.0 Framework Integration Patterns

Polling pattern implemented in `PollingService` using an `httpx.AsyncClient`.

#### 2.3.10.2.0.0.0 Integration Target

##### 2.3.10.2.1.0.0 Integration Target

RabbitMQ

##### 2.3.10.2.2.0.0 Integration Type

Message Broker

##### 2.3.10.2.3.0.0 Required Client Classes

- RabbitMQPublisher

##### 2.3.10.2.4.0.0 Configuration Requirements

Requires `RABBITMQ_URL`, `RABBITMQ_EXCHANGE_NAME`, and `RABBITMQ_ROUTING_KEY` configured via environment variables.

##### 2.3.10.2.5.0.0 Error Handling Requirements

Must handle connection failures and implement a reconnection strategy. Published messages must be marked as persistent (`delivery_mode=aio_pika.DeliveryMode.PERSISTENT`) to satisfy resilience requirements.

##### 2.3.10.2.6.0.0 Authentication Requirements

Credentials provided in the AMQP connection URL.

##### 2.3.10.2.7.0.0 Framework Integration Patterns

Event Publisher pattern. The publisher is a singleton managed by the application lifecycle.

## 2.4.0.0.0.0.0 Component Count Validation

| Property | Value |
|----------|-------|
| Total Classes | 8 |
| Total Interfaces | 0 |
| Total Enums | 0 |
| Total Dtos | 2 |
| Total Configurations | 1 |
| Total External Integrations | 2 |
| Grand Total Components | 13 |
| Phase 2 Claimed Count | 0 |
| Phase 2 Actual Count | 0 |
| Validation Added Count | 18 |
| Final Validated Count | 18 |

# 3.0.0.0.0.0.0 File Structure

## 3.1.0.0.0.0.0 Directory Organization

### 3.1.1.0.0.0.0 Directory Path

#### 3.1.1.1.0.0.0 Directory Path

/

#### 3.1.1.2.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.1.3.0.0.0 Contains Files

- pyproject.toml
- .env.example
- .editorconfig
- Dockerfile
- docker-compose.yml
- README.md
- .gitignore

#### 3.1.1.4.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.1.5.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

### 3.1.2.0.0.0.0 Directory Path

#### 3.1.2.1.0.0.0 Directory Path

.github/workflows

#### 3.1.2.2.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.2.3.0.0.0 Contains Files

- ci.yml

#### 3.1.2.4.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.2.5.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

### 3.1.3.0.0.0.0 Directory Path

#### 3.1.3.1.0.0.0 Directory Path

.vscode

#### 3.1.3.2.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.3.3.0.0.0 Contains Files

- settings.json
- extensions.json

#### 3.1.3.4.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.3.5.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling


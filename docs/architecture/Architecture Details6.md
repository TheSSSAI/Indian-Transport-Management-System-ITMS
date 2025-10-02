# 1 Style

Hybrid

# 2 Patterns

## 2.1 Modular Monolith (Odoo Addon)

### 2.1.1 Name

Modular Monolith (Odoo Addon)

### 2.1.2 Description

The core application logic is encapsulated within a custom, installable module (addon) for the Odoo 18 framework. This leverages Odoo's existing architecture (ORM, views, business logic layers) while organizing TMS-specific features into a cohesive but modular unit. (REQ-1-002, REQ-1-013)

### 2.1.3 Benefits

- Rapid development by leveraging a mature framework.
- Simplified deployment and management for core business logic.
- Consistent user experience by adhering to Odoo's UI conventions.
- Built-in support for users, roles, and data persistence.

### 2.1.4 Tradeoffs

- Tightly coupled to the Odoo framework and its versioning.
- Scaling is monolithic; the entire Odoo application must be scaled together.
- Performance of the core application can be impacted by high-volume, non-core tasks.

### 2.1.5 Applicability

#### 2.1.5.1 Scenarios

- Extending an existing ERP system with new, domain-specific functionality.
- Applications where core business logic is complex but transactional volume is manageable.
- Systems where leveraging an existing user and data management framework is a priority.

#### 2.1.5.2 Constraints

- An Odoo 18 Enterprise Edition environment must be available.
- Development must adhere to Odoo's module structure and API.

## 2.2.0.0 Microservice

### 2.2.1.0 Name

Microservice

### 2.2.2.0 Description

A single, decoupled microservice is used specifically for the high-volume task of ingesting real-time GPS location data. This isolates the performance-intensive data polling and processing from the core Odoo application. (REQ-1-013, REQ-1-401, REQ-1-301)

### 2.2.3.0 Benefits

- Isolates high-frequency operations, preventing performance degradation of the core application.
- Allows for independent scaling of the GPS ingestion component based on its specific load.
- Enables use of the best-fit technology (FastAPI) for a specific, focused task.
- Increases overall system resilience; a failure in the microservice does not bring down the entire TMS.

### 2.2.4.0 Tradeoffs

- Increases operational complexity (deployment, monitoring, management of a separate service).
- Introduces network latency and potential points of failure in communication (e.g., message queue).
- Requires data consistency management between the service and the monolith.

### 2.2.5.0 Applicability

#### 2.2.5.1 Scenarios

- Handling high-throughput, real-time data streams.
- Offloading specific, resource-intensive tasks from a primary monolithic application.
- Integrating with third-party APIs that have high polling frequency requirements.

#### 2.2.5.2 Constraints

- Requires a container orchestration platform (EKS) and a message broker (RabbitMQ).

## 2.3.0.0 Event-Driven Integration

### 2.3.1.0 Name

Event-Driven Integration

### 2.3.2.0 Description

Communication from the GPS microservice to the Odoo application is asynchronous, utilizing a RabbitMQ message queue. The microservice publishes location data as events, and Odoo consumes them, decoupling the two components. (REQ-1-301)

### 2.3.3.0 Benefits

- Decouples the producer (microservice) and consumer (Odoo), allowing them to operate and fail independently.
- Improves system scalability and elasticity by buffering requests.
- Enhances resilience through features like dead-letter queues (DLQ) for failed messages.

### 2.3.4.0 Tradeoffs

- Introduces eventual consistency for GPS data.
- Requires management and monitoring of a message broker.
- Adds complexity to debugging and tracing data flow.

### 2.3.5.0 Applicability

#### 2.3.5.1 Scenarios

- Asynchronous data transfer between loosely coupled services.
- Buffering high-volume data writes to a transactional system.
- Implementing background processing tasks.

#### 2.3.5.2 Constraints

- End-to-end latency must be acceptable for the business requirement (e.g., < 10 seconds per REQ-1-501).

# 3.0.0.0 Layers

## 3.1.0.0 Odoo Presentation Layer

### 3.1.1.0 Id

presentation-layer

### 3.1.2.0 Name

Odoo Presentation Layer

### 3.1.3.0 Description

Handles all user interaction and data visualization. It uses Odoo's native view system for standard interfaces and the OWL framework for custom, dynamic components like the Driver Portal.

### 3.1.4.0 Technologystack

Odoo 18 Views (XML for Form, List, Kanban, Map), OWL 2.0 Framework, JavaScript, CSS

### 3.1.5.0 Language

XML, JavaScript

### 3.1.6.0 Type

🔹 Presentation

### 3.1.7.0 Responsibilities

- Rendering master data forms (Vehicle, Driver, Customer). REQ-1-003
- Displaying trip management interfaces. REQ-1-004
- Providing a responsive UI for mobile web browsers. REQ-1-001
- Implementing a simplified, custom Driver Portal with large touch targets. REQ-1-112, REQ-1-300
- Visualizing real-time vehicle locations on a map view. REQ-1-105
- Presenting dashboards and filterable reports. REQ-1-009, REQ-1-601

### 3.1.8.0 Components

- Master Data CRUD Views
- Trip Management Kanban & Form Views
- Driver Portal (OWL Component)
- Map View Widget
- Dashboard Widgets
- Report Views

### 3.1.9.0 Dependencies

- {'layerId': 'business-logic-layer', 'type': 'Required'}

## 3.2.0.0 Odoo Business Logic Layer (Models & Controllers)

### 3.2.1.0 Id

business-logic-layer

### 3.2.2.0 Name

Odoo Business Logic Layer (Models & Controllers)

### 3.2.3.0 Description

The core of the TMS addon, containing all business rules, domain logic, and workflows. It extends Odoo's base models and creates new ones to implement the TMS functionality.

### 3.2.4.0 Technologystack

Odoo 18, Python 3.11

### 3.2.5.0 Language

Python

### 3.2.6.0 Type

🔹 BusinessLogic

### 3.2.7.0 Responsibilities

- Implementing the Trip lifecycle state machine. REQ-1-103, REQ-1-904
- Enforcing Role-Based Access Control (RBAC) via security groups and record rules. REQ-1-008, REQ-1-643
- Handling trip creation and expense approval workflows. REQ-1-102, REQ-1-108
- Calculating trip and vehicle profitability. REQ-1-111, REQ-1-54
- Executing scheduled jobs for alerts (document expiry, license expiry). REQ-1-660, REQ-1-663
- Implementing business validation rules (e.g., vehicle capacity, expired license, odometer reading). REQ-1-901, REQ-1-902, REQ-1-903
- Integrating with the GSP for e-invoicing. REQ-1-006

### 3.2.8.0 Components

- Trip Model (`tms.trip`)
- Vehicle Model (`tms.vehicle`)
- Extended Employee Model (`hr.employee`)
- Extended Partner Model (`res.partner`)
- Expense Model (`tms.expense`)
- Invoice Model (`account.move`)
- Scheduled Actions/Cron Jobs
- Security Rule Definitions (`ir.rule`)

### 3.2.9.0 Dependencies

#### 3.2.9.1 Required

##### 3.2.9.1.1 Layer Id

data-access-layer

##### 3.2.9.1.2 Type

🔹 Required

#### 3.2.9.2.0 Required

##### 3.2.9.2.1 Layer Id

integration-messaging-layer

##### 3.2.9.2.2 Type

🔹 Required

## 3.3.0.0.0 Odoo Data Access Layer

### 3.3.1.0.0 Id

data-access-layer

### 3.3.2.0.0 Name

Odoo Data Access Layer

### 3.3.3.0.0 Description

Abstracts the database interactions using Odoo's built-in Object-Relational Mapper (ORM). All data operations (CRUD) for the TMS models are performed through this layer.

### 3.3.4.0.0 Technologystack

Odoo 18 ORM

### 3.3.5.0.0 Language

Python

### 3.3.6.0.0 Type

🔹 DataAccess

### 3.3.7.0.0 Responsibilities

- Managing database schema for custom TMS models.
- Providing an API for creating, reading, updating, and deleting records.
- Ensuring data integrity through model constraints and relationships.
- Translating Python method calls into SQL queries for the PostgreSQL database.

### 3.3.8.0.0 Dependencies

- {'layerId': 'infrastructure-layer', 'type': 'Required'}

## 3.4.0.0.0 GPS Ingestion Microservice

### 3.4.1.0.0 Id

gps-microservice

### 3.4.2.0.0 Name

GPS Ingestion Microservice

### 3.4.3.0.0 Description

A standalone, lightweight service responsible for fetching GPS data from a third-party provider and publishing it for consumption by the Odoo application.

### 3.4.4.0.0 Technologystack

Python 3.11, FastAPI

### 3.4.5.0.0 Language

Python

### 3.4.6.0.0 Type

🔹 ApplicationServices

### 3.4.7.0.0 Responsibilities

- Polling the third-party GPS provider's API for location data. REQ-1-301
- Validating incoming data against a predefined contract.
- Publishing validated location data to a RabbitMQ message queue.
- Implementing robust error handling, including exponential backoff for API polling and a dead-letter queue (DLQ).
- Being packaged as a self-contained Docker image. REQ-1-401

### 3.4.8.0.0 Components

- API Polling Client
- Data Validation Module
- RabbitMQ Publisher
- Error Handling & Retry Logic

### 3.4.9.0.0 Dependencies

- {'layerId': 'integration-messaging-layer', 'type': 'Required'}

## 3.5.0.0.0 Integration & Messaging Layer

### 3.5.1.0.0 Id

integration-messaging-layer

### 3.5.2.0.0 Name

Integration & Messaging Layer

### 3.5.3.0.0 Description

Facilitates communication between the Odoo application, the GPS microservice, and external services like the GSP.

### 3.5.4.0.0 Technologystack

RabbitMQ (Amazon MQ), REST/HTTP

### 3.5.5.0.0 Language

N/A

### 3.5.6.0.0 Type

🔹 Messaging

### 3.5.7.0.0 Responsibilities

- Receiving and queuing GPS location messages from the microservice. REQ-1-301
- Providing a message consumption mechanism within Odoo to process GPS data.
- Handling synchronous and asynchronous (via background jobs) API calls to the GSP for e-invoice generation. REQ-1-302

### 3.5.8.0.0 Components

- RabbitMQ Message Queue
- RabbitMQ Consumer (Odoo Scheduled Action)
- GSP REST API Client
- Odoo Background Job Queue

## 3.6.0.0.0 Infrastructure & Operations Layer

### 3.6.1.0.0 Id

infrastructure-layer

### 3.6.2.0.0 Name

Infrastructure & Operations Layer

### 3.6.3.0.0 Description

The underlying cloud infrastructure on which the entire system is deployed, managed, and monitored. Defined as code for reproducibility.

### 3.6.4.0.0 Technologystack

AWS (EKS, RDS, S3, API Gateway, Secrets Manager), Docker, Terraform, Nginx, Prometheus, Grafana, Fluentbit, OpenSearch

### 3.6.5.0.0 Language

HCL, YAML

### 3.6.6.0.0 Type

🔹 Infrastructure

### 3.6.7.0.0 Responsibilities

- Hosting the containerized Odoo and Microservice applications on Amazon EKS. REQ-1-014
- Providing a managed PostgreSQL 16 database via Amazon RDS.
- Storing file attachments (receipts, PODs) securely on Amazon S3.
- Managing sensitive credentials and API keys using AWS Secrets Manager. REQ-1-503
- Orchestrating deployment and infrastructure changes via Terraform and GitHub Actions. REQ-1-402
- Collecting and centralizing logs (Fluentbit to OpenSearch) and metrics (Prometheus). REQ-1-602
- Providing visualization and alerting capabilities (Grafana, Alertmanager).

## 3.7.0.0.0 Cross-Cutting Concerns

### 3.7.1.0.0 Id

cross-cutting-layer

### 3.7.2.0.0 Name

Cross-Cutting Concerns

### 3.7.3.0.0 Description

Concerns that apply across multiple layers of the application.

### 3.7.4.0.0 Technologystack

Odoo Framework, Pytest, AWS Services

### 3.7.5.0.0 Language

Python

### 3.7.6.0.0 Type

🔹 CrossCutting

### 3.7.7.0.0 Responsibilities

- Implementing an immutable audit trail for key models. REQ-1-207
- Enforcing code quality and test coverage (>80%) via CI/CD pipelines. REQ-1-504
- Writing logs in a structured JSON format for centralized collection. REQ-1-680
- Centralized configuration and secrets management. REQ-1-503


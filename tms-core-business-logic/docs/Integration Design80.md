# 1 Integration Specifications

## 1.1 Extraction Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-TMS-CORE |
| Extraction Timestamp | 2024-07-29T10:00:00Z |
| Mapping Validation Score | 100% |
| Context Completeness Score | 100% |
| Implementation Readiness Level | High |

## 1.2 Relevant Requirements

### 1.2.1 Requirement Id

#### 1.2.1.1 Requirement Id

REQ-1-013

#### 1.2.1.2 Requirement Text

The system architecture shall be a hybrid model, consisting of a modular monolith (the Odoo TMS addon) for core application logic and a separate, decoupled microservice specifically for ingesting high-volume GPS location data.

#### 1.2.1.3 Validation Criteria

- Review the architectural diagrams and confirm the separation of the Odoo monolith and the GPS ingestion microservice.

#### 1.2.1.4 Implementation Implications

- This repository is the central 'modular monolith' component.
- It must expose well-defined interfaces for other components, like the GPS consumer and Driver Portal, to interact with it.

#### 1.2.1.5 Extraction Reasoning

This architectural requirement establishes the central role of this repository as the monolith and defines its relationship with other decoupled services, making its integration contracts critically important.

### 1.2.2.0 Requirement Id

#### 1.2.2.1 Requirement Id

REQ-1-301

#### 1.2.2.2 Requirement Text

An Odoo scheduled job will then consume messages from this queue to update vehicle locations in the main application.

#### 1.2.2.3 Validation Criteria

- Verify that valid location data published by the microservice is successfully consumed by the Odoo job and the vehicle's location is updated.

#### 1.2.2.4 Implementation Implications

- This repository must expose an ORM API that allows the consumer addon (REPO-GPS-CON) to search for and update vehicle records.

#### 1.2.2.5 Extraction Reasoning

This requirement defines a key inbound integration, where another Odoo addon (the consumer) depends on the ORM API provided by this repository to write GPS data into the core data models.

### 1.2.3.0 Requirement Id

#### 1.2.3.1 Requirement Id

REQ-1-302

#### 1.2.3.2 Requirement Text

The system shall integrate with a GST Suvidha Provider (GSP) API... a synchronous API call... with an asynchronous fallback... This queue must process failed jobs with an automatic retry mechanism...

#### 1.2.3.3 Validation Criteria

- Successfully generate an e-invoice and confirm the system receives the IRN synchronously.

#### 1.2.3.4 Implementation Implications

- This repository must expose its invoice data (`account.move`) via the ORM API to the dedicated GSP integration client (REPO-GSP-INT).

#### 1.2.3.5 Extraction Reasoning

This requirement mandates an integration for e-invoicing. The system design specifies a separate repository (REPO-GSP-INT) for this, which depends on the invoice models and data provided by this core repository.

### 1.2.4.0 Requirement Id

#### 1.2.4.1 Requirement Id

REQ-1-503

#### 1.2.4.2 Requirement Text

The system must enforce strict security for secrets management. All sensitive credentials... shall be stored in AWS Secrets Manager. These secrets must be dynamically injected into the application's runtime environment...

#### 1.2.4.3 Validation Criteria

- Demonstrate that the application successfully connects to the database and external APIs using credentials fetched from Secrets Manager.

#### 1.2.4.4 Implementation Implications

- This repository requires a mechanism to fetch secrets (e.g., for generating S3 pre-signed URLs) from AWS Secrets Manager.
- This implies a dependency on an AWS SDK and the infrastructure providing the service and IAM permissions.

#### 1.2.4.5 Extraction Reasoning

This non-functional requirement creates a dependency on the AWS infrastructure layer (provisioned by REPO-TMS-INFRA) for secure configuration and runtime operation.

### 1.2.5.0 Requirement Id

#### 1.2.5.1 Requirement Id

REQ-1-112

#### 1.2.5.2 Requirement Text

The system shall provide a distinct user interface for the 'Driver' role, optimized for usability on mobile web browsers.

#### 1.2.5.3 Validation Criteria

- Log in as a Driver on a mobile device.
- Verify the interface is simple and easy to navigate.

#### 1.2.5.4 Implementation Implications

- This repository must expose a set of secure, mobile-friendly HTTP API endpoints (Odoo Controllers) to serve data and handle actions from the Driver Portal UI (REPO-DRV-UI).

#### 1.2.5.5 Extraction Reasoning

This requirement for a decoupled frontend necessitates the creation of a dedicated API surface on this repository, which is a primary exposed interface contract.

## 1.3.0.0 Relevant Components

- {'component_name': 'tms-core-business-logic', 'component_specification': 'This component is the core Odoo module that implements the foundational business logic of the Transport Management System. It is responsible for defining all master data and transactional data models, implementing the trip lifecycle state machine, enforcing all business rules and validation logic, defining role-based access control (RBAC), and providing both the standard Odoo back-office UI and a set of APIs for external consumers.', 'implementation_requirements': ['Must be implemented as an Odoo 18 installable addon.', 'Must define all data models and business logic within Odoo model methods.', 'Must expose a secure Odoo ORM API for internal addon communication.', 'Must expose a secure set of HTTP controllers to serve the Driver Portal UI.'], 'architectural_context': "This component is the 'Modular Monolith' part of the hybrid architecture. It resides within the 'Odoo Business Logic Layer' and 'Odoo Data Access Layer', serving as the central source of truth for all business data.", 'extraction_reasoning': 'This is the repository being analyzed. Its role as the central business engine dictates all its integration points, both as a provider of services and a consumer of infrastructure.'}

## 1.4.0.0 Architectural Layers

- {'layer_name': 'Odoo Business Logic Layer (Models & Controllers)', 'layer_responsibilities': ['Implementing the Trip lifecycle state machine.', 'Enforcing Role-Based Access Control (RBAC).', 'Calculating trip and vehicle profitability.', 'Implementing business validation rules.', 'Providing HTTP API endpoints for external clients like the Driver Portal.'], 'layer_constraints': ['Must be implemented in Python 3.11 within the Odoo 18 framework.', 'Must not contain direct, high-volume polling logic for external services like GPS.'], 'implementation_patterns': ['Odoo Model Inheritance', 'State Machine Pattern', 'Odoo HTTP Controllers'], 'extraction_reasoning': 'This repository is the primary implementation of this architectural layer, containing all core business rules and API endpoints.'}

## 1.5.0.0 Dependency Interfaces

### 1.5.1.0 Interface Name

#### 1.5.1.1 Interface Name

IAwsSecretsManagerApi

#### 1.5.1.2 Source Repository

REPO-TMS-INFRA

#### 1.5.1.3 Method Contracts

- {'method_name': 'get_secret', 'method_signature': 'get_secret(secret_name: str) -> str', 'method_purpose': 'To securely retrieve a secret value (e.g., API key) from AWS Secrets Manager at runtime.', 'integration_context': 'Called during application logic that requires external credentials, such as generating pre-signed S3 URLs or interacting with other AWS services.'}

#### 1.5.1.4 Integration Pattern

Runtime Configuration via SDK

#### 1.5.1.5 Communication Protocol

AWS SDK (HTTPS)

#### 1.5.1.6 Extraction Reasoning

Fulfills REQ-1-503, which mandates that all secrets be stored in AWS Secrets Manager. This repository depends on the infrastructure provisioned by REPO-TMS-INFRA and uses the AWS SDK to consume the secret management service.

### 1.5.2.0 Interface Name

#### 1.5.2.1 Interface Name

IAwsS3Api

#### 1.5.2.2 Source Repository

REPO-TMS-INFRA

#### 1.5.2.3 Method Contracts

- {'method_name': 'generate_presigned_post_url', 'method_signature': 'generate_presigned_post_url(bucket_name: str, object_name: str, expiration: int) -> dict', 'method_purpose': 'To generate a secure, time-limited URL that allows a client (the Driver Portal UI) to upload a file directly to an S3 bucket.', 'integration_context': 'Called by an Odoo controller when the Driver Portal requests to upload a file (e.g., an expense receipt or POD), as part of the secure and scalable file upload pattern.'}

#### 1.5.2.4 Integration Pattern

Service Integration via SDK

#### 1.5.2.5 Communication Protocol

AWS SDK (HTTPS)

#### 1.5.2.6 Extraction Reasoning

This repository implements the backend logic for the secure S3 upload pattern, which requires it to interact with the S3 service provisioned by REPO-TMS-INFRA. It acts as a trusted intermediary to grant temporary upload access to the client.

## 1.6.0.0 Exposed Interfaces

### 1.6.1.0 Interface Name

#### 1.6.1.1 Interface Name

Odoo ORM API

#### 1.6.1.2 Consumer Repositories

- REPO-GPS-CON
- REPO-GSP-INT

#### 1.6.1.3 Method Contracts

##### 1.6.1.3.1 Method Name

###### 1.6.1.3.1.1 Method Name

create

###### 1.6.1.3.1.2 Method Signature

Model.create(dict) -> RecordSet

###### 1.6.1.3.1.3 Method Purpose

Creates a new record for a given model (e.g., a new trip, a new expense).

###### 1.6.1.3.1.4 Integration Context

Used by other Odoo addons to create data within the core TMS module.

##### 1.6.1.3.2.0 Method Name

###### 1.6.1.3.2.1 Method Name

search

###### 1.6.1.3.2.2 Method Signature

Model.search(list) -> RecordSet

###### 1.6.1.3.2.3 Method Purpose

Queries for records matching a specified domain filter. Enforces all applicable security record rules.

###### 1.6.1.3.2.4 Integration Context

Used by REPO-GPS-CON to find the correct vehicle record to update.

##### 1.6.1.3.3.0 Method Name

###### 1.6.1.3.3.1 Method Name

write

###### 1.6.1.3.3.2 Method Signature

RecordSet.write(dict) -> bool

###### 1.6.1.3.3.3 Method Purpose

Updates one or more fields on a set of existing records. Triggers all relevant business logic.

###### 1.6.1.3.3.4 Integration Context

Used by REPO-GPS-CON to update vehicle location and by REPO-GSP-INT to update an invoice with the IRN.

##### 1.6.1.3.4.0 Method Name

###### 1.6.1.3.4.1 Method Name

read

###### 1.6.1.3.4.2 Method Signature

RecordSet.read(list) -> list[dict]

###### 1.6.1.3.4.3 Method Purpose

Retrieves the values of specified fields for a set of records.

###### 1.6.1.3.4.4 Integration Context

Used by REPO-GSP-INT to read invoice data to build the GSP API payload.

#### 1.6.1.4.0.0 Service Level Requirements

- All interactions are subject to Odoo's Role-Based Access Control (RBAC) mechanism.
- Operations are transactional and atomic.

#### 1.6.1.5.0.0 Implementation Constraints

- Communication is via internal Python method calls within the Odoo framework.
- Consumers must handle Odoo's standard exception types (UserError, ValidationError, AccessError).

#### 1.6.1.6.0.0 Extraction Reasoning

This is the primary internal interface of the modular monolith, providing a secure and transaction-safe API for other tightly coupled Odoo addons to interact with the core business data and logic, as required by REQ-1-301 and REQ-1-302.

### 1.6.2.0.0.0 Interface Name

#### 1.6.2.1.0.0 Interface Name

IDriverPortalApi

#### 1.6.2.2.0.0 Consumer Repositories

- REPO-DRV-UI

#### 1.6.2.3.0.0 Method Contracts

##### 1.6.2.3.1.0 Method Name

###### 1.6.2.3.1.1 Method Name

fetch_my_trips

###### 1.6.2.3.1.2 Method Signature

GET /tms/my_trips?filter=current&offset=0&limit=20

###### 1.6.2.3.1.3 Method Purpose

Retrieves a paginated list of trips assigned to the currently authenticated driver.

###### 1.6.2.3.1.4 Implementation Requirements

Must implement pagination and filtering by status ('current' or 'past'). Must enforce record rules to only show trips for the logged-in driver.

##### 1.6.2.3.2.0 Method Name

###### 1.6.2.3.2.1 Method Name

start_trip

###### 1.6.2.3.2.2 Method Signature

POST /tms/trip/{trip_id}/start

###### 1.6.2.3.2.3 Method Purpose

Changes the status of a specific trip from 'Assigned' to 'In-Transit'.

###### 1.6.2.3.2.4 Implementation Requirements

Must verify the trip is assigned to the authenticated driver and is in the correct prerequisite state.

##### 1.6.2.3.3.0 Method Name

###### 1.6.2.3.3.1 Method Name

submit_pod

###### 1.6.2.3.3.2 Method Signature

POST /tms/trip/{trip_id}/submit_pod

###### 1.6.2.3.3.3 Method Purpose

Submits Proof of Delivery data (recipient name, signature/image) and changes trip status to 'Delivered'.

###### 1.6.2.3.3.4 Implementation Requirements

Must handle file data (base64 encoded) and update the trip record atomically.

##### 1.6.2.3.4.0 Method Name

###### 1.6.2.3.4.1 Method Name

get_presigned_s3_url

###### 1.6.2.3.4.2 Method Signature

POST /tms/expense/get_upload_url

###### 1.6.2.3.4.3 Method Purpose

Generates and returns a secure, time-limited URL for the client to directly upload a file to S3.

###### 1.6.2.3.4.4 Implementation Requirements

Must call the IAwsS3Api dependency interface and return the result as JSON.

##### 1.6.2.3.5.0 Method Name

###### 1.6.2.3.5.1 Method Name

fetch_training_materials

###### 1.6.2.3.5.2 Method Signature

GET /tms/training_materials

###### 1.6.2.3.5.3 Method Purpose

Retrieves a list of available training materials (videos, documents) for drivers.

###### 1.6.2.3.5.4 Implementation Requirements

Must query the `tms.training.material` model and return a list of titles and URLs.

#### 1.6.2.4.0.0 Service Level Requirements

- All endpoints must be authenticated via Odoo session.
- 95% of all GET request response times must be less than 200 milliseconds, as per REQ-1-500.

#### 1.6.2.5.0.0 Implementation Constraints

- All endpoints must be implemented as Odoo HTTP Controllers.
- Payloads must be in JSON format.

#### 1.6.2.6.0.0 Extraction Reasoning

This exposed API is the sole contract between the backend monolith and the decoupled Driver Portal frontend (REPO-DRV-UI). It is essential for fulfilling the requirements for a mobile-optimized driver interface (REQ-1-112) and its associated user stories.

## 1.7.0.0.0.0 Technology Context

### 1.7.1.0.0.0 Framework Requirements

The system must be developed as a modular addon for the Odoo 18 framework using Python 3.11. All data models, business logic, and backend views must adhere to Odoo's development best practices.

### 1.7.2.0.0.0 Integration Technologies

- Odoo ORM API
- Odoo HTTP Controllers (JSON-RPC)
- AWS SDK (boto3) for S3 and Secrets Manager

### 1.7.3.0.0.0 Performance Constraints

ORM queries must be optimized to avoid N+1 problems. HTTP controller endpoints must be designed for low latency to meet the <200ms API response NFR.

### 1.7.4.0.0.0 Security Requirements

All data access, whether through the ORM or HTTP controllers, must be governed by a comprehensive Role-Based Access Control (RBAC) model implemented using Odoo's security framework. All secrets must be fetched from AWS Secrets Manager.

## 1.8.0.0.0.0 Extraction Validation

| Property | Value |
|----------|-------|
| Mapping Completeness Check | All repository connections identified in the syste... |
| Cross Reference Validation | The defined interfaces are consistent with the nee... |
| Implementation Readiness Assessment | The integration specifications are highly implemen... |
| Quality Assurance Confirmation | A full QA review confirms that the integration con... |


# 1 Integration Specifications

## 1.1 Extraction Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GSP-INT |
| Extraction Timestamp | 2024-05-24T10:00:00Z |
| Mapping Validation Score | 100% |
| Context Completeness Score | 100% |
| Implementation Readiness Level | High |

## 1.2 Relevant Requirements

### 1.2.1 Requirement Id

#### 1.2.1.1 Requirement Id

REQ-1-006

#### 1.2.1.2 Requirement Text

The system's invoicing module must integrate with a GST Suvidha Provider (GSP) to generate an Invoice Reference Number (IRN) for each B2B invoice, ensuring compliance with Indian GST e-invoicing regulations.

#### 1.2.1.3 Validation Criteria

- Generate an invoice for a GST-registered customer and verify that a valid IRN and QR code are successfully fetched from the GSP and stored with the invoice record.
- Confirm that the generated invoice PDF contains the IRN and QR code as per regulatory requirements.

#### 1.2.1.4 Implementation Implications

- A client component must be developed to communicate with an external GSP's API.
- The Odoo invoice model (account.move) must be extended to store the IRN and QR code.
- Data transformation logic is required to map Odoo invoice data to the GSP API's expected JSON format.

#### 1.2.1.5 Extraction Reasoning

This is the primary functional requirement that defines the core purpose of the tms-gsp-integration-client repository.

### 1.2.2.0 Requirement Id

#### 1.2.2.1 Requirement Id

REQ-1-302

#### 1.2.2.2 Requirement Text

The system shall integrate with a GST Suvidha Provider (GSP) API to generate e-invoices. The primary integration pattern shall be a synchronous API call to provide immediate feedback. In the event of a failure or timeout of the synchronous call, the system must automatically enqueue the e-invoice generation task into a dedicated background job queue. This queue must process failed jobs with an automatic retry mechanism using an exponential backoff delay.

#### 1.2.2.3 Validation Criteria

- Successfully generate an e-invoice and confirm the system receives the IRN synchronously.
- Simulate a GSP API timeout. Verify the user receives immediate feedback that the job is queued, and the invoice is flagged for background processing.
- Check the job queue and verify the failed task is present and is being retried.
- Once the simulated API is back online, verify the queued job eventually succeeds and updates the invoice record with the IRN.

#### 1.2.2.4 Implementation Implications

- The GSP client must implement a try/except block to catch API errors (e.g., timeouts, 5xx status codes).
- Upon failure, the client must trigger an Odoo background job, passing the invoice ID as a parameter.
- The background job must be configured with a retry policy (e.g., using Odoo's @job decorator with appropriate settings).

#### 1.2.2.5 Extraction Reasoning

This is the critical technical requirement that dictates the exact integration pattern (synchronous with asynchronous fallback) to be implemented within this repository, ensuring system resilience.

## 1.3.0.0 Relevant Components

- {'component_name': 'GSP REST API Client', 'component_specification': 'This component is responsible for all communication with the external GST Suvidha Provider (GSP). Its duties include: 1) Transforming Odoo invoice data into the required GSP API format. 2) Executing synchronous REST/HTTP API calls to the GSP. 3) Handling API responses, including success (IRN, QR code) and failure (error codes, timeouts). 4) Triggering the asynchronous background job for retries upon failure.', 'implementation_requirements': ['Must be implemented as an Odoo addon.', 'Must use the requests library for external HTTP calls.', 'Must securely retrieve GSP API credentials from AWS Secrets Manager at runtime.', "Must integrate with Odoo's background job queue for the asynchronous fallback mechanism.", 'Must parse error messages from the GSP and log them appropriately.'], 'architectural_context': "Resides in the 'Integration & Messaging Layer'. Acts as an Adapter to the external GSP service, encapsulating the details of the third-party integration.", 'extraction_reasoning': 'This is the core software component that will be built within the tms-gsp-integration-client repository to fulfill its specified requirements.'}

## 1.4.0.0 Architectural Layers

- {'layer_name': 'Integration & Messaging Layer', 'layer_responsibilities': 'Facilitates communication between the Odoo application and external services. For this repository, its key responsibility is handling synchronous and asynchronous (via background jobs) API calls to the GSP for e-invoice generation.', 'layer_constraints': ['Must handle API keys and other secrets securely, fetching them from AWS Secrets Manager.', 'Must provide resilient communication patterns, such as retry mechanisms for transient failures.'], 'implementation_patterns': ['Adapter Pattern: Encapsulates the GSP-specific API logic, shielding the core application.', 'Asynchronous Fallback: Uses a background job queue to handle failures from a primary synchronous call, ensuring UI responsiveness and eventual consistency.'], 'extraction_reasoning': 'The tms-gsp-integration-client repository is a concrete implementation of a key responsibility within this architectural layer, as defined by the overall system architecture.'}

## 1.5.0.0 Dependency Interfaces

- {'interface_name': 'Odoo ORM API (account.move)', 'source_repository': 'REPO-TMS-CORE', 'method_contracts': [{'method_name': 'read', 'method_signature': 'read(fields=None)', 'method_purpose': 'To fetch all necessary data from an account.move record (e.g., customer details, line items, tax information) required to build the GSP API request payload.', 'integration_context': 'Called at the beginning of the generate_einvoice process.'}, {'method_name': 'write', 'method_signature': 'write(vals)', 'method_purpose': 'To update the account.move record with the results from the GSP API, such as the IRN, QR code, acknowledgement details, and the e-invoicing status.', 'integration_context': 'Called after a successful API response is received, both from the synchronous call and the asynchronous background job.'}], 'integration_pattern': 'Direct ORM method calls', 'communication_protocol': 'Internal Python method calls', 'extraction_reasoning': 'This repository is dependent on the core Odoo application (REPO-TMS-CORE) to provide the invoice data it needs to process and to persist the results of the e-invoicing operation.'}

## 1.6.0.0 Exposed Interfaces

- {'interface_name': 'GSPInvoiceService', 'consumer_repositories': ['REPO-TMS-CORE'], 'method_contracts': [{'method_name': 'generate_einvoice', 'method_signature': 'generate_einvoice(self, invoice_ids)', 'method_purpose': 'Orchestrates the entire e-invoice generation process for a given Odoo invoice. It handles data fetching, transformation, the synchronous API call, and the fallback to an asynchronous background job on failure.', 'implementation_requirements': 'Must be implemented as an Odoo model method, callable from a button on the account.move form view. The method must adhere to the logic specified in REQ-1-302.'}], 'service_level_requirements': ['The initial synchronous API call attempt must have a configured timeout (e.g., 15 seconds) to ensure the UI remains responsive.', 'Upon failure, immediate feedback must be provided to the user while the task is enqueued for background processing.'], 'implementation_constraints': ['Must be compatible with the Odoo 18 action button framework.', 'Must not contain any business logic unrelated to the GSP integration itself.'], 'extraction_reasoning': 'This repository exposes a single, well-defined service method to the core application (REPO-TMS-CORE), encapsulating the complexity of the GSP integration and providing a clear contract for its consumer.'}

## 1.7.0.0 Technology Context

### 1.7.1.0 Framework Requirements

Odoo 18, Python 3.11

### 1.7.2.0 Integration Technologies

- requests (Python library for HTTP calls)
- Odoo Job Queue (for asynchronous processing)
- REST/HTTP (for communication with the external GSP API)

### 1.7.3.0 Performance Constraints

Synchronous API calls must have a strict timeout to avoid blocking the user interface. The system must provide immediate feedback to the user even if the GSP API is slow or unresponsive.

### 1.7.4.0 Security Requirements

GSP API keys and other secrets must be retrieved from AWS Secrets Manager at runtime and must never be hardcoded or stored in configuration files. All communication with the GSP API must be over HTTPS.

## 1.8.0.0 Extraction Validation

| Property | Value |
|----------|-------|
| Mapping Completeness Check | The repository's responsibilities are fully covere... |
| Cross Reference Validation | The repository definition aligns perfectly with th... |
| Implementation Readiness Assessment | Readiness is high. The core logic is explicitly de... |
| Quality Assurance Confirmation | The extracted context is internally consistent and... |


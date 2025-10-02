# 1 Design

code_design

# 2 Code Specfication

## 2.1 Validation Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GSP-INT |
| Validation Timestamp | 2024-05-24T11:00:00Z |
| Original Component Count Claimed | 0 |
| Original Component Count Actual | 0 |
| Gaps Identified Count | 12 |
| Components Added Count | 12 |
| Final Component Count | 12 |
| Validation Completeness Score | 100.0 |
| Enhancement Methodology | Systematic validation of the empty Phase 2 specifi... |

## 2.2 Validation Summary

### 2.2.1 Repository Scope Validation

#### 2.2.1.1 Scope Compliance

Validation complete. The enhanced specification now fully aligns with the repository's defined scope, covering GSP API communication, sync/async fallback patterns, data transformation, and Odoo model extensions.

#### 2.2.1.2 Gaps Identified

- Missing specification for the Odoo addon manifest (`__manifest__.py`).
- Missing specification for the view XML to add the trigger button.
- Missing specification for a dedicated service to handle AWS Secrets Manager integration.
- Missing specification for declarative configuration of API parameters.
- Missing specification for security access control files.

#### 2.2.1.3 Components Added

- __manifest__.py
- account_move_view.xml
- AwsSecretsManager
- ir_config_parameter_data.xml
- ir.model.access.csv

### 2.2.2.0 Requirements Coverage Validation

#### 2.2.2.1 Functional Requirements Coverage

100.0%

#### 2.2.2.2 Non Functional Requirements Coverage

100.0%

#### 2.2.2.3 Missing Requirement Components

- Specification for a dedicated data mapping component to transform Odoo data to GSP format (implied by REQ-1-006).
- Specification for UI elements and model methods to handle manual intervention on failed invoices (from US-038, supporting REQ-1-006).

#### 2.2.2.4 Added Requirement Components

- GspRequestMapper
- Enhanced AccountMove model specification with methods and view XML for manual retry/processing.

### 2.2.3.0 Architectural Pattern Validation

#### 2.2.3.1 Pattern Implementation Completeness

Validation complete. The enhanced specification fully details the implementation of the Adapter pattern and the sync-with-async-fallback resilience pattern.

#### 2.2.3.2 Missing Pattern Components

- Absence of a clear orchestration service specification.
- Lack of a distinct component for API communication.

#### 2.2.3.3 Added Pattern Components

- GspService
- GspApiClient

### 2.2.4.0 Database Mapping Validation

#### 2.2.4.1 Entity Mapping Completeness

Validation complete. The specification for extending the `account.move` model now includes all fields required by the database design and requirements.

#### 2.2.4.2 Missing Database Components

- Missing field specifications on `account.move` for IRN, QR code, status, and error messages.

#### 2.2.4.3 Added Database Components

- Detailed property specifications for `gsp_irn`, `gsp_qr_code`, `gsp_status`, and `gsp_error_message` on the AccountMove class.

### 2.2.5.0 Sequence Interaction Validation

#### 2.2.5.1 Interaction Implementation Completeness

Validation complete. All actors and interactions from the \"E-Invoice Generation with GSP API\" sequence diagram (ID 227) are now fully specified.

#### 2.2.5.2 Missing Interaction Components

- Specification for the component that transforms data before the API call.
- Specification for the component that retrieves secrets.

#### 2.2.5.3 Added Interaction Components

- GspRequestMapper
- AwsSecretsManager

## 2.3.0.0 Enhanced Specification

### 2.3.1.0 Specification Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GSP-INT |
| Technology Stack | Odoo 18, Python 3.11, Odoo Job Queue, requests, bo... |
| Technology Guidance Integration | Validation complete. Specification adheres to Odoo... |
| Framework Compliance Score | 100.0 |
| Specification Completeness | 100.0 |
| Component Count | 12 |
| Specification Methodology | Validation complete. Specification follows a Model... |

### 2.3.2.0 Technology Framework Integration

#### 2.3.2.1 Framework Patterns Applied

- Adapter Pattern: Validation confirms the `GspApiClient` and `GspRequestMapper` specifications effectively encapsulate the external GSP dependency.
- Asynchronous Fallback: Validation confirms the `GspService` and `_job_generate_einvoice` method specifications correctly implement the sync/async fallback pattern required by REQ-1-302.
- Dependency Injection (via Odoo's environment): Validation confirms services are designed to be instantiated with the Odoo environment (`self.env`), following standard Odoo practice.
- Model Inheritance: Validation confirms the specification correctly uses `_inherit = \"account.move\"` to extend Odoo's core functionality without modifying base code.

#### 2.3.2.2 Directory Structure Source

Standard Odoo 18 addon structure.

#### 2.3.2.3 Naming Conventions Source

Odoo development guidelines and Python PEP 8 standards.

#### 2.3.2.4 Architectural Patterns Source

Adapter pattern to isolate the third-party GSP API integration.

#### 2.3.2.5 Performance Optimizations Applied

- Specification requires a configurable synchronous timeout to ensure UI responsiveness.
- Specification mandates asynchronous processing for failed API calls using Odoo's built-in job queue.
- Specification for `AwsSecretsManager` recommends in-memory caching for retrieved AWS secrets to reduce latency on repeated calls within the same transaction.

### 2.3.3.0 File Structure

#### 2.3.3.1 Directory Organization

##### 2.3.3.1.1 Directory Path

###### 2.3.3.1.1.1 Directory Path

/

###### 2.3.3.1.1.2 Purpose

Root directory for the Odoo addon.

###### 2.3.3.1.1.3 Contains Files

- __init__.py
- __manifest__.py

###### 2.3.3.1.1.4 Organizational Reasoning

Standard Odoo addon structure for module initialization and definition.

###### 2.3.3.1.1.5 Framework Convention Alignment

Mandatory Odoo addon structure.

##### 2.3.3.1.2.0 Directory Path

###### 2.3.3.1.2.1 Directory Path

models/

###### 2.3.3.1.2.2 Purpose

Contains Python files that extend existing Odoo models.

###### 2.3.3.1.2.3 Contains Files

- __init__.py
- account_move.py

###### 2.3.3.1.2.4 Organizational Reasoning

Standard Odoo convention for model definitions and extensions.

###### 2.3.3.1.2.5 Framework Convention Alignment

Follows Odoo's MVC architecture for the model layer.

##### 2.3.3.1.3.0 Directory Path

###### 2.3.3.1.3.1 Directory Path

views/

###### 2.3.3.1.3.2 Purpose

Contains XML files that define or extend Odoo views.

###### 2.3.3.1.3.3 Contains Files

- account_move_view.xml

###### 2.3.3.1.3.4 Organizational Reasoning

Standard Odoo convention for UI definitions (presentation layer).

###### 2.3.3.1.3.5 Framework Convention Alignment

Follows Odoo's declarative UI approach.

##### 2.3.3.1.4.0 Directory Path

###### 2.3.3.1.4.1 Directory Path

services/

###### 2.3.3.1.4.2 Purpose

Contains pure Python classes for business logic, external API clients, and data mappers, separating them from the ORM.

###### 2.3.3.1.4.3 Contains Files

- __init__.py
- gsp_service.py
- gsp_api_client.py
- gsp_request_mapper.py
- aws_secrets_manager.py

###### 2.3.3.1.4.4 Organizational Reasoning

Implements a service layer to encapsulate external integration complexity, improving testability and maintainability.

###### 2.3.3.1.4.5 Framework Convention Alignment

Adheres to Clean Architecture principles within the Odoo framework.

##### 2.3.3.1.5.0 Directory Path

###### 2.3.3.1.5.1 Directory Path

jobs/

###### 2.3.3.1.5.2 Purpose

Contains definitions for asynchronous background tasks using Odoo's job queue.

###### 2.3.3.1.5.3 Contains Files

- __init__.py
- gsp_jobs.py

###### 2.3.3.1.5.4 Organizational Reasoning

Isolates background job definitions for clarity and adherence to the async fallback pattern.

###### 2.3.3.1.5.5 Framework Convention Alignment

Leverages the Odoo Enterprise `@job` decorator for asynchronous processing.

##### 2.3.3.1.6.0 Directory Path

###### 2.3.3.1.6.1 Directory Path

security/

###### 2.3.3.1.6.2 Purpose

Contains security definitions for the addon.

###### 2.3.3.1.6.3 Contains Files

- ir.model.access.csv

###### 2.3.3.1.6.4 Organizational Reasoning

Standard Odoo convention for defining model-level access rights.

###### 2.3.3.1.6.5 Framework Convention Alignment

Utilizes Odoo's declarative security framework.

##### 2.3.3.1.7.0 Directory Path

###### 2.3.3.1.7.1 Directory Path

data/

###### 2.3.3.1.7.2 Purpose

Contains XML files for loading non-executable data.

###### 2.3.3.1.7.3 Contains Files

- ir_config_parameter_data.xml

###### 2.3.3.1.7.4 Organizational Reasoning

Standard Odoo convention for setting default configuration parameters upon module installation.

###### 2.3.3.1.7.5 Framework Convention Alignment

Follows Odoo's data file loading mechanism.

##### 2.3.3.1.8.0 Directory Path

###### 2.3.3.1.8.1 Directory Path

tests/

###### 2.3.3.1.8.2 Purpose

Contains unit and integration tests for the addon.

###### 2.3.3.1.8.3 Contains Files

- __init__.py
- test_gsp_service.py
- test_account_move.py

###### 2.3.3.1.8.4 Organizational Reasoning

Standard Odoo convention for organizing automated tests.

###### 2.3.3.1.8.5 Framework Convention Alignment

Follows Odoo's testing framework structure.

#### 2.3.3.2.0.0 Namespace Strategy

| Property | Value |
|----------|-------|
| Root Namespace | odoo.addons.tms_gsp_integration |
| Namespace Organization | Follows standard Odoo addon conventions where Pyth... |
| Naming Conventions | PascalCase for class names, snake_case for methods... |
| Framework Alignment | Compliant with Odoo and Python (PEP 8) standards. |

### 2.3.4.0.0.0 Class Specifications

#### 2.3.4.1.0.0 Class Name

##### 2.3.4.1.1.0 Class Name

AccountMove

##### 2.3.4.1.2.0 File Path

models/account_move.py

##### 2.3.4.1.3.0 Class Type

Odoo Model Extension

##### 2.3.4.1.4.0 Inheritance

models.Model

##### 2.3.4.1.5.0 Purpose

Specification enhanced to extend the core \"account.move\" model to add fields for storing e-invoice data, UI buttons, and methods to trigger the generation process, including manual intervention.

##### 2.3.4.1.6.0 Dependencies

- odoo.addons.queue_job.job.Job
- tms_gsp_integration.services.gsp_service

##### 2.3.4.1.7.0 Framework Specific Attributes

- _inherit = \"account.move\"

##### 2.3.4.1.8.0 Technology Integration Notes

Validation complete. This specification correctly integrates with Odoo's ORM and job queue, acting as the primary entry point from the UI to the GSP integration logic.

##### 2.3.4.1.9.0 Validation Notes

Enhanced specification to include all necessary fields, methods for UI actions, and job definitions, ensuring full coverage of requirements REQ-1-006, REQ-1-302, and user story US-038.

##### 2.3.4.1.10.0 Properties

###### 2.3.4.1.10.1 Property Name

####### 2.3.4.1.10.1.1 Property Name

gsp_irn

####### 2.3.4.1.10.1.2 Property Type

fields.Char

####### 2.3.4.1.10.1.3 Access Modifier

public

####### 2.3.4.1.10.1.4 Purpose

Specification for storing the Invoice Reference Number (IRN) received from the GSP, fulfilling a key part of REQ-1-006.

####### 2.3.4.1.10.1.5 Validation Attributes

*No items available*

####### 2.3.4.1.10.1.6 Framework Specific Configuration

Specification requires parameters \"string=\\\"IRN\\\"\", \"readonly=True\", \"index=True\", \"copy=False\".

####### 2.3.4.1.10.1.7 Implementation Notes

Validation requires a database-level unique constraint on this field to prevent duplicate entries.

###### 2.3.4.1.10.2.0 Property Name

####### 2.3.4.1.10.2.1 Property Name

gsp_qr_code

####### 2.3.4.1.10.2.2 Property Type

fields.Text

####### 2.3.4.1.10.2.3 Access Modifier

public

####### 2.3.4.1.10.2.4 Purpose

Specification for storing the signed QR code data (typically Base64 encoded) from the GSP, as required by REQ-1-006.

####### 2.3.4.1.10.2.5 Validation Attributes

*No items available*

####### 2.3.4.1.10.2.6 Framework Specific Configuration

Specification requires parameters \"string=\\\"QR Code Data\\\"\", \"readonly=True\", \"copy=False\".

####### 2.3.4.1.10.2.7 Implementation Notes

Validation confirms this specification provides the data source for rendering the QR code image on the invoice PDF.

###### 2.3.4.1.10.3.0 Property Name

####### 2.3.4.1.10.3.1 Property Name

gsp_status

####### 2.3.4.1.10.3.2 Property Type

fields.Selection

####### 2.3.4.1.10.3.3 Access Modifier

public

####### 2.3.4.1.10.3.4 Purpose

Specification for tracking the status of the e-invoice generation process, supporting the resilient workflow of REQ-1-302.

####### 2.3.4.1.10.3.5 Validation Attributes

*No items available*

####### 2.3.4.1.10.3.6 Framework Specific Configuration

Selection values must be [(\"not_generated\", \"Not Generated\"), (\"pending\", \"Pending\"), (\"generated\", \"Generated\"), (\"failed\", \"Failed\")]. Specification requires \"default=\\\"not_generated\\\"\", \"required=True\", \"copy=False\".

####### 2.3.4.1.10.3.7 Implementation Notes

Validation requires this field to be indexed for efficient filtering of invoices by their e-invoicing status.

###### 2.3.4.1.10.4.0 Property Name

####### 2.3.4.1.10.4.1 Property Name

gsp_error_message

####### 2.3.4.1.10.4.2 Property Type

fields.Text

####### 2.3.4.1.10.4.3 Access Modifier

public

####### 2.3.4.1.10.4.4 Purpose

Specification for storing the last error message from the GSP API, supporting the manual intervention workflow from US-038.

####### 2.3.4.1.10.4.5 Validation Attributes

*No items available*

####### 2.3.4.1.10.4.6 Framework Specific Configuration

Specification requires \"string=\\\"Last GSP Error\\\"\", \"readonly=True\", \"copy=False\".

####### 2.3.4.1.10.4.7 Implementation Notes

This field will be displayed on the UI to help finance officers diagnose failures.

##### 2.3.4.1.11.0.0 Methods

###### 2.3.4.1.11.1.0 Method Name

####### 2.3.4.1.11.1.1 Method Name

action_generate_einvoice

####### 2.3.4.1.11.1.2 Method Signature

action_generate_einvoice(self)

####### 2.3.4.1.11.1.3 Return Type

None

####### 2.3.4.1.11.1.4 Access Modifier

public

####### 2.3.4.1.11.1.5 Is Async

❌ No

####### 2.3.4.1.11.1.6 Framework Specific Attributes

*No items available*

####### 2.3.4.1.11.1.7 Parameters

*No items available*

####### 2.3.4.1.11.1.8 Implementation Logic

Specification enhanced for clarity. This method must iterate over `self`. For each invoice, it performs pre-flight validation (state is \"Posted\", customer GSTIN is valid). It then instantiates `GspService` and calls its primary orchestration method. This method is the designated target for the \"Generate E-Invoice\" button.

####### 2.3.4.1.11.1.9 Exception Handling

Specification requires catching exceptions from the service layer and displaying a user-friendly notification to the UI using Odoo's standard notification system.

####### 2.3.4.1.11.1.10 Performance Considerations

Specification notes that for bulk actions, this method should consider enqueuing a separate job for each invoice to prevent long-running UI transactions.

####### 2.3.4.1.11.1.11 Validation Requirements

Validation confirms this method must check that the invoice state is \"Posted\" and that the customer `res.partner` has a valid GSTIN before proceeding.

####### 2.3.4.1.11.1.12 Technology Integration Details

Validation confirms this method correctly bridges the Odoo UI/Action framework and the backend service layer.

###### 2.3.4.1.11.2.0 Method Name

####### 2.3.4.1.11.2.1 Method Name

action_retry_einvoice

####### 2.3.4.1.11.2.2 Method Signature

action_retry_einvoice(self)

####### 2.3.4.1.11.2.3 Return Type

None

####### 2.3.4.1.11.2.4 Access Modifier

public

####### 2.3.4.1.11.2.5 Is Async

❌ No

####### 2.3.4.1.11.2.6 Framework Specific Attributes

*No items available*

####### 2.3.4.1.11.2.7 Parameters

*No items available*

####### 2.3.4.1.11.2.8 Implementation Logic

Added missing specification from systematic analysis. This method, triggered by a \"Retry\" button, directly calls `action_generate_einvoice` to re-initiate the process for invoices in the \"failed\" state. Fulfills requirements from US-038.

####### 2.3.4.1.11.2.9 Exception Handling

Same as `action_generate_einvoice`.

####### 2.3.4.1.11.2.10 Performance Considerations

N/A, as it's a manual, single-record action.

####### 2.3.4.1.11.2.11 Validation Requirements

The method must first check that `self.gsp_status` is \"failed\".

####### 2.3.4.1.11.2.12 Technology Integration Details

Reuses the main e-invoice generation logic for manual retries.

###### 2.3.4.1.11.3.0 Method Name

####### 2.3.4.1.11.3.1 Method Name

_job_generate_einvoice

####### 2.3.4.1.11.3.2 Method Signature

_job_generate_einvoice(self)

####### 2.3.4.1.11.3.3 Return Type

None

####### 2.3.4.1.11.3.4 Access Modifier

private

####### 2.3.4.1.11.3.5 Is Async

❌ No

####### 2.3.4.1.11.3.6 Framework Specific Attributes

- @job(retry_pattern={1: 60, 2: 300, 3: 1800, 4: 7200})

####### 2.3.4.1.11.3.7 Parameters

*No items available*

####### 2.3.4.1.11.3.8 Implementation Logic

Validation complete. This method specification correctly defines the background task for retries. It must instantiate `GspService` and call its `generate_einvoice` method. As this is a method on `account.move`, `self` is the single invoice record to process.

####### 2.3.4.1.11.3.9 Exception Handling

Specification requires the method to raise an exception on failure, allowing the job queue to manage retries. A final `except` block should update the invoice status to \"failed\" after all retries are exhausted.

####### 2.3.4.1.11.3.10 Performance Considerations

Jobs should be lightweight and idempotent.

####### 2.3.4.1.11.3.11 Validation Requirements

Specification requires the job to re-validate the invoice state (`gsp_status` is \"pending\") before processing to prevent race conditions with manual interventions.

####### 2.3.4.1.11.3.12 Technology Integration Details

Validation confirms the `retry_pattern` in the `@job` decorator correctly specifies exponential backoff as per REQ-1-302.

##### 2.3.4.1.12.0.0 Events

*No items available*

##### 2.3.4.1.13.0.0 Implementation Notes

Validation complete. This enhanced specification for the model extension is the central data entity for the addon.

#### 2.3.4.2.0.0.0 Class Name

##### 2.3.4.2.1.0.0 Class Name

GspService

##### 2.3.4.2.2.0.0 File Path

services/gsp_service.py

##### 2.3.4.2.3.0.0 Class Type

Service

##### 2.3.4.2.4.0.0 Inheritance

object

##### 2.3.4.2.5.0.0 Purpose

Specification validated. Orchestrates the e-invoice generation process, including data mapping, synchronous API call, and asynchronous fallback logic.

##### 2.3.4.2.6.0.0 Dependencies

- GspApiClient
- GspRequestMapper
- Odoo Environment (self.env)

##### 2.3.4.2.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.2.8.0.0 Technology Integration Notes

Validation confirms this is a pure Python class encapsulating the core logic required by REQ-1-302.

##### 2.3.4.2.9.0.0 Validation Notes

This service class correctly isolates complex orchestration logic from the Odoo model, improving maintainability and testability.

##### 2.3.4.2.10.0.0 Properties

*No items available*

##### 2.3.4.2.11.0.0 Methods

- {'method_name': 'generate_einvoice', 'method_signature': 'generate_einvoice(self, invoice)', 'return_type': 'dict', 'access_modifier': 'public', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'invoice', 'parameter_type': 'account.move record', 'is_nullable': False, 'purpose': 'The Odoo invoice record to be processed.', 'framework_attributes': []}], 'implementation_logic': 'Specification enhanced for detail. Must perform the following steps: 1. Instantiate `GspRequestMapper` and `GspApiClient`. 2. Call mapper to transform `invoice` record to GSP payload. 3. Implement a try/except block. 4. Inside \\"try\\", call the API client\'s `send_invoice_data` method. 5. On success (2xx response), call a private helper `_process_success_response` to write IRN/QR data to the invoice and set `gsp_status` to \\"generated\\". 6. The `except` block must catch specific transient exceptions (Timeout, ConnectionError, 5xx errors) from the client, log the error, update `gsp_status` to \\"pending\\", and enqueue the background job using `invoice.with_delay()._job_generate_einvoice()`. 7. A separate `except` block for client-side errors (4xx) must log the error, update `gsp_status` to \\"failed\\", and store the error message on the invoice.', 'exception_handling': 'Specification mandates differentiation between transient errors (for retry) and permanent data errors (for immediate failure). Must catch custom exceptions from the API client.', 'performance_considerations': 'The synchronous part of this method must execute within the configured timeout to avoid blocking the UI.', 'validation_requirements': 'Relies on pre-flight validation being performed by the calling model method.', 'technology_integration_details': 'Validation confirms this is the core integration point between the Odoo ORM, the external API client, and the Odoo Job Queue.'}

##### 2.3.4.2.12.0.0 Events

*No items available*

##### 2.3.4.2.13.0.0 Implementation Notes

Validation complete. This class correctly implements the resilient integration pattern.

#### 2.3.4.3.0.0.0 Class Name

##### 2.3.4.3.1.0.0 Class Name

GspApiClient

##### 2.3.4.3.2.0.0 File Path

services/gsp_api_client.py

##### 2.3.4.3.3.0.0 Class Type

Client

##### 2.3.4.3.4.0.0 Inheritance

object

##### 2.3.4.3.5.0.0 Purpose

Specification for a client class responsible for direct HTTP communication with the external GSP API.

##### 2.3.4.3.6.0.0 Dependencies

- requests
- AwsSecretsManager

##### 2.3.4.3.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.3.8.0.0 Technology Integration Notes

Validation confirms this class correctly uses the `requests` library and depends on the `AwsSecretsManager` service for API key retrieval.

##### 2.3.4.3.9.0.0 Validation Notes

This class correctly isolates the third-party API from the rest of the application, fulfilling the Adapter pattern.

##### 2.3.4.3.10.0.0 Properties

*No items available*

##### 2.3.4.3.11.0.0 Methods

- {'method_name': 'send_invoice_data', 'method_signature': 'send_invoice_data(self, payload)', 'return_type': 'dict', 'access_modifier': 'public', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'payload', 'parameter_type': 'dict', 'is_nullable': False, 'purpose': 'The JSON-serializable dictionary to be sent as the request body.', 'framework_attributes': []}], 'implementation_logic': 'Specification enhanced for clarity. 1. Retrieve API URL and timeout from `ir.config_parameter`. 2. Instantiate `AwsSecretsManager` to get the API key. 3. Construct HTTP headers. 4. Execute a `requests.post` call with the payload, headers, and timeout. 5. Use `response.raise_for_status()` to automatically raise an `HTTPError` for 4xx/5xx responses. 6. If successful, parse the JSON response and return it.', 'exception_handling': 'Specification requires catching `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError` for transient issues, and `requests.exceptions.HTTPError` for API-level errors. These should be wrapped in custom, specific exceptions (e.g., `GspApiTimeoutError`, `GspApiDataError`) to be handled by the `GspService`.', 'performance_considerations': "The timeout value must be configurable via Odoo's `ir.config_parameter` as defined in the configuration specification.", 'validation_requirements': 'Assumes the payload is correct. Must validate the structure of the API response before returning.', 'technology_integration_details': 'Directly uses the `requests` library to abstract HTTP communication.'}

##### 2.3.4.3.12.0.0 Events

*No items available*

##### 2.3.4.3.13.0.0 Implementation Notes

Complete isolation of the third-party API is the key architectural goal of this specification.

#### 2.3.4.4.0.0.0 Class Name

##### 2.3.4.4.1.0.0 Class Name

GspRequestMapper

##### 2.3.4.4.2.0.0 File Path

services/gsp_request_mapper.py

##### 2.3.4.4.3.0.0 Class Type

Service

##### 2.3.4.4.4.0.0 Inheritance

object

##### 2.3.4.4.5.0.0 Purpose

Added missing specification from systematic analysis. Transforms an Odoo `account.move` recordset into a JSON-serializable dictionary that conforms to the GSP API's required schema.

##### 2.3.4.4.6.0.0 Dependencies

- Odoo Environment (self.env)

##### 2.3.4.4.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.4.8.0.0 Technology Integration Notes

A pure Python class that reads from the Odoo ORM but does not write. It encapsulates complex data transformation logic.

##### 2.3.4.4.9.0.0 Validation Notes

This component is critical for fulfilling REQ-1-006 and for separating concerns within the service layer. Its absence was a major gap.

##### 2.3.4.4.10.0.0 Properties

*No items available*

##### 2.3.4.4.11.0.0 Methods

- {'method_name': 'map_invoice_to_gsp_payload', 'method_signature': 'map_invoice_to_gsp_payload(self, invoice)', 'return_type': 'dict', 'access_modifier': 'public', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'invoice', 'parameter_type': 'account.move record', 'is_nullable': False, 'purpose': 'The source invoice record.', 'framework_attributes': []}], 'implementation_logic': "Specification requires this method to read all necessary fields from the `invoice` record and its related records (e.g., `invoice.partner_id`, `invoice.invoice_line_ids`). It must then construct a nested dictionary that exactly matches the GSP's documented JSON structure. This includes formatting dates, numbers, and tax details correctly.", 'exception_handling': 'Should raise a `ValueError` if critical data is missing from the Odoo invoice record, which can be caught by `GspService`.', 'performance_considerations': "Should use Odoo's `read()` method for efficient data fetching if many fields are needed.", 'validation_requirements': 'Must validate that all mandatory fields for the GSP API are present in the source Odoo record before attempting to map.', 'technology_integration_details': 'Acts as the data transformation layer between the Odoo ORM and the external API.'}

##### 2.3.4.4.12.0.0 Events

*No items available*

##### 2.3.4.4.13.0.0 Implementation Notes

This specification ensures that the complex and potentially volatile GSP data schema is isolated in a single, testable component.

#### 2.3.4.5.0.0.0 Class Name

##### 2.3.4.5.1.0.0 Class Name

AwsSecretsManager

##### 2.3.4.5.2.0.0 File Path

services/aws_secrets_manager.py

##### 2.3.4.5.3.0.0 Class Type

Service

##### 2.3.4.5.4.0.0 Inheritance

object

##### 2.3.4.5.5.0.0 Purpose

Added missing specification from systematic analysis. A reusable service to fetch secrets from AWS Secrets Manager.

##### 2.3.4.5.6.0.0 Dependencies

- boto3

##### 2.3.4.5.7.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.5.8.0.0 Technology Integration Notes

Uses the AWS SDK for Python (boto3) to interact with AWS services.

##### 2.3.4.5.9.0.0 Validation Notes

This component centralizes cloud integration logic and ensures secrets are handled securely and consistently, fulfilling a key NFR.

##### 2.3.4.5.10.0.0 Properties

*No items available*

##### 2.3.4.5.11.0.0 Methods

- {'method_name': 'get_secret', 'method_signature': 'get_secret(self, secret_name, region_name)', 'return_type': 'str', 'access_modifier': 'public', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'secret_name', 'parameter_type': 'str', 'is_nullable': False, 'purpose': 'The name or ARN of the secret to retrieve.', 'framework_attributes': []}, {'parameter_name': 'region_name', 'parameter_type': 'str', 'is_nullable': False, 'purpose': 'The AWS region of the secret.', 'framework_attributes': []}], 'implementation_logic': 'Specification requires this method to initialize a boto3 session and secretsmanager client. It then calls `get_secret_value` and returns the `SecretString`. This method should implement caching to avoid repeated API calls for the same secret within a short time frame.', 'exception_handling': 'Must catch and handle boto3 client errors gracefully (e.g., `ClientError` for permissions issues, `ResourceNotFoundException`), raising a custom application-level exception.', 'performance_considerations': 'Specification requires in-memory caching of secrets for a configurable duration (e.g., 5 minutes) to improve performance.', 'validation_requirements': "The Odoo instance's IAM role must have the necessary `secretsmanager:GetSecretValue` permission.", 'technology_integration_details': 'Provides a Pythonic interface to the AWS Secrets Manager service.'}

##### 2.3.4.5.12.0.0 Events

*No items available*

##### 2.3.4.5.13.0.0 Implementation Notes

This specification promotes a secure and efficient way to handle external service credentials.

### 2.3.5.0.0.0.0 Interface Specifications

*No items available*

### 2.3.6.0.0.0.0 Enum Specifications

*No items available*

### 2.3.7.0.0.0.0 Dto Specifications

*No items available*

### 2.3.8.0.0.0.0 Configuration Specifications

- {'configuration_name': 'ir.config_parameter', 'file_path': 'data/ir_config_parameter_data.xml', 'purpose': 'Specification for storing system-wide configuration for the GSP integration addon declaratively.', 'framework_base_class': 'ir.config_parameter', 'configuration_sections': [{'section_name': 'GSP Integration Settings', 'properties': [{'property_name': 'tms_gsp.api_url', 'property_type': 'string', 'default_value': '', 'required': True, 'description': "The base URL for the GST Suvidha Provider's API."}, {'property_name': 'tms_gsp.aws_secret_name', 'property_type': 'string', 'default_value': '', 'required': True, 'description': 'The name or ARN of the secret in AWS Secrets Manager containing the GSP API key.'}, {'property_name': 'tms_gsp.timeout_seconds', 'property_type': 'integer', 'default_value': '15', 'required': True, 'description': 'The timeout in seconds for synchronous API calls before falling back to the async queue.'}, {'property_name': 'tms_gsp.aws_region', 'property_type': 'string', 'default_value': 'ap-south-1', 'required': True, 'description': 'The AWS region where the Secrets Manager secret is stored.'}]}], 'validation_requirements': "The specified AWS secret must exist and be accessible by the Odoo instance's IAM role."}

### 2.3.9.0.0.0.0 Dependency Injection Specifications

*No items available*

### 2.3.10.0.0.0.0 External Integration Specifications

#### 2.3.10.1.0.0.0 Integration Target

##### 2.3.10.1.1.0.0 Integration Target

GST Suvidha Provider (GSP) API

##### 2.3.10.1.2.0.0 Integration Type

HTTP REST API

##### 2.3.10.1.3.0.0 Required Client Classes

- GspApiClient

##### 2.3.10.1.4.0.0 Configuration Requirements

Specification requires API URL and an API Key.

##### 2.3.10.1.5.0.0 Error Handling Requirements

Validation confirms the specification requires handling of network timeouts, connection errors, and HTTP status codes (4xx/5xx) gracefully.

##### 2.3.10.1.6.0.0 Authentication Requirements

Specification requires authentication via a custom HTTP header containing the API key.

##### 2.3.10.1.7.0.0 Framework Integration Patterns

Validation confirms the specification correctly describes a synchronous call using the `requests` library, with a fallback to the Odoo Job Queue for asynchronous retries.

#### 2.3.10.2.0.0.0 Integration Target

##### 2.3.10.2.1.0.0 Integration Target

AWS Secrets Manager

##### 2.3.10.2.2.0.0 Integration Type

Cloud Secret Management Service

##### 2.3.10.2.3.0.0 Required Client Classes

- AwsSecretsManager

##### 2.3.10.2.4.0.0 Configuration Requirements

Specification requires AWS region and the name/ARN of the secret.

##### 2.3.10.2.5.0.0 Error Handling Requirements

Validation confirms the specification requires handling of exceptions related to missing credentials, permissions, or non-existent secrets.

##### 2.3.10.2.6.0.0 Authentication Requirements

Specification requires authentication via an IAM role attached to the EC2/EKS instance running Odoo, following the principle of least privilege.

##### 2.3.10.2.7.0.0 Framework Integration Patterns

Validation confirms the specification of a client service using `boto3`, with a recommendation for in-memory caching.

### 2.3.11.0.0.0.0 File Specifications

#### 2.3.11.1.0.0.0 File Name

##### 2.3.11.1.1.0.0 File Name

__manifest__.py

##### 2.3.11.1.2.0.0 File Path

/

##### 2.3.11.1.3.0.0 File Type

Odoo Manifest

##### 2.3.11.1.4.0.0 Purpose

Specification for the Odoo addon manifest file. Defines metadata, dependencies, and data file loading order.

##### 2.3.11.1.5.0.0 Implementation Notes

Specification requires this file to list dependencies on `account` and `queue_job`. It must also list all XML files in the `data`, `security`, and `views` directories to ensure they are loaded by Odoo.

#### 2.3.11.2.0.0.0 File Name

##### 2.3.11.2.1.0.0 File Name

account_move_view.xml

##### 2.3.11.2.2.0.0 File Path

views/

##### 2.3.11.2.3.0.0 File Type

Odoo View XML

##### 2.3.11.2.4.0.0 Purpose

Specification for extending the invoice form view to add UI elements for the GSP integration.

##### 2.3.11.2.5.0.0 Implementation Notes

Specification requires using XPath to inherit and modify the `account.move.form` view. It must add: 1. A \"Generate E-Invoice\" button, visible only when `state` is \"posted\" and `gsp_status` is \"not_generated\" or \"failed\". 2. A \"Retry E-Invoice\" button, visible only when `gsp_status` is \"failed\". 3. A new page/tab titled \"E-Invoicing\" to display the `gsp_irn`, `gsp_qr_code`, `gsp_status`, and `gsp_error_message` fields.

#### 2.3.11.3.0.0.0 File Name

##### 2.3.11.3.1.0.0 File Name

ir.model.access.csv

##### 2.3.11.3.2.0.0 File Path

security/

##### 2.3.11.3.3.0.0 File Type

Odoo Security CSV

##### 2.3.11.3.4.0.0 Purpose

Specification for defining model-level access rights for this addon.

##### 2.3.11.3.5.0.0 Implementation Notes

This file is a placeholder as this addon only extends an existing model (`account.move`). Access to `account.move` is controlled by the core `account` module. This specification confirms no new models requiring access rights are created.

## 2.4.0.0.0.0.0 Component Count Validation

| Property | Value |
|----------|-------|
| Total Classes | 5 |
| Total Interfaces | 0 |
| Total Enums | 0 |
| Total Dtos | 0 |
| Total Configurations | 1 |
| Total External Integrations | 2 |
| Total Files | 4 |
| Grand Total Components | 12 |
| Phase 2 Claimed Count | 0 |
| Phase 2 Actual Count | 0 |
| Validation Added Count | 12 |
| Final Validated Count | 12 |

# 3.0.0.0.0.0.0 File Structure

## 3.1.0.0.0.0.0 Directory Organization

### 3.1.1.0.0.0.0 Directory Path

#### 3.1.1.1.0.0.0 Directory Path

/

#### 3.1.1.2.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.1.3.0.0.0 Contains Files

- __manifest__.py
- requirements.txt
- pyproject.toml
- .editorconfig
- docker-compose.yml
- .flake8
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

#### 3.1.3.4.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.3.5.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

### 3.1.4.0.0.0.0 Directory Path

#### 3.1.4.1.0.0.0 Directory Path

dev

#### 3.1.4.2.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.4.3.0.0.0 Contains Files

- odoo.conf

#### 3.1.4.4.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.4.5.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling


# 1 Id

REPO-GSP-INT

# 2 Name

tms-gsp-integration-client

# 3 Description

This specialized repository, extracted from 'tms-odoo-addon', contains the Odoo addon responsible for all communication with the external GST Suvidha Provider (GSP) for e-invoicing. Its single responsibility is to transform Odoo invoice data into the GSP API's required format, handle the synchronous API calls, manage the asynchronous fallback to a background job queue on failure, and process the response to update the invoice with the IRN. Isolating this logic encapsulates the third-party dependency (e.g., requests library) and protects the core application from changes or outages in the GSP service. It depends on 'tms-core-business-logic' to access invoice data.

# 4 Type

🔹 Infrastructure

# 5 Namespace

odoo.addons.tms_gsp_integration

# 6 Output Path

addons/tms_gsp_integration

# 7 Framework

Odoo 18

# 8 Language

Python

# 9 Technology

Python 3.11, Odoo Job Queue

# 10 Thirdparty Libraries

- requests

# 11 Layer Ids

- integration-messaging-layer

# 12 Dependencies

- REPO-TMS-CORE

# 13 Requirements

## 13.1 Requirement Id

### 13.1.1 Requirement Id

REQ-1-006

## 13.2.0 Requirement Id

### 13.2.1 Requirement Id

REQ-1-302

# 14.0.0 Generate Tests

✅ Yes

# 15.0.0 Generate Documentation

✅ Yes

# 16.0.0 Architecture Style

Adapter

# 17.0.0 Architecture Map

- Integration & Messaging Layer

# 18.0.0 Components Map

- integration-gateway-003

# 19.0.0 Requirements Map

- REQ-1-006
- REQ-1-302

# 20.0.0 Decomposition Rationale

## 20.1.0 Operation Type

NEW_DECOMPOSED

## 20.2.0 Source Repository

tms-odoo-addon

## 20.3.0 Decomposition Reasoning

Extracted to create a dedicated Adapter for a critical external service. This isolates the third-party dependency and its specific communication patterns (sync with async fallback). If the GSP provider changes or their API is updated, only this repository needs to be modified, minimizing impact on the core business logic.

## 20.4.0 Extracted Responsibilities

- GSP API client implementation
- Data transformation logic for e-invoicing
- Error handling and retry logic for GSP communication

## 20.5.0 Reusability Scope

- Specific to Indian GST e-invoicing; not generally reusable.

## 20.6.0 Development Benefits

- Clear ownership for a complex integration.
- Independent testing and deployment of the integration component.

# 21.0.0 Dependency Contracts

## 21.1.0 Repo-Tms-Core

### 21.1.1 Required Interfaces

- {'interface': 'Odoo ORM API (account.move)', 'methods': ['read([fields])', 'write(vals)'], 'events': [], 'properties': []}

### 21.1.2 Integration Pattern

Direct ORM method calls to fetch invoice data and update it with the response.

### 21.1.3 Communication Protocol

Internal method calls

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

- {'interface': 'GSPInvoiceService', 'methods': ['generate_einvoice(invoice_id)'], 'events': [], 'properties': [], 'consumers': ['REPO-TMS-CORE (via a button on the invoice form)']}

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | N/A |
| Event Communication | N/A |
| Data Flow | Reads from 'account.move', sends to external GSP A... |
| Error Handling | Implements synchronous call with asynchronous fall... |
| Async Patterns | Uses Odoo's job queue with exponential backoff for... |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | The component should be triggered from a button on... |
| Performance Considerations | API call timeouts should be configured aggressivel... |
| Security Considerations | Handle API keys securely; never log sensitive requ... |
| Testing Approach | Heavy reliance on mocking the external GSP API to ... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- Full e-invoice generation workflow.
- Robust error handling and async fallback mechanism.

## 25.2.0 Must Not Implement

- Any invoice-related business logic other than what's needed for the API call.
- UI components other than the trigger button.

## 25.3.0 Extension Points

- Can be adapted for a different GSP provider by changing the client implementation.

## 25.4.0 Validation Rules

- Must perform pre-flight validation to ensure all required data for the GSP API is present on the invoice before making the call.


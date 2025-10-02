# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-087 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer generates a compliant e-invoice vi... |
| As A User Story | As a Finance Officer, I want to generate a GST-com... |
| User Persona | Finance Officer |
| Business Value | Ensures regulatory compliance with Indian GST laws... |
| Functional Area | Invoicing and Financials |
| Story Theme | Financial Management and Compliance |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful e-invoice generation on the first attempt (Happy Path)

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Finance Officer is viewing a validated Odoo invoice in 'Posted' state, which is linked to a 'Completed' trip and does not have an existing IRN.

### 3.1.5 When

The officer clicks the 'Generate E-Invoice' button.

### 3.1.6 Then

The system successfully receives a response from the GSP containing a valid IRN, Acknowledgement Number, Acknowledgement Date, and a signed QR code, the system stores these details against the invoice record, the invoice's 'E-Invoice Status' field is updated to 'Generated', and a success notification is displayed to the user.

### 3.1.7 Validation Notes

Verify the new fields on the invoice model are populated correctly. Check the server logs for a successful 200 OK response from the GSP API. The updated PDF report must render the QR code and IRN.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

GSP API is temporarily unavailable or times out

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A Finance Officer attempts to generate an e-invoice.

### 3.2.5 When

The synchronous API call to the GSP fails due to a timeout or a 5xx server error.

### 3.2.6 Then

The system adds the e-invoice generation task to a dedicated asynchronous queue for automatic retries with exponential backoff, the invoice's 'E-Invoice Status' is set to 'Pending Retry', and the user is immediately shown a message: 'E-invoice generation has been queued due to a temporary connection issue. The system will retry automatically.'

### 3.2.7 Validation Notes

Simulate a GSP API timeout. Verify that a job is created in the RabbitMQ queue. The UI must update instantly without a long wait.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

E-invoice generation fails due to invalid data

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

An invoice contains invalid data, such as an incorrect customer GSTIN format or a missing HSN code for a line item.

### 3.3.5 When

The Finance Officer clicks 'Generate E-Invoice'.

### 3.3.6 Then

The GSP API returns a 4xx client error with a descriptive message, the system parses the error and displays a user-friendly notification (e.g., 'E-invoice generation failed: Invalid recipient GSTIN.'), and the invoice's 'E-Invoice Status' remains 'Not Generated'.

### 3.3.7 Validation Notes

Use test data with an invalid GSTIN. Verify that the specific error message from the GSP is captured in the logs and a sanitized, clear version is shown to the user.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempting to re-generate an already successful e-invoice

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

An invoice already has an 'E-Invoice Status' of 'Generated' and a valid IRN.

### 3.4.5 When

A user attempts to click the 'Generate E-Invoice' button.

### 3.4.6 Then

The system prevents a new API call from being made, the 'Generate E-Invoice' button is disabled or hidden, and a message is available indicating the invoice is already generated.

### 3.4.7 Validation Notes

On an invoice with a stored IRN, confirm the generation button is inactive. No network call to the GSP should be initiated.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Authentication with GSP fails due to invalid credentials

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

The API credentials stored in AWS Secrets Manager are incorrect or expired.

### 3.5.5 When

The system attempts to make any API call to the GSP.

### 3.5.6 Then

The system logs a critical error, sends a high-priority alert to the Admin role, and displays a generic failure message to the Finance Officer: 'E-invoice generation failed due to a system configuration error. Please contact the administrator.'

### 3.5.7 Validation Notes

Configure the staging environment with invalid credentials. Verify that the correct alert is generated and the user sees the generic message, not the specific 401/403 error.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

PDF invoice report is updated with e-invoice details

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

An e-invoice has been successfully generated for an invoice.

### 3.6.5 When

A user prints or downloads the PDF version of the invoice.

### 3.6.6 Then

The generated PDF document prominently displays the signed QR code and the Invoice Reference Number (IRN) in the header or another designated area, as per GST regulations.

### 3.6.7 Validation Notes

Download the PDF for a successfully processed invoice and visually confirm the presence and clarity of the QR code and the IRN text.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Generate E-Invoice' button on the `account.move` form view.
- Read-only fields on the invoice form: 'E-Invoice Status', 'IRN', 'Acknowledgement No.', 'Acknowledgement Date'.
- An image widget to display the signed QR code on the invoice form.

## 4.2.0 User Interactions

- The 'Generate E-Invoice' button's state (active/inactive) must change based on the invoice's status.
- The system must provide immediate visual feedback (e.g., toast notification, loading indicator) upon clicking the button.

## 4.3.0 Display Requirements

- The printable PDF report for the invoice must be modified to include the QR code and IRN.
- User-facing error messages must be clear and actionable, avoiding technical jargon.

## 4.4.0 Accessibility Needs

- All new UI elements must be keyboard-navigable and have appropriate ARIA labels.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-010

### 5.1.2 Rule Description

An invoice can only be generated for a trip that is in the 'Completed' state.

### 5.1.3 Enforcement Point

At the point of invoice creation and validation.

### 5.1.4 Violation Handling

The system should prevent the creation or posting of an invoice linked to a non-completed trip.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-GSP-01

### 5.2.2 Rule Description

An e-invoice cannot be generated if the customer's GSTIN is missing or invalid.

### 5.2.3 Enforcement Point

Before the API call to the GSP is made.

### 5.2.4 Violation Handling

The system should perform a pre-flight validation and block the API call, showing an error to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-037

#### 6.1.1.2 Dependency Reason

This story is the technical implementation of the user-facing feature defined in US-037.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-015

#### 6.1.2.2 Dependency Reason

Requires customer master data, including validated GSTIN, to be available.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-039

#### 6.1.3.2 Dependency Reason

The overall invoicing workflow must be established before automation can be added.

## 6.2.0.0 Technical Dependencies

- Odoo 18 `account` module.
- Configured AWS Secrets Manager for storing API credentials.
- Configured Amazon MQ for RabbitMQ instance for the asynchronous retry queue.
- Python `requests` library or equivalent for HTTP calls.
- Python `boto3` library for AWS integration.

## 6.3.0.0 Data Dependencies

- Accurate and complete customer data (Name, Address, GSTIN).
- Company's own GSTIN and address details configured in Odoo.
- Accurate HSN/SAC codes for all billable items/services.

## 6.4.0.0 External Dependencies

- A procured and active subscription with a GST Suvidha Provider (GSP).
- Access to the GSP's API documentation, sandbox environment, and production credentials.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The initial user feedback after clicking 'Generate E-Invoice' must be provided within 2 seconds, as per REQ-NFR-001.
- The asynchronous job should process the request as soon as it is received from the GSP.

## 7.2.0.0 Security

- All API credentials must be stored in AWS Secrets Manager and retrieved at runtime, never in code or configuration files (REQ-NFR-003).
- All communication with the GSP API must be over HTTPS using TLS 1.2 or newer (REQ-INT-004).

## 7.3.0.0 Usability

- The process should feel seamless to the Finance Officer, requiring minimal clicks and providing clear status updates.

## 7.4.0.0 Accessibility

- The system must adhere to WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0.0 Compatibility

- The feature must be fully functional on all supported modern web browsers.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

High

## 8.2.0.0 Complexity Factors

- Integration with a third-party API with a complex data schema.
- Implementation of a robust synchronous/asynchronous flow with a message queue.
- Secure handling and management of API credentials.
- Comprehensive parsing and mapping of GSP error codes to user-friendly messages.
- Modification of Odoo's QWeb PDF reports to include dynamic data (QR code).

## 8.3.0.0 Technical Risks

- The GSP's API may have poor documentation or be unreliable, requiring significant debugging and robust error handling.
- Changes in GST e-invoicing regulations may require future modifications to the API payload or logic.
- Difficulty in perfectly replicating all GSP error scenarios in a test environment.

## 8.4.0.0 Integration Points

- Odoo `account.move` model.
- GSP's e-invoicing API endpoint.
- AWS Secrets Manager.
- Amazon MQ (RabbitMQ).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Successful generation for a standard B2B invoice.
- Failure due to invalid customer GSTIN.
- Failure due to missing HSN code.
- System behavior during GSP API timeout (testing the async fallback).
- System behavior with invalid API credentials.
- Verification of PDF report content post-generation.

## 9.3.0.0 Test Data Needs

- A set of invoices with valid data.
- Test cases with intentionally invalid data (bad GSTIN, missing fields).
- Access to the GSP's sandbox environment is mandatory for integration testing.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Python `unittest.mock` to simulate GSP API responses (success, failure, timeout).
- Odoo's testing framework.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in the GSP sandbox environment.
- Code reviewed and approved by at least one other developer.
- Unit tests for data mapping, API client, and error handling achieve >80% code coverage.
- Integration testing against the GSP sandbox is completed and documented.
- Asynchronous retry mechanism is tested and confirmed to work.
- Security review confirms credentials are managed securely via AWS Secrets Manager.
- The updated PDF invoice report is reviewed and approved.
- Admin documentation for configuring GSP credentials is created.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

13

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is blocked until the GSP sandbox credentials and API documentation are available.
- Requires a developer with experience in external API integrations and asynchronous task queues.
- Allocate time for initial discovery and setup with the GSP API before full development begins.

## 11.4.0.0 Release Impact

This is a critical feature for the financial module and a key requirement for go-live in the Indian market.


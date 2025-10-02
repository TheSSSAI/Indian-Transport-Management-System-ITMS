# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-038 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer manually intervenes on a failed e-... |
| As A User Story | As a Finance Officer, I want to be immediately ale... |
| User Persona | Finance Officer. This user is responsible for bill... |
| Business Value | Ensures business continuity and GST compliance by ... |
| Functional Area | Invoicing and Payments |
| Story Theme | Financial Management and Compliance |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

System flags invoice and alerts user after automated retries fail

### 3.1.3 Scenario Type

Error_Condition

### 3.1.4 Given

An invoice has been submitted for e-invoicing, and the GSP integration's automated retry mechanism (with exponential backoff) has failed repeatedly

### 3.1.5 When

The final automated retry attempt fails

### 3.1.6 Then



```
The invoice's status must be changed to 'E-Invoice Failed'.
AND a high-priority notification is sent to the 'Finance Officer' user group via the Odoo notification system and email.
AND the last known error message from the GSP API (e.g., 'Connection Timeout', 'Invalid Data') is stored and displayed prominently on the invoice form view.
```

### 3.1.7 Validation Notes

Verify by mocking the GSP API to consistently return an error. Check the invoice state, the user's notifications (bell icon), and the presence of an error message on the invoice form.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Finance Officer successfully retries a failed e-invoice submission

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An invoice is in the 'E-Invoice Failed' state due to a temporary issue (e.g., GSP API was temporarily down)

### 3.2.5 When

The Finance Officer opens the invoice and clicks the 'Retry E-Invoicing' button

### 3.2.6 Then



```
The system initiates a new synchronous API call to the GSP.
AND upon a successful response, the invoice status updates to 'Invoiced'.
AND the IRN and other e-invoice data are correctly populated on the invoice record.
AND the error message is cleared from the view.
AND the 'Retry E-Invoicing' and 'Mark as Manually Processed' buttons are hidden.
```

### 3.2.7 Validation Notes

Use a mock API. First, have it return an error to get the invoice into the failed state. Then, configure it to return a success response and verify the state change and data population after the user clicks the retry button.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Finance Officer retries a submission that fails again due to persistent data error

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

An invoice is in the 'E-Invoice Failed' state with an error message like 'Invalid Customer GSTIN'

### 3.3.5 When

The Finance Officer clicks 'Retry E-Invoicing' without correcting the underlying data

### 3.3.6 Then



```
The system attempts the API call, which fails again.
AND the invoice remains in the 'E-Invoice Failed' state.
AND the error message is updated with the latest failure reason (if different) or remains the same.
```

### 3.3.7 Validation Notes

Mock the GSP API to consistently return a data validation error. Verify that retrying without fixing the data does not change the invoice's failed state.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Finance Officer manually processes an invoice during a prolonged outage

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

An invoice is in the 'E-Invoice Failed' state, and the Finance Officer has generated the IRN outside the system (e.g., via the government portal)

### 3.4.5 When

The Finance Officer clicks the 'Mark as Manually Processed' button

### 3.4.6 Then

A dialog box appears prompting for a mandatory 'IRN' text field and an optional 'Reason/Notes' text area.

### 3.4.7 Validation Notes

Verify the modal dialog appears with the correct input fields.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Finance Officer confirms manual processing with required details

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

The 'Mark as Manually Processed' dialog is open

### 3.5.5 When

The Finance Officer enters a valid IRN and an optional note, then confirms

### 3.5.6 Then



```
The invoice status updates to 'Invoiced'.
AND the manually entered IRN is saved to the invoice's IRN field.
AND the note is logged in the invoice's chatter for audit purposes.
AND the 'Retry E-Invoicing' and 'Mark as Manually Processed' buttons are hidden.
```

### 3.5.7 Validation Notes

Check that the invoice state changes, the IRN field is populated with the entered text, and a new message with the note appears in the chatter.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

UI elements for intervention are correctly displayed

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A user is viewing an invoice

### 3.6.5 When

The invoice is in any state other than 'E-Invoice Failed'

### 3.6.6 Then

The 'Retry E-Invoicing' and 'Mark as Manually Processed' buttons must be hidden.

### 3.6.7 Validation Notes

Check the invoice form view for invoices in 'Draft', 'Posted', and 'Paid' states to ensure the buttons are not visible.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new status 'E-Invoice Failed' in the invoice status bar, visually distinct (e.g., red color).
- A filter option 'E-Invoice Failed' in the main invoice list view.
- A non-editable text area or alert box on the invoice form to display the failure reason.
- A 'Retry E-Invoicing' button on the invoice form header.
- A 'Mark as Manually Processed' button on the invoice form header.
- A modal/dialog for capturing manual IRN and notes.

## 4.2.0 User Interactions

- Buttons for intervention are only visible and clickable for authorized users when the invoice is in the 'E-Invoice Failed' state.
- Clicking 'Retry' provides immediate feedback (e.g., a loading spinner) while the API call is in progress.
- The system should prevent saving the manual processing dialog if the IRN field is empty.

## 4.3.0 Display Requirements

- The last recorded error message must be clearly visible on the failed invoice's form view.
- The invoice list view should clearly indicate which invoices have failed.

## 4.4.0 Accessibility Needs

- Error messages and status changes must be accessible to screen readers.
- All buttons and interactive elements must be keyboard-navigable.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-010

### 5.1.2 Rule Description

An invoice can only be generated for a trip that is in the 'Completed' state. This rule is a prerequisite for the e-invoicing process to begin.

### 5.1.3 Enforcement Point

Invoice creation/validation.

### 5.1.4 Violation Handling

User is prevented from creating/validating the invoice.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-MAN-01

### 5.2.2 Rule Description

Only users with 'Finance Officer' or 'Admin' roles can perform the 'Retry E-Invoicing' and 'Mark as Manually Processed' actions.

### 5.2.3 Enforcement Point

UI (button visibility) and Server-side (action execution).

### 5.2.4 Violation Handling

Button is not visible to unauthorized users. Direct server calls are rejected with a permission error.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-037

#### 6.1.1.2 Dependency Reason

This story handles the failure case of the e-invoicing process defined in US-037. The success path must be implemented first.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-087

#### 6.1.2.2 Dependency Reason

The core integration with the GSP API must be established before its failure modes can be handled.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-060

#### 6.1.3.2 Dependency Reason

Depends on the system's notification framework to alert the Finance Officer of the failure.

## 6.2.0.0 Technical Dependencies

- Odoo's `queue.job` or a similar asynchronous task queue for handling the initial submission and automated retries.
- A custom state ('e_invoice_failed') added to the `account.move` model's state machine.
- Odoo's notification system (`mail.activity` or bus notifications).

## 6.3.0.0 Data Dependencies

- Requires a fully validated invoice record (`account.move`) with all necessary data for GST compliance (customer GSTIN, product HSN codes, etc.).

## 6.4.0.0 External Dependencies

- The behavior of the GSP API, specifically its error responses, which must be parsed and displayed to the user.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The user action to retry or manually mark an invoice should provide feedback within 1 second. The subsequent API call may take longer, but the UI should not be blocked.

## 7.2.0.0 Security

- Access to retry/manual processing functions must be strictly controlled by Odoo's group-based permissions (ir.rule and model access).
- All retry attempts and manual overrides must be logged in an immutable audit trail (Odoo chatter) including user, timestamp, and action taken, as per REQ-DAT-008.

## 7.3.0.0 Usability

- Error messages from the GSP API should be presented in a user-friendly format, avoiding technical jargon where possible.
- The workflow to resolve a failed invoice should be intuitive and require minimal clicks.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must function correctly on all supported browsers (latest versions of Chrome, Firefox, Safari).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Modifying Odoo's standard invoice state machine (`account.move`) requires care to avoid unintended side effects on accounting entries.
- Handling the transition from an asynchronous background job (the final failed retry) to a user-facing state change and notification.
- Designing the UI to conditionally show/hide actions and error messages cleanly within the Odoo form view framework.
- Ensuring the 'Retry' logic doesn't require the invoice to be reset to draft, while a 'Correct Data' flow would necessitate a cancel/reset/re-post cycle.

## 8.3.0.0 Technical Risks

- The GSP API may have a wide variety of undocumented error responses that need to be handled gracefully.
- Incorrectly managing the invoice state could lead to accounting discrepancies or locked records.

## 8.4.0.0 Integration Points

- Odoo's `account.move` model.
- The asynchronous job queue system (e.g., `queue.job`).
- The GSP API client/service layer.
- Odoo's notification/messaging system.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- End-to-end flow: Trip -> Invoice -> E-Invoice Submission Fails -> Alert -> User Retry -> Success.
- End-to-end flow: Trip -> Invoice -> E-Invoice Submission Fails -> Alert -> User Manually Processes -> Success.
- Permission testing: Verify a non-Finance user (e.g., Dispatch Manager) cannot see or use the intervention buttons.
- Data correction flow: Test the scenario where a user must cancel, reset to draft, correct data, and then re-submit the invoice for e-invoicing.

## 9.3.0.0 Test Data Needs

- Customer records with both valid and invalid GSTINs.
- Completed trip records ready for invoicing.

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- A mock GSP API server that can be configured to return specific success and error responses on demand.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code is peer-reviewed and merged into the main branch.
- Unit and integration tests are written and achieve a minimum of 80% coverage for the new logic.
- The feature is successfully demonstrated to the Product Owner.
- UI changes are reviewed and approved for consistency and usability.
- Security checks confirm that actions are restricted to authorized roles.
- User documentation (or a quick-reference guide) is updated to explain the failure handling process.
- The feature is deployed and verified in the staging environment without regressions.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a critical part of the e-invoicing epic and is required for a compliant MVP. It cannot be de-scoped.
- Must be scheduled in a sprint after the core e-invoicing success path (US-037, US-087) is completed and tested.

## 11.4.0.0 Release Impact

- This feature is essential for the production readiness of the invoicing module. Without it, the system cannot reliably handle real-world API failures, posing a significant business risk.


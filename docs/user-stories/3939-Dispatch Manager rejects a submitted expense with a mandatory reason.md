# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-034 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager rejects a submitted expense with ... |
| As A User Story | As a Dispatch Manager, I want to reject a submitte... |
| User Persona | Dispatch Manager, Finance Officer (or any user in ... |
| Business Value | Ensures financial accuracy by preventing payment f... |
| Functional Area | Expense Management |
| Story Theme | Trip Financials and Settlement |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Rejecting an expense with a valid reason

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Dispatch Manager logged into the system and am viewing an expense with the status 'Submitted'

### 3.1.5 When

I click the 'Reject' button, enter a reason like 'Receipt is blurry and unreadable' into the mandatory text field, and confirm the action

### 3.1.6 Then

The system must update the expense's status to 'Rejected', the rejection reason must be saved and permanently associated with the expense record, the expense must be removed from my 'Pending Approval' queue, and a notification containing the rejection reason must be sent to the driver who submitted it.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Error Condition: Attempting to reject an expense without providing a reason

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am a Dispatch Manager logged into the system and have opened the rejection dialog for a 'Submitted' expense

### 3.2.5 When

I attempt to confirm the rejection without entering any text in the reason field

### 3.2.6 Then

The system must display a validation error message, such as 'A reason for rejection is required.', the rejection dialog must remain open, and the expense's status must remain 'Submitted'.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Alternative Flow: Canceling the rejection action

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

I am a Dispatch Manager and have clicked the 'Reject' button, which opened a dialog to enter a reason

### 3.3.5 When

I click the 'Cancel' button or close the dialog without confirming

### 3.3.6 Then

The dialog must close, no changes must be saved, and the expense's status must remain 'Submitted'.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

System State: Rejected expense is excluded from financial calculations

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

An expense associated with a trip has been successfully rejected

### 3.4.5 When

I view the profitability calculation for that trip

### 3.4.6 Then

The amount of the rejected expense must not be included in the trip's total expenses.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

UI State: Rejection action is unavailable for non-pending expenses

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

I am a Dispatch Manager viewing an expense that has a status of 'Approved', 'Rejected', or 'Paid'

### 3.5.5 When

I view the actions available for that expense

### 3.5.6 Then

The 'Reject' button must not be visible or must be disabled.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Audit Trail: Rejection event is logged

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I am a Dispatch Manager and I am about to reject an expense

### 3.6.5 When

I successfully reject the expense with a reason

### 3.6.6 Then

An entry must be created in the system's audit trail for the expense record, logging my user ID, the timestamp, the action ('Rejection'), and the change in status from 'Submitted' to 'Rejected'.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Reject' button, visible on expense records in the 'Submitted' state.
- A modal dialog (wizard) that appears upon clicking 'Reject'.
- A mandatory multi-line text area within the modal for the 'Rejection Reason'.
- 'Confirm' and 'Cancel' buttons within the modal.
- A non-editable field on the expense form view to display the rejection reason if the status is 'Rejected'.

## 4.2.0 User Interactions

- Clicking 'Reject' opens the modal.
- Clicking 'Confirm' without a reason shows a validation error.
- Clicking 'Confirm' with a reason processes the rejection and closes the modal.
- Clicking 'Cancel' closes the modal with no action.
- The system should provide a toast notification confirming the successful rejection.

## 4.3.0 Display Requirements

- The expense list view should clearly indicate the 'Rejected' status, perhaps with a specific color or icon.
- The driver's view of their expenses must clearly show the 'Rejected' status and the reason provided by the manager.

## 4.4.0 Accessibility Needs

- The rejection modal and its form elements must be fully keyboard accessible (tab order, enter to submit, escape to cancel).
- All labels and error messages must be associated with their respective form controls for screen readers, compliant with WCAG 2.1 Level AA.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

REQ-FNC-004

### 5.1.2 Rule Description

Only 'Approved' expenses shall be included in the trip's profitability calculation.

### 5.1.3 Enforcement Point

During the calculation of trip profitability.

### 5.1.4 Violation Handling

The system logic must filter out any expense not in the 'Approved' state before summing total expenses.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-CUSTOM-001

### 5.2.2 Rule Description

A reason is mandatory when rejecting an expense claim.

### 5.2.3 Enforcement Point

On submission of the rejection form/modal.

### 5.2.4 Violation Handling

Prevent form submission and display a user-friendly error message.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-053

#### 6.1.1.2 Dependency Reason

A driver must be able to submit an expense before a manager can reject it.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-032

#### 6.1.2.2 Dependency Reason

A manager needs a view or queue of submitted expenses to access the expense they need to reject.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-060

#### 6.1.3.2 Dependency Reason

A notification system must exist to inform the driver that their expense has been rejected.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-025

#### 6.1.4.2 Dependency Reason

An audit trail system must be in place to log this critical financial action.

## 6.2.0.0 Technical Dependencies

- The expense data model must exist with a 'status' field (e.g., a selection field with states like 'Submitted', 'Approved', 'Rejected') and a 'rejection_reason' text field.
- Odoo's notification/messaging system (mail.thread) for sending alerts to the driver.

## 6.3.0.0 Data Dependencies

- Requires test data including at least one expense in the 'Submitted' state, linked to a trip, a driver, and a vehicle.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The rejection action (from click to UI confirmation) should complete in under 500ms.
- Loading the expense approval queue should not be noticeably slower due to this feature.

## 7.2.0.0 Security

- Only users with roles 'Dispatch Manager', 'Finance Officer', or 'Admin' can perform the rejection action. This must be enforced via Odoo's access control lists (ACLs).
- The rejection reason text field should be sanitized to prevent XSS attacks.

## 7.3.0.0 Usability

- The process of rejecting an expense should be intuitive and require minimal clicks.
- The error message for a missing reason should be clear and direct.

## 7.4.0.0 Accessibility

- Must meet WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0.0 Compatibility

- Functionality must be consistent across supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Involves standard Odoo development patterns: creating a wizard (transient model) for the rejection reason, overriding a model's method to change state, and using the chatter/messaging system.
- No complex algorithms or external integrations are required for this specific story.

## 8.3.0.0 Technical Risks

- Potential for race conditions if two managers try to action the same expense simultaneously, though Odoo's transactional nature mitigates this.
- Ensuring the notification is reliably sent and correctly formatted.

## 8.4.0.0 Integration Points

- Trip Profitability Calculation (REQ-FNC-007): Must ensure this logic correctly filters out rejected expenses.
- Driver Portal (REQ-FNC-008): The driver's view must be updated to show the rejected status and reason.
- Audit Trail (REQ-DAT-008): The action must be logged.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify a Dispatch Manager can reject an expense with a reason.
- Verify an attempt to reject without a reason fails with an error.
- Verify the driver receives a notification with the correct reason.
- Verify the trip's profitability report excludes the rejected expense amount.
- Verify a user without the correct role cannot see or use the 'Reject' button.
- Verify the 'Reject' button is not available on expenses in 'Approved' or 'Rejected' states.

## 9.3.0.0 Test Data Needs

- A user with 'Dispatch Manager' role.
- A user with 'Driver' role.
- An expense record in 'Submitted' state, created by the driver user.
- An expense record in 'Approved' state for negative testing.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- Manual or Selenium/Cypress-based E2E testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests implemented for the state change logic, achieving >80% coverage on new code.
- Integration testing completed to ensure notifications and financial calculations are correct.
- User interface reviewed and approved by the product owner.
- Security requirements (role-based access) validated.
- All changes are documented in the user manual.
- Story deployed and verified in the staging environment without regressions.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a core feature for financial control and must be implemented as part of the initial expense management module.
- Dependent on the completion of the expense submission story (US-053).

## 11.4.0.0 Release Impact

- Enables the full expense approval workflow. Without it, managers can only approve, not manage exceptions, making the expense module incomplete.


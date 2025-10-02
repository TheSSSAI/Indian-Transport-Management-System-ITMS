# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-033 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager approves a submitted expense |
| As A User Story | As a Dispatch Manager, I want to review the detail... |
| User Persona | Dispatch Manager. This user is responsible for the... |
| Business Value | Ensures financial accuracy by validating trip-rela... |
| Functional Area | Expense Management |
| Story Theme | Trip Financials and Settlement |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Successful approval of a submitted expense

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in user with the 'Dispatch Manager' role and I am viewing the details of an expense with the status 'Submitted'

### 3.1.5 When

I click the 'Approve' button

### 3.1.6 Then

The system must change the expense's status to 'Approved'.

### 3.1.7 And

An immutable audit log entry must be created recording my user ID, the timestamp, the expense ID, and the status change from 'Submitted' to 'Approved' (as per REQ-DAT-008).

### 3.1.8 Validation Notes

Verify the status change in the database. Check the trip's total expense value before and after the action. Confirm the UI updates correctly. Check the audit log table for the new entry.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Authorization: User without permission attempts to approve

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am a logged-in user with the 'Driver' role

### 3.2.5 When

I attempt to approve an expense (e.g., by navigating to the approval URL or making a direct API call)

### 3.2.6 Then

The system must prevent the action and return an authorization error.

### 3.2.7 And

The expense's status must remain 'Submitted'.

### 3.2.8 Validation Notes

The 'Approve' button should not be visible in the UI for a Driver. Test the backend endpoint directly with a Driver's session token to ensure it is properly secured.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

State Validation: Attempting to approve an expense not in 'Submitted' state

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

I am a logged-in user with the 'Dispatch Manager' role and I am viewing an expense that is already in 'Approved', 'Rejected', or 'Canceled' status

### 3.3.5 When

I view the expense details

### 3.3.6 Then

The 'Approve' button must not be visible or must be disabled.

### 3.3.7 Validation Notes

Check the UI for an expense in each of these terminal states to ensure the action cannot be performed.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Financial Impact: Trip profitability is updated correctly

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A trip has a total revenue of $1000 and total 'Approved' expenses of $200, with a current profitability of $800.

### 3.4.5 And

The trip's profitability must be recalculated to $750.

### 3.4.6 When

A Dispatch Manager approves the $50 expense

### 3.4.7 Then

The trip's total 'Approved' expenses must be recalculated to $250.

### 3.4.8 Validation Notes

Query the trip's financial summary fields before and after the approval action to confirm the values are updated as expected.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A clearly labeled 'Approve' button, visually distinct from the 'Reject' button.
- A confirmation modal is NOT required for approval to ensure a fast workflow, but a clear success toast/notification is mandatory.
- An indicator (e.g., a badge) showing the current status of the expense ('Submitted', 'Approved', 'Rejected').

## 4.2.0 User Interactions

- On successful approval, the UI should update in real-time without a full page reload.
- The 'Approve' and 'Reject' buttons should be removed or disabled immediately after the action is completed to prevent duplicate submissions.

## 4.3.0 Display Requirements

- The expense view must display all details submitted by the driver: Type, Amount, Date, attached Receipt (as a clickable thumbnail/link), Odometer reading (if applicable), and Driver notes.

## 4.4.0 Accessibility Needs

- The 'Approve' button must be keyboard accessible (focusable and activatable via Enter/Space key).
- The success notification must be announced by screen readers.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

REQ-FNC-004

### 5.1.2 Rule Description

Only users with 'Dispatch Manager' or 'Finance Officer' roles can approve or reject expenses.

### 5.1.3 Enforcement Point

Server-side, before executing the state change logic.

### 5.1.4 Violation Handling

Return a 403 Forbidden error. Log the unauthorized attempt.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

REQ-FNC-007

### 5.2.2 Rule Description

Only 'Approved' expenses shall be included in the trip's profitability calculation.

### 5.2.3 Enforcement Point

Within the profitability calculation logic for the Trip model.

### 5.2.4 Violation Handling

The calculation logic must filter expenses by status='Approved'.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-053

#### 6.1.1.2 Dependency Reason

An expense must be submitted by a driver before it can be approved. The expense data model must exist.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-032

#### 6.1.2.2 Dependency Reason

The Dispatch Manager needs a view/queue to find and select expenses that are pending approval.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-070

#### 6.1.3.2 Dependency Reason

The Role-Based Access Control (RBAC) framework must be in place to secure this action.

## 6.2.0.0 Technical Dependencies

- Odoo's ORM for state management and computed fields.
- Odoo's security framework (`ir.model.access.csv`, `ir.rule`).
- The audit trail module/service.

## 6.3.0.0 Data Dependencies

- Requires an existing 'Expense' record in a 'Submitted' state, linked to a valid 'Trip' record.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The server-side processing of the approval action (database update, audit log, triggering recalculation) must complete in under 500ms.

## 7.2.0.0 Security

- The action must be protected against Cross-Site Request Forgery (CSRF).
- The endpoint must enforce role-based authorization checks on the server, not just rely on hiding UI elements on the client.

## 7.3.0.0 Usability

- The action should be achievable with a single click from the expense detail view.
- The system must provide clear, immediate feedback to confirm the action was successful.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must function correctly on all supported browsers as defined in the project scope.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- The core logic is a straightforward state transition.
- Dependencies on profitability calculation and audit logging are the main integration points.
- Assuming the dependent stories are complete, this is primarily a UI and controller/model logic task.

## 8.3.0.0 Technical Risks

- Potential for race conditions if the profitability calculation is complex and not handled atomically.
- Ensuring the Odoo computed field for profitability correctly invalidates and recalculates when a related expense's state changes.

## 8.4.0.0 Integration Points

- Trip Model: To trigger the recalculation of total expenses and profitability.
- Audit Log Service: To record the approval event.
- Notification Service (Future): May need to trigger a notification to the driver or finance team.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify a Dispatch Manager can approve an expense.
- Verify a Driver cannot approve an expense.
- Verify that approving an expense correctly updates the trip's total expense and profitability fields.
- Verify that an already approved or rejected expense cannot be approved again.
- Verify an audit log is created upon successful approval.

## 9.3.0.0 Test Data Needs

- User accounts for 'Dispatch Manager' and 'Driver' roles.
- A trip record.
- An expense record in 'Submitted' status linked to the trip.
- An expense record in 'Approved' status to test state validation.

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- Selenium/Cypress for E2E testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the approval logic implemented with >80% code coverage and passing
- Integration test verifying the update to trip profitability is implemented and passing
- User interface reviewed and approved by the Product Owner
- Security requirements (RBAC) validated via automated or manual testing
- No new high or critical issues found by static code analysis tools
- Story deployed and verified in the staging environment by QA

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a core part of the expense workflow and a prerequisite for financial settlement features.
- Can be developed in parallel with US-034 (Reject Expense) as the UI and backend logic are very similar.

## 11.4.0.0 Release Impact

This feature is essential for the 'Core Operations' and 'Finance' phases of the rollout (REQ-TRN-001).


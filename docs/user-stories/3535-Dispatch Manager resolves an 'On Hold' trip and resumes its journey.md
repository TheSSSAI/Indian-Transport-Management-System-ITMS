# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-030 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager resolves an 'On Hold' trip and re... |
| As A User Story | As a Dispatch Manager, I want to be able to change... |
| User Persona | Dispatch Manager. This user is responsible for the... |
| Business Value | Enables operational continuity by allowing paused ... |
| Functional Area | Trip Management |
| Story Theme | Trip Lifecycle and Exception Handling |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-030-01

### 3.1.2 Scenario

Happy Path: Successfully resuming an 'On Hold' trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a 'Dispatch Manager' and I am viewing the form for a trip that is currently in the 'On Hold' status

### 3.1.5 When

I click the 'Resume Trip' button, enter a resolution comment (e.g., 'Tire replaced, vehicle is cleared to proceed'), and confirm the action

### 3.1.6 Then

The trip's status must immediately change from 'On Hold' to 'In-Transit'.

### 3.1.7 And

A new entry must be created in the trip's event history (chatter) containing the resolution comment, my username, and the timestamp of the action.

### 3.1.8 Validation Notes

Verify the status field on the trip model is updated. Check the `mail.message` records linked to the trip to confirm the new log entry.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-030-02

### 3.2.2 Scenario

Error Condition: Attempting to resume a trip without a resolution comment

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am logged in as a 'Dispatch Manager' and have opened the 'Resume Trip' dialog for an 'On Hold' trip

### 3.2.5 When

I attempt to confirm the action without entering any text in the resolution comment field

### 3.2.6 Then

The system must display a validation error message indicating that the resolution comment is mandatory.

### 3.2.7 And

The dialog must remain open, and the trip's status must remain 'On Hold'.

### 3.2.8 Validation Notes

Check for a client-side or server-side validation error. Confirm the trip record's status has not changed in the database.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-030-03

### 3.3.2 Scenario

Security: An unauthorized user attempts to resume a trip

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am logged in as a user who is not a 'Dispatch Manager' or 'Admin' (e.g., 'Driver', 'Finance Officer')

### 3.3.5 When

I view the form for a trip that is in the 'On Hold' status

### 3.3.6 Then

The 'Resume Trip' button must not be visible or must be disabled.

### 3.3.7 Validation Notes

Log in with test accounts for each role and inspect the trip form view to ensure the button is not actionable.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-030-04

### 3.4.2 Scenario

Edge Case: The 'Resume Trip' action is not available for trips in other statuses

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am logged in as a 'Dispatch Manager'

### 3.4.5 When

I view the form for a trip that is in any status other than 'On Hold' (e.g., 'Planned', 'Assigned', 'In-Transit', 'Delivered')

### 3.4.6 Then

The 'Resume Trip' button must not be visible.

### 3.4.7 Validation Notes

Check the trip form view for trips in each possible status to confirm the button's conditional visibility.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A button labeled 'Resume Trip' in the header of the Trip form view, conditionally visible only for 'On Hold' trips.
- A modal dialog (wizard) that appears upon clicking the 'Resume Trip' button.
- The modal must contain a multi-line text area for the 'Resolution Comment', marked with a required field indicator.
- The modal must have 'Confirm' and 'Cancel' buttons.

## 4.2.0 User Interactions

- Clicking 'Resume Trip' opens the modal.
- Clicking 'Cancel' in the modal closes it with no changes.
- Clicking 'Confirm' without a comment shows a validation error.
- Clicking 'Confirm' with a comment executes the action, closes the modal, and refreshes the trip view to show the new status and chatter entry.

## 4.3.0 Display Requirements

- The resolution comment must be clearly visible in the trip's event history log after submission.

## 4.4.0 Accessibility Needs

- The modal dialog and its form elements must be fully keyboard accessible (tab order, enter to submit).
- The comment field must have a proper label for screen readers, as per WCAG 2.1 Level AA (REQ-INT-001).

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-004

### 5.1.2 Rule Description

The trip status lifecycle must follow the defined path. This action specifically handles the 'On Hold' -> 'In-Transit' transition.

### 5.1.3 Enforcement Point

Server-side action triggered by the 'Resume Trip' wizard.

### 5.1.4 Violation Handling

The action to resume is only available when the trip is 'On Hold', preventing invalid state transitions.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

REQ-FNC-002

### 5.2.2 Rule Description

A user with the 'Dispatch Manager' role shall have the permission to change the status of an 'On Hold' trip back to 'In-Transit'. This action requires a mandatory text comment.

### 5.2.3 Enforcement Point

Access control on the button's visibility and the server action's execution. Field validation on the comment wizard.

### 5.2.4 Violation Handling

Access denied for unauthorized users. Validation error for missing comment.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-077

#### 6.1.1.2 Dependency Reason

This story provides the mechanism to resolve a trip's 'On Hold' status. It is functionally dependent on US-077, which defines how a trip enters the 'On Hold' status. A trip cannot be resumed if it can never be put on hold.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Requires the existence of the core Trip model and its lifecycle states, which are established in the trip creation story.

## 6.2.0.0 Technical Dependencies

- Odoo 18 framework (ORM, Views, Wizards).
- The custom Trip model (`tms.trip`) with a `state` field.
- Odoo's `mail.thread` mixin for logging events to the chatter.

## 6.3.0.0 Data Dependencies

- Requires test data including at least one trip record in the 'On Hold' status.
- Requires user accounts with 'Dispatch Manager' and 'Driver' roles for testing permissions.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The server action to update the status and log the comment must complete in under 200ms, as per REQ-NFR-001.

## 7.2.0.0 Security

- Access to this functionality must be strictly limited to authorized roles ('Dispatch Manager', 'Admin') using Odoo's `ir.model.access.csv` and record rules (`ir.rule`), as per REQ-NFR-003.
- The resolution comment input must be sanitized to prevent cross-site scripting (XSS) attacks.

## 7.3.0.0 Usability

- The process should be intuitive, requiring minimal clicks and clear instructions.
- Error feedback for the mandatory comment must be immediate and clear.

## 7.4.0.0 Accessibility

- Must adhere to WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0.0 Compatibility

- Functionality must be consistent across supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Standard Odoo development pattern: button calls a wizard which executes a server action.
- Logic is simple: state change and chatter post.
- Primary effort is in correctly defining the button's conditional visibility in the XML view (`attrs` attribute) and the wizard's view and logic.

## 8.3.0.0 Technical Risks

- Incorrectly configured access control could expose the action to unauthorized users. This must be a key focus during testing.

## 8.4.0.0 Integration Points

- This feature directly interacts with the Trip model's state machine.
- It writes to Odoo's `mail.message` model via the `mail.thread` integration for the event history.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify a Dispatch Manager can successfully resume a trip.
- Verify a Driver cannot see or use the 'Resume Trip' button.
- Verify the action fails if the comment is empty.
- Verify the button is not shown for trips in statuses other than 'On Hold'.
- Verify the event log (chatter) is correctly updated with the comment, user, and timestamp.

## 9.3.0.0 Test Data Needs

- A trip manually set to 'On Hold'.
- User accounts for 'Admin', 'Dispatch Manager', and 'Driver' roles.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main development branch.
- Unit tests covering the server action logic have been written and are passing with >= 80% coverage.
- Automated or manual integration tests confirm the correct UI behavior and role-based permissions.
- The UI/UX has been reviewed and approved.
- No security vulnerabilities have been introduced.
- The feature is documented in the User Manual for the Dispatch Manager role.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is functionally coupled with US-077 (System automatically changes trip status to 'On Hold'). It should be developed in the same sprint or the one immediately following to complete the exception handling loop.

## 11.4.0.0 Release Impact

- This is a critical feature for operational viability. The system cannot go live without a mechanism to resolve 'On Hold' trips.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-003 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin deactivates a user account |
| As A User Story | As an Admin, I want to deactivate a user's account... |
| User Persona | Admin user with full system access, responsible fo... |
| Business Value | Enhances system security by preventing unauthorize... |
| Functional Area | User and Access Management |
| Story Theme | System Administration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful deactivation of a standard user account

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an 'Admin' and I am on the user management screen

### 3.1.5 When

I select an active user account and trigger the 'Deactivate' action, then confirm the action in the confirmation dialog

### 3.1.6 Then

The system sets the user's status to 'Inactive', a success message is displayed, and the user is immediately unable to log in with their credentials.

### 3.1.7 Validation Notes

Verify by attempting to log in as the deactivated user. The login attempt must fail with an 'account disabled' or similar message. The user list should reflect the 'Inactive' status.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin attempts to deactivate their own account

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am logged in as an 'Admin' and I am viewing my own user record in the user management screen

### 3.2.5 When

I attempt to find or use the 'Deactivate' action for my own account

### 3.2.6 Then

The 'Deactivate' action must be disabled, hidden, or result in an error message stating that self-deactivation is not permitted.

### 3.2.7 Validation Notes

Check both the user list view (actions menu) and the user form view to ensure the deactivation control is not available for the current user.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Deactivated user's active session is terminated

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

A user is currently logged into the system in an active session

### 3.3.5 When

An 'Admin' deactivates that user's account from a separate session

### 3.3.6 Then

The user's active session is immediately invalidated, and upon their next action (e.g., page navigation, API call), they are forcefully logged out and redirected to the login page.

### 3.3.7 Validation Notes

Requires two browser sessions. In session 1, log in as the target user and navigate. In session 2, log in as Admin and deactivate the user. Go back to session 1 and click a link; it should redirect to the login screen.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Historical data integrity is maintained after deactivation

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

A user has created historical records (e.g., trips, invoices, expense entries)

### 3.4.5 When

An 'Admin' deactivates that user's account

### 3.4.6 Then

All historical records previously associated with the user must remain unchanged and still display the user's name as the creator or modifier.

### 3.4.7 Validation Notes

Before deactivation, identify a record created by the user. After deactivation, navigate to that record and verify the user's name is still correctly displayed.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Deactivation action is logged in the audit trail

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

The audit trail feature is enabled for the user model (Ref: REQ-DAT-008)

### 3.5.5 When

An 'Admin' deactivates a user's account

### 3.5.6 Then

A new entry is created in the audit trail log recording the timestamp, the Admin who performed the action, the user account that was affected, and the change of status from 'Active' to 'Inactive'.

### 3.5.7 Validation Notes

Check the audit log for a corresponding entry immediately after performing the deactivation.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Admin is presented with a confirmation dialog before deactivation

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I am logged in as an 'Admin' and I am on the user management screen

### 3.6.5 When

I trigger the 'Deactivate' action for a user

### 3.6.6 Then

A confirmation modal appears with a warning message like 'Are you sure you want to deactivate this user? They will lose all system access immediately.' and requires an explicit confirmation (e.g., 'Confirm' button) to proceed.

### 3.6.7 Validation Notes

Verify the modal appears and that clicking 'Cancel' aborts the action, leaving the user active.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Deactivate' action/button on the Odoo user form and/or list view.
- A confirmation modal dialog with 'Confirm' and 'Cancel' buttons.
- A visual indicator (e.g., status tag, greyed-out text) on the user list to distinguish 'Inactive' users from 'Active' ones.
- A system notification/toast message to confirm successful deactivation.

## 4.2.0 User Interactions

- Admin selects a user from a list.
- Admin clicks the 'Deactivate' action.
- Admin interacts with the confirmation modal to finalize or cancel the action.

## 4.3.0 Display Requirements

- The user's status ('Active'/'Inactive') must be clearly visible in the user management interface.

## 4.4.0 Accessibility Needs

- All UI elements (buttons, modals) must be keyboard accessible and compatible with screen readers, adhering to WCAG 2.1 Level AA. (Ref: REQ-INT-001)

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-SEC-001

### 5.1.2 Rule Description

An Admin user cannot deactivate their own account.

### 5.1.3 Enforcement Point

Server-side logic and client-side UI.

### 5.1.4 Violation Handling

The action is prevented, and an error message is displayed if attempted via API. The UI control is disabled.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-AUDIT-001

### 5.2.2 Rule Description

All user deactivation events must be logged in the system's audit trail.

### 5.2.3 Enforcement Point

Server-side logic upon successful deactivation.

### 5.2.4 Violation Handling

The deactivation transaction should fail if the audit log entry cannot be created.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-001

#### 6.1.1.2 Dependency Reason

A user account must be creatable before it can be deactivated. This story provides the foundational user model.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-002

#### 6.1.2.2 Dependency Reason

The user management interface (list/form views) where the 'Deactivate' action will be placed is likely built as part of the user editing story.

## 6.2.0.0 Technical Dependencies

- Odoo 18 framework, specifically the `res.users` model and its `active` field.
- Odoo's authentication and session management system.
- The system's audit trail module (as per REQ-DAT-008).

## 6.3.0.0 Data Dependencies

- Requires existing user records in the database to perform the deactivation on.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The deactivation action, including database update and UI feedback, should complete in under 500ms.

## 7.2.0.0 Security

- Access to this functionality must be strictly limited to the 'Admin' role via Odoo's access control lists (ACLs).
- The deactivation must be effective immediately, preventing any further actions from the deactivated user's session.
- The action must be logged for security auditing purposes as per REQ-DAT-008.

## 7.3.0.0 Usability

- The process should be intuitive, with a clear action and a confirmation step to prevent accidental deactivations.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must work correctly on all supported modern web browsers.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This functionality can be implemented by leveraging Odoo's standard 'active' field on the `res.users` model, which handles most of the access control automatically.
- Implementing immediate session invalidation for an already logged-in user might require a custom request handler or middleware, which adds minor complexity but is a solved problem.

## 8.3.0.0 Technical Risks

- If not implemented correctly, the session termination might not be immediate, creating a small window of vulnerability. This needs to be tested thoroughly.

## 8.4.0.0 Integration Points

- Odoo's core authentication system.
- The system's central audit logging service.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify an Admin can deactivate a non-Admin user.
- Verify a deactivated user cannot log in.
- Verify an Admin cannot deactivate their own account.
- Verify an active session of a user is killed upon deactivation.
- Verify historical data references to the deactivated user remain intact.
- Verify the deactivation event is correctly recorded in the audit log.

## 9.3.0.0 Test Data Needs

- At least two 'Admin' user accounts.
- At least two standard user accounts (e.g., 'Dispatch Manager', 'Driver').
- Historical data (trips, expenses) created by one of the standard users.

## 9.4.0.0 Testing Tools

- Pytest for backend unit/integration tests.
- Odoo's built-in testing framework.
- Manual testing using multiple browser sessions.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the deactivation logic and self-deactivation prevention, achieving >80% coverage
- Integration testing completed to verify login failure and API access denial for deactivated users
- User interface reviewed and approved by the product owner
- Security requirement for immediate session termination is validated
- Audit trail logging is confirmed to be working as expected
- Documentation for user management is updated to include the deactivation process
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational security feature and should be prioritized early in the development cycle.
- Dependent on US-001 and US-002 being completed in a prior or the same sprint.

## 11.4.0.0 Release Impact

- Essential for the initial release (MVP) to ensure basic security and user lifecycle management.


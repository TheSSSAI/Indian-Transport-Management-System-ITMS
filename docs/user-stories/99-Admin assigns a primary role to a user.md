# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-004 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin assigns a primary role to a user |
| As A User Story | As an Admin, I want to assign a single, predefined... |
| User Persona | Admin: A system administrator with full access rig... |
| Business Value | Enforces a secure and manageable Role-Based Access... |
| Functional Area | User and Access Management |
| Story Theme | System Security and Administration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Assign a primary role to a user

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am viewing the user management form for an existing user.

### 3.1.5 When

I select a primary role, for example 'Dispatch Manager', from the 'Primary Role' dropdown and save the user's record.

### 3.1.6 Then

The system successfully saves the change, assigns the 'Dispatch Manager' role to the user, and their permissions are immediately updated to reflect that role's access rights.

### 3.1.7 Validation Notes

Verify by logging in as the modified user and confirming they can access Dispatch Manager features (e.g., create trips) and cannot access features from their previous role.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Role selection is mutually exclusive

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and am on the user management form.

### 3.2.5 When

I interact with the 'Primary Role' field.

### 3.2.6 Then

The UI element must only allow the selection of a single role, enforcing Business Rule BR-001.

### 3.2.7 Validation Notes

Confirm the UI element is a dropdown/selection list or radio button group, not a multi-select checkbox.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

List of available roles is correct

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am logged in as an Admin and am on the user management form.

### 3.3.5 When

I click to expand the 'Primary Role' selection list.

### 3.3.6 Then

The list must contain the predefined primary roles: 'Admin', 'Dispatch Manager', 'Finance Officer', and 'Driver'.

### 3.3.7 Validation Notes

Check the options in the dropdown list to ensure they match the specification in REQ-USR-001.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Changing a user's role is logged in the audit trail

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I am logged in as an Admin and have just changed a user's role from 'Driver' to 'Finance Officer'.

### 3.4.5 When

I view the audit trail for that user record.

### 3.4.6 Then

A new audit log entry must exist recording my username, the timestamp, the user record that was modified, and the change from the old role ('Driver') to the new role ('Finance Officer').

### 3.4.7 Validation Notes

Check the Odoo chatter or a dedicated audit log model for the `res.users` object to verify the entry exists and is accurate.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Admin attempts to change their own role to a non-Admin role

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am logged in as an Admin and am editing my own user profile.

### 3.5.5 When

I attempt to change my 'Primary Role' from 'Admin' to 'Driver' and save the record.

### 3.5.6 Then

The system must prevent the change and display a clear validation error message, such as 'Administrators cannot revoke their own admin privileges.'

### 3.5.7 Validation Notes

Attempt this action and verify the save operation fails and the expected error message is shown to the user.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Primary Role' field (Odoo Selection widget/dropdown) on the User form view (`res.users`).

## 4.2.0 User Interactions

- Admin selects a single value from the 'Primary Role' dropdown.
- Admin saves the user form to apply the role change.

## 4.3.0 Display Requirements

- The user's currently assigned primary role must be clearly visible on their user record.
- Validation error messages must be displayed prominently if a business rule is violated (e.g., an admin self-demoting).

## 4.4.0 Accessibility Needs

- The 'Primary Role' dropdown must have a proper label and be keyboard-navigable, adhering to WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

- {'rule_id': 'BR-001', 'rule_description': 'A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver).', 'enforcement_point': 'On the user management form during role assignment.', 'violation_handling': 'The UI design (e.g., dropdown list) will prevent the assignment of more than one primary role.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-001

#### 6.1.1.2 Dependency Reason

A user account must exist before a role can be assigned to it.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-070

#### 6.1.2.2 Dependency Reason

The permission sets (access rights and rules) for each primary role must be defined before assigning them to users has any effect.

## 6.2.0.0 Technical Dependencies

- Odoo's base user and security group models (`res.users`, `res.groups`, `ir.model.access`).

## 6.3.0.0 Data Dependencies

- Pre-defined security groups corresponding to each primary role must be created in the system.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Saving a user's role change should complete in under 200ms, consistent with standard GET/POST request performance (REQ-NFR-001).

## 7.2.0.0 Security

- Only users with the 'Admin' role can access this functionality.
- All role changes must be logged in an immutable audit trail as per REQ-DAT-008.
- The implementation must prevent an Admin from accidentally removing their own administrative access.

## 7.3.0.0 Usability

- The process of assigning a role should be intuitive, requiring minimal steps on a single user configuration screen.

## 7.4.0.0 Accessibility

- Must meet WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0.0 Compatibility

- Functionality must be consistent across all supported modern web browsers.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This involves adding a `Selection` field to an existing Odoo model (`res.users`).
- Requires overriding the `write` method to manage Odoo security group memberships based on the selection.
- Logic must be robust to remove previous primary role groups when assigning a new one to prevent permission accumulation.
- A simple check is needed to prevent an admin from changing their own role.

## 8.3.0.0 Technical Risks

- Potential for incorrect permission assignment if the logic for adding/removing users from Odoo groups is flawed. This requires careful testing.

## 8.4.0.0 Integration Points

- Directly integrates with Odoo's core authentication and authorization system.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Assign a role to a brand new user.
- Change the role of an existing user and verify their permissions are updated.
- Verify an Admin cannot change their own role to a non-Admin role.
- Verify the audit log is correctly populated after a role change.
- Log in as a user from each role type to confirm their access is correctly restricted.

## 9.3.0.0 Test Data Needs

- Test user accounts for each role (Admin, Dispatch Manager, Finance Officer, Driver).
- A dedicated test Admin account for performing the changes.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.
- Manual E2E testing via a web browser.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the role-switching logic are implemented with >80% coverage and are passing
- Integration testing completed to confirm permissions are correctly applied
- User interface on the user form is reviewed and approved by the product owner
- Security requirement to prevent admin self-demotion is validated
- Audit trail functionality is verified
- Documentation for user management is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational security story and should be completed early in the project.
- Must be scheduled in a sprint after or alongside US-070, which defines the roles themselves.

## 11.4.0.0 Release Impact

- Critical for the first release as it enables the entire role-based access control system.


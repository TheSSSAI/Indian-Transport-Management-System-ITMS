# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-001 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates a new user account with a primary ro... |
| As A User Story | As an Admin, I want to create a new user account b... |
| User Persona | Admin user with full system access, responsible fo... |
| Business Value | Enables secure and controlled onboarding of new em... |
| Functional Area | User and Access Management |
| Story Theme | Core System Administration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful creation of a new user with a primary role

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am on the 'Create User' screen

### 3.1.5 When

I enter a unique, valid email address, the user's full name, and select a 'Primary Role' (e.g., 'Dispatch Manager') from the available options

### 3.1.6 Then

The system creates the new user account, the user appears in the list of system users, and the user is automatically assigned to the security group corresponding to the 'Dispatch Manager' role.

### 3.1.7 Validation Notes

Verify in the Odoo backend that the new 'res.users' record is created and that its 'groups_id' field contains the correct TMS security group for the selected role.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempt to create a user with a non-unique email address

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am logged in as an Admin and am on the 'Create User' screen

### 3.2.5 When

I enter an email address that already exists for another user in the system and attempt to save

### 3.2.6 Then

The system prevents the creation of the user and displays a clear, user-friendly error message such as 'A user with this email address already exists.'

### 3.2.7 Validation Notes

Test by creating a user, then attempting to create a second user with the exact same email address. The form should not submit.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to create a user with missing required information

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am logged in as an Admin and am on the 'Create User' screen

### 3.3.5 When

I attempt to save the new user without providing a name, email, or selecting a primary role

### 3.3.6 Then

The system prevents the record from being saved and visually indicates which mandatory fields are missing.

### 3.3.7 Validation Notes

Attempt to save the form with each required field left blank one at a time. Verify Odoo's standard required field validation is triggered.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Ensure single primary role assignment

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am logged in as an Admin and have created a new user with the 'Finance Officer' role

### 3.4.5 When

I inspect the user's assigned security groups

### 3.4.6 Then

The user must be a member of the 'Finance Officer' security group and must NOT be a member of other primary role groups like 'Dispatch Manager' or 'Driver'.

### 3.4.7 Validation Notes

Check the 'res.users' model for the created user and confirm only the correct TMS role group is present in their list of groups.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to create a user with an invalid email format

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am logged in as an Admin and am on the 'Create User' screen

### 3.5.5 When

I enter an email address with an invalid format (e.g., 'test@example' or 'test.example.com') and attempt to save

### 3.5.6 Then

The system prevents the record from being saved and displays a validation error on the email field.

### 3.5.7 Validation Notes

Test with multiple invalid email formats to ensure Odoo's standard email widget validation is working.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Primary Role' selection field (dropdown) on the user creation form.
- Standard Odoo input fields for 'Name', 'Email Address / Login'.

## 4.2.0 User Interactions

- The Admin selects one role from the 'Primary Role' dropdown.
- The system provides immediate feedback on validation errors (e.g., duplicate email) upon trying to save.

## 4.3.0 Display Requirements

- The 'Primary Role' dropdown must list the defined roles: Admin, Dispatch Manager, Finance Officer, Driver.
- Error messages must be clear and displayed near the source of the error.

## 4.4.0 Accessibility Needs

- The form must be keyboard navigable.
- All form fields must have associated labels for screen readers, adhering to WCAG 2.1 Level AA (REQ-INT-001).

# 5.0.0 Business Rules

- {'rule_id': 'BR-001', 'rule_description': 'A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver).', 'enforcement_point': 'During the creation and modification of a user record.', 'violation_handling': 'The system logic will automatically remove any other primary role security groups when a new one is selected and saved, ensuring only one is active.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-SYS-001', 'dependency_reason': 'The core Odoo security groups for each role (Admin, Dispatch Manager, Finance Officer, Driver) and their associated permissions must be defined before users can be assigned to them. This story represents that foundational setup.'}

## 6.2.0 Technical Dependencies

- Odoo 18 Framework
- Odoo's built-in user model (`res.users`) and security group mechanism.

## 6.3.0 Data Dependencies

*No items available*

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- User creation should complete in under 200ms, consistent with standard Odoo operations (REQ-NFR-001).

## 7.2.0 Security

- Only users with the 'Admin' role can access the user creation functionality (enforced by Odoo's `ir.model.access.csv`).
- The system must leverage Odoo's standard, secure password handling and user invitation workflow.
- All access to this functionality must be logged in the audit trail (REQ-DAT-008).

## 7.3.0 Usability

- The process should be intuitive for an administrator familiar with the Odoo interface.

## 7.4.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0 Compatibility

- Must function correctly on all modern web browsers supported by Odoo 18.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Requires inheriting and extending a standard Odoo model (`res.users`) and its view.
- Involves writing a small amount of Python logic in the `create` and `write` methods to manage security group assignments.
- Leverages existing Odoo framework features, minimizing the need for custom components.

## 8.3.0 Technical Risks

- Potential for conflict if other third-party modules also modify the `res.users` model. A code review should check for such overlaps.

## 8.4.0 Integration Points

- Directly interacts with Odoo's core authentication and authorization system (`res.users`, `res.groups`).

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- E2E

## 9.2.0 Test Scenarios

- Verify successful user creation for each defined role.
- Verify error handling for duplicate emails.
- Verify validation for missing required fields.
- Log in as a newly created user to confirm their permissions match the assigned role (part of E2E testing for role-specific stories).

## 9.3.0 Test Data Needs

- A list of unique email addresses for creating new test users.
- An existing user account to test the duplicate email scenario.

## 9.4.0 Testing Tools

- Pytest for Odoo unit tests.
- Manual testing via the Odoo web interface.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by a senior developer
- Unit tests implemented for the role assignment logic in `create`/`write` methods, with >80% coverage for new code
- Manual end-to-end testing completed successfully in a staging environment
- User interface reviewed and approved for consistency with Odoo standards
- Security requirement (Admin-only access) validated
- Relevant technical documentation (docstrings) for the model extensions is complete
- Story deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational story required for setting up test users for almost all other features. It should be completed in the first development sprint.

## 11.4.0 Release Impact

Blocks the ability to onboard new users. Critical for initial system setup and go-live.


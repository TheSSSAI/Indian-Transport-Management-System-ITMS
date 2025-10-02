# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-002 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin edits an existing user account's details and... |
| As A User Story | As an Admin, I want to edit an existing user's det... |
| User Persona | Admin: A user with full system access responsible ... |
| Business Value | Ensures system security by enforcing the principle... |
| Functional Area | User and Access Management |
| Story Theme | System Administration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin successfully edits a user's personal information

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and I am on the user management screen viewing a list of users

### 3.1.5 When

I select a user, change their name from 'John Doe' to 'Johnathan Doe' in the edit form, and click 'Save'

### 3.1.6 Then

The system displays a success confirmation message, and the user list now shows the name 'Johnathan Doe' for that user.

### 3.1.7 Validation Notes

Verify the change in the user list view and by re-opening the user's form. Check the audit log (REQ-DAT-008) for an entry showing the 'name' field changed from 'John Doe' to 'Johnathan Doe'.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin successfully changes a user's primary role

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and I am editing the record of a user whose primary role is 'Driver'

### 3.2.5 When

I change their primary role to 'Dispatch Manager' and click 'Save'

### 3.2.6 Then

The system saves the change, and the user is now assigned the default permissions associated with the 'Dispatch Manager' role and the 'Driver' role permissions are removed.

### 3.2.7 Validation Notes

Log in as the modified user to confirm they can access Dispatch Manager screens and can no longer access Driver-only screens. Check the audit log for the role change.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Admin grants an additional, specific permission to a user

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am logged in as an Admin and editing the record of a user with the 'Finance Officer' role

### 3.3.5 When

I add the specific permission group 'Access Vehicle Profitability Reports' to their account and click 'Save'

### 3.3.6 Then

The user retains all 'Finance Officer' permissions and gains the ability to access the Vehicle Profitability Report.

### 3.3.7 Validation Notes

Log in as the modified user and verify they can access both standard Finance Officer features AND the Vehicle Profitability Report.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Admin enters an invalid email format

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am logged in as an Admin and editing a user's record

### 3.4.5 When

I change the user's email address to 'invalid-email' and click 'Save'

### 3.4.6 Then

The system must prevent the record from being saved, highlight the email field, and display a user-friendly validation error message such as 'Please enter a valid email address.'

### 3.4.7 Validation Notes

Test with multiple invalid email formats (e.g., no '@', no domain, special characters).

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Admin attempts to remove their own administrative privileges

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am logged in as an Admin and I am editing my own user account

### 3.5.5 When

I attempt to remove the 'Admin' role or the 'Settings' access group from my account and click 'Save'

### 3.5.6 Then

The system must prevent the change and display a clear warning message, such as 'Action blocked: You cannot remove administrative privileges from your own account.'

### 3.5.7 Validation Notes

This is a critical security check to prevent accidental system lockout. The user should remain on the edit form with their original permissions intact.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Admin cancels an edit

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

I am logged in as an Admin and I have made changes to a user's record but have not saved them

### 3.6.5 When

I click the 'Discard' or 'Cancel' button

### 3.6.6 Then

The system discards all my changes, returns me to the previous view (e.g., the user list), and the user's data remains unchanged.

### 3.6.7 Validation Notes

Verify by re-opening the user's record to see that the original data is still present.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A searchable and filterable list view of all users.
- A form view for editing user details.
- Input fields for Name, Email, etc.
- A dropdown or selection widget for the 'Primary Role'.
- A multi-select list or checkbox group for 'Additional Permissions'.
- 'Save' and 'Discard' buttons.

## 4.2.0 User Interactions

- Admin can search for users by name or email.
- Admin clicks on a user from the list to open the edit form.
- Changes are persisted only upon clicking 'Save'.
- Clicking 'Discard' reverts all unsaved changes.

## 4.3.0 Display Requirements

- The user's current role and permissions must be clearly displayed on the edit form.
- Validation errors must be displayed next to the corresponding fields.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The UI must be navigable using a keyboard.
- Error messages must be programmatically associated with their respective inputs.

# 5.0.0 Business Rules

- {'rule_id': 'BR-001', 'rule_description': 'A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver).', 'enforcement_point': 'On the user edit form, the primary role selection should be a single-choice input (e.g., radio button or dropdown).', 'violation_handling': 'The UI component itself prevents the selection of more than one primary role.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-001

#### 6.1.1.2 Dependency Reason

The user creation story establishes the user model and the basic form view that this story modifies. A user must exist before they can be edited.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-004

#### 6.1.2.2 Dependency Reason

This story defines the concept of 'primary roles' and their associated default permission sets, which are managed and changed in the user edit screen.

## 6.2.0.0 Technical Dependencies

- Odoo's core user model (`res.users`).
- Odoo's security and access group framework (`res.groups`, `ir.model.access.csv`).
- The system's audit trail module (as per REQ-DAT-008) must be available to log changes.

## 6.3.0.0 Data Dependencies

- A pre-defined set of roles (Admin, Dispatch Manager, Finance Officer, Driver) and their corresponding permission groups must exist in the database.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The user edit form must load in under 2 seconds.
- Saving a user's record should complete within 500ms.

## 7.2.0.0 Security

- Only users with the 'Admin' role can access the user editing functionality.
- Changes to user permissions must be logged in an immutable audit trail (REQ-DAT-008).
- The system must prevent an admin from locking themselves out of the system.

## 7.3.0.0 Usability

- The distinction between a 'Primary Role' and 'Additional Permissions' must be visually clear and intuitive to the Admin.

## 7.4.0.0 Accessibility

- The user management interface must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must be fully functional on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This functionality leverages standard Odoo form views and model operations.
- The primary logic involves modifying fields on the `res.users` model.
- The self-lockout prevention logic is a simple check that needs to be added before saving.

## 8.3.0.0 Technical Risks

- A misconfiguration of the view could make managing permissions confusing. The UI needs to clearly separate the concept of a primary role from additional ad-hoc permissions.

## 8.4.0.0 Integration Points

- Odoo's `res.users` and `res.groups` models.
- The custom audit trail module.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify that changing a user's name, email, and other details works correctly.
- Verify that changing a user's primary role correctly adds the new role's permissions and removes the old ones.
- Verify that adding/removing individual permission groups works without affecting the primary role.
- Test the self-lockout prevention by having an Admin attempt to de-escalate their own privileges.
- Test all validation rules, especially for the email format.
- Log in as the modified user after each permission change to confirm the access rights are correctly applied in the UI.

## 9.3.0.0 Test Data Needs

- An Admin user account for performing the edits.
- At least one test user account for each primary role (Dispatch Manager, Finance Officer, Driver) to be the subject of the edits.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- Manual or automated E2E testing suite (e.g., Selenium, Playwright).

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for self-lockout prevention logic are implemented and passing with >80% coverage
- Integration testing confirms that saving the user correctly updates related models and creates an audit trail entry
- E2E testing confirms an Admin can edit a user and the edited user's permissions are correctly enforced
- User interface is responsive and consistent with Odoo's design standards
- Security requirement for audit logging is validated
- No regressions are introduced in the user management area
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational feature for system administration and should be completed early in the project.
- Dependent on US-001 and US-004 being completed in a prior or the same sprint.

## 11.4.0.0 Release Impact

- Core functionality required for the initial release (MVP) to allow for user setup and management.


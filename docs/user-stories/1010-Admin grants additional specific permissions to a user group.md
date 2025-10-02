# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-005 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin grants additional specific permissions to a ... |
| As A User Story | As an Admin, I want to grant specific, granular pe... |
| User Persona | Admin, as defined in REQ-USR-001, responsible for ... |
| Business Value | Provides the flexibility to tailor user access to ... |
| Functional Area | User and Access Management |
| Story Theme | Role-Based Access Control (RBAC) and Security |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Granting a new 'Read' permission to a standard role

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin, and a 'Dispatch Manager' user exists who belongs to the 'Dispatch Manager' group.

### 3.1.5 When

I navigate to 'Settings > Users & Companies > Groups', select the 'Dispatch Manager' group, and add a new 'Read' access right for the 'Invoice' (account.move) model.

### 3.1.6 Then

The 'Dispatch Manager' user, upon their next login or page refresh, can now access the Invoicing menu and view invoices in a read-only state.

### 3.1.7 Validation Notes

Verify by logging in as the Dispatch Manager. The user should see the invoice list but the 'Create' and 'Edit' buttons should be hidden or disabled. Attempting to access an invoice directly via URL should succeed for viewing but fail for editing.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Verifying lack of unintended permissions

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

The 'Dispatch Manager' group has been granted 'Read' access to the 'Invoice' model.

### 3.2.5 When

A user from that group views the list of invoices.

### 3.2.6 Then

The user cannot create, edit, or delete any invoices.

### 3.2.7 Validation Notes

Confirm that UI controls for create, edit, and delete actions are not present or are disabled for the test user on the invoice views.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Revoking a previously granted permission

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

The 'Dispatch Manager' group has 'Read' access to the 'Invoice' model.

### 3.3.5 When

I, as an Admin, remove the 'Read' access right for the 'Invoice' model from the 'Dispatch Manager' group.

### 3.3.6 Then

The 'Dispatch Manager' user immediately loses access to the Invoicing menu and can no longer view any invoices.

### 3.3.7 Validation Notes

After the Admin saves the change, the Dispatch Manager user should receive an 'Access Denied' error when trying to view the invoice list or a specific invoice URL. The menu item should disappear on refresh.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Permission changes are captured in the audit trail

### 3.4.3 Scenario Type

Security

### 3.4.4 Given

The Audit Trail feature (REQ-DAT-008) is active.

### 3.4.5 When

I, as an Admin, add or remove any access right from any user group.

### 3.4.6 Then

A new, immutable entry is created in the audit log.

### 3.4.7 Validation Notes

Check the audit log model for an entry containing the Admin's user ID, the timestamp, the group that was modified (e.g., 'Dispatch Manager' group), and details of the permission change (e.g., 'Added Read access for model account.move').

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Custom TMS models are available for permission assignment

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I am logged in as an Admin and navigating the Access Rights configuration for a group.

### 3.5.5 When

I click to add a new access right.

### 3.5.6 Then

The list of available models for which I can assign permissions includes custom TMS models such as 'Trip', 'Vehicle', and 'Route'.

### 3.5.7 Validation Notes

In the 'Access Rights' tab for any group, verify that 'tms.trip', 'tms.vehicle', etc., can be selected from the model dropdown list.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- This story leverages the standard Odoo interface for managing security groups and access rights.
- No custom UI is required.

## 4.2.0 User Interactions

- Admin navigates to Settings > Users & Companies > Groups.
- Admin selects a group to open its form view.
- Admin interacts with the 'Access Rights' tab, which is a standard one2many list view.
- Admin clicks 'Add a line' to create a new access rule, selects a model, and checks the boxes for Read, Write, Create, and/or Delete permissions.

## 4.3.0 Display Requirements

- The interface must clearly display the model and the four permission levels (Read, Write, Create, Delete) for each access rule.

## 4.4.0 Accessibility Needs

- Must adhere to Odoo's default accessibility standards, which are intended to meet WCAG 2.1 Level AA (as per REQ-INT-001).

# 5.0.0 Business Rules

- {'rule_id': 'BR-001', 'rule_description': "A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver). Additional permissions are layered on top of the primary role's group.", 'enforcement_point': 'User creation and editing.', 'violation_handling': 'The system should guide the Admin to add users to groups rather than assigning multiple conflicting primary roles.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-001

#### 6.1.1.2 Dependency Reason

Requires the ability to create user accounts that can be assigned to groups.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-004

#### 6.1.2.2 Dependency Reason

This story provides the mechanism to customize the base roles/groups defined in US-004.

## 6.2.0.0 Technical Dependencies

- Odoo's core security framework (`ir.model.access`, `res.groups`).
- The custom TMS models (e.g., `tms.trip`) must be defined in the system for them to be selectable.

## 6.3.0.0 Data Dependencies

- Requires existing user groups corresponding to the defined roles (Admin, Dispatch Manager, etc.).

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Permission changes should be reflected for the user within one web request (e.g., page refresh) after the Admin saves the change.

## 7.2.0.0 Security

- All modifications to user group permissions must be logged in the system's audit trail as per REQ-DAT-008.
- This functionality must only be accessible to users with 'Admin' privileges.

## 7.3.0.0 Usability

- The process should be intuitive for an Odoo administrator, leveraging familiar platform patterns.

## 7.4.0.0 Accessibility

- Adherence to WCAG 2.1 Level AA standards via the standard Odoo framework.

## 7.5.0.0 Compatibility

- Functionality must be consistent across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Leverages existing, core Odoo functionality.
- No custom UI development is needed.
- Primary development work is ensuring custom TMS models are correctly defined and registered, making them available to the security system.

## 8.3.0.0 Technical Risks

- Low risk. A potential risk is misconfiguration of base permissions, which could grant unintended access. This is a configuration risk, not a development risk.

## 8.4.0.0 Integration Points

- Integrates with Odoo's authentication and authorization engine.
- Integrates with the Audit Trail module (REQ-DAT-008) to log changes.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Integration
- Security
- Manual E2E

## 9.2.0.0 Test Scenarios

- Create a test user and assign them to a non-Admin group (e.g., Dispatch Manager).
- Verify the user's baseline access restrictions.
- As Admin, grant a new, specific permission (e.g., read-only on a financial model).
- Log in as the test user and confirm the new permission is active and correctly restricted (e.g., read but not write).
- As Admin, revoke the permission.
- Log in as the test user and confirm access has been removed.
- As Admin, verify that all permission changes were logged in the audit trail.

## 9.3.0.0 Test Data Needs

- At least one non-Admin user account for testing.
- Pre-defined user groups for each primary role.

## 9.4.0.0 Testing Tools

- Standard browser developer tools for inspecting UI and network requests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented and passing (if any new logic is added, though unlikely)
- Integration testing completed successfully, confirming permissions are applied correctly
- User interface reviewed and approved (verifying standard Odoo UI is used correctly)
- Security requirements validated, especially audit logging of permission changes
- Documentation updated to explain how to customize roles
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational security story that enables flexibility for the entire system. It should be implemented early in the project, alongside the initial setup of roles and permissions.

## 11.4.0.0 Release Impact

- Enables administrators to manage the system effectively post-launch without needing developer intervention for minor permission adjustments.


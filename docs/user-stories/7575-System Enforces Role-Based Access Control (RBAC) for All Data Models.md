# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-070 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System Enforces Role-Based Access Control (RBAC) f... |
| As A User Story | As a System Administrator, I want the system to st... |
| User Persona | System Administrator (on behalf of the business) |
| Business Value | Ensures data security and confidentiality, enforce... |
| Functional Area | Security & Access Control |
| Story Theme | Core System Architecture |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin has unrestricted access

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A user is logged in with the 'Admin' role

### 3.1.5 When

The user navigates to any module (e.g., Trips, Invoicing, Users, Settings)

### 3.1.6 Then

The user has full Create, Read, Update, and Delete (CRUD) permissions on all data records and can access all system configuration settings.

### 3.1.7 Validation Notes

Verify by logging in as Admin and confirming that all menus are visible and all actions (create, edit, delete) are available on key models like Trips, Invoices, and Users.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Dispatch Manager has operational access

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A user is logged in with the 'Dispatch Manager' role

### 3.2.5 When

The user accesses the system

### 3.2.6 Then

The user has full CRUD permissions on Trip and Expense records, but has read-only access to Customer, Vehicle, and Driver records.

### 3.2.7 Validation Notes

Log in as Dispatch Manager. Confirm ability to create/edit/delete Trips. Confirm that 'Create'/'Edit' buttons are disabled/hidden on Customer and Vehicle forms. Confirm that User Management menus are not visible.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Dispatch Manager is restricted from financial and admin functions

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A user is logged in with the 'Dispatch Manager' role

### 3.3.5 When

The user attempts to access User Management or generate a final customer Invoice

### 3.3.6 Then

The system prevents the action, either by hiding the relevant menu items and buttons or by raising an access error if accessed directly.

### 3.3.7 Validation Notes

Verify that the 'Settings' and 'Invoicing' menus have restricted options. The 'Generate Invoice' button should not be available to this role.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Finance Officer has financial access

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A user is logged in with the 'Finance Officer' role

### 3.4.5 When

The user accesses the system

### 3.4.6 Then

The user has full CRUD permissions on Invoices and Payments, and can view all Trip, Customer, and Expense records.

### 3.4.7 Validation Notes

Log in as Finance Officer. Confirm full access to the Invoicing module. Confirm ability to create/validate invoices and register payments.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Finance Officer is restricted from operational functions

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A user is logged in with the 'Finance Officer' role

### 3.5.5 When

The user attempts to create or assign a new Trip

### 3.5.6 Then

The system prevents the action by hiding the 'Create' button on the Trip list view and disabling save actions on any new Trip record.

### 3.5.7 Validation Notes

Verify that the 'Create' button is not visible on the Trip list view. Attempting to create a trip via a direct URL should result in an access error.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Driver has restricted, personal access (Record-Level Security)

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A user is logged in with the 'Driver' role

### 3.6.5 When

The user navigates to the list of Trips

### 3.6.6 Then

The user can ONLY see Trip records where they are the assigned driver.

### 3.6.7 Validation Notes

Create two trips assigned to two different drivers. Log in as the first driver and verify they can only see their assigned trip and not the other.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Driver is restricted from viewing sensitive financial data (Field-Level Security)

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

A user with the 'Driver' role is viewing a Trip form assigned to them

### 3.7.5 When

The Trip form is displayed

### 3.7.6 Then

Fields such as 'Rate', 'Total Revenue', and 'Profitability' are not visible on the user interface.

### 3.7.7 Validation Notes

Inspect the Trip form view while logged in as a Driver. Confirm these specific fields are absent from the view. An API call for the record should also not return these fields for this user.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Driver can view their own compensation data

### 3.8.3 Scenario Type

Happy_Path

### 3.8.4 Given

A user with the 'Driver' role is viewing their employee profile or a trip form

### 3.8.5 When

The view is displayed

### 3.8.6 Then

Fields related to their personal compensation, such as 'Incentives Earned' and 'Expense Reimbursements', are visible to them.

### 3.8.7 Validation Notes

Log in as a Driver and navigate to a completed trip or their profile to confirm visibility of personal financial data, while company financial data remains hidden.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Menus, buttons, and actions (e.g., 'Create', 'Edit', 'Delete') must be hidden or disabled if the user does not have the required permissions.
- Specific fields on forms (e.g., financial data for drivers) must be hidden based on the user's role.

## 4.2.0 User Interactions

- Attempting to perform an unauthorized action should result in a clear, non-technical access denied message to the user.
- The system should not expose URLs or navigation paths to features a user is not authorized to access.

## 4.3.0 Display Requirements

- List views must be filtered by record rules automatically (e.g., Drivers only see their own trips).
- The user's role should be clearly identifiable for administrative and debugging purposes.

## 4.4.0 Accessibility Needs

- N/A for this story, as it is a backend/framework feature. UI changes resulting from it must adhere to existing accessibility standards.

# 5.0.0 Business Rules

- {'rule_id': 'BR-001', 'rule_description': 'A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver). Additional permissions can be granted via supplemental groups.', 'enforcement_point': 'User creation and management screen.', 'violation_handling': 'The UI should guide the Admin to select one primary role. The security implementation should correctly aggregate permissions if multiple groups are assigned.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-004

#### 6.1.1.2 Dependency Reason

Requires the ability to assign roles (security groups) to users.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Requires the Trip data model to apply security rules to.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-037

#### 6.1.3.2 Dependency Reason

Requires the Invoice data model to apply security rules to.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-053

#### 6.1.4.2 Dependency Reason

Requires the Expense data model to apply security rules to.

## 6.2.0.0 Technical Dependencies

- Odoo 18 Security Framework (ir.model.access.csv, ir.rule, XML view attributes).

## 6.3.0.0 Data Dependencies

- Definition of security groups corresponding to each user role: 'group_tms_admin', 'group_tms_dispatch_manager', 'group_tms_finance_officer', 'group_tms_driver'.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Record rules (ir.rule) must be written efficiently to avoid slow database queries, especially on list views with thousands of records. The performance impact of security rules should be negligible (<5% increase in load time) for typical operations.

## 7.2.0.0 Security

- This story is the cornerstone of the application's security. It must correctly implement the principle of least privilege.
- Security rules must be enforced at the ORM level, not just in the UI, to prevent unauthorized API access.
- No hardcoded user IDs or bypasses should be present in the code.

## 7.3.0.0 Usability

- The user interface should feel clean and uncluttered, not showing options or data that are irrelevant or inaccessible to the user's role.

## 7.4.0.0 Accessibility

*No items available*

## 7.5.0.0 Compatibility

*No items available*

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires changes across multiple modules (models, views, security files).
- Writing correct and performant Odoo record rules requires expertise.
- Thorough testing is complex and time-consuming as it requires simulating each user role.

## 8.3.0.0 Technical Risks

- An incorrectly configured record rule could either leak data or incorrectly block access for legitimate users.
- Poorly optimized record rules can cause significant performance degradation on large datasets.

## 8.4.0.0 Integration Points

- This feature integrates with every data model and UI view in the TMS module.
- It relies on Odoo's core `res.users` and `res.groups` models.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- A comprehensive test plan must be created with a matrix of Roles vs. Models vs. Permissions (CRUD).
- Log in as each role and execute the scenarios outlined in the Acceptance Criteria.
- Attempt to access restricted data via direct URL manipulation to ensure server-side enforcement.
- Verify field-level security for the Driver role on the Trip form.

## 9.3.0.0 Test Data Needs

- At least one test user account for each role (Admin, Dispatch, Finance, Driver).
- Sample data for all core models (Trips, Vehicles, etc.) with varied assignments to test record rules.

## 9.4.0.0 Testing Tools

- Odoo's built-in testing framework for automated integration tests.
- Manual testing via web browser.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing for all defined roles.
- Code for security groups, access rights (`ir.model.access.csv`), and record rules (`ir.rule`) is implemented and peer-reviewed.
- XML views are updated with `groups` attributes where necessary.
- Automated integration tests are written to verify key access restrictions (e.g., driver can only see their trips).
- A manual testing cycle has been completed by QA, logging in as each user type to confirm UI and data visibility.
- No critical security vulnerabilities related to access control are found.
- Documentation for setting up user roles is updated.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story that should be implemented early in the project, as many other features depend on it.
- Requires significant time allocation for testing across all roles.

## 11.4.0.0 Release Impact

- This is a blocking feature for any release involving multiple user types. The system cannot go live without robust access control.


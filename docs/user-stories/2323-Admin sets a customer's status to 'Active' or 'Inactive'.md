# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-018 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin sets a customer's status to 'Active' or 'Ina... |
| As A User Story | As an Admin, I want to be able to set a customer's... |
| User Persona | Admin user with full permissions to manage master ... |
| Business Value | Improves data integrity and operational efficiency... |
| Functional Area | Master Data Management |
| Story Theme | Customer Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin deactivates an active customer

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am viewing an 'Active' customer's record

### 3.1.5 When

I change the customer's status to 'Inactive' (e.g., click the 'Archive' action) and confirm

### 3.1.6 Then

the customer's record is marked as 'Inactive' and is hidden from the default customer list view

### 3.1.7 And

this customer no longer appears in the customer selection dropdown when a Dispatch Manager creates a new trip.

### 3.1.8 Validation Notes

Verify the 'active' field for the res.partner record is set to false. Verify the domain filter on the trip form's customer field excludes inactive records.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin reactivates an inactive customer

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and am viewing an 'Inactive' (Archived) customer's record

### 3.2.5 When

I change the customer's status to 'Active' (e.g., click the 'Unarchive' action)

### 3.2.6 Then

the customer's record is marked as 'Active' and appears in the default customer list view

### 3.2.7 And

this customer now appears in the customer selection dropdown when a Dispatch Manager creates a new trip.

### 3.2.8 Validation Notes

Verify the 'active' field for the res.partner record is set to true. Verify the customer is selectable on the new trip form.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Inactive customer data is retained for reporting and financial records

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

a customer with historical trips and outstanding invoices has been set to 'Inactive'

### 3.3.5 When

a Finance Officer views the customer ledger or an Admin generates a historical revenue report

### 3.3.6 Then

the inactive customer's financial data remains accessible and is included in historical reports.

### 3.3.7 And

the Finance Officer can still record payments against the customer's outstanding invoices.

### 3.3.8 Validation Notes

Check that inactive res.partner records are not filtered out of financial reporting views and that related accounting models remain fully functional.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempting to deactivate a customer with active trips

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am an Admin viewing a customer record that is associated with one or more trips in an 'Assigned' or 'In-Transit' state

### 3.4.5 When

I attempt to change the customer's status to 'Inactive'

### 3.4.6 Then

the system displays a warning modal dialog with the message 'This customer has active trips. Are you sure you want to deactivate them?'

### 3.4.7 And

I am presented with options to 'Proceed' or 'Cancel' the action.

### 3.4.8 Validation Notes

This requires overriding the 'toggle_active' method on the res.partner model to check for related trips in specific states before archiving.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Non-Admin user attempts to change customer status

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am logged in as a user without Admin privileges (e.g., Dispatch Manager)

### 3.5.5 When

I view a customer's record

### 3.5.6 Then

I do not have any UI element (e.g., button or menu option) to change the customer's 'Active'/'Inactive' status.

### 3.5.7 Validation Notes

Verify through Odoo's access control lists (ACLs) that write permission on the 'active' field of res.partner is restricted to the Admin group.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- On the customer form view, utilize Odoo's standard 'Archive'/'Unarchive' functionality, typically presented as a smart button or an item in the 'Action' menu.
- A warning modal dialog for the edge case defined in AC-004.

## 4.2.0 User Interactions

- The default customer list view should be filtered to show only active customers.
- Users should be able to remove the default 'Active' filter to search for and view inactive (archived) customers.

## 4.3.0 Display Requirements

- The form view for an inactive customer should clearly indicate its archived status, typically with a banner.
- The customer selection field on the new trip form must only display active customers.

## 4.4.0 Accessibility Needs

- The archive/unarchive controls must be keyboard accessible and have appropriate ARIA labels.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-DAT-001

### 5.1.2 Rule Description

Inactive customers must be excluded from selection for new transactional records (e.g., Trips).

### 5.1.3 Enforcement Point

At the model level via domain filters on relational fields pointing to res.partner.

### 5.1.4 Violation Handling

The inactive customer will not be present in the selection list, preventing violation.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-SEC-001

### 5.2.2 Rule Description

Only users with the 'Admin' role can modify a customer's active/inactive status.

### 5.2.3 Enforcement Point

Odoo's access control layer (ir.model.access.csv).

### 5.2.4 Violation Handling

The UI control will be hidden/disabled for unauthorized users. Any direct API call will result in a permission denied error.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-015

#### 6.1.1.2 Dependency Reason

The customer record model (res.partner extension) must exist before its status can be managed.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

The trip creation form is required to test and validate that inactive customers are correctly filtered out.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-070

#### 6.1.3.2 Dependency Reason

The system's role-based access control framework must be established to enforce the Admin-only restriction.

## 6.2.0.0 Technical Dependencies

- This story will extend the base Odoo `res.partner` model, leveraging its built-in `active` field.

## 6.3.0.0 Data Dependencies

- Requires test data including active customers, inactive customers, and customers with associated active trips and outstanding invoices.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The filtering of inactive customers in selection dropdowns should not introduce any noticeable latency (<200ms), even with over 10,000 customer records.

## 7.2.0.0 Security

- Access to modify the 'active' flag on the customer model must be strictly limited to the Admin role via Odoo's security rules.

## 7.3.0.0 Usability

- The process of archiving and unarchiving a customer should follow standard Odoo conventions to ensure a consistent and intuitive user experience.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Leverages standard Odoo 'active' field and archiving functionality.
- The only custom logic is overriding the `toggle_active` method to implement the warning for customers with active trips.

## 8.3.0.0 Technical Risks

- Minor risk of forgetting to apply the `[('active', '=', True)]` domain filter on a relational field in a different module that links to customers for new transactions.

## 8.4.0.0 Integration Points

- The primary integration point is the Trip Management module, specifically the customer selection field on the trip creation form.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify deactivation flow and its impact on the trip creation form.
- Verify reactivation flow.
- Verify that a non-admin user cannot see the archive/unarchive options.
- Verify the warning mechanism for customers with active trips.
- Verify that inactive customer data appears correctly in historical financial and operational reports.

## 9.3.0.0 Test Data Needs

- A user with Admin role.
- A user with Dispatch Manager role.
- An active customer with no active trips.
- An active customer with at least one 'In-Transit' trip.
- An inactive customer with historical invoices.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit tests for the overridden `toggle_active` method are written and achieve >80% coverage for the new logic.
- Automated integration tests confirm the domain filter on the trip form and the access control restrictions.
- UI for the warning modal is approved by the product owner.
- Security requirement (Admin-only access) is validated.
- Relevant user documentation is updated to explain the customer archiving feature.
- Story is deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational master data feature. It should be completed before or in the same sprint as the trip creation story (US-026) to ensure proper system behavior from the start.

## 11.4.0.0 Release Impact

- Core functionality for data management. Essential for the initial release (Phase 1) of the system.


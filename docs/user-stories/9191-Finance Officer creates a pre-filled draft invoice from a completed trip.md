# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-086 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer creates a pre-filled draft invoice... |
| As A User Story | As a Finance Officer, I want to automatically gene... |
| User Persona | Finance Officer |
| Business Value | Improves billing accuracy and efficiency, reduces ... |
| Functional Area | Invoicing and Financials |
| Story Theme | Trip-to-Cash Lifecycle Automation |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Generate a draft invoice from a completed trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a Finance Officer and am viewing a Trip record that is in the 'Completed' state

### 3.1.5 When

I click the 'Create Invoice' button on the trip form

### 3.1.6 Then

The system creates a new customer invoice in 'Draft' status and redirects me to the new invoice form.

### 3.1.7 Validation Notes

Verify the new invoice record exists in the 'account.move' model. Check that the user's screen navigates to this new record.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Correct data mapping from Trip to Invoice

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A new draft invoice has been generated from a trip record

### 3.2.5 When

I view the newly created draft invoice

### 3.2.6 Then

The invoice's 'Customer' field must match the trip's 'Customer'.

### 3.2.7 Validation Notes

Compare `invoice.partner_id` with `trip.customer_id`.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Correct invoice line item creation

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A new draft invoice has been generated from a trip record

### 3.3.5 When

I view the invoice lines of the new draft invoice

### 3.3.6 Then

There is at least one invoice line with a description formatted as 'Transport services for Trip #[Trip ID] from [Source] to [Destination]'.

### 3.3.7 Validation Notes

Check the `invoice_line_ids` for a line with a description containing the source trip's ID, source, and destination.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Correct rate mapping to invoice line

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A new draft invoice has been generated from a trip record

### 3.4.5 When

I view the invoice lines of the new draft invoice

### 3.4.6 Then

The 'Unit Price' of the invoice line must match the 'Rate' from the trip record.

### 3.4.7 Validation Notes

Compare `invoice_line.price_unit` with `trip.rate`.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Trip record is linked to the new invoice

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

A new draft invoice has been generated from a trip record

### 3.5.5 When

I view the source trip record after the invoice is created

### 3.5.6 Then

The trip record now contains a direct link or smart button (e.g., 'View Invoice') that navigates to the generated invoice.

### 3.5.7 Validation Notes

A `Many2one` or similar field on the trip model should now be populated with the ID of the new invoice.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Prevent invoice creation for non-completed trips

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am logged in as a Finance Officer and am viewing a Trip record

### 3.6.5 When

The trip's status is anything other than 'Completed' (e.g., 'Planned', 'In-Transit', 'Canceled')

### 3.6.6 Then

The 'Create Invoice' button is not visible or is disabled.

### 3.6.7 Validation Notes

Check the trip form view for trips in various states to confirm the button's visibility/state.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Prevent duplicate invoice creation

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

I am viewing a 'Completed' trip for which an invoice has already been generated

### 3.7.5 When

I view the trip form

### 3.7.6 Then

The 'Create Invoice' button is hidden, and a 'View Invoice' button/link is displayed instead.

### 3.7.7 Validation Notes

Create an invoice for a trip, then revisit the trip form to ensure the button has changed.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Create Invoice' button on the Trip form view header.
- A smart button or link on the Trip form view, 'View Invoice', which appears after an invoice is created.

## 4.2.0 User Interactions

- Clicking 'Create Invoice' triggers the invoice creation process and redirects the user.
- The 'Create Invoice' button's visibility is conditional based on the trip's status and whether an invoice already exists.

## 4.3.0 Display Requirements

- The newly created invoice must be displayed in 'Draft' mode, allowing for edits before validation.
- The invoice line must clearly reference the source trip details.

## 4.4.0 Accessibility Needs

- The 'Create Invoice' button must be keyboard accessible and have a descriptive ARIA label.

# 5.0.0 Business Rules

- {'rule_id': 'BR-010', 'rule_description': "An invoice can only be generated for a trip that is in the 'Completed' state.", 'enforcement_point': 'UI level (button visibility) and backend logic before creating the invoice record.', 'violation_handling': 'The action to create an invoice is not presented to the user for non-completed trips. If triggered via API, an error should be raised.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-015

#### 6.1.1.2 Dependency Reason

Requires the Customer model (`res.partner`) to be defined to associate the invoice with a customer.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Requires the Trip model and its fields (Customer, Rate, Source, Destination, Status) to be implemented as the source of data.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-037

#### 6.1.3.2 Dependency Reason

This story (US-086) is a prerequisite for US-037. A draft invoice must be created before it can be validated and sent for e-invoicing.

## 6.2.0.0 Technical Dependencies

- Odoo's core Accounting module (`account`) which provides the `account.move` model for invoices.
- The custom TMS module containing the Trip model.

## 6.3.0.0 Data Dependencies

- Requires test data for Trips in a 'Completed' state.
- Requires test data for Customers (`res.partner`) with complete billing information.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The invoice creation and redirection process should complete in under 1 second to provide a responsive user experience.

## 7.2.0.0 Security

- Access to the 'Create Invoice' functionality must be restricted to authorized roles (e.g., 'Finance Officer', 'Admin') using Odoo's standard access control lists (ACLs).

## 7.3.0.0 Usability

- The process should be intuitive, requiring only a single click to generate the draft invoice, minimizing cognitive load on the user.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard Odoo workflow: adding a button to a view that calls a Python method.
- The logic involves reading from one model (`tms.trip`) and creating a record in another (`account.move`).
- Requires adding a `Many2one` field to the `tms.trip` model to store a reference to the created invoice.
- The logic for conditional UI element visibility is standard in Odoo XML views.

## 8.3.0.0 Technical Risks

- The logic for selecting the correct default GST tax on the invoice line might be complex if not configured properly in Odoo's accounting settings (Fiscal Positions).

## 8.4.0.0 Integration Points

- Direct integration with Odoo's `account.move` model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify invoice creation from a 'Completed' trip.
- Verify the 'Create Invoice' button is hidden/disabled for trips in 'Planned', 'Assigned', 'In-Transit', and 'Canceled' states.
- Verify that attempting to create a second invoice for the same trip is prevented and the UI updates to show a 'View Invoice' link.
- Verify all data fields (customer, rate, description) are correctly mapped to the new invoice.
- Verify the reverse link from the trip to the invoice is correctly established.

## 9.3.0.0 Test Data Needs

- Multiple trip records in various lifecycle states.
- Customer records with and without specific fiscal positions to test tax mapping.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the invoice creation method are written and achieve >80% coverage
- Integration testing completed successfully in a staging environment
- User interface changes on the Trip form view are reviewed and approved by the Product Owner
- Functionality is verified to be restricted to the correct user roles
- Relevant technical documentation (if any) is updated
- Story is deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a foundational piece for the financial workflow and a blocker for the e-invoicing feature (US-087). It should be prioritized early in the development of the financial module.

## 11.4.0.0 Release Impact

- Enables the core billing function of the TMS. Without this, the entire invoicing process would be manual and error-prone.


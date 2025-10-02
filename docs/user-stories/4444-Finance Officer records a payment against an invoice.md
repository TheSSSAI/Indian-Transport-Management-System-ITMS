# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-039 |
| Elaboration Date | 2025-01-17 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer records a payment against an invoi... |
| As A User Story | As a Finance Officer, I want to record partial or ... |
| User Persona | Finance Officer: A user responsible for managing f... |
| Business Value | Enables accurate tracking of accounts receivable a... |
| Functional Area | Financial Management |
| Story Theme | Invoicing and Payments |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Record a full payment against an invoice

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am viewing a customer invoice that is in the 'Posted' state with an outstanding balance of ₹50,000

### 3.1.5 When

I click 'Register Payment' and confirm a payment of ₹50,000

### 3.1.6 Then

The invoice's 'Amount Due' should be updated to ₹0, the invoice status should change to 'Paid', and a corresponding payment record should be created and reconciled with the invoice.

### 3.1.7 Validation Notes

Verify the invoice form view shows the 'Paid' ribbon. Check the customer's ledger (Partner Ledger report) to confirm their balance has been reduced by ₹50,000.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Record a partial payment against an invoice

### 3.2.3 Scenario Type

Alternative_Flow

### 3.2.4 Given

I am viewing a customer invoice that is in the 'Posted' state with an outstanding balance of ₹50,000

### 3.2.5 When

I click 'Register Payment' and confirm a payment of ₹20,000

### 3.2.6 Then

The invoice's 'Amount Due' should be updated to ₹30,000, the invoice status should remain 'Posted' (but show it is partially paid), and a payment record of ₹20,000 should be created and linked to the invoice.

### 3.2.7 Validation Notes

Verify the invoice form view shows the updated 'Amount Due'. The customer's ledger should reflect a reduction of ₹20,000 in their outstanding balance.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Record a second partial payment to fully pay an invoice

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

I am viewing a customer invoice with an outstanding balance of ₹30,000 (from AC-002)

### 3.3.5 When

I click 'Register Payment' and confirm a payment of ₹30,000

### 3.3.6 Then

The invoice's 'Amount Due' should be updated to ₹0 and the invoice status should change to 'Paid'.

### 3.3.7 Validation Notes

Verify the invoice now has two payment records linked to it, totaling the full invoice amount.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to record a payment with an invalid amount

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am in the 'Register Payment' wizard for an invoice

### 3.4.5 When

I enter an amount of '0' or a negative number and try to confirm the payment

### 3.4.6 Then

The system must display a validation error message stating that the payment amount must be greater than zero, and the payment should not be created.

### 3.4.7 Validation Notes

Test with '0', '-100', and a non-numeric string. The wizard should prevent submission and provide clear user feedback.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to record a payment on a fully paid invoice

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am viewing an invoice that is already in the 'Paid' state

### 3.5.5 When

I look for the payment registration action

### 3.5.6 Then

The 'Register Payment' button must not be visible or must be disabled.

### 3.5.7 Validation Notes

Check the form view for an invoice with status 'Paid' and 'Canceled'. The button should not be present.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Record an overpayment against an invoice

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

I am viewing a customer invoice with an outstanding balance of ₹50,000

### 3.6.5 When

I click 'Register Payment' and confirm a payment of ₹60,000

### 3.6.6 Then

The system should process the payment, mark the invoice as 'Paid', and create a credit of ₹10,000 on the customer's account.

### 3.6.7 Validation Notes

Verify the invoice is marked 'Paid'. Check the customer's ledger to confirm they have an outstanding credit of ₹10,000 that can be applied to future invoices.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Register Payment' button on the `account.move` form view for invoices.
- The standard Odoo `account.payment.register` wizard (modal dialog).
- Fields in the wizard: Journal (Payment Method), Amount, Payment Date, Memo.
- A 'Paid' ribbon/widget on the invoice form view to clearly indicate its status.

## 4.2.0 User Interactions

- The 'Register Payment' button should only be active for invoices in the 'Posted' state.
- The payment amount in the wizard should default to the invoice's remaining 'Amount Due'.
- Upon successful payment, the user is returned to the invoice view, which should be refreshed to show the new status and balance.

## 4.3.0 Display Requirements

- The invoice form must clearly display the 'Total', 'Amount Due', and any payments made.
- A list of all payments applied to the invoice should be easily accessible from the invoice view (e.g., in a separate tab or via a smart button).

## 4.4.0 Accessibility Needs

- The 'Register Payment' button and all wizard fields must be keyboard accessible and have proper labels for screen readers, adhering to WCAG 2.1 Level AA.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-PAY-001

### 5.1.2 Rule Description

A payment can only be registered against an invoice that is in a 'Posted' state.

### 5.1.3 Enforcement Point

UI (button visibility/state) and backend validation.

### 5.1.4 Violation Handling

The action to register a payment is not available to the user for invoices in other states (e.g., Draft, Paid, Canceled).

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-PAY-002

### 5.2.2 Rule Description

The payment amount must be a positive numerical value.

### 5.2.3 Enforcement Point

Validation within the payment registration wizard.

### 5.2.4 Violation Handling

Display an error message to the user and prevent the creation of the payment record.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-037

#### 6.1.1.2 Dependency Reason

An invoice must be created and posted before a payment can be recorded against it. This story provides the invoice object that this payment story acts upon.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-015

#### 6.1.2.2 Dependency Reason

A customer record (`res.partner`) must exist to associate the invoice and subsequent payment with.

## 6.2.0.0 Technical Dependencies

- Odoo 18 Accounting module (`account`).
- Proper configuration of Chart of Accounts and Payment Journals within Odoo.

## 6.3.0.0 Data Dependencies

- Requires at least one customer record.
- Requires at least one posted invoice record for testing.
- Requires at least one configured Payment Journal (e.g., 'Bank').

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The payment registration wizard should load in under 1 second.
- Processing the payment and updating the invoice status should complete within 2 seconds.

## 7.2.0.0 Security

- Only users with the 'Finance Officer' role (or equivalent accounting permissions) can access the 'Register Payment' functionality.
- All payment transactions must be logged in the system's audit trail (handled by Odoo core).

## 7.3.0.0 Usability

- The process of recording a payment should be intuitive, requiring minimal clicks from the invoice view.
- Error messages for invalid data entry must be clear and actionable.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be fully supported on modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This functionality leverages the standard, built-in Odoo payment registration wizard (`account.payment.register`).
- No new data models are required.
- The primary effort involves ensuring the action is correctly placed on the custom TMS invoice view and that the 'Finance Officer' role has the necessary access rights.

## 8.3.0.0 Technical Risks

- Minimal risk. A potential issue could be incorrect Odoo access rights configuration, preventing the Finance Officer from seeing the button or completing the action.

## 8.4.0.0 Integration Points

- Odoo `account.move` model (Invoice).
- Odoo `account.payment` model (Payment).
- Odoo `res.partner` model (Customer Ledger).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Integration
- E2E
- Security (Role-based access)

## 9.2.0.0 Test Scenarios

- Full end-to-end flow: Create Trip -> Generate Invoice -> Post Invoice -> Register Partial Payment -> Register Final Payment -> Verify Invoice is Paid.
- Verify that a user without the 'Finance Officer' role cannot see the 'Register Payment' button.
- Test payment registration using different journals (e.g., Bank, Cash).
- Test the overpayment scenario and confirm the credit is correctly applied to the customer's account.

## 9.3.0.0 Test Data Needs

- A test user with the 'Finance Officer' role.
- A test user without financial permissions.
- Multiple customer records.
- Posted invoices with various amounts.
- At least two configured payment journals.

## 9.4.0.0 Testing Tools

- Odoo's built-in testing framework.
- Manual testing via the Odoo UI.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by the development team.
- Unit and integration tests implemented and passing with sufficient coverage.
- Role-based access controls for this feature are verified.
- The feature is successfully tested end-to-end in a staging environment.
- Any necessary user documentation or training material is updated.
- The story is deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a critical part of the core financial loop and should be prioritized immediately after the invoice generation story (US-037).
- Requires that the Odoo accounting module is installed and basic configuration (journals) is complete.

## 11.4.0.0 Release Impact

- Completes the basic accounts receivable cycle. Without this story, the system cannot track actual revenue collection.


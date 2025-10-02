# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-015 |
| Elaboration Date | 2024-07-23 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates a new customer record |
| As A User Story | As an Admin, I want to create a new customer recor... |
| User Persona | Admin: A user with full system access responsible ... |
| Business Value | Enables new business by onboarding clients into th... |
| Functional Area | Master Data Management |
| Story Theme | Customer Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful creation of a new customer with valid data

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

The Admin is logged into the system and has navigated to the Customer management screen

### 3.1.5 When

The Admin clicks the 'Create' button, fills in all mandatory fields (Customer Name, Billing Address, GSTIN, Contact Person) with valid data, and clicks 'Save'

### 3.1.6 Then

The system successfully creates a new customer record, the record is saved to the database, and the Admin is viewing the form of the newly created customer.

### 3.1.7 Validation Notes

Verify the new customer record exists in the database and is searchable. Confirm the data saved matches the data entered.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempt to save a new customer with an invalid GSTIN format

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

The Admin is on the new customer creation form

### 3.2.5 When

The Admin enters a GSTIN that does not match the standard Indian format (e.g., 'ABCDE1234F1Z' instead of '22ABCDE1234F1Z5') and attempts to save

### 3.2.6 Then

The system prevents the record from being saved and displays a clear, user-friendly error message next to the GSTIN field, such as 'Invalid GSTIN format. Please enter a valid 15-digit GSTIN.'

### 3.2.7 Validation Notes

Test with multiple invalid formats: incorrect length, wrong character types, invalid checksum (if implemented).

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to save a new customer with a missing mandatory field

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

The Admin is on the new customer creation form

### 3.3.5 When

The Admin leaves the 'Customer Name' field blank but fills in other details and attempts to save

### 3.3.6 Then

The system prevents the record from being saved, highlights the 'Customer Name' field, and displays a validation message indicating that the field is required.

### 3.3.7 Validation Notes

Test this for each mandatory field defined in the system (e.g., Billing Address, GSTIN).

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

New customer defaults to 'Active' status

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A new customer record has been successfully created via the process in AC-001

### 3.4.5 When

The Admin or another authorized user views the newly created customer record

### 3.4.6 Then

The 'Status' field for the customer is automatically set to 'Active' by default.

### 3.4.7 Validation Notes

Inspect the customer record's form view and database value to confirm the default status is 'Active'.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Functionality extends the standard Odoo partner model

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

The TMS module is installed in the Odoo instance

### 3.5.5 When

The Admin navigates to the standard Odoo 'Contacts' application to create a new partner/customer

### 3.5.6 Then

The form view for the partner correctly includes the TMS-specific fields and validation logic, such as the GSTIN format check.

### 3.5.7 Validation Notes

Confirm that creating a customer through the standard Odoo menu inherits all the functionality specified in this user story.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Input field for 'Customer Name' (Text, Mandatory)
- Input field for 'Billing Address' (Address block, Mandatory)
- Input field for 'GSTIN' (Text, Mandatory)
- Input field for 'Contact Person' (Text, Mandatory)
- Read-only field or toggle for 'Status' (Default: Active)
- 'Save' and 'Discard' buttons

## 4.2.0 User Interactions

- Mandatory fields are visually indicated (e.g., bold label).
- Validation errors for fields like GSTIN should appear on blur or form submission.
- Upon successful save, the user remains on the form view of the newly created record.

## 4.3.0 Display Requirements

- The customer creation form must be consistent with the standard Odoo 18 UI/UX.
- Error messages must be clear, concise, and displayed near the relevant input field.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The form must be navigable using a keyboard.
- Error states must be communicated to assistive technologies.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-GSTIN-FORMAT

### 5.1.2 Rule Description

The GSTIN field must conform to the standard 15-character format for Indian Goods and Services Tax Identification Numbers.

### 5.1.3 Enforcement Point

Client-side (on blur) and Server-side (on save) validation of the customer creation form.

### 5.1.4 Violation Handling

Prevent form submission and display a specific error message to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-MANDATORY-FIELDS

### 5.2.2 Rule Description

A new customer record cannot be saved without a Customer Name, Billing Address, and GSTIN.

### 5.2.3 Enforcement Point

Server-side validation upon attempting to save the record.

### 5.2.4 Violation Handling

Prevent form submission and highlight the required fields that are missing data.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

*No items available*

## 6.2.0 Technical Dependencies

- Odoo 18 Framework
- Odoo `res.partner` base model

## 6.3.0 Data Dependencies

*No items available*

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The customer creation form should load in under 3 seconds.
- The save operation (server-side processing and database commit) should complete in under 200ms as per REQ-NFR-001.

## 7.2.0 Security

- Access to create, view, edit, and delete customer records must be controlled by Odoo's Role-Based Access Control (RBAC).
- This specific creation functionality must be granted to the 'Admin' role.
- All data must be sanitized to prevent XSS and other injection attacks.

## 7.3.0 Usability

- The workflow for creating a customer should be intuitive and require minimal training for an Odoo user.
- Error messages must be constructive and guide the user to correct the input.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards, as per REQ-INT-001.

## 7.5.0 Compatibility

- The feature must be fully functional on modern web browsers (Chrome, Firefox, Safari, Edge) supported by Odoo 18.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Involves extending a standard, well-documented Odoo model (`res.partner`).
- UI is a standard Odoo form view, requiring minimal custom OWL development.
- Validation logic for GSTIN is straightforward (e.g., regex).

## 8.3.0 Technical Risks

- Minimal risk. A potential but unlikely risk is creating conflicts if another third-party module also modifies the `res.partner` model in an incompatible way.

## 8.4.0 Integration Points

- The created customer record (`res.partner`) will be a foreign key in the 'Trip' model.
- The customer record will be used by the Odoo 'Invoicing' module to generate invoices.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Create a customer with all valid data.
- Attempt to create a customer with various invalid GSTINs.
- Attempt to create a customer with each mandatory field left blank one at a time.
- Verify that the new customer is available for selection in the 'Create Trip' form (integration test).
- Verify that a user without the 'Admin' role cannot access the create customer functionality.

## 9.3.0 Test Data Needs

- A set of valid Indian GSTINs.
- A set of invalid GSTINs (wrong length, invalid characters, etc.).
- Sample customer names and addresses.

## 9.4.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main development branch.
- Unit tests for GSTIN validation logic are written and achieve >80% coverage.
- Integration tests confirm the extended `res.partner` model functions correctly.
- UI has been reviewed for consistency with Odoo's design language.
- Security check confirms that access is restricted to authorized roles.
- Relevant technical documentation (e.g., model extensions) is updated.
- The story has been demonstrated to the Product Owner and accepted.

# 11.0.0 Planning Information

## 11.1.0 Story Points

2

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational story and a prerequisite for trip management (US-026) and invoicing (US-037). It should be scheduled in one of the earliest sprints.

## 11.4.0 Release Impact

- This feature is critical for the Phase 1 (Core Operations) rollout as defined in REQ-TRN-001.


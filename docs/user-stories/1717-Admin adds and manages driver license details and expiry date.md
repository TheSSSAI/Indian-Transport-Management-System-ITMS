# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-012 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin adds and manages driver license details and ... |
| As A User Story | As an Admin, I want to add and edit a driver's lic... |
| User Persona | Admin: A user with full system access responsible ... |
| Business Value | Enables enforcement of critical business rule BR-0... |
| Functional Area | Master Data Management |
| Story Theme | Driver Master Data |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successfully add license details to a new driver record

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am an Admin logged into the system and I am viewing a driver's employee record that has no license information

### 3.1.5 When

I enter a valid, unique string in the 'License Number' field, select a future date in the 'License Expiry Date' field, and save the record

### 3.1.6 Then

The system saves the record without errors, and the new license number and expiry date are correctly displayed when I reopen the record.

### 3.1.7 Validation Notes

Verify by navigating to the driver's record, entering the data, saving, and then re-loading the form to confirm the data persistence.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Successfully edit existing license details

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am an Admin viewing a driver's record that already contains a license number and expiry date

### 3.2.5 When

I change the value in the 'License Number' field and select a new future date in the 'License Expiry Date' field, and save the record

### 3.2.6 Then

The system updates the record with the new information, which is correctly displayed upon reloading the form.

### 3.2.7 Validation Notes

Find a record with existing data, modify both fields, save, and verify the new values are present.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

System prevents saving with a past expiry date

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am an Admin editing a driver's record

### 3.3.5 When

I attempt to save the record after selecting a date in the past for the 'License Expiry Date'

### 3.3.6 Then

The system must prevent the save operation and display a user-friendly validation error message, such as 'License expiry date cannot be in the past.'

### 3.3.7 Validation Notes

Use the date picker to select yesterday's date and attempt to save. Confirm the error message appears and the record is not saved.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

System requires license number if expiry date is provided

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am an Admin editing a driver's record

### 3.4.5 When

I leave the 'License Number' field blank but select a date for the 'License Expiry Date' and attempt to save

### 3.4.6 Then

The system must prevent the save operation and display a validation error message, such as 'License Number is required if an expiry date is set.'

### 3.4.7 Validation Notes

Clear the license number field, add an expiry date, and try to save. Verify the error and that the save fails.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

System allows saving with a license number but no expiry date

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am an Admin editing a driver's record

### 3.5.5 When

I enter a value in the 'License Number' field but leave the 'License Expiry Date' field empty and save the record

### 3.5.6 Then

The system successfully saves the record with the license number.

### 3.5.7 Validation Notes

Enter a license number, ensure the expiry date is empty, and save. Verify the record saves correctly.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Non-Admin roles cannot edit license details

### 3.6.3 Scenario Type

Security

### 3.6.4 Given

I am logged in as a user with a 'Dispatch Manager' or 'Finance Officer' role and am viewing a driver's record

### 3.6.5 When

I navigate to the section containing the license details

### 3.6.6 Then

The 'License Number' and 'License Expiry Date' fields must be read-only or not visible, and I cannot modify them.

### 3.6.7 Validation Notes

Log in with a test user for each non-admin role and attempt to edit the fields on a driver's record.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A text input field for 'License Number'.
- A date picker widget for 'License Expiry Date'.

## 4.2.0 User Interactions

- The fields should be placed within the `hr.employee` form view, ideally under a new tab or page titled 'Driver Details' or 'Compliance Information'.
- Standard Odoo validation error messages should appear near the respective fields upon failed validation.

## 4.3.0 Display Requirements

- The date format displayed should be consistent with the user's locale settings in Odoo.

## 4.4.0 Accessibility Needs

- All new fields must have associated `<label>` tags for screen reader compatibility, adhering to WCAG 2.1 standards as per REQ-INT-001.

# 5.0.0 Business Rules

- {'rule_id': 'BR-003', 'rule_description': 'A driver with an expired license cannot be assigned to a new trip. This story provides the data needed to enforce this rule elsewhere.', 'enforcement_point': 'Trip Assignment (covered in another story, e.g., US-027, US-074)', 'violation_handling': 'System prevents assignment and shows an error.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-011', 'dependency_reason': 'This story adds fields to a driver record. The functionality to create the base driver record (extending hr.employee) must exist first.'}

## 6.2.0 Technical Dependencies

- Requires inheritance of the Odoo `hr.employee` model and its corresponding form view (`hr.employee_form_view`).

## 6.3.0 Data Dependencies

- Relies on the existence of `hr.employee` records in the database.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- Saving the driver record with new license details should complete in under 200ms, consistent with standard Odoo form save operations (REQ-NFR-001).

## 7.2.0 Security

- Access to view and edit these fields must be restricted to the 'Admin' role, enforced via Odoo's access control lists (ACLs) and record rules (REQ-FNC-001).

## 7.3.0 Usability

- The new fields should be logically grouped on the driver form to be intuitive for the Admin user.

## 7.4.0 Accessibility

- The UI must adhere to WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0 Compatibility

- Functionality must be fully supported on modern web browsers (Chrome, Firefox, Safari, Edge) on both desktop and mobile, as per the mobile-friendly requirement (REQ-SCP-001).

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Standard Odoo development pattern: inheriting a model to add fields and a view to display them.
- Validation logic can be implemented using standard Odoo `@api.constrains`.

## 8.3.0 Technical Risks

- Minimal risk. A potential for an XPath conflict in the view inheritance if another custom module modifies the same part of the `hr.employee` form, but this is easily resolved.

## 8.4.0 Integration Points

- This story modifies the `hr.employee` model, which is a core Odoo model. The new fields will be available via the ORM for other parts of the TMS module to use (e.g., for trip assignment validation and expiry alerts).

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Verify successful creation and editing of license details.
- Verify validation failure for past expiry dates.
- Verify validation failure for missing license number when date is present.
- Verify role-based access control for non-Admin users.
- Verify data persistence after saving and reloading the form.

## 9.3.0 Test Data Needs

- User accounts for 'Admin', 'Dispatch Manager', and 'Finance Officer' roles.
- At least two `hr.employee` records to test adding and editing.

## 9.4.0 Testing Tools

- Pytest for unit tests of the model constraints.
- Odoo's built-in testing framework for integration tests.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing in the staging environment.
- Code has been peer-reviewed and merged into the main development branch.
- Unit tests for the model constraints have been written and achieve >80% coverage for the new logic.
- Integration tests confirm the form view saves and loads data correctly.
- UI changes have been reviewed and approved by the product owner.
- Security requirements (role-based access) have been manually tested and verified.
- Relevant technical documentation (if any) has been updated.
- The story has been successfully deployed and verified on the staging environment.

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational story for driver compliance. It is a prerequisite for US-074 (System prevents assignment of a driver with an expired license) and US-079 (System generates alerts for an upcoming driver license expiry). It should be prioritized early in the development cycle.

## 11.4.0 Release Impact

This feature is a core component of the Driver Master data model and is essential for the initial release (Phase 1) of the TMS.


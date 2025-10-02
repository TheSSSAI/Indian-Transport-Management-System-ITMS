# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-011 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates a new driver record by extending an ... |
| As A User Story | As an Admin, I want to create a new driver record ... |
| User Persona | Admin user with full system access to manage maste... |
| Business Value | Enables the creation of a compliant and operationa... |
| Functional Area | Master Data Management |
| Story Theme | Driver Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-011-01

### 3.1.2 Scenario

Successfully designate an existing HR employee as a driver with all required information

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am on the form view of an 'hr.employee' record that is not yet designated as a driver

### 3.1.5 When

I enable a flag (e.g., a checkbox 'Is a Driver'), enter a valid 'License Number' and a future 'License Expiry Date', and save the record

### 3.1.6 Then

The system saves the employee record successfully, the driver-specific fields are visible and contain the saved data, and this employee now appears in the list of available drivers for trip assignments.

### 3.1.7 Validation Notes

Verify by navigating to the Trip creation form and checking if the newly designated driver is present in the driver selection dropdown. Re-open the employee form to confirm data persistence.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-011-02

### 3.2.2 Scenario

Attempt to save a driver record without mandatory fields

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am logged in as an Admin and have enabled the 'Is a Driver' flag on an employee's form

### 3.2.5 When

I attempt to save the record without entering a 'License Number'

### 3.2.6 Then

The system prevents the save operation and displays a user-friendly validation error message indicating that the 'License Number' is a required field.

### 3.2.7 Validation Notes

Repeat this test for the 'License Expiry Date' field to ensure it is also mandatory.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-011-03

### 3.3.2 Scenario

New driver record defaults to 'Active' status

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am logged in as an Admin and am designating an employee as a driver for the first time

### 3.3.5 When

I successfully save the record with all mandatory driver information

### 3.3.6 Then

The system automatically sets the driver's status to 'Active' by default.

### 3.3.7 Validation Notes

Check the value of the 'Status' field on the newly created driver record. It should be 'Active'.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-011-04

### 3.4.2 Scenario

Driver-specific fields are hidden for non-driver employees

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

I am logged in as an Admin and am viewing the form of an 'hr.employee' record

### 3.4.5 When

The 'Is a Driver' flag is not enabled

### 3.4.6 Then

The fields for 'License Number', 'License Expiry Date', 'License Scan', and 'Driver Status' are not visible on the form.

### 3.4.7 Validation Notes

Toggle the 'Is a Driver' flag on and off to confirm the conditional visibility of the driver-specific section.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-011-05

### 3.5.2 Scenario

Entering a past date for license expiry

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

I am logged in as an Admin and creating a new driver record

### 3.5.5 When

I enter a 'License Expiry Date' that is in the past and save the record

### 3.5.6 Then

The system should display a non-blocking warning message to the user (e.g., 'Warning: License has expired'), but it must still allow the record to be saved.

### 3.5.7 Validation Notes

This allows for entering historical data. The system should correctly save the past date. The business rule BR-003 will handle the operational restriction.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A boolean field (e.g., checkbox) labeled 'Is a Driver' on the `hr.employee` form.
- A new tab or section on the `hr.employee` form labeled 'TMS Driver Information'.
- Input field for 'License Number' (Text).
- Date picker for 'License Expiry Date'.
- File upload widget for 'License Scan'.
- Selection/dropdown for 'Driver Status' with options ('Active', 'Inactive').

## 4.2.0 User Interactions

- The 'TMS Driver Information' section should only become visible when the 'Is a Driver' checkbox is ticked.
- Standard Odoo validation feedback (e.g., red highlighting) should be used for mandatory fields.

## 4.3.0 Display Requirements

- The driver-specific information should be logically grouped together and clearly separated from standard HR information.

## 4.4.0 Accessibility Needs

- All new form fields must have associated labels for screen reader compatibility, adhering to WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

- {'rule_id': 'BR-003', 'rule_description': "A driver with an expired license cannot be assigned to a new trip. This story provides the data point ('License Expiry Date') for this rule to be enforced elsewhere.", 'enforcement_point': 'Trip Assignment (Handled in US-074)', 'violation_handling': 'The driver will not appear in the list of available drivers for assignment if their license is expired.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

*No items available*

## 6.2.0 Technical Dependencies

- The Odoo `hr` module must be installed and accessible.
- The implementation requires inheriting and extending the `hr.employee` model and its corresponding form view.

## 6.3.0 Data Dependencies

- Requires the existence of `hr.employee` records to be converted into drivers.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- Loading the `hr.employee` form with the additional TMS fields should not increase the page load time by more than 10% compared to the baseline.

## 7.2.0 Security

- Access to create or modify the driver-specific fields ('License Number', 'Expiry Date', etc.) must be restricted to the 'Admin' role via Odoo's access control lists (`ir.model.access.csv`) and record rules.
- The uploaded license scan is considered PII and must be stored securely in the configured object storage (Amazon S3) with appropriate access controls, as per REQ-DAT-007.

## 7.3.0 Usability

- The process of converting an employee to a driver should be intuitive and require minimal clicks.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0 Compatibility

- The feature must render and function correctly on all supported modern web browsers.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- This involves a standard Odoo development pattern: inheriting an existing model and view.
- The business logic is straightforward, primarily involving field additions and conditional UI visibility.
- No complex integrations are required for this specific story.

## 8.3.0 Technical Risks

- Potential for view conflicts if other custom modules also modify the `hr.employee` form. A code review should check for other inheritances of the same view.

## 8.4.0 Integration Points

- The extended `hr.employee` model will be a data source for the Trip Management module (for driver selection).
- The 'License Expiry Date' field will be used by the System Alerts module (REQ-REP-004) to generate notifications.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Create a driver from a new employee.
- Convert an existing employee to a driver.
- Attempt to save without required license info.
- Verify a new driver appears in the trip assignment dropdown.
- Verify a non-driver employee does not appear in the trip assignment dropdown.
- Upload and then download a license scan file.

## 9.3.0 Test Data Needs

- A set of `hr.employee` records that are not yet drivers.
- Sample license scan files (e.g., JPG, PNG, PDF) for upload testing.

## 9.4.0 Testing Tools

- Pytest for Odoo unit tests.
- Manual testing via the Odoo web interface.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by a senior developer
- Unit tests for model validation logic are implemented with >= 80% coverage and are passing
- Integration testing completed to ensure the new driver is available for trip assignment
- User interface changes on the `hr.employee` form are reviewed and approved by the product owner
- Security rules restricting access to the 'Admin' role are implemented and verified
- Technical documentation for the model extension is added to the codebase
- Story deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

2

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational story for the Driver and Trip management epics. It should be prioritized in an early sprint as it is a blocker for US-027, US-074, and US-079.

## 11.4.0 Release Impact

- This feature is critical for the initial release (Phase 1) as it enables the core operational workflow of the TMS.


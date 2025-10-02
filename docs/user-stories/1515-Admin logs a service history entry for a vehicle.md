# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-010 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin logs a service history entry for a vehicle |
| As A User Story | As an Admin, I want to create, view, and manage de... |
| User Persona | Admin. This functionality is critical for fleet ma... |
| Business Value | Provides a centralized and accurate record of all ... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successfully create a new service history entry

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am an Admin logged into the system and I am viewing the form for a specific vehicle

### 3.1.5 When

I navigate to the 'Service History' tab and click 'Add a new service entry'

### 3.1.6 And

I fill in all mandatory fields (Service Date, Service Type, Cost, Odometer Reading) with valid data and click 'Save'

### 3.1.7 Then

The new service entry is created and appears in the 'Service History' list for that vehicle, sorted with the most recent entry at the top.

### 3.1.8 Validation Notes

Verify the record is created in the database (`tms.vehicle.service.log` table) and correctly linked to the vehicle. The UI list should update immediately.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

View and edit an existing service history entry

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am an Admin viewing the 'Service History' list for a vehicle

### 3.2.5 When

I click on an existing service entry

### 3.2.6 Then

The entry is updated with the new information, and the list view reflects the change.

### 3.2.7 And

When I change a value (e.g., the cost) and click 'Save'

### 3.2.8 Validation Notes

Confirm the database record is updated. Check the audit trail (REQ-DAT-008) if implemented, to see the change logged.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to save a service entry with a future date

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am an Admin creating a new service entry

### 3.3.5 When

I enter a date in the future for the 'Service Date' field and attempt to save

### 3.3.6 Then

The system must prevent the record from being saved and display a user-friendly validation error message, such as 'Service Date cannot be in the future'.

### 3.3.7 Validation Notes

Test with dates one day in the future and one year in the future. The form should remain open for correction.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to save a service entry with invalid numeric data

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am an Admin creating a new service entry

### 3.4.5 When

I enter a negative number or non-numeric text in the 'Cost' or 'Odometer Reading' fields and attempt to save

### 3.4.6 Then

The system must prevent saving and display a validation error message indicating that the fields must be positive numbers.

### 3.4.7 Validation Notes

Test with values like '-100', 'abc', and '0'. The field should be highlighted.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Upload a valid attachment to a service entry

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I am an Admin creating or editing a service entry

### 3.5.5 When

I use the file upload widget to attach a valid file (e.g., a 2MB PDF or JPG)

### 3.5.6 And

I save the service entry

### 3.5.7 Then

The file is successfully attached to the record and can be downloaded or viewed later.

### 3.5.8 Validation Notes

Verify the attachment is stored in the configured location (Amazon S3 as per REQ-DEP-001) and linked correctly in Odoo's `ir.attachment` model.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Attempt to upload an invalid attachment

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am an Admin creating or editing a service entry

### 3.6.5 When

I attempt to upload a file that is larger than 5MB or has an unsupported file type (e.g., .zip, .exe)

### 3.6.6 Then

The system must reject the upload and display an error message specifying the allowed file types (JPG, PNG, PDF) and the maximum size (5MB).

### 3.6.7 Validation Notes

Test with a 6MB PDF and a 1MB .txt file. The error should appear before the record is saved.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Service History' tab or section within the Vehicle form view.
- A list/tree view to display existing service entries, showing at least 'Service Date', 'Service Type', and 'Cost'.
- An 'Add' or 'Create' button to initiate a new service entry.
- A form view for creating/editing a service entry with fields for: Service Date (date picker), Service Type (dropdown/selection), Cost (numeric), Odometer Reading (numeric), Service Provider (link to contacts), Description (text area), and Attachments (file upload widget).

## 4.2.0 User Interactions

- The list of service entries should be sortable by any column, with the default sort being 'Service Date' descending.
- The 'Service Type' field should be a dropdown populated from a configurable list.
- The 'Service Provider' field should be a Many2one widget allowing selection of an existing contact (vendor) or creation of a new one on the fly.

## 4.3.0 Display Requirements

- Costs should be displayed in the local currency format.
- Dates should be displayed in the user's preferred format as configured in Odoo.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The UI must be navigable using a keyboard, consistent with WCAG 2.1 Level AA standards (REQ-INT-001).

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-SVC-001

### 5.1.2 Rule Description

The Service Date for a maintenance entry cannot be a future date.

### 5.1.3 Enforcement Point

On validation before creating or saving a `tms.vehicle.service.log` record.

### 5.1.4 Violation Handling

Prevent save operation and display an inline validation error on the 'Service Date' field.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-SVC-002

### 5.2.2 Rule Description

The Odometer Reading for a new service entry should ideally be greater than the previous entry's reading for the same vehicle.

### 5.2.3 Enforcement Point

On validation before saving a new record.

### 5.2.4 Violation Handling

Display a non-blocking warning to the user if the entered odometer reading is less than the last recorded one, but allow them to proceed after confirmation. This handles cases like odometer replacement.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-006', 'dependency_reason': 'The Vehicle Master record and its underlying Odoo model (`tms.vehicle`) must exist before a service history can be associated with it.'}

## 6.2.0 Technical Dependencies

- Requires a new Odoo model, e.g., `tms.vehicle.service.log`.
- Requires a new Odoo model for configurable service types, e.g., `tms.service.type`.
- Relies on Odoo's base `res.partner` model for Service Providers.
- Relies on Odoo's attachment handling (`ir.attachment`) and integration with Amazon S3 for file storage.

## 6.3.0 Data Dependencies

- A pre-populated or configurable list of 'Service Types' (e.g., Oil Change, Tire Rotation, Brake Service) is needed for the dropdown menu.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The service history list on the vehicle form should load in under 1 second, even with 100+ entries.
- Saving a new service entry, including a small attachment, should complete within 2 seconds.

## 7.2.0 Security

- Access to create, read, update, and delete service history entries must be restricted to authorized roles (initially 'Admin') using Odoo's `ir.model.access.csv`.
- No sensitive data is expected, but standard data-at-rest encryption provided by AWS RDS and S3 must be active.

## 7.3.0 Usability

- The process of adding a new service entry should be intuitive and require minimal clicks from the vehicle form.
- Error messages must be clear and guide the user on how to correct the input.

## 7.4.0 Accessibility

- Must adhere to the system-wide WCAG 2.1 Level AA standard (REQ-INT-001).

## 7.5.0 Compatibility

- Functionality must be fully supported on all modern web browsers targeted by the project.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Standard Odoo development: creating two new models (`tms.vehicle.service.log`, `tms.service.type`).
- Defining model fields, including Many2one and One2many relationships.
- Creating standard Odoo views (form, tree).
- Implementing Python-level constraints for validation.
- Configuring access control lists (ACLs).

## 8.3.0 Technical Risks

- Minimal risk. Potential for minor issues if the relationship between the vehicle and service log is modeled incorrectly. The non-blocking odometer check (BR-SVC-002) adds a small amount of logic.

## 8.4.0 Integration Points

- The cost data from service logs will be aggregated for the 'Vehicle Profitability Report' (REQ-REP-001).

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Create/Read/Update/Delete (CRUD) operations for service entries.
- Validation of all fields as per acceptance criteria (future date, negative numbers, required fields).
- File upload validation (type and size).
- Verification that access is denied for unauthorized roles (e.g., Driver).
- Test the non-blocking warning for a lower-than-previous odometer reading.

## 9.3.0 Test Data Needs

- At least 2-3 vehicle records.
- A list of at least 5 service types.
- Several vendor records in `res.partner`.
- Test files of various sizes and types (valid and invalid).

## 9.4.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework.
- Manual testing via the Odoo web interface.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main development branch.
- Unit tests covering model constraints and validation logic are implemented and achieve >80% coverage for the new code.
- Integration testing confirms that service costs are correctly linked to the vehicle.
- UI/UX has been reviewed and approved by the product owner.
- Security rules have been tested to ensure only Admins can access the functionality.
- Relevant technical documentation for the new models is created.
- Story has been deployed and verified in the staging environment.

# 11.0.0 Planning Information

## 11.1.0 Story Points

2

## 11.2.0 Priority

🟡 Medium

## 11.3.0 Sprint Considerations

- This story is dependent on US-006 (Create Vehicle Record) and should be scheduled in a sprint after it is completed.
- It is a self-contained piece of work suitable for one developer.

## 11.4.0 Release Impact

- This feature is a foundational component for accurate vehicle cost tracking and is a prerequisite for the Vehicle Profitability Report.


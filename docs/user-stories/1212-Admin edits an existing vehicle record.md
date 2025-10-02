# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-007 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin edits an existing vehicle record |
| As A User Story | As an Admin, I want to edit the details of an exis... |
| User Persona | Admin: A user with full system access responsible ... |
| Business Value | Ensures data integrity for the vehicle fleet, whic... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successfully edit and save a vehicle record

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am an 'Admin' user logged into the system and am viewing the form for an existing vehicle

### 3.1.5 When

I modify one or more fields (e.g., change 'Capacity' from 20 to 25) and click 'Save'

### 3.1.6 Then

The system successfully saves the changes, I see a confirmation message, and the updated information is immediately visible on the vehicle's form and list view.

### 3.1.7 Validation Notes

Verify the database record for the vehicle reflects the new values. Check the Odoo UI to confirm the display is updated.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempt to save with a duplicate Truck Number

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am an 'Admin' user editing vehicle 'V-001', and another vehicle 'V-002' already exists with the Truck Number 'KA01AB1234'

### 3.2.5 When

I change the 'Truck Number' of 'V-001' to 'KA01AB1234' and click 'Save'

### 3.2.6 Then

The system must prevent the save operation and display a clear, user-friendly error message such as 'Truck Number must be unique. KA01AB1234 is already assigned to another vehicle.'

### 3.2.7 Validation Notes

Check that the database record for 'V-001' has not been updated. The UI should highlight the 'Truck Number' field as the source of the error.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to save with an invalid Truck Number format

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am an 'Admin' user editing an existing vehicle record

### 3.3.5 When

I change the 'Truck Number' to an invalid format (e.g., 'INVALID-123') and click 'Save'

### 3.3.6 Then

The system must prevent the save and display a validation error message like 'Invalid Truck Number format. Please use a valid Indian vehicle registration number format.'

### 3.3.7 Validation Notes

The save action should fail, and the form should remain in edit mode with the invalid data still present for correction.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Discard changes made to a vehicle record

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

I am an 'Admin' user and have made unsaved changes to a vehicle's form

### 3.4.5 When

I click the 'Discard' button

### 3.4.6 Then

The system prompts me for confirmation, and upon confirming, all my changes are reverted, and the form displays the last saved state of the record.

### 3.4.7 Validation Notes

Verify that no changes were written to the database. The UI should reflect the original data.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Audit trail is created upon successful edit

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I am an 'Admin' user editing an existing vehicle record

### 3.5.5 When

I successfully change the 'Next Service Due Date' and save the record

### 3.5.6 Then

The system must create an immutable audit log entry that records my user ID, the timestamp, the action ('update'), the vehicle record ID, and the specific change (e.g., 'Next Service Due Date' changed from '2024-11-10' to '2024-12-15').

### 3.5.7 Validation Notes

Query the audit trail model/table to confirm the new log entry exists and contains the correct details.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Non-Admin user attempts to edit a vehicle

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am logged in as a user with the 'Driver' or 'Finance Officer' role

### 3.6.5 When

I navigate to the vehicle list view and open a vehicle's form

### 3.6.6 Then

The 'Edit' button must not be visible, and all fields must be read-only.

### 3.6.7 Validation Notes

Verify through UI inspection and by attempting to send an edit request via developer tools, which should be rejected by the server.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Standard Odoo Form View for the vehicle model.
- An 'Edit' button to enter edit mode.
- A 'Save' button to commit changes.
- A 'Discard' button to cancel changes.
- Inline validation messages next to fields with errors.

## 4.2.0 User Interactions

- User clicks 'Edit' to make the form fields editable.
- User modifies data in input fields, dropdowns, and date pickers.
- User clicks 'Save' to persist changes or 'Discard' to cancel.
- System provides immediate feedback on save success or failure.

## 4.3.0 Display Requirements

- All fields defined in REQ-DAT-001 must be displayed and editable: Truck Number, Model, Capacity, Owner Details, Fuel Type, Last Service Date, Next Service Due Date.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- Validation errors must be programmatically associated with their respective fields.
- The form must be navigable using a keyboard.

# 5.0.0 Business Rules

- {'rule_id': 'BR-002', 'rule_description': "The 'Truck Number' for each vehicle must be unique across all vehicle records.", 'enforcement_point': "On the 'save' (write) operation of the vehicle record.", 'violation_handling': 'Prevent the database transaction and return a validation error to the user interface.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

The vehicle model, fields, and creation form must exist before the edit functionality can be implemented.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-071

#### 6.1.2.2 Dependency Reason

Implements the uniqueness validation logic (BR-002) that must be enforced during the edit operation.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-072

#### 6.1.3.2 Dependency Reason

Implements the truck number format validation that must be enforced during the edit operation.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-025

#### 6.1.4.2 Dependency Reason

The audit trail mechanism (REQ-DAT-008) must be in place to log the changes made by this story.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM and Views framework.
- The custom `tms.vehicle` model must be defined.

## 6.3.0.0 Data Dependencies

- Requires existing vehicle records in the database for testing purposes.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The vehicle form view must load in under 3 seconds.
- The save operation for an edit should complete within 200ms under normal load.

## 7.2.0.0 Security

- Only users with appropriate permissions (e.g., 'Admin' role) can edit vehicle records. This must be enforced on both the client-side (hiding buttons) and server-side (access control rules).
- All data modifications must be logged in the audit trail as per REQ-DAT-008.

## 7.3.0.0 Usability

- Error messages for validation failures must be clear, concise, and guide the user toward a solution.

## 7.4.0.0 Accessibility

- The form must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must be fully functional on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard CRUD operation in Odoo.
- Validation logic (uniqueness, format) needs to be correctly applied in the model's `write` method.
- Integration with the audit trail system is required.

## 8.3.0.0 Technical Risks

- Incorrectly overriding the `write` method could bypass standard Odoo logic or introduce performance issues.
- Failure to properly handle database constraints for uniqueness could lead to data integrity issues if not caught at the application layer.

## 8.4.0.0 Integration Points

- Odoo's base ORM for data persistence.
- The system's central audit logging service/module.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify successful editing of each field individually.
- Test the duplicate truck number validation.
- Test the truck number format validation with multiple invalid inputs.
- Verify the 'Discard' functionality.
- Confirm that a user without Admin rights cannot see the 'Edit' button or save changes.
- Check the audit log after a successful save to ensure the entry is correct.

## 9.3.0.0 Test Data Needs

- A set of at least two distinct vehicle records.
- A list of valid and invalid Indian vehicle registration numbers.
- User accounts with 'Admin' and non-'Admin' roles.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- A browser automation tool like Selenium or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for model validation logic implemented and passing with >80% coverage
- Integration testing completed successfully in a staging environment
- User interface reviewed and approved by the product owner
- Security requirements (role-based access) validated
- Audit trail generation is confirmed to be working as expected
- Documentation for the vehicle model's fields and validation is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story should be prioritized immediately after the 'Create Vehicle' story (US-006) to complete the core management functionality for this master data.
- Dependent on the implementation of the audit trail framework.

## 11.4.0.0 Release Impact

- This is a fundamental feature for the initial release (Phase 1). Without it, master data cannot be maintained, rendering the system unusable.


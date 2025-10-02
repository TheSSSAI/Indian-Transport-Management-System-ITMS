# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-072 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System validates format of Indian vehicle registra... |
| As A User Story | As an Admin, I want the system to validate the for... |
| User Persona | Admin, Dispatch Manager (any user with permission ... |
| Business Value | Ensures high data quality for a critical master da... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Master |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Valid standard format with no spaces

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

An Admin is on the 'Create Vehicle' or 'Edit Vehicle' form.

### 3.1.5 When

The user enters a valid truck number like 'MH12AB1234' into the 'Truck Number' field and attempts to save.

### 3.1.6 Then

The system accepts the value and the record saves successfully.

### 3.1.7 Validation Notes

Verify that the record is created/updated in the database with the provided truck number.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Valid format with spaces or hyphens

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An Admin is on the 'Create Vehicle' form.

### 3.2.5 When

The user enters a valid truck number with separators like 'KA 01 AB 1234' or 'TN-22-CQ-5555'.

### 3.2.6 Then

The system accepts the value and saves the record successfully.

### 3.2.7 Validation Notes

The system should ideally normalize the value by removing separators and converting to uppercase before saving (e.g., 'KA01AB1234').

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Valid format with mixed case letters

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

An Admin is on the 'Create Vehicle' form.

### 3.3.5 When

The user enters a valid truck number with mixed case letters like 'dl01cAb1234'.

### 3.3.6 Then

The system accepts the value and saves the record, normalizing the input to uppercase ('DL01CAB1234').

### 3.3.7 Validation Notes

Check the database to ensure the stored value is in a consistent, uppercase format.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Invalid format with incorrect length

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

An Admin is on the 'Create Vehicle' form.

### 3.4.5 When

The user enters an incomplete truck number like 'MH12AB123' and attempts to save.

### 3.4.6 Then

The system prevents the form from saving and displays a clear error message like 'Invalid format. Please use a format like XX12AB1234.'

### 3.4.7 Validation Notes

Verify the error message is visible and the save action is blocked.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Invalid format with special characters

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

An Admin is on the 'Create Vehicle' form.

### 3.5.5 When

The user enters a truck number with special characters like 'MH12AB1234!' and tabs out of the field.

### 3.5.6 Then

The system displays an inline validation error message immediately.

### 3.5.7 Validation Notes

The validation should trigger on blur for immediate user feedback.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Invalid format with incorrect structure

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

An Admin is on the 'Create Vehicle' form.

### 3.6.5 When

The user enters a truck number with an incorrect structure like 'M112AB1234' (incorrect state code) or 'MH1AB1234' (incorrect RTO code).

### 3.6.6 Then

The system prevents the form from saving and displays the format validation error message.

### 3.6.7 Validation Notes

Test multiple structural variations to ensure the validation logic is robust.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Clearing an invalid entry removes the error

### 3.7.3 Scenario Type

Alternative_Flow

### 3.7.4 Given

The 'Truck Number' field is showing a validation error.

### 3.7.5 When

The user corrects the entry to a valid format like 'UP14CD5678'.

### 3.7.6 Then

The validation error message is cleared.

### 3.7.7 Validation Notes

Verify that the UI state updates correctly upon valid input.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Input field for 'Truck Number' on the Vehicle form.
- Error message display area adjacent to the input field.

## 4.2.0 User Interactions

- Validation should trigger on field blur (losing focus) for immediate feedback.
- Validation must also trigger on form submission as a final safeguard.
- The form's 'Save' button should be disabled or the save action should be prevented if validation fails.

## 4.3.0 Display Requirements

- The error message must be user-friendly and provide an example of a valid format (e.g., 'Invalid format. Example: MH12AB1234').

## 4.4.0 Accessibility Needs

- The error message should be programmatically associated with the input field using `aria-describedby` for screen reader users.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-002

### 5.1.2 Rule Description

The 'Truck Number' for each vehicle must be unique across all vehicle records. This story validates format; uniqueness is handled by US-071.

### 5.1.3 Enforcement Point

Database constraint and model-level validation.

### 5.1.4 Violation Handling

Display an error message indicating the number is already in use.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-TMS-VEH-01

### 5.2.2 Rule Description

The vehicle registration number must conform to the standard format prescribed by the Indian Motor Vehicles Act.

### 5.2.3 Enforcement Point

Frontend (UI) and Backend (Odoo model) on create and update operations.

### 5.2.4 Violation Handling

Prevent record creation/update and display a format validation error to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-006', 'dependency_reason': "This story implements a validation rule on the vehicle creation form. The form and the 'Truck Number' field must exist first."}

## 6.2.0 Technical Dependencies

- Odoo 18 framework
- Odoo Web Library (OWL) for frontend components
- The `tms.vehicle` model must be defined in the Odoo backend.

## 6.3.0 Data Dependencies

*No items available*

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The validation logic (regex) must execute in under 50ms to ensure a responsive user interface without any noticeable lag during data entry.

## 7.2.0 Security

- Input must be sanitized on the backend to prevent any potential injection attacks, even though the format is restrictive.

## 7.3.0 Usability

- Validation feedback should be provided in real-time (on blur) to allow users to correct mistakes immediately.
- The system should be lenient with user input regarding case and separators (spaces/hyphens), normalizing it upon save.

## 7.4.0 Accessibility

- Compliant with WCAG 2.1 Level AA standards for form validation feedback.

## 7.5.0 Compatibility

- Validation must work consistently across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Requires implementation of a regular expression for validation.
- Requires both backend validation (e.g., Odoo's `@api.constrains`) for data integrity and frontend validation (in OWL) for user experience.

## 8.3.0 Technical Risks

- The regex might need to be adjusted to accommodate less common or older vehicle number formats if they are required by the business. The initial implementation should cover the most common modern formats.

## 8.4.0 Integration Points

- This validation will be part of the `tms.vehicle` model and its corresponding form view in Odoo.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Test with a comprehensive list of valid Indian vehicle numbers from different states and eras.
- Test with a list of common invalid formats (wrong length, special characters, incorrect structure).
- Test the UI flow: enter invalid data, see error, correct data, see error disappear, save successfully.
- Test case-insensitivity and handling of spaces/hyphens.

## 9.3.0 Test Data Needs

- Valid examples: 'MH12AB1234', 'KA 05 XY 9999', 'dl-01-c-4321'.
- Invalid examples: 'MH12ABC123', '12MHAB1234', 'MH-12-AB-1234!', '' (empty string).

## 9.4.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in tour/JS testing framework for frontend/E2E tests.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Backend validation using `@api.constrains` is implemented and covered by unit tests.
- Frontend validation in the OWL component is implemented and provides real-time feedback.
- Code has been peer-reviewed and adheres to project coding standards (Flake8, Black).
- Unit test coverage for the new logic meets the project's 80% threshold.
- End-to-end testing confirms the user flow on the vehicle form.
- The feature is deployed and verified in the staging environment without regressions.

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational data integrity feature for the Vehicle Master. It should be implemented in the same sprint as or immediately after the creation of the vehicle master form (US-006).

## 11.4.0 Release Impact

- This feature is critical for the initial release of the Vehicle Management module to ensure data quality from the start.


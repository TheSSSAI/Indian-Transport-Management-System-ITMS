# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-071 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System validates uniqueness of vehicle truck numbe... |
| As A User Story | As an Admin, I want the system to prevent me from ... |
| User Persona | Admin |
| Business Value | Ensures high data integrity for the vehicle master... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Create a new vehicle with a unique truck number

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

An Admin is on the 'Create New Vehicle' form

### 3.1.5 When

The Admin enters a truck number that does not exist in the system and clicks 'Save'

### 3.1.6 Then

The new vehicle record is created and saved successfully.

### 3.1.7 Validation Notes

Verify that the new vehicle record appears in the vehicle list view.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Error Condition: Attempt to create a new vehicle with a duplicate truck number

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A vehicle with the truck number 'MH12AB3456' already exists in the system

### 3.2.5 When

An Admin attempts to create a new vehicle with the truck number 'MH12AB3456' and clicks 'Save'

### 3.2.6 Then

The system prevents the record from being saved.

### 3.2.7 And

A user-friendly error message, such as "Error: Truck number 'MH12AB3456' is already in use.", is displayed next to the truck number field.

### 3.2.8 Validation Notes

Confirm the save operation fails and the specified error message is visible to the user.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Error Condition: Attempt to edit an existing vehicle to have a duplicate truck number

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

Vehicle A has truck number 'KA01BC7890' and Vehicle B has truck number 'TN05XY1234'

### 3.3.5 When

An Admin edits Vehicle A and changes its truck number to 'TN05XY1234' and clicks 'Save'

### 3.3.6 Then

The system prevents the changes from being saved.

### 3.3.7 And

A user-friendly error message indicating the duplication is displayed.

### 3.3.8 Validation Notes

Verify that Vehicle A's truck number remains 'KA01BC7890' after the failed save attempt.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Happy Path: Edit an existing vehicle without changing its truck number

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

An Admin is editing an existing vehicle with truck number 'DL03DE5678'

### 3.4.5 When

The Admin modifies other fields (e.g., Model, Capacity) but leaves the truck number unchanged and clicks 'Save'

### 3.4.6 Then

The vehicle record is updated and saved successfully.

### 3.4.7 Validation Notes

Check the vehicle's form view to confirm the other fields were updated while the truck number remained the same.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Edge Case: Uniqueness check is case-insensitive

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A vehicle with the truck number 'MH12AB3456' already exists

### 3.5.5 When

An Admin attempts to create a new vehicle with the truck number 'mh12ab3456'

### 3.5.6 Then

The system correctly identifies it as a duplicate and prevents the save.

### 3.5.7 Validation Notes

Test with various casings (all lower, all upper, mixed) to ensure the check is case-insensitive.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Edge Case: Uniqueness check ignores whitespace and common separators

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

A vehicle with the truck number 'MH12AB3456' already exists

### 3.6.5 When

An Admin attempts to create a new vehicle with the truck number 'MH 12 AB 3456' or 'MH-12-AB-3456'

### 3.6.6 Then

The system correctly identifies it as a duplicate and prevents the save.

### 3.6.7 Validation Notes

Test with spaces, hyphens, and other potential separators to ensure the underlying value is normalized before comparison.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Edge Case: Uniqueness check includes 'Inactive' vehicles

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

A vehicle with truck number 'GJ05FG9012' exists but is marked as 'Inactive'

### 3.7.5 When

An Admin attempts to create a new vehicle with the truck number 'GJ05FG9012'

### 3.7.6 Then

The system prevents the save and displays the uniqueness violation error.

### 3.7.7 Validation Notes

Ensure the uniqueness constraint is checked against all records, regardless of their active status.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Error message display area next to the 'Truck Number' input field.

## 4.2.0 User Interactions

- On attempting to save a form with a duplicate truck number, the save action is blocked.
- The input field for the truck number should be visually highlighted (e.g., with a red border) upon validation failure.

## 4.3.0 Display Requirements

- The error message must clearly state that the truck number is a duplicate and preferably show the conflicting number.

## 4.4.0 Accessibility Needs

- Error messages must be associated with the input field programmatically for screen readers (e.g., using `aria-describedby`).

# 5.0.0 Business Rules

- {'rule_id': 'BR-002', 'rule_description': "The 'Truck Number' for each vehicle must be unique across all vehicle records, including active and inactive ones.", 'enforcement_point': "Server-side, upon the 'create' or 'write' (update) operation on a vehicle record.", 'violation_handling': 'The transaction is rolled back, and a `ValidationError` is raised to be displayed on the user interface.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

This story implements validation within the vehicle creation form defined in US-006.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-007

#### 6.1.2.2 Dependency Reason

This story implements validation within the vehicle editing form defined in US-007.

## 6.2.0.0 Technical Dependencies

- Odoo ORM for model definition and validation.
- PostgreSQL database to enforce the uniqueness constraint at the database level.

## 6.3.0.0 Data Dependencies

- Requires read access to the entire set of existing vehicle records to perform the uniqueness check.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The uniqueness check query must be optimized (e.g., using a database index) and complete in under 50ms to avoid noticeable delays during form submission.

## 7.2.0.0 Security

- Validation logic must be enforced on the server-side (Odoo backend) to prevent circumvention by client-side manipulation.

## 7.3.0.0 Usability

- Error feedback must be immediate, clear, and specific to guide the user in correcting the input.

## 7.4.0.0 Accessibility

- Meets WCAG 2.1 Level AA standards for form validation and error feedback.

## 7.5.0.0 Compatibility

- Validation behavior must be consistent across all supported browsers.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Implementing a robust normalization function to handle case, whitespace, and separators before the check.
- Using a database-level unique constraint on a separate, normalized field is the most reliable approach.
- Overriding Odoo's `create` and `write` methods to populate the normalized field before saving.
- Ensuring Odoo's `ValidationError` is caught and displayed correctly in the UI.

## 8.3.0.0 Technical Risks

- A purely application-level check without a database constraint could allow race conditions, where two simultaneous requests create a duplicate. This must be mitigated with a DB constraint.
- The normalization logic must be carefully designed to avoid stripping characters that are a valid part of a registration number.

## 8.4.0.0 Integration Points

- This logic integrates directly with the Odoo Vehicle model (`fleet.vehicle` or a custom equivalent).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration

## 9.2.0.0 Test Scenarios

- Test creation of a new vehicle with a unique number.
- Test creation with an exact duplicate number.
- Test creation with a case-variant duplicate number.
- Test creation with a whitespace/separator-variant duplicate number.
- Test editing a vehicle to have a duplicate number.
- Test editing a vehicle without changing its number.
- Test creation with a number that matches an inactive vehicle.

## 9.3.0.0 Test Data Needs

- A set of pre-existing vehicle records with a variety of truck number formats.
- At least one 'Inactive' vehicle record.

## 9.4.0.0 Testing Tools

- Pytest for Odoo unit tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests for normalization and validation logic implemented and passing with >80% coverage
- A database-level unique constraint is implemented on a normalized version of the truck number field
- Integration testing completed successfully on a staging environment
- User interface displays clear, non-technical error messages upon validation failure
- Performance of the save action is verified to be within acceptable limits
- Documentation for the Vehicle model is updated to reflect the uniqueness constraint

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational data integrity feature and should be implemented as part of the initial development of the Vehicle Master module.
- It is a blocker for any functionality that relies on uniquely identifying vehicles.

## 11.4.0.0 Release Impact

- Critical for the initial release (Phase 1) to ensure the core dataset is clean and reliable from the start.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-075 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System prevents trip assignment if material weight... |
| As A User Story | As a Dispatch Manager, I want the system to preven... |
| User Persona | Dispatch Manager |
| Business Value | Enforces legal and safety compliance by preventing... |
| Functional Area | Trip Management |
| Story Theme | Core Business Rule Enforcement |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Assigning a suitable vehicle to a trip with a pre-filled weight

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A trip record is being created with a 'Material Weight' of 15 Tons

### 3.1.5 When

The Dispatch Manager assigns a vehicle with a 'Capacity' of 20 Tons and saves the record

### 3.1.6 Then

The system successfully saves the trip record without any validation errors.

### 3.1.7 Validation Notes

Verify the trip record is created/updated successfully in the database.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Happy Path: Entering a valid weight for a trip with a pre-assigned vehicle

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A trip record is being created with an assigned vehicle that has a 'Capacity' of 10 Tons

### 3.2.5 When

The Dispatch Manager enters a 'Material Weight' of 9.5 Tons and saves the record

### 3.2.6 Then

The system successfully saves the trip record without any validation errors.

### 3.2.7 Validation Notes

Verify the trip record is created/updated successfully in the database.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Happy Path: Weight is exactly equal to vehicle capacity

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A trip record has an assigned vehicle with a 'Capacity' of 12 Tons

### 3.3.5 When

The Dispatch Manager enters a 'Material Weight' of 12 Tons and saves the record

### 3.3.6 Then

The system successfully saves the trip record.

### 3.3.7 Validation Notes

Verify the record saves. The boundary condition (equal to) must be allowed.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Error Condition: Entering a weight that exceeds the capacity of an assigned vehicle

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A trip record has an assigned vehicle with a 'Capacity' of 10 Tons

### 3.4.5 When

The Dispatch Manager enters a 'Material Weight' of 11 Tons and attempts to save

### 3.4.6 Then

The system must prevent the record from being saved AND display a clear error message to the user, such as 'Error: Material weight (11 Tons) exceeds the selected vehicle's capacity (10 Tons).'

### 3.4.7 Validation Notes

Confirm the record is not saved and the specified error message appears in the UI.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Error Condition: Assigning an undersized vehicle to a trip with an existing weight

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A trip record has a 'Material Weight' of 25 Tons

### 3.5.5 When

The Dispatch Manager attempts to assign a vehicle with a 'Capacity' of 20 Tons and save

### 3.5.6 Then

The system must prevent the record from being saved AND display a clear error message, such as 'Error: The selected vehicle's capacity (20 Tons) is less than the required material weight (25 Tons).'

### 3.5.7 Validation Notes

Confirm the record is not saved and the specified error message appears in the UI.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Edge Case: Changing the vehicle on an existing trip to one with insufficient capacity

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

An existing trip record has a 'Material Weight' of 18 Tons and a suitable assigned vehicle (e.g., 20-Ton capacity)

### 3.6.5 When

The Dispatch Manager edits the trip and changes the assigned vehicle to one with a 'Capacity' of 15 Tons

### 3.6.6 Then

The system must prevent the change and display the capacity validation error message.

### 3.6.7 Validation Notes

Verify the update fails and the original vehicle assignment remains.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Edge Case: Vehicle record has a null or zero capacity

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

A vehicle record exists with its 'Capacity' field set to 0 or null

### 3.7.5 When

The Dispatch Manager attempts to assign this vehicle to a trip with a 'Material Weight' greater than 0

### 3.7.6 Then

The system must prevent the assignment and display an informative error, such as 'Error: Cannot assign vehicle [Truck Number] as its capacity is not defined. Please update the vehicle record.'

### 3.7.7 Validation Notes

Test with both 0 and null values for vehicle capacity.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A validation error message/pop-up.

## 4.2.0 User Interactions

- The validation should be triggered on the server-side upon attempting to save the trip record.
- For an enhanced user experience, the validation should also trigger via an on-change event in the UI when either the 'Vehicle' or 'Material Weight' field is modified, providing immediate feedback.

## 4.3.0 Display Requirements

- The error message must clearly state the conflicting values: the entered material weight and the vehicle's capacity.

## 4.4.0 Accessibility Needs

- Error messages must be associated with the form fields and be accessible to screen readers, following WCAG guidelines.

# 5.0.0 Business Rules

- {'rule_id': 'BR-007', 'rule_description': "The specified material weight for a trip shall not exceed the assigned vehicle's registered capacity.", 'enforcement_point': 'On creation and update of a Trip record.', 'violation_handling': 'The system transaction (create/update) is blocked, and a user-facing error message is displayed.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

The Vehicle Master model, including the 'Capacity' field, must exist to be referenced.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

The Trip Management model and its form view, including 'Material Weight' and 'Vehicle' fields, must exist for the validation to be implemented.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM for model constraints.
- Odoo Web Library (OWL) for client-side on-change validation (optional but recommended for UX).

## 6.3.0.0 Data Dependencies

- Vehicle records must have the 'Capacity' field populated with a valid, non-negative numeric value representing tons.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The server-side validation must complete in under 100ms to ensure a responsive user experience when saving the form.

## 7.2.0.0 Security

- The validation logic MUST be enforced on the server-side (e.g., using Odoo's `@api.constrains`) to prevent circumvention by client-side manipulations.

## 7.3.0.0 Usability

- The error message must be clear, concise, and actionable, guiding the user on how to correct the issue.

## 7.4.0.0 Accessibility

- Compliant with WCAG 2.1 Level AA for error identification and suggestion.

## 7.5.0.0 Compatibility

- The validation must function correctly across all supported browsers for the Odoo 18 web client.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard validation that can be implemented with a single Odoo model constraint.
- The logic is a simple numerical comparison.

## 8.3.0.0 Technical Risks

- Potential for inconsistent units if not standardized (e.g., tons vs. kg). The SRS specifies 'Tons' for vehicle capacity, so the trip weight field must use the same unit.

## 8.4.0.0 Integration Points

- This logic is self-contained within the TMS Odoo module, specifically between the Trip and Vehicle models.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify successful save when weight < capacity.
- Verify successful save when weight = capacity.
- Verify save failure and correct error message when weight > capacity.
- Verify save failure when assigning an undersized vehicle to a trip with existing weight.
- Verify save failure when a vehicle with zero/null capacity is assigned.
- Verify UI feedback on field change (if on-change handler is implemented).

## 9.3.0.0 Test Data Needs

- Vehicle records with various capacities (e.g., 10, 15, 20 tons).
- A vehicle record with 0 capacity.
- A vehicle record with null capacity.

## 9.4.0.0 Testing Tools

- Pytest for Odoo unit tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented with >80% coverage for the new logic and passing
- Integration testing completed successfully on a staging environment
- User interface validation and error messaging reviewed and approved by a UX stakeholder
- Performance requirements verified
- Security requirements (server-side enforcement) validated
- Documentation for the business rule is updated if necessary
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a core business rule and should be implemented in the same sprint as the basic Trip creation functionality to ensure data integrity from the start.

## 11.4.0.0 Release Impact

- Essential for the initial release of the Trip Management feature.


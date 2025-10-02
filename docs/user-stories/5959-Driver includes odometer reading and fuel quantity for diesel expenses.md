# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-054 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver includes odometer reading and fuel quantity... |
| As A User Story | As a Driver, I want to enter the vehicle's current... |
| User Persona | Driver, who accesses the system via a mobile-frien... |
| Business Value | Enables accurate fuel efficiency (km/liter) tracki... |
| Functional Area | Expense Management |
| Story Theme | Trip Execution & Tracking |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Submitting a valid diesel expense

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Driver is logged in and on the 'Submit Expense' form for an active trip, and the vehicle's last recorded odometer reading was 50,000 km

### 3.1.5 When

The Driver selects 'Diesel' as the expense type, enters an amount, an odometer reading of 50,500, a fuel quantity of 100, and uploads a valid receipt

### 3.1.6 Then

The expense is successfully submitted for approval, and the new expense record in the database contains the odometer reading of 50,500 and fuel quantity of 100.

### 3.1.7 Validation Notes

Verify the record is created in the backend with the correct values. The expense should appear in the Dispatch Manager's approval queue.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

UI: Conditional field visibility

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A Driver is on the 'Submit Expense' form

### 3.2.5 When

The Driver selects an expense type other than 'Diesel' (e.g., 'Toll', 'Food')

### 3.2.6 Then

The 'Odometer Reading' and 'Fuel Quantity' fields are not visible.

### 3.2.7 Validation Notes

Cycle through all non-diesel expense types to ensure the fields remain hidden. Then, switch to 'Diesel' to confirm they appear.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Error Condition: Odometer reading is lower than the previous reading

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A Driver is submitting a 'Diesel' expense for a vehicle whose last recorded odometer reading was 50,000 km

### 3.3.5 When

The Driver enters an odometer reading of 49,999 and attempts to submit the form

### 3.3.6 Then

The system prevents submission and displays a clear, user-friendly error message, such as 'Odometer reading must be greater than the last recorded value of 50,000 km.'

### 3.3.7 Validation Notes

Test with values less than and equal to the last reading. The validation should be triggered by the backend.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Error Condition: Mandatory fields for diesel expense are empty

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A Driver has selected 'Diesel' as the expense type

### 3.4.5 When

The Driver leaves either the 'Odometer Reading' or 'Fuel Quantity' field blank and attempts to submit

### 3.4.6 Then

The system prevents submission and highlights the required fields with a validation error.

### 3.4.7 Validation Notes

Test with each field empty individually and both empty.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Edge Case: First diesel expense for a new vehicle

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A Driver is submitting the very first 'Diesel' expense for a vehicle with no prior odometer history in the system

### 3.5.5 When

The Driver enters a valid odometer reading (e.g., 150 km) and fuel quantity

### 3.5.6 Then

The system accepts the submission without performing the 'greater than previous' validation and successfully creates the expense record.

### 3.5.7 Validation Notes

This requires test data for a vehicle with no associated expense records. The validation logic must gracefully handle a null or zero result for the previous reading.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Alternative Flow: Changing expense type from Diesel to something else

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

A Driver has selected 'Diesel' as the expense type and entered values for odometer and quantity

### 3.6.5 When

The Driver changes the expense type to 'Toll'

### 3.6.6 Then

The 'Odometer Reading' and 'Fuel Quantity' fields become hidden, and their previously entered values are cleared to prevent accidental submission of incorrect data.

### 3.6.7 Validation Notes

Verify that if the user switches back to 'Diesel', the fields are empty again.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A numeric input field for 'Odometer Reading (km)'
- A numeric input field for 'Fuel Quantity (liters)'
- User-friendly validation messages for errors

## 4.2.0 User Interactions

- The odometer and quantity fields must become visible and required only when 'Expense Type' is 'Diesel'.
- On mobile devices, tapping these fields should bring up a numeric keypad.

## 4.3.0 Display Requirements

- Clear labels must be associated with each new input field.
- The last recorded odometer reading should be displayed in the error message when validation fails.

## 4.4.0 Accessibility Needs

- All form labels must be correctly associated with their input fields using the 'for' attribute.
- Error messages must be programmatically linked to the corresponding input fields for screen reader users.

# 5.0.0 Business Rules

- {'rule_id': 'BR-009', 'rule_description': "The odometer reading submitted with a 'Diesel' expense entry must be greater than the previously recorded odometer reading for that vehicle.", 'enforcement_point': "On submission of an expense record of type 'Diesel'.", 'violation_handling': 'Prevent record creation and return a validation error to the user interface.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-053

#### 6.1.1.2 Dependency Reason

This story adds fields to the expense submission form, which must be created first by US-053.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

The system needs to know which vehicle is assigned to the trip to fetch its last odometer reading. This assignment is handled by US-027.

## 6.2.0.0 Technical Dependencies

- The Odoo expense model (`tms.expense`) must exist and be modifiable.
- The Odoo vehicle model (`tms.vehicle`) must be accessible to link expenses and retrieve history.

## 6.3.0.0 Data Dependencies

- Requires access to historical expense data for the specific vehicle to validate the new odometer reading.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The backend validation check to retrieve the last odometer reading must complete in under 100ms to avoid noticeable delay in form submission.

## 7.2.0.0 Security

- All user-supplied input (odometer, quantity) must be sanitized on the backend to prevent injection attacks.

## 7.3.0.0 Usability

- The UI must be intuitive on a mobile screen. Error messages must be clear and guide the user to a resolution.

## 7.4.0.0 Accessibility

- The form must be navigable and operable using a keyboard and screen reader, compliant with WCAG 2.1 Level AA.

## 7.5.0.0 Compatibility

- The feature must function correctly on the latest versions of Chrome and Safari on both desktop and mobile (iOS/Android).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Requires frontend changes with conditional logic (OWL).
- Requires backend model extension (new fields).
- Requires a new backend validation constraint (`@api.constrains`) with a database query.
- Logic must handle the edge case of a vehicle's first fuel entry.

## 8.3.0.0 Technical Risks

- The query to find the last odometer reading could be inefficient if not indexed properly, potentially slowing down submissions as data grows. The query should be optimized (e.g., `order by date desc, limit=1`).

## 8.4.0.0 Integration Points

- The data captured will be a key input for the 'Fuel Efficiency Report' (REQ-REP-001).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Successful submission of a diesel expense.
- Attempted submission with an odometer reading lower than the last one.
- Attempted submission with an odometer reading equal to the last one.
- Submission for a vehicle with no prior diesel expenses.
- UI check: Toggling between 'Diesel' and other expense types to verify field visibility.
- Validation check for non-numeric and empty inputs.

## 9.3.0.0 Test Data Needs

- A test vehicle with at least one existing diesel expense record.
- A test vehicle with no expense history.
- A test user with the 'Driver' role assigned to an active trip.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- Browser developer tools for mobile viewport testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the backend validation logic are implemented with >80% coverage and are passing
- Integration testing of the form submission process is completed successfully
- User interface has been reviewed and approved on both mobile and desktop viewports
- Performance of the odometer validation query is verified to be within acceptable limits
- Security requirements (input sanitization) are validated
- No new accessibility regressions are introduced
- Story is deployed and verified in the staging environment by QA

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a direct dependency for generating the Fuel Efficiency Report. It should be prioritized accordingly.
- Must be scheduled in a sprint after its prerequisite story US-053 is completed.

## 11.4.0.0 Release Impact

This is a core feature for operational cost management. Its completion is necessary for the financial and operational reporting modules to be effective.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-084 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System validates odometer reading for diesel expen... |
| As A User Story | As a Dispatch Manager, I want the system to enforc... |
| User Persona | The primary actor is the 'Driver' submitting the e... |
| Business Value | Prevents data entry errors, ensuring the integrity... |
| Functional Area | Expense Management |
| Story Theme | Trip Lifecycle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Submitting a valid (higher) odometer reading

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Driver is submitting a 'Diesel' type expense for a trip associated with Vehicle 'KA-01-AB-1234'

### 3.1.5 When

The last recorded odometer reading for this vehicle is 50,000 km, and the Driver enters a new reading of 50,250 km and submits the form

### 3.1.6 Then

The system validates the reading successfully, the expense is created and enters the approval queue, and the new reading is now considered the latest for the vehicle.

### 3.1.7 Validation Notes

Verify that the expense record is created in the database with the correct odometer value and is visible in the manager's approval queue.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Error Condition: Submitting an invalid (lower) odometer reading

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A Driver is submitting a 'Diesel' type expense for Vehicle 'KA-01-AB-1234'

### 3.2.5 When

The last recorded odometer reading for this vehicle is 50,000 km, and the Driver enters a new reading of 49,950 km and attempts to submit

### 3.2.6 Then

The system prevents the submission and displays a clear, inline error message: 'Odometer reading must be greater than the last recorded value of 50,000 km.'

### 3.2.7 Validation Notes

Confirm that no new expense record is created and the user interface shows the specified error message.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Error Condition: Submitting an invalid (equal) odometer reading

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A Driver is submitting a 'Diesel' type expense for Vehicle 'KA-01-AB-1234'

### 3.3.5 When

The last recorded odometer reading for this vehicle is 50,000 km, and the Driver enters a new reading of 50,000 km and attempts to submit

### 3.3.6 Then

The system prevents the submission and displays the error message: 'Odometer reading must be greater than the last recorded value of 50,000 km.'

### 3.3.7 Validation Notes

Confirm that no new expense record is created and the UI shows the specified error message.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Edge Case: First-ever diesel expense for a vehicle

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

A Driver is submitting the first-ever 'Diesel' type expense for a new Vehicle 'KA-01-CD-5678'

### 3.4.5 When

There is no previously recorded odometer reading for this vehicle, and the Driver enters a reading of 150 km

### 3.4.6 Then

The system accepts the submission without performing the 'greater than' validation, and the expense is created successfully.

### 3.4.7 Validation Notes

Verify that any positive number is accepted as the first odometer reading for a vehicle.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Alternative Flow: Submitting a non-diesel expense

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

A Driver is submitting an expense for a trip

### 3.5.5 When

The Driver selects the expense type 'Toll' or 'Food'

### 3.5.6 Then

The odometer reading field is not required and the validation logic is not triggered.

### 3.5.7 Validation Notes

Check the expense submission form's behavior. The odometer field should ideally be hidden or, if visible, not mandatory for non-diesel types.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Error Condition: Submitting a diesel expense with no odometer reading

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

A Driver is submitting a 'Diesel' type expense

### 3.6.5 When

The Driver leaves the odometer reading field blank and attempts to submit

### 3.6.6 Then

The system prevents the submission and displays a standard 'This field is required' validation error.

### 3.6.7 Validation Notes

Verify that the odometer field is marked as mandatory on the form for diesel expenses.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Odometer reading input field (numeric)
- Inline error message display area associated with the odometer field

## 4.2.0 User Interactions

- When a user selects 'Diesel' as the expense type, the 'Odometer Reading' field must become visible and mandatory.
- On submission failure due to this validation, the form should not clear, and focus should be returned to the invalid odometer field.

## 4.3.0 Display Requirements

- The error message must dynamically include the last recorded odometer value to provide context to the user.

## 4.4.0 Accessibility Needs

- The error message must be programmatically linked to the input field using `aria-describedby` to be accessible to screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-009', 'rule_description': "The odometer reading submitted with a 'Diesel' expense entry must be greater than the previously recorded odometer reading for that vehicle.", 'enforcement_point': 'On submission of the driver expense form.', 'violation_handling': 'Block the form submission and display a descriptive error message to the user.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-053

#### 6.1.1.2 Dependency Reason

This story implements a validation rule within the expense submission feature. The core expense submission functionality must exist first.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-006

#### 6.1.2.2 Dependency Reason

Requires the existence of a Vehicle model to associate the odometer reading with.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-027

#### 6.1.3.2 Dependency Reason

The system needs the trip-to-vehicle assignment to identify which vehicle's odometer history to check.

## 6.2.0.0 Technical Dependencies

- Odoo's form validation framework (OWL).
- The database schema for expense records and vehicle records.

## 6.3.0.0 Data Dependencies

- Requires access to historical expense data to find the last recorded odometer reading for a specific vehicle.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The database query to retrieve the last odometer reading must be highly optimized (e.g., using an index) and complete in under 200ms to provide real-time feedback to the user.

## 7.2.0.0 Security

- Validation must be performed on the server-side to prevent client-side bypass. Client-side validation can be used for a better user experience but cannot be the only check.

## 7.3.0.0 Usability

- The error message must be clear, concise, and helpful, guiding the user to correct the mistake without confusion.

## 7.4.0.0 Accessibility

- WCAG 2.1 Level AA standards must be met for form fields and error messages.

## 7.5.0.0 Compatibility

- The validation must work consistently across all supported browsers for the mobile-friendly web interface.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Requires a backend database query to fetch the last odometer reading before validating the new entry.
- Frontend logic is needed to handle the error display.
- The logic must correctly handle the edge case of a vehicle's first-ever odometer entry.

## 8.3.0.0 Technical Risks

- A poorly optimized query for the last odometer reading could cause performance issues as the expense data grows. An index on `(vehicle_id, create_date)` or similar on the expense model is crucial.

## 8.4.0.0 Integration Points

- Integrates directly with the Expense Submission form controller and the Vehicle data model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Test with a valid reading.
- Test with a lower reading.
- Test with an equal reading.
- Test the first submission for a new vehicle.
- Test submission of a non-diesel expense type.
- Test submission with a blank odometer field for a diesel expense.

## 9.3.0.0 Test Data Needs

- A test vehicle with no prior diesel expenses.
- A test vehicle with at least one prior diesel expense and a known last odometer reading.

## 9.4.0.0 Testing Tools

- Pytest for backend unit and integration tests.
- Odoo's built-in testing framework.
- Selenium or Cypress for E2E UI testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Backend validation logic is covered by unit tests with at least 80% coverage.
- The full submission flow is covered by an integration test.
- Code has been peer-reviewed and merged into the main development branch.
- UI changes are responsive and meet accessibility standards.
- The database query for the last odometer reading is confirmed to be indexed and performant.
- No regressions are introduced in the expense submission process.
- Story is verified by QA and approved by the Product Owner.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is an enhancement to the core expense submission feature (US-053) and should be prioritized shortly after it to ensure data quality from the start.

## 11.4.0.0 Release Impact

Improves data integrity, which is foundational for several key reports (Fuel Efficiency, Vehicle Profitability). Essential for a reliable V1 release.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-074 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System prevents assignment of a driver with an exp... |
| As A User Story | As a Dispatch Manager, I want the system to preven... |
| User Persona | Dispatch Manager, Admin |
| Business Value | Ensures compliance with the Indian Motor Vehicles ... |
| Functional Area | Trip Management |
| Story Theme | Compliance and Risk Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Assigning a driver with a valid, future license expiry date

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Dispatch Manager is on the Trip form, creating or editing a trip

### 3.1.5 When

The manager selects a driver whose 'License Expiry Date' is in the future and saves the trip record

### 3.1.6 Then

The system successfully assigns the driver to the trip and saves the record without any validation errors.

### 3.1.7 Validation Notes

Verify that the trip record is saved in the database with the correct driver assigned.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempting to assign a driver with a past license expiry date

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A Dispatch Manager is on the Trip form, creating or editing a trip

### 3.2.5 When

The manager selects a driver whose 'License Expiry Date' is in the past and attempts to save the trip record

### 3.2.6 Then

The system prevents the record from being saved AND displays a clear, user-friendly error message stating 'Cannot assign [Driver Name]. Their license expired on [Expiry Date].'

### 3.2.7 Validation Notes

Confirm the database record is not saved/updated. Verify the exact error message is displayed to the user.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Assigning a driver whose license expires on the current date

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

A Dispatch Manager is on the Trip form, creating or editing a trip

### 3.3.5 When

The manager selects a driver whose 'License Expiry Date' is the same as the current system date and saves the trip record

### 3.3.6 Then

The system successfully assigns the driver to the trip, as the license is valid through the end of its expiry day.

### 3.3.7 Validation Notes

The validation logic must use a 'less than' (<) comparison against the current date, not 'less than or equal to' (<=).

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempting to assign a driver with no license expiry date recorded

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A Dispatch Manager is on the Trip form, creating or editing a trip

### 3.4.5 When

The manager selects a driver for whom the 'License Expiry Date' field is empty/null and attempts to save the trip record

### 3.4.6 Then

The system prevents the record from being saved AND displays a clear error message stating 'Cannot assign [Driver Name]. Their license expiry date is not recorded in the system.'

### 3.4.7 Validation Notes

This ensures data integrity and prevents assignment of drivers whose license validity cannot be confirmed.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Validation is enforced on the server-side

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A user attempts to bypass the frontend validation

### 3.5.5 When

An API call is made to assign a driver with an expired license to a trip

### 3.5.6 Then

The server rejects the request with a validation error, ensuring the rule cannot be circumvented.

### 3.5.7 Validation Notes

This must be tested via an integration test or direct API call, not just through the UI.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Error notification/dialog box

## 4.2.0 User Interactions

- When the user clicks 'Save' on the Trip form with an invalid driver, the save action is blocked and an error message is displayed.

## 4.3.0 Display Requirements

- The error message must be specific, mentioning the driver's name and the reason for the failure (e.g., expired license date or missing date).

## 4.4.0 Accessibility Needs

- Error messages must be associated with the relevant form field and be readable by screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-003', 'rule_description': 'A driver with an expired license cannot be assigned to a new trip.', 'enforcement_point': 'On save/commit of the Trip record after a driver has been selected or changed.', 'violation_handling': 'The transaction is aborted, and a user-facing error message is displayed.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-011

#### 6.1.1.2 Dependency Reason

The Driver model must exist to store driver information.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-012

#### 6.1.2.2 Dependency Reason

The 'License Expiry Date' field must exist on the Driver model for the validation to work.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-027

#### 6.1.3.2 Dependency Reason

The functionality to assign a driver to a trip on the Trip form must be implemented first.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM with server-side validation capabilities (e.g., @api.constrains).

## 6.3.0.0 Data Dependencies

- Requires test data for drivers with valid, expired, today's date, and null license expiry dates.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The validation check must add negligible latency (<50ms) to the record save operation.

## 7.2.0.0 Security

- The validation logic must be implemented on the server-side to prevent client-side bypass.

## 7.3.0.0 Usability

- Error messages must be clear, concise, and actionable for the user.

## 7.4.0.0 Accessibility

- Compliant with WCAG 2.1 Level AA for error feedback.

## 7.5.0.0 Compatibility

- The validation must work consistently across all supported browsers for the Odoo web client.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard server-side validation.
- The logic is a simple date comparison.
- Odoo provides a standard mechanism (@api.constrains) for this type of rule.

## 8.3.0.0 Technical Risks

- Risk of a poorly worded or non-translatable error message, leading to user confusion.

## 8.4.0.0 Integration Points

- Odoo ORM: The validation will be triggered by the Odoo framework during the write/create workflow for the Trip model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify successful assignment with a valid license.
- Verify blocked assignment with an expired license.
- Verify successful assignment with a license expiring today.
- Verify blocked assignment with a missing license expiry date.
- Verify the exact error message content for each failure scenario.

## 9.3.0.0 Test Data Needs

- Driver record with license_expiry_date > today
- Driver record with license_expiry_date < today
- Driver record with license_expiry_date = today
- Driver record with license_expiry_date = null

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- Manual testing via the Odoo UI.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented with >90% coverage for the validation logic, covering all scenarios (valid, expired, today, null)
- Integration testing completed successfully to confirm the constraint fires correctly on the model
- User interface error messaging is reviewed and approved for clarity
- Performance requirements verified
- Security requirements validated (server-side enforcement)
- Documentation updated appropriately
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational business rule and should be implemented early in the development cycle.
- Dependent on the core Trip and Driver models being available.

## 11.4.0.0 Release Impact

- This is a critical feature for the Minimum Viable Product (MVP) due to its compliance implications.


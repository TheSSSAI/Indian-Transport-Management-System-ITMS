# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-006 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates a new vehicle record |
| As A User Story | As an Admin, I want to create a new vehicle record... |
| User Persona | Admin: A system administrator responsible for mana... |
| Business Value | Establishes the foundational master data for the v... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful creation of a new vehicle record with all mandatory fields

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am on the 'Vehicles' list view

### 3.1.5 When

I click the 'Create' button, fill in all mandatory fields (Truck Number, Model, Capacity, Owner Details, Fuel Type) with valid and unique data, and click 'Save'

### 3.1.6 Then

A new vehicle record is successfully created in the system, I am redirected to the new vehicle's form view, and a confirmation message is displayed. The vehicle's status defaults to 'Active'.

### 3.1.7 Validation Notes

Verify the record exists in the database and is visible in the vehicle list view. Check that the default status is 'Active'.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempt to create a vehicle with a duplicate Truck Number

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A vehicle with the Truck Number 'KA01AB1234' already exists in the system

### 3.2.5 When

I attempt to create a new vehicle and enter 'KA01AB1234' in the Truck Number field and click 'Save'

### 3.2.6 Then

The system prevents the record from being saved and displays a clear, user-friendly error message stating that the 'Truck Number must be unique'.

### 3.2.7 Validation Notes

This should be enforced by a database constraint (e.g., `sql_constraints` in Odoo) to ensure data integrity at the lowest level.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to create a vehicle with an invalid Truck Number format

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am on the 'Create Vehicle' form

### 3.3.5 When

I enter 'INVALID-FORMAT' into the Truck Number field and attempt to save the record

### 3.3.6 Then

The system prevents the save action and displays a validation error next to the field, indicating that the format is incorrect and should match the standard Indian vehicle registration pattern.

### 3.3.7 Validation Notes

Test with several valid and invalid formats to ensure the validation logic (e.g., regex) is robust.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to create a vehicle without filling in a mandatory field

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am on the 'Create Vehicle' form

### 3.4.5 When

I fill in the Truck Number but leave the mandatory 'Capacity' field blank and click 'Save'

### 3.4.6 Then

The system prevents the record from being saved and visually highlights the 'Capacity' field, displaying a message that it is a required field.

### 3.4.7 Validation Notes

Verify this behavior for all fields defined as mandatory in the model.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

User discards the creation of a new vehicle

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am on the 'Create Vehicle' form and have entered some data

### 3.5.5 When

I click the 'Discard' button

### 3.5.6 Then

The form is closed, no new vehicle record is created, and I am returned to the vehicle list view.

### 3.5.7 Validation Notes

Confirm that no new record was written to the database.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Standard Odoo Form View for vehicle creation.
- Input field for 'Truck Number' (Text).
- Input field for 'Model' (Text).
- Input field for 'Capacity' (Numeric, with 'Tons' unit label).
- Selection/Dropdown for 'Owner Details' with options: 'Company-Owned', 'Outsourced'.
- Selection/Dropdown for 'Fuel Type' with options like 'Diesel', 'Petrol', 'CNG', 'Electric'.
- Date picker widget for 'Last Service Date' and 'Next Service Due Date'.
- Status field ('Active'/'Inactive') displayed, defaulting to 'Active'.
- 'Save & Close', 'Save & New', and 'Discard' buttons.

## 4.2.0 User Interactions

- Real-time validation feedback for invalid formats or missing mandatory fields upon attempting to save.
- Date pickers should provide a calendar interface for easy date selection.

## 4.3.0 Display Requirements

- All field labels must be clear and descriptive.
- Error messages must be displayed inline, next to the field causing the error.

## 4.4.0 Accessibility Needs

- The form must be fully navigable using the keyboard (tabbing through fields).
- All form fields must have associated labels for screen reader compatibility, adhering to WCAG 2.1 Level AA standards.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-002

### 5.1.2 Rule Description

The 'Truck Number' for each vehicle must be unique across all vehicle records.

### 5.1.3 Enforcement Point

Database level (unique constraint) and on the form upon save.

### 5.1.4 Violation Handling

Prevent record creation and display a user-friendly error message.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

TMS-BR-001

### 5.2.2 Rule Description

The 'Truck Number' must conform to the standard Indian vehicle registration number format.

### 5.2.3 Enforcement Point

On the form upon save, using a validation rule (e.g., regex).

### 5.2.4 Violation Handling

Prevent record creation and display a validation error message.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-058

#### 6.1.1.2 Dependency Reason

User must be able to log in to the system to access any functionality.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-070

#### 6.1.2.2 Dependency Reason

The system's Role-Based Access Control must be functional to ensure only authorized Admins can create vehicle records.

## 6.2.0.0 Technical Dependencies

- Odoo 18 framework and ORM.
- Definition of the `tms.vehicle` data model in the database.

## 6.3.0.0 Data Dependencies

- None for creation, but this story creates the foundational data required by Trip Management (e.g., US-027) and Expense Management (e.g., US-041).

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The vehicle creation form should load in under 2 seconds.
- The save operation (database write) should complete in under 200ms as per REQ-NFR-001.

## 7.2.0.0 Security

- Access to the vehicle creation functionality must be strictly limited to users with the 'Admin' role or equivalent permissions.
- Input validation must be performed on the server-side to prevent injection attacks.

## 7.3.0.0 Usability

- The form should be intuitive and follow standard Odoo design patterns for consistency.
- Error messages should be clear and guide the user on how to correct the input.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0.0 Compatibility

- The interface must be fully functional on modern web browsers (Chrome, Firefox, Safari, Edge) and be mobile-responsive.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Standard Odoo model and view creation.
- Requires implementing two specific validation rules: uniqueness and format regex for the truck number.
- This is a core model that will be linked to many other models, so the data structure must be well-defined from the start.

## 8.3.0.0 Technical Risks

- The regex for the Indian vehicle registration number could be complex and may need refinement to cover all valid state and territory formats.

## 8.4.0.0 Integration Points

- The created vehicle record will be a foreign key in other models, such as `tms.trip`, `tms.expense`, and `tms.service_log`.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E (UI Automation)

## 9.2.0.0 Test Scenarios

- Verify successful creation with valid data.
- Verify failure on duplicate truck number.
- Verify failure on invalid truck number format (test multiple invalid strings).
- Verify failure when each mandatory field is left blank one by one.
- Verify the 'Discard' functionality works as expected.
- Verify that a non-Admin user cannot access the creation form.

## 9.3.0.0 Test Data Needs

- A list of valid Indian vehicle registration numbers from different states.
- A list of invalid/malformed registration numbers.
- An existing vehicle record in the database to test the uniqueness constraint.

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- A UI automation framework like Selenium or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria are validated and passing.
- Code has been peer-reviewed and merged into the main branch.
- Unit tests for the model's constraints and methods are written and achieve >80% coverage.
- Automated E2E tests for the happy path and key error conditions are implemented and passing.
- The feature is deployed and verified in the staging environment by a QA engineer.
- The UI is confirmed to be responsive and meets accessibility standards.
- Any necessary technical documentation for the `tms.vehicle` model is created or updated.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story and a blocker for the entire Trip Management epic. It should be scheduled in one of the earliest development sprints.

## 11.4.0.0 Release Impact

This feature is a mandatory component of the Phase 1 (Core Operations) rollout as defined in REQ-TRN-001.


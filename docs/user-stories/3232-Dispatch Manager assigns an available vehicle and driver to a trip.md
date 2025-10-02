# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-027 |
| Elaboration Date | 2024-05-22 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager assigns an available vehicle and ... |
| As A User Story | As a Dispatch Manager, I want to select an availab... |
| User Persona | Dispatch Manager: Responsible for core logistics o... |
| Business Value | Enables the transition of a trip from planning to ... |
| Functional Area | Trip Management |
| Story Theme | Trip Lifecycle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Successful assignment of a valid vehicle and driver

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Dispatch Manager viewing a trip in 'Planned' status

### 3.1.5 When

I select an 'Active' vehicle with sufficient capacity and an 'Active' driver with a valid license, and save the assignment

### 3.1.6 Then

The system successfully links the selected vehicle and driver to the trip record, the trip's status changes from 'Planned' to 'Assigned', and a confirmation message is displayed.

### 3.1.7 Validation Notes

Verify in the database that the trip record's vehicle_id and driver_id fields are populated correctly and the state field is 'Assigned'. The UI should reflect these changes immediately.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Vehicle selection list is correctly filtered

### 3.2.3 Scenario Type

Alternative_Flow

### 3.2.4 Given

I am a Dispatch Manager viewing a trip in 'Planned' status with a material weight of 18 Tons

### 3.2.5 When

I open the vehicle selection dropdown

### 3.2.6 Then

The list of vehicles MUST NOT include any vehicles that are marked as 'Inactive' OR are currently assigned to another trip with a status of 'In-Transit'.

### 3.2.7 Validation Notes

Prepare test data with inactive and in-transit vehicles. Check the domain filter applied to the Odoo field to ensure it correctly excludes these records.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Driver selection list is correctly filtered

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

I am a Dispatch Manager viewing a trip in 'Planned' status

### 3.3.5 When

I open the driver selection dropdown

### 3.3.6 Then

The list of drivers MUST NOT include any drivers that are marked as 'Inactive', have an expired license, OR are currently assigned to another trip with a status of 'In-Transit'.

### 3.3.7 Validation Notes

Prepare test data with inactive drivers and drivers with expired licenses. Check the domain filter applied to the Odoo field to ensure it correctly excludes these records.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to assign a vehicle with insufficient capacity

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am a Dispatch Manager viewing a trip in 'Planned' status with a material weight of 25 Tons

### 3.4.5 When

I attempt to select and assign a vehicle with a registered capacity of only 20 Tons

### 3.4.6 Then

The system must prevent the assignment and display a clear, user-friendly error message, such as 'Assignment failed: Vehicle capacity (20 Tons) is less than the trip weight (25 Tons).'

### 3.4.7 Validation Notes

This can be implemented either by disabling invalid options in the dropdown or via a server-side validation check upon saving. The validation message is critical.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

UI updates after successful assignment

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I have successfully assigned a vehicle and driver to a trip

### 3.5.5 When

The trip form view is reloaded or updated

### 3.5.6 Then

The form must clearly display the assigned vehicle's truck number and the driver's name, and the status indicator must show 'Assigned'.

### 3.5.7 Validation Notes

Visual inspection of the Odoo Form View for the trip record.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Searchable dropdown (Many2one field) for Vehicle selection on the Trip form.
- Searchable dropdown (Many2one field) for Driver selection on the Trip form.
- A 'Save' or 'Confirm Assignment' button.
- A status bar/badge that visually represents the trip's current status ('Planned', 'Assigned', etc.).
- Read-only display fields for assigned vehicle and driver details after assignment.

## 4.2.0 User Interactions

- User opens a 'Planned' trip from the list/kanban view.
- User clicks into the Vehicle field to open a filtered list of available vehicles.
- User clicks into the Driver field to open a filtered list of available drivers.
- User saves the form to confirm the assignment.
- System provides immediate feedback (success message or validation error).

## 4.3.0 Display Requirements

- Vehicle dropdown should display Truck Number and Model.
- Driver dropdown should display Driver Name and License Number.
- Vehicles with insufficient capacity should be visually distinct (e.g., greyed out) or excluded from the selection list.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- Dropdown lists must be keyboard-navigable.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-003

### 5.1.2 Rule Description

A driver with an expired license cannot be assigned to a new trip.

### 5.1.3 Enforcement Point

During population of the driver selection list for trip assignment.

### 5.1.4 Violation Handling

Drivers with expired licenses are filtered out and are not available for selection.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-004

### 5.2.2 Rule Description

The trip status lifecycle must follow the defined path. This action transitions the status from 'Planned' to 'Assigned'.

### 5.2.3 Enforcement Point

Upon successful save of both a vehicle and driver to a 'Planned' trip.

### 5.2.4 Violation Handling

The status change is an atomic part of the successful assignment operation.

## 5.3.0 Rule Id

### 5.3.1 Rule Id

BR-007

### 5.3.2 Rule Description

The specified material weight for a trip shall not exceed the assigned vehicle's registered capacity.

### 5.3.3 Enforcement Point

During the assignment of a vehicle to a trip.

### 5.3.4 Violation Handling

The system prevents the assignment and displays a validation error message to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-026

#### 6.1.1.2 Dependency Reason

A trip must be created and exist in a 'Planned' state before resources can be assigned to it.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-006

#### 6.1.2.2 Dependency Reason

Vehicle master records, including capacity and status, must exist to be available for assignment.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-012

#### 6.1.3.2 Dependency Reason

Driver master records, including license expiry and status, must exist to be available for assignment.

## 6.2.0.0 Technical Dependencies

- Odoo ORM and Views framework.
- Completed data models for Trip, Vehicle, and Driver.

## 6.3.0.0 Data Dependencies

- Requires existing vehicle and driver records in the database for selection and testing of filters.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The filtered lists for vehicles and drivers should load in under 1 second for up to 1,000 active resources.

## 7.2.0.0 Security

- Only users with the 'Dispatch Manager' role (or 'Admin') can assign vehicles and drivers to a trip.

## 7.3.0.0 Usability

- Error messages for failed assignments must be clear and actionable.
- Filtering of selection lists should be automatic, requiring no extra steps from the user.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Implementing the dynamic domain filters for the vehicle and driver selection fields in Odoo is the primary complexity.
- Ensuring the definition of 'availability' (i.e., not on another 'In-Transit' trip) is robust.
- Handling multiple validation rules (capacity, license, status) in a clean and user-friendly way.

## 8.3.0.0 Technical Risks

- The logic for determining if a resource is 'already assigned' could become complex if future assignments need to be considered. The initial implementation should scope this to only currently 'In-Transit' trips.

## 8.4.0.0 Integration Points

- This feature directly reads from the Vehicle Master (tms.vehicle) and Driver Master (hr.employee) models.
- It directly updates the Trip (tms.trip) model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify a valid assignment moves the trip to 'Assigned'.
- Verify an inactive vehicle does not appear in the selection list.
- Verify a driver with an expired license does not appear in the selection list.
- Verify an attempt to assign an overweight vehicle fails with a proper error message.
- Verify a vehicle currently on an 'In-Transit' trip is not available for assignment to a new trip.

## 9.3.0.0 Test Data Needs

- A trip in 'Planned' status.
- Multiple vehicle records: one active/sufficient capacity, one inactive, one with insufficient capacity, one assigned to an in-transit trip.
- Multiple driver records: one active/valid license, one inactive, one with an expired license, one assigned to an in-transit trip.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests for domain filtering and validation logic are implemented and passing with >80% coverage
- Integration testing of the assignment workflow completed successfully
- User interface on the Trip form is reviewed and approved by the product owner
- Performance of the selection dropdowns is verified against requirements
- Role-based security is confirmed (only Dispatch Manager/Admin can perform the action)
- Relevant developer documentation for the filtering logic is created
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a core feature in the trip lifecycle and a blocker for subsequent trip statuses. It should be prioritized early, immediately after the master data models are stable.

## 11.4.0.0 Release Impact

- Critical for the initial release (MVP). The system is not viable without this functionality.


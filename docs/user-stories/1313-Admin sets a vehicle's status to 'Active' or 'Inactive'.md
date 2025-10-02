# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-008 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin sets a vehicle's status to 'Active' or 'Inac... |
| As A User Story | As an Admin, I want to set the status of a vehicle... |
| User Persona | Admin user responsible for maintaining master data... |
| Business Value | Improves data integrity by preventing the assignme... |
| Functional Area | Master Data Management |
| Story Theme | Vehicle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin deactivates an available vehicle

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am viewing the record of a vehicle with the status 'Active' that is not assigned to any trip in a non-terminal state (e.g., 'In-Transit', 'Assigned')

### 3.1.5 When

I change the vehicle's status to 'Inactive' and save the record

### 3.1.6 Then



```
The system saves the vehicle's status as 'Inactive'.
AND The vehicle no longer appears in the list of selectable vehicles when creating a new trip.
```

### 3.1.7 Validation Notes

Verify by checking the vehicle record's status and then attempting to create a new trip as a Dispatch Manager to confirm the vehicle is absent from the selection dropdown.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin reactivates an inactive vehicle

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and am viewing the record of a vehicle with the status 'Inactive'

### 3.2.5 When

I change the vehicle's status to 'Active' and save the record

### 3.2.6 Then



```
The system saves the vehicle's status as 'Active'.
AND The vehicle now appears in the list of selectable vehicles when creating a new trip.
```

### 3.2.7 Validation Notes

Verify by checking the vehicle record's status and then attempting to create a new trip as a Dispatch Manager to confirm the vehicle is present in the selection dropdown.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempting to deactivate a vehicle assigned to an active trip

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am logged in as an Admin and am viewing the record of a vehicle that is currently assigned to a trip with a status of 'Assigned' or 'In-Transit'

### 3.3.5 When

I attempt to change the vehicle's status to 'Inactive' and save

### 3.3.6 Then



```
The system prevents the status change.
AND The system displays a user-friendly error message, such as 'This vehicle cannot be deactivated as it is currently assigned to an active trip (Trip ID: [Trip ID]).'
```

### 3.3.7 Validation Notes

Create a trip, assign the vehicle, set the trip to 'In-Transit'. Then, as an Admin, try to deactivate the vehicle and verify the error message appears and the status remains 'Active'.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

New vehicle defaults to 'Active' status

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I am logged in as an Admin

### 3.4.5 When

I navigate to create a new vehicle record

### 3.4.6 Then

The status field on the new vehicle form defaults to 'Active'.

### 3.4.7 Validation Notes

Simply open the 'Create Vehicle' form and check the default value of the status field.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Inactive vehicles are retained for historical reporting

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

A vehicle was previously used on a completed trip and has since been set to 'Inactive'

### 3.5.5 When

I run a historical report (e.g., Trip Profitability Report) that includes the completed trip

### 3.5.6 Then

The report correctly displays the data for the completed trip, including the details of the now-inactive vehicle.

### 3.5.7 Validation Notes

Complete a trip with a vehicle. Deactivate the vehicle. Run a report covering the period of the trip and confirm the trip and vehicle data are present and correct.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Vehicle list view displays status and is filterable

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I am logged in as an Admin and viewing the list of all vehicles

### 3.6.5 When

I view the vehicle list

### 3.6.6 Then



```
The list view includes a column showing the 'Active'/'Inactive' status.
AND The list view defaults to showing only 'Active' vehicles.
AND I can remove the default filter to view all vehicles, including inactive ones.
```

### 3.6.7 Validation Notes

Navigate to the vehicle list view and verify the column exists, the default filter is applied, and that the filter can be removed to show all records.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A boolean toggle switch or similar control on the Vehicle Form View labeled 'Active'.
- A status column in the Vehicle List/Tree View.
- A default filter on the Vehicle List View for 'Active' status.

## 4.2.0 User Interactions

- Admin clicks the toggle to change the status from 'Active' to 'Inactive' or vice-versa.
- The change is persisted upon saving the vehicle record.
- Admin can search and filter the vehicle list based on the status field.

## 4.3.0 Display Requirements

- The current status ('Active' or 'Inactive') must be clearly visible on both the form and list views for a vehicle.
- Error messages for failed deactivation must be clear and informative.

## 4.4.0 Accessibility Needs

- The status toggle must be keyboard accessible and have a clear label for screen readers, compliant with WCAG 2.1 Level AA.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-VEH-STATUS-01

### 5.1.2 Rule Description

A vehicle cannot be set to 'Inactive' if it is currently assigned to a trip that is in an active state (e.g., 'Assigned', 'In-Transit').

### 5.1.3 Enforcement Point

On save/write operation of the vehicle record.

### 5.1.4 Violation Handling

Prevent the save operation and display a blocking error message to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-TRIP-ASSIGN-01

### 5.2.2 Rule Description

Only vehicles with an 'Active' status can be selected for assignment to a new trip.

### 5.2.3 Enforcement Point

In the vehicle selection field on the Trip creation/editing form.

### 5.2.4 Violation Handling

Filter the list of available vehicles to exclude any record where status is 'Inactive'.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

The vehicle model and views must exist before a status field can be added to them.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

This story is a consumer of the status field. The logic to filter the vehicle selection list on the trip form, as defined in this story's acceptance criteria, will be implemented in US-027.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM
- The `tms.vehicle` model must be defined.

## 6.3.0.0 Data Dependencies

*No items available*

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Filtering inactive vehicles from the trip assignment dropdown must not introduce any noticeable delay (>200ms) to the form load time.

## 7.2.0.0 Security

- Only users with the 'Admin' role (or equivalent permissions for managing vehicle master data) can modify the active/inactive status of a vehicle. This must be enforced via Odoo's access control lists (ACLs).

## 7.3.0.0 Usability

- The vehicle list should default to showing only active vehicles to reduce clutter for daily operations.
- The status control on the form should be visually intuitive.

## 7.4.0.0 Accessibility

- The feature must meet WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must function correctly on all supported browsers as per the overall project requirements.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Adding a boolean field to an Odoo model is a standard task.
- Implementing a domain filter on a Many2one field is a standard Odoo practice.
- The logic to check for active trips before deactivation requires overriding the `write` method, which is a common pattern but adds a small amount of complexity.

## 8.3.0.0 Technical Risks

- The definition of an 'active trip' must be precise. The check should include all relevant non-terminal statuses (e.g., 'Planned', 'Assigned', 'In-Transit', 'On Hold').

## 8.4.0.0 Integration Points

- The `tms.trip` model's form view, specifically the `vehicle_id` field.
- Any reporting modules that aggregate data based on vehicles.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify deactivation of an available vehicle and its removal from trip assignment list.
- Verify reactivation of a vehicle and its reappearance in trip assignment list.
- Verify system blocks deactivation of a vehicle on an active trip.
- Verify historical reports still function correctly with data from inactive vehicles.

## 9.3.0.0 Test Data Needs

- User accounts for 'Admin' and 'Dispatch Manager' roles.
- At least two vehicle records.
- A trip record that can be set to 'In-Transit' and 'Completed' states.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code is peer-reviewed and adheres to project coding standards (Flake8, Black).
- Unit tests are written for the business logic (e.g., blocking deactivation) and achieve required coverage.
- Integration testing confirms that the vehicle selection list on the trip form is correctly filtered.
- UI elements are reviewed and approved for usability and consistency.
- Security permissions are verified to ensure only authorized users can change the status.
- Relevant documentation (if any) is updated.
- The feature is deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a foundational piece of master data management. It should be completed before or in the same sprint as the trip assignment story (US-027) to ensure the business rule can be implemented correctly.

## 11.4.0.0 Release Impact

- This is a core feature for managing the vehicle fleet lifecycle within the system. Its absence would lead to operational errors and data clutter.


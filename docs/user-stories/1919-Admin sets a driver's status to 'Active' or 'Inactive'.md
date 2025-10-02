# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-014 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin sets a driver's status to 'Active' or 'Inact... |
| As A User Story | As an Admin, I want to change a driver's status be... |
| User Persona | Admin |
| Business Value | Ensures operational accuracy by preventing assignm... |
| Functional Area | Master Data Management |
| Story Theme | Driver Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin deactivates an available driver

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am viewing the record of a driver with the status 'Active' who is not assigned to any ongoing trips

### 3.1.5 When

I change the driver's status to 'Inactive' and save the record

### 3.1.6 Then

The system updates the driver's status to 'Inactive' and the record is preserved in the database.

### 3.1.7 Validation Notes

Verify in the database or on the driver's form view that the status is 'Inactive'. The standard Odoo 'active' field should be set to False.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin reactivates an inactive driver

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and am viewing the record of a driver with the status 'Inactive'

### 3.2.5 When

I change the driver's status to 'Active' and save the record

### 3.2.6 Then

The system updates the driver's status to 'Active'.

### 3.2.7 Validation Notes

Verify on the driver's form view that the status is now 'Active'. The standard Odoo 'active' field should be set to True.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Inactive driver is excluded from trip assignment

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A driver's status has been set to 'Inactive'

### 3.3.5 When

A Dispatch Manager creates a new trip and accesses the dropdown list to assign a driver

### 3.3.6 Then

The inactive driver's name must NOT appear in the list of available drivers.

### 3.3.7 Validation Notes

Check the domain filter on the driver selection field in the trip creation form. It should filter for active drivers only.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Admin attempts to deactivate a driver with an active trip

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am logged in as an Admin and a driver is assigned to a trip with a status of 'Assigned' or 'In-Transit'

### 3.4.5 When

I attempt to change that driver's status to 'Inactive'

### 3.4.6 Then

The system must prevent the change and display a user-friendly error message like 'Cannot deactivate a driver with an active trip. Please reassign or complete the trip first.'

### 3.4.7 Validation Notes

Create a trip and assign a driver. Attempt to deactivate the driver and verify the error message appears and the status remains 'Active'.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

New driver defaults to 'Active' status

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I am logged in as an Admin

### 3.5.5 When

I open the form to create a new driver record

### 3.5.6 Then

The status field for the new driver must default to 'Active'.

### 3.5.7 Validation Notes

Navigate to the 'New Driver' form and check the default value of the status field.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Non-Admin users cannot change driver status

### 3.6.3 Scenario Type

Security

### 3.6.4 Given

I am logged in as a 'Dispatch Manager' or 'Finance Officer'

### 3.6.5 When

I view a driver's record

### 3.6.6 Then

I must not have the ability to change the driver's 'Active'/'Inactive' status (the control should be read-only or hidden).

### 3.6.7 Validation Notes

Log in with a non-admin test user and attempt to modify the status. Verify access is denied.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A status toggle or button on the Driver form view (e.g., Odoo's standard 'Archive'/'Unarchive' button linked to the 'active' field).
- A status indicator column in the Driver list (tree) view.

## 4.2.0 User Interactions

- Admin clicks the status control to toggle between 'Active' and 'Inactive'.
- The system provides immediate visual feedback of the status change upon saving.

## 4.3.0 Display Requirements

- The current status ('Active' or 'Inactive') must be clearly visible on the driver's record.
- Error messages related to this functionality must be clear and informative.

## 4.4.0 Accessibility Needs

- The status control must be keyboard-accessible and have appropriate ARIA labels.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-003

### 5.1.2 Rule Description

A driver with an expired license cannot be assigned to a new trip. (Related rule, status is another check).

### 5.1.3 Enforcement Point

Trip Assignment

### 5.1.4 Violation Handling

Driver is excluded from selection list.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-TMS-01

### 5.2.2 Rule Description

A driver cannot be made 'Inactive' if they are assigned to a trip that is not in a terminal state (e.g., 'Delivered', 'Completed', 'Paid', 'Canceled').

### 5.2.3 Enforcement Point

On saving the Driver record after status change.

### 5.2.4 Violation Handling

Prevent save operation and display an error message to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-011

#### 6.1.1.2 Dependency Reason

This story creates the core driver record (extending hr.employee) where the status field will be added.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

This story consumes the status field. The logic in US-027 to filter available drivers depends on the completion of US-014.

## 6.2.0.0 Technical Dependencies

- Odoo 18 framework
- The custom Driver model (extension of `hr.employee`)
- The custom Trip model (to check for active assignments)

## 6.3.0.0 Data Dependencies

*No items available*

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The status change and save operation on the driver record should complete in under 500ms.
- The check for active trips should not introduce noticeable delay to the save operation.

## 7.2.0.0 Security

- Only users with the 'Admin' role (or equivalent high-level permissions) can modify the driver's active status.
- The status change must be logged in the system's audit trail as per REQ-DAT-008, recording the user, timestamp, and the change from old to new value.

## 7.3.0.0 Usability

- The control to change the status should be intuitive and follow standard Odoo conventions.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across supported modern web browsers (Chrome, Firefox, Safari).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This involves adding a standard Odoo 'active' boolean field.
- Requires a server-side constraint to check for active trips, which is a common pattern.
- Requires verification of the domain filter on a related model's form view.

## 8.3.0.0 Technical Risks

- The query to check for 'active' trips must be performant to avoid slowing down the save operation on the driver record.
- Forgetting to update the domain filter on the trip assignment field could lead to a silent failure where the business rule is not enforced.

## 8.4.0.0 Integration Points

- Trip Management Module: The driver status directly impacts the driver selection logic within this module.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify an admin can deactivate and reactivate a driver.
- Verify an inactive driver does not appear in the trip assignment dropdown.
- Verify an admin cannot deactivate a driver with an 'In-Transit' trip.
- Verify a non-admin user cannot change the driver status.
- Verify a newly created driver is 'Active' by default.

## 9.3.0.0 Test Data Needs

- Test users for 'Admin' and 'Dispatch Manager' roles.
- At least two driver records.
- A trip record with a status of 'In-Transit' assigned to one of the drivers.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the business logic (e.g., active trip constraint) are written, passing, and meet coverage targets
- Integration testing completed successfully in a staging environment
- User interface on the driver form/list view is reviewed and approved by the Product Owner
- Security requirements (role-based access) are validated
- Relevant documentation (if any) is updated
- Story is deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational feature for master data management and should be completed early in the development cycle.
- It is a prerequisite for the complete implementation of the trip assignment logic.

## 11.4.0.0 Release Impact

- This feature is critical for the initial release (MVP) as it provides essential operational control.


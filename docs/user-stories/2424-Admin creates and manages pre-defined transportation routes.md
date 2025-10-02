# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-019 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates and manages pre-defined transportati... |
| As A User Story | As an Admin, I want to create and manage a master ... |
| User Persona | Admin: A system administrator responsible for conf... |
| Business Value | Improves operational efficiency by reducing manual... |
| Functional Area | Master Data Management |
| Story Theme | Trip Planning & Configuration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-019-01

### 3.1.2 Scenario

Admin successfully creates a new pre-defined route

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

The user is logged in as an 'Admin' and has navigated to the 'Routes' management screen

### 3.1.5 When

The user initiates the creation of a new route and fills in all mandatory fields ('Route Name', 'Source', 'Destination', 'Standard Distance') with valid data

### 3.1.6 Then

The system saves the new route record to the database and it appears in the list of pre-defined routes.

### 3.1.7 Validation Notes

Verify the record is created in the `tms.route` table with the correct values. The user should be redirected to the list view, and the new route should be visible and searchable.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-019-02

### 3.2.2 Scenario

System prevents route creation with missing mandatory information

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

The user is on the new route creation form

### 3.2.5 When

The user attempts to save the route without providing a 'Route Name', 'Source', or 'Destination'

### 3.2.6 Then

The system prevents the record from being saved and displays a clear validation message indicating which fields are required.

### 3.2.7 Validation Notes

Test each mandatory field individually and in combination to ensure validation triggers correctly.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-019-03

### 3.3.2 Scenario

System validates data types for numeric fields

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

The user is on the new route creation form

### 3.3.5 When

The user enters non-numeric text into the 'Standard Distance (km)' or 'Estimated Transit Time' fields

### 3.3.6 Then

The system prevents the save and displays a user-friendly error message indicating that the field must be a number.

### 3.3.7 Validation Notes

Attempt to input strings like 'abc' or 'one hundred' into numeric fields and verify the validation.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-019-04

### 3.4.2 Scenario

System validates that distance and time are positive values

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

The user is on the new route creation form

### 3.4.5 When

The user enters '0' or a negative number for 'Standard Distance (km)'

### 3.4.6 Then

The system prevents the save and displays a validation message stating that the distance must be greater than zero.

### 3.4.7 Validation Notes

Test with values like 0, -10, and -0.5 to ensure the constraint is enforced.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-019-05

### 3.5.2 Scenario

Non-Admin users cannot access route management

### 3.5.3 Scenario Type

Security

### 3.5.4 Given

A user is logged in with a role other than 'Admin' (e.g., 'Dispatch Manager', 'Finance Officer', 'Driver')

### 3.5.5 When

The user attempts to navigate to the route management section via direct URL or menu

### 3.5.6 Then

The system denies access and displays an authorization error, and the menu item for route management is not visible to them.

### 3.5.7 Validation Notes

Log in as each non-admin role and verify the menu is hidden and direct access is blocked.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item under a 'Configuration' or 'Master Data' section of the TMS module, labeled 'Routes'.
- A standard Odoo list/tree view to display existing routes with columns for Name, Source, Destination, and Distance.
- A standard Odoo form view for creating and editing a route.
- Input fields on the form: 'Route Name' (Text), 'Source' (Text), 'Destination' (Text), 'Standard Distance (km)' (Numeric), 'Estimated Transit Time (hours)' (Numeric, optional).

## 4.2.0 User Interactions

- Admin can create, edit, and view routes.
- The list view for routes must be searchable by Name, Source, and Destination.
- The list view should be sortable by any of the displayed columns.

## 4.3.0 Display Requirements

- All created routes must be visible in the list view.
- Validation errors must be clearly displayed next to the corresponding fields on the form.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- Standard keyboard navigation (Tab, Enter) must be supported for form interaction.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-ROUTE-001

### 5.1.2 Rule Description

The 'Route Name' must be unique to prevent duplicate and confusing entries.

### 5.1.3 Enforcement Point

Database level (unique constraint) and on form save.

### 5.1.4 Violation Handling

The system will display a validation error message, such as 'A route with this name already exists.', and prevent the record from being saved.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-ROUTE-002

### 5.2.2 Rule Description

The 'Standard Distance (km)' must be a positive number greater than zero.

### 5.2.3 Enforcement Point

On form validation before saving.

### 5.2.4 Violation Handling

The system will display a validation error and prevent the record from being saved.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-001', 'dependency_reason': 'An Admin user account must exist to perform this function.'}

## 6.2.0 Technical Dependencies

- Requires the base Odoo 18 framework.
- Requires the creation of a new Odoo model (e.g., `tms.route`) and associated views (list, form) and access control lists.

## 6.3.0 Data Dependencies

- None. This story creates foundational data.

## 6.4.0 External Dependencies

- None.

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The route management list view should load in under 2 seconds with up to 1,000 route records.
- Saving a new route should complete within 500ms.

## 7.2.0 Security

- Access to create, write, and delete route records must be restricted to the 'Admin' user group via Odoo's `ir.model.access.csv`.
- Read access may be granted to other internal user groups like 'Dispatch Manager' if needed for selection purposes in other stories.

## 7.3.0 Usability

- The process of creating a route should be intuitive, following standard Odoo patterns for master data creation.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards, consistent with the overall system requirement (REQ-INT-001).

## 7.5.0 Compatibility

- The interface must be fully functional on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- This is a standard CRUD (Create, Read, Update, Delete) feature, which is a core competency of the Odoo framework.
- Involves creating one new model, two views, one menu item, and access control rules.
- No complex business logic or external integrations are required.

## 8.3.0 Technical Risks

- Minimal risk. The primary consideration is ensuring the data model is robust enough for future needs (e.g., should 'Source' and 'Destination' be simple text fields or linked to a more complex address/location model?). For the initial implementation, text fields are sufficient as per REQ-DAT-004.

## 8.4.0 Integration Points

- The created `tms.route` model will be a key integration point for the Trip Management feature (US-028), where Dispatch Managers will select from these pre-defined routes.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0 Test Scenarios

- Verify an Admin can create, read, update, and delete a route.
- Verify form validation for all fields (required, numeric, positive values, uniqueness).
- Verify that a user with the 'Dispatch Manager' role cannot see the 'Routes' menu item in Configuration and cannot create/edit routes.
- Verify that the search functionality on the list view works for all relevant fields.

## 9.3.0 Test Data Needs

- A set of at least 10-15 sample routes with varying names, sources, and destinations.
- Test data with invalid formats (e.g., text in numeric fields, negative numbers) to test validation.

## 9.4.0 Testing Tools

- Pytest for unit tests.
- Manual testing via the Odoo UI.
- Browser developer tools for checking UI behavior.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code for the `tms.route` model, views, and security rules is written, reviewed, and merged
- Unit tests covering model constraints and validations are implemented and achieve >80% coverage for the new code
- Manual E2E testing confirms all user interactions and validations work as expected
- Security testing confirms that non-Admin roles cannot access the functionality
- The feature is deployed and verified in the staging environment without regressions
- Developer documentation for the new model is added if necessary

# 11.0.0 Planning Information

## 11.1.0 Story Points

2

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational master data story. It should be prioritized early in the development cycle, as the Trip Creation feature (e.g., US-028) will depend on it.
- Low complexity makes it a good candidate for an early sprint to build momentum.

## 11.4.0 Release Impact

- This feature is a key enabler for the efficiency gains promised by the TMS. Its absence would significantly reduce the value of the trip planning module.


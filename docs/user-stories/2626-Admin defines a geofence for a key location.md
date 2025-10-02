# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-021 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin defines a geofence for a key location |
| As A User Story | As an Admin, I want to create, view, and manage na... |
| User Persona | Admin user with full system access, responsible fo... |
| Business Value | Enables automated, real-time monitoring of vehicle... |
| Functional Area | Master Data Management |
| Story Theme | GPS Tracking and Monitoring |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin successfully creates a new polygonal geofence

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

The Admin is logged in and has navigated to the 'Geofence Management' screen, which displays an interactive map.

### 3.1.5 When

The Admin clicks the 'Create' button, enters a unique name (e.g., 'Mumbai Central Warehouse'), draws a closed polygon on the map, and clicks 'Save'.

### 3.1.6 Then

The system saves the geofence with its name and coordinates, and the new geofence appears in the list of existing geofences and is visibly rendered on the map.

### 3.1.7 Validation Notes

Verify the new record exists in the database with correct name and geospatial data. The UI should update to show the new geofence without a page reload.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin views and edits an existing geofence

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An existing geofence is selected from the list and displayed on the map.

### 3.2.5 When

The Admin modifies the name of the geofence and/or adjusts the vertices of its polygon shape on the map, and then clicks 'Save'.

### 3.2.6 Then

The system updates the record with the new name and coordinates, and the changes are immediately reflected on the map and in the list view.

### 3.2.7 Validation Notes

Check the database to confirm the record was updated. Verify the UI shows the modified shape and name.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Admin successfully deletes a geofence

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

An existing geofence is selected from the list.

### 3.3.5 When

The Admin clicks the 'Delete' button and confirms the action in a confirmation dialog.

### 3.3.6 Then

The geofence is permanently removed from the system, disappears from the list view, and is no longer rendered on the map.

### 3.3.7 Validation Notes

Verify the record is deleted from the database. The UI should reflect the removal.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to save a geofence without a name

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

The Admin is in the process of creating a new geofence.

### 3.4.5 When

The Admin draws a polygon on the map but leaves the 'Name' field blank and clicks 'Save'.

### 3.4.6 Then

The system prevents the save operation and displays a user-friendly validation message, such as 'Geofence name is required'.

### 3.4.7 Validation Notes

Ensure no new record is created in the database. The validation message should be clear and visible.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to save a geofence with a duplicate name

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A geofence named 'Main Depot' already exists, and the Admin is creating a new geofence.

### 3.5.5 When

The Admin enters 'Main Depot' as the name for the new geofence and clicks 'Save'.

### 3.5.6 Then

The system prevents the save and displays a validation error, such as 'A geofence with this name already exists'.

### 3.5.7 Validation Notes

The check for name duplication should be case-insensitive. Verify no new record is created.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Attempt to save a geofence without a valid shape

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

The Admin is creating a new geofence.

### 3.6.5 When

The Admin provides a name but does not draw a shape (or draws an open/invalid shape with fewer than 3 points) and clicks 'Save'.

### 3.6.6 Then

The system prevents the save and displays a validation error, such as 'A valid, closed shape with at least 3 points is required'.

### 3.6.7 Validation Notes

Test by clicking save immediately after clicking create, and after drawing only one or two points.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Non-Admin user attempts to access the geofence management page

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

A user with a 'Dispatch Manager' or 'Driver' role is logged into the system.

### 3.7.5 When

The user attempts to navigate to the geofence management URL directly.

### 3.7.6 Then

The system denies access and displays an 'Access Denied' error, consistent with Odoo's security framework.

### 3.7.7 Validation Notes

Verify via Odoo's `ir.model.access.csv` that only the Admin group has CRUD permissions on the geofence model.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- An interactive map view (e.g., using Leaflet.js integrated with Odoo).
- A list or Kanban view displaying all existing geofences with their names.
- 'Create', 'Edit', 'Save', and 'Delete' buttons.
- A text input field for the geofence name.
- Map drawing tools: 'Start Drawing', 'Add Point', 'Finish Drawing', 'Cancel Drawing'.

## 4.2.0 User Interactions

- Clicking 'Create' enables drawing mode on the map.
- Clicking on the map in drawing mode adds vertices to the polygon.
- Vertices of an existing polygon should be draggable to edit the shape.
- Selecting a geofence from the list should center the map on and highlight that geofence.
- A confirmation modal must appear before deleting a geofence.

## 4.3.0 Display Requirements

- All saved geofences should be rendered on the map as semi-transparent, filled polygons.
- The name of the geofence should be visible, perhaps as a tooltip or a label at the center of the shape.

## 4.4.0 Accessibility Needs

- All UI controls (buttons, input fields) must have appropriate labels for screen readers.
- Keyboard navigation should be supported for the list view and action buttons.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-GEO-001

### 5.1.2 Rule Description

Each geofence must have a unique, non-empty name.

### 5.1.3 Enforcement Point

On create and update operations of a geofence record.

### 5.1.4 Violation Handling

The operation is blocked, and a user-facing validation error is displayed.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-GEO-002

### 5.2.2 Rule Description

A geofence must be defined by a valid, closed polygon with at least 3 vertices.

### 5.2.3 Enforcement Point

On create and update operations of a geofence record.

### 5.2.4 Violation Handling

The operation is blocked, and a user-facing validation error is displayed.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-029

#### 6.1.1.2 Dependency Reason

This story establishes the core map view component and GPS data display, which the geofence UI will be built upon.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-001

#### 6.1.2.2 Dependency Reason

Establishes the user management framework, which is required to enforce Admin-only access.

## 6.2.0.0 Technical Dependencies

- An Odoo map view module (e.g., `web_map`) and a frontend library (e.g., Leaflet.js).
- PostgreSQL with the PostGIS extension enabled for efficient storage and querying of geospatial data.
- A backend Python library (e.g., Shapely, GeoAlchemy2) to handle geometric operations and interact with PostGIS.

## 6.3.0.0 Data Dependencies

- This feature creates a new master data model for geofences. It has an optional dependency on Customer Location data (from `res.partner`) to enhance usability (e.g., centering the map).

## 6.4.0.0 External Dependencies

- An external map tile provider API (e.g., OpenStreetMap, Mapbox) to render the base map layer.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The map interface with up to 100 geofences rendered must load in under 4 seconds.
- Drawing and editing interactions on the map should feel instantaneous with no perceivable lag.

## 7.2.0.0 Security

- Only users with the 'Admin' role can create, edit, or delete geofences. This must be enforced at the model level using Odoo's access control lists (`ir.model.access.csv`).

## 7.3.0.0 Usability

- The drawing tools should be intuitive, allowing users to easily create and modify shapes without requiring special training.

## 7.4.0.0 Accessibility

- The feature should adhere to WCAG 2.1 Level AA standards where applicable, especially for form elements and controls.
- REQ-INT-001

## 7.5.0.0 Compatibility

- The map and drawing tools must function correctly on the latest versions of Chrome, Firefox, and Safari, including their mobile equivalents.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires integration of a third-party JavaScript map library into the Odoo Web Library (OWL) framework.
- Requires backend setup and development for handling geospatial data types (PostGIS), which is outside standard Odoo development.
- The logic for point-in-polygon checks, which will be used by the alerting feature (US-080), must be designed for high performance.

## 8.3.0.0 Technical Risks

- Potential performance issues when rendering a large number of complex geofences on the map.
- Complexity in managing the state of the drawing UI within the OWL component lifecycle.

## 8.4.0.0 Integration Points

- The created geofence data model will be read by the GPS data processing service to check for entry/exit events.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- CRUD operations for geofences.
- Validation rule enforcement (unique name, valid shape).
- Role-based access control for non-Admin users.
- UI responsiveness and drawing tool functionality on different screen sizes and browsers.
- Creating complex, concave, and multi-vertex polygons.

## 9.3.0.0 Test Data Needs

- A set of pre-defined geofences with varying complexity.
- User accounts with different roles (Admin, Dispatch Manager, etc.).

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- A UI automation framework like Cypress or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests for backend models and validation logic achieve >80% coverage.
- E2E tests for the geofence creation and editing flow are implemented and passing.
- Access control rules are verified to restrict access to Admins only.
- Feature is documented in the Administrator Guide.
- Story deployed and verified in the staging environment by a QA engineer or product owner.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a foundational blocker for the geofence alerting feature (US-080) and should be prioritized accordingly.
- A technical spike may be needed beforehand to evaluate and select the best Odoo map integration module and confirm the PostGIS setup.

## 11.4.0.0 Release Impact

This feature is a key component of the real-time tracking module. Its completion is critical for delivering the full value proposition of the GPS tracking functionality.


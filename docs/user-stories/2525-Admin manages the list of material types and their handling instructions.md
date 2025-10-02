# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-020 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin manages the list of material types and their... |
| As A User Story | As an Admin, I want to create, view, edit, and dea... |
| User Persona | Admin. This user is responsible for system configu... |
| Business Value | Ensures data integrity for accurate reporting, enh... |
| Functional Area | Master Data Management |
| Story Theme | Core System Configuration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin creates a new material type successfully

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

The user is logged in as an Admin and is on the 'Material Types' list view

### 3.1.5 When

The user clicks 'New', enters a unique name (e.g., 'Industrial Solvents') and optional handling instructions (e.g., 'Hazardous Material - Requires ventilation'), and clicks 'Save'

### 3.1.6 Then

The system creates a new, active material type record, and it appears in the list view.

### 3.1.7 Validation Notes

Verify the new record exists in the database with the correct data and the 'active' flag set to true.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin edits an existing material type

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An existing material type with the name 'Steel Beams' exists

### 3.2.5 When

The Admin opens the 'Steel Beams' record, updates the handling instructions to 'Heavy Load - Use appropriate lifting gear', and clicks 'Save'

### 3.2.6 Then

The system updates the record with the new handling instructions.

### 3.2.7 Validation Notes

Query the database or view the record in the UI to confirm the 'handling_instructions' field has been updated.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

System prevents creation of a material type with a duplicate name

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A material type with the name 'Cement Bags' already exists

### 3.3.5 When

The Admin attempts to create a new material type and enters 'Cement Bags' as the name

### 3.3.6 Then

The system prevents saving the record and displays a user-friendly validation error message, such as 'A material type with this name already exists.'

### 3.3.7 Validation Notes

Attempt to create a duplicate record and verify that the expected validation error is triggered and no new record is created.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

System prevents creation of a material type with a blank name

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

The Admin is on the 'New Material Type' form

### 3.4.5 When

The Admin leaves the 'Name' field blank and attempts to save the record

### 3.4.6 Then

The system prevents saving and highlights the 'Name' field as mandatory, showing a validation message.

### 3.4.7 Validation Notes

Verify that the form submission fails and the UI indicates that the name field is required.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Admin deactivates (archives) a material type

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

An active material type named 'Obsolete Part' exists

### 3.5.5 When

The Admin opens the record and uses the 'Archive' action

### 3.5.6 Then

The material type's 'active' flag is set to false, and it is hidden from the default list view.

### 3.5.7 Validation Notes

Check that the record is no longer in the default list. Use a filter to view archived records and confirm its presence there.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Deactivated material types are not available for selection on new trips

### 3.6.3 Scenario Type

Integration

### 3.6.4 Given

The material type 'Obsolete Part' has been archived

### 3.6.5 When

A Dispatch Manager creates a new trip and accesses the 'Material' selection field

### 3.6.6 Then

The 'Obsolete Part' material type does not appear in the list of available options.

### 3.6.7 Validation Notes

This requires the Trip creation story (US-026) to be implemented. Test by creating a new trip and inspecting the options in the material selection widget.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item 'Material Types' under the TMS module's 'Configuration' section.
- A standard Odoo list/tree view with columns for 'Name' and 'Active' status.
- A standard Odoo form view with fields for 'Name' (Char), 'Special Handling Instructions' (Text), and an 'Active' toggle.

## 4.2.0 User Interactions

- Standard CRUD operations (Create, Read, Update) via the Odoo web client.
- Ability to Archive/Unarchive records using standard Odoo actions.
- Search and filter functionality in the list view.

## 4.3.0 Display Requirements

- The material name must be clearly displayed in both list and form views.
- Handling instructions should be displayed in a multi-line text area on the form view.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The interface must be navigable using a keyboard, adhering to WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-MAT-001

### 5.1.2 Rule Description

The name of each material type must be unique within the system.

### 5.1.3 Enforcement Point

On create and update operations at the database and application level.

### 5.1.4 Violation Handling

A validation error is displayed to the user, and the transaction is rolled back.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-MAT-002

### 5.2.2 Rule Description

The name of a material type is a mandatory field.

### 5.2.3 Enforcement Point

On create and update operations at the database and application level.

### 5.2.4 Violation Handling

A validation error is displayed to the user, and the transaction is rolled back.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-001', 'dependency_reason': 'An Admin user account must exist to perform this function.'}

## 6.2.0 Technical Dependencies

- Odoo 18 framework and the base TMS addon module structure must be in place.

## 6.3.0 Data Dependencies

*No items available*

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The list view for material types should load in under 2 seconds with up to 1,000 records.

## 7.2.0 Security

- Only users with the 'Admin' role (or equivalent group permissions) can create, edit, or delete/archive material types, as per REQ-FNC-001.
- Other roles, such as 'Dispatch Manager', should have read-only access to this data.

## 7.3.0 Usability

- The interface should be consistent with the standard Odoo user experience.

## 7.4.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0 Compatibility

- Must function correctly on all modern web browsers supported by Odoo 18.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- This involves creating a standard Odoo model with basic fields and views.
- No complex business logic or external integrations are required.

## 8.3.0 Technical Risks

- Negligible. The primary risk would be incorrect configuration of access control rules, allowing non-Admins to modify the data.

## 8.4.0 Integration Points

- The 'Trip' model (to be developed in US-026) will have a Many2one relationship to this new 'Material Type' model.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Verify CRUD operations for material types.
- Test the uniqueness and mandatory constraints on the 'Name' field.
- Test the archive/unarchive functionality.
- Verify access rights for Admin vs. other roles.
- Once US-026 is complete, perform an integration test to confirm that archived materials do not appear in the trip creation form.

## 9.3.0 Test Data Needs

- A set of at least 10 sample material types with and without handling instructions.
- At least one archived material type.

## 9.4.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code is peer-reviewed and merged into the main development branch
- Unit tests covering model constraints (uniqueness, required) are implemented and achieve >80% coverage for the new model
- Integration testing with the Trip model's selection field is completed successfully (can be deferred until US-026 is ready)
- UI for list and form views is reviewed and approved
- Access control rules are implemented and verified for Admin and other relevant roles
- The feature is deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational master data story and should be prioritized early in the development cycle as it is a blocker for the core Trip Management feature (US-026).

## 11.4.0 Release Impact

- This feature is essential for the initial release (Phase 1) as defined in the implementation strategy (REQ-TRN-001).


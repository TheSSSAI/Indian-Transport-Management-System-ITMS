# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-017 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin creates and manages customer-specific rate a... |
| As A User Story | As an Admin, I want to create and manage customer-... |
| User Persona | Admin |
| Business Value | Ensures accurate and consistent billing, reducing ... |
| Functional Area | Master Data Management |
| Story Theme | Customer and Financial Configuration |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-017-01

### 3.1.2 Scenario

Create a new 'Per Km' rate agreement for a customer

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am an Admin logged into the system and am viewing the 'ABC Corp' customer record

### 3.1.5 When

I navigate to the 'Rate Agreements' section, click 'Add', and enter a new rate with a specific Source, Destination, Material, select 'Per Km' as the Rate Type, and enter a numeric value for the rate

### 3.1.6 Then

The system saves the new rate agreement, and it appears in the list of agreements for 'ABC Corp' with all the entered details correctly displayed.

### 3.1.7 Validation Notes

Verify the new record is created in the database and is visible in the customer's form view under a 'Rate Agreements' tab or list.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-017-02

### 3.2.2 Scenario

Create a new 'Per Ton' rate agreement for a customer

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am an Admin adding a new rate agreement for 'ABC Corp'

### 3.2.5 When

I select 'Per Ton' as the Rate Type and enter a numeric value for the rate

### 3.2.6 Then

The system saves the new 'Per Ton' rate agreement successfully.

### 3.2.7 Validation Notes

Confirm the record is saved with the correct rate type.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-017-03

### 3.3.2 Scenario

Create a new 'Fixed' rate agreement for a customer

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am an Admin adding a new rate agreement for 'ABC Corp'

### 3.3.5 When

I select 'Fixed' as the Rate Type and enter a numeric value for the rate

### 3.3.6 Then

The system saves the new 'Fixed' rate agreement successfully.

### 3.3.7 Validation Notes

Confirm the record is saved with the correct rate type.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-017-04

### 3.4.2 Scenario

Edit an existing rate agreement

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A rate agreement for 'ABC Corp' exists for the route 'Mumbai' to 'Delhi'

### 3.4.5 When

I open the existing rate agreement and change the rate value from '50' to '55'

### 3.4.6 Then

The system updates the record, and the list now shows the new rate of '55'.

### 3.4.7 Validation Notes

Check the database to ensure the value is updated. The system should log this change in the audit trail as per REQ-DAT-008.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-017-05

### 3.5.2 Scenario

Attempt to create a duplicate rate agreement

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A rate agreement already exists for 'ABC Corp' with Source 'Mumbai', Destination 'Delhi', and Material 'Steel Coils'

### 3.5.5 When

I attempt to create a new rate agreement for 'ABC Corp' with the exact same Source, Destination, and Material

### 3.5.6 Then

The system prevents the save action and displays a user-friendly error message, such as 'A rate agreement for this customer, route, and material combination already exists.'

### 3.5.7 Validation Notes

Verify that a database unique constraint is enforced on the combination of customer, source, destination, and material.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-017-06

### 3.6.2 Scenario

Attempt to save a rate agreement with invalid data

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am creating a new rate agreement

### 3.6.5 When

I enter a negative number (e.g., -100) or non-numeric text in the 'Rate' field and try to save

### 3.6.6 Then

The system displays a validation error message, such as 'Rate must be a positive number', and does not save the record.

### 3.6.7 Validation Notes

Test with negative numbers, zero, and text strings to ensure proper field validation.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-017-07

### 3.7.2 Scenario

Archive an obsolete rate agreement

### 3.7.3 Scenario Type

Alternative_Flow

### 3.7.4 Given

An old rate agreement exists for a customer that is no longer valid

### 3.7.5 When

I locate the rate agreement and set its status to 'Archived' or 'Inactive'

### 3.7.6 Then

The rate agreement is no longer considered for new trip calculations but is retained in the system for historical reporting purposes.

### 3.7.7 Validation Notes

Verify that creating a new trip with the same parameters does not use the archived rate. The archived rate should still be linked to historical trips that used it.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new tab or section labeled 'Rate Agreements' on the Customer form view (extending `res.partner`).
- A list/tree view within this tab to display existing rate agreements.
- Columns in the list view for: Source, Destination, Material, Rate Type, Rate, Status (Active/Archived).
- 'Add' and 'Edit' buttons to manage rate agreements.
- A form/modal for creating/editing a rate agreement with fields for Source, Destination, Material (dropdowns/Many2one), Rate Type (selection/dropdown), and Rate (numeric field).

## 4.2.0 User Interactions

- The Admin can add, edit, and archive rate agreements directly from the customer's record.
- Source, Destination, and Material fields should be searchable lookups to their respective master data models.

## 4.3.0 Display Requirements

- The list of rate agreements should be clearly associated with the specific customer being viewed.
- Validation error messages must be displayed clearly to the user near the relevant field.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The UI must be navigable using a keyboard, adhering to WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-RATE-001

### 5.1.2 Rule Description

A rate agreement must be unique for a given combination of Customer, Source, Destination, and Material.

### 5.1.3 Enforcement Point

On create and on update of a rate agreement record.

### 5.1.4 Violation Handling

Prevent saving the record and display a user-facing error message.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-RATE-002

### 5.2.2 Rule Description

The rate value must be a positive, non-zero number.

### 5.2.3 Enforcement Point

On save of a rate agreement record.

### 5.2.4 Violation Handling

Prevent saving the record and display a field-level validation error.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-015

#### 6.1.1.2 Dependency Reason

Rate agreements are associated with a customer record, so the customer master must exist first.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-019

#### 6.1.2.2 Dependency Reason

Rate agreements are defined for specific routes (Source/Destination), requiring the Route Master to be available for selection.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-020

#### 6.1.3.2 Dependency Reason

Rate agreements can be material-specific, requiring the Material Master to be available for selection.

## 6.2.0.0 Technical Dependencies

- Requires a new Odoo model (e.g., `tms.rate.agreement`) with relationships to `res.partner`, `tms.location` (or similar for Source/Destination), and `tms.material`.
- Requires modification of the `res.partner` form view to include the new One2many field for rate agreements.

## 6.3.0.0 Data Dependencies

- Relies on existing Customer, Route, and Material master data.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Loading the customer form with up to 100 rate agreements should not noticeably impact page load time (<500ms added latency).

## 7.2.0.0 Security

- Only users with the 'Admin' role (or specifically granted permissions) can create, edit, or archive rate agreements, as per REQ-FNC-001.
- Changes to rate agreements must be logged in the audit trail as per REQ-DAT-008.

## 7.3.0.0 Usability

- The process of adding a new rate should be intuitive and require minimal clicks from the customer screen.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across supported modern web browsers.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Creation of a new Odoo model and its associated views (form, tree).
- Implementing a robust unique constraint across multiple fields.
- Modifying the standard Odoo `res.partner` view to embed the new functionality.
- This story lays the foundation for rate auto-population in trip creation (US-026), so the data model must be designed with that future integration in mind.

## 8.3.0.0 Technical Risks

- Potential performance degradation on the customer form if a customer has thousands of rate agreements. Consider pagination or optimized loading for the list view.
- Ensuring the rate lookup logic for future stories is efficient.

## 8.4.0.0 Integration Points

- This story's primary integration point will be with the Trip Management module (US-026), where the trip creation form will need to query this new model to find and apply the correct rate.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify creation, editing, and archiving of all three rate types (Per Km, Per Ton, Fixed).
- Test the unique constraint by attempting to create duplicates.
- Test field validations for the rate value (negative, zero, text).
- Verify that an Admin can perform these actions, while a user with a different role (e.g., Driver) cannot.
- Integration Test: After this story is complete, create a test that verifies the Trip Creation story (US-026) can correctly fetch and use a rate defined here.

## 9.3.0.0 Test Data Needs

- A set of test customers, routes, and materials.
- Test cases with multiple rate agreements for a single customer.

## 9.4.0.0 Testing Tools

- Odoo's built-in testing framework.
- Pytest for unit tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for model constraints and business logic, with >80% coverage
- Integration testing with the customer model completed successfully
- User interface on the customer form reviewed and approved by the product owner
- Security permissions are correctly implemented and verified
- Technical documentation for the new `tms.rate.agreement` model is created
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story for automated billing. It should be prioritized early in the development cycle, ideally before or in the same sprint as the trip creation story (US-026) to allow for integrated development and testing.

## 11.4.0.0 Release Impact

- This feature is a key differentiator for the system, moving it from a simple tracking tool to a financially integrated management platform. It is critical for the 'Finance & Tracking' phase of the rollout (REQ-TRN-001).


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-026 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager creates a new trip |
| As A User Story | As a Dispatch Manager, I want to create a new trip... |
| User Persona | Dispatch Manager: Responsible for core logistics o... |
| Business Value | Initiates the primary revenue-generating workflow ... |
| Functional Area | Trip Management |
| Story Theme | Trip Lifecycle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-026-01

### 3.1.2 Scenario

Successful trip creation with all valid manual inputs

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a Dispatch Manager and am on the 'New Trip' form

### 3.1.5 When

I select an 'Active' customer, manually enter a Source and Destination, select a Material, enter a Weight, select a Rate Type (e.g., 'Fixed'), enter a Rate value, and select a future Expected Delivery Date

### 3.1.6 Then

The system successfully creates a new trip record with a unique ID, sets its initial status to 'Planned', and redirects me to the Trip List view where the new trip is visible at the top.

### 3.1.7 Validation Notes

Verify the new record in the database (`tms.trip` model). Check that the status is correctly set to 'planned'. Confirm the user is redirected to the list view.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-026-02

### 3.2.2 Scenario

Trip creation using a pre-defined route

### 3.2.3 Scenario Type

Alternative_Flow

### 3.2.4 Given

I am on the 'New Trip' form and pre-defined routes exist in the system

### 3.2.5 When

I select a pre-defined route from the 'Route' dropdown

### 3.2.6 Then

The 'Source', 'Destination', and 'Standard Distance' fields on the form are automatically populated with the values from the selected route record.

### 3.2.7 Validation Notes

Test with a known route record. Verify that the form fields update immediately after selection without a page reload.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-026-03

### 3.3.2 Scenario

Attempt to save a trip with missing mandatory fields

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am on the 'New Trip' form

### 3.3.5 When

I attempt to save the form without selecting a Customer (or Source, or Destination)

### 3.3.6 Then

The system prevents the record from being saved and displays a clear, user-friendly validation message next to the required field (e.g., 'Customer is a required field').

### 3.3.7 Validation Notes

Test this for each mandatory field identified in BR-006 (Customer, Source, Destination) individually.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-026-04

### 3.4.2 Scenario

Attempt to save a trip with a past Expected Delivery Date

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am on the 'New Trip' form

### 3.4.5 When

I select an 'Expected Delivery Date' that is before the current date

### 3.4.6 Then

The system prevents the record from being saved and displays a validation message: 'Expected Delivery Date cannot be in the past'.

### 3.4.7 Validation Notes

Test with yesterday's date. The validation should be triggered upon attempting to save.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-026-05

### 3.5.2 Scenario

Customer selection field only shows active customers

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

There are both 'Active' and 'Inactive' customers in the system

### 3.5.5 When

I click on the 'Customer' selection field on the 'New Trip' form

### 3.5.6 Then

The list of available customers for selection only contains customers with an 'Active' status.

### 3.5.7 Validation Notes

Requires test data with at least one 'Inactive' customer. Verify this customer does not appear in the search results or dropdown list.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-026-06

### 3.6.2 Scenario

Dynamic revenue calculation based on rate type

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I am on the 'New Trip' form and have entered a distance and weight

### 3.6.5 When

I select the rate type 'per km' and enter a rate, OR 'per ton' and enter a rate

### 3.6.6 Then

A read-only 'Estimated Revenue' field on the form updates automatically to show the calculated total (Rate * Distance or Rate * Weight).

### 3.6.7 Validation Notes

This should be an on-change calculation. Verify the calculation is correct for both 'per km' and 'per ton' types.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A standard Odoo Form View for creating a new Trip.
- Searchable dropdown (Many2one) for 'Customer'.
- Searchable dropdown (Many2one) for 'Route'.
- Text fields for 'Source' and 'Destination'.
- Searchable dropdown (Many2one) for 'Material'.
- Numeric field for 'Weight' (in Tons).
- Selection field for 'Rate Type' with options: 'Fixed', 'per km', 'per ton'.
- Numeric field for 'Rate'.
- Date picker for 'Expected Delivery Date'.
- Read-only field for 'Estimated Revenue'.
- 'Save & Close', 'Save & New', and 'Discard' buttons.

## 4.2.0 User Interactions

- Selecting a pre-defined route auto-populates source, destination, and distance fields.
- Changing the 'Rate Type' or its associated values (Rate, Weight, Distance) dynamically recalculates the 'Estimated Revenue'.
- Validation messages should appear inline next to the relevant field upon a failed save attempt.

## 4.3.0 Display Requirements

- The newly created trip must have its status clearly displayed as 'Planned'.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The form must be navigable using a keyboard.
- Validation errors must be programmatically associated with their respective fields.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-004

### 5.1.2 Rule Description

The trip status lifecycle must begin with 'Planned'.

### 5.1.3 Enforcement Point

On creation of a new trip record.

### 5.1.4 Violation Handling

System must default the status to 'Planned'. This is not user-configurable at creation.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-006

### 5.2.2 Rule Description

A new trip record cannot be saved without a valid Customer, Source location, and Destination location.

### 5.2.3 Enforcement Point

On attempting to save the new trip form.

### 5.2.4 Violation Handling

Prevent save operation and display a validation error to the user.

## 5.3.0 Rule Id

### 5.3.1 Rule Id

BR-008

### 5.3.2 Rule Description

The 'Expected Delivery Date' for a new trip must be on or after the current date.

### 5.3.3 Enforcement Point

On attempting to save the new trip form.

### 5.3.4 Violation Handling

Prevent save operation and display a validation error to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-015

#### 6.1.1.2 Dependency Reason

Requires the Customer Master module to be functional to select a customer.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-019

#### 6.1.2.2 Dependency Reason

Requires the Route Master module to be functional to select a pre-defined route.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-020

#### 6.1.3.2 Dependency Reason

Requires the Material Master module to be functional to select a material type.

## 6.2.0.0 Technical Dependencies

- The core Odoo ORM and Views framework.
- A defined `tms.trip` Odoo model with all necessary fields and relationships.

## 6.3.0.0 Data Dependencies

- Requires existing records in the Customer, Route, and Material master data tables for selection.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The 'New Trip' form must load in under 3 seconds.
- Search-as-you-type results for Customer and Route fields must appear in under 500ms.

## 7.2.0.0 Security

- Only users with 'Dispatch Manager' or 'Admin' roles (or equivalent permissions) can access the functionality to create a new trip, as per REQ-FNC-001.

## 7.3.0.0 Usability

- The form layout should be logical and group related fields together (e.g., route details, material details, financial details).
- Error messages must be clear and guide the user on how to correct the input.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of Chrome, Firefox, and Safari, including their mobile-friendly responsive views.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creation of a new core Odoo model (`tms.trip`) and its associated views (form, tree, kanban).
- Implementation of multiple server-side validation rules (BR-006, BR-008).
- Implementation of client-side logic (on-change events) for auto-populating fields from a selected route and for dynamic revenue calculation.
- Requires setting up the initial state of a state machine for the trip lifecycle.

## 8.3.0.0 Technical Risks

- Performance of searchable dropdowns if master data (e.g., customers) grows very large. May require optimization of Odoo's `name_search` method.
- Potential for future complexity in the rate calculation logic if more rate types are added.

## 8.4.0.0 Integration Points

- Reads from `res.partner` (Customer), `tms.route` (Route), and `tms.material` (Material) models.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Create a trip with valid data and verify its creation.
- Create a trip using a pre-defined route and verify auto-population.
- Attempt to create a trip with each mandatory field missing one by one.
- Attempt to create a trip with a past delivery date.
- Verify that inactive customers do not appear in the selection list.
- Verify the accuracy of the dynamic revenue calculation for all rate types.

## 9.3.0.0 Test Data Needs

- At least 2 'Active' customers.
- At least 1 'Inactive' customer.
- At least 2 pre-defined routes.
- At least 3 material types.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- A UI automation framework like Selenium or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit tests for all new business logic and validations have been written and are passing with >80% coverage.
- Automated E2E tests for the happy path and key error conditions are passing.
- The feature has been demonstrated to and accepted by the Product Owner.
- All UI elements are mobile-responsive.
- Relevant technical documentation for the `tms.trip` model has been created.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story for the entire trip management workflow. It must be completed after the master data stories (US-015, US-019, US-020) but before any trip assignment or tracking stories.
- Requires close collaboration with the UX designer to finalize the form layout for efficiency.

## 11.4.0.0 Release Impact

- This story is critical for the Phase 1 (Core Operations) rollout as defined in REQ-TRN-001. The system is not usable without this functionality.


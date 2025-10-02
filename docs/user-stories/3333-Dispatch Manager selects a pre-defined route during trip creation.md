# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-028 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager selects a pre-defined route durin... |
| As A User Story | As a Dispatch Manager, I want to select a pre-defi... |
| User Persona | Dispatch Manager: A user responsible for core logi... |
| Business Value | Increases operational efficiency by reducing manua... |
| Functional Area | Trip Management |
| Story Theme | Trip Planning and Creation |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Select a pre-defined route and auto-populate trip details

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Dispatch Manager on the 'Create New Trip' form, and at least one pre-defined route exists in the system (e.g., 'Mumbai to Delhi', Distance: 1420 km).

### 3.1.5 When

I select the 'Mumbai to Delhi' route from the 'Route' selection field.

### 3.1.6 Then



```
The 'Source' field on the trip form is automatically populated with 'Mumbai'.
AND The 'Destination' field is automatically populated with 'Delhi'.
AND The 'Standard Distance' field is automatically populated with '1420'.
```

### 3.1.7 Validation Notes

Verify that the onchange event on the route field correctly fetches and sets the values for the source, destination, and distance fields on the trip form view.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Override auto-populated values after selecting a route

### 3.2.3 Scenario Type

Alternative_Flow

### 3.2.4 Given

I have selected a pre-defined route, and the 'Source', 'Destination', and 'Distance' fields have been auto-populated.

### 3.2.5 When

I manually edit the 'Destination' field to a different location (e.g., 'Gurgaon').

### 3.2.6 Then



```
The 'Destination' field must retain the new value 'Gurgaon'.
AND The 'Source' and 'Distance' fields must remain as they were auto-populated.
```

### 3.2.7 Validation Notes

Confirm that the auto-populated fields are not read-only and can be modified by the user after the initial population.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Clear the route selection

### 3.3.3 Scenario Type

Alternative_Flow

### 3.3.4 Given

I have selected a pre-defined route, and the 'Source', 'Destination', and 'Distance' fields have been auto-populated.

### 3.3.5 When

I clear the selection in the 'Route' field.

### 3.3.6 Then

The 'Source', 'Destination', and 'Standard Distance' fields that were previously auto-populated must become empty.

### 3.3.7 Validation Notes

Test the onchange event to ensure it handles the case where the route field is cleared, resetting the dependent fields.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Overwrite manually entered data with route selection

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am on the 'Create New Trip' form and have manually entered 'Kolkata' into the 'Source' field.

### 3.4.5 When

I then select the pre-defined route 'Mumbai to Delhi'.

### 3.4.6 Then

The 'Source' field's value must be updated from 'Kolkata' to 'Mumbai'.

### 3.4.7 Validation Notes

Ensure the onchange event from the route selection takes precedence and overwrites any pre-existing manual data in the target fields.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

No pre-defined routes exist

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am a Dispatch Manager on the 'Create New Trip' form.

### 3.5.5 When

I access the 'Route' selection field, and no routes have been configured in the Route Master.

### 3.5.6 Then

The system should allow me to proceed with creating the trip by manually entering the Source, Destination, and Distance without any errors.

### 3.5.7 Validation Notes

Verify that the trip form remains fully functional for manual entry when the Route Master data is empty. The route selection field can be empty or show a 'No records found' message.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Route' selection field (Odoo Many2one widget) on the Trip creation form.

## 4.2.0 User Interactions

- User can search for routes by name in the selection field.
- Selecting a route from the dropdown/search results triggers an onchange event.
- Clearing the route selection field also triggers an onchange event.

## 4.3.0 Display Requirements

- The 'Source', 'Destination', and 'Standard Distance' fields must update instantly upon route selection without a full page refresh.

## 4.4.0 Accessibility Needs

- The 'Route' selection field must be keyboard accessible and have a proper ARIA label.

# 5.0.0 Business Rules

- {'rule_id': 'REQ-DAT-004', 'rule_description': 'The system shall auto-populate the source, destination, and distance fields when a pre-defined route is selected during trip creation.', 'enforcement_point': "On the 'Create Trip' form, during the onchange event of the 'Route' field.", 'violation_handling': 'N/A. This is a feature implementation, not a validation rule.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-019

#### 6.1.1.2 Dependency Reason

The functionality to create and manage pre-defined routes (Route Master) must exist before a user can select one.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

The core functionality to create a new trip, including the trip creation form, must exist as the context for this feature.

## 6.2.0.0 Technical Dependencies

- Odoo 18 Web Framework (OWL)
- Odoo ORM and `onchange` decorator mechanism

## 6.3.0.0 Data Dependencies

- Requires access to the 'Route Master' model (from REQ-DAT-004) to fetch route data.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The auto-population of fields after selecting a route must complete in under 200ms to ensure a smooth user experience.

## 7.2.0.0 Security

- Access to this feature is restricted to users with the 'Dispatch Manager' role or equivalent permissions to create trips.

## 7.3.0.0 Usability

- The feature should be intuitive, requiring no special training. The cause-and-effect of selecting a route should be immediately obvious.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- Functionality must be consistent across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard Odoo development pattern using a Many2one field and an `onchange` method.
- The logic is self-contained within the Trip model and its view.
- No complex calculations or external API calls are required.

## 8.3.0.0 Technical Risks

- Minimal risk. A poorly implemented onchange method could cause minor UI lag, but this is unlikely given the simplicity of the operation.

## 8.4.0.0 Integration Points

- Directly integrates with the 'Trip' model and reads from the 'Route Master' model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify successful auto-population with a valid route.
- Verify user can override auto-populated data.
- Verify clearing the route selection clears dependent fields.
- Verify selecting a route overwrites existing manual data.
- Verify the form works correctly when no routes are available.

## 9.3.0.0 Test Data Needs

- A set of at least 3-5 pre-defined routes with unique names, sources, destinations, and distances.
- A test environment with no pre-defined routes.

## 9.4.0.0 Testing Tools

- Pytest for Odoo unit tests.
- Manual testing via the Odoo web client.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests for the onchange logic implemented and passing with >80% coverage
- Integration testing completed successfully within the trip creation workflow
- User interface reviewed and approved for responsiveness and usability
- Performance requirements verified
- Security requirements validated
- Documentation updated appropriately
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

1

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a key quality-of-life improvement for Dispatch Managers and should be prioritized early in the development of the Trip Management module.
- Must be scheduled in a sprint after US-019 (Route Master creation) is complete.

## 11.4.0.0 Release Impact

- Enhances the core trip creation workflow. Its inclusion is expected for the initial release of the Trip Management feature.


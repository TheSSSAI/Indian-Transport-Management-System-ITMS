# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-049 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver starts a trip from the mobile portal |
| As A User Story | As a Driver, I want to be able to mark a trip as '... |
| User Persona | Driver, who accesses the system via a mobile-frien... |
| Business Value | Provides real-time operational visibility to dispa... |
| Functional Area | Trip Management |
| Story Theme | Driver On-Road Workflow |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Happy Path: Driver successfully starts an assigned trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Driver logged into the mobile portal and viewing the details of a trip that is assigned to me and has the status 'Assigned'

### 3.1.5 When

I tap the 'Start Trip' button and confirm the action in the subsequent prompt

### 3.1.6 Then

The system updates the trip's status to 'In-Transit' and the change is saved to the database.

### 3.1.7 Validation Notes

Verify the trip record's state field is 'In-Transit'. Check the UI on the driver's portal and the manager's trip view for the updated status.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

System logs a 'Trip Start' event upon successful trip start

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A driver has successfully started a trip

### 3.2.5 When

The trip status is changed from 'Assigned' to 'In-Transit'

### 3.2.6 Then

The system automatically creates a new event log entry associated with the trip, with the event type 'Trip Start' and an accurate timestamp.

### 3.2.7 Validation Notes

Query the trip event history model for the specific trip and confirm the existence of a 'Trip Start' event record.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

UI updates after a trip is started

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am a Driver on the trip details page

### 3.3.5 When

I successfully start the trip

### 3.3.6 Then

The 'Start Trip' button is hidden or replaced with a non-interactive status indicator showing 'In-Transit'.

### 3.3.7 Validation Notes

Manually test the UI flow on a mobile browser to ensure the button's state changes correctly after the action is completed.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Action is unavailable for trips not in 'Assigned' status

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

I am a Driver viewing the details of a trip assigned to me

### 3.4.5 When

The trip's status is anything other than 'Assigned' (e.g., 'In-Transit', 'Delivered', 'Canceled')

### 3.4.6 Then

The 'Start Trip' button must not be visible or must be disabled.

### 3.4.7 Validation Notes

Check the trip details page for trips in various states to confirm the button is not available for interaction.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

System prevents starting a trip with an expired driver's license

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am a Driver viewing an 'Assigned' trip

### 3.5.5 And

My driver's license expiry date in the system is in the past

### 3.5.6 When

I attempt to start the trip

### 3.5.7 Then

The system must prevent the status change and display a clear error message to me, such as 'Cannot start trip: Your license has expired.'

### 3.5.8 Validation Notes

Set a driver's license expiry date to yesterday and attempt to start a trip. Verify the error message is shown and the trip status remains 'Assigned'.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

System prevents starting a trip with an inactive vehicle

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am a Driver viewing an 'Assigned' trip

### 3.6.5 And

The vehicle assigned to the trip is marked as 'Inactive'

### 3.6.6 When

I attempt to start the trip

### 3.6.7 Then

The system must prevent the status change and display a clear error message, such as 'Cannot start trip: The assigned vehicle is currently inactive.'

### 3.6.8 Validation Notes

Set the assigned vehicle's status to 'Inactive' and attempt to start the trip. Verify the error and that the status does not change.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Backend authorization check

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

I am a logged-in Driver

### 3.7.5 When

I attempt to trigger the 'start trip' action for a trip that is not assigned to me (e.g., via a direct API call)

### 3.7.6 Then

The system must reject the request with an 'Access Denied' or similar authorization error, and the trip's status must not be changed.

### 3.7.7 Validation Notes

Use an API client like Postman to send a request to the 'start trip' endpoint using the credentials of a driver not assigned to the target trip. Verify a 403 Forbidden or similar error is returned.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A prominent, clearly labeled 'Start Trip' button on the trip details view.
- A confirmation modal/dialog (e.g., 'Are you sure you want to start this trip?').
- A toast notification or inline message to confirm success or failure.
- A static text indicator to display the 'In-Transit' status after the trip has started.

## 4.2.0 User Interactions

- User taps the 'Start Trip' button.
- User confirms the action in a modal.
- System provides immediate visual feedback on the action's outcome.

## 4.3.0 Display Requirements

- The trip's current status must always be clearly visible.
- Error messages must be user-friendly and explain why the action failed.

## 4.4.0 Accessibility Needs

- The 'Start Trip' button must have a minimum tap target size of 44x44 CSS pixels.
- Button text must have sufficient color contrast against its background to meet WCAG 2.1 AA standards.
- The button and confirmation dialog must be keyboard-navigable and screen-reader accessible.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-004

### 5.1.2 Rule Description

The trip status lifecycle must follow the defined path: `Planned` -> `Assigned` -> `In-Transit`...

### 5.1.3 Enforcement Point

This action enforces the transition from 'Assigned' to 'In-Transit'.

### 5.1.4 Violation Handling

The action to start a trip is only available when the current state is 'Assigned'.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-003

### 5.2.2 Rule Description

A driver with an expired license cannot be assigned to a new trip.

### 5.2.3 Enforcement Point

The system will re-validate this rule at the point of starting the trip as an extra safeguard.

### 5.2.4 Violation Handling

The trip start action is blocked, and an error message is displayed to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-027

#### 6.1.1.2 Dependency Reason

A trip must be created and assigned to a driver and vehicle before it can be started.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-046

#### 6.1.2.2 Dependency Reason

The driver must be able to log in to the system to access their trips.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-047

#### 6.1.3.2 Dependency Reason

The driver needs a view to list and select their assigned trips.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-050

#### 6.1.4.2 Dependency Reason

The underlying functionality to log trip events must exist, as this action creates a 'Trip Start' event.

## 6.2.0.0 Technical Dependencies

- Odoo Trip model with a 'state' field supporting 'Assigned' and 'In-Transit'.
- Odoo security rules (`ir.rule`) to restrict drivers to their own trips.
- The Driver Portal UI framework (OWL) must be in place.

## 6.3.0.0 Data Dependencies

- Requires existing trip, driver, and vehicle records in the database.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The server-side state change and response must complete in under 200ms, as per REQ-NFR-001.

## 7.2.0.0 Security

- The action must be protected by a server-side authorization check to ensure only the assigned driver can start the trip. Relying on hiding the UI button is not sufficient.

## 7.3.0.0 Usability

- The action must be simple and intuitive, requiring no more than two taps (one to initiate, one to confirm) on a mobile device.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of major mobile browsers (Chrome on Android, Safari on iOS).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- The core logic is a standard Odoo model state transition.
- Requires adding validation checks for driver license and vehicle status before the state change.
- Frontend work in OWL is required for the button, confirmation dialog, and UI update.

## 8.3.0.0 Technical Risks

- Potential for race conditions if the trip status is modified by another user (e.g., a manager canceling it) at the exact moment the driver tries to start it. The backend logic should handle this gracefully.

## 8.4.0.0 Integration Points

- This action updates the central Trip model, which is read by other parts of the system (e.g., Manager Dashboard, Reporting module).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security
- Usability

## 9.2.0.0 Test Scenarios

- Verify a driver can start their assigned trip.
- Verify the 'Start Trip' button is not present for trips in other statuses.
- Verify a driver cannot start a trip assigned to another driver.
- Verify a trip cannot be started if the driver's license is expired.
- Verify a trip cannot be started if the assigned vehicle is inactive.
- Test the UI flow on a small mobile screen.

## 9.3.0.0 Test Data Needs

- A user account with the 'Driver' role.
- A trip record in 'Assigned' status, assigned to the test driver.
- A trip record in 'In-Transit' status to verify the button is hidden.
- A driver record with an expired license.
- A vehicle record with an 'Inactive' status.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- A frontend testing framework like Cypress or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests implemented for the backend logic with >80% coverage and all are passing
- Integration tests for validation rules are implemented and passing
- E2E test scenario for the happy path is automated and passing
- User interface reviewed and approved by the Product Owner for mobile usability
- Security requirements (server-side authorization) validated
- Documentation for the feature (if any) is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a core feature for the driver workflow and a prerequisite for tracking and delivery updates. It should be prioritized early in the development of the driver portal.

## 11.4.0.0 Release Impact

- Essential for the Phase 1 (Core Operations) rollout as defined in REQ-TRN-001.


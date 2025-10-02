# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-051 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver reports a trip halt |
| As A User Story | As a Driver, I want to report that my trip is halt... |
| User Persona | Driver, accessing the system via the mobile-friend... |
| Business Value | Provides real-time visibility of operational delay... |
| Functional Area | Trip Management |
| Story Theme | Driver Portal & On-Trip Operations |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Driver successfully reports a trip halt

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Driver, logged into the Driver Portal and viewing the details of my active trip which is in 'In-Transit' status

### 3.1.5 When

I tap the 'Report Halt' button, enter a valid reason (e.g., 'Unexpected road closure due to accident'), and tap 'Submit'

### 3.1.6 Then

The system records a 'Halt' event against the trip record, storing the reason, the driver's identity, and the current timestamp.

### 3.1.7 And

A high-priority alert is generated and displayed on the dashboard for users with the 'Dispatch Manager' or 'Admin' role, as per REQ-REP-002.

### 3.1.8 Validation Notes

Verify the new event log in the trip's history. Log in as a Dispatch Manager to confirm the alert appears on the dashboard.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Driver attempts to report a halt without a reason

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am a Driver on the 'Report Halt' screen for my active trip

### 3.2.5 When

I tap the 'Submit' button without entering any text in the reason field

### 3.2.6 Then

The submission is blocked.

### 3.2.7 And

A validation error message is displayed on the screen, such as 'A reason for the halt is mandatory'.

### 3.2.8 Validation Notes

Check that no event is logged and the UI displays the expected error message.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

The 'Report Halt' option is not available for non-active trips

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

I am a Driver, logged into the Driver Portal

### 3.3.5 When

I view the details of a trip that is in 'Assigned', 'Delivered', or 'Canceled' status

### 3.3.6 Then

The 'Report Halt' button is not visible or is disabled.

### 3.3.7 Validation Notes

Check the trip details screen for trips in various statuses to ensure the button's visibility is correctly controlled.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

System handles network failure during submission

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am a Driver on the 'Report Halt' screen with a valid reason entered, but my device has lost its internet connection

### 3.4.5 When

I tap the 'Submit' button

### 3.4.6 Then

The system displays an informative error message, such as 'No network connection. Please try again when you are online'.

### 3.4.7 And

The data I entered in the reason field is preserved so I don't have to re-type it.

### 3.4.8 Validation Notes

Use browser developer tools to simulate offline mode and test the submission process.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A clearly labeled 'Report Halt' button on the active trip details view.
- A modal or dedicated screen for reporting the halt.
- A multi-line text area for entering the reason.
- A 'Submit' button to confirm the action.
- A 'Cancel' or close button to exit the action.
- Client-side validation message display area.

## 4.2.0 User Interactions

- Tapping 'Report Halt' opens the submission form.
- Tapping 'Submit' triggers validation and, if successful, sends the data to the server.
- A success or error message is displayed to the user after the submission attempt.

## 4.3.0 Display Requirements

- The reason field must be clearly marked as mandatory.
- The trip identifier (e.g., Trip ID) should be visible on the halt reporting screen for context.

## 4.4.0 Accessibility Needs

- All UI elements must have sufficient color contrast and be operable via keyboard or screen reader, adhering to WCAG 2.1 Level AA standards (REQ-INT-001).

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-HALT-001

### 5.1.2 Rule Description

A reason for a trip halt is mandatory.

### 5.1.3 Enforcement Point

Client-side form validation and server-side API validation.

### 5.1.4 Violation Handling

The submission is rejected, and an error message is returned to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-HALT-002

### 5.2.2 Rule Description

A halt can only be reported for a trip that is currently in the 'In-Transit' status.

### 5.2.3 Enforcement Point

The UI will hide/disable the button for trips in other statuses. The server-side API will reject any requests for trips not in the correct status.

### 5.2.4 Violation Handling

API will return an error code (e.g., 409 Conflict) if the trip is in an invalid state.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

Driver must be able to log into the portal to access any functionality.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-047

#### 6.1.2.2 Dependency Reason

Driver must be able to view their assigned trips to select one to report a halt on.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-049

#### 6.1.3.2 Dependency Reason

A trip must be started and in 'In-Transit' status before a halt can be reported.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-065

#### 6.1.4.2 Dependency Reason

The manager's dashboard alert panel must exist to receive and display the notification generated by this action.

## 6.2.0.0 Technical Dependencies

- Odoo's messaging and notification system (`mail.thread` or equivalent).
- A backend API endpoint to receive and process the halt report.
- The Driver Portal's UI framework (OWL).

## 6.3.0.0 Data Dependencies

- Requires an existing Trip record assigned to the logged-in Driver.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The API response for the submission should be under 500ms.
- The user should receive visual feedback in the UI within 2 seconds of tapping 'Submit' on a standard mobile connection (as per REQ-NFR-001).

## 7.2.0.0 Security

- The API endpoint must be authenticated and authorized, ensuring a driver can only report halts for trips they are assigned to.
- All input from the reason field must be properly sanitized to prevent XSS attacks.

## 7.3.0.0 Usability

- The feature must be easily discoverable and usable with minimal taps on a mobile device, as per the simplified driver interface requirement (REQ-INT-001).

## 7.4.0.0 Accessibility

- Must meet WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0.0 Compatibility

- The feature must be fully functional on modern mobile web browsers (Chrome, Safari) on screen sizes from 360px width upwards (REQ-INT-001).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Requires both frontend (OWL component) and backend (Odoo controller) development.
- Integration with the existing Odoo notification system is required.
- The business logic is straightforward and self-contained.

## 8.3.0.0 Technical Risks

- Potential for delays in the notification system under heavy load, which could impact the real-time nature of the alert.

## 8.4.0.0 Integration Points

- Odoo Trip Model: To log the event.
- Odoo Notification System: To create an alert for managers.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- Verify successful halt submission and alert generation.
- Verify validation failure for empty reason.
- Verify the button is not present for trips in 'Assigned' or 'Delivered' states.
- Verify API security by attempting to report a halt for a trip assigned to another driver.
- Verify UI responsiveness on various mobile device screen sizes.

## 9.3.0.0 Test Data Needs

- A test user with the 'Driver' role.
- A test user with the 'Dispatch Manager' role.
- At least one trip in 'In-Transit' status assigned to the test driver.
- At least one trip in 'Assigned' status assigned to the test driver.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Browser developer tools for frontend testing and network simulation.
- An E2E testing framework like Cypress or Playwright would be beneficial.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the backend controller with >80% coverage
- Integration testing completed to ensure the alert is generated correctly
- User interface reviewed and approved for mobile usability
- Performance requirements verified
- Security requirements validated (authorization checks, input sanitization)
- Documentation updated appropriately
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a core operational feature for drivers.
- Dependent on the completion of the basic driver portal and trip view (US-046, US-047) and the manager's dashboard alert panel (US-065).

## 11.4.0.0 Release Impact

- Enhances the real-time tracking and management capabilities of the system, a key value proposition.


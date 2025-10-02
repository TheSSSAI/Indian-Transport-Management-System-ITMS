# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-065 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Manager views and acknowledges critical alerts on ... |
| As A User Story | As a Dispatch Manager or Admin, I want to view a d... |
| User Persona | Dispatch Manager, Admin |
| Business Value | Improves operational responsiveness by centralizin... |
| Functional Area | Dashboard & Reporting |
| Story Theme | Operational Monitoring & Exception Handling |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Display of a new critical trip event alert

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in Manager viewing the main dashboard, and a driver has just logged a critical event ('Accident') for an active trip

### 3.1.5 When

the dashboard loads or updates

### 3.1.6 Then

the 'Critical Alerts' panel must display a new, unacknowledged alert.

### 3.1.7 Validation Notes

The alert must be visually distinct as 'new' or 'unacknowledged' (e.g., bright color, bold text). The alert content must include the event type ('Accident'), vehicle number, and trip ID. The alert must have a timestamp.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Acknowledging a critical alert

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am viewing an unacknowledged alert in the 'Critical Alerts' panel

### 3.2.5 When

I click the 'Acknowledge' button for that specific alert

### 3.2.6 Then

the alert's visual state must change to 'acknowledged' (e.g., background becomes grey, icon changes).

### 3.2.7 Validation Notes

The 'Acknowledge' button should become disabled or be removed. An audit entry must be created linking my user ID and the current timestamp to the acknowledged alert.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Navigating from an alert to its source record

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am viewing an alert in the 'Critical Alerts' panel related to a trip

### 3.3.5 When

I click on the main body of the alert (not the 'Acknowledge' button)

### 3.3.6 Then

the system must navigate me directly to the detail form view of the associated trip record.

### 3.3.7 Validation Notes

Test this for different alert types: trip events navigate to trips, document expiries navigate to vehicles/drivers, low balance alerts navigate to the card management screen.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Alert panel empty state

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am a logged-in Manager viewing the main dashboard

### 3.4.5 When

there are no active, unacknowledged critical alerts for the system

### 3.4.6 Then

the 'Critical Alerts' panel must display a clear, user-friendly message, such as 'No critical alerts at this time.'

### 3.4.7 Validation Notes

The panel should not show an error or appear broken. It should clearly communicate the absence of alerts.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Display of multiple types of alerts

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am a logged-in Manager and multiple alert-triggering events have occurred: a trip 'Repair' event, a vehicle's insurance is expiring in 7 days, and a FASTag card balance is low

### 3.5.5 When

I view the dashboard

### 3.5.6 Then

the 'Critical Alerts' panel must display three distinct, unacknowledged alerts, sorted with the newest on top.

### 3.5.7 Validation Notes

Verify that each alert displays context-appropriate information and links to the correct source record.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Alert panel updates without full page reload

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I have the dashboard open and visible on my screen

### 3.6.5 When

a new critical event is triggered elsewhere in the system (e.g., by a driver's action)

### 3.6.6 Then

the new alert must appear in the 'Critical Alerts' panel within 15 seconds without requiring me to manually refresh the page.

### 3.6.7 Validation Notes

This can be tested using Odoo's bus/long-polling mechanism. The update should be efficient and not cause UI flickering.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Access restriction for non-manager roles

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

a user with the 'Driver' role is logged into the system

### 3.7.5 When

they access their user portal/dashboard

### 3.7.6 Then

the 'Critical Alerts' panel must not be visible or accessible.

### 3.7.7 Validation Notes

Check the view's XML definition to ensure it is restricted to the correct user groups ('Admin', 'Dispatch Manager').

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A dedicated dashboard widget/panel titled 'Critical Alerts'.
- A list container for individual alert items.
- For each alert: an icon representing the alert type (e.g., accident, document, finance), a text description, a timestamp, and an 'Acknowledge' button.
- A message for the empty state when no alerts are present.
- A subtle visual indicator to differentiate unacknowledged alerts from acknowledged ones (e.g., color, font weight).

## 4.2.0 User Interactions

- Clicking the 'Acknowledge' button performs the acknowledgment action.
- Clicking the alert body navigates to the source record.
- The panel should be scrollable if the list of alerts exceeds the allocated space.

## 4.3.0 Display Requirements

- Alerts should be sorted chronologically, with the most recent alert at the top.
- The alert text must be concise but informative enough to understand the context without clicking through (e.g., 'Accident reported for vehicle MH04AB1234 on Trip-00123').

## 4.4.0 Accessibility Needs

- Color should not be the only means of distinguishing alert states; use icons or text in addition.
- All interactive elements (buttons, links) must be keyboard-navigable and have clear focus indicators.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-ALERT-001

### 5.1.2 Rule Description

An acknowledged alert is considered actioned from a notification standpoint but must remain in the system for audit purposes.

### 5.1.3 Enforcement Point

When the 'Acknowledge' action is triggered.

### 5.1.4 Violation Handling

N/A - System behavior.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-ALERT-002

### 5.2.2 Rule Description

Only users with 'Dispatch Manager' or 'Admin' roles can view and acknowledge alerts in this panel.

### 5.2.3 Enforcement Point

On dashboard view rendering.

### 5.2.4 Violation Handling

The panel is not rendered for unauthorized users.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-064

#### 6.1.1.2 Dependency Reason

The main dashboard must exist to serve as a container for the alerts panel.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-050

#### 6.1.2.2 Dependency Reason

Driver's ability to log trip events is a primary trigger for generating critical alerts.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-077

#### 6.1.3.2 Dependency Reason

The system logic that generates alerts from critical events must be in place.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-078

#### 6.1.4.2 Dependency Reason

The system logic for generating document expiry alerts must be implemented.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-081

#### 6.1.5.2 Dependency Reason

The system logic for generating low card balance alerts must be implemented.

## 6.2.0.0 Technical Dependencies

- Odoo's dashboard view framework (e.g., `board.board`).
- Odoo's bus module or equivalent real-time communication channel for live updates.
- A new database model (e.g., `tms.alert`) to store alert information, status, and audit trails.

## 6.3.0.0 Data Dependencies

- Requires data from Trips, Vehicles, Drivers, and Card Management modules to generate meaningful alerts.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The query fetching alerts for the dashboard must execute in under 100ms to avoid delaying the dashboard load.
- Real-time updates should not cause noticeable performance degradation on the client-side.

## 7.2.0.0 Security

- Alerts displayed must be scoped to the data the user is permitted to see, as per their record rules.
- The acknowledgment action must be logged against the specific user who performed it for auditability.

## 7.3.0.0 Usability

- The alerts panel must be intuitive and require no training to understand.
- The distinction between acknowledged and unacknowledged alerts must be immediately obvious.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The dashboard widget must render correctly on all supported browsers and be responsive on mobile screen sizes as per REQ-INT-001.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires a new, flexible data model (`tms.alert`) that can link to multiple other models (Trip, Vehicle, Driver, etc.).
- Implementation of a real-time update mechanism using Odoo's bus system.
- Logic for generating alerts needs to be integrated into multiple, disparate parts of the application (e.g., trip event handling, scheduled jobs for expiry checks).

## 8.3.0.0 Technical Risks

- The real-time update feature could be complex to implement robustly, potentially leading to missed updates or performance issues if not handled carefully.
- Ensuring the alert generation logic is not brittle and captures all required events without creating duplicates.

## 8.4.0.0 Integration Points

- The Trip model, when a critical event is logged.
- Scheduled actions that check for document/license expiries.
- The Card Balance model, when a balance is updated below a threshold.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- End-to-end flow: A driver logs an 'Accident', a manager sees the alert, navigates to the trip, and acknowledges the alert.
- Expiry check: Manually set a vehicle document's expiry date to be within the alert threshold, run the scheduled job, and verify the alert appears.
- UI behavior: Test with zero, one, and many (e.g., 20+) alerts to check scrolling and performance.
- Role-based access: Log in as each user role to confirm who can and cannot see the panel.

## 9.3.0.0 Test Data Needs

- Users with 'Admin', 'Dispatch Manager', and 'Driver' roles.
- Trips in an 'In-Transit' state.
- Vehicles and drivers with documents having various expiry dates (expired, expiring soon, not expiring).

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in tour/JS testing framework for frontend validation.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit test coverage for new logic is at or above the project standard (80%).
- An end-to-end automated test for the primary success scenario has been created and is passing.
- The UI has been reviewed by a UX designer or product owner and approved.
- The performance impact on dashboard loading has been measured and is within acceptable limits.
- Security audit trail for acknowledgment is confirmed to be working.
- Relevant user documentation (e.g., in the User Manual) has been updated to explain the feature.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a high-value feature for managers and should be prioritized early after its dependencies are met.
- Requires both backend (model, business logic, triggers) and frontend (OWL component) development, which can be done in parallel to some extent.

## 11.4.0.0 Release Impact

This feature is a key component of the manager's dashboard and a major selling point for operational control. Its absence would be a significant gap in the user experience.


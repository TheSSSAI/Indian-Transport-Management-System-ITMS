# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-077 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System automatically changes trip status to 'On Ho... |
| As A User Story | As a Dispatch Manager, I want the system to automa... |
| User Persona | Dispatch Manager, Admin |
| Business Value | Enables immediate operational awareness of on-road... |
| Functional Area | Trip Management |
| Story Theme | Operational Monitoring and Alerts |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Trip status changes to 'On Hold' when driver logs an 'Accident' event

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A trip exists with the status 'In-Transit'

### 3.1.5 When

The assigned driver logs a new trip event of type 'Accident'

### 3.1.6 Then

The trip's status is automatically updated to 'On Hold' AND a high-priority alert is generated for the Admin/Manager dashboard AND the event is recorded in the trip's history.

### 3.1.7 Validation Notes

Verify the trip record's state field in the database. Check the manager's dashboard for a new alert related to this trip. Check the trip's chatter/log for the 'Accident' event entry.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Trip status changes to 'On Hold' when driver logs a 'Repair' event

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A trip exists with the status 'In-Transit'

### 3.2.5 When

The assigned driver logs a new trip event of type 'Repair'

### 3.2.6 Then

The trip's status is automatically updated to 'On Hold'.

### 3.2.7 Validation Notes

Verify the trip record's state field in the database changes from 'in_transit' to 'on_hold'.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Trip status changes to 'On Hold' when driver logs a 'Government Stoppage' event

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A trip exists with the status 'In-Transit'

### 3.3.5 When

The assigned driver logs a new trip event of type 'Government Stoppage'

### 3.3.6 Then

The trip's status is automatically updated to 'On Hold'.

### 3.3.7 Validation Notes

Verify the trip record's state field in the database changes from 'in_transit' to 'on_hold'.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Trip status does not change for non-critical events

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

A trip exists with the status 'In-Transit'

### 3.4.5 When

The assigned driver logs a new trip event of type 'Fueling' or 'Trip Start'

### 3.4.6 Then

The trip's status remains 'In-Transit' AND the event is recorded in the trip's history without generating a critical alert.

### 3.4.7 Validation Notes

Verify the trip record's state field remains 'in_transit'. Check the trip's chatter/log for the event entry.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Logging a critical event on a trip that is not 'In-Transit'

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A trip exists with the status 'Assigned'

### 3.5.5 When

The assigned driver logs a new trip event of type 'Accident'

### 3.5.6 Then

The trip's status is automatically updated to 'On Hold'.

### 3.5.7 Validation Notes

This ensures that if a problem occurs before the trip officially starts (e.g., an accident in the yard), it is still flagged correctly.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Logging a critical event on a trip already 'On Hold'

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

A trip exists with the status 'On Hold'

### 3.6.5 When

The assigned driver logs another new trip event of type 'Repair'

### 3.6.6 Then

The trip's status remains 'On Hold' AND the new event is added to the trip's history.

### 3.6.7 Validation Notes

Verify the state does not change and the new event is visible in the trip's log.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- This story is primarily backend logic. The UI impact is the result of the status change.
- Trip Kanban/List View: The trip card/row must visually reflect the new 'On Hold' status.
- Manager Dashboard: The 'Alerts Panel' must display a new high-priority notification for the critical event.

## 4.2.0 User Interactions

- No direct user interaction for this story. This is a system-automated reaction to an action defined in US-050.

## 4.3.0 Display Requirements

- The 'On Hold' status should be clearly distinguishable, possibly with a different color (e.g., red or orange) in list and kanban views.

## 4.4.0 Accessibility Needs

- Status changes indicated by color must also be accompanied by a text label to meet accessibility standards.

# 5.0.0 Business Rules

- {'rule_id': 'BR-005', 'rule_description': "Logging of critical events ('Accident', 'Repair', 'Government Stoppage') by a driver shall automatically change the trip status to 'On Hold'.", 'enforcement_point': 'On creation of a new trip event record.', 'violation_handling': 'N/A. This is a system process rule.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-050

#### 6.1.1.2 Dependency Reason

This story implements the backend logic that is triggered by the functionality in US-050 (Driver logs a trip event). The API endpoint and data model for trip events must exist first.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

A trip model with a state machine (including 'In-Transit' and 'On Hold' statuses) must exist.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-065

#### 6.1.3.2 Dependency Reason

The manager's dashboard with an 'Alerts Panel' must exist to display the generated high-priority alert.

## 6.2.0.0 Technical Dependencies

- Odoo's automation or model ORM capabilities for triggering actions on record creation.
- The system's notification/alerting service.

## 6.3.0.0 Data Dependencies

- A predefined list of 'Trip Event Types' with a flag to identify which ones are 'critical'.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The status update and alert generation must be completed within 5 seconds of the server receiving the event log from the driver's device.

## 7.2.0.0 Security

- The system must validate that the user logging the event is the driver currently assigned to that specific trip.

## 7.3.0.0 Usability

- The resulting status change and alert must be unambiguous and immediately draw the manager's attention.

## 7.4.0.0 Accessibility

*No items available*

## 7.5.0.0 Compatibility

*No items available*

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- The logic is a straightforward state transition.
- Requires a clear definition of which event types are 'critical'. A new boolean field `is_critical` on the `tms.event.type` model is recommended for maintainability.
- The logic can be implemented by overriding the `create` method of the `tms.trip.event` model or using an Odoo Automated Action.

## 8.3.0.0 Technical Risks

- If the list of critical events is hard-coded, it will require a code change to update. A configurable model is preferred.
- Potential for race conditions if multiple events are logged simultaneously, though unlikely to be a major issue.

## 8.4.0.0 Integration Points

- Trip Event model (`tms.trip.event`)
- Trip model (`tms.trip`)
- System Notification/Alerting module

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify status change for each defined critical event type.
- Verify status does NOT change for any non-critical event type.
- Verify behavior when a critical event is logged for a trip in 'Assigned' state.
- Verify behavior when a critical event is logged for a trip already in 'On Hold' state.
- End-to-end test: Log in as Driver, log event, log out. Log in as Manager, verify status change on trip list and presence of alert on dashboard.

## 9.3.0.0 Test Data Needs

- A user with 'Driver' role.
- A user with 'Dispatch Manager' role.
- An active trip in 'In-Transit' status assigned to the test driver.
- An active trip in 'Assigned' status assigned to the test driver.
- A list of event types, with at least 3 marked as critical and 2 marked as non-critical.

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- Browser-based E2E testing framework (e.g., Cypress, Playwright) or manual testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests implemented for the state transition logic, covering all ACs, with >80% coverage for new code
- Integration testing completed to verify the trigger from event creation to status change
- The list of critical events is confirmed with the Product Owner
- The generation of a dashboard alert is verified
- Documentation for the event type configuration is updated
- Story deployed and verified in the staging environment by QA

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a core part of the real-time operational monitoring feature set.
- Must be scheduled in a sprint after or alongside its prerequisite, US-050.

## 11.4.0.0 Release Impact

This feature is critical for the initial release (MVP) as it directly addresses a key business need for managing operational exceptions.


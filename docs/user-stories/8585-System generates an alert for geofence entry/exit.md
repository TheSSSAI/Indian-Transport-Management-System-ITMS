# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-080 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System generates an alert for geofence entry/exit |
| As A User Story | As a Dispatch Manager, I want to receive automatic... |
| User Persona | Dispatch Manager, Admin |
| Business Value | Provides real-time operational awareness of vehicl... |
| Functional Area | GPS Tracking & Alerts |
| Story Theme | Real-Time Fleet Monitoring |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Vehicle enters a geofence for the first time on a trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A vehicle 'MH-01-AB-1234' is on an 'In-Transit' trip, and a geofence named 'Customer Warehouse A' is defined and associated with the trip's destination.

### 3.1.5 When

The system processes a GPS location update for 'MH-01-AB-1234' that is inside the boundary of 'Customer Warehouse A', and its previous known state was 'outside' this geofence.

### 3.1.6 Then

The system shall generate an 'Entry' event.

### 3.1.7 And

The alert must be visible in the 'Alerts Panel' on the Dispatch Manager's dashboard.

### 3.1.8 Validation Notes

Verify the alert record is created in the database and appears in the UI for a logged-in Dispatch Manager. The timestamp should match the GPS data point's timestamp.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Vehicle exits a geofence

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

Vehicle 'MH-01-AB-1234' has a known state of 'inside' the 'Customer Warehouse A' geofence.

### 3.2.5 When

The system processes a GPS location update for 'MH-01-AB-1234' that is outside the boundary of 'Customer Warehouse A'.

### 3.2.6 Then

The system shall generate an 'Exit' event.

### 3.2.7 And

The alert must be visible in the 'Alerts Panel' on the Dispatch Manager's dashboard.

### 3.2.8 Validation Notes

Verify the alert record is created and the vehicle's state is updated. The alert should appear in the UI.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

No duplicate alerts are generated for a vehicle remaining within a geofence

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

Vehicle 'MH-01-AB-1234' has already triggered an 'Entry' alert for 'Customer Warehouse A' and its state is 'inside'.

### 3.3.5 When

The system processes subsequent GPS location updates that are also inside the 'Customer Warehouse A' boundary.

### 3.3.6 Then

No new 'Entry' alerts for this geofence and vehicle shall be generated.

### 3.3.7 Validation Notes

Monitor the alert log for the user. After the initial entry alert, no further entry alerts should appear until after an exit event has occurred.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Alerts are not generated for vehicles not on an active trip

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A vehicle 'MH-04-XY-9876' has a status of 'Available' (not on an 'In-Transit' trip).

### 3.4.5 When

The vehicle's GPS device sends a location update from within the 'Customer Warehouse A' geofence.

### 3.4.6 Then

The system shall not generate a trip-related geofence alert.

### 3.4.7 Validation Notes

Check the system logs and user-facing alerts to confirm no notification was generated for this event.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

System handles boundary hovering without generating alert spam

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A vehicle is driving along the boundary of a geofence, causing its GPS coordinates to fluctuate between just inside and just outside.

### 3.5.5 When

The system detects an 'Exit' event immediately followed by an 'Entry' event within a short, configurable time threshold (e.g., 60 seconds).

### 3.5.6 Then

The system should suppress the second alert to prevent alert fatigue.

### 3.5.7 Validation Notes

Simulate rapid entry/exit GPS pings. Verify that only the first significant state change (e.g., the initial exit) generates an alert within the debounce period.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Alerts Panel on the main dashboard (as defined in US-065)

## 4.2.0 User Interactions

- Alerts should be dismissible or markable as 'read'.
- Clicking on a geofence alert should ideally navigate the user to the map view, centered on the vehicle and the relevant geofence.

## 4.3.0 Display Requirements

- Alert text must clearly state: Vehicle Number, Geofence Name, Event Type (Entered/Exited), and Timestamp.
- Geofence alerts should have a distinct icon (e.g., a map pin) to differentiate them from other alert types.

## 4.4.0 Accessibility Needs

- Alert notifications must use appropriate ARIA roles to be accessible to screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-GEO-01', 'rule_description': "Geofence alerts are only triggered for vehicles with a trip status of 'In-Transit'.", 'enforcement_point': 'GPS Ingestion Microservice, during event processing.', 'violation_handling': 'GPS data points for non-eligible vehicles are processed for location updates but ignored by the geofence event logic.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-021

#### 6.1.1.2 Dependency Reason

The system must allow creation and management of geofences before alerts can be generated against them.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-029

#### 6.1.2.2 Dependency Reason

The underlying real-time GPS data ingestion pipeline must be operational to provide the location data needed for geofence checks.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-065

#### 6.1.3.2 Dependency Reason

A UI component for displaying and managing alerts on the dashboard must exist to make these alerts visible to the user.

## 6.2.0.0 Technical Dependencies

- GPS Ingestion Microservice (FastAPI)
- Amazon MQ for RabbitMQ (for asynchronous alert notification)
- Amazon ElastiCache for Redis (for efficient vehicle state management)

## 6.3.0.0 Data Dependencies

- Real-time GPS data stream from the third-party provider.
- Geofence definitions (polygon coordinates) stored in the database.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The geofence check (point-in-polygon calculation) must add less than 50ms of latency to the processing of each GPS data point within the microservice.
- End-to-end alert latency (from GPS event to UI notification) should be under 60 seconds, consistent with REQ-FNC-003.

## 7.2.0.0 Security

- Access to view geofence alerts must be restricted by role (Dispatch Manager, Admin) as per the system's RBAC model.

## 7.3.0.0 Usability

- Alert messages must be clear, concise, and immediately understandable.
- The system must prevent alert spam from boundary hovering.

## 7.4.0.0 Accessibility

- WCAG 2.1 Level AA standards apply to the display of alerts in the UI.

## 7.5.0.0 Compatibility

- Alerts must display correctly on all supported browsers and mobile-responsive views.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires implementation of an efficient point-in-polygon algorithm.
- Needs robust state management (e.g., using Redis) to track the current inside/outside status of every active vehicle for every relevant geofence.
- Involves asynchronous communication between the GPS microservice and the Odoo monolith via a message queue.
- Logic for debouncing alerts to prevent spam adds complexity.

## 8.3.0.0 Technical Risks

- The geofence checking logic could become a performance bottleneck if not implemented efficiently, especially as the number of vehicles and geofences grows.
- Potential for race conditions in state management if not handled carefully.

## 8.4.0.0 Integration Points

- GPS Ingestion Microservice: This is where the core detection logic will reside.
- RabbitMQ: A new topic/exchange will be needed for geofence events.
- Odoo Monolith: A new consumer is required to process geofence event messages and create Odoo notifications.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Simulate a vehicle path that clearly enters a geofence.
- Simulate a vehicle path that clearly exits a geofence.
- Simulate a vehicle path that passes near but never enters a geofence.
- Simulate a vehicle path that hovers on the boundary of a geofence.
- Test with vehicles that are not on an active trip to ensure no alerts are generated.

## 9.3.0.0 Test Data Needs

- A set of defined geofences with varying shapes (simple square, complex polygon).
- Scripted sequences of GPS coordinates representing different vehicle paths.
- Test users with 'Dispatch Manager' and other roles to verify access control.

## 9.4.0.0 Testing Tools

- Pytest for unit tests of the geofence algorithm and state logic.
- A script to publish mock GPS data to the ingestion endpoint or message queue for integration testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests for the point-in-polygon logic and state transitions are implemented with >80% coverage and passing
- Integration testing of the microservice -> message queue -> Odoo consumer flow is completed successfully
- User interface for alerts is reviewed and approved by the product owner
- Performance testing confirms that the geofence check does not degrade the GPS ingestion pipeline performance
- Security requirements for alert visibility are validated
- Documentation for the geofence event and alert mechanism is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a cornerstone of the real-time tracking feature set.
- Requires coordinated work between backend developers working on the microservice and the Odoo monolith.
- Ensure prerequisite stories are completed in a prior sprint.

## 11.4.0.0 Release Impact

- Enables a key monitoring and alerting capability, significantly increasing the value of the GPS tracking module.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-029 |
| Elaboration Date | 2025-01-18 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager views the real-time location of v... |
| As A User Story | As a Dispatch Manager, I want to see a real-time m... |
| User Persona | Dispatch Manager |
| Business Value | Provides real-time operational awareness, enabling... |
| Functional Area | Trip Management & Tracking |
| Story Theme | Real-Time Operations Monitoring |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Map displays all 'In-Transit' vehicles upon loading

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a Dispatch Manager and there are multiple trips with the status 'In-Transit', each with a unique vehicle assigned and recent GPS data

### 3.1.5 When

I navigate to the 'Live Map' view

### 3.1.6 Then

The map loads and displays a distinct marker for each 'In-Transit' vehicle at its last known location, and the map view is automatically zoomed and centered to encompass all markers.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Clicking a vehicle marker displays trip details

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am viewing the 'Live Map' with active vehicle markers

### 3.2.5 When

I click on a specific vehicle marker

### 3.2.6 Then

An info-window or pop-up appears, displaying the following details: Trip ID, Vehicle Number, Driver Name, and Destination.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Vehicle marker position updates in near real-time

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am viewing the 'Live Map' and an 'In-Transit' vehicle is moving

### 3.3.5 When

The system receives a new GPS location update for that vehicle

### 3.3.6 Then

The corresponding marker on the map smoothly moves to the new location without a full page reload, meeting the maximum 60-second latency requirement from device to UI.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Map view when no vehicles are in transit

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am logged in as a Dispatch Manager and there are no trips with the status 'In-Transit'

### 3.4.5 When

I navigate to the 'Live Map' view

### 3.4.6 Then

The map loads correctly, and a user-friendly message is displayed over the map, such as 'No vehicles are currently in transit.'

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Vehicle marker is removed when trip status changes from 'In-Transit'

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am viewing the 'Live Map' with a marker for vehicle 'MH-01-AB-1234'

### 3.5.5 When

The trip associated with that vehicle is updated to 'Delivered', 'On Hold', or 'Canceled'

### 3.5.6 Then

The marker for 'MH-01-AB-1234' is automatically removed from the map.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

New vehicle marker appears when a trip starts

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

I am viewing the 'Live Map'

### 3.6.5 When

A driver starts a trip, changing its status from 'Assigned' to 'In-Transit'

### 3.6.6 Then

A new marker for the corresponding vehicle appears on the map at its current location.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Handling of stale GPS data

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

A vehicle is 'In-Transit', but the system has not received a GPS update for it in over 15 minutes

### 3.7.5 When

I view the 'Live Map'

### 3.7.6 Then

The marker for that vehicle is visually distinct (e.g., grayed out, different icon) to indicate stale data, and its info-window displays the timestamp of the last received update.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- An interactive map canvas (e.g., using Odoo Map view with OpenStreetMap or another provider).
- Custom vehicle markers/icons.
- Info-windows for displaying trip details on marker click.
- Zoom in/out controls.
- A message overlay for the 'no vehicles in transit' case.

## 4.2.0 User Interactions

- User can pan the map by clicking and dragging.
- User can zoom using the scroll wheel or on-screen controls.
- Clicking a marker opens an info-window; clicking the map or an 'x' icon closes it.

## 4.3.0 Display Requirements

- The map must be responsive and usable on mobile devices as per REQ-INT-001.
- Vehicle markers must be clearly distinguishable, especially if they are close together.

## 4.4.0 Accessibility Needs

- Map controls must be keyboard-accessible.
- Information in the info-window must be readable by screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-MAP-001', 'rule_description': "Only vehicles assigned to trips with the status 'In-Transit' shall be displayed on the map.", 'enforcement_point': 'Data query for the map view.', 'violation_handling': 'Vehicles in other states are filtered out and not sent to the frontend.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-027

#### 6.1.1.2 Dependency Reason

A trip must be created and have a vehicle assigned to it before it can be tracked.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-049

#### 6.1.2.2 Dependency Reason

A driver must be able to change a trip's status to 'In-Transit' to make it appear on the map.

## 6.2.0.0 Technical Dependencies

- Completion of the GPS data ingestion pipeline (FastAPI microservice, RabbitMQ message queue, and Odoo consumer job) as specified in REQ-ARC-001 and REQ-INT-003.
- A data model within Odoo (likely an extension of the Vehicle Master) to store the last known latitude, longitude, and timestamp for each vehicle.

## 6.3.0.0 Data Dependencies

- A live, reliable data feed from the third-party GPS provider's API.

## 6.4.0.0 External Dependencies

- Availability and stability of the third-party GPS Provider API.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- End-to-end latency for a GPS data point (from device to UI update) must be under 10 seconds, with a maximum of 60 seconds as per REQ-FNC-003.
- The map view must load with all markers within 3 seconds on a standard broadband connection (LCP as per REQ-NFR-001).

## 7.2.0.0 Security

- Access to the map view must be restricted to authorized roles (Dispatch Manager, Admin) as per REQ-FNC-001.
- API endpoints serving location data to the frontend must be secured and only accessible to authenticated users.

## 7.3.0.0 Usability

- The map should be intuitive to navigate, with standard pan and zoom controls.
- The info-window should present information clearly and concisely.

## 7.4.0.0 Accessibility

- The feature should strive to meet WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0.0 Compatibility

- The map view must function correctly on all modern web browsers supported by Odoo 18 and be fully responsive on screen sizes from 360px width upwards.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

High

## 8.2.0.0 Complexity Factors

- The primary complexity is in ensuring the real-time data pipeline is robust, scalable, and low-latency.
- Frontend complexity involves efficiently handling real-time data updates on the map without performance degradation, potentially requiring websockets or efficient polling.
- Integrating a third-party mapping library into an Odoo OWL component requires careful implementation.

## 8.3.0.0 Technical Risks

- The GPS data ingestion pipeline could become a bottleneck or point of failure.
- The third-party GPS provider API may have reliability issues, rate limits, or breaking changes.
- Performance degradation on the map UI if a very large number of vehicles are in transit simultaneously.

## 8.4.0.0 Integration Points

- Odoo Backend <-> RabbitMQ (consuming location data).
- Odoo Frontend (OWL) <-> Odoo Backend (API to fetch initial and updated locations).
- GPS Ingestion Microservice <-> Third-Party GPS Provider API.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Verify all acceptance criteria.
- Simulate a high volume of GPS updates to test the performance of the data pipeline and frontend rendering.
- Simulate API failure from the GPS provider to test error handling and the 'stale data' indicator.
- Test the map view on various screen sizes, including mobile phones and tablets.

## 9.3.0.0 Test Data Needs

- A set of test vehicles and trips in various statuses ('Planned', 'Assigned', 'In-Transit', 'Delivered').
- A script or tool to mock the GPS provider API and send simulated location data to the ingestion microservice.

## 9.4.0.0 Testing Tools

- Pytest for backend unit/integration tests.
- A mock server or API simulation tool (e.g., Mock-Server, Postman) for the GPS provider.
- A frontend testing framework like Cypress or Selenium for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for new logic with >= 80% coverage
- Integration testing of the full data pipeline (mock GPS to Odoo DB) completed successfully
- E2E tests for map loading, marker display, and updates are passing
- User interface reviewed and approved by the product owner
- Performance requirements for data latency and page load are verified in staging
- Security requirements for data access are validated
- Documentation for the map view feature is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is critically dependent on the completion of the backend GPS data ingestion pipeline. It cannot be started until that technical dependency is resolved.
- Requires a developer with both Odoo backend and OWL frontend skills, particularly with integrating JavaScript libraries.

## 11.4.0.0 Release Impact

- This is a cornerstone feature for the operational value proposition of the TMS. Its inclusion is critical for the Phase 2 rollout (Finance & Tracking).


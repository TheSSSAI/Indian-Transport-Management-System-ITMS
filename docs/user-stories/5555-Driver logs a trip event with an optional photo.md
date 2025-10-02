# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-050 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver logs a trip event with an optional photo |
| As A User Story | As a Driver, I want to log specific events for my ... |
| User Persona | Driver, accessing the system via a mobile-friendly... |
| Business Value | Provides real-time operational visibility into on-... |
| Functional Area | Trip Management |
| Story Theme | Driver Portal & On-Trip Activities |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Driver logs a non-critical event without a photo

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Driver logged into the mobile web portal and I have an active trip with the status 'In-Transit'

### 3.1.5 When

I navigate to the 'Log Event' screen for my active trip, select the event type 'Fueling', enter the text 'Filled 200 liters', and submit the form without attaching a photo

### 3.1.6 Then

A new event record is created and associated with my trip, the event details (type, text, timestamp, driver) are saved correctly, the trip status remains 'In-Transit', and no high-priority alert is generated for managers.

### 3.1.7 Validation Notes

Verify in the backend that a `tms.trip.event` record is created with the correct data and relationships. Check the trip's chatter/log to see the new event. Confirm the trip's status has not changed.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Driver logs a critical event with a photo, triggering a status change and alert

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am a Driver logged into the mobile web portal and I have an active trip with the status 'In-Transit'

### 3.2.5 When

I select 'Log Event', choose the event type 'Accident', enter 'Minor collision, vehicle is not drivable', attach a photo of the damage, and submit the form

### 3.2.6 Then

A new event record is created with all details and the photo, the trip's status is automatically changed to 'On Hold', and a high-priority alert appears on the Admin/Manager dashboard.

### 3.2.7 Validation Notes

Verify the trip status is updated to 'On Hold'. Verify the photo is successfully uploaded to S3 and linked to the event record. Log in as a Manager and confirm a new, visible alert for this event is present on the dashboard (implements REQ-FNC-008 and BR-005).

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempting to log an event without an active trip

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

I am a Driver logged into the mobile web portal and I do not have any trips with the status 'In-Transit'

### 3.3.5 When

I view my list of trips

### 3.3.6 Then

The option or button to 'Log Event' is not available or is disabled for all trips not in 'In-Transit' status.

### 3.3.7 Validation Notes

Check the UI to ensure the action is not presented to the user for trips in 'Planned', 'Assigned', 'Delivered', etc. statuses.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Form submission fails due to missing event type

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am on the 'Log Event' screen for my active trip

### 3.4.5 When

I enter a description but do not select an event type from the predefined list, and I press submit

### 3.4.6 Then

The form is not submitted, a user-friendly validation message like 'Please select an event type' is displayed, and the data I entered is preserved in the form.

### 3.4.7 Validation Notes

Verify client-side or server-side validation prevents form submission and displays the correct error message.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Photo upload exceeds size or format limits

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am on the 'Log Event' screen for my active trip

### 3.5.5 When

I attempt to attach a file that is larger than 5MB or is not a JPG, PNG, or PDF

### 3.5.6 Then

The file is rejected, and a clear error message is displayed to me (e.g., 'File is too large. Max 5MB.' or 'Invalid file type. Please use JPG, PNG, or PDF.').

### 3.5.7 Validation Notes

Test with oversized files and unsupported file types (e.g., .zip, .mov) to confirm validation logic.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Log Event' button on the active trip details view in the driver portal.
- A simple form with a dropdown or radio buttons for 'Event Type'.
- A multi-line text area for 'Description/Notes'.
- A file input button for 'Attach Photo' that accesses the device camera or gallery.
- A 'Submit' button.

## 4.2.0 User Interactions

- The interface must be designed for mobile-first use with large, easily tappable controls.
- Upon successful submission, a confirmation message (e.g., a toast notification) should appear briefly.
- If the photo upload is in progress, a visual indicator (e.g., a spinner) should be shown.

## 4.3.0 Display Requirements

- The list of event types must be populated from a predefined, centrally managed list: 'Accident', 'Repair', 'Government Stoppage', 'Fueling', 'Trip Start' (as per REQ-FNC-008).
- The trip's event history should be displayed in chronological order.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- Buttons must have clear, descriptive text.
- The feature must be operable using touch controls on a mobile device.

# 5.0.0 Business Rules

- {'rule_id': 'BR-005', 'rule_description': "Logging of critical events ('Accident', 'Repair', 'Government Stoppage') by a driver shall automatically change the trip status to 'On Hold'.", 'enforcement_point': 'Server-side, upon submission of a new trip event.', 'violation_handling': 'N/A - This is a system-enforced process.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-047

#### 6.1.1.2 Dependency Reason

Driver must be able to view their assigned trips to select the one to log an event against.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-049

#### 6.1.2.2 Dependency Reason

A trip must be started and in 'In-Transit' status before an event can be logged.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-065

#### 6.1.3.2 Dependency Reason

The manager's dashboard and alert panel must exist to display the high-priority alerts generated by this story.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-077

#### 6.1.4.2 Dependency Reason

This story is the primary implementation of the system rule defined in US-077.

## 6.2.0.0 Technical Dependencies

- Odoo backend model for storing trip events (`tms.trip.event`).
- File storage configured to use Amazon S3 for photo attachments (as per REQ-DEP-001).
- Odoo's notification/alerting system (e.g., Odoo Bus) to push real-time alerts to the manager dashboard.

## 6.3.0.0 Data Dependencies

- A predefined, configurable list of event types and their classification (critical vs. non-critical).

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The event submission, including photo upload on a stable 4G connection, should complete within 5 seconds.
- The automatic status change and alert generation should be processed by the backend in under 500ms.

## 7.2.0.0 Security

- Drivers can only log events for trips explicitly assigned to them.
- File uploads must be scanned for malware.
- All data transmission must be over HTTPS.

## 7.3.0.0 Usability

- The process of logging an event should require no more than 4 taps/clicks on the happy path.

## 7.4.0.0 Accessibility

- The feature should adhere to WCAG 2.1 Level AA standards where applicable for web content.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of mobile Chrome (Android) and Safari (iOS).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires a new Odoo model and associated views.
- Frontend development for the driver portal using OWL.
- Backend business logic to conditionally change trip status and trigger alerts.
- Integration with S3 for file storage.
- Real-time notification mechanism for alerts.

## 8.3.0.0 Technical Risks

- Handling network interruptions during file uploads from mobile devices gracefully.
- Ensuring the real-time alert mechanism is reliable and does not impact overall system performance.

## 8.4.0.0 Integration Points

- Odoo's `tms.trip` model.
- Odoo's user notification system.
- Amazon S3 for file storage.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- Log a non-critical event and verify trip status is unchanged.
- Log each type of critical event ('Accident', 'Repair', 'Government Stoppage') and verify trip status changes to 'On Hold' and an alert is generated.
- Test photo upload with valid and invalid file types/sizes.
- Test on a device with a slow network connection.
- Verify that a manager sees the alert immediately after a driver logs a critical event.

## 9.3.0.0 Test Data Needs

- Test users for 'Driver' and 'Dispatch Manager' roles.
- A trip assigned to the test driver in 'In-Transit' status.
- Sample image files of various sizes and formats.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Browser developer tools for mobile emulation.
- A physical mobile device for final validation.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the new business logic with >80% coverage
- Integration testing of the form submission, status change, and alert generation is completed successfully
- User interface reviewed and approved for mobile usability
- Performance requirements for submission time are verified
- Security requirements, especially for file uploads and data access, are validated
- Documentation for the `tms.trip.event` model is created
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- Requires both backend (Odoo model, controller logic) and frontend (OWL portal UI) development effort.
- The alert mechanism (US-065) should ideally be developed in the same or a preceding sprint to allow for full E2E testing.

## 11.4.0.0 Release Impact

This is a key feature for the Driver Portal and is critical for achieving the project's goal of improved operational visibility. It should be included in the initial release.


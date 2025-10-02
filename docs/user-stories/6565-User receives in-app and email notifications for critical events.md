# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-060 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | User receives in-app and email notifications for c... |
| As A User Story | As a System User (e.g., Dispatch Manager, Finance ... |
| User Persona | Any authenticated system user (Admin, Dispatch Man... |
| Business Value | Improves operational responsiveness by proactively... |
| Functional Area | System-Wide Services |
| Story Theme | User Communication and Alerting |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Manager receives notification for a critical trip event

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Dispatch Manager is logged into the TMS

### 3.1.5 When

A driver assigned to an 'In-Transit' trip logs a critical event (e.g., 'Accident') via the driver portal

### 3.1.6 Then



```
The Dispatch Manager's in-app notification icon immediately shows an unread count badge.
AND clicking the icon reveals a new notification with a summary like 'Trip T-00123: Critical Event 'Accident' logged by Driver John Doe'.
AND the manager receives an email with a similar subject and body, containing a direct link to the trip's record.
AND clicking the in-app notification navigates the manager to the trip's form view.
```

### 3.1.7 Validation Notes

Verify the notification badge appears in real-time using Odoo's bus service. Check the test email inbox for the correctly formatted email. Confirm the deep link in both notifications works.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin receives notification for an upcoming document expiry

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A vehicle's insurance document has an expiry date 30 days from today

### 3.2.5 When

The daily scheduled job for checking document expiries runs

### 3.2.6 Then



```
The Admin user receives an in-app notification and an email stating 'Vehicle MH01AB1234: Insurance is expiring on [Expiry Date]'.
AND the notification links directly to the vehicle's record.
```

### 3.2.7 Validation Notes

Manually trigger the scheduled job and verify that notifications are generated for all documents meeting the 30, 15, and 7-day criteria. Check that no duplicate notifications are sent for the same document on the same day.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Driver receives notification for a canceled trip

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A driver is assigned to a trip with status 'Assigned'

### 3.3.5 When

A Dispatch Manager cancels that trip

### 3.3.6 Then

The assigned driver receives an in-app notification and an email stating 'Trip T-00456 has been canceled. Reason: [Cancellation Reason]'.

### 3.3.7 Validation Notes

Log in as a driver on a separate session/device to confirm the notification is received promptly after the manager cancels the trip.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

User interacts with the in-app notification center

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

A user has several unread notifications

### 3.4.5 When

The user clicks on the notification icon to open the notification panel

### 3.4.6 Then



```
The panel displays a list of recent notifications, with unread ones highlighted.
AND after the panel is viewed for a few seconds or closed, the unread count badge on the icon disappears.
AND the notifications in the panel are now marked as 'read'.
```

### 3.4.7 Validation Notes

Verify the state change from unread to read is correctly persisted and the UI updates accordingly.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

System handles email service failure

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

The external SMTP email service is unavailable

### 3.5.5 When

A notifiable event occurs (e.g., a critical trip event is logged)

### 3.5.6 Then



```
The in-app notification is still delivered successfully to the user.
AND the system logs an error indicating the email delivery failure.
AND the failed email job is placed in a retry queue to be attempted later.
```

### 3.5.7 Validation Notes

Simulate SMTP failure in a test environment. Verify the in-app notification works and check system logs for the specific error message and evidence of a queued retry job.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A persistent notification icon (e.g., a bell) in the main application header.
- A numerical badge on the icon to indicate the count of unread notifications.
- A dropdown/panel that displays a list of recent notifications upon clicking the icon.

## 4.2.0 User Interactions

- Clicking the icon toggles the visibility of the notification panel.
- Clicking a specific notification in the panel navigates the user to the relevant record (e.g., Trip, Vehicle).
- Viewing the panel marks the displayed notifications as 'read' and clears the unread count badge.

## 4.3.0 Display Requirements

- Each notification item must display a summary of the event, the source record (e.g., Trip ID), and a relative timestamp (e.g., '5 minutes ago').
- Unread notifications should be visually distinct from read ones.

## 4.4.0 Accessibility Needs

- The notification icon and panel must be fully keyboard accessible.
- The unread count must be announced by screen readers.
- WCAG 2.1 Level AA standards must be met.

# 5.0.0 Business Rules

*No items available*

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-050

#### 6.1.1.2 Dependency Reason

The ability to log trip events is required to trigger critical event notifications.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-009

#### 6.1.2.2 Dependency Reason

The ability to store documents with expiry dates is required to trigger expiry notifications.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-031

#### 6.1.3.2 Dependency Reason

The ability to cancel a trip is required to trigger cancellation notifications for drivers.

## 6.2.0.0 Technical Dependencies

- Odoo's core mail module (`mail.thread`) for creating notification records.
- Odoo's web bus (`bus.bus`) for real-time UI updates.
- A configured SMTP service for email delivery.
- RabbitMQ message queue for asynchronous notification processing, as per REQ-ARC-001.

## 6.3.0.0 Data Dependencies

- User records (`res.users`) must have valid and verified email addresses.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Notification generation and sending must be processed asynchronously to not block the user action that triggered the event.
- The in-app notification badge should update in near real-time (under 2 seconds latency).

## 7.2.0.0 Security

- A user must only receive notifications for data and records they are authorized to view, respecting all `ir.rule` configurations.
- Links within emails must point to pages that require authentication.

## 7.3.0.0 Usability

- Notification messages must be clear, concise, and immediately understandable.
- It should be easy for the user to navigate from a notification to the context of the event.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The notification UI must function correctly on all supported modern web browsers (Chrome, Firefox, Safari, Edge) and mobile-responsive views.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creating a centralized, extensible notification service.
- Involves both backend (event listeners, async jobs, email templating) and frontend (OWL component for the notification center) development.
- Integration with Odoo's bus for real-time updates can be complex.
- Requires defining a clear data model for notifications and their states (unread, read, archived).

## 8.3.0.0 Technical Risks

- Potential for performance issues if the real-time bus is overloaded.
- Ensuring the reliability of the asynchronous job queue (RabbitMQ) and handling failed jobs gracefully.

## 8.4.0.0 Integration Points

- Odoo's ORM `create`/`write` methods for triggering notifications on data changes.
- Odoo's scheduled actions for time-based triggers (e.g., document expiry).
- External SMTP gateway for email dispatch.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- Verify notification delivery for each defined event type (critical trip event, document expiry, trip cancellation).
- Test the complete flow from event trigger to in-app display and email receipt.
- Test the UI interactions: opening the panel, clicking a notification, marking as read.
- Test failure scenarios, such as the SMTP server being down.
- Verify role-based routing of notifications (e.g., a driver's event notifies a manager, not another driver).

## 9.3.0.0 Test Data Needs

- Users for each role with valid email addresses in a test mail server.
- Vehicles with documents set to expire at 30, 15, 7, and 1 day(s) in the future.
- Active trips that can be used to log events or be canceled.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- A mock SMTP server (e.g., MailHog) to capture and inspect outgoing emails.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the notification service and trigger logic, with >80% coverage
- Integration testing completed for the async job processing and email generation
- The OWL component for the notification center is implemented, reviewed, and approved
- Performance requirements for asynchronous processing are verified
- Security requirements for role-based access are validated
- Developer documentation on how to add new notification types is created
- Story deployed and verified in the staging environment by QA

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story for user alerting. It should be completed early in the project timeline as other features depend on it.
- Requires both backend and frontend development effort, which should be coordinated.

## 11.4.0.0 Release Impact

- Enables a core communication mechanism for the entire application. Subsequent features related to alerts and user feedback will build upon this framework.


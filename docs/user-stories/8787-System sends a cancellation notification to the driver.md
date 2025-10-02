# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-082 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System sends a cancellation notification to the dr... |
| As A User Story | As a Driver, I want to receive an immediate notifi... |
| User Persona | Driver |
| Business Value | Prevents wasted fuel, time, and resources on trips... |
| Functional Area | Trip Management & Notifications |
| Story Theme | Operational Communications |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful notification on trip cancellation

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A trip is in 'Assigned' status and is assigned to a specific driver with a valid email address and system access

### 3.1.5 When

A user with 'Dispatch Manager' or 'Admin' permissions changes the trip's status to 'Canceled'

### 3.1.6 Then

The assigned driver immediately receives a notification via the Odoo internal notification system (bell icon).

### 3.1.7 And

The notification content clearly states the trip ID, source, and destination, and that it has been canceled (e.g., 'Trip T00123 from Mumbai to Pune has been canceled.').

### 3.1.8 Validation Notes

Verify the in-app notification appears for the driver user. Check the email logs or a test inbox (e.g., MailHog) to confirm the email was sent and its content is correct.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Trip canceled with no driver assigned

### 3.2.3 Scenario Type

Edge_Case

### 3.2.4 Given

A trip is in 'Planned' status and has no driver assigned

### 3.2.5 When

A user with 'Dispatch Manager' or 'Admin' permissions changes the trip's status to 'Canceled'

### 3.2.6 Then

The system successfully cancels the trip.

### 3.2.7 And

No driver notification is triggered and no error is generated.

### 3.2.8 Validation Notes

Perform the cancellation and check system logs to ensure no notification attempt was made and no errors were thrown.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Trip canceled for a driver with no valid email

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A trip is assigned to a driver whose user profile has a missing or invalidly formatted email address

### 3.3.5 When

A user with 'Dispatch Manager' or 'Admin' permissions cancels the trip

### 3.3.6 Then

The driver still receives the Odoo internal notification (bell icon).

### 3.3.7 And

The system logs the email delivery failure for administrative review, without blocking the cancellation process.

### 3.3.8 Validation Notes

Set up a driver user with a blank or malformed email. Cancel their trip. Verify the in-app notification is received and check the server logs for a logged email failure.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Notification content is clear and informative

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A trip from 'Mumbai Port' to 'Delhi Warehouse' with ID 'TRIP-2025-001' is assigned to a driver

### 3.4.5 When

The trip is canceled

### 3.4.6 Then

The body of the notification (both in-app and email) contains the essential details: 'Trip TRIP-2025-001 from Mumbai Port to Delhi Warehouse has been canceled.'

### 3.4.7 Validation Notes

Review the content of the generated notifications to ensure they are user-friendly and contain the necessary information.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- This story does not introduce new UI elements but utilizes the existing Odoo notification system (bell icon) and email templates.

## 4.2.0 User Interactions

- The driver will see a notification indicator on the bell icon.
- Clicking the notification should ideally navigate the driver to the read-only view of the canceled trip for context.

## 4.3.0 Display Requirements

- The notification message must be clear and concise.
- The email notification must be mobile-responsive.

## 4.4.0 Accessibility Needs

- Email notifications must use semantic HTML to be compatible with screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-NOTIFY-01', 'rule_description': 'A cancellation notification must be sent if and only if a trip has a driver assigned at the moment of cancellation.', 'enforcement_point': "On state change of a trip record to 'Canceled'.", 'violation_handling': 'If a driver is assigned, failure to send a notification should be logged as a system error.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-031

#### 6.1.1.2 Dependency Reason

The functionality to cancel a trip is the trigger for this notification.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

The functionality to assign a driver to a trip must exist to have a recipient for the notification.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-060

#### 6.1.3.2 Dependency Reason

The underlying system framework for sending in-app and email notifications must be in place.

## 6.2.0.0 Technical Dependencies

- A correctly configured Odoo instance with a functional mail server (SMTP) for sending emails.
- Odoo's internal messaging bus (`mail.thread`, `mail.activity`) must be operational.

## 6.3.0.0 Data Dependencies

- Driver records must have an associated `res.users` record to receive in-app notifications.
- Driver records must have a valid email address for email notifications.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The notification must be triggered and dispatched to the message queue/mail server within 60 seconds of the cancellation action.

## 7.2.0.0 Security

- The notification must only be sent to the specific driver assigned to the canceled trip.
- Notification content must not include sensitive financial data (e.g., trip revenue, customer rates).

## 7.3.0.0 Usability

- The notification message must be easily understandable by the driver.

## 7.4.0.0 Accessibility

- As per REQ-INT-001, the system strives for WCAG 2.1 Level AA. Email templates should adhere to this where applicable.

## 7.5.0.0 Compatibility

- Email notifications must render correctly on major mobile and web email clients.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Requires overriding the `write` method of the trip model to detect the status change.
- Logic to fetch the assigned driver's user and email is straightforward.
- Leverages existing Odoo notification and mail template functionalities.

## 8.3.0.0 Technical Risks

- Misconfiguration of the mail server could lead to silent email failures. Robust logging is required.
- Potential for race conditions if trip assignment and cancellation happen nearly simultaneously, though unlikely.

## 8.4.0.0 Integration Points

- Odoo Mail Module (for email templates and sending)
- Odoo Bus Module (for live in-app notifications)

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify notification is sent (in-app and email) when a trip with an assigned driver is canceled.
- Verify no notification is sent when a trip without a driver is canceled.
- Verify in-app notification is sent but an error is logged if the driver's email is invalid.
- Verify the content of both notification types is correct and contains trip details.

## 9.3.0.0 Test Data Needs

- A user with 'Dispatch Manager' role.
- A user with 'Driver' role, with a valid email address.
- A user with 'Driver' role, with an invalid or missing email address.
- At least one trip record that can be assigned and then canceled.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- A local mail server like MailHog for integration testing of emails.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the notification trigger logic, covering all scenarios, and passing
- Integration testing completed successfully in a staging environment with a test mail server
- User interface (email template) reviewed and approved for clarity and mobile responsiveness
- Performance requirement (notification within 60s) verified
- Security requirements (correct recipient) validated
- Documentation for the notification event is updated if applicable
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story provides critical operational feedback and should be prioritized soon after the core trip cancellation feature is complete.
- Ensure prerequisite stories (US-031, US-027, US-060) are completed in a prior or the same sprint.

## 11.4.0.0 Release Impact

Improves the core user experience for drivers and reduces operational inefficiencies. Key feature for a successful rollout of the trip management module.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-078 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System generates automated alerts for upcoming veh... |
| As A User Story | As an Admin or Dispatch Manager, I want the system... |
| User Persona | Admin, Dispatch Manager |
| Business Value | Mitigates legal and financial risks associated wit... |
| Functional Area | Alerts & Notifications |
| Story Theme | Fleet Compliance Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

30-Day Expiry Alert Generation

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

An 'Active' vehicle record exists with an attached document (e.g., 'Insurance') that has an expiry date exactly 30 days from the current date

### 3.1.5 When

The daily scheduled job for checking document expiries runs

### 3.1.6 Then

An alert is generated and delivered to users with 'Admin' or 'Dispatch Manager' roles via the Odoo internal notification system (bell icon) and email.

### 3.1.7 And

The alert is displayed in the 'Alerts Panel' on the main dashboard.

### 3.1.8 Validation Notes

Verify by setting a document's expiry date to T+30 days, manually triggering the cron job, and checking for the notification in the UI, dashboard, and email client.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

15-Day and 7-Day Expiry Alerts

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An 'Active' vehicle record has a document with an expiry date exactly 15 days (or 7 days) from the current date

### 3.2.5 When

The daily scheduled job runs

### 3.2.6 Then

A corresponding 15-day (or 7-day) alert is generated and delivered through all configured channels.

### 3.2.7 Validation Notes

Test each timeframe (15 days, 7 days) independently to ensure alerts are triggered at the correct milestone.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

No Alert Generated Outside Defined Windows

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

An 'Active' vehicle has a document with an expiry date that is not 30, 15, or 7 days away (e.g., 25 days away)

### 3.3.5 When

The daily scheduled job runs

### 3.3.6 Then

No new expiry alert is generated for that specific document on that day.

### 3.3.7 Validation Notes

Set a document's expiry to a date like T+29 days and confirm that no alert is created by the daily job.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Alerts for Already Expired Documents

### 3.4.3 Scenario Type

Alternative_Flow

### 3.4.4 Given

An 'Active' vehicle has a document with an expiry date in the past (e.g., yesterday)

### 3.4.5 When

The daily scheduled job runs

### 3.4.6 Then

A high-priority 'EXPIRED' alert is generated and delivered.

### 3.4.7 And

This 'EXPIRED' alert is visually distinct (e.g., red color, warning icon) in the dashboard's 'Alerts Panel' to indicate urgency.

### 3.4.8 Validation Notes

Set a document's expiry date to T-1 day and verify the generation of a distinct, high-priority alert.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Inactive Vehicles are Ignored

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A vehicle is marked as 'Inactive' in the system

### 3.5.5 And

It has a document that is due to expire in 30 days

### 3.5.6 When

The daily scheduled job runs

### 3.5.7 Then

The system does not generate any expiry alerts for this inactive vehicle's documents.

### 3.5.8 Validation Notes

Create an inactive vehicle with a document expiring in 30 days and confirm no alert is generated.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Alert Idempotency

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

A 30-day alert has already been generated and sent for a specific document

### 3.6.5 And

The document's expiry date has not been updated

### 3.6.6 When

The daily scheduled job runs on the following day (when the document is 29 days from expiry)

### 3.6.7 Then

The system does not re-send the 30-day alert.

### 3.6.8 Validation Notes

Trigger the job, confirm the 30-day alert is sent. Trigger it again the next day (after advancing the system clock or test date) and confirm a duplicate alert is not sent.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- An 'Alerts Panel' widget on the Admin/Manager dashboard (as defined in REQ-REP-002).
- Standard Odoo notification pop-ups (bell icon).
- Formatted email template for notifications.

## 4.2.0 User Interactions

- Alerts displayed in the dashboard panel should be clickable.
- Clicking an alert should navigate the user directly to the corresponding vehicle's form view to take action.

## 4.3.0 Display Requirements

- Alert text must contain: Vehicle Number, Document Type, and Expiry Date.
- Expired alerts must be visually highlighted to differentiate them from upcoming expiry warnings.

## 4.4.0 Accessibility Needs

- Color indicators for alert severity (e.g., red for expired) must be accompanied by text or icons to be accessible for color-blind users.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-ALERT-01

### 5.1.2 Rule Description

Alerts are triggered at 30, 15, and 7 days pre-expiry, and daily post-expiry.

### 5.1.3 Enforcement Point

During the execution of the daily scheduled job (`ir.cron`).

### 5.1.4 Violation Handling

N/A - System logic.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-ALERT-02

### 5.2.2 Rule Description

Expiry alerts are only generated for documents associated with 'Active' vehicles.

### 5.2.3 Enforcement Point

During the initial data query of the daily scheduled job.

### 5.2.4 Violation Handling

N/A - System logic.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

The Vehicle Master model must exist to associate documents with.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-008

#### 6.1.2.2 Dependency Reason

The 'Active'/'Inactive' status field on the vehicle model is required to filter which vehicles to check.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-009

#### 6.1.3.2 Dependency Reason

The functionality to attach documents with an 'Expiry Date' to a vehicle is a hard prerequisite.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-060

#### 6.1.4.2 Dependency Reason

The underlying notification framework (Odoo internal and email) must be in place to deliver the alerts.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-065

#### 6.1.5.2 Dependency Reason

The dashboard 'Alerts Panel' component must exist as a destination for displaying these alerts.

## 6.2.0.0 Technical Dependencies

- Odoo's scheduled action framework (`ir.cron`).
- Odoo's email templating and mail gateway configuration.
- Odoo's internal messaging/notification system.

## 6.3.0.0 Data Dependencies

- Requires vehicle records with attached documents and valid expiry dates to be present in the database for testing.

## 6.4.0.0 External Dependencies

- A correctly configured SMTP server/service for sending email notifications.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The scheduled job must be optimized to handle a large fleet (e.g., 1000+ vehicles) and complete its daily run within 10 minutes.
- The job should be scheduled during off-peak hours (e.g., 3:00 AM server time) to minimize impact on system performance.

## 7.2.0.0 Security

- Notifications should only be sent to users with appropriate roles (Admin, Dispatch Manager) who have permission to view the vehicle data.

## 7.3.0.0 Usability

- Alert messages must be concise, clear, and actionable.

## 7.4.0.0 Accessibility

- Compliant with WCAG 2.1 Level AA standards, especially regarding the use of color and text for alerts.

## 7.5.0.0 Compatibility

- Email notifications must render correctly in major modern email clients (Gmail, Outlook).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creating a robust and efficient Odoo scheduled action (`ir.cron`).
- Logic must be idempotent to prevent sending duplicate alerts for the same milestone.
- Integration with three different notification destinations (dashboard, internal Odoo bus, email).
- Requires careful date/time handling to avoid timezone-related issues.

## 8.3.0.0 Technical Risks

- A poorly optimized database query could cause performance degradation as the number of vehicles and documents grows.
- Failure in the email sending service could lead to missed notifications; the system should handle this gracefully (e.g., log the error but continue processing other notifications).

## 8.4.0.0 Integration Points

- Odoo `ir.cron` for scheduling.
- Odoo `mail.template` for email content.
- Odoo `mail.activity` or `bus.bus` for internal notifications.
- Custom dashboard component for displaying alerts.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify alert generation at exactly T+30, T+15, and T+7 days.
- Verify high-priority alert generation for T-1 day (expired).
- Verify no alert is generated for T+29 days.
- Verify no alert is generated for inactive vehicles.
- Verify alert delivery to all three channels: dashboard, internal notification, and email.
- Verify clicking the dashboard alert navigates to the correct vehicle record.

## 9.3.0.0 Test Data Needs

- A set of 'Active' vehicle records with documents expiring at T+30, T+15, T+7, T+29, T-1 days.
- An 'Inactive' vehicle record with a document expiring at T+30 days.
- User accounts with 'Admin' and 'Dispatch Manager' roles.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.
- Mailhog or a similar tool to capture and inspect outgoing emails during testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented with >80% coverage for the new logic and passing
- Integration testing of the cron job and notification delivery completed successfully
- User interface for alerts on the dashboard reviewed and approved
- Performance of the scheduled job has been tested against a representative data volume
- Security requirements validated (alerts only sent to authorized roles)
- Documentation for configuring the scheduled job and notification templates is created/updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is blocked by the completion of core vehicle master, document attachment, and dashboard/notification framework stories.
- Requires coordination with infrastructure/DevOps to ensure the email gateway is configured correctly in all environments.

## 11.4.0.0 Release Impact

- This is a key feature for ensuring fleet compliance and is critical for the 'Core Operations' phase of the rollout.


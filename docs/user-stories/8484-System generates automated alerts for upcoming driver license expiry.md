# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-079 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System generates automated alerts for upcoming dri... |
| As A User Story | As an Admin / Dispatch Manager, I want the system ... |
| User Persona | Admin, Dispatch Manager |
| Business Value | Mitigates significant legal and operational risk b... |
| Functional Area | Compliance & Alerts |
| Story Theme | Master Data Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

30-Day Expiry Alert Generation

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

An 'Active' driver has a license expiry date set to exactly 30 days from today

### 3.1.5 When

The daily automated check for license expiries is executed

### 3.1.6 Then

An alert is generated for users with 'Admin' or 'Dispatch Manager' roles, the alert is visible on the dashboard's alert panel, and a notification is sent via configured channels (in-app and email).

### 3.1.7 Validation Notes

Verify a notification record is created in the database. Check the UI for the dashboard alert and the bell icon notification. Check email logs for the sent notification.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

15-Day Expiry Alert Generation

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

An 'Active' driver has a license expiry date set to exactly 15 days from today

### 3.2.5 When

The daily automated check for license expiries is executed

### 3.2.6 Then

A new, distinct alert for the 15-day milestone is generated and delivered.

### 3.2.7 Validation Notes

Similar to AC-001, but for the 15-day milestone.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

7-Day Expiry Alert Generation

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

An 'Active' driver has a license expiry date set to exactly 7 days from today

### 3.3.5 When

The daily automated check for license expiries is executed

### 3.3.6 Then

A new, distinct alert for the 7-day milestone is generated and delivered.

### 3.3.7 Validation Notes

Similar to AC-001, but for the 7-day milestone.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Notification Content and Link

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

An expiry alert has been generated

### 3.4.5 When

A manager views the notification in the UI (dashboard or bell icon) or email

### 3.4.6 Then

The notification content clearly states the driver's name, the exact expiry date, and the number of days remaining (e.g., 'Driver John Doe's license expires on 2025-03-30 (in 30 days).'), and the notification is a clickable link that navigates directly to that driver's record.

### 3.4.7 Validation Notes

Manually click the link in the UI and email to confirm it navigates to the correct Odoo form view.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

No Alert for Inactive Drivers

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A driver is marked as 'Inactive' in the system

### 3.5.5 And

Their license is due to expire in 30, 15, or 7 days

### 3.5.6 When

The daily automated check is executed

### 3.5.7 Then

No alert is generated for this driver.

### 3.5.8 Validation Notes

Check the system logs and notification records to confirm no alert was created for the inactive driver.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

No Alert Outside of Milestones

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

An 'Active' driver has a license expiry date set to 29 days from today

### 3.6.5 When

The daily automated check is executed

### 3.6.6 Then

No new alert is generated.

### 3.6.7 Validation Notes

Verify that alerts are only triggered on the exact milestone days (30, 15, 7).

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Handling of Already Expired Licenses

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

An 'Active' driver's license expiry date is in the past

### 3.7.5 When

The daily automated check is executed

### 3.7.6 Then

A persistent, high-priority alert is displayed on the dashboard, but no new email notifications are sent daily to prevent spam.

### 3.7.7 Validation Notes

Confirm the dashboard shows a clear 'EXPIRED' status alert for the driver. Verify that repeated email notifications are not sent.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Idempotency of Alerts

### 3.8.3 Scenario Type

Error_Condition

### 3.8.4 Given

An alert for the 30-day milestone has already been sent for a specific driver

### 3.8.5 And

The driver's license expiry date has not been updated

### 3.8.6 When

The daily automated check runs again the next day (when the license is 29 days from expiry)

### 3.8.7 Then

The system does not generate a duplicate 30-day alert for that driver.

### 3.8.8 Validation Notes

The system must track that a milestone alert has been sent to prevent re-sending. Check database records to confirm only one alert per milestone is created.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- An item within the dashboard's 'Alerts Panel' (REQ-REP-002).
- A notification item in Odoo's standard notification menu (bell icon).

## 4.2.0 User Interactions

- Clicking on an alert in the dashboard or notification menu must navigate the user directly to the corresponding driver's form view.

## 4.3.0 Display Requirements

- Alert text must be clear and concise, including driver name, expiry date, and time remaining.
- Alerts for already expired licenses should be visually distinct (e.g., red color, warning icon) on the dashboard.

## 4.4.0 Accessibility Needs

- Alert colors must have sufficient contrast ratio to meet WCAG 2.1 AA standards.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-ALERT-01

### 5.1.2 Rule Description

Alerts are triggered at 30, 15, and 7-day intervals before the license expiry date.

### 5.1.3 Enforcement Point

During the execution of the daily scheduled system job.

### 5.1.4 Violation Handling

N/A - This is a system-generated event.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-ALERT-02

### 5.2.2 Rule Description

Expiry alerts are only generated for drivers with an 'Active' status.

### 5.2.3 Enforcement Point

During the initial data query of the daily scheduled job.

### 5.2.4 Violation Handling

N/A - Inactive drivers are filtered out from the check.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-012

#### 6.1.1.2 Dependency Reason

The driver model must have a 'License Expiry Date' field to be checked.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-014

#### 6.1.2.2 Dependency Reason

The driver model must have an 'Active'/'Inactive' status to filter out irrelevant drivers.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-060

#### 6.1.3.2 Dependency Reason

The core notification system (in-app and email) must be implemented to deliver the alerts.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-065

#### 6.1.4.2 Dependency Reason

The dashboard's 'Alerts Panel' component must exist as a target for displaying these alerts.

## 6.2.0.0 Technical Dependencies

- Odoo's scheduled action framework (`ir.cron`).
- Odoo's mail and messaging system (`mail.thread`, `mail.activity`).

## 6.3.0.0 Data Dependencies

- Accurate and populated 'License Expiry Date' field in driver records.

## 6.4.0.0 External Dependencies

- A correctly configured email server (SMTP) for sending email notifications.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The daily scheduled job must complete its execution in under 5 minutes for a database of up to 10,000 active drivers.

## 7.2.0.0 Security

- Email notifications must not contain sensitive PII other than the driver's name.
- Links within notifications must point to the secure (HTTPS) application.

## 7.3.0.0 Usability

- Alerts must be actionable, providing a direct link to the relevant record to minimize clicks.

## 7.4.0.0 Accessibility

- Compliant with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- N/A - This is a backend process with UI components that fall under general system compatibility.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires a backend scheduled job (`ir.cron`).
- Logic to ensure idempotency (not sending duplicate alerts for the same milestone) needs to be implemented, likely by creating and checking records in a custom model.
- Integration with both the Odoo notification system and the custom dashboard alert panel.

## 8.3.0.0 Technical Risks

- Incorrect timezone handling could cause the job to run on the wrong day or calculate date differences incorrectly.
- A poorly optimized query could cause performance degradation on large datasets.

## 8.4.0.0 Integration Points

- Odoo `hr.employee` model (read).
- Odoo `ir.cron` model (create/configure).
- Odoo messaging/activity system (write).
- Custom dashboard component (write/read).

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify alert generation at exactly 30, 15, and 7 days.
- Verify no alert is generated at 29, 16, or 8 days.
- Verify no alerts for inactive drivers.
- Verify persistent dashboard alert for already expired licenses.
- Verify clicking a notification navigates to the correct driver.
- Verify the scheduled job can be run manually for testing purposes.
- Verify that running the job multiple times on the same day does not create duplicate alerts.

## 9.3.0.0 Test Data Needs

- Driver records with license expiry dates set to T+30, T+15, T+7 days.
- Driver records with expiry dates at T+29, T-1 (expired).
- An inactive driver record with an upcoming expiry date.
- A driver record with a null expiry date.

## 9.4.0.0 Testing Tools

- Pytest for unit/integration tests.
- Odoo's developer mode for manually triggering scheduled actions.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code is peer-reviewed and merged into the main branch.
- Unit tests are written for the date calculation and driver selection logic, achieving >80% coverage.
- Integration tests are written to verify the `ir.cron` job creates the correct notifications.
- UI components (dashboard alert, notification link) are reviewed and approved by the product owner.
- The scheduled job's performance is verified against the NFR.
- Technical documentation for the scheduled job and alert mechanism is created.
- Story is deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- Requires all prerequisite stories to be completed and merged.
- The logic for idempotency should be carefully designed to avoid future issues.
- Requires coordination with frontend development if the dashboard alert panel is being built concurrently.

## 11.4.0.0 Release Impact

This is a key compliance feature and should be included in the initial release (Phase 1 or 2 as per REQ-TRN-001).


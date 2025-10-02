# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-061 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | User configures notification preferences for type ... |
| As A User Story | As an authenticated system user, I want to access ... |
| User Persona | Any authenticated system user (Admin, Dispatch Man... |
| Business Value | Improves user satisfaction and efficiency by reduc... |
| Functional Area | User Profile & Settings |
| Story Theme | System Usability and Personalization |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

User can access and view their notification preferences screen

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am an authenticated user logged into the system

### 3.1.5 When

I navigate to my user profile or settings area and select 'Notification Preferences'

### 3.1.6 Then

The system displays a screen listing all notification types applicable to my user role.

### 3.1.7 And

The displayed settings accurately reflect my currently saved preferences.

### 3.1.8 Validation Notes

Verify by logging in as each user role (Admin, Manager, Finance, Driver) and confirming the preference screen is accessible and displays role-appropriate options.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

User successfully updates and saves their notification preferences

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am on the 'Notification Preferences' screen

### 3.2.5 When

I change one or more settings (e.g., I disable 'Email' for 'Document Expiry' alerts)

### 3.2.6 And

If I navigate away from and back to the screen, my new settings are correctly displayed.

### 3.2.7 Then

The system displays a success message like 'Your notification preferences have been saved.'

### 3.2.8 Validation Notes

Test by changing a setting, saving, reloading the page, and verifying the change is still present.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

System respects the user's configured preferences when sending notifications

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am a Finance Officer and I have configured my preferences to receive 'Low Card Balance' alerts via 'In-App' but NOT via 'Email'

### 3.3.5 When

A system event occurs that triggers a 'Low Card Balance' alert targeted to me

### 3.3.6 Then

I receive a notification within the Odoo application (e.g., bell icon).

### 3.3.7 And

I do not receive an email for this specific alert.

### 3.3.8 Validation Notes

Requires an integration test. Configure a user's preferences, then trigger a specific event and check the Odoo mail queue and the user's in-app notifications to verify the correct channel was used.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Notification options are filtered based on user role

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am logged in as a 'Driver'

### 3.4.5 When

I view my 'Notification Preferences' screen

### 3.4.6 Then

I do not see options for administrative or financial alerts like 'GSP API Failure' or 'Trip Profitability Report Ready'.

### 3.4.7 And

I only see options relevant to my role, such as 'New Trip Assigned', 'Trip Canceled', or 'Expense Rejected'.

### 3.4.8 Validation Notes

Log in as a Driver and inspect the list of available notification types. Compare this with the list shown to a Finance Officer.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

New users have a set of default notification preferences

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

An Admin creates a new user account for a Dispatch Manager

### 3.5.5 When

The new Dispatch Manager logs in for the first time and navigates to their notification preferences

### 3.5.6 Then

A predefined set of default preferences is already configured.

### 3.5.7 And

Critical alerts (e.g., 'Critical Trip Event Logged') have both 'In-App' and 'Email' channels enabled by default.

### 3.5.8 Validation Notes

Create a new user, log in as them, and immediately check the preferences screen to verify defaults are applied.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

System provides feedback on failure to save preferences

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am on the 'Notification Preferences' screen

### 3.6.5 When

I attempt to save my changes, but a server-side error occurs

### 3.6.6 Then

The system displays a user-friendly error message, such as 'Could not save preferences. Please try again.'

### 3.6.7 And

My unsaved changes remain on the screen, and the old preferences are retained in the database.

### 3.6.8 Validation Notes

Simulate a server error (e.g., using browser developer tools to block the save request) and verify the UI response.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item under User Settings/Profile named 'Notification Preferences'.
- A view that lists notification types in rows.
- Checkboxes or toggle switches for 'In-App' and 'Email' channels for each notification type.
- A 'Save' button to persist changes.
- A 'Cancel' or 'Discard' button to revert unsaved changes.
- Success and error message banners.

## 4.2.0 User Interactions

- The 'Save' button should be disabled by default and only become enabled when a preference is changed.
- Clicking 'Save' triggers an API call to update the user's preferences and displays a confirmation message upon success.
- Toggling a checkbox should immediately reflect a pending change in the UI.

## 4.3.0 Display Requirements

- The list of notification types must be dynamically generated based on the user's role.
- Each notification type should have a clear, user-friendly label (e.g., 'Upcoming Document Expiry' instead of 'doc_expiry_alert').

## 4.4.0 Accessibility Needs

- All interactive elements (toggles, buttons) must be keyboard-navigable and have appropriate ARIA labels.
- The layout must be responsive and usable on mobile devices, as per REQ-INT-001.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-PREF-001

### 5.1.2 Rule Description

A user can only configure notification preferences for alert types relevant to their assigned role(s).

### 5.1.3 Enforcement Point

Backend logic that populates the preferences screen.

### 5.1.4 Violation Handling

Irrelevant notification types are not rendered on the user's preference screen.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-PREF-002

### 5.2.2 Rule Description

If a user has no preference saved for a specific notification type, a system-defined default setting must be applied.

### 5.2.3 Enforcement Point

The notification dispatch service.

### 5.2.4 Violation Handling

The system falls back to a default configuration (e.g., send critical alerts to all channels).

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-058

#### 6.1.1.2 Dependency Reason

Requires an authenticated user session to associate preferences with a user.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-060

#### 6.1.2.2 Dependency Reason

The core notification delivery system (both in-app and email) must exist to be configured. This story modifies its behavior.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-078

#### 6.1.3.2 Dependency Reason

The 'Document Expiry' alert mechanism must exist to be a configurable notification type.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-081

#### 6.1.4.2 Dependency Reason

The 'Low Card Balance' alert mechanism must exist to be a configurable notification type.

## 6.2.0.0 Technical Dependencies

- A new Odoo model to store user notification preferences (e.g., `tms.notification.preference`) linked to `res.users`.
- A centralized notification dispatch service/method that can be modified to check user preferences before sending.
- Odoo's email server configuration must be functional.
- Odoo's internal messaging/bus system must be active.

## 6.3.0.0 Data Dependencies

- A master, extensible list of all possible notification types (e.g., as a selection field or a separate data model) that can be associated with user roles.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The preferences screen must load in under 2 seconds.
- Saving preferences should provide feedback to the user within 1 second.

## 7.2.0.0 Security

- A user must only be able to view and edit their own notification preferences.
- API endpoints for managing preferences must be protected and require authentication.

## 7.3.0.0 Usability

- The purpose of each notification type should be clear and unambiguous.
- The interface should be simple and intuitive, minimizing clicks to change a setting.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards, as stated in REQ-INT-001.

## 7.5.0.0 Compatibility

- The feature must be fully functional on all modern web browsers supported by Odoo 18.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creating a new data model and a new settings view in Odoo.
- The primary complexity lies in refactoring all existing and future notification trigger points throughout the application to query this new preference model before dispatching an alert.
- Logic is needed to map user roles to available notification types.
- Requires a data seeding strategy for default preferences for new and existing users.

## 8.3.0.0 Technical Risks

- Risk of missing a notification trigger point during refactoring, causing some alerts to bypass user preferences.
- Performance risk if the preference check adds significant overhead to every notification event.

## 8.4.0.0 Integration Points

- Integrates with Odoo's user management system (`res.users`).
- Integrates with Odoo's mail and messaging systems.
- Touches every module/feature that generates a user-facing notification.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Accessibility

## 9.2.0.0 Test Scenarios

- Verify preferences screen for each user role (Admin, Manager, Finance, Driver).
- Test saving and persistence of settings for each role.
- End-to-end test for at least one notification type: enable email, trigger event, verify email is received. Disable email, trigger event, verify email is NOT received.
- End-to-end test for in-app notifications in the same manner.
- Test the default settings for a newly created user.

## 9.3.0.0 Test Data Needs

- User accounts for each of the four roles.
- Test data that can trigger specific alerts on demand (e.g., a vehicle document with an expiry date of tomorrow).

## 9.4.0.0 Testing Tools

- Pytest for backend unit/integration tests.
- Odoo's built-in testing framework.
- Browser developer tools for UI and accessibility checks.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests implemented for the new model and preference-checking logic, with >80% coverage.
- Integration testing completed to confirm preferences are respected by the notification system.
- User interface reviewed and approved by the product owner/designer.
- Performance requirements for screen load and save times are met.
- Security requirement (users can only edit their own preferences) is validated.
- User documentation is updated to explain how to manage notification preferences.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🟡 Medium

## 11.3.0.0 Sprint Considerations

- This story should be prioritized after the core notification system (US-060) is in place.
- Requires a clear definition of all notification types across the system before development begins. A technical task to identify all notification points may be needed first.

## 11.4.0.0 Release Impact

This is a significant usability enhancement. While not critical for a minimum viable product, its absence will be felt as system usage and the number of alerts increase.


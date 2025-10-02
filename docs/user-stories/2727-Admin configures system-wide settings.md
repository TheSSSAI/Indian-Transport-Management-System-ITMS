# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-022 |
| Elaboration Date | 2025-01-18 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin configures system-wide settings |
| As A User Story | As an Admin, I want a centralized settings page to... |
| User Persona | Admin: A user with full system access responsible ... |
| Business Value | Enables the business to adapt the system to changi... |
| Functional Area | System Administration & Configuration |
| Story Theme | System Foundation & Customization |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin can access the TMS settings page

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a user with the 'Admin' role

### 3.1.5 When

I navigate to the main Odoo 'Settings' application

### 3.1.6 Then

I should see a menu item or section titled 'Transport Management'

### 3.1.7 Validation Notes

Verify the 'Transport Management' settings link is visible and clickable for the Admin group within the standard Odoo settings interface.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Settings page displays all configurable parameters with current values

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am on the 'Transport Management' settings page

### 3.2.5 When

the page finishes loading

### 3.2.6 Then

I should see labeled input fields for 'Session Timeout (minutes)', 'Expense Submission Deadline (days)', and 'Document Expiry Alert Intervals (days)'

### 3.2.7 Validation Notes

Check that each field is populated with the current value from the database, or a sensible default if not yet set.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Admin successfully edits and saves a setting

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am on the 'Transport Management' settings page

### 3.3.5 When

I change the value of 'Session Timeout (minutes)' to '45' and click 'Save'

### 3.3.6 Then

the system should confirm the settings have been saved

### 3.3.7 And

when I refresh the page, the 'Session Timeout (minutes)' field should display '45'

### 3.3.8 Validation Notes

Verify the value is persisted in the `ir.config_parameter` table or the custom `res.config.settings` model.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

System rejects non-numeric input for numeric fields

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am on the 'Transport Management' settings page

### 3.4.5 When

I enter 'thirty' into the 'Session Timeout (minutes)' field and click 'Save'

### 3.4.6 Then

the system must prevent the save operation

### 3.4.7 And

a user-friendly validation error message like 'Please enter a valid number' should be displayed next to the field

### 3.4.8 Validation Notes

Test with various non-numeric strings in all integer-based fields.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

System rejects out-of-range values

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am on the 'Transport Management' settings page

### 3.5.5 When

I enter '-5' into the 'Expense Submission Deadline (days)' field and click 'Save'

### 3.5.6 Then

the system must prevent the save operation

### 3.5.7 And

a validation error message like 'Value must be a positive number' should be displayed

### 3.5.8 Validation Notes

Test with zero and negative numbers for fields that require a positive integer (e.g., timeout > 0).

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Non-Admin user is denied access to the settings page

### 3.6.3 Scenario Type

Security

### 3.6.4 Given

I am logged in as a user with the 'Dispatch Manager' role

### 3.6.5 When

I attempt to navigate directly to the URL for the 'Transport Management' settings page

### 3.6.6 Then

the system must display an 'Access Denied' error and prevent me from viewing or editing any settings

### 3.6.7 Validation Notes

Verify using Odoo's `ir.model.access.csv` and/or record rules that only the Admin group has read/write access to the `res.config.settings` model for this module.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

System correctly validates the format for alert intervals

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

I am on the 'Transport Management' settings page

### 3.7.5 When

I enter '30,15,foo' into the 'Document Expiry Alert Intervals (days)' field and click 'Save'

### 3.7.6 Then

the system must prevent the save

### 3.7.7 And

a validation error message like 'Please enter a comma-separated list of numbers' should be displayed

### 3.7.8 Validation Notes

Test with various malformed strings, including trailing commas, spaces, and non-numeric characters.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item under Odoo's main 'Settings' application for 'Transport Management'.
- Integer input field for 'Session Timeout (minutes)'.
- Integer input field for 'Expense Submission Deadline (days)'.
- Character/Text input field for 'Document Expiry Alert Intervals (days)'.
- Standard Odoo 'Save' and 'Discard' buttons.

## 4.2.0 User Interactions

- Admin clicks the menu item to open the settings view.
- Admin edits values in the input fields.
- Admin clicks 'Save' to persist changes or 'Discard' to cancel.
- The system provides immediate visual feedback on validation errors without a full page reload where possible.

## 4.3.0 Display Requirements

- Each setting must have a clear, descriptive label.
- Each setting should have a tooltip or help text explaining its purpose and impact (e.g., 'Duration of user inactivity in minutes before automatic logout. Set to 0 to disable.').

## 4.4.0 Accessibility Needs

- All form fields must have associated labels for screen reader compatibility.
- Validation error messages must be programmatically associated with their respective fields.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-CFG-001

### 5.1.2 Rule Description

Only users with Admin privileges can view or modify system-wide settings.

### 5.1.3 Enforcement Point

Server-side, on any read or write request to the configuration model.

### 5.1.4 Violation Handling

An 'Access Denied' error is returned to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-CFG-002

### 5.2.2 Rule Description

Session timeout must be a positive integer, representing minutes.

### 5.2.3 Enforcement Point

On save/validation of the settings form.

### 5.2.4 Violation Handling

The save is blocked and a validation error is displayed.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-004

#### 6.1.1.2 Dependency Reason

A user must be assignable to the 'Admin' role to test the access control for this feature.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-070

#### 6.1.2.2 Dependency Reason

The core Role-Based Access Control (RBAC) mechanism must be implemented to enforce security rules on the settings page.

## 6.2.0.0 Technical Dependencies

- This feature must be implemented using Odoo's standard `res.config.settings` transient model to integrate seamlessly with the Odoo settings interface.

## 6.3.0.0 Data Dependencies

*No items available*

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The settings page must load in under 2 seconds.
- Saving the settings must complete in under 500ms.

## 7.2.0.0 Security

- Access to the settings model (`res.config.settings` for this module) must be strictly limited to the Admin user group via Odoo's security layer (`ir.model.access.csv`).
- Input values must be properly sanitized to prevent injection attacks, although Odoo's ORM provides this by default.

## 7.3.0.0 Usability

- The settings should be grouped logically under a 'Transport Management' heading.
- Help text for each setting is mandatory to ensure the Admin understands the impact of their changes.

## 7.4.0.0 Accessibility

- The settings page must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The settings page must render correctly on all browsers supported by Odoo 18.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- The UI for the settings page using `res.config.settings` is low complexity.
- Implementing the *effect* of the session timeout (REQ-NFR-003) is the primary complexity driver. It may require overriding core Odoo behavior or configuring the underlying web server, which requires careful implementation and testing.
- The other settings (expense deadline, alert intervals) are low complexity as they will simply be read by other components.

## 8.3.0.0 Technical Risks

- Incorrectly implementing the session timeout could introduce security vulnerabilities or affect system stability. This requires thorough testing across different user scenarios.

## 8.4.0.0 Integration Points

- Odoo's core authentication/session management system (for session timeout).
- The Expense Management module (to check the submission deadline).
- The scheduled job/cron that generates document expiry alerts.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify that a non-Admin user cannot read or write settings via direct RPC calls.
- Create an automated test to confirm the session timeout mechanism works. This may involve manipulating time in the test environment.
- Create an integration test where another feature (e.g., expense submission) correctly reads and applies a value from these settings.
- Manually test the end-to-end flow: log in as Admin, change timeout to 1 minute, log in as another user, wait 1+ minute, and verify the session is invalidated upon the next action.

## 9.3.0.0 Test Data Needs

- A user account with 'Admin' role.
- A user account with a non-Admin role (e.g., 'Dispatch Manager').

## 9.4.0.0 Testing Tools

- Pytest for backend unit and integration tests.
- Odoo's built-in testing framework.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests implemented for the settings model logic and validation, achieving >80% coverage
- Integration testing completed to verify access control and that other modules can read the settings
- User interface reviewed and approved by the product owner
- Security requirements validated, including a manual test of access control for non-Admin roles
- Help text and labels are implemented for all settings
- Story deployed and verified in the staging environment, including a manual E2E test of the session timeout feature

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story that provides configuration for other features. It should be prioritized in an early sprint.
- Allocate specific time for researching and testing the session timeout implementation, as it is the highest-risk part of this story.

## 11.4.0.0 Release Impact

This feature is critical for the initial release as it allows administrators to tailor the system to their organization's policies from day one.


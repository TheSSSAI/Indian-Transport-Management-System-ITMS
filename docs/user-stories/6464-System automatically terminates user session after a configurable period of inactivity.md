# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-059 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System automatically terminates user session after... |
| As A User Story | As an authenticated system user, I want my session... |
| User Persona | Any authenticated user of the system (Admin, Dispa... |
| Business Value | Enhances system security by mitigating the risk of... |
| Functional Area | Security & User Management |
| Story Theme | System Security Hardening |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful Timeout and Logout

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

an Admin has configured the session timeout to 15 minutes and the warning period to 2 minutes, and a user is logged into the TMS

### 3.1.5 When

the user remains inactive for 13 minutes, causing a warning modal to appear, and the user takes no further action for the next 2 minutes

### 3.1.6 Then

the user is automatically logged out, their session is invalidated on the server, and they are redirected to the login page.

### 3.1.7 Validation Notes

Verify redirection to the login page. Attempt to access a protected page using the browser's back button; it should fail and redirect back to login.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Session Extension from Warning Dialog

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

the session timeout warning modal is displayed after a period of inactivity

### 3.2.5 When

the user clicks the 'Stay Logged In' button before the warning countdown ends

### 3.2.6 Then

the modal closes, the inactivity timer is reset to its full duration (15 minutes), and the user can continue their work without interruption.

### 3.2.7 Validation Notes

After clicking the button, wait for another 14 minutes of inactivity. The warning modal should reappear, confirming the timer was reset.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

User Activity Resets Inactivity Timer

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

the session timeout is configured to 15 minutes and a user is logged in

### 3.3.5 When

the user performs any server-interacting action (e.g., navigates to a new page, saves a record) after 10 minutes of inactivity

### 3.3.6 Then

the inactivity timer is reset to 15 minutes without any warning being shown to the user.

### 3.3.7 Validation Notes

Perform an action at the 10-minute mark. Wait another 10 minutes. No warning should appear.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Admin Configuration of Timeout Duration

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

a user with the 'Admin' role is logged in

### 3.4.5 When

the user navigates to the system settings and changes the 'Session Inactivity Timeout' value from 15 to 30 minutes and saves

### 3.4.6 Then

the new timeout duration of 30 minutes is applied to all subsequent user sessions.

### 3.4.7 Validation Notes

Log out and log back in as a non-admin user. Verify that the timeout warning now appears after 28 minutes of inactivity (assuming a 2-minute warning).

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Activity in One Browser Tab Resets Timer for All Tabs

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

a user is logged into the TMS in two separate browser tabs of the same browser

### 3.5.5 When

the user is inactive in Tab 1 for 14 minutes but performs an action in Tab 2

### 3.5.6 Then

the session timer is reset for the entire session, and the user is not logged out from Tab 1.

### 3.5.7 Validation Notes

Open two tabs. Let Tab 1 sit idle. Interact with Tab 2 at the 14-minute mark. Switch back to Tab 1; it should remain active.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Server-Side Session Invalidation

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

a user's session has timed out and they have been redirected to the login page

### 3.6.5 When

a malicious actor attempts to reuse the old session token to make a direct API call to a protected endpoint

### 3.6.6 Then

the server rejects the request with an authentication error (e.g., 401 Unauthorized).

### 3.6.7 Validation Notes

This requires a technical test using a tool like Postman or cURL to capture a session cookie and replay it after the session has expired on the server.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Modal dialog for session timeout warning.
- Countdown timer within the modal.
- 'Stay Logged In' button.
- 'Log Out Now' button.
- Input field in Admin settings for 'Session Inactivity Timeout (minutes)'.

## 4.2.0 User Interactions

- The warning modal should appear on top of all other content.
- Clicking 'Stay Logged In' should close the modal and reset the timer.
- Clicking 'Log Out Now' should immediately log the user out.
- If no action is taken, the system should automatically log the user out when the countdown finishes.

## 4.3.0 Display Requirements

- The warning modal must clearly state that the session is about to expire and show the remaining time.
- Upon logout, the user must be redirected to the login page with a message like 'Your session has expired due to inactivity.'

## 4.4.0 Accessibility Needs

- The warning modal must be keyboard accessible (focusable buttons, Esc to close).
- The countdown and text must be announced by screen readers.
- Complies with WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-SEC-001

### 5.1.2 Rule Description

The session inactivity timeout duration must be a configurable system parameter accessible only to users with the 'Admin' role.

### 5.1.3 Enforcement Point

System Settings panel.

### 5.1.4 Violation Handling

Non-admin users cannot see or edit the setting.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-SEC-002

### 5.2.2 Rule Description

Session invalidation must occur on the server-side to ensure security. A client-side redirect alone is insufficient.

### 5.2.3 Enforcement Point

Odoo server session handling logic.

### 5.2.4 Violation Handling

N/A - System design requirement.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-058

#### 6.1.1.2 Dependency Reason

A user must be able to log in and have an active session before that session can time out.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-022

#### 6.1.2.2 Dependency Reason

An Admin settings page is required to host the configurable timeout value.

## 6.2.0.0 Technical Dependencies

- Odoo 18 session management framework (`res.users`).
- Odoo Web Library (OWL) for the frontend warning modal.

## 6.3.0.0 Data Dependencies

- Access to Odoo's `ir.config_parameter` to store and retrieve the timeout setting.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The client-side activity tracking mechanism must have negligible impact on browser performance.

## 7.2.0.0 Security

- This entire story is a security requirement as defined in REQ-NFR-003. The primary goal is to prevent unauthorized access via stale sessions. Server-side session invalidation is mandatory.

## 7.3.0.0 Usability

- The warning modal should be clear and provide sufficient time for the user to respond before logging them out.

## 7.4.0.0 Accessibility

- All UI components related to this feature must meet WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must work consistently across all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires coordinated implementation between frontend (OWL for the dialog and timer) and backend (Odoo for session invalidation).
- Correctly handling the multi-tab scenario requires robust client-side logic.
- The configuration setting must be securely stored and correctly applied to the session logic.

## 8.3.0.0 Technical Risks

- A purely client-side implementation would be a security risk; ensuring the server-side invalidation is robust is critical.
- Potential for race conditions if not handled carefully (e.g., user clicks 'Stay Logged In' just as the server invalidates the session).

## 8.4.0.0 Integration Points

- Integrates with Odoo's core authentication and session management system.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify successful logout after the exact timeout period.
- Verify session extension from the warning dialog.
- Verify activity in one tab resets the timer for another.
- Verify that an Admin can change the timeout duration and it takes effect.
- Perform a security test to confirm an expired session token cannot be used to access protected API endpoints.

## 9.3.0.0 Test Data Needs

- An 'Admin' user account.
- A non-admin user account (e.g., 'Dispatch Manager').

## 9.4.0.0 Testing Tools

- Odoo's built-in testing framework for backend logic.
- A browser automation tool like Cypress or Playwright for E2E testing.
- An API client like Postman for security testing of expired tokens.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for backend configuration logic and passing with >80% coverage
- Automated E2E tests for the timeout and session extension flow are implemented and passing
- User interface reviewed and approved for clarity and usability
- Security requirement for server-side session invalidation is explicitly tested and verified
- Documentation for the Admin setting is added to the Administrator Guide
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational security feature and should be prioritized early in the development cycle.
- Requires a developer comfortable with both Odoo's Python backend and the OWL JavaScript frontend.

## 11.4.0.0 Release Impact

- Essential for the initial production release to ensure baseline security standards are met.


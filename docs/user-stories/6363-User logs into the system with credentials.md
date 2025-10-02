# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-058 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | User logs into the system with credentials |
| As A User Story | As a Registered System User (Admin, Dispatch Manag... |
| User Persona | Any provisioned user of the TMS (Admin, Dispatch M... |
| Business Value | Enables secure, role-based access to the system, e... |
| Functional Area | User Authentication & Security |
| Story Theme | Core System Access |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful login with valid credentials

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a registered user with an active account, and I am on the TMS login page

### 3.1.5 When

I enter my correct email and password and click the 'Log In' button

### 3.1.6 Then

I am successfully authenticated, a session is created, and I am redirected to my role-specific dashboard.

### 3.1.7 Validation Notes

Test with an active account for each user role (Admin, Manager, Finance, Driver) and verify redirection to the correct landing page for each.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Login attempt with an incorrect password

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am on the TMS login page and have entered a valid email for an active account

### 3.2.5 When

I enter an incorrect password and click the 'Log In' button

### 3.2.6 Then

The system displays a generic error message 'Invalid email or password.', I remain on the login page, and the password field is cleared.

### 3.2.7 Validation Notes

Verify that the error message does not indicate whether the email or the password was incorrect to prevent user enumeration.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Login attempt with a non-existent email

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am on the TMS login page

### 3.3.5 When

I enter an email address that is not registered in the system and click the 'Log In' button

### 3.3.6 Then

The system displays the same generic error message 'Invalid email or password.' and I remain on the login page.

### 3.3.7 Validation Notes

This ensures the system does not confirm the existence of user accounts to unauthorized individuals.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Login attempt with an inactive account

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am a registered user whose account has been deactivated by an Admin

### 3.4.5 When

I enter my correct email and password and click the 'Log In' button

### 3.4.6 Then

The system prevents login and displays a specific error message, such as 'Your account is inactive. Please contact an administrator.'

### 3.4.7 Validation Notes

Create an inactive user account in the test data to verify this specific flow.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Login attempt with empty credentials

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am on the TMS login page

### 3.5.5 When

I click the 'Log In' button without entering an email or a password

### 3.5.6 Then

The system prevents the form submission and displays inline validation messages indicating that both fields are required.

### 3.5.7 Validation Notes

Check for standard HTML5 or framework-specific form validation behavior.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Password field masks input

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

I am on the TMS login page

### 3.6.5 When

I type characters into the password field

### 3.6.6 Then

The characters are masked (e.g., displayed as dots or asterisks).

### 3.6.7 Validation Notes

Verify the input type of the password field is 'password'.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Login communication is secure

### 3.7.3 Scenario Type

Happy_Path

### 3.7.4 Given

I am on the TMS login page

### 3.7.5 When

I submit my login credentials

### 3.7.6 Then

The request is sent to the server over an HTTPS connection.

### 3.7.7 Validation Notes

Use browser developer tools to inspect the network request and confirm the protocol is HTTPS and the connection is secure (TLS 1.2+ as per REQ-INT-004).

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Email input field
- Password input field (masked)
- Log In button
- Area for displaying error messages

## 4.2.0 User Interactions

- User can type into input fields.
- User can click the 'Log In' button to submit the form.
- The form can be submitted by pressing 'Enter' in the password field.

## 4.3.0 Display Requirements

- The login page should be clean, professional, and consistent with the Odoo 18 UI.
- Error messages must be clear and user-friendly.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The page must be fully navigable using a keyboard.
- Error messages must be programmatically associated with their respective fields for screen readers.
- Meets WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

*No items available*

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-001', 'dependency_reason': 'A user account must be created by an Admin before any user can log in. This story provides the mechanism for user provisioning.'}

## 6.2.0 Technical Dependencies

- Odoo 18 framework, specifically its core authentication module (`res.users` model and associated controllers).
- A configured and running PostgreSQL database.

## 6.3.0 Data Dependencies

- At least one active user account must exist in the `res.users` table for testing.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- 95% of login attempts (from button click to redirect or error message) must complete in under 2 seconds, as per REQ-NFR-001.

## 7.2.0 Security

- All authentication traffic must be encrypted in transit using TLS 1.2 or newer (REQ-INT-004).
- The system must leverage Odoo's built-in protection against brute-force attacks (e.g., rate limiting).
- User passwords must be securely hashed and salted in the database (handled by Odoo core).
- The system must not be vulnerable to user enumeration attacks.
- User session timeout must be implemented as per REQ-NFR-003.

## 7.3.0 Usability

- The login process must be simple and intuitive for all user types.

## 7.4.0 Accessibility

- The login page must comply with WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0 Compatibility

- The login page must be fully functional and responsive on modern web browsers (Chrome, Firefox, Safari, Edge) and on mobile screen sizes from 360px width upwards (REQ-INT-001).

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- This story primarily leverages Odoo's standard, out-of-the-box authentication functionality.
- The main development effort is ensuring the post-login redirection logic correctly routes users based on their role, and theming the login page if necessary.

## 8.3.0 Technical Risks

- Minimal risk. Potential for misconfiguration of Odoo's security settings or redirection rules.

## 8.4.0 Integration Points

- Integrates directly with Odoo's `res.users` model and authentication system.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E
- Security
- Accessibility

## 9.2.0 Test Scenarios

- Successful login for each of the 4 user roles.
- Failed login due to incorrect password.
- Failed login due to non-existent email.
- Failed login for a deactivated user.
- Validation of required fields.
- Verification of correct redirection post-login for each role.
- Manual security check for user enumeration.

## 9.3.0 Test Data Needs

- An active user account for each role: Admin, Dispatch Manager, Finance Officer, Driver.
- One deactivated user account.
- A list of email addresses that do not exist in the system.

## 9.4.0 Testing Tools

- Odoo's built-in test framework.
- Pytest for backend tests.
- Browser-based E2E testing framework (e.g., Playwright, Cypress).
- Browser developer tools for network and accessibility inspection.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit and integration tests covering the redirection logic are written and passing with >80% coverage.
- Automated E2E tests for the happy path login scenario are created and passing.
- The login page UI is verified to be responsive and matches design specifications.
- Security checks (HTTPS, no user enumeration) have been manually verified.
- Accessibility of the login form has been validated against WCAG 2.1 AA.
- The story has been deployed and verified in the staging environment.

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational, blocking story. It must be completed in the first development sprint to enable testing of any other user-facing features.

## 11.4.0 Release Impact

- Critical for the initial release (Phase 1). The system cannot go live without this functionality.


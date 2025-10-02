# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-046 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver logs into the mobile-friendly web portal |
| As A User Story | As a Driver, I want to securely log into a simple,... |
| User Persona | Driver: An on-field user who primarily interacts w... |
| Business Value | Enables drivers to access the system, which is the... |
| Functional Area | User Authentication & Access |
| Story Theme | Driver Portal |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful login with valid credentials

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A user with the 'Driver' role exists and is on the mobile-friendly login page

### 3.1.5 When

The driver enters their correct username and password and taps the 'Log In' button

### 3.1.6 Then

The system validates the credentials, establishes a secure session, and redirects the driver to their main portal dashboard.

### 3.1.7 Validation Notes

Verify redirection to the correct driver-specific dashboard URL. Check for the creation of a valid session cookie.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Login attempt with invalid password

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A user is on the login page

### 3.2.5 When

The user enters a valid username but an incorrect password and taps 'Log In'

### 3.2.6 Then

The system displays a generic error message like 'Invalid username or password', the password field is cleared, and the user remains on the login page.

### 3.2.7 Validation Notes

Ensure the error message does not specify whether the username or password was incorrect. The username field should retain its value.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Login attempt with non-existent username

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A user is on the login page

### 3.3.5 When

The user enters a username that does not exist in the system and taps 'Log In'

### 3.3.6 Then

The system displays a generic error message like 'Invalid username or password' and the user remains on the login page.

### 3.3.7 Validation Notes

This should behave identically to AC-002 to prevent username enumeration attacks.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Login attempt with empty credentials

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A user is on the login page

### 3.4.5 When

The user taps the 'Log In' button without entering a username or password

### 3.4.6 Then

The system prevents the login attempt and displays inline validation messages like 'This field is required' for both empty fields.

### 3.4.7 Validation Notes

Verify that no authentication request is sent to the server.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Login attempt by an inactive driver

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

A driver's account has been set to 'Inactive'

### 3.5.5 When

The driver attempts to log in with their previously valid credentials

### 3.5.6 Then

The system denies access and displays a specific message, such as 'Your account is inactive. Please contact your manager.'

### 3.5.7 Validation Notes

Test with a user account that is active, then deactivate it and re-test.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Login page responsiveness on mobile device

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A user is accessing the login page

### 3.6.5 When

The page is viewed on a device with a screen width of 360px

### 3.6.6 Then

All UI elements (input fields, labels, button) are clearly visible, usable, and correctly formatted without horizontal scrolling.

### 3.6.7 Validation Notes

Test using browser developer tools (mobile view) and on a physical mobile device.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Password input is masked

### 3.7.3 Scenario Type

Happy_Path

### 3.7.4 Given

A user is on the login page

### 3.7.5 When

The user types their password into the password field

### 3.7.6 Then

The characters entered are masked (e.g., displayed as dots or asterisks).

### 3.7.7 Validation Notes

Verify the input type of the password field is 'password'.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Text input for 'Username' or 'Email'
- Password input for 'Password'
- Primary button labeled 'Log In'
- Link for 'Forgot Password?'
- Display area for error messages

## 4.2.0 User Interactions

- Tapping into a field should bring up the appropriate keyboard (text or email).
- Tapping the 'Log In' button should trigger the authentication attempt.
- The interface should provide clear visual feedback on failed login attempts.

## 4.3.0 Display Requirements

- The page should have a clean, simple layout optimized for single-hand use on a mobile phone.
- Company branding/logo should be present.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels for screen readers.
- The page must be fully navigable using a keyboard.
- Color contrast for text and UI elements must meet WCAG 2.1 AA standards.

# 5.0.0 Business Rules

*No items available*

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-001

#### 6.1.1.2 Dependency Reason

A user account must be creatable in the system before anyone can log in.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-004

#### 6.1.2.2 Dependency Reason

The user account must be assigned the 'Driver' role to ensure correct redirection and permissions after login.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-014

#### 6.1.3.2 Dependency Reason

The ability to set a driver's status to 'Active' or 'Inactive' is required to test the inactive login scenario (AC-005).

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-047

#### 6.1.4.2 Dependency Reason

A basic 'Driver Portal Dashboard' page/view must exist as a redirection target upon successful login.

## 6.2.0.0 Technical Dependencies

- Odoo 18 authentication framework (`res.users`).
- Odoo Web Library (OWL) for building the custom, mobile-friendly UI.
- A defined URL route for the driver login portal.

## 6.3.0.0 Data Dependencies

- Availability of test user accounts with the 'Driver' role (one active, one inactive).

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The login process (from button tap to redirection or error message) must complete in under 2 seconds on a 4G mobile connection.

## 7.2.0.0 Security

- All login traffic must be encrypted using HTTPS (TLS 1.2+).
- The system must use Odoo's built-in authentication mechanisms and password hashing.
- The system must prevent username enumeration by providing a generic error message for both invalid usernames and passwords.
- Session management must be secure, with appropriate cookie flags (HttpOnly, Secure).

## 7.3.0.0 Usability

- The login process must be simple and intuitive, requiring minimal steps.
- Error messages must be clear and helpful.

## 7.4.0.0 Accessibility

- The login page must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The login page must render and function correctly on the latest versions of Chrome and Safari on both iOS and Android.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creating a custom OWL view and controller for the login page, separate from the standard Odoo backend login.
- Ensuring the custom UI securely integrates with Odoo's core authentication and session management.
- Thorough responsive design testing across different mobile device sizes and operating systems.

## 8.3.0.0 Technical Risks

- Potential for insecure implementation of the custom login form if not done correctly.
- CSS/layout issues on less common mobile screen sizes.

## 8.4.0.0 Integration Points

- Odoo's `res.users` model for user authentication.
- Odoo's web session management system.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security
- Accessibility
- Compatibility

## 9.2.0.0 Test Scenarios

- Verify login with a valid active driver.
- Verify login failure with an invalid password.
- Verify login failure with an invalid username.
- Verify login failure with an inactive driver account.
- Verify login failure with a valid non-driver account (should not redirect to driver portal).
- Verify UI on multiple mobile viewports (e.g., 360x640, 375x812, 414x896).
- Verify accessibility using an automated tool like Axe and manual keyboard navigation.

## 9.3.0.0 Test Data Needs

- An active user account with the 'Driver' role.
- An inactive user account with the 'Driver' role.
- A user account with a different role (e.g., 'Dispatch Manager').
- A list of invalid credentials to test with.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Browser developer tools for responsive testing.
- Axe for accessibility scanning.
- Postman or similar for API-level security testing (e.g., checking headers).

# 10.0.0.0 Definition Of Done

- All acceptance criteria are validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit and integration tests are written and achieve required coverage.
- E2E automated tests for the login flow are created and passing.
- The feature has been successfully tested on representative iOS and Android devices/emulators.
- Security review confirms adherence to security NFRs.
- Accessibility scan (automated and manual) confirms WCAG 2.1 AA compliance.
- Any necessary documentation for the custom login controller/view is created.
- The story is deployed and verified in the staging environment by a QA engineer or product owner.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story for the Driver Portal epic and blocks all other driver-facing stories.
- It should be prioritized for an early sprint to unblock parallel development of other driver features.

## 11.4.0.0 Release Impact

Critical for the initial release of the Driver Portal functionality. The system cannot go live for drivers without this feature.


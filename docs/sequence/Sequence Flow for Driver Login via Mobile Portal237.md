# 1 Overview

## 1.1 Diagram Id

SEQ-AF-014

## 1.2 Name

Driver Login via Mobile Portal

## 1.3 Description

A driver provides their credentials on the mobile-friendly web portal. The system validates these credentials against stored user records and, upon success, establishes an authenticated session.

## 1.4 Type

🔹 AuthenticationFlow

## 1.5 Purpose

To securely authenticate a user with the 'Driver' role and grant access to the driver-specific portal functionalities.

## 1.6 Complexity

Low

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-DRV-UI
- REPO-TMS-CORE

## 1.10 Key Interactions

- Driver enters username and password into the login form.
- REPO-DRV-UI submits credentials to an authentication endpoint.
- REPO-TMS-CORE validates credentials against the res.users model.
- Upon success, a session cookie is created and returned.
- Driver is redirected to their personalized portal dashboard.

## 1.11 Triggers

- Driver accesses the TMS login page.

## 1.12 Outcomes

- Driver gains access to the system.
- An active session is established for the driver.

## 1.13 Business Rules

- User authentication shall be handled by Odoo's built-in user management system (REQ-NFR-003).

## 1.14 Error Scenarios

- Invalid credentials are provided, and an error message is displayed.
- The user account is inactive.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-AF-014-IMPL

## 2.2 Name

Implementation: Driver Authentication via Mobile Portal using Odoo Session

## 2.3 Description

Technical sequence for a user with the 'Driver' role authenticating via the mobile-friendly web portal. The OWL frontend submits credentials to the standard Odoo JSON-RPC authentication endpoint. The Odoo backend validates credentials against the 'res.users' model, checks for active status and correct user group, and upon success, establishes a session by returning a secure, HttpOnly session cookie. This sequence adheres to Odoo's built-in session management as required by REQ-NFR-003.

## 2.4 Participants

### 2.4.1 UI Component

#### 2.4.1.1 Repository Id

REPO-DRV-UI

#### 2.4.1.2 Display Name

Driver Portal UI

#### 2.4.1.3 Type

🔹 UI Component

#### 2.4.1.4 Technology

Odoo Web Library (OWL) 2.0, JavaScript

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #1f77b4 |
| Stereotype | <<OWL Frontend>> |

### 2.4.2.0 Business Logic Layer

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

TMS Core (Odoo Backend)

#### 2.4.2.3 Type

🔹 Business Logic Layer

#### 2.4.2.4 Technology

Odoo 18, Python 3.11, PostgreSQL 16

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #ff7f0e |
| Stereotype | <<Odoo Monolith>> |

## 2.5.0.0 Interactions

### 2.5.1.0 Request

#### 2.5.1.1 Source Id

REPO-DRV-UI

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

POST /web/session/authenticate with credentials

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Request

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

200 OK with session data and 'Set-Cookie' header

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

##### 2.5.1.10.1 Protocol

HTTP/1.1

##### 2.5.1.10.2 Method

POST

##### 2.5.1.10.3 Parameters

| Property | Value |
|----------|-------|
| Schema | {'type': 'object', 'properties': {'jsonrpc': {'type': 'string', 'example': '2.0'}, 'method': {'type': 'string', 'example': 'call'}, 'params': {'type': 'object', 'properties': {'db': {'type': 'string'}, 'login': {'type': 'string', 'description': "User's email/username"}, 'password': {'type': 'string', 'description': "User's password"}}, 'required': ['db', 'login', 'password']}}} |

##### 2.5.1.10.4 Authentication

None (Public Endpoint)

##### 2.5.1.10.5 Error Handling

Returns a 200 OK with a JSON-RPC error object in the response body for authentication failures (e.g., invalid credentials, inactive user).

##### 2.5.1.10.6 Performance

###### 2.5.1.10.6.1 Slo

p95 latency < 500ms

###### 2.5.1.10.6.2 Notes

Authentication is a critical, high-frequency operation.

#### 2.5.1.11.0.0 Nested Interactions

##### 2.5.1.11.1.0 Internal Call

###### 2.5.1.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.1.3 Message

1a. Find user by login

###### 2.5.1.11.1.4 Sequence Number

1.1

###### 2.5.1.11.1.5 Type

🔹 Internal Call

###### 2.5.1.11.1.6 Is Synchronous

✅ Yes

###### 2.5.1.11.1.7 Return Message

User record or null

###### 2.5.1.11.1.8 Has Return

✅ Yes

###### 2.5.1.11.1.9 Is Activation

❌ No

###### 2.5.1.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | ORM |
| Method | res.users.search([('login', '=', login)]) |
| Parameters | Odoo domain filter |
| Authentication | N/A (Internal) |
| Error Handling | Handles cases where no user is found. |
| Performance | Query must be indexed on the 'login' column for fa... |

##### 2.5.1.11.2.0 Security Check

###### 2.5.1.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.2.3 Message

1b. [IF user found] Validate active status and 'Driver' role

###### 2.5.1.11.2.4 Sequence Number

1.2

###### 2.5.1.11.2.5 Type

🔹 Security Check

###### 2.5.1.11.2.6 Is Synchronous

✅ Yes

###### 2.5.1.11.2.7 Return Message

Validation result (pass/fail)

###### 2.5.1.11.2.8 Has Return

✅ Yes

###### 2.5.1.11.2.9 Is Activation

❌ No

###### 2.5.1.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Logic |
| Method | user._check_user_is_active_and_driver() |
| Parameters | User record object |
| Authentication | N/A (Internal) |
| Error Handling | If check fails, immediately short-circuit to retur... |
| Performance | In-memory check, negligible performance impact. |

##### 2.5.1.11.3.0 Security Check

###### 2.5.1.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.3.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.3.3 Message

1c. [IF valid user] Authenticate credentials

###### 2.5.1.11.3.4 Sequence Number

1.3

###### 2.5.1.11.3.5 Type

🔹 Security Check

###### 2.5.1.11.3.6 Is Synchronous

✅ Yes

###### 2.5.1.11.3.7 Return Message

Authenticated user ID or raises exception

###### 2.5.1.11.3.8 Has Return

✅ Yes

###### 2.5.1.11.3.9 Is Activation

❌ No

###### 2.5.1.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Logic |
| Method | res.users._login(db, login, password) |
| Parameters | Database name, login, password |
| Authentication | Verifies password against stored hash (e.g., PBKDF... |
| Error Handling | Raises 'AccessDenied' exception on password mismat... |
| Performance | Password hashing is CPU-intensive by design; monit... |

##### 2.5.1.11.4.0 Internal Call

###### 2.5.1.11.4.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.4.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.4.3 Message

1d. [IF authenticated] Create session

###### 2.5.1.11.4.4 Sequence Number

1.4

###### 2.5.1.11.4.5 Type

🔹 Internal Call

###### 2.5.1.11.4.6 Is Synchronous

✅ Yes

###### 2.5.1.11.4.7 Return Message

Session object

###### 2.5.1.11.4.8 Has Return

✅ Yes

###### 2.5.1.11.4.9 Is Activation

❌ No

###### 2.5.1.11.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Logic |
| Method | request.session.authenticate(db, login, password) |
| Parameters | DB, login, password |
| Authentication | N/A |
| Error Handling | Logs errors related to session store failures. |
| Performance | Requires fast access to session storage (e.g., Red... |

### 2.5.2.0.0.0 Client-Side Action

#### 2.5.2.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.2.2.0.0 Target Id

REPO-DRV-UI

#### 2.5.2.3.0.0 Message

On Success: Redirect to Driver Portal Dashboard (/my/home)

#### 2.5.2.4.0.0 Sequence Number

2

#### 2.5.2.5.0.0 Type

🔹 Client-Side Action

#### 2.5.2.6.0.0 Is Synchronous

❌ No

#### 2.5.2.7.0.0 Return Message



#### 2.5.2.8.0.0 Has Return

❌ No

#### 2.5.2.9.0.0 Is Activation

❌ No

#### 2.5.2.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Browser API |
| Method | window.location.href = '/my/home' |
| Parameters | Target URL |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Dependent on network and page load time of the das... |

### 2.5.3.0.0.0 Client-Side Action

#### 2.5.3.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.3.2.0.0 Target Id

REPO-DRV-UI

#### 2.5.3.3.0.0 Message

On Failure: Display 'Invalid Credentials' error message

#### 2.5.3.4.0.0 Sequence Number

3

#### 2.5.3.5.0.0 Type

🔹 Client-Side Action

#### 2.5.3.6.0.0 Is Synchronous

❌ No

#### 2.5.3.7.0.0 Return Message



#### 2.5.3.8.0.0 Has Return

❌ No

#### 2.5.3.9.0.0 Is Activation

❌ No

#### 2.5.3.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | DOM Manipulation |
| Method | updateErrorState(message) |
| Parameters | Error message from the server response payload |
| Authentication | N/A |
| Error Handling | Ensures the error message is clearly visible and a... |
| Performance | Immediate UI update. |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

The 'Set-Cookie' header returned on successful login is critical. It must have 'HttpOnly', 'Secure', and 'SameSite=Lax' (or 'Strict') attributes to mitigate XSS and CSRF attacks.

#### 2.6.1.2.0.0 Position

top_right

#### 2.6.1.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.1.4.0.0 Sequence Number

1

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

The UI must never display detailed error messages from the backend (e.g., 'User not found' vs 'Invalid password'). A generic 'Invalid login or password' message should be used to prevent username enumeration.

#### 2.6.2.2.0.0 Position

bottom_left

#### 2.6.2.3.0.0 Participant Id

REPO-DRV-UI

#### 2.6.2.4.0.0 Sequence Number

3

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Session Management: Odoo's default session managem... |
| Performance Targets | The entire authentication sequence (from POST requ... |
| Error Handling Strategy | Authentication failures (invalid password, inactiv... |
| Testing Considerations | Unit tests must cover the credential validation lo... |
| Monitoring Requirements | Prometheus metrics should be exported for: 'login_... |
| Deployment Considerations | The session storage mechanism (e.g., filesystem, R... |


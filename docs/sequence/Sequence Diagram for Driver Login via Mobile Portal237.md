sequenceDiagram
    participant "Driver Portal UI" as DriverPortalUI
    participant "TMS Core (Odoo Backend)" as TMSCoreOdooBackend

    activate TMSCoreOdooBackend
    DriverPortalUI->>TMSCoreOdooBackend: 1. POST /web/session/authenticate with credentials
    TMSCoreOdooBackend-->>DriverPortalUI: 200 OK with session data and 'Set-Cookie' header
    TMSCoreOdooBackend->>TMSCoreOdooBackend: 1.1. 1a. Find user by login
    TMSCoreOdooBackend-->>TMSCoreOdooBackend: User record or null
    TMSCoreOdooBackend->>TMSCoreOdooBackend: 1.2. 1b. [IF user found] Validate active status and 'Driver' role
    TMSCoreOdooBackend-->>TMSCoreOdooBackend: Validation result (pass/fail)
    TMSCoreOdooBackend->>TMSCoreOdooBackend: 1.3. 1c. [IF valid user] Authenticate credentials
    TMSCoreOdooBackend-->>TMSCoreOdooBackend: Authenticated user ID or raises exception
    TMSCoreOdooBackend->>TMSCoreOdooBackend: 1.4. 1d. [IF authenticated] Create session
    TMSCoreOdooBackend-->>TMSCoreOdooBackend: Session object
    DriverPortalUI->>DriverPortalUI: 2. On Success: Redirect to Driver Portal Dashboard (/my/home)
    DriverPortalUI->>DriverPortalUI: 3. On Failure: Display 'Invalid Credentials' error message

    note over TMSCoreOdooBackend: The 'Set-Cookie' header returned on successful login is critical. It must have 'HttpOnly', 'Secur...
    note over DriverPortalUI: The UI must never display detailed error messages from the backend (e.g., 'User not found' vs 'In...

    deactivate TMSCoreOdooBackend

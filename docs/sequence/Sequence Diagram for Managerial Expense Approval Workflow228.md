sequenceDiagram
    actor "Approver (User)" as ApproverUser
    participant "Odoo Notification Service" as OdooNotificationService
    participant "Odoo Notification Service" as OdooNotificationService
    participant "Odoo Notification Service" as OdooNotificationService
    participant "Odoo Notification Service" as OdooNotificationService

    activate OdooNotificationService
    ApproverUser->>OdooNotificationService: 1. 1. Navigates to Expense Approval view
    OdooNotificationService-->>ApproverUser: Displays list of expenses with 'Submitted' status
    OdooNotificationService->>OdooNotificationService: 1.1. 1.1. Request expense data
    OdooNotificationService-->>OdooNotificationService: List of expense records
    ApproverUser->>OdooNotificationService: 2. 2. Selects an expense to review details
    OdooNotificationService-->>ApproverUser: Displays expense form view with details and receipt
    ApproverUser->>OdooNotificationService: 3. 3a. Clicks 'Approve' button
    OdooNotificationService-->>ApproverUser: UI refreshes to show 'Approved' status
    OdooNotificationService->>OdooNotificationService: 3.1. 3.1. Invoke approval business logic
    OdooNotificationService-->>OdooNotificationService: Success/Failure
    ApproverUser->>OdooNotificationService: 4. 3b. Clicks 'Reject', enters mandatory reason, and submits
    OdooNotificationService-->>ApproverUser: UI refreshes to show 'Rejected' status
    OdooNotificationService->>OdooNotificationService: 4.1. 4.1. Invoke rejection business logic
    OdooNotificationService-->>OdooNotificationService: Success/Failure

    note over OdooNotificationService: Business Rule: Only expenses with state='approved' are included in trip profitability calculation...
    note over OdooNotificationService: Audit Trail: All state changes and posted messages (including rejection reasons) are automaticall...

    deactivate OdooNotificationService

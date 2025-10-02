sequenceDiagram
    actor "User (Admin)" as UserAdmin
    actor "Odoo Web Client" as OdooWebClient
    participant "TMS Core (Odoo Server)" as TMSCoreOdooServer
    participant "PostgreSQL Database" as PostgreSQLDatabase

    UserAdmin->>OdooWebClient: 1. 1. Modifies tracked field (e.g., 'amount_total') on Invoice form and clicks 'Save'
    activate TMSCoreOdooServer
    OdooWebClient->>TMSCoreOdooServer: 2. 2. RPC Call: execute_kw('account.move', 'write', [invoice_id], {'amount_total': new_value})
    TMSCoreOdooServer-->>OdooWebClient: 7. HTTP 200 OK Response with success status
    TMSCoreOdooServer->>TMSCoreOdooServer: 3. 3. Invoke ORM: account_move.write({'amount_total': new_value})
    TMSCoreOdooServer-->>TMSCoreOdooServer: ORM write operation successful
    TMSCoreOdooServer->>TMSCoreOdooServer: 3.1. 3.1. [mail.thread] Detect change on field with tracking=True
    TMSCoreOdooServer-->>TMSCoreOdooServer: List of changes detected
    TMSCoreOdooServer->>TMSCoreOdooServer: 3.2. 3.2. ORM Call: self.env['mail.message'].create(...)
    TMSCoreOdooServer-->>TMSCoreOdooServer: New mail.message record object
    activate PostgreSQLDatabase
    TMSCoreOdooServer->>PostgreSQLDatabase: 4. 4. Execute SQL Transaction
    PostgreSQLDatabase-->>TMSCoreOdooServer: 6. Transaction COMMIT successful
    OdooWebClient->>UserAdmin: 8. 8. Render updated Invoice view, displaying new value and audit log in chatter widget

    note over TMSCoreOdooServer: Implementation Detail: The audit trail is enabled by inheriting the mail.thread mixin in the Pyth...
    note over PostgreSQLDatabase: Compliance Requirement (REQ-DAT-008): The creation of the mail.message (audit log) and the update...

    deactivate PostgreSQLDatabase
    deactivate TMSCoreOdooServer

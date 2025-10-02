sequenceDiagram
    actor "User (Admin)" as UserAdmin
    participant "Odoo Web UI (Browser)" as OdooWebUIBrowser
    participant "TMS Core (Odoo Server)" as TMSCoreOdooServer
    participant "PostgreSQL Database" as PostgreSQLDatabase

    UserAdmin->>OdooWebUIBrowser: 1. 1. Fills 'New Vehicle' form with data (e.g., Truck Number, Model) and clicks 'Save'.
    activate TMSCoreOdooServer
    OdooWebUIBrowser->>TMSCoreOdooServer: 2. 2. [RPC] call('tms.vehicle', 'create', [vals])
    TMSCoreOdooServer-->>OdooWebUIBrowser: 8. [RPC Response] Success with new record ID OR Validation Error
    TMSCoreOdooServer->>TMSCoreOdooServer: 3. 3. Verify user has 'create' access rights for 'tms.vehicle' model.
    TMSCoreOdooServer-->>TMSCoreOdooServer: Access granted or denied.
    activate PostgreSQLDatabase
    TMSCoreOdooServer->>PostgreSQLDatabase: 4. 4. [SQL] SELECT 1 FROM tms_vehicle WHERE truck_number = $1
    PostgreSQLDatabase-->>TMSCoreOdooServer: 5. [SQL Result] Returns 0 rows (Unique) or 1 row (Duplicate).
    TMSCoreOdooServer->>PostgreSQLDatabase: 6. 6. [ALT: Success] [SQL] INSERT INTO tms_vehicle (truck_number, ...) VALUES ($1, ...)
    PostgreSQLDatabase-->>TMSCoreOdooServer: 7. [SQL Result] Commit successful, returns new record ID.
    TMSCoreOdooServer->>TMSCoreOdooServer: 6.1. 6a. [ALT: Failure] Raise ValidationError('Truck Number must be unique.')
    TMSCoreOdooServer-->>TMSCoreOdooServer: Error object is prepared for RPC response.
    OdooWebUIBrowser->>UserAdmin: 9. 9. [ALT: Success] Display success notification and redirect to the new vehicle's form view.
    OdooWebUIBrowser->>UserAdmin: 9.1. 9a. [ALT: Failure] Display validation error message next to the 'Truck Number' field.

    note over TMSCoreOdooServer: Business Rule BR-002 is enforced at two levels: programmatically by the SELECT query, and structu...

    deactivate PostgreSQLDatabase
    deactivate TMSCoreOdooServer

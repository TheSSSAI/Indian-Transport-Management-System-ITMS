sequenceDiagram
    actor "User Client (Browser)" as UserClientBrowser
    participant "Odoo ORM (Data Access)" as OdooORMDataAccess
    participant "Odoo ORM (Data Access)" as OdooORMDataAccess
    participant "Odoo ORM (Data Access)" as OdooORMDataAccess

    UserClientBrowser->>OdooORMDataAccess: 1. 1. GET /web/action/tms.financial_report_action
    OdooORMDataAccess-->>UserClientBrowser: 8. HTTP/1.1 403 Forbidden
    activate OdooORMDataAccess
    OdooORMDataAccess->>OdooORMDataAccess: 2. 2. Pre-fetch check: Controller invokes security check before accessing data.
    OdooORMDataAccess-->>OdooORMDataAccess: 7. Propagate AccessError exception
    OdooORMDataAccess->>OdooORMDataAccess: 3. 3. Security Layer receives request to check model-level access.
    OdooORMDataAccess-->>OdooORMDataAccess: 6. raise AccessError('...you are not allowed to access this document.')

    note over OdooORMDataAccess: Because the model-level access check (ir.model.access) fails, the system does not proceed to eval...
    note over OdooORMDataAccess: The ORM and the underlying PostgreSQL database are never touched during this interaction, prevent...

    deactivate OdooORMDataAccess

sequenceDiagram
    actor "User Browser" as UserBrowser
    participant "Odoo Controller" as OdooController
    participant "Odoo ORM / Models" as OdooORMModels
    participant "PostgreSQL Database" as PostgreSQLDatabase

    activate OdooController
    UserBrowser->>OdooController: 1. POST /report/tms/profitability
    OdooController-->>UserBrowser: HTTP 200 OK with report file
    OdooController->>OdooController: 2. validateRequest(auth, params)
    OdooController-->>OdooController: Validation status (success/fail)
    activate OdooORMModels
    OdooController->>OdooORMModels: 3. fetch_profitability_data(start_date, end_date)
    OdooORMModels-->>OdooController: List of aggregated data dictionaries
    activate PostgreSQLDatabase
    OdooORMModels->>PostgreSQLDatabase: 4. EXECUTE SQL Query for Aggregated Data
    PostgreSQLDatabase-->>OdooORMModels: Result Set (rows of aggregated data)
    PostgreSQLDatabase->>OdooORMModels: 5. Return Aggregated Data Rows
    OdooORMModels->>OdooController: 6. Return list of dicts
    OdooController->>OdooController: 7. calculateProfitability(data)
    OdooController-->>OdooController: Enriched data with 'profit' key
    OdooController->>OdooController: 8. renderReport(template_name, data)
    OdooController-->>OdooController: Binary content of the report file
    OdooController->>UserBrowser: 9. Return HTTP 200 OK with Report File

    note over OdooORMModels: Query Optimization is critical. Using a raw, optimized SQL query via env.cr.execute() is preferre...

    deactivate PostgreSQLDatabase
    deactivate OdooORMModels
    deactivate OdooController

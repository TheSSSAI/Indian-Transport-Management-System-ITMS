sequenceDiagram
    participant "Odoo Scheduler" as OdooScheduler
    participant "TMS Core Business Logic" as TMSCoreBusinessLogic
    participant "PostgreSQL Database" as PostgreSQLDatabase
    participant "Observability Platform" as ObservabilityPlatform

    activate TMSCoreBusinessLogic
    OdooScheduler->>TMSCoreBusinessLogic: 1. 1. Trigger Scheduled Action: _cron_check_document_expiries()
    TMSCoreBusinessLogic->>ObservabilityPlatform: 2. 2. Log Job Start
    activate PostgreSQLDatabase
    TMSCoreBusinessLogic->>PostgreSQLDatabase: 3. 3. Query for Active Driver Licenses Nearing Expiry
    PostgreSQLDatabase-->>TMSCoreBusinessLogic: 4. Return Driver Records
    TMSCoreBusinessLogic->>PostgreSQLDatabase: 5. 5. Query for Active Vehicle Documents Nearing Expiry
    PostgreSQLDatabase-->>TMSCoreBusinessLogic: 6. Return Vehicle Document Records
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 7. 7. Process records and build list of alerts to create
    TMSCoreBusinessLogic->>PostgreSQLDatabase: 8. 8. Create System Alert Records in Bulk
    PostgreSQLDatabase-->>TMSCoreBusinessLogic: 9. Acknowledge Creation
    TMSCoreBusinessLogic->>ObservabilityPlatform: 10. 10. Emit Operational Metrics
    TMSCoreBusinessLogic->>ObservabilityPlatform: 11. 11. Log Job Completion

    note over TMSCoreBusinessLogic: The entire process from step 2 to 11 is wrapped in a try/finally block to ensure that job complet...

    deactivate PostgreSQLDatabase
    deactivate TMSCoreBusinessLogic

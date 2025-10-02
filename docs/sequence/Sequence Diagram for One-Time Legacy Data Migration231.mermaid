sequenceDiagram
    participant "Migration Operator" as MigrationOperator
    participant "Legacy System DB" as LegacySystemDB
    participant "Python Migration Scripts" as PythonMigrationScripts
    participant "REPO-TMS-CORE (Staging)" as REPOTMSCOREStaging
    participant "REPO-TMS-CORE (Production)" as REPOTMSCOREProduction

    activate LegacySystemDB
    MigrationOperator->>LegacySystemDB: 1. 1. Extract Active Data to CSVs (as per REQ-TRN-002)
    LegacySystemDB-->>MigrationOperator: 2. Return CSV files (customers.csv, vehicles.csv, drivers.csv, open_invoices.csv)
    activate PythonMigrationScripts
    MigrationOperator->>PythonMigrationScripts: 3. 3. Execute Dry-Run Transformation
    PythonMigrationScripts-->>MigrationOperator: 9. Return Dry-Run Summary (Record Counts, Error Log)
    PythonMigrationScripts->>PythonMigrationScripts: 4. 4. Loop (for each row): Read, Cleanse, Validate, Transform to Odoo Schema
    activate REPOTMSCOREStaging
    PythonMigrationScripts->>REPOTMSCOREStaging: 5. 5. Load Transformed Data Batch
    REPOTMSCOREStaging-->>PythonMigrationScripts: 6. Return Batch Import Result (Success/Failure)
    MigrationOperator->>REPOTMSCOREStaging: 7. 7. Execute Post-Dry-Run Validation Checks
    REPOTMSCOREStaging-->>MigrationOperator: 8. Return Validation Results (Record Counts, Financial Totals)
    activate REPOTMSCOREProduction
    MigrationOperator->>REPOTMSCOREProduction: 10. 10. [During Cutover] Take DB Backup & Freeze Transactions
    REPOTMSCOREProduction-->>MigrationOperator: 11. Acknowledge Maintenance Mode
    MigrationOperator->>PythonMigrationScripts: 12. 12. Execute Production Migration
    PythonMigrationScripts-->>MigrationOperator: 14. Return Production-Run Summary
    PythonMigrationScripts->>REPOTMSCOREProduction: 13. 13. Load Transformed Data Batch to Production
    REPOTMSCOREProduction-->>PythonMigrationScripts: Return Batch Import Result (Success)
    MigrationOperator->>REPOTMSCOREProduction: 15. 15. Execute Final Post-Migration Validation
    REPOTMSCOREProduction-->>MigrationOperator: 16. Return Final Validation Results
    MigrationOperator->>REPOTMSCOREProduction: 17. 17. Disable Maintenance Mode & Enable User Access
    REPOTMSCOREProduction-->>MigrationOperator: 18. Acknowledge Go-Live

    note over PythonMigrationScripts: The Dry-Run phase (Steps 3-8) is mandatory and may be iterated multiple times to resolve all data...
    note over REPOTMSCOREProduction: The Production Migration (Steps 10-18) is a critical, time-sensitive operation. A failure at any ...

    deactivate REPOTMSCOREProduction
    deactivate REPOTMSCOREStaging
    deactivate PythonMigrationScripts
    deactivate LegacySystemDB

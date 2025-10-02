sequenceDiagram
    participant "SRE (Site Reliability Engineer)" as SRESiteReliabilityEngineer
    participant "Prometheus / Alertmanager" as PrometheusAlertmanager
    participant "TMS Application (Odoo)" as TMSApplicationOdoo
    participant "Amazon EKS Control Plane" as AmazonEKSControlPlane
    participant "AWS Secrets Manager" as AWSSecretsManager
    participant "Primary RDS DB (Corrupted)" as PrimaryRDSDBCorrupted
    participant "AWS Management Console" as AWSManagementConsole
    participant "Restored RDS DB" as RestoredRDSDB

    activate SRESiteReliabilityEngineer
    PrometheusAlertmanager->>SRESiteReliabilityEngineer: 1. Fire Critical Alert: 'Data Corruption Detected' or 'High DB Error Rate'
    SRESiteReliabilityEngineer->>AmazonEKSControlPlane: 2. Enable Maintenance Mode (e.g., apply config map, scale down deployment)
    AmazonEKSControlPlane-->>SRESiteReliabilityEngineer: Deployment scaled / ConfigMap applied
    activate AWSManagementConsole
    SRESiteReliabilityEngineer->>AWSManagementConsole: 3. Initiate 'Restore to point in time'
    AWSManagementConsole-->>SRESiteReliabilityEngineer: Restore configuration UI
    activate PrimaryRDSDBCorrupted
    AWSManagementConsole->>PrimaryRDSDBCorrupted: 4. aws rds restore-db-instance-to-point-in-time
    PrimaryRDSDBCorrupted-->>AWSManagementConsole: Restore task initiated
    activate RestoredRDSDB
    PrimaryRDSDBCorrupted->>RestoredRDSDB: 5. Provision & Restore Data from Snapshots and Transaction Logs
    RestoredRDSDB->>AWSManagementConsole: 6. Status: 'Available'
    SRESiteReliabilityEngineer->>RestoredRDSDB: 7. Execute Data Validation Script
    RestoredRDSDB-->>SRESiteReliabilityEngineer: Validation Result (OK / FAILED)
    activate AWSSecretsManager
    SRESiteReliabilityEngineer->>AWSSecretsManager: 8. Update Database Connection Secret
    AWSSecretsManager-->>SRESiteReliabilityEngineer: Secret updated successfully
    activate AmazonEKSControlPlane
    SRESiteReliabilityEngineer->>AmazonEKSControlPlane: 9. Trigger Rolling Restart of Application Deployment
    AmazonEKSControlPlane-->>SRESiteReliabilityEngineer: Deployment restart triggered
    activate TMSApplicationOdoo
    AmazonEKSControlPlane->>TMSApplicationOdoo: 10. Create New Pods; Pods fetch new secret
    TMSApplicationOdoo->>RestoredRDSDB: 11. Establish Connection Pool
    RestoredRDSDB-->>TMSApplicationOdoo: Connection successful
    SRESiteReliabilityEngineer->>TMSApplicationOdoo: 12. Perform Smoke Tests on Application
    TMSApplicationOdoo-->>SRESiteReliabilityEngineer: Smoke Tests Passed
    SRESiteReliabilityEngineer->>AmazonEKSControlPlane: 13. Disable Maintenance Mode
    AmazonEKSControlPlane-->>SRESiteReliabilityEngineer: Maintenance mode disabled

    note over PrimaryRDSDBCorrupted: Data loss is possible for transactions occurring between the last backup and the restore point. R...
    note over SRESiteReliabilityEngineer: Validation is the most critical manual step. The script must be comprehensive to ensure business ...

    deactivate TMSApplicationOdoo
    deactivate AmazonEKSControlPlane
    deactivate AWSSecretsManager
    deactivate RestoredRDSDB
    deactivate PrimaryRDSDBCorrupted
    deactivate AWSManagementConsole
    deactivate SRESiteReliabilityEngineer

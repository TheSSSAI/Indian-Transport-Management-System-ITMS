sequenceDiagram
    actor "User (Finance Officer)" as UserFinanceOfficer
    participant "TMS Core (Odoo Addon)" as TMSCoreOdooAddon
    participant "AWS Secrets Manager" as AWSSecretsManager
    participant "External GSP API" as ExternalGSPAPI
    participant "Odoo Job Queue" as OdooJobQueue
    participant "Odoo Notification Service" as OdooNotificationService

    activate TMSCoreOdooAddon
    UserFinanceOfficer->>TMSCoreOdooAddon: 1. 1. Triggers 'Generate E-Invoice' action for a 'Completed' trip.
    TMSCoreOdooAddon-->>UserFinanceOfficer: Returns immediate UI feedback (success, queued, or error).
    TMSCoreOdooAddon->>TMSCoreOdooAddon: 2. 2. Validates preconditions: Trip status is 'Completed' and invoice contains all required fields (e.g., GSTIN).
    TMSCoreOdooAddon-->>TMSCoreOdooAddon: Validation success or raises ValidationError.
    TMSCoreOdooAddon->>AWSSecretsManager: 3. 3. Retrieves GSP API Key from secure storage.
    AWSSecretsManager-->>TMSCoreOdooAddon: Returns secret string containing the API key.
    AWSSecretsManager->>TMSCoreOdooAddon: 4. 4. Returns GSP API Key.
    TMSCoreOdooAddon->>TMSCoreOdooAddon: 5. 5. Transforms Odoo invoice record into the required GSP JSON format.
    TMSCoreOdooAddon-->>TMSCoreOdooAddon: Returns JSON-serializable Python dictionary.
    activate ExternalGSPAPI
    TMSCoreOdooAddon->>ExternalGSPAPI: 6. 6. [Sync Attempt] Submits e-invoice generation request.
    ExternalGSPAPI-->>TMSCoreOdooAddon: Returns HTTP status and JSON response.
    ExternalGSPAPI->>TMSCoreOdooAddon: 7. 7. [Success Path] Responds with 200 OK and IRN.
    TMSCoreOdooAddon->>TMSCoreOdooAddon: 8. 8. [Success Path] Persists IRN and updates invoice & trip status.
    TMSCoreOdooAddon->>UserFinanceOfficer: 9. 9. [Success Path] Displays success message and updated invoice status in UI.
    ExternalGSPAPI->>TMSCoreOdooAddon: 10. 7a. [Failure Path] Responds with 5xx error or times out.
    activate OdooJobQueue
    TMSCoreOdooAddon->>OdooJobQueue: 11. 8a. [Failure Path] Enqueues background job for async processing.
    TMSCoreOdooAddon->>UserFinanceOfficer: 12. 9a. [Failure Path] Displays message: 'E-invoice queued for background processing.'
    OdooJobQueue->>TMSCoreOdooAddon: 13. 10. [Async Path] Executes job from queue.
    TMSCoreOdooAddon-->>OdooJobQueue: Job completion status.
    TMSCoreOdooAddon->>ExternalGSPAPI: 14. 11. [Async Path] Retries e-invoice generation request.
    ExternalGSPAPI-->>TMSCoreOdooAddon: Returns HTTP status and JSON response.
    ExternalGSPAPI->>TMSCoreOdooAddon: 15. 12. [Async Success] Responds with 200 OK and IRN.
    activate OdooNotificationService
    TMSCoreOdooAddon->>OdooNotificationService: 16. 13. [Async Success] Sends success notification to user.
    ExternalGSPAPI->>TMSCoreOdooAddon: 17. 12a. [Async Failure] Responds with 400 Bad Request after all retries.
    TMSCoreOdooAddon->>TMSCoreOdooAddon: 18. 13a. [Async Failure] Marks invoice for manual intervention.
    TMSCoreOdooAddon->>OdooNotificationService: 19. 14a. [Async Failure] Sends high-priority failure alert to user.

    note over TMSCoreOdooAddon: Data Transformation Logic (Step 5): Maps fields from Odoo models (account.move, res.partner, acco...
    note over OdooJobQueue: Background Job Retry Policy (Step 8a): Configured with 5 retries. Delays: 5m, 15m, 1h, 4h, 12h. T...

    deactivate OdooNotificationService
    deactivate OdooJobQueue
    deactivate ExternalGSPAPI
    deactivate TMSCoreOdooAddon

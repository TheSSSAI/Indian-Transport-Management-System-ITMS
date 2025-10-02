sequenceDiagram
    participant "Dispatch Manager" as DispatchManager
    participant "Odoo Data Access Layer (ORM/DB)" as OdooDataAccessLayerORMDB
    participant "Odoo Data Access Layer (ORM/DB)" as OdooDataAccessLayerORMDB
    participant "Odoo Data Access Layer (ORM/DB)" as OdooDataAccessLayerORMDB

    activate OdooDataAccessLayerORMDB
    DispatchManager->>OdooDataAccessLayerORMDB: 1. 1. User, having identified an 'On Hold' trip from the dashboard, clicks the 'Resume Trip' button on the Trip form view.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 2. 2. Renders and displays an OWL-based wizard/modal, prompting for a mandatory 'Resolution Comment'.
    DispatchManager->>OdooDataAccessLayerORMDB: 3. 3. Enters resolution comment and clicks 'Confirm'.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 4. 4. Executes Odoo model method action_resume_trip via JSON-RPC call.
    OdooDataAccessLayerORMDB-->>OdooDataAccessLayerORMDB: 13. Odoo Action dictionary for UI refresh or success/error notification.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 5. 5. [Security Checkpoint] Verify user role.
    OdooDataAccessLayerORMDB-->>OdooDataAccessLayerORMDB: Success or AccessError exception.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 6. 6. [Business Rule] Validate mandatory comment.
    OdooDataAccessLayerORMDB-->>OdooDataAccessLayerORMDB: Success or ValidationError exception.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 7. 7. Initiate database transaction.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 8. 8. Update trip status via ORM.
    OdooDataAccessLayerORMDB-->>OdooDataAccessLayerORMDB: 10. DB operation successful.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 9. 9. [Audit Trail] Post resolution comment to trip's chatter.
    OdooDataAccessLayerORMDB-->>OdooDataAccessLayerORMDB: 11. DB operation successful.
    OdooDataAccessLayerORMDB->>OdooDataAccessLayerORMDB: 12. 12. Commit transaction.
    OdooDataAccessLayerORMDB->>DispatchManager: 14. 14. UI closes the modal and refreshes the trip form, displaying the new 'In-Transit' status and the new comment in the history.

    note over OdooDataAccessLayerORMDB: This entire business process (steps 5-12) MUST be executed within a single, atomic database trans...
    note over OdooDataAccessLayerORMDB: The check has_group is critical for enforcing the separation of duties outlined in REQ-FNC-001 an...

    deactivate OdooDataAccessLayerORMDB

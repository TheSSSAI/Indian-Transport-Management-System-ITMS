sequenceDiagram
    actor "Driver (User)" as DriverUser
    participant "Odoo Driver Portal (OWL)" as OdooDriverPortalOWL
    participant "Odoo Core Business Logic" as OdooCoreBusinessLogic
    participant "Amazon S3" as AmazonS3

    DriverUser->>OdooDriverPortalOWL: 1. 1. Fills expense form (Type, Amount, Odometer) and selects receipt file.
    OdooDriverPortalOWL->>OdooDriverPortalOWL: 2. 2. Perform client-side validation (file type, size, required fields).
    OdooDriverPortalOWL-->>OdooDriverPortalOWL: Validation result (pass/fail).
    activate OdooDriverPortalOWL
    DriverUser->>OdooDriverPortalOWL: 3. 3. Taps 'Submit' button.
    activate OdooCoreBusinessLogic
    OdooDriverPortalOWL->>OdooCoreBusinessLogic: 4. 4. Request pre-signed URL for receipt upload.
    OdooCoreBusinessLogic-->>OdooDriverPortalOWL: HTTP 200 OK with pre-signed URL data or HTTP 400 with validation error.
    OdooCoreBusinessLogic->>OdooCoreBusinessLogic: 5. 4a. Validate file metadata against business rules (type, size).
    OdooCoreBusinessLogic-->>OdooCoreBusinessLogic: Validation result.
    OdooCoreBusinessLogic->>AmazonS3: 6. 4b. Generate pre-signed POST URL using AWS SDK.
    AmazonS3-->>OdooCoreBusinessLogic: Pre-signed URL object.
    OdooDriverPortalOWL->>AmazonS3: 7. 5. Upload receipt file directly using pre-signed URL.
    AmazonS3-->>OdooDriverPortalOWL: HTTP 204 No Content (on success) or S3 error response.
    OdooDriverPortalOWL->>OdooCoreBusinessLogic: 8. 6. Submit final expense data with S3 file key.
    OdooCoreBusinessLogic-->>OdooDriverPortalOWL: HTTP 201 Created with new expense ID, or HTTP 400 with validation errors.
    OdooCoreBusinessLogic->>OdooCoreBusinessLogic: 9. 6a. Perform server-side validation (BR-009).
    OdooCoreBusinessLogic->>OdooCoreBusinessLogic: 10. Query database for last recorded odometer for the vehicle.
    OdooCoreBusinessLogic-->>OdooCoreBusinessLogic: Last odometer value.
    OdooCoreBusinessLogic->>OdooCoreBusinessLogic: 11. Compare submitted odometer > last recorded odometer.
    OdooCoreBusinessLogic-->>OdooCoreBusinessLogic: Validation result.
    OdooCoreBusinessLogic->>OdooCoreBusinessLogic: 12. 7. Create tms.expense record in 'Submitted' state.
    OdooCoreBusinessLogic-->>OdooCoreBusinessLogic: New record object.
    OdooDriverPortalOWL->>DriverUser: 13. 8. Display success confirmation to user.

    note over OdooCoreBusinessLogic: Server-side validation is critical and serves as the ultimate source of truth, even if client-sid...

    deactivate OdooCoreBusinessLogic
    deactivate OdooDriverPortalOWL

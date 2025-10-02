sequenceDiagram
    participant "Dispatch Manager" as DispatchManager
    participant "Driver" as Driver
    participant "Finance Officer" as FinanceOfficer
    participant "Driver Portal UI (OWL)" as DriverPortalUIOWL
    participant "TMS Core Business Logic" as TMSCoreBusinessLogic

    activate TMSCoreBusinessLogic
    DispatchManager->>TMSCoreBusinessLogic: 1. 1. createTrip(vals: dict)
    TMSCoreBusinessLogic-->>DispatchManager: Returns new trip record ID
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 1.1. 1.1. Validate required fields per BR-006 (Customer, Source, Destination).
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 1.2. 1.2. Create tms.trip record with state = 'Planned'.
    TMSCoreBusinessLogic-->>TMSCoreBusinessLogic: new_trip_id
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 1.3. 1.3. Create audit trail entry for 'Trip Created'.
    DispatchManager->>TMSCoreBusinessLogic: 2. 2. assignVehicleAndDriver(trip_id, vehicle_id, driver_id)
    TMSCoreBusinessLogic-->>DispatchManager: Returns success status
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 2.1. 2.1. Validate vehicle capacity against trip weight (BR-007).
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 2.2. 2.2. Validate driver's license expiry date (BR-003).
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 2.3. 2.3. [State Transition] Update tms.trip record state from 'Planned' to 'Assigned'.
    activate DriverPortalUIOWL
    Driver->>DriverPortalUIOWL: 3. 3. Taps 'Start Trip' button
    DriverPortalUIOWL->>TMSCoreBusinessLogic: 4. 4. startTrip(trip_id)
    TMSCoreBusinessLogic-->>DriverPortalUIOWL: Returns success status
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 4.1. 4.1. [State Transition] Update tms.trip state from 'Assigned' to 'In-Transit'.
    Driver->>DriverPortalUIOWL: 5. 5. Uploads Proof of Delivery (POD)
    DriverPortalUIOWL->>TMSCoreBusinessLogic: 6. 6. submitPOD(trip_id, pod_file, recipient_name)
    TMSCoreBusinessLogic-->>DriverPortalUIOWL: Returns success status
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 6.1. 6.1. Upload pod_file to Amazon S3 and create ir.attachment record.
    TMSCoreBusinessLogic-->>TMSCoreBusinessLogic: s3_url
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 6.2. 6.2. [State Transition] Update tms.trip state from 'In-Transit' to 'Delivered'.
    DispatchManager->>TMSCoreBusinessLogic: 7. 7. completeTrip(trip_id)
    TMSCoreBusinessLogic-->>DispatchManager: Returns success status
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 7.1. 7.1. [State Transition] Update tms.trip state from 'Delivered' to 'Completed'.
    FinanceOfficer->>TMSCoreBusinessLogic: 8. 8. generateInvoice(trip_id)
    TMSCoreBusinessLogic-->>FinanceOfficer: Returns new invoice record ID
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 8.1. 8.1. Validate trip state is 'Completed' (BR-010).
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 8.2. 8.2. Create account.move record from trip data.
    TMSCoreBusinessLogic-->>TMSCoreBusinessLogic: invoice_id
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 8.3. 8.3. [State Transition] Update tms.trip state from 'Completed' to 'Invoiced'.
    FinanceOfficer->>TMSCoreBusinessLogic: 9. 9. recordPayment(invoice_id, payment_data)
    TMSCoreBusinessLogic-->>FinanceOfficer: Returns success status
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 9.1. 9.1. Reconcile payment and update invoice payment_state.
    TMSCoreBusinessLogic->>TMSCoreBusinessLogic: 9.2. 9.2. IF all invoices for trip are paid, [State Transition] update tms.trip state from 'Invoiced' to 'Paid'.

    note over TMSCoreBusinessLogic: All state transitions and critical financial operations (invoice/payment creation) must generate ...

    deactivate DriverPortalUIOWL
    deactivate TMSCoreBusinessLogic

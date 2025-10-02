sequenceDiagram
    actor "Driver (User)" as DriverUser
    participant "Driver Portal UI (OWL)" as DriverPortalUIOWL
    participant "TMS Core (Odoo Controller)" as TMSCoreOdooController
    participant "Amazon S3" as AmazonS3

    activate DriverPortalUIOWL
    DriverUser->>DriverPortalUIOWL: 1. 1. Tap 'Help & Training' menu item.
    DriverPortalUIOWL->>DriverPortalUIOWL: 2. 2. Mount 'TrainingMaterials' OWL component and display loading state.
    activate TMSCoreOdooController
    DriverPortalUIOWL->>TMSCoreOdooController: 3. 3. Fetch training materials list.
    TMSCoreOdooController-->>DriverPortalUIOWL: 4. Return JSON list of materials or empty list.
    TMSCoreOdooController->>TMSCoreOdooController: 3.1. 3.1. Query for active training materials.
    TMSCoreOdooController-->>TMSCoreOdooController: Return list of tms.training.material records.
    DriverPortalUIOWL->>DriverPortalUIOWL: 5. 5. Update state and render list of materials or 'No materials' message.
    DriverUser->>DriverPortalUIOWL: 6. 6. Tap on a video tutorial item.
    DriverPortalUIOWL->>DriverPortalUIOWL: 7. 7. Render HTML5 video player component with S3 URL.
    activate AmazonS3
    DriverPortalUIOWL->>AmazonS3: 8. 8. Browser requests video stream.
    AmazonS3-->>DriverPortalUIOWL: 9. Stream video data chunks.
    DriverPortalUIOWL->>DriverUser: 10. 10. Play video for the driver.

    note over DriverPortalUIOWL: AC-005 & AC-006: Error handling for 'No Materials' is implemented in step 5 by the UI. Error hand...
    note over TMSCoreOdooController: REQ-TRN-003: The controller in step 3.1 is responsible for fetching the URLs for both video tutor...

    deactivate AmazonS3
    deactivate TMSCoreOdooController
    deactivate DriverPortalUIOWL

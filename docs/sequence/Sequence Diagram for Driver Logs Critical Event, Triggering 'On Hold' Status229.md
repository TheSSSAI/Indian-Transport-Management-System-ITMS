sequenceDiagram
    participant "Driver Portal UI (Browser/OWL Component)" as DriverPortalUIBrowserOWLComponent
    participant "TMS Core Backend" as TMSCoreBackend
    participant "Amazon S3" as AmazonS3

    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 1. User with 'Driver' role taps 'Help & Training' navigation item.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 2. Navigate to Training Materials view. Set component state to 'loading' and render a loading indicator (e.g., spinner).
    activate TMSCoreBackend
    DriverPortalUIBrowserOWLComponent->>TMSCoreBackend: 3. Asynchronously fetch list of available training materials.
    TMSCoreBackend-->>DriverPortalUIBrowserOWLComponent: Returns 200 OK with JSON array of training materials or an empty array if none exist. Returns 403/500 on error.
    TMSCoreBackend->>TMSCoreBackend: 3.1. Verify user session and check if user has 'Driver' role using request.env.user.has_group('tms_management.group_tms_driver').
    TMSCoreBackend-->>TMSCoreBackend: Proceeds on success, returns 403 Forbidden on failure.
    TMSCoreBackend->>TMSCoreBackend: 3.2. Query tms.training.material model for all active records. search_read([('active', '=', True)], ['title', 'type', 'url'])
    TMSCoreBackend-->>TMSCoreBackend: Returns a list of Odoo record objects.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 4. On API success, process response. If data array is not empty, set state to 'loaded'. If empty, set state to 'empty'.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 5. Render view based on state: Display list of material cards/links for 'loaded' state, or 'No materials available' message for 'empty' state. Hide loading indicator.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 6. User taps on a video tutorial item.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 7. Render an embedded HTML5 <video> player within the component, setting the src attribute to the material's S3 URL.
    activate AmazonS3
    DriverPortalUIBrowserOWLComponent->>AmazonS3: 8. Browser initiates an HTTP GET request to stream the video content from the provided S3 URL.
    AmazonS3-->>DriverPortalUIBrowserOWLComponent: Returns video stream chunk by chunk.
    DriverPortalUIBrowserOWLComponent->>DriverPortalUIBrowserOWLComponent: 9. User taps on the Quick-Reference Guide (QRG) link.
    DriverPortalUIBrowserOWLComponent->>AmazonS3: 10. Browser opens a new tab and initiates an HTTP GET request to download/display the PDF from the S3 URL.
    AmazonS3-->>DriverPortalUIBrowserOWLComponent: Returns PDF content.

    note over DriverPortalUIBrowserOWLComponent: Error Handling: If the API call at step 3 fails (e.g., network error, 500 response), the UI compo...

    deactivate AmazonS3
    deactivate TMSCoreBackend

# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-048 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver views and downloads documents for their cur... |
| As A User Story | As a Driver, I want to easily view and download al... |
| User Persona | Driver: Field user accessing the system via a mobi... |
| Business Value | Enhances on-road compliance, reduces the risk of f... |
| Functional Area | Driver Portal |
| Story Theme | Trip Execution & Compliance |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful viewing and downloading of vehicle documents

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

a Driver is logged into the portal and is assigned to an active trip with a specific vehicle

### 3.1.5 When

the Driver navigates to the 'Vehicle Documents' section for their current trip

### 3.1.6 Then

the system displays a list of all documents associated with that vehicle, showing the 'Document Type' and 'Expiry Date' for each, and provides options to both view and download each document.

### 3.1.7 Validation Notes

Verify that clicking 'view' opens the document in the browser and 'download' saves the file to the device. Test with PDF, JPG, and PNG file types.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Display of expired vehicle documents

### 3.2.3 Scenario Type

Edge_Case

### 3.2.4 Given

a Driver is viewing the document list for their assigned vehicle

### 3.2.5 And

one of the documents (e.g., 'Insurance') has an expiry date in the past

### 3.2.6 When

the document list is displayed

### 3.2.7 Then

the expired document is clearly and visually distinguished from valid documents (e.g., using red text, an 'Expired' label, or an icon).

### 3.2.8 Validation Notes

Ensure the visual indicator is clear and meets accessibility contrast requirements.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Vehicle has no documents uploaded

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

a Driver is assigned to a trip with a vehicle for which no documents have been uploaded

### 3.3.5 When

the Driver navigates to the 'Vehicle Documents' section

### 3.3.6 Then

the system displays a user-friendly message, such as 'No documents are available for this vehicle.'

### 3.3.7 Validation Notes

Confirm that the page does not show an error and the message is clear.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Driver has no active trip assigned

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

a Driver is logged into the portal but is not currently assigned to an active trip

### 3.4.5 When

the Driver views their main portal dashboard

### 3.4.6 Then

the option to view vehicle documents is not visible or is disabled, preventing access.

### 3.4.7 Validation Notes

Check the main driver portal view to ensure the UI reflects this state correctly.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Security check for unauthorized document access

### 3.5.3 Scenario Type

Security

### 3.5.4 Given

a Driver is assigned to a trip with Vehicle 'A'

### 3.5.5 And

Vehicle 'B' exists in the system with its own documents

### 3.5.6 When

the Driver attempts to access the documents for Vehicle 'B' through any means (e.g., manipulating a URL parameter)

### 3.5.7 Then

the system must deny access and return an authorization error.

### 3.5.8 Validation Notes

This requires a specific security test to ensure the record rules are correctly isolating data.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A button or link within the current trip view labeled 'Vehicle Documents'.
- A list view to display documents, with columns for 'Document Type' and 'Expiry Date'.
- Intuitive icons for 'View' and 'Download' actions for each document.
- A clear visual indicator for expired documents.
- A message area for displaying 'No documents available' or other informational texts.

## 4.2.0 User Interactions

- Tapping a document's 'View' icon opens it in a new browser tab or a modal viewer.
- Tapping a document's 'Download' icon initiates a file download to the user's device.
- The interface must be responsive and optimized for mobile touch interaction with large tap targets.

## 4.3.0 Display Requirements

- The document list must be sorted logically, for example, by expiry date (soonest first) or alphabetically by type.
- Expiry dates should be displayed in a clear, unambiguous format (e.g., DD-MMM-YYYY).

## 4.4.0 Accessibility Needs

- Must comply with WCAG 2.1 Level AA standards as per REQ-INT-001.
- Color contrast for expired document indicators must be sufficient for users with color vision deficiencies.
- All interactive elements (buttons, links) must have accessible names for screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-SEC-01', 'rule_description': "A user with the 'Driver' role can only access documents for the vehicle they are actively assigned to for a current trip ('Assigned' or 'In-Transit' status).", 'enforcement_point': 'Server-side API and database query level.', 'violation_handling': "The system will return a '403 Forbidden' or equivalent authorization error."}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-009

#### 6.1.1.2 Dependency Reason

Functionality to attach documents to vehicle records must exist before they can be viewed.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

The system must support the concept of assigning a driver and vehicle to a trip.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-047

#### 6.1.3.2 Dependency Reason

A view for the driver's current trip is required to host the link to the vehicle documents.

## 6.2.0.0 Technical Dependencies

- Odoo's security model, specifically `ir.rule` for enforcing row-level security.
- Odoo's attachment model (`ir.attachment`) for storing document metadata.
- Integration with Amazon S3 for file storage and retrieval, as per REQ-DEP-001. Secure, pre-signed URLs should be used for access.

## 6.3.0.0 Data Dependencies

- Requires vehicle records to exist in the system.
- Requires document files (e.g., PDF, JPG) to be uploaded and associated with vehicle records.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The document list should load in under 3 seconds on a 3G mobile connection.
- Document downloads should initiate within 2 seconds of the user's request.

## 7.2.0.0 Security

- Access to documents must be strictly controlled by the business rule BR-SEC-01.
- File access should be granted via secure, time-limited, pre-signed URLs to prevent unauthorized sharing or access.
- All data transmission must be over HTTPS.

## 7.3.0.0 Usability

- The interface must be intuitive for non-technical users on a mobile device.
- The process to find and download a document should require no more than 3 taps after logging in and selecting the current trip.

## 7.4.0.0 Accessibility

- Adherence to WCAG 2.1 Level AA is mandatory.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of Chrome and Safari on both iOS and Android mobile devices.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- The primary complexity lies in correctly implementing the server-side Odoo record rule (`ir.rule`) to enforce strict data access control. This requires a deep understanding of Odoo's ORM and security layers.
- Generating secure, pre-signed S3 URLs for document access adds a layer of backend logic.
- Ensuring a seamless and robust user experience for file viewing/downloading across different mobile browsers can be challenging.

## 8.3.0.0 Technical Risks

- An incorrectly implemented security rule could lead to a data leak, allowing drivers to see documents for other vehicles.
- Performance of the document list query if the number of trips or documents becomes very large.

## 8.4.0.0 Integration Points

- Odoo `hr.employee`, `tms.trip`, `tms.vehicle`, and `ir.attachment` models.
- Amazon S3 API for retrieving file objects.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security
- Usability

## 9.2.0.0 Test Scenarios

- Verify a driver can view/download documents for their assigned vehicle.
- Verify an expired document is correctly flagged in the UI.
- Verify a driver CANNOT access documents for a vehicle not assigned to them (negative security test).
- Verify the 'no documents' message appears when appropriate.
- Verify the feature is hidden/disabled when the driver has no active trip.
- Test on physical mobile devices (iOS and Android) with both Wi-Fi and cellular data.

## 9.3.0.0 Test Data Needs

- A test user with the 'Driver' role.
- At least two vehicle records.
- One vehicle with multiple valid documents (PDF, JPG).
- One vehicle with at least one expired document.
- One vehicle with no documents.
- An active trip assigning the test driver to one of the vehicles.

## 9.4.0.0 Testing Tools

- Pytest for backend unit/integration tests.
- Browser developer tools for frontend and responsiveness testing.
- A test automation framework (e.g., Selenium, Playwright) for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in the staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit tests covering the security rule and data retrieval logic are implemented and achieve >80% coverage.
- Automated E2E tests for the happy path and the negative security scenario are passing.
- UI/UX has been reviewed and approved by the product owner, confirming mobile-friendliness.
- Security review confirms that the access control mechanism is robust.
- Feature documentation for the User Manual is updated.
- Story is deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is critical for driver-side adoption and compliance. It should be prioritized early in the development of the Driver Portal.
- Requires close collaboration between a backend developer (for the security rule and S3 integration) and a frontend developer (for the OWL component).

## 11.4.0.0 Release Impact

This is a core feature for the Driver Portal and is essential for the initial release to drivers.


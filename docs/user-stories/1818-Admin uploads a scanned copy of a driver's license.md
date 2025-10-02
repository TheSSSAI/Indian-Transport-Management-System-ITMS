# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-013 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin uploads a scanned copy of a driver's license |
| As A User Story | As an Admin, I want to upload a scanned copy of a ... |
| User Persona | Admin user responsible for managing master data an... |
| Business Value | Centralizes critical compliance documents, improve... |
| Functional Area | Master Data Management |
| Story Theme | Driver Master Data |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful upload of a valid license file (Image)

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am on the form view of an existing driver record

### 3.1.5 When

I click the 'Upload License' field and select a valid image file (JPG or PNG) that is under 5MB

### 3.1.6 Then

The file upload is successful, a success notification is shown, and a thumbnail of the license image is displayed in the designated field on the driver's form.

### 3.1.7 Validation Notes

Verify the file appears in the UI. Check the underlying `ir.attachment` record and confirm it is stored in the configured Amazon S3 bucket.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Successful upload of a valid license file (PDF)

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am logged in as an Admin and am on the form view of an existing driver record

### 3.2.5 When

I click the 'Upload License' field and select a valid PDF file that is under 5MB

### 3.2.6 Then

The file upload is successful, a success notification is shown, and a placeholder icon for the PDF file is displayed in the designated field, along with the filename.

### 3.2.7 Validation Notes

Verify the PDF icon and filename appear. Clicking it should allow downloading or viewing the PDF.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to upload a file with an unsupported format

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am logged in as an Admin and am on the form view of an existing driver record

### 3.3.5 When

I attempt to upload a file with an unsupported extension, such as .docx or .zip

### 3.3.6 Then

The system rejects the upload and displays a user-friendly error message stating 'Invalid file type. Please upload a JPG, PNG, or PDF file.'

### 3.3.7 Validation Notes

Test with multiple invalid file types (.txt, .xlsx, .exe) to ensure the validation is robust.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to upload a file exceeding the size limit

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am logged in as an Admin and am on the form view of an existing driver record

### 3.4.5 When

I attempt to upload a valid file type (e.g., JPG) that is larger than 5MB

### 3.4.6 Then

The system rejects the upload and displays a user-friendly error message stating 'File size exceeds the 5MB limit.'

### 3.4.7 Validation Notes

Create a dummy file of ~6MB to test this scenario.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Replace an existing license file

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am an Admin on a driver record that already has a license file uploaded

### 3.5.5 When

I use the upload functionality again to select a new, valid file

### 3.5.6 Then

The new file successfully replaces the old one, and the new file's thumbnail or icon is displayed.

### 3.5.7 Validation Notes

Verify in the S3 bucket that the old attachment is removed or superseded and the new one is present.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

View or download the uploaded license

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A driver record has a license file successfully uploaded

### 3.6.5 When

I click on the file's thumbnail or icon

### 3.6.6 Then

The file is opened in a new browser tab for viewing or a download is initiated, allowing me to access the stored document.

### 3.6.7 Validation Notes

Confirm that the downloaded file is intact and matches the originally uploaded file.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Remove an existing license file

### 3.7.3 Scenario Type

Alternative_Flow

### 3.7.4 Given

A driver record has a license file successfully uploaded

### 3.7.5 When

I click the 'clear' or 'delete' control associated with the file upload field

### 3.7.6 Then

The file is removed from the driver's record, and the field reverts to its empty state (e.g., showing the 'Upload License' prompt).

### 3.7.7 Validation Notes

Verify the attachment is also removed from the backend storage (S3).

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A file upload field on the Driver (hr.employee) form view, labeled 'Driver's License'.
- Standard Odoo binary/image widget controls for uploading, clearing, and downloading the file.

## 4.2.0 User Interactions

- User clicks on the field to open a native file selector.
- User can drag-and-drop a file onto the widget.
- User receives immediate visual feedback upon successful upload (thumbnail/icon appears) or failure (error message).

## 4.3.0 Display Requirements

- Display a thumbnail for image files (JPG, PNG).
- Display a generic file icon and filename for PDF documents.
- The field should be clearly positioned alongside other license information like 'License Number' and 'License Expiry Date'.

## 4.4.0 Accessibility Needs

- The upload button/field must be keyboard accessible.
- The field must have a proper ARIA label, such as 'Upload driver's license scan'.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-FILE-01

### 5.1.2 Rule Description

Uploaded license files must be of type JPG, PNG, or PDF.

### 5.1.3 Enforcement Point

Client-side validation on file selection and server-side validation upon submission.

### 5.1.4 Violation Handling

The upload is blocked, and an informative error message is displayed to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-FILE-02

### 5.2.2 Rule Description

Uploaded license files must not exceed a maximum size of 5MB.

### 5.2.3 Enforcement Point

Server-side validation upon submission.

### 5.2.4 Violation Handling

The upload is blocked, and an informative error message is displayed to the user.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-011', 'dependency_reason': 'The driver record model and view must exist before a field can be added to it for uploading a license.'}

## 6.2.0 Technical Dependencies

- Odoo's `hr.employee` model must be available for extension.
- The system's attachment storage must be configured to use Amazon S3, as per REQ-DEP-001.

## 6.3.0 Data Dependencies

- Requires at least one existing driver record in the database for testing.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- File upload for a 5MB file should complete in under 10 seconds on a standard broadband connection.
- Loading the driver form with an existing license image should not add more than 500ms to the page load time.

## 7.2.0 Security

- File uploads must be transmitted over HTTPS (REQ-INT-004).
- Files must be stored with encryption at rest in the S3 bucket (REQ-NFR-003).
- Access to view or upload the license file must be restricted by Odoo's RBAC to authorized roles (Admin, Dispatch Manager, Finance Officer). A Driver user should not be able to view another driver's license.

## 7.3.0 Usability

- The upload process should be intuitive, requiring minimal user instruction.
- Error messages must be clear, concise, and actionable.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards (REQ-INT-001).

## 7.5.0 Compatibility

- The upload functionality must work on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- This is a standard Odoo development task involving adding a `fields.Binary` to an existing model and view.
- No complex business logic is required.
- Primary effort is in configuration and ensuring security rules are correctly applied.

## 8.3.0 Technical Risks

- Potential misconfiguration of the S3 attachment storage, leading to files being saved on the local server instead.

## 8.4.0 Integration Points

- Odoo `ir.attachment` model.
- Amazon S3 for file storage.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0 Test Scenarios

- Verify successful upload of JPG, PNG, and PDF files under 5MB.
- Verify rejection of invalid file types (.docx, .zip, .exe).
- Verify rejection of files over 5MB.
- Verify the replace and delete functionalities.
- Verify file download/viewing.
- Role-based access test: Log in as a Driver and attempt to view another driver's license scan (should be denied).

## 9.3.0 Test Data Needs

- Sample JPG, PNG, and PDF files under 5MB.
- A sample image file over 5MB.
- Sample files with invalid extensions.

## 9.4.0 Testing Tools

- Standard browser developer tools.
- Odoo's testing framework.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for any custom logic and passing with >80% coverage
- Integration testing with S3 storage is completed successfully
- User interface reviewed and approved by the Product Owner
- Security requirements validated, including role-based access checks
- Documentation for the new field is updated in the technical specification
- Story deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational feature for the Driver Master module and should be prioritized early.
- Depends on the base Driver model (US-011) being completed in the same or a prior sprint.

## 11.4.0 Release Impact

- This feature is critical for the initial release (Phase 1) as it's a core part of driver data management and compliance.


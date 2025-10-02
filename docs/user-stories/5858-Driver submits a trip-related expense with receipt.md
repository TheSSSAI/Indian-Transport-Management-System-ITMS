# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-053 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver submits a trip-related expense with receipt |
| As A User Story | As a Driver, I want to submit a trip-related expen... |
| User Persona | Driver |
| Business Value | Enables accurate and timely tracking of trip-relat... |
| Functional Area | Expense Management |
| Story Theme | Driver Portal & On-Trip Activities |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful submission of a standard expense (e.g., Toll)

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in Driver and I am viewing an 'In-Transit' trip assigned to me

### 3.1.5 When

I navigate to the 'Add Expense' form, select 'Toll' as the type, enter '250.00' as the amount, upload a valid receipt image (JPG, <5MB), and press 'Submit'

### 3.1.6 Then

The system must create a new expense record linked to my trip with a status of 'Submitted', store the uploaded receipt, and display a confirmation message 'Expense submitted successfully'.

### 3.1.7 Validation Notes

Verify the new expense record in the database and check that it appears in the Dispatch Manager's approval queue. Confirm the receipt file is accessible and stored in the configured S3 bucket.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Successful submission of a 'Diesel' expense with required extra fields

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am a logged-in Driver viewing an 'In-Transit' trip, and the last recorded odometer for my vehicle was 150000 km

### 3.2.5 When

I select 'Diesel' as the expense type, enter amount '7500', quantity '75' liters, odometer '150250', upload a valid receipt, and press 'Submit'

### 3.2.6 Then

The system must create a new expense record with all the provided details (including quantity and odometer), and display a success message.

### 3.2.7 Validation Notes

Verify the expense record contains the odometer and quantity fields. The odometer reading should be saved against the vehicle's history for future validation.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to submit with missing required fields

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am on the 'Add Expense' form for my trip

### 3.3.5 When

I select 'Food' as the type, upload a receipt, but leave the 'Amount' field blank and press 'Submit'

### 3.3.6 Then

The system must prevent submission, display an inline validation error message 'Amount is a required field' next to the amount input, and the form data must be preserved.

### 3.3.7 Validation Notes

Test for each required field individually (Type, Amount, Receipt).

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to upload an invalid file type for the receipt

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am on the 'Add Expense' form

### 3.4.5 When

I attempt to upload a file with an unsupported extension, such as '.docx' or '.zip'

### 3.4.6 Then

The system must reject the file and display a clear error message, 'Invalid file type. Please upload a JPG, PNG, or PDF.'

### 3.4.7 Validation Notes

Test with multiple invalid file types.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to upload a file that exceeds the size limit

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am on the 'Add Expense' form

### 3.5.5 When

I attempt to upload a PNG file that is 6MB in size

### 3.5.6 Then

The system must reject the file and display an error message, 'File size cannot exceed 5MB.'

### 3.5.7 Validation Notes

Test with a file just over the 5MB limit.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Attempt to submit a 'Diesel' expense with an invalid odometer reading

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

I am submitting a 'Diesel' expense, and the last recorded odometer for my vehicle was 150000 km

### 3.6.5 When

I enter an odometer reading of '149950' and press 'Submit'

### 3.6.6 Then

The system must prevent submission and display a specific validation error, 'Odometer reading must be greater than the last recorded value (150000 km).'

### 3.6.7 Validation Notes

Verify this check works for values less than or equal to the last reading.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

UI behavior for conditional 'Diesel' fields

### 3.7.3 Scenario Type

Alternative_Flow

### 3.7.4 Given

I am on the 'Add Expense' form

### 3.7.5 When

I select 'Diesel' from the 'Expense Type' dropdown

### 3.7.6 Then

The 'Quantity (Liters)' and 'Odometer Reading' input fields must become visible and be marked as required.

### 3.7.7 Validation Notes

Further, when the user changes the selection from 'Diesel' to 'Toll', these conditional fields must be hidden again.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Dropdown for 'Expense Type' (populated with Diesel, Toll, Food, etc.)
- Numeric input for 'Amount'
- File input button for 'Upload Receipt' (allowing camera access)
- Numeric input for 'Quantity (Liters)' (conditional)
- Numeric input for 'Odometer Reading' (conditional)
- Submit button
- Success/Error message display area

## 4.2.0 User Interactions

- Selecting an expense type dynamically shows/hides relevant fields.
- Uploading a file should show a preview or filename.
- Submitting the form should show a loading indicator until a response is received.

## 4.3.0 Display Requirements

- The form should clearly indicate which trip the expense is being submitted for.
- All required fields should be clearly marked (e.g., with an asterisk).

## 4.4.0 Accessibility Needs

- All form fields must have associated labels.
- The interface must be navigable using a keyboard.
- Buttons and interactive elements must have sufficient size for touch targets on mobile devices.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-009

### 5.1.2 Rule Description

The odometer reading submitted with a 'Diesel' expense entry must be greater than the previously recorded odometer reading for that vehicle.

### 5.1.3 Enforcement Point

Server-side validation upon form submission.

### 5.1.4 Violation Handling

Reject the submission and return a specific error message to the user.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

REQ-FNC-004-Validation

### 5.2.2 Rule Description

Uploaded receipt files shall be restricted to common image and document formats (JPG, PNG, PDF) with a maximum file size of 5MB.

### 5.2.3 Enforcement Point

Client-side and server-side validation.

### 5.2.4 Violation Handling

Reject the file upload and display an informative error message.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

Driver must be able to log into the portal to access any functionality.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-047

#### 6.1.2.2 Dependency Reason

Driver needs to select an assigned trip to associate the expense with.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-032

#### 6.1.3.2 Dependency Reason

A backend queue/view for submitted expenses is required for a manager to approve them, completing the workflow.

## 6.2.0.0 Technical Dependencies

- Odoo's file storage system (ir.attachment) must be configured to use Amazon S3.
- The `tms.expense` Odoo model must be defined.
- The Odoo Web Library (OWL) component for the mobile-friendly form.

## 6.3.0.0 Data Dependencies

- A master list of expense types must be available.
- The system must be able to retrieve the last known odometer reading for a specific vehicle.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The expense form should load in under 3 seconds on a 4G mobile connection.
- Form submission, including file upload of up to 5MB, should provide user feedback (success/error) within 8 seconds on a 4G connection.

## 7.2.0.0 Security

- All data transmission must be over HTTPS.
- A driver must only be able to submit expenses for trips they are assigned to (enforced by server-side authorization).
- Uploaded files should be stored securely and scanned for malware if possible.

## 7.3.0.0 Usability

- The submission process must be intuitive and require minimal steps.
- Error messages must be clear and actionable for a non-technical user.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of Chrome on Android and Safari on iOS.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Implementing the dynamic UI for conditional fields in OWL.
- Handling file uploads robustly on mobile web, including potential network interruptions.
- Backend validation logic, especially the odometer check which requires a database query on historical data.
- Integration with S3 for file storage.

## 8.3.0.0 Technical Risks

- Poor mobile network conditions could lead to failed uploads and a frustrating user experience.
- Cross-browser compatibility issues with the file input/camera API on mobile devices.

## 8.4.0.0 Integration Points

- Odoo `tms.trip` model: To link the expense to a trip.
- Odoo `tms.vehicle` model: To retrieve the last odometer reading.
- Amazon S3: For storing receipt attachments.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability
- Compatibility

## 9.2.0.0 Test Scenarios

- Submit each type of expense.
- Test all validation rules (required fields, file type/size, odometer).
- Test on physical Android and iOS devices to check camera/file picker functionality.
- Use browser developer tools to simulate slow network conditions during upload.
- Verify that a submitted expense correctly appears for the Dispatch Manager.

## 9.3.0.0 Test Data Needs

- A test Driver user.
- An active trip assigned to the test driver.
- A vehicle with a pre-existing odometer reading.
- Sample files for testing uploads: valid JPG/PNG/PDF under 5MB, invalid file types, files over 5MB.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- A frontend testing framework like Playwright for E2E tests.
- Physical mobile devices for manual QA.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for all validation logic, achieving >80% coverage
- Integration testing completed successfully (form -> DB -> S3)
- User interface reviewed and approved for mobile usability
- Performance requirements verified on a throttled network connection
- Security requirements validated (e.g., cannot submit expense for another driver's trip)
- Documentation updated for the Driver Portal module
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a core feature for the Driver persona and a high-value item for the business. It unblocks financial tracking workflows.
- Ensure the team has access to a test S3 bucket and credentials before starting development.

## 11.4.0.0 Release Impact

- This feature is critical for the 'Core Operations' phase (Phase 1) of the rollout strategy.


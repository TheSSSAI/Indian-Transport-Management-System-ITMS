# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-092 |
| Elaboration Date | 2025-01-26 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver: Access Self-Service Training Materials in ... |
| As A User Story | As a Driver, I want to access a dedicated 'Help & ... |
| User Persona | Driver: An on-field user who accesses the system v... |
| Business Value | Reduces the support load on dispatch and admin sta... |
| Functional Area | Driver Portal |
| Story Theme | User Training and Support |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Navigation to Training Section

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a user with the 'Driver' role and I am logged into the mobile-friendly web portal

### 3.1.5 When

I view the main navigation menu of the portal

### 3.1.6 Then

I see a clearly labeled and easily tappable option for 'Help & Training'.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Viewing Available Training Materials

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I have navigated to the 'Help & Training' page

### 3.2.5 When

the page finishes loading

### 3.2.6 Then

I see a list of available video tutorials, each with a descriptive title (e.g., 'How to Submit an Expense').

### 3.2.7 Validation Notes

The list should be populated from a backend model that stores training material metadata. The layout must be mobile-first and easy to read.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Viewing and Accessing the Quick-Reference Guide (QRG)

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am on the 'Help & Training' page

### 3.3.5 When

the page is loaded

### 3.3.6 Then

I see a clearly marked link, button, or card for the 'Quick-Reference Guide (QRG)'.

### 3.3.7 Validation Notes

Tapping this link should open the QRG (PDF) in a new browser tab or trigger a download, consistent with standard mobile browser behavior.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Playing a Video Tutorial

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I am on the 'Help & Training' page with a list of videos

### 3.4.5 When

I tap on a video tutorial's title or thumbnail

### 3.4.6 Then

an embedded video player loads and plays the video directly within the page without navigating away.

### 3.4.7 Validation Notes

The video player must include standard controls: play/pause, volume, and a fullscreen option. It should function correctly in both portrait and landscape mode.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

No Training Materials Available

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

I have navigated to the 'Help & Training' page

### 3.5.5 And

no training materials have been uploaded by an Admin

### 3.5.6 When

the page loads

### 3.5.7 Then

I see a user-friendly message, such as 'No training materials are available at this time. Please check back later.'

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Video or Document Fails to Load

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am on the 'Help & Training' page

### 3.6.5 And

the URL for a video or the QRG is incorrect or the file is missing from the server

### 3.6.6 When

I attempt to view the content

### 3.6.7 Then

the system displays a clear error message within the UI, such as 'This content could not be loaded. Please try again later or contact support.'

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Help & Training' navigation item (icon and/or text) in the Driver Portal's main menu.
- A dedicated page/view for training materials.
- A list or card layout for displaying each training item with its title.
- An embedded HTML5 video player with standard controls.
- A distinct link or button with a document icon (e.g., PDF icon) for the QRG.

## 4.2.0 User Interactions

- User taps the navigation item to access the training page.
- User scrolls through the list of available materials.
- User taps a video item to play it inline.
- User taps the QRG link to open/download the document.

## 4.3.0 Display Requirements

- The page must be fully responsive and optimized for mobile viewports (from 360px width upwards as per REQ-INT-001).
- Video titles must be clear and legible.
- Loading indicators should be displayed while video content is buffering.

## 4.4.0 Accessibility Needs

- All interactive elements (links, buttons, video controls) must have sufficient touch target sizes for mobile use.
- Video player controls must be keyboard-accessible and have appropriate ARIA labels.
- Text must meet WCAG 2.1 AA contrast ratio requirements.

# 5.0.0 Business Rules

*No items available*

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

The Driver must be able to log in and access the mobile-friendly web portal before any portal-specific features can be added.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-Admin-Manage-Training-Materials

#### 6.1.2.2 Dependency Reason

An Admin-facing feature to upload, title, and manage the URLs for videos and the QRG document is required. This story cannot be completed without content to display.

## 6.2.0.0 Technical Dependencies

- Odoo Web Library (OWL) for frontend component development.
- Amazon S3 for hosting video and PDF files, as specified in REQ-DEP-001. The application will store URLs to these files, not the files themselves.

## 6.3.0.0 Data Dependencies

- Requires a new Odoo model (e.g., `tms.training.material`) to store metadata for each training item: title, type (video/document), URL, and an active flag.

## 6.4.0.0 External Dependencies

- Creation of the actual training content (videos, QRG document) by the business/training team is an external dependency for this feature to have value.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The 'Help & Training' page must load in under 3 seconds on a standard 4G mobile connection.
- Videos should begin playback within 5 seconds of the user tapping play, utilizing appropriate buffering strategies.

## 7.2.0.0 Security

- Access to the 'Help & Training' page must be restricted to authenticated users with the 'Driver' role.
- URLs for training materials stored in S3 should not expose any sensitive information.

## 7.3.0.0 Usability

- The process of finding and viewing a training video should take no more than 3 taps from the portal's home screen.
- The interface must be simple and intuitive, requiring no prior training to navigate.

## 7.4.0.0 Accessibility

- The feature must adhere to WCAG 2.1 Level AA standards, as stated in REQ-INT-001.

## 7.5.0.0 Compatibility

- The feature must be fully functional on the latest versions of Chrome on Android and Safari on iOS.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Requires creating a new, simple Odoo model and corresponding OWL view.
- Integration of a standard HTML5 `<video>` element is straightforward.
- The primary effort will be in ensuring a clean, responsive UI/UX for mobile devices.

## 8.3.0.0 Technical Risks

- Potential for poor video streaming performance on unstable mobile networks. This is mitigated by hosting files on S3, but not entirely eliminated.
- Minor cross-browser compatibility issues with the video player styling or behavior.

## 8.4.0.0 Integration Points

- The backend will read training material URLs from the new Odoo model.
- The frontend will fetch these records via an Odoo controller and render them.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability
- Accessibility

## 9.2.0.0 Test Scenarios

- Verify a driver can log in, navigate to the training page, and see the list of materials.
- Test video playback on both an Android (Chrome) and iOS (Safari) device.
- Test QRG download/viewing on both platforms.
- Verify the 'no materials' message appears when the backend model is empty.
- Test the UI layout on various screen sizes, including the smallest supported width (360px).
- Simulate a broken URL to verify the error handling mechanism.

## 9.3.0.0 Test Data Needs

- A test user with the 'Driver' role.
- At least two sample video files and one sample PDF file hosted on a test S3 bucket.
- Records created in the `tms.training.material` model pointing to the test files.

## 9.4.0.0 Testing Tools

- Browser developer tools for mobile emulation and network throttling.
- Physical mobile devices for final validation.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing on target mobile browsers.
- Code has been peer-reviewed and merged into the main development branch.
- Unit tests for the new Odoo model and controller achieve >80% coverage.
- E2E tests simulating the driver's journey are implemented and passing.
- The UI has been reviewed and approved by the Product Owner for usability and adherence to design standards.
- Accessibility checks (automated and manual) have been completed.
- The feature is deployed and verified in the staging environment.
- The dependency on the Admin content management story is resolved and tested in conjunction with this story.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🟡 Medium

## 11.3.0.0 Sprint Considerations

- This story should be scheduled in a sprint after the foundational Driver Portal (US-046) is complete.
- Must be coordinated with the development of the corresponding Admin story for managing training content.

## 11.4.0.0 Release Impact

Enhances user experience and long-term supportability. It is not a blocker for the initial release of core trip management functionality but is highly desirable for a successful rollout.


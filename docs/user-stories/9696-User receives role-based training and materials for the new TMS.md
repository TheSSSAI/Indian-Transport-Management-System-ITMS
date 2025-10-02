# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-091 |
| Elaboration Date | 2025-01-26 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | User receives role-based training and materials fo... |
| As A User Story | As a new system user (Admin, Manager, Finance Offi... |
| User Persona | All TMS user roles: Admin, Dispatch Manager, Finan... |
| Business Value | Ensures smooth user adoption, reduces post-launch ... |
| Functional Area | Project Management & Transition |
| Story Theme | System Implementation and Go-Live |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Instructor-Led Training for Office Staff

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

The TMS is feature-complete and stable in the staging environment

### 3.1.5 When

An Admin, Dispatch Manager, or Finance Officer attends their scheduled, role-specific training session

### 3.1.6 Then

They can successfully complete a set of predefined key tasks for their role in the staging environment and confirm their understanding of the system.

### 3.1.7 Validation Notes

Validated by instructor observation during the session and a post-training sign-off sheet. Attendance must be tracked.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Distribution of User Manual

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A comprehensive User Manual for office staff roles has been created and approved

### 3.2.5 When

The training sessions for office staff are conducted

### 3.2.6 Then

Each attendee receives a digital copy of the User Manual for future reference.

### 3.2.7 Validation Notes

Confirm distribution via email tracking or a shared document link.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Driver Accesses Video Tutorials

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A Driver is logged into the mobile-friendly web portal

### 3.3.5 When

They navigate to the 'Help & Training' section

### 3.3.6 Then

They see a list of short video tutorials covering their key tasks (e.g., 'How to Submit an Expense', 'How to Upload a POD') and can play them directly within the browser.

### 3.3.7 Validation Notes

Manual test on multiple mobile devices (iOS/Android) to ensure the training section is present, links are correct, and videos are playable.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Distribution of Driver Quick Reference Guide (QRG)

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A laminated, one-page Quick Reference Guide (QRG) for drivers has been created and printed

### 3.4.5 When

The go-live date approaches

### 3.4.6 Then

Every driver has been given a physical copy of the QRG.

### 3.4.7 Validation Notes

Validated via a distribution checklist signed by each driver or their supervisor.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

User Misses Scheduled Training

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

A user is unable to attend their scheduled instructor-led training session

### 3.5.5 When

They notify the project team

### 3.5.6 Then

They are provided with alternative training options, such as a recorded session or a scheduled make-up class, to ensure they are trained before go-live.

### 3.5.7 Validation Notes

Verify that a process for handling absences is defined and communicated.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Help & Training' menu item or button within the Driver Portal.
- A dedicated page in the Driver Portal to list and embed training videos.
- A download link for the digital (PDF) version of the Quick Reference Guide.

## 4.2.0 User Interactions

- Driver can tap on a video title to play it in an embedded player.
- Driver can tap a link to download the QRG PDF.

## 4.3.0 Display Requirements

- The training page should clearly title each video based on the task it demonstrates.

## 4.4.0 Accessibility Needs

- Training videos should include optional closed captions.
- The QRG PDF should be structured to be reasonably accessible to screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-TRN-001', 'rule_description': 'All users must complete their role-specific training before being granted full production access on go-live day.', 'enforcement_point': 'Project Management / Go-Live Checklist', 'violation_handling': 'User account remains in a restricted state until training completion is verified.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

The Driver Portal must exist to host the video tutorials and QRG download link.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

ALL_CORE_FUNCTIONALITY

#### 6.1.2.2 Dependency Reason

All features for a specific role (e.g., Trip Creation, Expense Submission, Invoicing) must be complete and stable in the staging environment before training on them can occur.

## 6.2.0.0 Technical Dependencies

- A solution for hosting and embedding videos (e.g., private YouTube, Vimeo, S3 bucket with an HTML5 player).

## 6.3.0.0 Data Dependencies

- A stable, production-like dataset in the staging environment is required for users to practice on during training.

## 6.4.0.0 External Dependencies

- Availability of all users for scheduling and attending training sessions, requiring coordination with operational managers.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Training videos hosted online should start playing within 5 seconds on a standard mobile data connection.

## 7.2.0.0 Security

- Training videos, if containing sensitive operational details, should be hosted privately and not be publicly discoverable.

## 7.3.0.0 Usability

- All training materials must be written in clear, simple language appropriate for the target audience.
- The 'Help & Training' section in the Driver Portal must be easily discoverable.

## 7.4.0.0 Accessibility

- As per UI requirements, videos should have captions and documents should be screen-reader friendly.

## 7.5.0.0 Compatibility

- The training page in the Driver Portal must function correctly on the latest versions of Chrome and Safari on both iOS and Android.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

High

## 8.2.0.0 Complexity Factors

- This story's effort is primarily in non-development tasks: curriculum design, creating video content, writing manuals, graphic design for the QRG, and the logistics of scheduling and conducting training for all users.
- The software development portion (creating the training page) is low complexity, but the overall story effort is high.

## 8.3.0.0 Technical Risks

- Underestimation of the time required for creating high-quality training content.
- Logistical challenges in scheduling training for all staff, especially drivers, without disrupting operations.

## 8.4.0.0 Integration Points

- The Driver Portal is the only software integration point.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Usability
- User Acceptance Testing (UAT)

## 9.2.0.0 Test Scenarios

- A pilot training session should be conducted with a small group of 'super users' to gather feedback on materials and presentation before rolling out to all staff.
- Verify that the driver training page works on a range of mobile devices.
- Verify all training materials for accuracy against the implemented system features in the staging environment.

## 9.3.0.0 Test Data Needs

- A fully populated staging environment that allows trainees to execute end-to-end workflows for their roles.

## 9.4.0.0 Testing Tools

- Standard web browsers on mobile and desktop devices.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- All training materials (User Manual, Videos, QRG) created, reviewed, and approved
- Software component for Driver Portal training page is developed, code-reviewed, tested, and deployed to staging
- All instructor-led training sessions have been completed and attendance recorded
- All drivers have received their QRG and been notified of the video tutorials
- A process for training new hires post-launch has been documented and handed over to the business

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

13

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story must be completed in the sprint(s) immediately preceding the planned go-live date.
- The content creation tasks can be started in earlier sprints, but the final delivery is dependent on feature completion.
- This is a critical path item for a successful launch and cannot be descoped.

## 11.4.0.0 Release Impact

- Successful completion is a mandatory gate for the production go-live.


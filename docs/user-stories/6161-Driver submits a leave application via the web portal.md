# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-056 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver submits a leave application via the web por... |
| As A User Story | As a Driver, I want to submit a leave application ... |
| User Persona | Driver: An on-field user accessing the system via ... |
| Business Value | Streamlines the leave request process, reduces adm... |
| Functional Area | Driver Portal |
| Story Theme | Driver Self-Service |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful submission of a valid leave application

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a Driver logged into the Driver Portal and I am on the 'New Leave Request' page

### 3.1.5 When

I select a 'Leave Type', choose a 'Start Date' and 'End Date' (where start date is not after end date and not in the past), enter an optional reason, and click 'Submit'

### 3.1.6 Then

The system creates a new leave application record with a 'Pending' status, I see a success confirmation message, and I am redirected to my list of leave applications where the new request is visible at the top.

### 3.1.7 Validation Notes

Verify a new record is created in the `tms.leave.application` model with the correct driver, dates, and status. Verify the UI redirects and displays the success message.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Attempt to submit a leave request with an invalid date range

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

I am a Driver on the 'New Leave Request' page

### 3.2.5 When

I select a 'Start Date' that is after the 'End Date' and click 'Submit'

### 3.2.6 Then

The system prevents submission and displays a clear validation error message, such as 'Start date cannot be after the end date'.

### 3.2.7 Validation Notes

Test with various invalid date combinations. The form should not submit, and the error message should be user-friendly.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempt to submit a leave request for a past date

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am a Driver on the 'New Leave Request' page

### 3.3.5 When

I select a 'Start Date' that is before today's date and click 'Submit'

### 3.3.6 Then

The system prevents submission and displays a clear validation error message, such as 'Leave cannot be requested for past dates'.

### 3.3.7 Validation Notes

The date picker for the 'Start Date' should ideally disable past dates to prevent this error proactively.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to submit a leave request with missing required fields

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am a Driver on the 'New Leave Request' page

### 3.4.5 When

I click 'Submit' without selecting a 'Leave Type', 'Start Date', or 'End Date'

### 3.4.6 Then

The system prevents submission and highlights the required fields that are missing.

### 3.4.7 Validation Notes

Verify that form submission is blocked and visual cues indicate which fields need to be filled.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to submit a leave request that overlaps with an existing request

### 3.5.3 Scenario Type

Edge_Case

### 3.5.4 Given

I am a Driver and I have an existing leave request from July 10th to July 15th (status can be 'Pending' or 'Approved')

### 3.5.5 When

I try to submit a new leave request for a period that overlaps, such as July 12th to July 17th

### 3.5.6 Then

The system prevents submission and displays a clear validation error message, such as 'This request overlaps with an existing leave application'.

### 3.5.7 Validation Notes

Test all overlap scenarios: new request inside existing, new request contains existing, new request overlaps start, new request overlaps end.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Driver views their history of leave applications

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

I am a Driver logged into the Driver Portal

### 3.6.5 When

I navigate to the 'Leave Requests' section

### 3.6.6 Then

I can see a list of all my past and present leave applications, including the dates, type, and current status ('Pending', 'Approved', 'Rejected') for each.

### 3.6.7 Validation Notes

Verify the list is sorted with the most recent requests first and that the status is clearly displayed.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A 'Leave Requests' menu item in the Driver Portal navigation.
- A 'New Leave Request' button on the leave history page.
- A leave application form with a 'Leave Type' dropdown, 'Start Date' and 'End Date' date pickers, and a multi-line 'Reason' text area.
- 'Submit' and 'Cancel' buttons on the form.

## 4.2.0 User Interactions

- The date pickers should be mobile-friendly and should disable selection of past dates for the 'Start Date'.
- Upon successful submission, a toast notification or confirmation message should appear.
- The list of leave requests should clearly indicate the status of each request using color-coded tags or badges.

## 4.3.0 Display Requirements

- The leave history list must display: Leave Type, Start Date, End Date, and Status.
- Validation errors must be displayed near the relevant form fields.

## 4.4.0 Accessibility Needs

- All form fields must have associated labels for screen readers.
- All UI elements must be keyboard-navigable and have clear focus indicators, adhering to WCAG 2.1 Level AA.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-DRV-LEAVE-01

### 5.1.2 Rule Description

A driver cannot request leave for dates that conflict with an already assigned trip's expected delivery window.

### 5.1.3 Enforcement Point

On submission of the leave application form.

### 5.1.4 Violation Handling

The system will prevent submission and display an error message specifying the conflicting trip ID (e.g., 'This request conflicts with assigned trip TRP-00123').

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-DRV-LEAVE-02

### 5.2.2 Rule Description

The list of available 'Leave Types' (e.g., Vacation, Sick Leave) is centrally managed by an Admin user.

### 5.2.3 Enforcement Point

The 'Leave Type' dropdown on the application form.

### 5.2.4 Violation Handling

N/A - The driver can only select from the predefined list.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

Driver must be able to log into the portal to access the leave application feature.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-011

#### 6.1.2.2 Dependency Reason

A driver record must exist in the system to associate the leave request with.

## 6.2.0.0 Technical Dependencies

- Requires a new Odoo model `tms.leave.application` to store leave requests.
- Requires a new Odoo model `tms.leave.type` for admin-managed leave categories.
- Requires Odoo web controllers and OWL templates for the Driver Portal interface.

## 6.3.0.0 Data Dependencies

- Relies on the existence of the driver's `hr.employee` record.
- Needs access to the driver's assigned trips to check for scheduling conflicts.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The leave application form must load in under 3 seconds.
- Form submission and validation feedback must be provided to the user within 2 seconds.

## 7.2.0.0 Security

- A driver can only view, create, and manage their own leave applications.
- Access to this feature requires an authenticated session as a 'Driver' role.

## 7.3.0.0 Usability

- The interface must be simple and intuitive for use on a mobile device with minimal training.

## 7.4.0.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The feature must be fully functional on modern mobile web browsers (latest versions of Chrome and Safari).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Creation of two new Odoo models and their associated views/access rights.
- Development of a custom web portal interface using OWL.
- Implementation of server-side validation logic for date ranges, overlaps, and conflicts with existing trips.
- Requires a corresponding feature for managers to approve/reject requests to be fully functional.

## 8.3.0.0 Technical Risks

- The logic for detecting conflicts with assigned trips could be complex if trip schedules are not well-defined.
- Ensuring a seamless and responsive UI/UX on a wide range of mobile devices.

## 8.4.0.0 Integration Points

- The approved leave data must be integrated into the trip assignment logic (US-027) to filter out unavailable drivers.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability

## 9.2.0.0 Test Scenarios

- Verify successful submission and record creation.
- Test all validation rules: past dates, inverted dates, overlapping dates, and trip conflicts.
- Test viewing leave history and status updates (after manager approval story is done).
- Perform testing on a physical mobile device to confirm usability and responsiveness.

## 9.3.0.0 Test Data Needs

- A test user with the 'Driver' role.
- Existing leave applications for the test driver to test overlap logic.
- An assigned trip for the test driver to test conflict logic.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework.
- Browser developer tools for mobile emulation.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for all validation logic, achieving >80% coverage, and passing
- Integration testing completed to ensure leave data is correctly stored and retrieved
- User interface reviewed and approved for mobile-friendliness and usability
- Performance requirements verified
- Security requirements validated (a driver cannot see another driver's leave)
- Documentation for the new models and portal endpoints is created
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🟡 Medium

## 11.3.0.0 Sprint Considerations

- This story provides value on its own but delivers full business value when paired with the corresponding manager approval story. It is recommended to plan them in consecutive or the same sprint.
- The update to the trip assignment logic (US-027) to check for leave should be planned as a follow-up.

## 11.4.0.0 Release Impact

This introduces a significant new self-service feature for drivers, improving their engagement and streamlining HR processes.


# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-047 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver views their list of current and past trips |
| As A User Story | As a Driver, I want to view a clear, mobile-friend... |
| User Persona | Driver: An on-field user who accesses the system v... |
| Business Value | Improves operational efficiency by providing drive... |
| Functional Area | Driver Portal |
| Story Theme | Trip Lifecycle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Default view shows current trips

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

a Driver is logged into the mobile web portal

### 3.1.5 And

the driver has trips with statuses 'Assigned' and 'In-Transit'

### 3.1.6 When

the driver navigates to the 'My Trips' page

### 3.1.7 Then

a list of their 'Current' trips is displayed by default, containing only the trips with 'Assigned' or 'In-Transit' status.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Switching to view past trips

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

a Driver is on the 'My Trips' page

### 3.2.5 And

the driver has trips with statuses 'Delivered', 'Completed', or 'Canceled'

### 3.2.6 When

the driver selects the 'Past Trips' view (e.g., via a tab or filter)

### 3.2.7 Then

the list updates to display only their trips with 'Delivered', 'Completed', 'Invoiced', 'Paid', or 'Canceled' status.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Information displayed on each trip item

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

the driver is viewing either the current or past trips list

### 3.3.5 When

the list is rendered

### 3.3.6 Then

each trip item in the list must clearly display the Trip ID, Customer Name, Source Location, Destination Location, and current Trip Status.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Data is properly scoped to the logged-in driver

### 3.4.3 Scenario Type

Security

### 3.4.4 Given

a Driver is logged in

### 3.4.5 When

they access the 'My Trips' page

### 3.4.6 Then

the system must ensure that only trips explicitly assigned to that driver are ever fetched and displayed.

### 3.4.7 Validation Notes

This must be enforced on the backend using Odoo's record rules (`ir.rule`) and verified via API testing with different user credentials.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

List sorting order

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

the driver is viewing a list of trips

### 3.5.5 When

the list is displayed

### 3.5.6 Then

the 'Current Trips' list is sorted by the trip's start date in descending order (newest first)

### 3.5.7 And

the 'Past Trips' list is sorted by the trip's completion/delivery date in descending order (most recent first).

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Driver has no trips assigned

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

a new Driver is logged in and has no trips assigned to them

### 3.6.5 When

they navigate to the 'My Trips' page

### 3.6.6 Then

the 'Current Trips' view displays a user-friendly message such as 'You have no current trips assigned.'

### 3.6.7 And

switching to the 'Past Trips' view displays a message like 'No past trips found.'

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Performance on long trip history

### 3.7.3 Scenario Type

Non_Functional

### 3.7.4 Given

a Driver has a history of over 100 past trips

### 3.7.5 When

they view their 'Past Trips' list

### 3.7.6 Then

the list must use lazy loading or pagination to load trips incrementally, ensuring the initial page load is under 3 seconds.

### 3.7.7 Validation Notes

Test with a user account populated with 200+ historical trips.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

API failure to load trips

### 3.8.3 Scenario Type

Error_Condition

### 3.8.4 Given

the Driver navigates to the 'My Trips' page

### 3.8.5 When

the backend API call to fetch trips fails

### 3.8.6 Then

a clear, non-technical error message like 'Could not load trips. Please check your connection and try again.' is displayed to the user.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Tabs or segmented control for 'Current' and 'Past' trips.
- A list/card view for displaying trips.
- A placeholder message for when no trips are available.
- A loading indicator while data is being fetched.
- An error message display area.

## 4.2.0 User Interactions

- User can tap to switch between 'Current' and 'Past' trip views.
- User can scroll through the list of trips.
- For long lists, scrolling to the bottom should trigger loading of more items (lazy loading).
- Tapping on a trip card navigates the user to the trip detail view (covered in a separate story).

## 4.3.0 Display Requirements

- Each trip card must show: Trip ID, Customer Name, Source, Destination, Status.
- Trip status should be visually distinct (e.g., using color-coded badges).
- The layout must be responsive and optimized for mobile screens (360px width and up).

## 4.4.0 Accessibility Needs

- All interactive elements (tabs, cards) must have a minimum tap target size of 44x44 pixels.
- Color-coded statuses must also have a text label for color-blind users.
- The page must be navigable using a screen reader.

# 5.0.0 Business Rules

- {'rule_id': 'BR-004', 'rule_description': "The trip status lifecycle must follow the defined path: `Planned` -> `Assigned` -> `In-Transit` <-> `On Hold` -> `Delivered` -> `Completed` -> `Invoiced` -> `Paid`. This story's logic depends on these statuses to categorize trips.", 'enforcement_point': 'Backend API controller when filtering trips.', 'violation_handling': 'N/A - This is a data categorization rule.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-046

#### 6.1.1.2 Dependency Reason

Driver must be able to log in to the system to access any personalized information.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-027

#### 6.1.2.2 Dependency Reason

A mechanism to assign trips to drivers must exist for any trips to appear in their list.

## 6.2.0.0 Technical Dependencies

- Odoo's authentication system (`res.users`).
- Odoo's security record rules (`ir.rule`) for data scoping.
- A backend API endpoint (Odoo controller) to serve the trip data.
- Odoo Web Library (OWL) for the frontend component.

## 6.3.0.0 Data Dependencies

- Requires the existence of the Trip data model with fields for assigned driver, status, customer, source, and destination.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The initial list of trips must load in under 3 seconds on a 4G mobile connection (as per REQ-NFR-001 LCP target).
- API response time for fetching the trip list should be under 200ms (as per REQ-NFR-001).

## 7.2.0.0 Security

- The API endpoint must be protected and only accessible to authenticated users with the 'Driver' role.
- Server-side logic must strictly enforce that a driver can only query trips assigned to them.

## 7.3.0.0 Usability

- The interface must be simple and intuitive, with large touch targets, suitable for on-the-go use by drivers.
- Information must be presented clearly with minimal clutter.

## 7.4.0.0 Accessibility

- Must adhere to WCAG 2.1 Level AA standards (as per REQ-INT-001).

## 7.5.0.0 Compatibility

- The web interface must be fully functional on the latest versions of Chrome and Safari on both iOS and Android mobile devices.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Standard Odoo backend development (controller with domain search).
- Standard OWL frontend development for a responsive list view.
- The logic for separating 'current' vs 'past' trips is straightforward.
- Pagination/lazy loading is a common pattern but requires careful state management on the client side.

## 8.3.0.0 Technical Risks

- Potential for performance issues if the 'past trips' list becomes very large and pagination is not implemented correctly.
- Ensuring the UI is truly usable and not just functional on a variety of mobile device screen sizes.

## 8.4.0.0 Integration Points

- This story integrates with the core Trip model in the Odoo backend.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Usability
- Performance

## 9.2.0.0 Test Scenarios

- Verify a driver sees only their own trips.
- Verify correct categorization of trips into 'Current' and 'Past' based on status.
- Verify the 'no trips' message appears for new drivers.
- Verify lazy loading triggers correctly for a driver with a large trip history.
- Verify UI responsiveness on small, medium, and large mobile screen sizes.
- Verify the error message is displayed on API failure.

## 9.3.0.0 Test Data Needs

- A test user with the 'Driver' role.
- Test driver with 0 trips.
- Test driver with a mix of 'Assigned' and 'In-Transit' trips.
- Test driver with a mix of 'Delivered', 'Completed', and 'Canceled' trips.
- Test driver with >100 past trips to test pagination.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Browser developer tools for responsive testing.
- An E2E testing framework like Playwright or Cypress.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests for the backend controller achieve >80% coverage.
- E2E tests for the happy path and 'no trips' scenarios are implemented and passing.
- UI has been manually tested and approved on both a small (e.g., iPhone SE) and large (e.g., Pixel Pro) mobile viewport.
- Performance of the list loading has been verified against requirements.
- Backend API endpoint is confirmed to be secure via record rules.
- Documentation for the OWL component and API endpoint is created.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

3

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a foundational story for the Driver Portal. It should be completed early in the development cycle as it unblocks other driver-facing features like viewing trip details, submitting expenses, and uploading PODs.

## 11.4.0.0 Release Impact

- This feature is critical for the initial release of the Driver Portal functionality.


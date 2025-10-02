# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-057 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Driver views their personal compensation details |
| As A User Story | As a Driver, I want to access a clear and simple v... |
| User Persona | Driver, who primarily accesses the system via a mo... |
| Business Value | Increases driver satisfaction and trust through fi... |
| Functional Area | Driver Portal |
| Story Theme | Driver Financial Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Driver views their expense reimbursements list

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

a Driver is logged into the mobile web portal and has submitted multiple expenses

### 3.1.5 When

the Driver navigates to the 'My Earnings' or 'Compensation' page

### 3.1.6 Then

a section titled 'Expense Reimbursements' is displayed, listing all expenses submitted by that driver.

### 3.1.7 Validation Notes

Verify the list appears and contains entries. Each entry must show at least: Trip ID, Expense Type, Amount, Submission Date, and Status ('Pending Approval', 'Approved', 'Rejected', 'Paid').

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Driver views their earned incentives list

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

a Driver is logged into the mobile web portal and has earned incentives from completed trips

### 3.2.5 When

the Driver navigates to the 'My Earnings' page

### 3.2.6 Then

a section titled 'Incentives' is displayed, listing all incentives earned by that driver.

### 3.2.7 Validation Notes

Verify the list appears and contains entries. Each entry must show at least: Trip ID, Incentive Amount, and Date Earned.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Driver views summary totals for unpaid compensation

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

the Driver is on the 'My Earnings' page

### 3.3.5 When

the page loads with expense and incentive data

### 3.3.6 Then

the page must display a summary total for 'Total Approved Expenses (Unpaid)' and 'Total Incentives Earned (Unpaid)'.

### 3.3.7 Validation Notes

Verify that the totals are calculated correctly, only including items with 'Approved' status and excluding 'Pending', 'Rejected', or 'Paid' items.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Driver filters compensation data by date range

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

the Driver is on the 'My Earnings' page with a history of compensation records

### 3.4.5 When

the Driver selects a date range filter (e.g., 'Last 30 Days')

### 3.4.6 Then

both the expense and incentive lists are updated to show only records within that date range, and the summary totals are recalculated accordingly.

### 3.4.7 Validation Notes

Test with predefined ranges ('This Month', 'Last Month') and a custom date range picker.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Driver views a rejected expense

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

a Driver is on the 'My Earnings' page

### 3.5.5 And

one of their submitted expenses has been 'Rejected' by a manager

### 3.5.6 When

the Driver views the expense list

### 3.5.7 Then

the rejected expense is clearly marked with the 'Rejected' status and the reason for rejection is visible to the driver.

### 3.5.8 Validation Notes

Verify the rejection reason, as entered by the manager, is displayed. The amount of this expense should not be included in the 'Total Approved Expenses (Unpaid)' sum.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

New driver with no compensation data views the page

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

a new Driver with no submitted expenses or earned incentives is logged in

### 3.6.5 When

the Driver navigates to the 'My Earnings' page

### 3.6.6 Then

the system displays a user-friendly message in each section, such as 'You have not submitted any expenses yet.' and 'No incentives earned yet.'

### 3.6.7 Validation Notes

Ensure the page does not show an error or a blank white screen. The summary totals should display as zero.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Driver cannot view another driver's compensation data

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

Driver A is logged into the system

### 3.7.5 When

Driver A attempts to access the compensation data for Driver B (e.g., by manipulating a URL parameter)

### 3.7.6 Then

the system must enforce security rules and prevent access, displaying an 'Access Denied' or similar authorization error.

### 3.7.7 Validation Notes

This must be tested explicitly. The backend query must be filtered by the current user's employee ID.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item in the Driver Portal navigation for 'My Earnings'.
- Two distinct sections on the page: 'Expense Reimbursements' and 'Incentives'.
- A date range filter component (e.g., dropdown with presets and a custom range option).
- Summary cards to display total unpaid amounts.
- List view for expenses and incentives with clear status indicators (e.g., color-coded tags).

## 4.2.0 User Interactions

- Driver can tap on a list item to potentially view more details (e.g., the receipt image for an expense).
- Applying a date filter should refresh the lists and totals without a full page reload (asynchronous update).

## 4.3.0 Display Requirements

- All monetary values must be displayed with the correct currency symbol (e.g., ₹).
- Dates should be in a consistent, easy-to-read format (e.g., DD-MMM-YYYY).
- The layout must be responsive and optimized for mobile screens as per REQ-INT-001.

## 4.4.0 Accessibility Needs

- Ensure sufficient color contrast for status indicators.
- All interactive elements (filters, buttons) must be easily tappable on a mobile device.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-FNC-001

### 5.1.2 Rule Description

A driver can only view their own personal compensation data. Access to other drivers' financial information is strictly prohibited.

### 5.1.3 Enforcement Point

Backend API/Controller level, using Odoo's `ir.rule` for row-level security.

### 5.1.4 Violation Handling

The system returns a 403 Forbidden or equivalent access error.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-FNC-002

### 5.2.2 Rule Description

The 'Total Approved Expenses (Unpaid)' summary must only include expenses with the status 'Approved'.

### 5.2.3 Enforcement Point

Backend calculation logic for the summary API endpoint.

### 5.2.4 Violation Handling

N/A - this is a calculation rule.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-053

#### 6.1.1.2 Dependency Reason

The expense submission feature must exist before a driver can view submitted expenses.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-033

#### 6.1.2.2 Dependency Reason

The expense approval feature must exist to provide the 'Approved' status.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-034

#### 6.1.3.2 Dependency Reason

The expense rejection feature must exist to provide the 'Rejected' status and reason.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-XXX (TBD)

#### 6.1.4.2 Dependency Reason

A mechanism for creating and assigning driver incentives must be implemented. This story depends on the existence of an 'incentive' data model and records.

## 6.2.0.0 Technical Dependencies

- Odoo's `hr.employee` model for driver identification.
- The custom expense management model.
- A new or existing model for tracking driver incentives.

## 6.3.0.0 Data Dependencies

- Requires existing expense records with various statuses for testing.
- Requires existing incentive records for testing.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The 'My Earnings' page must load within 3 seconds on a standard mobile 4G connection.
- API response time for fetching compensation data should be under 500ms for a driver with up to 2 years of history.
- The system should use pagination for API calls if a driver has more than 100 records to display.

## 7.2.0.0 Security

- All data transmission must be over HTTPS.
- Backend logic must enforce strict data ownership, preventing any possibility of one driver viewing another's data, as per REQ-NFR-003.

## 7.3.0.0 Usability

- The interface must be intuitive for non-technical users (drivers) on a mobile device.
- Financial information must be presented clearly and unambiguously.

## 7.4.0.0 Accessibility

- The interface should adhere to WCAG 2.1 Level AA standards, particularly for mobile responsiveness and contrast.

## 7.5.0.0 Compatibility

- The web portal must be functional on the latest versions of Chrome and Safari on both iOS and Android devices.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires creating a new, secure API endpoint in Odoo.
- Requires building a new responsive UI component in OWL for the Driver Portal.
- The logic for calculating summary totals needs to be accurate and performant.
- Depends on the final data model for 'Incentives', which may not be defined yet.

## 8.3.0.0 Technical Risks

- The incentive model might be more complex than anticipated, requiring additional backend logic.
- Performance degradation for drivers with a very large history of expenses if queries are not optimized and paginated.

## 8.4.0.0 Integration Points

- Reads data from the expense management module.
- Reads data from the (to be defined) incentive management module.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security
- Performance

## 9.2.0.0 Test Scenarios

- Verify data for a driver with a mix of approved, pending, rejected, and paid expenses.
- Verify data for a brand new driver with no records.
- Verify data for a driver with only expenses and no incentives, and vice-versa.
- Execute a security test to attempt to access another driver's data via the API.
- Test the date filter with various ranges, including edge cases like leap years.

## 9.3.0.0 Test Data Needs

- Multiple test driver accounts.
- A set of expense records for each driver with all possible statuses.
- A set of incentive records for each driver.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- A browser automation tool like Selenium or Playwright for E2E tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests implemented for backend logic with >80% coverage
- Integration testing completed successfully, verifying the API and UI work together
- UI component is fully responsive and approved by a UX designer or Product Owner
- Security test case for data segregation is created and passed
- Performance of the API endpoint is benchmarked and meets requirements
- Documentation for the new API endpoint is created
- Story deployed and verified in the staging environment by QA

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- Requires clarification on the 'Incentive' data model and how incentive records are generated before development can begin.
- The frontend and backend work can be done in parallel once the API contract is defined.

## 11.4.0.0 Release Impact

This is a key feature for the Driver Portal and is critical for driver adoption and satisfaction. It should be included in the earliest possible release to drivers.


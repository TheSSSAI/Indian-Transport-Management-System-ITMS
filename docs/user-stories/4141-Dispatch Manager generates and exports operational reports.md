# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-036 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager generates and exports operational... |
| As A User Story | As a Dispatch Manager, I want to access, filter, a... |
| User Persona | Dispatch Manager: Responsible for daily logistics,... |
| Business Value | Enables data-driven decision-making to improve ope... |
| Functional Area | Reporting & Analytics |
| Story Theme | Operational Insights |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Accessing the main reporting interface

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged into the system as a Dispatch Manager

### 3.1.5 When

I navigate to the 'Reports' section from the main menu

### 3.1.6 Then

I am presented with a list of available operational reports, including 'Trip Report', 'Vehicle Utilization Report', 'Driver Performance Report', and 'Trip Interruption Report'.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Generating a Trip Report with default filters

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am on the reporting interface and there is existing trip data in the system

### 3.2.5 When

I select the 'Trip Report'

### 3.2.6 Then

The system displays the report for a default date range (e.g., last 30 days) in a sortable table format with columns for Trip ID, Customer, Source, Destination, Driver, Vehicle, Start Date, End Date, and Status.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Applying filters to a report

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am viewing the 'Trip Report'

### 3.3.5 When

I apply filters for a specific date range, customer, and vehicle, and click 'Apply'

### 3.3.6 Then

The report data refreshes to show only the records that match all the selected filter criteria.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Exporting a filtered report to Excel

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I have generated a filtered report on the screen

### 3.4.5 When

I click the 'Export to Excel' button

### 3.4.6 Then

The system initiates a download of an '.xlsx' file that contains the exact data and columns currently displayed in the on-screen report.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Exporting a filtered report to PDF

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

I have generated a filtered report on the screen

### 3.5.5 When

I click the 'Export to PDF' button

### 3.5.6 Then

The system initiates a download of a '.pdf' file, which is well-formatted for printing and includes a header with the report title and the filters that were applied.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Generating a report with no matching data

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

I am on the reporting interface

### 3.6.5 When

I apply filters for which no data exists (e.g., a customer with no trips in the selected date range)

### 3.6.6 Then

The system displays a user-friendly message such as 'No data found for the selected criteria' instead of an empty table or an error.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Generating the Vehicle Utilization Report

### 3.7.3 Scenario Type

Happy_Path

### 3.7.4 Given

I am on the reporting interface

### 3.7.5 When

I select the 'Vehicle Utilization Report' and apply a date range filter

### 3.7.6 Then

The system displays a report with a row for each vehicle, showing columns for Truck Number, Total On-Trip Time, Total Idle Time, and Utilization Percentage for the selected period.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Generating the Driver Performance Report

### 3.8.3 Scenario Type

Happy_Path

### 3.8.4 Given

I am on the reporting interface

### 3.8.5 When

I select the 'Driver Performance Report' and apply a date range filter

### 3.8.6 Then

The system displays a report with a row for each driver, showing columns for Driver Name, Total Trips Completed, On-Time Delivery Percentage, and Total Incentives Earned.

## 3.9.0 Criteria Id

### 3.9.1 Criteria Id

AC-009

### 3.9.2 Scenario

Generating the Trip Interruption Report

### 3.9.3 Scenario Type

Happy_Path

### 3.9.4 Given

I am on the reporting interface

### 3.9.5 When

I select the 'Trip Interruption Report' and apply a date range filter

### 3.9.6 Then

The system displays a report listing all trips that were 'On Hold', with columns for Trip ID, Driver, Vehicle, Halt Reason, Halt Start Time, and Halt Duration.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A main 'Reports' menu item.
- A report selection screen or dropdown.
- Standard filter controls: Date Range Picker, Dropdowns for Customer, Driver, Vehicle.
- 'Apply Filters' and 'Reset Filters' buttons.
- Clearly labeled 'Export to Excel' and 'Export to PDF' buttons.
- A data table with sortable column headers.
- A loading indicator/spinner shown while data is being fetched.

## 4.2.0 User Interactions

- User selects a report to view.
- User configures filters and applies them to refresh the data.
- User can sort the report data by clicking on column headers.
- User clicks an export button to download the report file.

## 4.3.0 Display Requirements

- The applied filters must be clearly displayed above the report data.
- Data in tables should be paginated if the result set is large.
- Monetary values should be formatted correctly (e.g., with currency symbols).

## 4.4.0 Accessibility Needs

- All filter controls and buttons must be keyboard accessible.
- Data tables must use proper HTML tags (`<thead>`, `<tbody>`, `<th>`) for screen reader compatibility.
- Compliant with WCAG 2.1 Level AA standards.

# 5.0.0 Business Rules

- {'rule_id': 'REQ-REP-001', 'rule_description': 'The Dispatch Manager role shall have access to operational reports: Trip, Vehicle Utilization, Driver Performance, and Trip Interruption.', 'enforcement_point': 'Application access control layer (Odoo ir.rule).', 'violation_handling': "The report options will not be visible or accessible to users without the 'Dispatch Manager' or 'Admin' role."}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-026

#### 6.1.1.2 Dependency Reason

Trip data must be created and managed before any trip-related reports can be generated.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-006

#### 6.1.2.2 Dependency Reason

Vehicle master data is required for the Vehicle Utilization Report.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-011

#### 6.1.3.2 Dependency Reason

Driver master data is required for the Driver Performance Report.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-051

#### 6.1.4.2 Dependency Reason

The ability for drivers to report trip halts is required to populate the Trip Interruption Report.

## 6.2.0.0 Technical Dependencies

- Odoo's reporting framework (or a custom view implementation).
- A Python library for Excel generation (e.g., openpyxl).
- A Python library for PDF generation (e.g., reportlab).

## 6.3.0.0 Data Dependencies

- Requires access to historical and real-time data from the Trip, Vehicle, Driver, and Customer models.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- 90% of report generations with standard filters (e.g., 30-day range) should complete and render in under 5 seconds.
- Exporting a report with up to 1,000 rows should complete in under 10 seconds.

## 7.2.0.0 Security

- Access to the reporting module must be restricted based on the user's role as defined in REQ-FNC-001.
- Database queries for reports must be parameterized to prevent SQL injection vulnerabilities.

## 7.3.0.0 Usability

- The filtering interface must be intuitive and easy to use.
- Exported reports must be formatted for easy readability.

## 7.4.0.0 Accessibility

- The system shall strive to meet WCAG 2.1 Level AA accessibility standards.

## 7.5.0.0 Compatibility

- The reporting interface must be fully functional on the latest versions of Chrome, Firefox, and Safari.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires writing multiple, potentially complex, and optimized database queries for data aggregation.
- Integration of third-party libraries for Excel and PDF export.
- Building a flexible and reusable filtering component.
- Handling large datasets efficiently to meet performance requirements.

## 8.3.0.0 Technical Risks

- Poorly optimized database queries could lead to slow report generation and high server load.
- Inconsistencies between on-screen data and exported file data if the data sources differ.

## 8.4.0.0 Integration Points

- Odoo's ORM for data retrieval.
- Odoo's view and controller layers for rendering the UI.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Verify each report type displays the correct columns and data.
- Test all filter combinations for each report.
- Validate the content and format of exported Excel and PDF files.
- Test report generation with an empty database.
- Test report generation with a large volume of data (e.g., 100,000+ trips) to check performance.

## 9.3.0.0 Test Data Needs

- A comprehensive dataset including multiple trips, drivers, vehicles, and customers.
- Data must include trips with various statuses, including those that have been 'On Hold' to test the interruption report.
- Data spanning multiple months to test date range filters effectively.

## 9.4.0.0 Testing Tools

- Pytest for unit and integration tests.
- A browser automation tool like Selenium or Playwright for E2E tests.
- A load testing tool like Locust or JMeter for performance testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests implemented for all data aggregation logic, achieving >80% coverage.
- Integration tests completed for filter and data retrieval functionality.
- E2E tests successfully run by QA, verifying UI, filtering, and export functionality.
- Performance testing confirms that report generation meets the specified NFRs.
- User interface reviewed and approved by the Product Owner.
- Documentation for the reporting feature is updated in the User Manual.
- Story deployed and verified in the staging environment.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story depends on the completion of core trip management and master data user stories.
- Could be broken down into smaller stories, one for each report type, to fit into a single sprint if needed.
- Requires significant QA effort to validate all reports and filter combinations.

## 11.4.0.0 Release Impact

- This is a key feature for the 'Finance & Tracking' phase (Phase 2) of the rollout plan.


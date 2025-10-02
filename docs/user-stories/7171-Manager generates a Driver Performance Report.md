# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-066 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Manager generates a Driver Performance Report |
| As A User Story | As a Dispatch Manager or Admin, I want to generate... |
| User Persona | Dispatch Manager, Admin |
| Business Value | Enables data-driven driver management, improves op... |
| Functional Area | Reporting & Analytics |
| Story Theme | Operational Insights |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Default Report View

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

the user is logged in as a 'Dispatch Manager' or 'Admin'

### 3.1.5 When

the user navigates to the 'Driver Performance Report' page

### 3.1.6 Then

the system displays a report for all 'Active' drivers for the current month by default.

### 3.1.7 Validation Notes

Verify that the default date range filter is set to the current month and the report table is populated.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Report Data Columns

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

the Driver Performance Report is displayed

### 3.2.5 When

the user views the report table

### 3.2.6 Then

the table must contain the following columns: 'Driver Name', 'Total Trips Completed', 'On-Time Delivery %', 'Total Distance (km)', 'Average Fuel Efficiency (km/l)', 'Total Approved Expenses', 'Total Incentives Earned', and 'Number of Critical Events'.

### 3.2.7 Validation Notes

Check for the presence and correct labeling of all specified columns.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Filtering by Date Range and Driver

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

the user is on the Driver Performance Report page

### 3.3.5 When

the user selects a custom date range and filters for one or more specific drivers

### 3.3.6 Then

the report table immediately updates to show data only for the selected drivers and trips that were completed within that date range.

### 3.3.7 Validation Notes

Test with various date ranges and driver selections. Verify that the metrics are recalculated and reflect the filtered data set.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Exporting Report to Excel

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

a Driver Performance Report is displayed on the screen

### 3.4.5 When

the user clicks the 'Export to Excel' button

### 3.4.6 Then

the system generates and downloads an Excel (.xlsx) file containing the exact data and columns currently displayed in the report table.

### 3.4.7 Validation Notes

Open the downloaded file and verify its content matches the on-screen report. The filename should be descriptive, e.g., 'Driver_Performance_Report_2025-01-15.xlsx'.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Exporting Report to PDF

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

a Driver Performance Report is displayed on the screen

### 3.5.5 When

the user clicks the 'Export to PDF' button

### 3.5.6 Then

the system generates and downloads a PDF file containing the exact data and columns currently displayed in the report table, formatted for readability.

### 3.5.7 Validation Notes

Open the downloaded PDF and verify its content and formatting.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

No Data Found for Filters

### 3.6.3 Scenario Type

Edge_Case

### 3.6.4 Given

the user is on the Driver Performance Report page

### 3.6.5 When

the user applies filters that result in no matching trip data

### 3.6.6 Then

the system hides the report table and displays a user-friendly message, such as 'No performance data found for the selected criteria.'

### 3.6.7 Validation Notes

Test with a date range in the future or a driver with no trips.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Calculation of On-Time Delivery Percentage

### 3.7.3 Scenario Type

Alternative_Flow

### 3.7.4 Given

a driver has completed multiple trips with 'Expected Delivery Dates' and POD timestamps

### 3.7.5 When

the system calculates the 'On-Time Delivery %'

### 3.7.6 Then

the value is calculated as `(Number of trips where POD submission timestamp <= Expected Delivery Date) / (Total number of 'Delivered' trips) * 100`.

### 3.7.7 Validation Notes

Verify the calculation with a test dataset including on-time, late, and non-delivered trips. Canceled trips must be excluded.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Handling of Missing Fuel Data

### 3.8.3 Scenario Type

Edge_Case

### 3.8.4 Given

a driver has completed trips but has no 'Diesel' expense entries with odometer readings

### 3.8.5 When

the Driver Performance Report is generated for that driver

### 3.8.6 Then

the 'Average Fuel Efficiency (km/l)' column for that driver displays 'N/A'.

### 3.8.7 Validation Notes

Ensure the system does not show 0 or an error, but a clear indicator of missing data.

## 3.9.0 Criteria Id

### 3.9.1 Criteria Id

AC-009

### 3.9.2 Scenario

Access Control

### 3.9.3 Scenario Type

Error_Condition

### 3.9.4 Given

a user is logged in with a 'Driver' or 'Finance Officer' role

### 3.9.5 When

the user attempts to access the Driver Performance Report URL

### 3.9.6 Then

the system denies access and shows a standard 'Access Denied' page.

### 3.9.7 Validation Notes

Verify that only users with 'Dispatch Manager' or 'Admin' roles can view the report.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Date range filter (with presets like 'This Month', 'Last Quarter')
- Multi-select dropdown with search for filtering by Driver
- Checkbox to 'Include Inactive Drivers'
- Buttons for 'Apply Filters', 'Reset Filters', 'Export to Excel', 'Export to PDF'
- A data table with sortable columns
- Pagination controls if the result set exceeds 25 records

## 4.2.0 User Interactions

- Selecting a date range updates the report.
- Selecting drivers updates the report.
- Clicking a column header sorts the table by that column.
- Clicking export buttons initiates a file download.

## 4.3.0 Display Requirements

- The report must clearly display the active filter criteria.
- All numerical data should be right-aligned for readability.
- The report should have a clear title, e.g., 'Driver Performance Report'.

## 4.4.0 Accessibility Needs

- The report table must use proper `<table>`, `<thead>`, `<tbody>`, and `<th>` tags for screen reader compatibility.
- All filter controls and buttons must have accessible labels.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-REP-01

### 5.1.2 Rule Description

The report must only include data from trips with a status of 'Delivered', 'Completed', 'Invoiced', or 'Paid' for performance calculations.

### 5.1.3 Enforcement Point

Backend data query

### 5.1.4 Violation Handling

Trips with other statuses (e.g., 'Planned', 'In-Transit', 'Canceled') are excluded from the dataset before aggregation.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-REP-02

### 5.2.2 Rule Description

Critical events are defined as 'Accident', 'Repair', and 'Government Stoppage'. The count should only include these specific event types.

### 5.2.3 Enforcement Point

Backend data query

### 5.2.4 Violation Handling

Other event types like 'Fueling' or 'Trip Start' are ignored for this specific metric.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-011

#### 6.1.1.2 Dependency Reason

Requires the Driver Master data model to exist.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Requires the Trip Management feature to create the core trip data.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-050

#### 6.1.3.2 Dependency Reason

Requires the Trip Event logging feature for the 'Number of Critical Events' metric.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-052

#### 6.1.4.2 Dependency Reason

Requires the POD upload feature for the delivery timestamp needed for 'On-Time Delivery %'.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-054

#### 6.1.5.2 Dependency Reason

Requires the Diesel Expense submission feature for the data needed for 'Average Fuel Efficiency'.

## 6.2.0.0 Technical Dependencies

- Odoo's reporting engine (QWeb for PDF)
- A Python library for Excel export (e.g., openpyxl)
- Finalized data models for Trip, Driver, Expense, and Trip Event

## 6.3.0.0 Data Dependencies

- Requires a sufficient amount of historical trip and expense data to be meaningful.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Report generation for a one-year period with 100 drivers should complete in under 5 seconds.
- Database queries must be optimized to avoid full table scans on large tables like trips and expenses.

## 7.2.0.0 Security

- Access to the report must be strictly limited to users with 'Dispatch Manager' and 'Admin' roles via Odoo's access control lists (ACLs) and record rules.

## 7.3.0.0 Usability

- Filters should be intuitive and easy to use.
- The report layout should be clean and uncluttered, presenting data clearly.

## 7.4.0.0 Accessibility

- The report must adhere to WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The report must render correctly on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- The primary complexity is in designing an efficient database query that joins and aggregates data from multiple models (trips, drivers, expenses, events).
- The business logic for calculating derived metrics like 'On-Time Delivery %' and 'Average Fuel Efficiency' needs to be robust and handle edge cases.
- Ensuring the query remains performant as the data volume grows.

## 8.3.0.0 Technical Risks

- A poorly optimized query could lead to slow report generation times, impacting user experience.
- Inaccurate metric calculations if edge cases (e.g., missing data points) are not handled correctly.

## 8.4.0.0 Integration Points

- This feature is an internal integration, reading data from various modules within the TMS Odoo addon.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Verify the accuracy of each metric with a controlled, known dataset.
- Test all filter combinations (date range, single driver, multiple drivers, inactive drivers).
- Test export functionality and validate the contents of the downloaded files.
- Test the 'no data' message.
- Test role-based access control by attempting to access as an unauthorized user.
- Test report performance with a large volume of seeded data.

## 9.3.0.0 Test Data Needs

- A set of drivers (active and inactive).
- A history of trips for these drivers, including some delivered on-time and some late.
- A history of approved expenses, including diesel expenses with odometer readings.
- A log of various trip events, including critical and non-critical ones.

## 9.4.0.0 Testing Tools

- Pytest for unit tests of the calculation logic.
- Odoo's built-in testing framework for integration tests.
- Browser-based E2E testing framework (e.g., Cypress, Playwright) for UI interaction testing.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for all calculation logic implemented with >80% coverage
- Integration tests verifying data aggregation are implemented and passing
- E2E tests for the user flow (filtering, exporting) are passing
- User interface reviewed and approved by the Product Owner
- Performance testing confirms report generation is within the 5-second threshold
- Security access controls are verified
- Relevant user and technical documentation is updated
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story must be scheduled in a sprint after all prerequisite data-capturing stories are completed and deployed.
- Requires a well-defined test dataset to be available in the development/staging environment for proper validation.

## 11.4.0.0 Release Impact

- This is a key feature for management users and a major value-add for the reporting module.


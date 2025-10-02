# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-068 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Manager generates a Vehicle Profitability Report |
| As A User Story | As a Manager (Admin, Dispatch Manager, or Finance ... |
| User Persona | Manager (Admin, Dispatch Manager, Finance Officer) |
| Business Value | Enables data-driven asset management by providing ... |
| Functional Area | Reporting & Analytics |
| Story Theme | Financial Performance Analysis |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Report Generation with Date Filter

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a Manager and have navigated to the 'Reports' section

### 3.1.5 When

I select the 'Vehicle Profitability Report', choose a valid date range, and click 'Generate Report'

### 3.1.6 Then

The system displays a data table with a row for each vehicle that completed at least one trip or incurred an expense within the selected date range.

### 3.1.7 Validation Notes

Verify that the report interface loads and the generate button triggers a data fetch.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Correct Data Columns Displayed

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

A Vehicle Profitability Report has been successfully generated

### 3.2.5 When

I view the report table

### 3.2.6 Then

The table must contain the following sortable columns: 'Truck Number', 'Total Revenue', 'Total Expenses', 'Net Profit', and 'Profit Margin (%)'.

### 3.2.7 Validation Notes

Check for the presence and correct labeling of all required columns. Verify that clicking on each column header sorts the data.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Accurate Revenue Calculation

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

A Vehicle Profitability Report has been generated for a specific date range

### 3.3.5 When

I view the 'Total Revenue' column for a specific vehicle

### 3.3.6 Then

The value must be the sum of the revenue from all trips assigned to that vehicle with a 'Completed' date that falls within the selected date range.

### 3.3.7 Validation Notes

Manually sum the revenue of relevant trips for a test vehicle and compare it with the value in the report.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Accurate and Comprehensive Expense Calculation

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A Vehicle Profitability Report has been generated for a specific date range

### 3.4.5 When

I view the 'Total Expenses' column for a specific vehicle

### 3.4.6 Then

The value must be the sum of all 'Approved' trip-related expenses AND all non-trip-related expenses (e.g., Maintenance, Insurance) associated with that vehicle, where the expense date falls within the selected date range.

### 3.4.7 Validation Notes

Verify that only 'Approved' expenses are included. Manually sum all relevant expenses from different sources for a test vehicle and compare.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Accurate Profit and Margin Calculation

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

A Vehicle Profitability Report has been generated with 'Total Revenue' and 'Total Expenses' calculated

### 3.5.5 When

I view the 'Net Profit' and 'Profit Margin (%)' columns

### 3.5.6 Then

'Net Profit' must be calculated as (Total Revenue - Total Expenses), and 'Profit Margin (%)' must be calculated as ((Net Profit / Total Revenue) * 100), displaying 0 if revenue is zero.

### 3.5.7 Validation Notes

Check the calculated values for correctness based on the revenue and expense columns.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Export Functionality

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A Vehicle Profitability Report is displayed on the screen

### 3.6.5 When

I click the 'Export to Excel' or 'Export to PDF' button

### 3.6.6 Then

The system initiates a download of a file in the selected format, containing the exact data shown in the report table, including a summary row with grand totals.

### 3.6.7 Validation Notes

Open the downloaded files and verify their content and formatting match the on-screen report.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

No Data Available

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

I am on the report generation screen

### 3.7.5 When

I select a date range in which no trips were completed and no vehicle expenses were recorded

### 3.7.6 Then

The system displays a user-friendly message, such as 'No profitability data available for the selected period', instead of an empty table or an error.

### 3.7.7 Validation Notes

Test with a future date range or a past period with known zero activity.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Vehicle with Only Expenses

### 3.8.3 Scenario Type

Edge_Case

### 3.8.4 Given

A vehicle incurred maintenance costs but completed no trips within the selected date range

### 3.8.5 When

I generate the report for that period

### 3.8.6 Then

The vehicle is included in the report with 'Total Revenue' as 0, 'Total Expenses' as the sum of its costs, and a corresponding negative 'Net Profit'.

### 3.8.7 Validation Notes

Set up test data for a vehicle with only non-trip expenses and verify its inclusion and correct negative profit.

## 3.9.0 Criteria Id

### 3.9.1 Criteria Id

AC-009

### 3.9.2 Scenario

Invalid Date Range Input

### 3.9.3 Scenario Type

Error_Condition

### 3.9.4 Given

I am on the report generation screen

### 3.9.5 When

I enter a start date that is after the end date and click 'Generate Report'

### 3.9.6 Then

The system displays a validation error message and does not attempt to generate the report.

### 3.9.7 Validation Notes

Verify the UI prevents submission or shows an immediate error for invalid date logic.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Date range picker (Start Date, End Date)
- Optional filters (e.g., Vehicle Type, specific Vehicle Number)
- 'Generate Report' button
- 'Export to Excel' button
- 'Export to PDF' button
- Sortable data table for displaying results
- Summary row for grand totals

## 4.2.0 User Interactions

- User selects a date range to filter the report.
- User clicks a button to generate/refresh the report data.
- User can click on column headers to sort the data in ascending or descending order.
- User clicks export buttons to download the report.

## 4.3.0 Display Requirements

- The report must clearly display the selected filter criteria (e.g., 'Report for: 01-Oct-2024 to 31-Oct-2024').
- Financial figures should be formatted consistently (e.g., with currency symbols and two decimal places).
- Negative profit values should be clearly indicated (e.g., in red text or with a negative sign).

## 4.4.0 Accessibility Needs

- The report table must use semantic HTML (`<table>`, `<thead>`, `<th>`) for screen reader compatibility.
- All buttons and form controls must have appropriate labels.
- Sufficient color contrast must be used, especially for indicating negative values.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-REP-01

### 5.1.2 Rule Description

Only expenses with an 'Approved' status shall be included in the 'Total Expenses' calculation.

### 5.1.3 Enforcement Point

Backend data aggregation query

### 5.1.4 Violation Handling

Expenses with 'Pending' or 'Rejected' status are filtered out and ignored by the query.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-REP-02

### 5.2.2 Rule Description

Trip revenue is recognized only when the trip status is 'Completed' and its completion date falls within the report's date range.

### 5.2.3 Enforcement Point

Backend data aggregation query

### 5.2.4 Violation Handling

Trips in other statuses ('In-Transit', 'Planned', etc.) are excluded from the revenue calculation.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

Requires the Vehicle Master data model to exist.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Requires Trip records with associated revenue and vehicle assignments.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-033

#### 6.1.3.2 Dependency Reason

Requires the expense approval workflow to exist, as the report only considers 'Approved' expenses.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-041

#### 6.1.4.2 Dependency Reason

Requires the ability to log non-trip-related expenses against a vehicle.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-063

#### 6.1.5.2 Dependency Reason

Requires the core report export functionality (if implemented as a separate framework).

## 6.2.0.0 Technical Dependencies

- Odoo's reporting engine (QWeb for PDF)
- A library for Excel export (e.g., xlsxwriter)

## 6.3.0.0 Data Dependencies

- Access to Vehicle, Trip, and Expense data models.
- Accurate and complete historical data for trips and expenses.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- For a fleet of 100 vehicles, report generation for a 3-month period must complete in under 5 seconds.
- The database query must be optimized to handle at least 2 years of historical data without significant performance degradation.

## 7.2.0.0 Security

- Access to this report must be restricted to users with 'Admin', 'Dispatch Manager', and 'Finance Officer' roles via Odoo's access control lists.

## 7.3.0.0 Usability

- The report interface should be intuitive, requiring minimal training for a manager to generate and interpret the report.

## 7.4.0.0 Accessibility

- The report must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The report must render correctly on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- The database query requires joining multiple models (vehicle, trip, expense) and performing complex aggregations.
- Ensuring query performance over a large dataset is a primary challenge.
- Logic must correctly differentiate between trip-related and non-trip-related expenses and their respective date fields.
- Formatting for PDF and Excel exports can be time-consuming.

## 8.3.0.0 Technical Risks

- A poorly optimized database query could lead to long load times or server timeouts.
- Inaccurate data aggregation if the join conditions or date filters are incorrect.

## 8.4.0.0 Integration Points

- Odoo ORM for data retrieval.
- Odoo's reporting framework for file generation.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Generate report for a standard month.
- Generate report for a period with no activity.
- Generate report including vehicles with only expenses and no revenue.
- Verify calculations for a vehicle with multiple trips and expenses.
- Test export to both PDF and Excel and validate file contents.
- Test role-based access by attempting to access the report as a 'Driver'.

## 9.3.0.0 Test Data Needs

- A set of vehicles with a mix of trip histories.
- Trips with varying revenue.
- A mix of 'Approved', 'Pending', and 'Rejected' expenses.
- Non-trip-related expenses (Maintenance, Fines) with dates inside and outside the test period.

## 9.4.0.0 Testing Tools

- Pytest for backend unit and integration tests.
- Odoo's built-in testing framework.
- Browser-based E2E testing tool (e.g., Cypress, Playwright).

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for all calculation logic, achieving >80% coverage
- Integration testing of the data aggregation query completed successfully
- User interface reviewed and approved by the Product Owner
- Performance requirements verified against a realistic test dataset
- Security access rules are implemented and tested
- Documentation for the report feature is updated in the User Manual
- Story deployed and verified in the staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story should be scheduled after all core data entry stories (trips, expenses) are complete and stable.
- Requires significant QA focus on data accuracy, so adequate time for testing must be allocated.

## 11.4.0.0 Release Impact

This is a key feature for management and a major value-add for the system. Its completion is critical for demonstrating the system's analytical capabilities.


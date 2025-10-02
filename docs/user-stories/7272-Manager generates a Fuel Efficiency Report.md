# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-067 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Manager generates a Fuel Efficiency Report |
| As A User Story | As a Manager (Admin or Dispatch Manager), I want t... |
| User Persona | Admin, Dispatch Manager |
| Business Value | Provides critical insights into a major operationa... |
| Functional Area | Reporting & Analytics |
| Story Theme | Operational Performance Monitoring |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Generate report with valid data

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in Manager on the 'Fuel Efficiency Report' page

### 3.1.5 When

I select a date range and one or more vehicles that have had at least two 'Diesel' expense entries with odometer readings within that period, and I click 'Generate Report'

### 3.1.6 Then

The system displays a table with rows for each selected vehicle, containing columns for 'Vehicle Number', 'Total Distance (km)', 'Total Fuel (Liters)', and 'Fuel Efficiency (km/L)'. The 'Total Distance' is calculated as the difference between the last and first odometer readings within the period. The 'Total Fuel' is the sum of all diesel quantities within the period. The 'Fuel Efficiency' is correctly calculated as (Total Distance / Total Fuel).

### 3.1.7 Validation Notes

Verify the calculations against a manually prepared dataset. For example, if a vehicle has a first odometer reading of 10000km and a last of 11000km, and consumed 200L of diesel in the period, the distance should be 1000km and efficiency should be 5.0 km/L.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Report filtering and display

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

The Fuel Efficiency Report is displayed

### 3.2.5 When

I view the report table

### 3.2.6 Then

The table is sortable by any column header. The report includes filter controls for 'Date Range' (start and end date) and a multi-select dropdown for 'Vehicle'.

### 3.2.7 Validation Notes

Click on each column header to confirm sorting works in ascending and descending order. Verify the vehicle filter allows selecting multiple vehicles.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Vehicle has fuel expenses but no travel (or only one odometer reading)

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

I am on the 'Fuel Efficiency Report' page

### 3.3.5 When

I generate a report for a period where a vehicle has 'Diesel' expenses but only one or zero odometer readings recorded

### 3.3.6 Then

The report row for that vehicle displays 'Total Distance (km)' as 0, and 'Fuel Efficiency (km/L)' as '0' or 'N/A'.

### 3.3.7 Validation Notes

Create test data for a vehicle with a single diesel expense entry in a given month. Generate the report for that month and verify the output.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Vehicle has trips but no diesel expenses recorded

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am on the 'Fuel Efficiency Report' page

### 3.4.5 When

I generate a report for a period where a vehicle has completed trips but no 'Diesel' expenses were submitted

### 3.4.6 Then

The report row for that vehicle displays 'Total Fuel (Liters)' as 0, and 'Fuel Efficiency (km/L)' as 'N/A' or infinity symbol (∞).

### 3.4.7 Validation Notes

Create test data for a vehicle with completed trips but no associated diesel expenses in the test period. Generate the report and verify the output.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Generate report with no data matching filters

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am on the 'Fuel Efficiency Report' page

### 3.5.5 When

I apply filters for which no expense data exists and click 'Generate Report'

### 3.5.6 Then

The system displays a user-friendly message such as 'No data found for the selected criteria' instead of an empty table.

### 3.5.7 Validation Notes

Select a date range in the future or a vehicle with no history and confirm the message is displayed.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Invalid date range filter

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am on the 'Fuel Efficiency Report' page

### 3.6.5 When

I select a 'Start Date' that is after the 'End Date' and click 'Generate Report'

### 3.6.6 Then

The system prevents the report from running and displays a validation error message like 'Start Date cannot be after End Date'.

### 3.6.7 Validation Notes

Attempt to set an invalid date range and verify the error message appears and no report is generated.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Exporting the report

### 3.7.3 Scenario Type

Happy_Path

### 3.7.4 Given

A Fuel Efficiency Report is successfully generated and displayed on the screen

### 3.7.5 When

I click the 'Export to Excel' button

### 3.7.6 Then

The system generates and downloads an Excel file containing the exact data shown in the report table, including headers.

### 3.7.7 Validation Notes

Verify the downloaded file opens correctly and its content matches the on-screen report. This depends on US-063.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Date range picker (Start Date, End Date)
- Multi-select dropdown for 'Vehicle'
- 'Generate Report' button
- 'Export to Excel' button
- 'Export to PDF' button
- Data grid/table for displaying results
- Loading indicator while the report is being generated

## 4.2.0 User Interactions

- User selects date range and vehicles.
- User clicks 'Generate Report' to trigger data fetching and calculation.
- User can sort the results table by clicking on column headers.
- User clicks an export button to download the report.

## 4.3.0 Display Requirements

- The report must clearly display the applied filters.
- The results table must have the following columns: Vehicle Number, Total Distance (km), Total Fuel (Liters), Fuel Efficiency (km/L).
- Numerical values should be formatted to a consistent number of decimal places (e.g., 2 decimal places for efficiency).
- A message indicating 'No data found' should be shown if the query returns no results.

## 4.4.0 Accessibility Needs

- All filter controls and buttons must be keyboard accessible.
- The results table must use proper HTML `<table>`, `<thead>`, `<th>`, and `<tbody>` tags for screen reader compatibility.
- Meets WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-R-01

### 5.1.2 Rule Description

Fuel efficiency calculation is defined as Total Distance / Total Fuel.

### 5.1.3 Enforcement Point

During report generation logic.

### 5.1.4 Violation Handling

If Total Fuel is zero, the result should be handled gracefully (display 'N/A' or '∞') to avoid a division-by-zero error.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-R-02

### 5.2.2 Rule Description

Total Distance for the report is calculated as the difference between the maximum and minimum odometer readings from 'Diesel' expense entries within the selected period for a given vehicle.

### 5.2.3 Enforcement Point

During report generation logic.

### 5.2.4 Violation Handling

If fewer than two odometer readings are available in the period, the distance is considered 0.

## 5.3.0 Rule Id

### 5.3.1 Rule Id

BR-R-03

### 5.3.2 Rule Description

Only expenses of type 'Diesel' are included in the 'Total Fuel' calculation.

### 5.3.3 Enforcement Point

During data aggregation for the report.

### 5.3.4 Violation Handling

N/A. This is a filtering rule.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

Requires the Vehicle Master data model to exist to filter by vehicle.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-053

#### 6.1.2.2 Dependency Reason

Requires the expense submission functionality to exist, as this is the source of fuel data.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-054

#### 6.1.3.2 Dependency Reason

Critically depends on the capture of odometer readings with diesel expenses, which is the source for distance calculation.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-063

#### 6.1.4.2 Dependency Reason

Requires the generic report export functionality to be implemented for the 'Export' buttons to work.

## 6.2.0.0 Technical Dependencies

- Odoo's reporting engine or a custom view implementation.
- Database access to `vehicle`, `expense`, and related models.

## 6.3.0.0 Data Dependencies

- Requires historical expense data of type 'Diesel' with associated vehicle, quantity, and odometer readings.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Report generation for a 1-year period across a fleet of 100 vehicles should complete in under 15 seconds.
- The report page itself should load in under 3 seconds as per REQ-NFR-001.

## 7.2.0.0 Security

- Access to this report must be restricted to users with 'Admin' or 'Dispatch Manager' roles, enforced by Odoo's access control lists (ACLs).

## 7.3.0.0 Usability

- The report interface should be intuitive, requiring minimal training for a manager to use.
- Filter controls should be clearly labeled and easy to operate.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0.0 Compatibility

- The report must render correctly on all supported modern web browsers (Chrome, Firefox, Safari, Edge).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- The data aggregation logic requires careful construction to ensure accuracy, especially for calculating distance from odometer readings.
- Potential for performance issues with large datasets, requiring an optimized database query (e.g., using appropriate indexes on date and foreign key fields).
- Handling edge cases like missing or incomplete data (e.g., only one odometer reading) adds complexity to the business logic.

## 8.3.0.0 Technical Risks

- Inaccurate or missing odometer data from drivers will lead to a useless report. Data quality is a major risk.
- A poorly optimized query could lead to slow report generation and server timeouts, impacting user experience.

## 8.4.0.0 Integration Points

- Reads data from the Expense Management module.
- Reads data from the Vehicle Master module.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance

## 9.2.0.0 Test Scenarios

- Verify calculation accuracy with a known dataset.
- Test with a vehicle having no diesel expenses.
- Test with a vehicle having only one diesel expense entry.
- Test with a vehicle having expenses outside the selected date range.
- Test report generation across a large volume of data to check performance.
- Test the multi-vehicle filter functionality.
- Test the export functionality for both Excel and PDF.

## 9.3.0.0 Test Data Needs

- A set of vehicles with varying numbers of 'Diesel' expense entries.
- Expense entries must have realistic, sequential odometer readings.
- Data should span multiple months to allow for robust date range filtering.
- At least one vehicle with no diesel expenses and one with only a single entry in a given period.

## 9.4.0.0 Testing Tools

- Pytest for backend unit and integration tests.
- Odoo's built-in testing framework.
- Browser-based E2E testing tool like Playwright or Selenium.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by at least one other developer
- Unit tests for the calculation logic achieve >80% code coverage
- Integration tests confirm correct data retrieval from dependent models
- E2E tests for report generation and export are passing
- Performance testing confirms report generation is within the 15-second threshold for the specified load
- Security rules restricting access to authorized roles are verified
- User documentation for generating and interpreting the report is created
- Story deployed and verified in the staging environment by a QA engineer and the Product Owner

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

5

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- The accuracy of this report is highly dependent on the quality of data entered in US-054. Ensure that story has robust validation.
- Allocate time for creating comprehensive test data, as it's crucial for validating the calculations.

## 11.4.0.0 Release Impact

This is a key feature for operational managers and a significant value-add for the reporting module. It should be included in any release focused on operational analytics.


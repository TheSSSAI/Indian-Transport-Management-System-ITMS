# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-064 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Manager views the main dashboard with operational ... |
| As A User Story | As a Manager (Admin or Dispatch Manager), I want t... |
| User Persona | Admin, Dispatch Manager |
| Business Value | Provides an at-a-glance overview of business healt... |
| Functional Area | Reporting & Analytics |
| Story Theme | Operational Oversight |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Dashboard loads successfully for an authorized user

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a user logged in with the 'Admin' or 'Dispatch Manager' role

### 3.1.5 When

I navigate to the main dashboard page

### 3.1.6 Then

The dashboard view loads successfully, and all widgets display a loading state initially, then populate with data.

### 3.1.7 Validation Notes

Verify page load and that all defined widgets are present. Check against performance NFR REQ-NFR-001 (LCP under 3 seconds).

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Vehicle Status widget displays correct data

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am viewing the main dashboard

### 3.2.5 When

the 'Vehicle Status' widget finishes loading

### 3.2.6 Then

I see a pie chart correctly representing the proportion of all 'Active' vehicles in 'Available', 'On-Trip', and 'In-Maintenance' statuses, and hovering over a slice displays the exact vehicle count.

### 3.2.7 Validation Notes

Create vehicles with different statuses and verify the counts and proportions in the chart are accurate.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Clicking on a Vehicle Status slice navigates to a filtered list

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

The 'Vehicle Status' widget is displayed

### 3.3.5 When

I click on the 'On-Trip' slice of the pie chart

### 3.3.6 Then

I am navigated to the Vehicle list view, which is pre-filtered to show only vehicles with the 'On-Trip' status.

### 3.3.7 Validation Notes

Test click-through functionality for each status slice in the pie chart.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Operational and Financial KPI cards display correct values

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I am viewing the main dashboard

### 3.4.5 When

the KPI cards finish loading

### 3.4.6 Then

I see distinct KPI cards for 'Pending Deliveries', 'Delayed Trips', 'Pending Payment Collections', 'Total Revenue (MTD)', and 'Total Expenses (MTD)' displaying the correct, calculated numerical values.

### 3.4.7 Validation Notes

Manually calculate each KPI based on test data and verify the numbers on the dashboard match.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Clicking on a KPI card navigates to a relevant filtered list

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

The KPI cards are displayed

### 3.5.5 When

I click on the 'Delayed Trips' KPI card

### 3.5.6 Then

I am navigated to the Trip list view, pre-filtered to show only trips that are 'In-Transit' and past their 'Expected Delivery Date'.

### 3.5.7 Validation Notes

Test click-through for each KPI card to ensure it navigates to the correct view with the correct filters applied.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Alerts Panel displays critical system alerts

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

There are upcoming document expiries, critical trip events, and low card balances in the system

### 3.6.5 When

I view the 'Alerts Panel' on the dashboard

### 3.6.6 Then

I see a list of these alerts, each clearly stating the issue (e.g., 'Vehicle ABC's Insurance expires in 10 days', 'Trip 123 reported an Accident').

### 3.6.7 Validation Notes

Create test data for each alert type (expiring doc, critical event, low balance) and confirm it appears in the panel.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Dashboard handles a no-data state gracefully

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

The system has no trips, vehicles, or invoices

### 3.7.5 When

I view the main dashboard

### 3.7.6 Then

Each widget and KPI card displays '0' or a 'No Data Available' message instead of showing an error.

### 3.7.7 Validation Notes

Test on a clean database or with data that results in zero counts for all metrics.

## 3.8.0 Criteria Id

### 3.8.1 Criteria Id

AC-008

### 3.8.2 Scenario

Unauthorized user is denied access to the dashboard

### 3.8.3 Scenario Type

Error_Condition

### 3.8.4 Given

I am a user logged in with the 'Driver' role

### 3.8.5 When

I attempt to navigate to the manager dashboard URL

### 3.8.6 Then

I am shown an 'Access Denied' error page and am not able to view the dashboard.

### 3.8.7 Validation Notes

Verify that Odoo's access control rules prevent users without the correct group/role from viewing the dashboard view.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Main dashboard container view
- Pie chart widget for 'Vehicle Status'
- KPI card components for each metric
- Alerts panel/list component
- Date range filter for financial KPIs (optional, for future enhancement if not in scope now)
- Manual 'Refresh' button

## 4.2.0 User Interactions

- Hovering over chart elements reveals tooltips with more data.
- Clicking on chart elements or KPI cards navigates the user to a filtered list view.
- Clicking on an alert navigates the user to the source record of the alert.

## 4.3.0 Display Requirements

- Dashboard must be the default view upon login for Admin and Dispatch Manager roles.
- Financial values should be formatted with appropriate currency symbols and separators.
- Alerts should be sorted by priority/recency.

## 4.4.0 Accessibility Needs

- All widgets must be keyboard navigable.
- Charts must have text alternatives or accessible labels for screen readers.
- Color contrast must meet WCAG 2.1 AA standards.

# 5.0.0 Business Rules

- {'rule_id': 'REQ-REP-002', 'rule_description': "The dashboard must include specific widgets: 'Vehicle Status' (pie chart), KPIs for 'Pending Deliveries', 'Delayed Trips', 'Pending Payment Collections', 'Total Revenue (MTD/YTD)', 'Total Expenses (MTD/YTD)', and an 'Alerts Panel'.", 'enforcement_point': 'Dashboard view rendering', 'violation_handling': "If a widget is missing, it's a feature defect."}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-006

#### 6.1.1.2 Dependency Reason

Vehicle master data is required for the 'Vehicle Status' widget.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-026

#### 6.1.2.2 Dependency Reason

Trip management is required for 'Pending Deliveries' and 'Delayed Trips' KPIs.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-037

#### 6.1.3.2 Dependency Reason

Invoicing is required for 'Pending Payment Collections' and 'Total Revenue' KPIs.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-053

#### 6.1.4.2 Dependency Reason

Expense submission is required for the 'Total Expenses' KPI.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-009

#### 6.1.5.2 Dependency Reason

Vehicle document management is required for the 'Alerts Panel'.

### 6.1.6.0 Story Id

#### 6.1.6.1 Story Id

US-050

#### 6.1.6.2 Dependency Reason

Trip event logging is required for the 'Alerts Panel'.

## 6.2.0.0 Technical Dependencies

- Odoo Web Library (OWL) for custom view development.
- Odoo's ORM for data aggregation queries.

## 6.3.0.0 Data Dependencies

- Requires access to Vehicle, Trip, Invoice, Account Payment, and Expense models.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- Dashboard page must achieve a Largest Contentful Paint (LCP) of under 3 seconds as per REQ-NFR-001.
- Data aggregation queries must be optimized to complete in under 500ms to avoid blocking the UI.

## 7.2.0.0 Security

- Access to the dashboard view must be strictly controlled by user roles ('Admin', 'Dispatch Manager').
- Data displayed must be limited by any applicable record rules.

## 7.3.0.0 Usability

- The dashboard must provide a clear, intuitive, and high-level summary of the business state.
- Navigation from the dashboard to detailed views must be simple and direct.

## 7.4.0.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0.0 Compatibility

- The dashboard must be fully responsive and functional on screen sizes from 360px width upwards as per REQ-INT-001.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Medium

## 8.2.0.0 Complexity Factors

- Requires building a custom dashboard view in Odoo, which is more complex than standard form/list views.
- Involves writing multiple, potentially complex data aggregation queries across several models.
- Ensuring the performance of these queries is critical and may require optimization (e.g., indexing, materialized views if necessary).

## 8.3.0.0 Technical Risks

- Performance degradation as data volume grows. Queries must be written scalably.
- Complexity in creating a responsive and interactive dashboard using OWL.

## 8.4.0.0 Integration Points

- Reads data from `tms.vehicle`, `tms.trip`, `account.move` (Invoices), `tms.expense`, and `hr.employee` models.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Performance
- Accessibility

## 9.2.0.0 Test Scenarios

- Verify each KPI calculation with known test data.
- Verify click-through navigation from each widget and KPI.
- Verify correct behavior when no data exists for a given metric.
- Verify access control for different user roles.
- Test dashboard rendering and functionality on mobile and desktop viewports.

## 9.3.0.0 Test Data Needs

- A set of vehicles with various statuses.
- Multiple trips, including some that are delayed.
- Invoices in 'Posted' and 'Paid' states.
- Approved and pending expenses.
- Vehicle/driver documents with near-future expiry dates.

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.
- Browser developer tools for performance (LCP) and accessibility checks.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for all KPI calculation logic with >80% coverage
- Integration testing completed successfully to verify data fetching
- User interface reviewed and approved by the Product Owner
- Performance requirements (LCP < 3s) verified
- Security requirements (role-based access) validated
- Dashboard is confirmed to be responsive on mobile viewport (360px width)
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

8

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a 'capstone' feature and depends on many other core functionalities. It should be scheduled in a later sprint after all prerequisite stories are completed and stable.

## 11.4.0.0 Release Impact

- This is a key feature for management users and a major selling point of the system. Its completion is critical for User Acceptance Testing (UAT).


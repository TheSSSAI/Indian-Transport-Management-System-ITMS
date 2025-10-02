# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-085 |
| Elaboration Date | 2025-01-24 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | System calculates trip profitability using only ap... |
| As A User Story | As a Dispatch Manager or Finance Officer, I want t... |
| User Persona | Dispatch Manager, Finance Officer, Admin |
| Business Value | Ensures financial accuracy in reporting by prevent... |
| Functional Area | Financial Management & Reporting |
| Story Theme | Trip Profitability Analysis |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Profitability calculation with mixed expense statuses

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A trip exists with a total revenue of 25,000 INR

### 3.1.5 And

the system must display the final 'Trip Profitability' as 15,500 INR (25,000 - 9,500).

### 3.1.6 When

a user with appropriate permissions views the trip's details or a profitability report containing this trip

### 3.1.7 Then

the system must display the 'Total Approved Expenses' as 9,500 INR (8,000 + 1,500)

### 3.1.8 Validation Notes

Verify the profitability calculation on the Trip Form View and in the Trip Profitability Report.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Profitability calculation when an expense is approved

### 3.2.3 Scenario Type

Alternative_Flow

### 3.2.4 Given

A trip exists with a total revenue of 25,000 INR and one 'Approved' expense of 8,000 INR, showing a current profitability of 17,000 INR

### 3.2.5 And

the trip's 'Trip Profitability' must be automatically updated to 16,500 INR.

### 3.2.6 When

a Dispatch Manager changes the status of the 'Food' expense from 'Pending' to 'Approved'

### 3.2.7 Then

the trip's 'Total Approved Expenses' must be recalculated to 8,500 INR

### 3.2.8 Validation Notes

Check the Trip Form View after approving the expense. The profitability value should update upon page refresh or via AJAX if implemented.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Profitability calculation with no approved expenses

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

A trip exists with a total revenue of 15,000 INR

### 3.3.5 And

the system must display the 'Trip Profitability' as 15,000 INR (equal to the total revenue).

### 3.3.6 When

a user views the trip's details

### 3.3.7 Then

the system must display the 'Total Approved Expenses' as 0 INR

### 3.3.8 Validation Notes

Verify that expenses not in 'Approved' state do not affect the calculation.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Profitability calculation with no expenses submitted

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

A trip exists with a total revenue of 20,000 INR

### 3.4.5 And

the system must display the 'Trip Profitability' as 20,000 INR.

### 3.4.6 When

a user views the trip's details

### 3.4.7 Then

the system must display the 'Total Approved Expenses' as 0 INR

### 3.4.8 Validation Notes

Ensure the calculation handles an empty set of expense records gracefully.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Profitability calculation when an approved expense is edited

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

A trip has a revenue of 10,000 INR and one 'Approved' expense of 2,000 INR, showing a profitability of 8,000 INR

### 3.5.5 When

a user with permission edits the amount of the 'Approved' expense to 2,500 INR

### 3.5.6 Then

the trip's 'Trip Profitability' must be recalculated and updated to 7,500 INR.

### 3.5.7 Validation Notes

This tests that the calculation is dependent on both the status and the amount of the expense records.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A non-editable field on the Trip Form View to display 'Total Approved Expenses'.
- A non-editable field on the Trip Form View to display 'Trip Profitability'.

## 4.2.0 User Interactions

- The profitability calculation is automatic and requires no direct user interaction.
- The displayed values should update automatically or upon a page refresh after a related expense's status or amount is changed.

## 4.3.0 Display Requirements

- The profitability calculation (Revenue - Approved Expenses) must be clearly displayed on the main form view for a Trip.
- The same calculated value must be used as the basis for all profitability-related reports (e.g., Trip Profitability Report, Vehicle Profitability Report).

## 4.4.0 Accessibility Needs

- Displayed financial figures should have appropriate labels for screen readers.

# 5.0.0 Business Rules

- {'rule_id': 'BR-PROFIT-01', 'rule_description': "Only expense records with a status of 'Approved' shall be included in the sum of total expenses for any profitability calculation.", 'enforcement_point': 'System-wide, wherever trip profitability is calculated or displayed (e.g., computed fields, report queries).', 'violation_handling': 'N/A. This is a calculation rule; violations are not possible if implemented correctly.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-026

#### 6.1.1.2 Dependency Reason

Requires the Trip model to exist, which holds the revenue value.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-053

#### 6.1.2.2 Dependency Reason

Requires the Expense model and the ability for drivers to submit expenses associated with a trip.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-033

#### 6.1.3.2 Dependency Reason

Requires the functionality for a Dispatch Manager to approve an expense, which sets the 'Approved' status.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

REQ-FNC-007

#### 6.1.4.2 Dependency Reason

This story is the direct implementation of the profitability calculation requirement.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM for creating a computed field.
- The existence of a 'Trip' model with a revenue field.
- The existence of an 'Expense' model with amount and status fields, linked to a Trip.

## 6.3.0.0 Data Dependencies

- Requires trip records with revenue data.
- Requires expense records with status ('Approved', 'Pending', 'Rejected') and amount data.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The profitability calculation for a single trip view must complete in under 200ms.
- Reports aggregating profitability across many trips must not cause significant database load or timeouts.

## 7.2.0.0 Security

- The visibility of profitability figures must be restricted by role-based access control as defined in REQ-FNC-001. For example, a 'Driver' must not be able to see trip revenue or profitability.

## 7.3.0.0 Usability

- The breakdown of the calculation (Revenue, Approved Expenses, Profit) should be transparent to the user on the Trip form to build trust.

## 7.4.0.0 Accessibility

- WCAG 2.1 Level AA standards apply.

## 7.5.0.0 Compatibility

- The display must be correct on all supported browsers and mobile-responsive views.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- The logic is a straightforward filtered database aggregation.
- Implementation in Odoo is standard using a computed field.
- Dependencies must be correctly defined in the `@api.depends` decorator to ensure the field recalculates when an associated expense's status or amount changes.

## 8.3.0.0 Technical Risks

- Minor risk of performance issues if the profitability field is added to a list view with thousands of records. The computation should be optimized to avoid N+1 query problems.
- Incorrectly configured dependencies for the computed field could lead to stale data being displayed.

## 8.4.0.0 Integration Points

- Trip Model (Odoo)
- Expense Model (Odoo)
- Reporting Module (Odoo)

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0.0 Test Scenarios

- Verify calculation with one approved, one pending, one rejected expense.
- Verify calculation with zero approved expenses.
- Verify calculation with zero expenses.
- Verify that approving a pending expense correctly updates the profitability.
- Verify that changing the amount of an approved expense correctly updates the profitability.
- Verify that the value in the Trip Profitability Report matches the value on the Trip Form View.

## 9.3.0.0 Test Data Needs

- A test trip with a defined revenue.
- Multiple expense records associated with the test trip, with different statuses ('Approved', 'Pending', 'Rejected') and amounts.

## 9.4.0.0 Testing Tools

- Pytest for Odoo unit tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code is peer-reviewed and merged into the main development branch.
- Unit tests for the computed field logic are implemented, achieving >80% coverage for the new code, and are passing in the CI/CD pipeline.
- Integration tests confirm that changing an expense status correctly triggers recalculation.
- The profitability figure is correctly displayed on the Trip Form View and used in the Trip Profitability Report.
- No performance degradation is observed on trip list or form views.
- Role-based access to profitability data is confirmed to be working as specified.
- Relevant technical documentation is updated.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a core financial feature and is critical for business value. It should be prioritized as soon as its prerequisite stories (expense creation and approval) are complete.

## 11.4.0.0 Release Impact

- Enables key financial reporting features. Without this, the profitability reports are not possible or would be inaccurate.


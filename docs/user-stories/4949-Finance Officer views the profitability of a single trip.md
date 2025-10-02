# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-044 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer views the profitability of a singl... |
| As A User Story | As a Finance Officer, I want to view the calculate... |
| User Persona | Finance Officer. This user is responsible for fina... |
| Business Value | Provides granular financial insight into individua... |
| Functional Area | Financial Management & Reporting |
| Story Theme | Trip Lifecycle Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Profitability calculation for a profitable trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as a Finance Officer and viewing a 'Completed' trip with a revenue of ₹50,000 and two associated expenses with 'Approved' status, one for ₹10,000 and another for ₹5,000.

### 3.1.5 When

I open the form view of this trip.

### 3.1.6 Then

I must see a dedicated profitability section that displays 'Total Revenue: ₹50,000', 'Total Approved Expenses: ₹15,000', and 'Net Profitability: ₹35,000'.

### 3.1.7 Validation Notes

Verify the calculation is Revenue - SUM(Approved Expenses). The values should be clearly labeled and formatted as currency.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Profitability calculation for a trip resulting in a loss

### 3.2.3 Scenario Type

Edge_Case

### 3.2.4 Given

I am logged in as a Finance Officer and viewing a 'Completed' trip with a revenue of ₹20,000 and approved expenses totaling ₹22,000.

### 3.2.5 When

I open the form view of this trip.

### 3.2.6 Then

The profitability section must display 'Net Profitability: -₹2,000', and the value should be visually highlighted (e.g., in red text) to indicate a loss.

### 3.2.7 Validation Notes

Confirm that negative values are calculated and displayed correctly and are visually distinct from positive values.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Calculation correctly ignores non-approved expenses

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am logged in as a Finance Officer and viewing a trip with a revenue of ₹30,000. The trip has one 'Approved' expense of ₹8,000, one 'Pending' expense of ₹1,500, and one 'Rejected' expense of ₹500.

### 3.3.5 When

I view the profitability section for this trip.

### 3.3.6 Then

The 'Total Approved Expenses' must be displayed as ₹8,000, and the 'Net Profitability' must be calculated as ₹22,000, correctly excluding the pending and rejected expenses.

### 3.3.7 Validation Notes

Check the underlying query or function to ensure it filters expenses strictly by 'Approved' status.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Profitability for a trip with no expenses

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

I am logged in as a Finance Officer and viewing a 'Completed' trip with a revenue of ₹40,000 and no associated expenses.

### 3.4.5 When

I open the form view of this trip.

### 3.4.6 Then

The profitability section must display 'Total Approved Expenses: ₹0' and 'Net Profitability: ₹40,000'.

### 3.4.7 Validation Notes

Ensure the system handles cases with zero expenses gracefully without errors.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Role-based access control for profitability data

### 3.5.3 Scenario Type

Security

### 3.5.4 Given

I am logged in as a Driver and am assigned to a trip.

### 3.5.5 When

I open the view for my assigned trip.

### 3.5.6 Then

I must not be able to see the 'Total Revenue', 'Total Approved Expenses', or 'Net Profitability' fields or section.

### 3.5.7 Validation Notes

Test by logging in with a 'Driver' role. This must be enforced by Odoo's record rules or group-based view inheritance.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Profitability display for trips in pre-completion states

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

I am logged in as a Finance Officer and viewing a trip with a status of 'In-Transit'.

### 3.6.5 When

I open the form view of this trip.

### 3.6.6 Then

The profitability section should be visible but must include a clear visual indicator or text (e.g., 'Provisional', 'Not Final') to signify that the calculation is subject to change.

### 3.6.7 Validation Notes

Verify that the UI communicates the non-final state of the calculation for ongoing trips.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A dedicated 'Profitability' section or widget on the Trip form view.
- Read-only fields for 'Total Revenue', 'Total Approved Expenses', and 'Net Profitability'.
- A visual indicator (e.g., red text color) for negative profitability values.

## 4.2.0 User Interactions

- The 'Total Approved Expenses' value should ideally be a clickable link that opens a filtered list view of the approved expenses for that specific trip.

## 4.3.0 Display Requirements

- All financial figures must be displayed with the correct currency symbol (e.g., ₹).
- Labels must be clear and unambiguous.
- The profitability section must be visible to Admin, Dispatch Manager, and Finance Officer roles, but hidden from the Driver role.

## 4.4.0 Accessibility Needs

- If color is used to indicate profit/loss, it must not be the only means of conveying the information. The negative sign (-) is sufficient. Color should meet WCAG 2.1 AA contrast ratios.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

REQ-FNC-007

### 5.1.2 Rule Description

Profitability is calculated as Revenue minus the sum of all 'Approved' trip-related expenses.

### 5.1.3 Enforcement Point

On the Trip model, whenever the profitability fields are computed or displayed.

### 5.1.4 Violation Handling

N/A - This is a calculation rule.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

REQ-FNC-001

### 5.2.2 Rule Description

A user with the 'Driver' role shall not be able to view company financial data, such as trip revenue or overall profitability.

### 5.2.3 Enforcement Point

At the view layer (XML) and model layer (ir.rule) to restrict field access.

### 5.2.4 Violation Handling

The fields will be hidden or inaccessible to unauthorized roles.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-026

#### 6.1.1.2 Dependency Reason

The Trip model must exist with a field for 'Rate' (Revenue) to be used in the calculation.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-053

#### 6.1.2.2 Dependency Reason

The Expense model must exist and be linkable to a Trip record.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-033

#### 6.1.3.2 Dependency Reason

The Expense model must have an approval status ('Approved', 'Pending', 'Rejected') as the calculation relies on it.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-070

#### 6.1.4.2 Dependency Reason

The core Role-Based Access Control framework must be in place to enforce security requirements.

## 6.2.0.0 Technical Dependencies

- Odoo 18 framework
- Odoo's ORM for computed fields
- Odoo's security model (`ir.rule`, `ir.model.access.csv`)

## 6.3.0.0 Data Dependencies

- Requires existing Trip records with revenue data.
- Requires existing Expense records linked to trips with various statuses.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The profitability calculation must not add more than 50ms to the Trip form view load time.
- The database query to sum approved expenses must be optimized to handle trips with a large number of expense entries.

## 7.2.0.0 Security

- Access to profitability data must be strictly limited to authorized roles (Admin, Dispatch Manager, Finance Officer) using Odoo's built-in security mechanisms.

## 7.3.0.0 Usability

- The profitability information must be presented clearly and concisely, making it easy for a user to understand a trip's financial outcome at a glance.

## 7.4.0.0 Accessibility

- Must adhere to WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0.0 Compatibility

- The feature must render correctly on all supported modern web browsers and be responsive on mobile screen sizes.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- This is a standard Odoo development task involving computed fields and view modifications.
- The logic for calculation is straightforward.
- Security implementation uses standard Odoo patterns.

## 8.3.0.0 Technical Risks

- A poorly optimized query for summing expenses could lead to performance degradation on trips with many expense entries, though this is a low risk.

## 8.4.0.0 Integration Points

- This feature reads data from the Trip model and the Expense model.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify calculation with positive, negative, and zero profit.
- Verify calculation with zero, one, and multiple approved expenses.
- Verify that pending and rejected expenses are ignored.
- Log in as each user role (Admin, Dispatch Manager, Finance Officer, Driver) to confirm access permissions are correctly enforced.
- Click the 'Total Approved Expenses' link to ensure it navigates to the correct filtered list.

## 9.3.0.0 Test Data Needs

- A set of trip records in various states ('In-Transit', 'Completed', 'Invoiced').
- Trips with a mix of expense records having 'Approved', 'Pending', and 'Rejected' statuses.
- User accounts for each defined role.

## 9.4.0.0 Testing Tools

- Pytest for unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing in a staging environment.
- Code has been peer-reviewed and merged into the main branch.
- Unit tests for the calculation logic have been written and achieve >80% coverage.
- Integration tests confirming the interaction between Trip and Expense models are passing.
- A QA engineer has manually verified the UI and security rules for all relevant user roles.
- Performance impact on the Trip form view load time is confirmed to be within acceptable limits.
- The feature is documented in the user manual.
- Story has been demonstrated to the Product Owner and accepted.

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is a key financial feature and provides significant business value.
- Ensure all prerequisite stories related to Trip and Expense management are completed before starting this one.

## 11.4.0.0 Release Impact

- This is a core feature for the financial module and is essential for the Phase 2 rollout (Finance & Tracking).


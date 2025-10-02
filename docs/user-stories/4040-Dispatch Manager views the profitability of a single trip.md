# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-035 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Dispatch Manager views the profitability of a sing... |
| As A User Story | As a Dispatch Manager, I want to view the automati... |
| User Persona | Dispatch Manager. This user is responsible for the... |
| Business Value | Provides immediate visibility into the financial h... |
| Functional Area | Trip Management |
| Story Theme | Financial Oversight and Reporting |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Profitability calculation for a profitable trip

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A Dispatch Manager is viewing a trip record with a 'Total Revenue' of ₹50,000

### 3.1.5 When

The trip has associated expenses with a status of 'Approved' totaling ₹12,000, and other expenses that are 'Pending' or 'Rejected'

### 3.1.6 Then

A profitability section on the trip form displays 'Total Revenue' as ₹50,000, 'Total Approved Expenses' as ₹12,000, and 'Profitability' as ₹38,000.

### 3.1.7 Validation Notes

Verify the calculation is Revenue - SUM(Approved Expenses). Ensure pending/rejected expenses are excluded.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Profitability calculation for a loss-making trip

### 3.2.3 Scenario Type

Edge_Case

### 3.2.4 Given

A Dispatch Manager is viewing a trip record with a 'Total Revenue' of ₹20,000

### 3.2.5 When

The trip has 'Approved' expenses totaling ₹22,500

### 3.2.6 Then

The 'Profitability' field displays -₹2,500 and the value is visually highlighted (e.g., colored red).

### 3.2.7 Validation Notes

Confirm that negative values are calculated correctly and are visually distinct.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Profitability calculation with no approved expenses

### 3.3.3 Scenario Type

Edge_Case

### 3.3.4 Given

A Dispatch Manager is viewing a trip record with a 'Total Revenue' of ₹30,000

### 3.3.5 When

The trip has no expenses or all its expenses are in 'Pending' or 'Rejected' status

### 3.3.6 Then

The 'Total Approved Expenses' field displays ₹0.00 and the 'Profitability' field displays ₹30,000.

### 3.3.7 Validation Notes

Test with zero expense records and with expense records that are not yet approved.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Role-based access control for profitability data

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A user with the 'Driver' role is logged into the system

### 3.4.5 When

They view the details of their assigned trip

### 3.4.6 Then

The entire profitability section (including Total Revenue, Total Approved Expenses, and Profitability fields) is not visible.

### 3.4.7 Validation Notes

Verify using Odoo's field-level or view-level security mechanisms. This is a critical security requirement based on REQ-FNC-001.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Profitability calculation updates after an expense is approved

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

A Dispatch Manager is viewing a trip with a calculated profitability of ₹15,000

### 3.5.5 When

The manager approves a new 'Pending' expense of ₹1,000 for that same trip

### 3.5.6 Then

The 'Total Approved Expenses' value updates to include the new expense, and the 'Profitability' value is recalculated and displayed as ₹14,000 upon view refresh.

### 3.5.7 Validation Notes

Ensure the computed field's dependencies are correctly configured to trigger recalculation when related expense records change.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A dedicated section or group on the Trip Form View labeled 'Profitability Summary'.
- Read-only currency fields for 'Total Revenue', 'Total Approved Expenses', and 'Profitability'.

## 4.2.0 User Interactions

- The profitability fields are for display only and are not editable by the user.
- The values are automatically calculated and updated by the system.

## 4.3.0 Display Requirements

- All values must be formatted as currency with the appropriate symbol (e.g., ₹).
- Negative profitability values must be clearly indicated with a minus sign and should be visually distinct (e.g., red text).

## 4.4.0 Accessibility Needs

- Color should not be the only indicator for negative values; a standard minus sign (-) must be used, per WCAG guidelines.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-FNC-007-1

### 5.1.2 Rule Description

Profitability is calculated as Total Revenue minus the sum of all 'Approved' trip-related expenses.

### 5.1.3 Enforcement Point

System-wide, on the Trip model's computed field.

### 5.1.4 Violation Handling

N/A - System calculation.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-FNC-001-1

### 5.2.2 Rule Description

Users with the 'Driver' role are not permitted to view trip revenue or profitability data.

### 5.2.3 Enforcement Point

Application access control layer (Odoo ir.rule, ir.model.access.csv, and view XML).

### 5.2.4 Violation Handling

The fields and their values will be hidden from the user interface for unauthorized roles.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-026

#### 6.1.1.2 Dependency Reason

Requires the Trip model to exist with a field for revenue/rate.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-053

#### 6.1.2.2 Dependency Reason

Requires the ability to create expense records and associate them with a trip.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-033

#### 6.1.3.2 Dependency Reason

Requires the expense management workflow, including the ability to set an expense status to 'Approved'.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-070

#### 6.1.4.2 Dependency Reason

Requires the core Role-Based Access Control framework to be in place to secure the financial data.

## 6.2.0.0 Technical Dependencies

- Odoo 18 ORM with support for computed fields.
- Odoo's view inheritance mechanism for modifying the Trip form view.

## 6.3.0.0 Data Dependencies

- Requires existing Trip records with revenue data.
- Requires existing Expense records linked to trips, with a status field.

## 6.4.0.0 External Dependencies

*No items available*

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The profitability calculation must not introduce any noticeable delay (>200ms) to the loading time of the Trip form view, as per REQ-NFR-001.

## 7.2.0.0 Security

- Access to profitability fields must be strictly limited to authorized roles (e.g., Admin, Dispatch Manager, Finance Officer) and explicitly denied to others (e.g., Driver).

## 7.3.0.0 Usability

- The profitability summary must be presented in a clear, easily scannable format within the main trip view.

## 7.4.0.0 Accessibility

- The feature must adhere to WCAG 2.1 Level AA standards, particularly regarding the use of color to convey information.

## 7.5.0.0 Compatibility

- The feature must render correctly on all supported browsers and on mobile-responsive views.

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

Low

## 8.2.0.0 Complexity Factors

- Implementation requires creating computed fields in the Odoo model.
- Requires modifying the XML view to display the new fields.
- Requires careful configuration of field-level security to restrict access.

## 8.3.0.0 Technical Risks

- Incorrectly defining the dependencies for the computed field could lead to stale data that doesn't update when expenses are approved.
- Misconfiguration of access control rules could lead to a data leak, exposing financial information to unauthorized users.

## 8.4.0.0 Integration Points

- Directly integrates with the Trip model and the Expense model within the Odoo application.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration
- E2E
- Security

## 9.2.0.0 Test Scenarios

- Verify calculation with positive, negative, and zero profitability.
- Verify calculation with zero expenses and with only non-approved expenses.
- Log in as a Dispatch Manager and confirm visibility and correctness of data.
- Log in as a Driver and confirm the profitability section is not visible.
- Approve a pending expense and verify the profitability figure updates on the trip form.

## 9.3.0.0 Test Data Needs

- A set of users with different roles (Dispatch Manager, Driver, Admin).
- Trip records with varying revenue amounts.
- Expense records linked to trips with different statuses ('Approved', 'Pending', 'Rejected').

## 9.4.0.0 Testing Tools

- Pytest for backend unit tests.
- Odoo's built-in testing framework for integration tests.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests for the computation logic implemented and passing with >80% coverage
- Integration testing completed successfully
- User interface reviewed and approved by the Product Owner
- Security requirements validated by testing with different user roles
- Documentation updated appropriately
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

2

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This story is dependent on the completion of core trip and expense management stories. It should be scheduled in a sprint after those prerequisites are met.

## 11.4.0.0 Release Impact

- This is a key feature for the Dispatch Manager persona, providing significant value by linking operational actions to financial outcomes.


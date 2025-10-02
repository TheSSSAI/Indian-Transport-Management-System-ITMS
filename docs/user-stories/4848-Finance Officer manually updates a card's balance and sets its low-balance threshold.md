# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-043 |
| Elaboration Date | 2024-10-27 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer manually updates a card's balance ... |
| As A User Story | As a Finance Officer, I want to manually update th... |
| User Persona | Finance Officer. This user is responsible for mana... |
| Business Value | Enables proactive management of prepaid card funds... |
| Functional Area | Financial Management |
| Story Theme | Card Balance Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successfully update a card's balance

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in Finance Officer viewing the form for a specific FASTag or diesel card

### 3.1.5 When

I enter a new, valid positive number in the 'Current Balance' field and save the record

### 3.1.6 Then

The system must save the new balance, and the updated value must be displayed on the card's record.

### 3.1.7 Validation Notes

Verify the new balance value is persisted in the database and correctly displayed on the form view after a page refresh.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Successfully set a low-balance threshold

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am a logged-in Finance Officer viewing the form for a specific card

### 3.2.5 When

I enter a valid positive number in the 'Low-Balance Threshold' field and save the record

### 3.2.6 Then

The system must save the new threshold, and the updated value must be displayed on the card's record.

### 3.2.7 Validation Notes

Verify the new threshold value is persisted in the database and correctly displayed on the form view.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Updating balance below the threshold triggers an alert

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

I am a logged-in Finance Officer viewing a card record with a 'Low-Balance Threshold' set to 1000

### 3.3.5 When

I update the 'Current Balance' to 999 and save the record

### 3.3.6 Then

The system must trigger the low-balance alert mechanism for this card, as defined in US-081.

### 3.3.7 Validation Notes

Requires integration with the alert system. Test by checking if the corresponding alert is generated in the system (e.g., an Odoo notification or email is queued).

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Attempt to save with non-numeric balance

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

I am a logged-in Finance Officer editing a card record

### 3.4.5 When

I enter 'abc' into the 'Current Balance' field and attempt to save

### 3.4.6 Then

The system must prevent the save operation and display a user-friendly validation error message, such as 'Current Balance must be a valid number.'

### 3.4.7 Validation Notes

Check that the record is not saved and an inline validation message appears next to the field.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Attempt to save with a negative balance

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

I am a logged-in Finance Officer editing a card record

### 3.5.5 When

I enter '-100' into the 'Current Balance' field and attempt to save

### 3.5.6 Then

The system must prevent the save operation and display a validation error message, such as 'Current Balance cannot be negative.'

### 3.5.7 Validation Notes

Verify using a model-level constraint. The save action should fail, and an error dialog should appear.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Attempt to save with a negative threshold

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

I am a logged-in Finance Officer editing a card record

### 3.6.5 When

I enter '-50' into the 'Low-Balance Threshold' field and attempt to save

### 3.6.6 Then

The system must prevent the save operation and display a validation error message, such as 'Low-Balance Threshold cannot be negative.'

### 3.6.7 Validation Notes

Verify using a model-level constraint. The save action should fail, and an error dialog should appear.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Updating balance to a value equal to the threshold

### 3.7.3 Scenario Type

Edge_Case

### 3.7.4 Given

I am a logged-in Finance Officer viewing a card record with a 'Low-Balance Threshold' set to 1000

### 3.7.5 When

I update the 'Current Balance' to 1000 and save the record

### 3.7.6 Then

The system must save the record successfully and must NOT trigger the low-balance alert.

### 3.7.7 Validation Notes

Confirm that no alert is generated. The alert should only trigger when the balance is strictly less than the threshold.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- An editable numeric input field for 'Current Balance' on the card model's form view.
- An editable numeric input field for 'Low-Balance Threshold' on the card model's form view.
- Standard Odoo 'Save' and 'Discard' buttons.

## 4.2.0 User Interactions

- User can type or paste numeric values into the fields.
- The system provides immediate feedback on invalid input format (e.g., non-numeric characters).
- Saving the form commits the changes to both fields simultaneously.

## 4.3.0 Display Requirements

- The 'Current Balance' and 'Low-Balance Threshold' fields should be clearly labeled.
- Balance and threshold values should be formatted as currency or a number with two decimal places for consistency.

## 4.4.0 Accessibility Needs

- All input fields must have associated labels for screen reader compatibility.
- Validation error messages must be programmatically associated with their respective fields.

# 5.0.0 Business Rules

## 5.1.0 Rule Id

### 5.1.1 Rule Id

BR-CARD-001

### 5.1.2 Rule Description

Card balance and threshold values must be non-negative.

### 5.1.3 Enforcement Point

On save/update of the card record.

### 5.1.4 Violation Handling

The system will raise a validation error and prevent the record from being saved.

## 5.2.0 Rule Id

### 5.2.1 Rule Id

BR-CARD-002

### 5.2.2 Rule Description

A low-balance alert is triggered only when the current balance falls strictly below the defined threshold.

### 5.2.3 Enforcement Point

On save/update of the card record, after the balance field is modified.

### 5.2.4 Violation Handling

N/A - This is a system action, not a user violation.

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-042', 'dependency_reason': 'This story requires the existence of the card management model and its basic views, which are created in US-042.'}

## 6.2.0 Technical Dependencies

- The custom Odoo model for 'Card Management'.
- Odoo's notification/alerting framework (or the custom implementation from US-081).

## 6.3.0 Data Dependencies

- Requires at least one existing card record (FASTag or diesel) to be present in the system for testing.

## 6.4.0 External Dependencies

- This story's full value depends on the completion of US-081 (System generates an alert for low card balance) to handle the triggered alert.

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- Saving the card record form should complete in under 200ms, as per REQ-NFR-001.

## 7.2.0 Security

- Only users with 'Finance Officer' or 'Admin' roles must have write access to the 'Current Balance' and 'Low-Balance Threshold' fields. Other roles (e.g., Dispatch Manager) may have read-only access if required.
- Access control must be enforced at the model and field level using Odoo's security mechanisms (`ir.model.access.csv`, `ir.rule`, and field-level groups).

## 7.3.0 Usability

- Validation error messages must be clear, concise, and guide the user to correct the input.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards.

## 7.5.0 Compatibility

- The feature must function correctly on all browsers supported by Odoo 18.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Adding two fields to an existing Odoo model.
- Adding fields to the corresponding XML view.
- Implementing standard Python constraints (`@api.constrains`) for validation.
- Writing a small piece of logic in the `write()` method to check the balance against the threshold and trigger the alert mechanism.

## 8.3.0 Technical Risks

- Minor risk of incorrect implementation of the alert trigger logic, leading to alerts not firing or firing at the wrong time. This can be mitigated with thorough integration testing.

## 8.4.0 Integration Points

- The primary integration point is with the system's alerting/notification service, which will be invoked when the balance drops below the threshold.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Verify successful update of balance and threshold.
- Verify validation logic for non-numeric and negative inputs.
- Verify that an alert is correctly triggered when balance is updated to be less than the threshold.
- Verify that no alert is triggered when balance is updated to be equal to or greater than the threshold.

## 9.3.0 Test Data Needs

- A test user with the 'Finance Officer' role.
- A test user with a non-finance role to verify access restrictions.
- At least two card records: one with a threshold of 0, and one with a positive threshold (e.g., 1000).

## 9.4.0 Testing Tools

- Pytest for unit and integration tests.
- Manual testing via the Odoo web interface.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing.
- Code reviewed and approved by at least one other developer.
- Unit tests covering validation logic and the alert trigger condition are implemented and achieve >80% coverage for the modified code.
- Integration testing with the alert mechanism (US-081) is completed successfully.
- User interface changes are reviewed and approved by the Product Owner or a UX specialist.
- Security rules restricting access to Finance Officers/Admins are implemented and verified.
- No performance regressions are introduced.
- Relevant documentation (if any) is updated.
- Story is deployed and verified in the staging environment without issues.

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This story should be scheduled in a sprint after US-042 is completed.
- Can be worked on in parallel with US-081, but final integration testing must wait for US-081 to be available in the testing environment.

## 11.4.0 Release Impact

This is a core feature for the financial management module and is essential for the initial release to provide proactive operational support.


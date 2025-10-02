# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-042 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Finance Officer creates and manages records for FA... |
| As A User Story | As a Finance Officer, I want to create, view, and ... |
| User Persona | Finance Officer. This user is responsible for fina... |
| Business Value | Centralizes management of critical financial instr... |
| Functional Area | Financial Management |
| Story Theme | Expense and Asset Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Create a new FASTag card record

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am a logged-in user with the 'Finance Officer' role and I am on the 'Card Management' screen

### 3.1.5 When

I click the 'Create' button and fill in the form with valid details for a new FASTag card, including Card Number, Card Type ('FASTag'), Provider, Status ('Active'), and optionally assign it to a vehicle

### 3.1.6 Then

The system saves the new card record, and it appears in the list of cards.

### 3.1.7 Validation Notes

Verify the record is created in the database with the correct values. Check the list view to ensure the new record is displayed.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Create a new Diesel card record

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am a logged-in user with the 'Finance Officer' role and I am on the 'Card Management' screen

### 3.2.5 When

I click the 'Create' button and fill in the form with valid details for a new Diesel card, including Card Number, Card Type ('Diesel'), Provider, and Status ('Active')

### 3.2.6 Then

The system saves the new card record, and it appears in the list of cards.

### 3.2.7 Validation Notes

Verify the record is created in the database with the correct values. Check the list view to ensure the new record is displayed.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

View the list of all managed cards

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

Multiple card records exist in the system

### 3.3.5 When

I navigate to the 'Card Management' screen

### 3.3.6 Then

I see a list view displaying all card records with columns for Card Number (partially masked), Card Type, Provider, Assigned Vehicle, and Status.

### 3.3.7 Validation Notes

Confirm the list view loads without errors and displays the correct data. Ensure the card number is masked (e.g., showing only the last 4 digits).

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Edit an existing card record

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

I am viewing the details of an existing card record

### 3.4.5 When

I click 'Edit' and change the 'Provider' and 'Assigned Vehicle' fields

### 3.4.6 Then

The system saves the changes, and the updated information is reflected in both the form and list views.

### 3.4.7 Validation Notes

Modify a record, save it, and then reload the page to confirm the changes have persisted.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Deactivate a card record

### 3.5.3 Scenario Type

Happy_Path

### 3.5.4 Given

An 'Active' card record exists

### 3.5.5 When

I edit the card record and change its 'Status' to 'Inactive'

### 3.5.6 Then

The system saves the change, and the card is now marked as 'Inactive'. By default, it should be hidden from the main list view which filters for 'Active' cards.

### 3.5.7 Validation Notes

Change status to 'Inactive'. Verify the default list view no longer shows the card. Remove the 'Active' filter to confirm the inactive card can still be found.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Attempt to create a card with a duplicate number

### 3.6.3 Scenario Type

Error_Condition

### 3.6.4 Given

A card with the number '1234567890' already exists

### 3.6.5 When

I attempt to create a new card and enter '1234567890' in the 'Card Number' field

### 3.6.6 Then

The system prevents saving the record and displays a clear validation error message, such as 'A card with this number already exists.'

### 3.6.7 Validation Notes

This requires a database unique constraint on the card number field. Test by creating a card, then attempting to create a second card with the identical number.

## 3.7.0 Criteria Id

### 3.7.1 Criteria Id

AC-007

### 3.7.2 Scenario

Attempt to save a card with missing required fields

### 3.7.3 Scenario Type

Error_Condition

### 3.7.4 Given

I am on the new card creation form

### 3.7.5 When

I attempt to save the form without providing a 'Card Number' or 'Card Type'

### 3.7.6 Then

The system prevents saving and highlights the mandatory fields that need to be filled.

### 3.7.7 Validation Notes

Try to save a new record with required fields left blank and verify the Odoo UI validation triggers correctly.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A new menu item under a 'Finance' or 'Configuration' menu, labeled 'Card Management' or similar.
- An Odoo list/tree view to display all card records.
- An Odoo form view for creating and editing card records.
- Fields: Card Number (Text), Card Type (Selection: 'FASTag', 'Diesel'), Provider (Text), Assigned Vehicle (Many2One to Vehicle Master), Status (Selection: 'Active', 'Inactive').
- Search and filter capabilities on the list view (e.g., filter by Status, search by Provider).

## 4.2.0 User Interactions

- User clicks 'Create' to open a blank form.
- User selects a card type from a dropdown list.
- User selects an optional vehicle from a searchable dropdown list.
- The system defaults the 'Status' of a new card to 'Active'.

## 4.3.0 Display Requirements

- The list view must show key information at a glance.
- The full card number should be masked in list views for security, showing only the last 4 digits (e.g., '...-1234'). The full number should be visible in the form view to authorized users.

## 4.4.0 Accessibility Needs

- The form must be navigable using a keyboard.
- All form fields must have proper labels for screen readers, adhering to WCAG 2.1 Level AA standards.

# 5.0.0 Business Rules

- {'rule_id': 'BR-CARD-001', 'rule_description': "The 'Card Number' must be unique across all card records in the system.", 'enforcement_point': 'Database level (unique constraint) and on record save/validation.', 'violation_handling': 'Prevent the record from being saved and display a user-friendly error message.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-006', 'dependency_reason': "The Vehicle Master model must exist to implement the 'Assigned Vehicle' (Many2One) field on the card form."}

## 6.2.0 Technical Dependencies

- Requires creation of a new Odoo model (e.g., `tms.card`).
- Requires creation of Odoo views (form, tree, search) and menu actions.
- Requires configuration of Odoo Access Control Lists (ACLs) to restrict access to Finance Officer and Admin roles.

## 6.3.0 Data Dependencies

- Relies on the existence of vehicle records in the Vehicle Master data for the assignment feature.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The card list view should load in under 2 seconds with up to 1,000 card records.

## 7.2.0 Security

- Access to create, read, update, and delete card records must be restricted to 'Finance Officer' and 'Admin' roles via Odoo's security rules.
- Card numbers should be masked in list views to prevent casual exposure of sensitive information.

## 7.3.0 Usability

- The interface for managing cards should be consistent with standard Odoo patterns to ensure a low learning curve for users.

## 7.4.0 Accessibility

- Must comply with WCAG 2.1 Level AA standards.

## 7.5.0 Compatibility

- The feature must be fully functional on all browsers supported by Odoo 18.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Standard Odoo model and view creation.
- Implementation of a unique constraint.
- Configuration of security rules.

## 8.3.0 Technical Risks

- Minimal risk. A potential issue could be incorrect implementation of the unique constraint, leading to data integrity problems. This can be mitigated with unit testing.

## 8.4.0 Integration Points

- This model will be a foreign key source for future expense tracking records.
- This model will be the data source for the low-balance alert feature (US-081).

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Verify CRUD operations (Create, Read, Update, Deactivate) for both FASTag and Diesel cards.
- Test the unique card number constraint by attempting to create a duplicate.
- Test role-based access: confirm a 'Dispatch Manager' or 'Driver' cannot see or access the 'Card Management' menu.
- Verify the 'Assigned Vehicle' link correctly pulls data from the Vehicle Master.
- Test the search and filter functionality on the list view.

## 9.3.0 Test Data Needs

- At least 2-3 existing vehicle records.
- A mix of FASTag and Diesel card data.
- User accounts with 'Finance Officer', 'Admin', and 'Driver' roles for access testing.

## 9.4.0 Testing Tools

- Pytest for Odoo unit tests.
- Manual testing checklist based on acceptance criteria.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for the unique constraint and passing with >80% coverage for the new model
- Integration testing of the vehicle link completed successfully
- User interface reviewed and approved for usability and consistency
- Security requirements (role access, data masking) validated
- Documentation for the new model and its fields is added to the technical specification
- Story deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

2

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational story for several other financial features (US-043, US-081). It should be scheduled in an early sprint dedicated to master data setup.
- Requires the Vehicle Master (US-006) to be completed in the same or a prior sprint.

## 11.4.0 Release Impact

- This feature is part of the core financial setup and is essential for the initial release (Phase 2 as per REQ-TRN-001).


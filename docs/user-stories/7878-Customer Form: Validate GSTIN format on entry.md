# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-073 |
| Elaboration Date | 2025-01-15 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Customer Form: Validate GSTIN format on entry |
| As A User Story | As a Finance Officer, I want the system to validat... |
| User Persona | Finance Officer, Admin |
| Business Value | Ensures data integrity of customer records, preven... |
| Functional Area | Master Data Management |
| Story Theme | Customer Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

User enters a correctly formatted GSTIN

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A user is on the 'Create/Edit Customer' form

### 3.1.5 When

The user enters a valid 15-character alphanumeric GSTIN (e.g., '27AAFCE1234A1Z5') into the GSTIN field and attempts to save the record

### 3.1.6 Then

The system accepts the input, saves the customer record successfully, and no validation error is displayed.

### 3.1.7 Validation Notes

Test with a known valid GSTIN format. The save operation should complete without any warnings related to the GSTIN field.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

User enters a GSTIN with incorrect length

### 3.2.3 Scenario Type

Error_Condition

### 3.2.4 Given

A user is on the 'Create/Edit Customer' form

### 3.2.5 When

The user enters a GSTIN with fewer than 15 characters (e.g., '27AAFCE1234A1Z') and attempts to save

### 3.2.6 Then

The system must prevent the record from being saved, display a clear error message like 'Invalid GSTIN format. It must be 15 characters long.', and visually highlight the GSTIN field.

### 3.2.7 Validation Notes

Test with strings of length 14 and 16. The save action must fail, and the user must be clearly notified of the error.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

User enters a GSTIN with an incorrect pattern

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

A user is on the 'Create/Edit Customer' form

### 3.3.5 When

The user enters a 15-character string that does not match the standard GSTIN pattern (e.g., 'ABAAFCE1234A1Z5', where the first two characters are not digits) and attempts to save

### 3.3.6 Then

The system must prevent the record from being saved, display a clear error message like 'Invalid GSTIN format. Please check the structure.', and visually highlight the GSTIN field.

### 3.3.7 Validation Notes

Test with various invalid patterns: non-digit state code, special characters, incorrect 14th character, etc. The save must be blocked.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

User leaves the GSTIN field empty

### 3.4.3 Scenario Type

Edge_Case

### 3.4.4 Given

A user is on the 'Create/Edit Customer' form and has filled in all other mandatory fields

### 3.4.5 When

The user leaves the GSTIN field empty and attempts to save the record

### 3.4.6 Then

The system saves the customer record successfully without any validation error for the GSTIN field.

### 3.4.7 Validation Notes

Verify that GSTIN is not a mandatory field and an empty value is permissible.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

User enters a valid GSTIN in lowercase

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

A user is on the 'Create/Edit Customer' form

### 3.5.5 When

The user enters a valid GSTIN in lowercase (e.g., '27aafce1234a1z5') and saves the record

### 3.5.6 Then

The system automatically converts the input to uppercase ('27AAFCE1234A1Z5') and saves the record successfully.

### 3.5.7 Validation Notes

After saving, reopen the customer record and verify that the GSTIN is stored in uppercase.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Real-time validation feedback in the UI

### 3.6.3 Scenario Type

Happy_Path

### 3.6.4 Given

A user is on the 'Create/Edit Customer' form and has entered an invalid GSTIN

### 3.6.5 When

The user clicks or tabs out of the GSTIN field (on blur event)

### 3.6.6 Then

The validation error message and visual highlighting appear immediately, without waiting for the user to click 'Save'.

### 3.6.7 Validation Notes

This provides a better user experience. The error should disappear if the user corrects the input.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- GSTIN text input field on the Customer form (extending `res.partner`).
- Error message display area adjacent to the GSTIN field.

## 4.2.0 User Interactions

- On attempting to save with an invalid GSTIN, the save action is blocked.
- On field blur (losing focus), validation is triggered, and immediate feedback is provided.
- The input should be automatically converted to uppercase.

## 4.3.0 Display Requirements

- Error messages must be user-friendly and specific (e.g., mention length or format issues).
- The input field should be visually highlighted (e.g., with a red border) when its content is invalid.

## 4.4.0 Accessibility Needs

- Error messages must be programmatically linked to the input field for screen readers (using `aria-describedby`).
- Color-based highlighting must be supplemented with text or icons to meet accessibility standards.

# 5.0.0 Business Rules

- {'rule_id': 'REQ-DAT-003', 'rule_description': 'The system shall validate the format of the GSTIN field upon entry.', 'enforcement_point': 'On the Customer (res.partner) model, both on the frontend (UI) and backend (server-side constraints).', 'violation_handling': 'Prevent the record from being saved and display a descriptive error message to the user.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-015', 'dependency_reason': 'This story implements the validation on the customer creation form, which is established in US-015.'}

## 6.2.0 Technical Dependencies

- Odoo 18 `res.partner` model and its corresponding form view.
- Odoo's backend validation mechanism (`@api.constrains`).
- Odoo Web Library (OWL) for frontend validation logic.

## 6.3.0 Data Dependencies

*No items available*

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- The validation logic (regex) must execute in under 50ms to avoid any noticeable UI lag during typing or on blur.

## 7.2.0 Security

- While this is a format validation, all user input should be treated as untrusted and properly handled by the Odoo framework to prevent injection attacks.

## 7.3.0 Usability

- Feedback on validation failure must be immediate and clear to allow users to correct mistakes efficiently.
- Auto-converting to uppercase improves user experience by reducing input errors.

## 7.4.0 Accessibility

- The feature must comply with WCAG 2.1 Level AA standards as per REQ-INT-001.

## 7.5.0 Compatibility

- Validation must work consistently across all supported modern web browsers.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Requires a well-defined regular expression for the GSTIN format.
- Involves both backend (Python) and frontend (JavaScript/OWL) implementation for robust validation and good UX.

## 8.3.0 Technical Risks

- The regex for GSTIN validation must be accurate and cover all rules of the format. An incorrect regex could block valid numbers or allow invalid ones.

## 8.4.0 Integration Points

- This validation is a critical prerequisite for the GSP e-invoicing integration (REQ-INT-003), as an invalid GSTIN will cause API calls to fail.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- E2E

## 9.2.0 Test Scenarios

- Create a customer with a valid GSTIN.
- Attempt to create a customer with an invalid GSTIN (wrong length, wrong pattern).
- Edit an existing customer to add a valid/invalid GSTIN.
- Create a customer with a blank GSTIN.
- Enter a valid GSTIN in lowercase and verify it's saved as uppercase.

## 9.3.0 Test Data Needs

- A list of known valid GSTINs.
- A list of invalid strings: too short, too long, incorrect characters, incorrect pattern.

## 9.4.0 Testing Tools

- Pytest for backend unit tests.
- Manual testing in a browser for UI/UX validation.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Backend validation logic is implemented with `@api.constrains` on the Odoo model.
- Frontend validation logic is implemented in the OWL component for immediate feedback.
- Code reviewed and approved by team
- Unit tests for the validation logic are implemented with at least 90% coverage and are passing
- Integration testing completed successfully
- User interface reviewed and approved for clarity of error messages and visual cues
- Performance requirements verified
- Security requirements validated
- Documentation updated appropriately
- Story deployed and verified in staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

1

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This is a foundational data integrity feature and a blocker for the e-invoicing epic. It should be prioritized in an early sprint along with the Customer Master story (US-015).

## 11.4.0 Release Impact

- Critical for the initial release, especially for the finance module. A release without this feature would be considered incomplete and risky for financial operations.


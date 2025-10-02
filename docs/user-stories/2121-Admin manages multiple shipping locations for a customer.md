# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-016 |
| Elaboration Date | 2025-01-17 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin manages multiple shipping locations for a cu... |
| As A User Story | As an Admin, I want to add, view, and manage multi... |
| User Persona | Admin. This user is responsible for maintaining ac... |
| Business Value | Improves operational efficiency by speeding up the... |
| Functional Area | Master Data Management |
| Story Theme | Customer Management |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Admin successfully adds a new shipping location to a customer

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

I am logged in as an Admin and am viewing the form for an existing customer.

### 3.1.5 When

I navigate to the 'Shipping Locations' tab, click 'Add a line', fill in all mandatory address fields (e.g., Address, City, State, Pincode), and click 'Save'.

### 3.1.6 Then

The new shipping location is saved and displayed in the list of shipping locations for that customer, and the customer record is saved successfully.

### 3.1.7 Validation Notes

Verify the new location appears in the customer's record. Also, verify this new location is available in the 'Destination' dropdown when creating a trip for this customer (dependency on US-026).

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Admin edits an existing shipping location

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

I am an Admin viewing a customer record that has at least one existing shipping location.

### 3.2.5 When

I select a shipping location from the list, modify its details (e.g., change the Pincode), and save the customer record.

### 3.2.6 Then

The changes to the shipping location are saved and reflected in the list.

### 3.2.7 Validation Notes

Check the list view on the customer form to see the updated Pincode. Verify that any future trips created using this location reflect the new information.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Attempting to save a shipping location with missing mandatory fields

### 3.3.3 Scenario Type

Error_Condition

### 3.3.4 Given

I am an Admin adding a new shipping location for a customer.

### 3.3.5 When

I enter some details but leave a mandatory field, such as 'City', blank and attempt to save.

### 3.3.6 Then

The system shall display a validation error message indicating which fields are required, and the record shall not be saved.

### 3.3.7 Validation Notes

Test by leaving each mandatory field blank one by one and attempting to save. The system should prevent saving in all cases and provide a user-friendly error message.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Shipping locations are available for selection during trip creation

### 3.4.3 Scenario Type

Happy_Path

### 3.4.4 Given

A customer has multiple active shipping locations defined, and a Dispatch Manager is creating a new trip for that customer.

### 3.4.5 When

The Dispatch Manager selects the customer in the trip creation form.

### 3.4.6 Then

The 'Destination' field dropdown should be populated with a list of the customer's active shipping locations, in addition to their primary billing address.

### 3.4.7 Validation Notes

This is an integration test with the Trip Management feature (US-026). The list should be filterable and searchable if it contains many entries.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Admin deactivates a shipping location

### 3.5.3 Scenario Type

Alternative_Flow

### 3.5.4 Given

I am an Admin viewing a customer record with an existing shipping location that is no longer in use.

### 3.5.5 When

I edit the shipping location and mark it as 'Inactive' (or use a similar mechanism like archiving).

### 3.5.6 Then

The location is no longer available for selection in the 'Destination' field for new trips, but it is retained in the system for historical reporting on past trips.

### 3.5.7 Validation Notes

Verify the location disappears from the trip creation dropdown. Verify that historical trip records that used this location still display the address correctly.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- A dedicated tab or section labeled 'Shipping Locations' on the Odoo `res.partner` form view.
- An editable list view (One2Many) within this tab to display and manage locations.
- Standard Odoo controls ('Add a line', 'Delete', form view pop-up) for managing list entries.
- Input fields for a complete address: Location Name/Alias, Street, Street2, City, State, Zip/Pincode, Country, Contact Person, Contact Phone.

## 4.2.0 User Interactions

- Admin can click to add a new row to the list of locations.
- Clicking on an existing location opens a form or modal for editing.
- The list of locations should be clearly separated from the customer's primary billing address.

## 4.3.0 Display Requirements

- The list of shipping locations should display key summary information like Location Name, City, and State for easy identification.

## 4.4.0 Accessibility Needs

- All form fields and controls must have proper labels for screen readers, adhering to WCAG 2.1 Level AA standards as per REQ-INT-001.

# 5.0.0 Business Rules

- {'rule_id': 'BR-CUST-01', 'rule_description': 'A shipping location must have a complete address, including at least Street, City, and Pincode, to be considered valid.', 'enforcement_point': 'On save of the customer record or the shipping location sub-record.', 'violation_handling': 'Prevent saving the record and display a user-friendly validation error highlighting the missing fields.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

- {'story_id': 'US-015', 'dependency_reason': 'This story extends the customer record created in US-015. The core customer model must exist before multiple addresses can be associated with it.'}

## 6.2.0 Technical Dependencies

- This feature will be implemented by extending Odoo's standard `res.partner` model. It should leverage Odoo's native support for parent/child contacts, using the `type='delivery'` convention to identify shipping addresses.

## 6.3.0 Data Dependencies

- Requires existing customer records in the database for testing the addition of shipping locations.

## 6.4.0 External Dependencies

*No items available*

# 7.0.0 Non Functional Requirements

## 7.1.0 Performance

- Loading a customer form with up to 50 shipping locations should not degrade the page load time significantly (LCP under 3 seconds as per REQ-NFR-001).

## 7.2.0 Security

- Only users with appropriate permissions (e.g., Admin) should be able to add, edit, or delete customer shipping locations, enforced by Odoo's access control lists (ACLs).

## 7.3.0 Usability

- The process of adding a new shipping location should be intuitive and require minimal clicks.
- Error messages for invalid data should be clear and specific.

## 7.4.0 Accessibility

- Compliant with WCAG 2.1 Level AA standards.

## 7.5.0 Compatibility

- The interface must be fully functional and responsive on all supported browsers and screen sizes (from 360px width upwards) as per REQ-INT-001.

# 8.0.0 Implementation Considerations

## 8.1.0 Complexity Assessment

Low

## 8.2.0 Complexity Factors

- Leverages standard Odoo functionality (`res.partner` child contacts).
- Complexity is primarily in UI/View customization (XML) to present the information clearly within the TMS context.
- Requires ensuring the domain/filter on the trip creation form's 'Destination' field is correctly configured.

## 8.3.0 Technical Risks

- Potential for conflict if other custom modules also modify the `res.partner` view. A clean implementation using Odoo's inheritance (`xpath`) is required.

## 8.4.0 Integration Points

- The primary integration point is the Trip Creation form (US-026), where the list of shipping locations will be consumed.

# 9.0.0 Testing Requirements

## 9.1.0 Testing Types

- Unit
- Integration
- E2E

## 9.2.0 Test Scenarios

- Create a new customer and add three shipping locations.
- Edit one of the shipping locations.
- Attempt to save a location with an empty 'City' field.
- Deactivate a shipping location.
- Create a new trip and verify that only the two active shipping locations plus the primary address appear in the destination dropdown.
- Select a shipping location and confirm the trip's destination is populated correctly.

## 9.3.0 Test Data Needs

- A set of test customers.
- Sample valid and invalid address data for testing validation rules.

## 9.4.0 Testing Tools

- Odoo's built-in testing framework.
- Pytest for backend unit tests.

# 10.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Code reviewed and approved by team
- Unit tests implemented for any new model logic and passing with >80% coverage
- Integration testing with the Trip Creation form completed successfully
- User interface on the customer form is reviewed and approved by the product owner
- Functionality is deployed and verified in the staging environment

# 11.0.0 Planning Information

## 11.1.0 Story Points

3

## 11.2.0 Priority

🔴 High

## 11.3.0 Sprint Considerations

- This story is a foundational element for efficient trip creation. It should be prioritized to be completed before or in the same sprint as the trip creation story (US-026).

## 11.4.0 Release Impact

- This is a core feature for the initial release (Phase 1) as it directly impacts the primary operational workflow.


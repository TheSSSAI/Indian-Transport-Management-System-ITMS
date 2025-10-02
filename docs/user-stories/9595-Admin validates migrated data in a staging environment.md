# 1 Story Metadata

| Property | Value |
|----------|-------|
| Story Id | US-090 |
| Elaboration Date | 2025-01-26 |
| Development Readiness | Complete |

# 2 Story Narrative

| Property | Value |
|----------|-------|
| Title | Admin validates migrated data in a staging environ... |
| As A User Story | As an Admin responsible for the system's go-live, ... |
| User Persona | Admin: A technical user responsible for system dep... |
| Business Value | Mitigates the significant business risk of data lo... |
| Functional Area | System Administration & Data Migration |
| Story Theme | Transition & Go-Live Readiness |

# 3 Acceptance Criteria

## 3.1 Criteria Id

### 3.1.1 Criteria Id

AC-001

### 3.1.2 Scenario

Successful execution of migration and validation scripts

### 3.1.3 Scenario Type

Happy_Path

### 3.1.4 Given

A clean staging TMS database is available, and a complete data dump from the legacy system has been provided

### 3.1.5 When

The Admin executes the documented command to run the data migration dry-run, followed by the command to run the validation process

### 3.1.6 Then

The scripts complete without unhandled errors, and a structured validation report (e.g., CSV or text file) is generated in a predefined location.

### 3.1.7 Validation Notes

Verify that the scripts are executable and produce an output file. The content of the file is checked in subsequent criteria.

## 3.2.0 Criteria Id

### 3.2.1 Criteria Id

AC-002

### 3.2.2 Scenario

Validation report shows matching record counts for master data

### 3.2.3 Scenario Type

Happy_Path

### 3.2.4 Given

The migration and validation process has been successfully executed

### 3.2.5 When

The Admin reviews the generated validation report

### 3.2.6 Then

The report must contain a section for 'Record Count Comparison' which shows identical counts for 'active Customers', 'all Vehicles', and 'active Drivers' between the source data dump and the target staging database.

### 3.2.7 Validation Notes

Manually query the source data dump and the staging database to confirm the counts reported are accurate.

## 3.3.0 Criteria Id

### 3.3.1 Criteria Id

AC-003

### 3.3.2 Scenario

Validation report shows successful financial reconciliation

### 3.3.3 Scenario Type

Happy_Path

### 3.3.4 Given

The migration and validation process has been successfully executed

### 3.3.5 When

The Admin reviews the generated validation report

### 3.3.6 Then

The report must contain a 'Financial Reconciliation' section that shows the sum of all open (unpaid) invoice balances from the source data matches the sum of all outstanding balances in the staging TMS customer ledgers.

### 3.3.7 Validation Notes

Requires a script to sum the relevant financial fields from the source and target systems. The report must show both totals and confirm they match.

## 3.4.0 Criteria Id

### 3.4.1 Criteria Id

AC-004

### 3.4.2 Scenario

Validation report identifies data transformation or mapping errors

### 3.4.3 Scenario Type

Error_Condition

### 3.4.4 Given

A legacy data dump contains records that violate the new system's validation rules (e.g., an invalid GSTIN format)

### 3.4.5 When

The migration and validation process is executed

### 3.4.6 Then

The validation report must list the specific records that failed to migrate or were migrated with data integrity issues, along with a reason for the failure (e.g., 'Invalid GSTIN format for Customer ID 123').

### 3.4.7 Validation Notes

Prepare a test data dump with known bad data and verify the report correctly identifies these records.

## 3.5.0 Criteria Id

### 3.5.1 Criteria Id

AC-005

### 3.5.2 Scenario

Validation report flags count mismatches

### 3.5.3 Scenario Type

Error_Condition

### 3.5.4 Given

The migration script fails to migrate a subset of records for a specific data model

### 3.5.5 When

The validation process is executed

### 3.5.6 Then

The 'Record Count Comparison' section of the report must clearly flag the mismatch, showing the source count and the lower target count for the affected model.

### 3.5.7 Validation Notes

Simulate a partial migration and verify the report accurately reflects the discrepancy.

## 3.6.0 Criteria Id

### 3.6.1 Criteria Id

AC-006

### 3.6.2 Scenario

Staging environment can be reset for repeated dry-runs

### 3.6.3 Scenario Type

Alternative_Flow

### 3.6.4 Given

A migration dry-run has been completed, and the staging database contains migrated data

### 3.6.5 When

The Admin executes the documented procedure to reset the staging environment

### 3.6.6 Then

The TMS-related tables in the staging database are wiped clean, ready for another migration attempt.

### 3.6.7 Validation Notes

After running the reset procedure, connect to the database and verify that tables like `res_partner` (for customers), `tms_vehicle`, etc., are empty.

# 4.0.0 User Interface Requirements

## 4.1.0 Ui Elements

- Command-Line Interface (CLI) for executing migration and validation scripts.
- A structured, human-readable output file for the validation report (e.g., CSV, formatted text, or simple HTML).

## 4.2.0 User Interactions

- Admin executes a script from the command line, potentially passing parameters like the path to the legacy data dump.
- Admin receives feedback on the command line regarding the script's progress and completion status.
- Admin opens the generated report file in a standard viewer (text editor, spreadsheet program) to analyze the results.

## 4.3.0 Display Requirements

- The validation report must be clearly sectioned (e.g., 'Summary', 'Record Count Comparison', 'Financial Reconciliation', 'Data Integrity Errors').
- All discrepancies in the report must be highlighted and easy to identify.

## 4.4.0 Accessibility Needs

- Not applicable for a CLI/report-based tool, but the report format should be simple text or CSV to be universally accessible.

# 5.0.0 Business Rules

- {'rule_id': 'REQ-TRN-002', 'rule_description': 'A mandatory dry-run of the migration must be performed in the staging environment, and the results must be validated and signed off by the Admin before the production cutover can be scheduled.', 'enforcement_point': 'Project Management / Go-Live Checklist', 'violation_handling': 'The production cutover is postponed until a successful and validated dry-run is completed.'}

# 6.0.0 Dependencies

## 6.1.0 Prerequisite Stories

### 6.1.1 Story Id

#### 6.1.1.1 Story Id

US-089

#### 6.1.1.2 Dependency Reason

This story (US-090) is about validating the migration. It requires the actual migration scripts and tools, developed in US-089, to exist first.

### 6.1.2.0 Story Id

#### 6.1.2.1 Story Id

US-006

#### 6.1.2.2 Dependency Reason

The target Vehicle data model must be finalized to validate vehicle data migration.

### 6.1.3.0 Story Id

#### 6.1.3.1 Story Id

US-011

#### 6.1.3.2 Dependency Reason

The target Driver data model must be finalized to validate driver data migration.

### 6.1.4.0 Story Id

#### 6.1.4.1 Story Id

US-015

#### 6.1.4.2 Dependency Reason

The target Customer data model must be finalized to validate customer data migration.

### 6.1.5.0 Story Id

#### 6.1.5.1 Story Id

US-039

#### 6.1.5.2 Dependency Reason

The target Invoice and Payment models must be finalized to perform financial reconciliation.

## 6.2.0.0 Technical Dependencies

- A fully provisioned staging environment that is a replica of the production setup (as per REQ-DEP-001).
- A documented and repeatable process for deploying the TMS application to the staging environment.
- Secure access to the staging database for the validation scripts.

## 6.3.0.0 Data Dependencies

- A representative, full-scale data dump from the legacy system.
- Clear documentation of the legacy system's data schema.

## 6.4.0.0 External Dependencies

- Availability of the Admin user to perform the validation and provide sign-off.

# 7.0.0.0 Non Functional Requirements

## 7.1.0.0 Performance

- The entire dry-run process (migration + validation) on the full dataset should complete within 4 hours to be feasible within a standard off-hours window.

## 7.2.0.0 Security

- Database credentials and other secrets must not be hardcoded in the scripts. They should be retrieved from a secure source like AWS Secrets Manager or environment variables at runtime.
- The legacy data dump must be stored and handled securely, especially if it contains PII.

## 7.3.0.0 Usability

- The validation report must be clear, concise, and actionable. An Admin should be able to quickly understand the migration's success or failure and pinpoint specific areas of concern.

## 7.4.0.0 Accessibility

- N/A

## 7.5.0.0 Compatibility

- The scripts must be compatible with the specified technology stack (Python 3.11, PostgreSQL 16).

# 8.0.0.0 Implementation Considerations

## 8.1.0.0 Complexity Assessment

High

## 8.2.0.0 Complexity Factors

- Requires deep understanding of both legacy and new data models.
- Logic for data transformation and validation can be complex, especially for financial data.
- Building robust error handling and reporting into the scripts.
- Potential for large data volumes impacting script performance.

## 8.3.0.0 Technical Risks

- Undocumented nuances in the legacy data may lead to incorrect transformations.
- Performance bottlenecks when processing large tables.
- Inconsistencies between the staging and production environments could lead to a false sense of security.

## 8.4.0.0 Integration Points

- The scripts will read from the legacy system data dump.
- The scripts will write to and read from the new TMS PostgreSQL database in the staging environment.

# 9.0.0.0 Testing Requirements

## 9.1.0.0 Testing Types

- Unit
- Integration

## 9.2.0.0 Test Scenarios

- Test the validation scripts against a small, controlled dataset with known good data to verify correct 'happy path' reporting.
- Test the validation scripts against a dataset with known errors (e.g., mismatched counts, bad data formats, financial discrepancies) to verify correct error detection and reporting.
- Test the performance of the scripts against a full-scale data dump.
- The Admin will perform User Acceptance Testing (UAT) by executing the entire process and confirming the report is accurate and useful.

## 9.3.0.0 Test Data Needs

- A full-scale (or near full-scale) data dump from the legacy system.
- Several small, purpose-built test data dumps designed to trigger specific validation failures.

## 9.4.0.0 Testing Tools

- Pytest for unit testing the Python script logic.
- A database client (e.g., DBeaver, psql) for manual verification of data in the staging database.

# 10.0.0.0 Definition Of Done

- All acceptance criteria validated and passing
- Migration validation scripts are written, code-reviewed, and merged into the main branch.
- Unit tests for the validation logic are implemented and passing with sufficient coverage.
- The process for executing the dry-run and generating the report is clearly documented.
- A successful dry-run has been demonstrated to the project stakeholders using the full legacy dataset.
- The Admin user has formally signed off on the process and its results.
- The staging environment reset procedure is documented and has been successfully tested.
- Story deployed and verified in staging environment

# 11.0.0.0 Planning Information

## 11.1.0.0 Story Points

13

## 11.2.0.0 Priority

🔴 High

## 11.3.0.0 Sprint Considerations

- This is a critical-path story for the go-live and must be completed before the final cutover weekend.
- Allocate sufficient time for multiple test runs, as issues are likely to be found in the first few attempts.
- Requires close collaboration between developers and the system Admin.

## 11.4.0.0 Release Impact

- Successful completion is a key gate for the go/no-go decision for the production launch. Failure to complete this story will delay the entire project release.


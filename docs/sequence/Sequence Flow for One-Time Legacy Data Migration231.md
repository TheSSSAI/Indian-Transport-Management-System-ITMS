# 1 Overview

## 1.1 Diagram Id

SEQ-DF-008

## 1.2 Name

One-Time Legacy Data Migration

## 1.3 Description

Describes the critical one-time process to extract data from the legacy system, transform it through cleansing and validation scripts, and load it into the new TMS Odoo database. This sequence is executed during the pre-go-live cutover window.

## 1.4 Type

🔹 DataFlow

## 1.5 Purpose

To ensure business continuity by migrating all essential active data (customers, vehicles, drivers, open invoices) to the new system, enabling a seamless transition for users.

## 1.6 Complexity

High

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- Data is extracted from the legacy system into a set of predefined CSV files.
- Custom Python scripts are executed to cleanse (e.g., trim whitespace), validate (e.g., check formats), and transform the data to match Odoo's schema.
- A mandatory dry-run is performed in the staging environment using Odoo's Data Import module to identify potential issues.
- Post-dry-run validation checks, including record counts and financial reconciliation of open balances, are performed.
- After successful validation and sign-off, the final migration is executed against the production database during the planned cutover weekend.

## 1.11 Triggers

- The initiation of the planned production cutover for the new TMS system.

## 1.12 Outcomes

- The new TMS system is populated with the clean and necessary data required to begin live operations.
- The legacy system is successfully transitioned to a read-only state post-migration.

## 1.13 Business Rules

- REQ-TRN-002: The migration scope is strictly defined to include active Customers, all Vehicles, active Drivers, and open financial transactions.
- A mandatory dry-run of the migration must be performed and validated in the staging environment.

## 1.14 Error Scenarios

- Data validation fails during the dry-run, necessitating a cycle of data correction in the source extract and re-running the dry-run.
- The production migration fails or exceeds the cutover window, triggering the formal rollback plan.

## 1.15 Integration Points

- Source: Legacy System Database (indirectly via CSV extracts)

# 2.0 Details

## 2.1 Diagram Id

SEQ-DF-008

## 2.2 Name

Implementation: One-Time Legacy Data Migration ETL Process

## 2.3 Description

Provides a detailed technical specification for the one-time ETL (Extract, Transform, Load) process for migrating active business data from a legacy system into the new TMS Odoo database. The sequence covers the mandatory dry-run phase in a staging environment and the final execution in production during a planned cutover window, as defined in REQ-TRN-002.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

MIGRATION-OPERATOR

#### 2.4.1.2 Display Name

Migration Operator

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Human / CI/CD Pipeline

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | <<Actor>> |

### 2.4.2.0 External Database

#### 2.4.2.1 Repository Id

LEGACY-SYSTEM-DB

#### 2.4.2.2 Display Name

Legacy System DB

#### 2.4.2.3 Type

🔹 External Database

#### 2.4.2.4 Technology

CSV Data Extracts

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #FFC0CB |
| Stereotype | <<ExternalSystem>> |

### 2.4.3.0 ETL Component

#### 2.4.3.1 Repository Id

PYTHON-MIGRATION-SCRIPTS

#### 2.4.3.2 Display Name

Python Migration Scripts

#### 2.4.3.3 Type

🔹 ETL Component

#### 2.4.3.4 Technology

Python 3.11, Pandas, Odoo XML-RPC Client

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #F0E68C |
| Stereotype | <<Component>> |

### 2.4.4.0 Application Environment

#### 2.4.4.1 Repository Id

REPO-TMS-CORE-STAGING

#### 2.4.4.2 Display Name

REPO-TMS-CORE (Staging)

#### 2.4.4.3 Type

🔹 Application Environment

#### 2.4.4.4 Technology

Odoo 18, PostgreSQL 16 (AWS RDS)

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #87CEEB |
| Stereotype | <<Staging>> |

### 2.4.5.0 Application Environment

#### 2.4.5.1 Repository Id

REPO-TMS-CORE

#### 2.4.5.2 Display Name

REPO-TMS-CORE (Production)

#### 2.4.5.3 Type

🔹 Application Environment

#### 2.4.5.4 Technology

Odoo 18, PostgreSQL 16 (AWS RDS)

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #3CB371 |
| Stereotype | <<Production>> |

## 2.5.0.0 Interactions

### 2.5.1.0 DataExtraction

#### 2.5.1.1 Source Id

MIGRATION-OPERATOR

#### 2.5.1.2 Target Id

LEGACY-SYSTEM-DB

#### 2.5.1.3 Message

1. Extract Active Data to CSVs (as per REQ-TRN-002)

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 DataExtraction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

2. Return CSV files (customers.csv, vehicles.csv, drivers.csv, open_invoices.csv)

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL Query / File Transfer |
| Method | SELECT ... INTO OUTFILE / scp |
| Parameters | Scope definition from REQ-TRN-002: active customer... |
| Authentication | Database credentials for legacy system. |
| Error Handling | Log SQL errors. Verify file integrity with checksu... |
| Performance | Extraction must complete within 1 hour. |

### 2.5.2.0 ProcessExecution

#### 2.5.2.1 Source Id

MIGRATION-OPERATOR

#### 2.5.2.2 Target Id

PYTHON-MIGRATION-SCRIPTS

#### 2.5.2.3 Message

3. Execute Dry-Run Transformation

#### 2.5.2.4 Sequence Number

3

#### 2.5.2.5 Type

🔹 ProcessExecution

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

9. Return Dry-Run Summary (Record Counts, Error Log)

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

✅ Yes

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Shell Command |
| Method | python migrate.py --mode=dry-run --config=staging.... |
| Parameters | Input CSV file paths, Staging DB credentials. |
| Authentication | N/A |
| Error Handling | Script exits with non-zero code on critical failur... |
| Performance | Process 50k records < 30 minutes. |

#### 2.5.2.11 Nested Interactions

##### 2.5.2.11.1 InternalProcessing

###### 2.5.2.11.1.1 Source Id

PYTHON-MIGRATION-SCRIPTS

###### 2.5.2.11.1.2 Target Id

PYTHON-MIGRATION-SCRIPTS

###### 2.5.2.11.1.3 Message

4. Loop (for each row): Read, Cleanse, Validate, Transform to Odoo Schema

###### 2.5.2.11.1.4 Sequence Number

4

###### 2.5.2.11.1.5 Type

🔹 InternalProcessing

###### 2.5.2.11.1.6 Is Synchronous

✅ Yes

###### 2.5.2.11.1.7 Return Message



###### 2.5.2.11.1.8 Has Return

❌ No

###### 2.5.2.11.1.9 Is Activation

❌ No

###### 2.5.2.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | In-Memory |
| Method | data_cleanse(), validate_format(), map_to_odoo_mod... |
| Parameters | Pandas DataFrame row. |
| Authentication | N/A |
| Error Handling | Invalid rows are skipped and written to 'errors.cs... |
| Performance | High-speed in-memory operations. |

##### 2.5.2.11.2.0 DataLoad

###### 2.5.2.11.2.1 Source Id

PYTHON-MIGRATION-SCRIPTS

###### 2.5.2.11.2.2 Target Id

REPO-TMS-CORE-STAGING

###### 2.5.2.11.2.3 Message

5. Load Transformed Data Batch

###### 2.5.2.11.2.4 Sequence Number

5

###### 2.5.2.11.2.5 Type

🔹 DataLoad

###### 2.5.2.11.2.6 Is Synchronous

✅ Yes

###### 2.5.2.11.2.7 Return Message

6. Return Batch Import Result (Success/Failure)

###### 2.5.2.11.2.8 Has Return

✅ Yes

###### 2.5.2.11.2.9 Is Activation

✅ Yes

###### 2.5.2.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo XML-RPC |
| Method | object.execute_kw(db, uid, password, model, 'load'... |
| Parameters | Model name ('res.partner', etc.), fields, data (li... |
| Authentication | Staging Odoo admin user credentials. |
| Error Handling | Odoo API will return errors for constraint violati... |
| Performance | Use batch sizes of 1000 records to optimize perfor... |

### 2.5.3.0.0.0 DataValidation

#### 2.5.3.1.0.0 Source Id

MIGRATION-OPERATOR

#### 2.5.3.2.0.0 Target Id

REPO-TMS-CORE-STAGING

#### 2.5.3.3.0.0 Message

7. Execute Post-Dry-Run Validation Checks

#### 2.5.3.4.0.0 Sequence Number

7

#### 2.5.3.5.0.0 Type

🔹 DataValidation

#### 2.5.3.6.0.0 Is Synchronous

✅ Yes

#### 2.5.3.7.0.0 Return Message

8. Return Validation Results (Record Counts, Financial Totals)

#### 2.5.3.8.0.0 Has Return

✅ Yes

#### 2.5.3.9.0.0 Is Activation

✅ Yes

#### 2.5.3.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL / Odoo ORM |
| Method | SELECT COUNT(*), SELECT SUM(amount_total) |
| Parameters | Table names (res_partner, account_move). |
| Authentication | Staging DB read-only user. |
| Error Handling | Compare returned values against source totals; dis... |
| Performance | Queries must be optimized and run in seconds. |

### 2.5.4.0.0.0 SystemCommand

#### 2.5.4.1.0.0 Source Id

MIGRATION-OPERATOR

#### 2.5.4.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.4.3.0.0 Message

10. [During Cutover] Take DB Backup & Freeze Transactions

#### 2.5.4.4.0.0 Sequence Number

10

#### 2.5.4.5.0.0 Type

🔹 SystemCommand

#### 2.5.4.6.0.0 Is Synchronous

✅ Yes

#### 2.5.4.7.0.0 Return Message

11. Acknowledge Maintenance Mode

#### 2.5.4.8.0.0 Has Return

✅ Yes

#### 2.5.4.9.0.0 Is Activation

✅ Yes

#### 2.5.4.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS CLI / Odoo Admin |
| Method | aws rds create-db-snapshot; Odoo Maintenance Mode ... |
| Parameters | DB instance identifier, snapshot identifier. |
| Authentication | AWS IAM Role, Odoo Admin credentials. |
| Error Handling | Migration cannot proceed if backup fails. |
| Performance | N/A |

### 2.5.5.0.0.0 ProcessExecution

#### 2.5.5.1.0.0 Source Id

MIGRATION-OPERATOR

#### 2.5.5.2.0.0 Target Id

PYTHON-MIGRATION-SCRIPTS

#### 2.5.5.3.0.0 Message

12. Execute Production Migration

#### 2.5.5.4.0.0 Sequence Number

12

#### 2.5.5.5.0.0 Type

🔹 ProcessExecution

#### 2.5.5.6.0.0 Is Synchronous

✅ Yes

#### 2.5.5.7.0.0 Return Message

14. Return Production-Run Summary

#### 2.5.5.8.0.0 Has Return

✅ Yes

#### 2.5.5.9.0.0 Is Activation

✅ Yes

#### 2.5.5.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Shell Command |
| Method | python migrate.py --mode=production --config=produ... |
| Parameters | Input CSV file paths, Production DB credentials in... |
| Authentication | N/A |
| Error Handling | Any failure triggers the rollback plan. No errors ... |
| Performance | Must complete within the allocated cutover window ... |

#### 2.5.5.11.0.0 Nested Interactions

- {'sourceId': 'PYTHON-MIGRATION-SCRIPTS', 'targetId': 'REPO-TMS-CORE', 'message': '13. Load Transformed Data Batch to Production', 'sequenceNumber': 13, 'type': 'DataLoad', 'isSynchronous': True, 'returnMessage': 'Return Batch Import Result (Success)', 'hasReturn': True, 'isActivation': True, 'technicalDetails': {'protocol': 'Odoo XML-RPC', 'method': "object.execute_kw(db, uid, password, model, 'load', ...)", 'parameters': 'Model name, fields, data.', 'authentication': 'Production Odoo admin user credentials (from AWS Secrets Manager).', 'errorHandling': 'A single failure will abort the entire script and trigger the system rollback procedure.', 'performance': 'Optimized batch sizes are critical to stay within the cutover window.'}}

### 2.5.6.0.0.0 DataValidation

#### 2.5.6.1.0.0 Source Id

MIGRATION-OPERATOR

#### 2.5.6.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.6.3.0.0 Message

15. Execute Final Post-Migration Validation

#### 2.5.6.4.0.0 Sequence Number

15

#### 2.5.6.5.0.0 Type

🔹 DataValidation

#### 2.5.6.6.0.0 Is Synchronous

✅ Yes

#### 2.5.6.7.0.0 Return Message

16. Return Final Validation Results

#### 2.5.6.8.0.0 Has Return

✅ Yes

#### 2.5.6.9.0.0 Is Activation

✅ Yes

#### 2.5.6.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL / Odoo ORM |
| Method | SELECT COUNT(*), SELECT SUM(amount_total) |
| Parameters | Same validation queries as the dry-run. |
| Authentication | Production DB read-only user. |
| Error Handling | Discrepancies trigger the rollback plan. |
| Performance | Queries must run instantly. |

### 2.5.7.0.0.0 SystemCommand

#### 2.5.7.1.0.0 Source Id

MIGRATION-OPERATOR

#### 2.5.7.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.7.3.0.0 Message

17. Disable Maintenance Mode & Enable User Access

#### 2.5.7.4.0.0 Sequence Number

17

#### 2.5.7.5.0.0 Type

🔹 SystemCommand

#### 2.5.7.6.0.0 Is Synchronous

✅ Yes

#### 2.5.7.7.0.0 Return Message

18. Acknowledge Go-Live

#### 2.5.7.8.0.0 Has Return

✅ Yes

#### 2.5.7.9.0.0 Is Activation

✅ Yes

#### 2.5.7.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo Admin |
| Method | Odoo Maintenance Mode UI |
| Parameters | N/A |
| Authentication | Odoo Admin credentials. |
| Error Handling | N/A |
| Performance | N/A |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

The Dry-Run phase (Steps 3-8) is mandatory and may be iterated multiple times to resolve all data validation and transformation issues before attempting the production migration.

#### 2.6.1.2.0.0 Position

top

#### 2.6.1.3.0.0 Participant Id

PYTHON-MIGRATION-SCRIPTS

#### 2.6.1.4.0.0 Sequence Number

3

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

The Production Migration (Steps 10-18) is a critical, time-sensitive operation. A failure at any point must trigger the formal Rollback Plan (restore DB from pre-migration backup and revert user access).

#### 2.6.2.2.0.0 Position

bottom

#### 2.6.2.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.2.4.0.0 Sequence Number

12

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Production database credentials must not be stored... |
| Performance Targets | The entire production ETL process must be complete... |
| Error Handling Strategy | The ETL script must implement robust error handlin... |
| Testing Considerations | A comprehensive test suite for the Python scripts ... |
| Monitoring Requirements | The migration script must provide verbose logging,... |
| Deployment Considerations | The Python scripts and their dependencies should b... |


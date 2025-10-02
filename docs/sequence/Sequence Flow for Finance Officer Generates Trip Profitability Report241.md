# 1 Overview

## 1.1 Diagram Id

SEQ-DF-018

## 1.2 Name

Finance Officer Generates Trip Profitability Report

## 1.3 Description

A Finance Officer requests the Trip Profitability Report for a specific date range. The system queries the database, aggregates revenue and approved expense data, calculates the profit for each trip, and renders the report.

## 1.4 Type

🔹 DataFlow

## 1.5 Purpose

To provide financial insights by generating a report that details the profitability of individual trips based on recorded revenue and approved expenses.

## 1.6 Complexity

Medium

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- Finance Officer selects the 'Trip Profitability Report' menu item and sets a date filter.
- The Odoo controller receives the request.
- The ORM constructs a SQL query to fetch all trips within the date range.
- The query joins the Trip model with the Approved Expense model.
- The database aggregates total revenue and the sum of approved expenses for each trip.
- The result set is returned to the Odoo controller.
- The controller calculates profitability (Revenue - Expenses) for each row.
- The final data is passed to the QWeb reporting engine to render the PDF/Excel output.

## 1.11 Triggers

- User request for the profitability report.

## 1.12 Outcomes

- A downloadable report (PDF/Excel) is generated.
- The user gains insight into the financial performance of trips.

## 1.13 Business Rules

- REQ-FNC-007: Profitability is calculated as Revenue - Approved Expenses.
- REQ-REP-001: The system must provide a Trip Profitability Report.

## 1.14 Error Scenarios

- The database query times out due to a very large date range.

## 1.15 Integration Points

- Database: Amazon RDS for PostgreSQL

# 2.0 Details

## 2.1 Diagram Id

SEQ-DF-018

## 2.2 Name

Finance Officer Generates Trip Profitability Report Data Flow

## 2.3 Description

Detailed technical sequence for generating the Trip Profitability Report. A Finance Officer initiates a request via the Odoo UI, which is handled by a secured controller. The Odoo ORM constructs an optimized SQL query to aggregate trip revenue and approved expenses from the PostgreSQL database. The controller calculates the final profit and passes the dataset to the QWeb engine for rendering a downloadable PDF/Excel report. This sequence emphasizes query optimization, data aggregation, and role-based security.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

User-Browser

#### 2.4.1.2 Display Name

User Browser

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Odoo Web Library (OWL), HTML5

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6F7FF |
| Stereotype | UI |

### 2.4.2.0 Controller

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

Odoo Controller

#### 2.4.2.3 Type

🔹 Controller

#### 2.4.2.4 Technology

Odoo 18, Python 3.11

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #D4EDDA |
| Stereotype | Business Logic Layer |

### 2.4.3.0 ORM

#### 2.4.3.1 Repository Id

REPO-TMS-CORE-ORM

#### 2.4.3.2 Display Name

Odoo ORM / Models

#### 2.4.3.3 Type

🔹 ORM

#### 2.4.3.4 Technology

Odoo 18 ORM

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #FFF3CD |
| Stereotype | Data Access Layer |

### 2.4.4.0 Database

#### 2.4.4.1 Repository Id

REPO-TMS-CORE-DB

#### 2.4.4.2 Display Name

PostgreSQL Database

#### 2.4.4.3 Type

🔹 Database

#### 2.4.4.4 Technology

Amazon RDS for PostgreSQL 16

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #F8D7DA |
| Stereotype | Infrastructure Layer |

## 2.5.0.0 Interactions

### 2.5.1.0 Request

#### 2.5.1.1 Source Id

User-Browser

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

POST /report/tms/profitability

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Request

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

HTTP 200 OK with report file

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST |
| Parameters | Payload: {'start_date': 'YYYY-MM-DD', 'end_date': ... |
| Authentication | Requires valid Odoo Session Cookie (session_id). |
| Error Handling | Client-side handling for network errors or non-200... |
| Performance | User action triggers a single, synchronous request... |

### 2.5.2.0 InternalProcessing

#### 2.5.2.1 Source Id

REPO-TMS-CORE

#### 2.5.2.2 Target Id

REPO-TMS-CORE

#### 2.5.2.3 Message

validateRequest(auth, params)

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 InternalProcessing

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

Validation status (success/fail)

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | check_access_rights, validate_params |
| Parameters | User context (self.env.user), request parameters (... |
| Authentication | Verifies user is in 'Finance Officer' or 'Admin' s... |
| Error Handling | Raises `AccessError` (HTTP 403) if unauthorized. R... |
| Performance | Negligible performance impact. |

### 2.5.3.0 DataAccessRequest

#### 2.5.3.1 Source Id

REPO-TMS-CORE

#### 2.5.3.2 Target Id

REPO-TMS-CORE-ORM

#### 2.5.3.3 Message

fetch_profitability_data(start_date, end_date)

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 DataAccessRequest

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

List of aggregated data dictionaries

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | self.env.cr.execute(query, params) |
| Parameters | A raw SQL query and date parameters to avoid ORM p... |
| Authentication | Connection to the database uses credentials manage... |
| Error Handling | Propagates database exceptions (e.g., timeout) to ... |
| Performance | Bypasses the ORM's object instantiation for read p... |

### 2.5.4.0 DatabaseQuery

#### 2.5.4.1 Source Id

REPO-TMS-CORE-ORM

#### 2.5.4.2 Target Id

REPO-TMS-CORE-DB

#### 2.5.4.3 Message

EXECUTE SQL Query for Aggregated Data

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 DatabaseQuery

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

Result Set (rows of aggregated data)

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | SELECT |
| Parameters | SQL: SELECT t.id, t.name, t.revenue, COALESCE(SUM(... |
| Authentication | N/A (Handled by Odoo's connection pool). |
| Error Handling | Database handles query execution. May raise timeou... |
| Performance | Crucial for overall performance. Requires composit... |

### 2.5.5.0 DataResponse

#### 2.5.5.1 Source Id

REPO-TMS-CORE-DB

#### 2.5.5.2 Target Id

REPO-TMS-CORE-ORM

#### 2.5.5.3 Message

Return Aggregated Data Rows

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 DataResponse

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message



#### 2.5.5.8 Has Return

❌ No

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | Data Rows |
| Parameters | A stream of rows matching the query. |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | The size of the result set directly impacts networ... |

### 2.5.6.0 DataResponse

#### 2.5.6.1 Source Id

REPO-TMS-CORE-ORM

#### 2.5.6.2 Target Id

REPO-TMS-CORE

#### 2.5.6.3 Message

Return list of dicts

#### 2.5.6.4 Sequence Number

6

#### 2.5.6.5 Type

🔹 DataResponse

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Return Message



#### 2.5.6.8 Has Return

❌ No

#### 2.5.6.9 Is Activation

❌ No

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | Returns a list of dictionaries, e.g., `[{'id': 1, ... |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | The result set is held in the Odoo worker's memory... |

### 2.5.7.0 InternalProcessing

#### 2.5.7.1 Source Id

REPO-TMS-CORE

#### 2.5.7.2 Target Id

REPO-TMS-CORE

#### 2.5.7.3 Message

calculateProfitability(data)

#### 2.5.7.4 Sequence Number

7

#### 2.5.7.5 Type

🔹 InternalProcessing

#### 2.5.7.6 Is Synchronous

✅ Yes

#### 2.5.7.7 Return Message

Enriched data with 'profit' key

#### 2.5.7.8 Has Return

✅ Yes

#### 2.5.7.9 Is Activation

❌ No

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | Python loop |
| Parameters | The list of aggregated data dictionaries from the ... |
| Authentication | N/A |
| Error Handling | Handles potential KeyError if a field is missing, ... |
| Performance | Low CPU and memory overhead, linear complexity bas... |

### 2.5.8.0 Rendering

#### 2.5.8.1 Source Id

REPO-TMS-CORE

#### 2.5.8.2 Target Id

REPO-TMS-CORE

#### 2.5.8.3 Message

renderReport(template_name, data)

#### 2.5.8.4 Sequence Number

8

#### 2.5.8.5 Type

🔹 Rendering

#### 2.5.8.6 Is Synchronous

✅ Yes

#### 2.5.8.7 Return Message

Binary content of the report file

#### 2.5.8.8 Has Return

✅ Yes

#### 2.5.8.9 Is Activation

❌ No

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Odoo API Call |
| Method | self.env['ir.actions.report']._render_qweb_pdf(rep... |
| Parameters | Report XML ID ('tms.report_profitability'), proces... |
| Authentication | N/A |
| Error Handling | Catches QWeb template rendering errors. |
| Performance | Can be CPU-intensive, especially for large PDF rep... |

### 2.5.9.0 Response

#### 2.5.9.1 Source Id

REPO-TMS-CORE

#### 2.5.9.2 Target Id

User-Browser

#### 2.5.9.3 Message

Return HTTP 200 OK with Report File

#### 2.5.9.4 Sequence Number

9

#### 2.5.9.5 Type

🔹 Response

#### 2.5.9.6 Is Synchronous

✅ Yes

#### 2.5.9.7 Return Message



#### 2.5.9.8 Has Return

❌ No

#### 2.5.9.9 Is Activation

❌ No

#### 2.5.9.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | HTTP Response |
| Parameters | Headers: {'Content-Type': 'application/pdf', 'Cont... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | File download time depends on report size and netw... |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

Transaction Management: This entire operation is a read-only process. Odoo automatically wraps the HTTP request in a database transaction with a `READ COMMITTED` isolation level, which is sufficient for this reporting use case.

#### 2.6.1.2 Position

bottom

#### 2.6.1.3 Participant Id

*Not specified*

#### 2.6.1.4 Sequence Number

*Not specified*

### 2.6.2.0 Content

#### 2.6.2.1 Content

Query Optimization is critical. Using a raw, optimized SQL query via `env.cr.execute()` is preferred over the standard ORM `search_read_group` for this type of complex aggregation to avoid performance bottlenecks.

#### 2.6.2.2 Position

right

#### 2.6.2.3 Participant Id

REPO-TMS-CORE-ORM

#### 2.6.2.4 Sequence Number

4

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The Odoo controller endpoint (`/report/tms/profita... |
| Performance Targets | The p95 latency for report generation must be unde... |
| Error Handling Strategy | The controller must validate date range inputs to ... |
| Testing Considerations | Develop an integration test using a dataset with t... |
| Monitoring Requirements | Log the report generation request with user ID and... |
| Deployment Considerations | Ensure the PostgreSQL database has B-tree indexes ... |


# 1 Title

TMS Odoo Monolith Database

# 2 Name

tms_postgres_db

# 3 Db Type

- relational

# 4 Db Technology

PostgreSQL 16

# 5 Entities

## 5.1 User (res.users)

### 5.1.1 Name

User (res.users)

### 5.1.2 Description

Represents system users, leveraging Odoo's 'res.users' model. Manages authentication and role assignments. The TMS addon assigns users to specific 'res.groups' to implement role-based access. REQ-1-008.

### 5.1.3 Attributes

#### 5.1.3.1 id

##### 5.1.3.1.1 Name

id

##### 5.1.3.1.2 Type

🔹 INT

##### 5.1.3.1.3 Is Required

✅ Yes

##### 5.1.3.1.4 Is Primary Key

✅ Yes

##### 5.1.3.1.5 Size

0

##### 5.1.3.1.6 Is Unique

✅ Yes

##### 5.1.3.1.7 Constraints

*No items available*

##### 5.1.3.1.8 Precision

0

##### 5.1.3.1.9 Scale

0

##### 5.1.3.1.10 Is Foreign Key

❌ No

#### 5.1.3.2.0 name

##### 5.1.3.2.1 Name

name

##### 5.1.3.2.2 Type

🔹 VARCHAR

##### 5.1.3.2.3 Is Required

✅ Yes

##### 5.1.3.2.4 Is Primary Key

❌ No

##### 5.1.3.2.5 Size

255

##### 5.1.3.2.6 Is Unique

❌ No

##### 5.1.3.2.7 Constraints

*No items available*

##### 5.1.3.2.8 Precision

0

##### 5.1.3.2.9 Scale

0

##### 5.1.3.2.10 Is Foreign Key

❌ No

#### 5.1.3.3.0 login

##### 5.1.3.3.1 Name

login

##### 5.1.3.3.2 Type

🔹 VARCHAR

##### 5.1.3.3.3 Is Required

✅ Yes

##### 5.1.3.3.4 Is Primary Key

❌ No

##### 5.1.3.3.5 Size

255

##### 5.1.3.3.6 Is Unique

✅ Yes

##### 5.1.3.3.7 Constraints

*No items available*

##### 5.1.3.3.8 Precision

0

##### 5.1.3.3.9 Scale

0

##### 5.1.3.3.10 Is Foreign Key

❌ No

#### 5.1.3.4.0 password

##### 5.1.3.4.1 Name

password

##### 5.1.3.4.2 Type

🔹 VARCHAR

##### 5.1.3.4.3 Is Required

✅ Yes

##### 5.1.3.4.4 Is Primary Key

❌ No

##### 5.1.3.4.5 Size

255

##### 5.1.3.4.6 Is Unique

❌ No

##### 5.1.3.4.7 Constraints

*No items available*

##### 5.1.3.4.8 Precision

0

##### 5.1.3.4.9 Scale

0

##### 5.1.3.4.10 Is Foreign Key

❌ No

#### 5.1.3.5.0 active

##### 5.1.3.5.1 Name

active

##### 5.1.3.5.2 Type

🔹 BOOLEAN

##### 5.1.3.5.3 Is Required

✅ Yes

##### 5.1.3.5.4 Is Primary Key

❌ No

##### 5.1.3.5.5 Size

0

##### 5.1.3.5.6 Is Unique

❌ No

##### 5.1.3.5.7 Constraints

- DEFAULT true

##### 5.1.3.5.8 Precision

0

##### 5.1.3.5.9 Scale

0

##### 5.1.3.5.10 Is Foreign Key

❌ No

### 5.1.4.0.0 Primary Keys

- id

### 5.1.5.0.0 Unique Constraints

- {'name': 'res_users_login_key', 'columns': ['login']}

### 5.1.6.0.0 Indexes

*No items available*

## 5.2.0.0.0 Role (res.groups)

### 5.2.1.0.0 Name

Role (res.groups)

### 5.2.2.0.0 Description

Represents user roles (e.g., Admin, Dispatch Manager), leveraging Odoo's 'res.groups' model for access control. The TMS module creates groups like 'TMS Dispatch Manager', 'TMS Finance Officer', 'TMS Driver'. REQ-1-008.

### 5.2.3.0.0 Attributes

#### 5.2.3.1.0 id

##### 5.2.3.1.1 Name

id

##### 5.2.3.1.2 Type

🔹 INT

##### 5.2.3.1.3 Is Required

✅ Yes

##### 5.2.3.1.4 Is Primary Key

✅ Yes

##### 5.2.3.1.5 Size

0

##### 5.2.3.1.6 Is Unique

✅ Yes

##### 5.2.3.1.7 Constraints

*No items available*

##### 5.2.3.1.8 Precision

0

##### 5.2.3.1.9 Scale

0

##### 5.2.3.1.10 Is Foreign Key

❌ No

#### 5.2.3.2.0 name

##### 5.2.3.2.1 Name

name

##### 5.2.3.2.2 Type

🔹 VARCHAR

##### 5.2.3.2.3 Is Required

✅ Yes

##### 5.2.3.2.4 Is Primary Key

❌ No

##### 5.2.3.2.5 Size

255

##### 5.2.3.2.6 Is Unique

✅ Yes

##### 5.2.3.2.7 Constraints

*No items available*

##### 5.2.3.2.8 Precision

0

##### 5.2.3.2.9 Scale

0

##### 5.2.3.2.10 Is Foreign Key

❌ No

### 5.2.4.0.0 Primary Keys

- id

### 5.2.5.0.0 Unique Constraints

*No items available*

### 5.2.6.0.0 Indexes

*No items available*

## 5.3.0.0.0 Customer (res.partner)

### 5.3.1.0.0 Name

Customer (res.partner)

### 5.3.2.0.0 Description

Represents a customer, extending Odoo's 'res.partner' model with TMS-specific attributes. REQ-1-003, REQ-1-012, REQ-1-205.

### 5.3.3.0.0 Attributes

#### 5.3.3.1.0 id

##### 5.3.3.1.1 Name

id

##### 5.3.3.1.2 Type

🔹 INT

##### 5.3.3.1.3 Is Required

✅ Yes

##### 5.3.3.1.4 Is Primary Key

✅ Yes

##### 5.3.3.1.5 Size

0

##### 5.3.3.1.6 Is Unique

✅ Yes

##### 5.3.3.1.7 Constraints

*No items available*

##### 5.3.3.1.8 Precision

0

##### 5.3.3.1.9 Scale

0

##### 5.3.3.1.10 Is Foreign Key

❌ No

#### 5.3.3.2.0 name

##### 5.3.3.2.1 Name

name

##### 5.3.3.2.2 Type

🔹 VARCHAR

##### 5.3.3.2.3 Is Required

✅ Yes

##### 5.3.3.2.4 Is Primary Key

❌ No

##### 5.3.3.2.5 Size

255

##### 5.3.3.2.6 Is Unique

❌ No

##### 5.3.3.2.7 Constraints

*No items available*

##### 5.3.3.2.8 Precision

0

##### 5.3.3.2.9 Scale

0

##### 5.3.3.2.10 Is Foreign Key

❌ No

#### 5.3.3.3.0 gstin

##### 5.3.3.3.1 Name

gstin

##### 5.3.3.3.2 Type

🔹 VARCHAR

##### 5.3.3.3.3 Is Required

❌ No

##### 5.3.3.3.4 Is Primary Key

❌ No

##### 5.3.3.3.5 Size

15

##### 5.3.3.3.6 Is Unique

❌ No

##### 5.3.3.3.7 Constraints

- GSTIN_FORMAT_VALIDATION

##### 5.3.3.3.8 Precision

0

##### 5.3.3.3.9 Scale

0

##### 5.3.3.3.10 Is Foreign Key

❌ No

#### 5.3.3.4.0 is_tms_customer

##### 5.3.3.4.1 Name

is_tms_customer

##### 5.3.3.4.2 Type

🔹 BOOLEAN

##### 5.3.3.4.3 Is Required

✅ Yes

##### 5.3.3.4.4 Is Primary Key

❌ No

##### 5.3.3.4.5 Size

0

##### 5.3.3.4.6 Is Unique

❌ No

##### 5.3.3.4.7 Constraints

- DEFAULT true

##### 5.3.3.4.8 Precision

0

##### 5.3.3.4.9 Scale

0

##### 5.3.3.4.10 Is Foreign Key

❌ No

### 5.3.4.0.0 Primary Keys

- id

### 5.3.5.0.0 Unique Constraints

*No items available*

### 5.3.6.0.0 Indexes

#### 5.3.6.1.0 idx_res_partner_is_tms_customer

##### 5.3.6.1.1 Name

idx_res_partner_is_tms_customer

##### 5.3.6.1.2 Columns

- is_tms_customer

##### 5.3.6.1.3 Type

🔹 BTree

#### 5.3.6.2.0 idx_res_partner_gstin

##### 5.3.6.2.1 Name

idx_res_partner_gstin

##### 5.3.6.2.2 Columns

- gstin

##### 5.3.6.2.3 Type

🔹 BTree

## 5.4.0.0.0 Driver (hr.employee)

### 5.4.1.0.0 Name

Driver (hr.employee)

### 5.4.2.0.0 Description

Represents a driver, extending Odoo's 'hr.employee' model with TMS-specific attributes like license details. REQ-1-003, REQ-1-012, REQ-1-203.

### 5.4.3.0.0 Attributes

#### 5.4.3.1.0 id

##### 5.4.3.1.1 Name

id

##### 5.4.3.1.2 Type

🔹 INT

##### 5.4.3.1.3 Is Required

✅ Yes

##### 5.4.3.1.4 Is Primary Key

✅ Yes

##### 5.4.3.1.5 Size

0

##### 5.4.3.1.6 Is Unique

✅ Yes

##### 5.4.3.1.7 Constraints

*No items available*

##### 5.4.3.1.8 Precision

0

##### 5.4.3.1.9 Scale

0

##### 5.4.3.1.10 Is Foreign Key

❌ No

#### 5.4.3.2.0 name

##### 5.4.3.2.1 Name

name

##### 5.4.3.2.2 Type

🔹 VARCHAR

##### 5.4.3.2.3 Is Required

✅ Yes

##### 5.4.3.2.4 Is Primary Key

❌ No

##### 5.4.3.2.5 Size

255

##### 5.4.3.2.6 Is Unique

❌ No

##### 5.4.3.2.7 Constraints

*No items available*

##### 5.4.3.2.8 Precision

0

##### 5.4.3.2.9 Scale

0

##### 5.4.3.2.10 Is Foreign Key

❌ No

#### 5.4.3.3.0 license_number

##### 5.4.3.3.1 Name

license_number

##### 5.4.3.3.2 Type

🔹 VARCHAR

##### 5.4.3.3.3 Is Required

❌ No

##### 5.4.3.3.4 Is Primary Key

❌ No

##### 5.4.3.3.5 Size

50

##### 5.4.3.3.6 Is Unique

✅ Yes

##### 5.4.3.3.7 Constraints

*No items available*

##### 5.4.3.3.8 Precision

0

##### 5.4.3.3.9 Scale

0

##### 5.4.3.3.10 Is Foreign Key

❌ No

#### 5.4.3.4.0 license_expiry_date

##### 5.4.3.4.1 Name

license_expiry_date

##### 5.4.3.4.2 Type

🔹 Date

##### 5.4.3.4.3 Is Required

❌ No

##### 5.4.3.4.4 Is Primary Key

❌ No

##### 5.4.3.4.5 Size

0

##### 5.4.3.4.6 Is Unique

❌ No

##### 5.4.3.4.7 Constraints

*No items available*

##### 5.4.3.4.8 Precision

0

##### 5.4.3.4.9 Scale

0

##### 5.4.3.4.10 Is Foreign Key

❌ No

#### 5.4.3.5.0 is_tms_driver

##### 5.4.3.5.1 Name

is_tms_driver

##### 5.4.3.5.2 Type

🔹 BOOLEAN

##### 5.4.3.5.3 Is Required

✅ Yes

##### 5.4.3.5.4 Is Primary Key

❌ No

##### 5.4.3.5.5 Size

0

##### 5.4.3.5.6 Is Unique

❌ No

##### 5.4.3.5.7 Constraints

- DEFAULT true

##### 5.4.3.5.8 Precision

0

##### 5.4.3.5.9 Scale

0

##### 5.4.3.5.10 Is Foreign Key

❌ No

### 5.4.4.0.0 Primary Keys

- id

### 5.4.5.0.0 Unique Constraints

- {'name': 'uc_hr_employee_license_number', 'columns': ['license_number']}

### 5.4.6.0.0 Indexes

- {'name': 'idx_hr_employee_license_expiry_date', 'columns': ['license_expiry_date'], 'type': 'BTree'}

## 5.5.0.0.0 tms_vehicle

### 5.5.1.0.0 Name

tms_vehicle

### 5.5.2.0.0 Description

Represents a vehicle (truck) used for transport. REQ-1-200, REQ-1-202, REQ-1-900.

### 5.5.3.0.0 Attributes

#### 5.5.3.1.0 id

##### 5.5.3.1.1 Name

id

##### 5.5.3.1.2 Type

🔹 INT

##### 5.5.3.1.3 Is Required

✅ Yes

##### 5.5.3.1.4 Is Primary Key

✅ Yes

##### 5.5.3.1.5 Size

0

##### 5.5.3.1.6 Is Unique

✅ Yes

##### 5.5.3.1.7 Constraints

*No items available*

##### 5.5.3.1.8 Precision

0

##### 5.5.3.1.9 Scale

0

##### 5.5.3.1.10 Is Foreign Key

❌ No

#### 5.5.3.2.0 truck_number

##### 5.5.3.2.1 Name

truck_number

##### 5.5.3.2.2 Type

🔹 VARCHAR

##### 5.5.3.2.3 Is Required

✅ Yes

##### 5.5.3.2.4 Is Primary Key

❌ No

##### 5.5.3.2.5 Size

20

##### 5.5.3.2.6 Is Unique

✅ Yes

##### 5.5.3.2.7 Constraints

- UNIQUE

##### 5.5.3.2.8 Precision

0

##### 5.5.3.2.9 Scale

0

##### 5.5.3.2.10 Is Foreign Key

❌ No

#### 5.5.3.3.0 model

##### 5.5.3.3.1 Name

model

##### 5.5.3.3.2 Type

🔹 VARCHAR

##### 5.5.3.3.3 Is Required

❌ No

##### 5.5.3.3.4 Is Primary Key

❌ No

##### 5.5.3.3.5 Size

100

##### 5.5.3.3.6 Is Unique

❌ No

##### 5.5.3.3.7 Constraints

*No items available*

##### 5.5.3.3.8 Precision

0

##### 5.5.3.3.9 Scale

0

##### 5.5.3.3.10 Is Foreign Key

❌ No

#### 5.5.3.4.0 capacity_tons

##### 5.5.3.4.1 Name

capacity_tons

##### 5.5.3.4.2 Type

🔹 DECIMAL

##### 5.5.3.4.3 Is Required

✅ Yes

##### 5.5.3.4.4 Is Primary Key

❌ No

##### 5.5.3.4.5 Size

0

##### 5.5.3.4.6 Is Unique

❌ No

##### 5.5.3.4.7 Constraints

- POSITIVE_VALUE

##### 5.5.3.4.8 Precision

10

##### 5.5.3.4.9 Scale

2

##### 5.5.3.4.10 Is Foreign Key

❌ No

#### 5.5.3.5.0 ownership_type

##### 5.5.3.5.1 Name

ownership_type

##### 5.5.3.5.2 Type

🔹 VARCHAR

##### 5.5.3.5.3 Is Required

✅ Yes

##### 5.5.3.5.4 Is Primary Key

❌ No

##### 5.5.3.5.5 Size

20

##### 5.5.3.5.6 Is Unique

❌ No

##### 5.5.3.5.7 Constraints

- ENUM('Company-Owned', 'Outsourced')

##### 5.5.3.5.8 Precision

0

##### 5.5.3.5.9 Scale

0

##### 5.5.3.5.10 Is Foreign Key

❌ No

#### 5.5.3.6.0 status

##### 5.5.3.6.1 Name

status

##### 5.5.3.6.2 Type

🔹 VARCHAR

##### 5.5.3.6.3 Is Required

✅ Yes

##### 5.5.3.6.4 Is Primary Key

❌ No

##### 5.5.3.6.5 Size

20

##### 5.5.3.6.6 Is Unique

❌ No

##### 5.5.3.6.7 Constraints

- ENUM('Active', 'Inactive', 'In-Maintenance')

##### 5.5.3.6.8 Precision

0

##### 5.5.3.6.9 Scale

0

##### 5.5.3.6.10 Is Foreign Key

❌ No

#### 5.5.3.7.0 last_odometer_reading

##### 5.5.3.7.1 Name

last_odometer_reading

##### 5.5.3.7.2 Type

🔹 INT

##### 5.5.3.7.3 Is Required

❌ No

##### 5.5.3.7.4 Is Primary Key

❌ No

##### 5.5.3.7.5 Size

0

##### 5.5.3.7.6 Is Unique

❌ No

##### 5.5.3.7.7 Constraints

- NON_NEGATIVE

##### 5.5.3.7.8 Precision

0

##### 5.5.3.7.9 Scale

0

##### 5.5.3.7.10 Is Foreign Key

❌ No

#### 5.5.3.8.0 last_latitude

##### 5.5.3.8.1 Name

last_latitude

##### 5.5.3.8.2 Type

🔹 DECIMAL

##### 5.5.3.8.3 Is Required

❌ No

##### 5.5.3.8.4 Is Primary Key

❌ No

##### 5.5.3.8.5 Size

0

##### 5.5.3.8.6 Is Unique

❌ No

##### 5.5.3.8.7 Constraints

*No items available*

##### 5.5.3.8.8 Precision

9

##### 5.5.3.8.9 Scale

6

##### 5.5.3.8.10 Is Foreign Key

❌ No

#### 5.5.3.9.0 last_longitude

##### 5.5.3.9.1 Name

last_longitude

##### 5.5.3.9.2 Type

🔹 DECIMAL

##### 5.5.3.9.3 Is Required

❌ No

##### 5.5.3.9.4 Is Primary Key

❌ No

##### 5.5.3.9.5 Size

0

##### 5.5.3.9.6 Is Unique

❌ No

##### 5.5.3.9.7 Constraints

*No items available*

##### 5.5.3.9.8 Precision

9

##### 5.5.3.9.9 Scale

6

##### 5.5.3.9.10 Is Foreign Key

❌ No

#### 5.5.3.10.0 last_location_timestamp

##### 5.5.3.10.1 Name

last_location_timestamp

##### 5.5.3.10.2 Type

🔹 DateTime

##### 5.5.3.10.3 Is Required

❌ No

##### 5.5.3.10.4 Is Primary Key

❌ No

##### 5.5.3.10.5 Size

0

##### 5.5.3.10.6 Is Unique

❌ No

##### 5.5.3.10.7 Constraints

*No items available*

##### 5.5.3.10.8 Precision

0

##### 5.5.3.10.9 Scale

0

##### 5.5.3.10.10 Is Foreign Key

❌ No

#### 5.5.3.11.0 create_date

##### 5.5.3.11.1 Name

create_date

##### 5.5.3.11.2 Type

🔹 DateTime

##### 5.5.3.11.3 Is Required

❌ No

##### 5.5.3.11.4 Is Primary Key

❌ No

##### 5.5.3.11.5 Size

0

##### 5.5.3.11.6 Is Unique

❌ No

##### 5.5.3.11.7 Constraints

*No items available*

##### 5.5.3.11.8 Precision

0

##### 5.5.3.11.9 Scale

0

##### 5.5.3.11.10 Is Foreign Key

❌ No

#### 5.5.3.12.0 write_date

##### 5.5.3.12.1 Name

write_date

##### 5.5.3.12.2 Type

🔹 DateTime

##### 5.5.3.12.3 Is Required

❌ No

##### 5.5.3.12.4 Is Primary Key

❌ No

##### 5.5.3.12.5 Size

0

##### 5.5.3.12.6 Is Unique

❌ No

##### 5.5.3.12.7 Constraints

*No items available*

##### 5.5.3.12.8 Precision

0

##### 5.5.3.12.9 Scale

0

##### 5.5.3.12.10 Is Foreign Key

❌ No

### 5.5.4.0.0 Primary Keys

- id

### 5.5.5.0.0 Unique Constraints

- {'name': 'uc_tms_vehicle_truck_number', 'columns': ['truck_number']}

### 5.5.6.0.0 Indexes

- {'name': 'idx_tms_vehicle_status', 'columns': ['status'], 'type': 'BTree'}

## 5.6.0.0.0 tms_vehicle_document

### 5.6.1.0.0 Name

tms_vehicle_document

### 5.6.2.0.0 Description

Stores documents associated with a vehicle, such as RC, Insurance, etc., including their expiry dates. REQ-1-201.

### 5.6.3.0.0 Attributes

#### 5.6.3.1.0 id

##### 5.6.3.1.1 Name

id

##### 5.6.3.1.2 Type

🔹 INT

##### 5.6.3.1.3 Is Required

✅ Yes

##### 5.6.3.1.4 Is Primary Key

✅ Yes

##### 5.6.3.1.5 Size

0

##### 5.6.3.1.6 Is Unique

✅ Yes

##### 5.6.3.1.7 Constraints

*No items available*

##### 5.6.3.1.8 Precision

0

##### 5.6.3.1.9 Scale

0

##### 5.6.3.1.10 Is Foreign Key

❌ No

#### 5.6.3.2.0 vehicle_id

##### 5.6.3.2.1 Name

vehicle_id

##### 5.6.3.2.2 Type

🔹 INT

##### 5.6.3.2.3 Is Required

✅ Yes

##### 5.6.3.2.4 Is Primary Key

❌ No

##### 5.6.3.2.5 Size

0

##### 5.6.3.2.6 Is Unique

❌ No

##### 5.6.3.2.7 Constraints

*No items available*

##### 5.6.3.2.8 Precision

0

##### 5.6.3.2.9 Scale

0

##### 5.6.3.2.10 Is Foreign Key

✅ Yes

#### 5.6.3.3.0 document_type

##### 5.6.3.3.1 Name

document_type

##### 5.6.3.3.2 Type

🔹 VARCHAR

##### 5.6.3.3.3 Is Required

✅ Yes

##### 5.6.3.3.4 Is Primary Key

❌ No

##### 5.6.3.3.5 Size

50

##### 5.6.3.3.6 Is Unique

❌ No

##### 5.6.3.3.7 Constraints

*No items available*

##### 5.6.3.3.8 Precision

0

##### 5.6.3.3.9 Scale

0

##### 5.6.3.3.10 Is Foreign Key

❌ No

#### 5.6.3.4.0 expiry_date

##### 5.6.3.4.1 Name

expiry_date

##### 5.6.3.4.2 Type

🔹 Date

##### 5.6.3.4.3 Is Required

✅ Yes

##### 5.6.3.4.4 Is Primary Key

❌ No

##### 5.6.3.4.5 Size

0

##### 5.6.3.4.6 Is Unique

❌ No

##### 5.6.3.4.7 Constraints

*No items available*

##### 5.6.3.4.8 Precision

0

##### 5.6.3.4.9 Scale

0

##### 5.6.3.4.10 Is Foreign Key

❌ No

#### 5.6.3.5.0 attachment_url

##### 5.6.3.5.1 Name

attachment_url

##### 5.6.3.5.2 Type

🔹 VARCHAR

##### 5.6.3.5.3 Is Required

✅ Yes

##### 5.6.3.5.4 Is Primary Key

❌ No

##### 5.6.3.5.5 Size

512

##### 5.6.3.5.6 Is Unique

❌ No

##### 5.6.3.5.7 Constraints

*No items available*

##### 5.6.3.5.8 Precision

0

##### 5.6.3.5.9 Scale

0

##### 5.6.3.5.10 Is Foreign Key

❌ No

### 5.6.4.0.0 Primary Keys

- id

### 5.6.5.0.0 Unique Constraints

- {'name': 'uc_tms_vehicle_document_vehicle_type', 'columns': ['vehicle_id', 'document_type']}

### 5.6.6.0.0 Indexes

- {'name': 'idx_tms_vehicle_document_expiry_date', 'columns': ['expiry_date'], 'type': 'BTree'}

## 5.7.0.0.0 tms_material

### 5.7.1.0.0 Name

tms_material

### 5.7.2.0.0 Description

Master data for types of materials being transported. REQ-1-003.

### 5.7.3.0.0 Attributes

#### 5.7.3.1.0 id

##### 5.7.3.1.1 Name

id

##### 5.7.3.1.2 Type

🔹 INT

##### 5.7.3.1.3 Is Required

✅ Yes

##### 5.7.3.1.4 Is Primary Key

✅ Yes

##### 5.7.3.1.5 Size

0

##### 5.7.3.1.6 Is Unique

✅ Yes

##### 5.7.3.1.7 Constraints

*No items available*

##### 5.7.3.1.8 Precision

0

##### 5.7.3.1.9 Scale

0

##### 5.7.3.1.10 Is Foreign Key

❌ No

#### 5.7.3.2.0 name

##### 5.7.3.2.1 Name

name

##### 5.7.3.2.2 Type

🔹 VARCHAR

##### 5.7.3.2.3 Is Required

✅ Yes

##### 5.7.3.2.4 Is Primary Key

❌ No

##### 5.7.3.2.5 Size

100

##### 5.7.3.2.6 Is Unique

✅ Yes

##### 5.7.3.2.7 Constraints

*No items available*

##### 5.7.3.2.8 Precision

0

##### 5.7.3.2.9 Scale

0

##### 5.7.3.2.10 Is Foreign Key

❌ No

#### 5.7.3.3.0 description

##### 5.7.3.3.1 Name

description

##### 5.7.3.3.2 Type

🔹 TEXT

##### 5.7.3.3.3 Is Required

❌ No

##### 5.7.3.3.4 Is Primary Key

❌ No

##### 5.7.3.3.5 Size

0

##### 5.7.3.3.6 Is Unique

❌ No

##### 5.7.3.3.7 Constraints

*No items available*

##### 5.7.3.3.8 Precision

0

##### 5.7.3.3.9 Scale

0

##### 5.7.3.3.10 Is Foreign Key

❌ No

### 5.7.4.0.0 Primary Keys

- id

### 5.7.5.0.0 Unique Constraints

- {'name': 'uc_tms_material_name', 'columns': ['name']}

### 5.7.6.0.0 Indexes

*No items available*

## 5.8.0.0.0 tms_route

### 5.8.1.0.0 Name

tms_route

### 5.8.2.0.0 Description

Master data for predefined transport routes. REQ-1-003, REQ-1-206.

### 5.8.3.0.0 Attributes

#### 5.8.3.1.0 id

##### 5.8.3.1.1 Name

id

##### 5.8.3.1.2 Type

🔹 INT

##### 5.8.3.1.3 Is Required

✅ Yes

##### 5.8.3.1.4 Is Primary Key

✅ Yes

##### 5.8.3.1.5 Size

0

##### 5.8.3.1.6 Is Unique

✅ Yes

##### 5.8.3.1.7 Constraints

*No items available*

##### 5.8.3.1.8 Precision

0

##### 5.8.3.1.9 Scale

0

##### 5.8.3.1.10 Is Foreign Key

❌ No

#### 5.8.3.2.0 name

##### 5.8.3.2.1 Name

name

##### 5.8.3.2.2 Type

🔹 VARCHAR

##### 5.8.3.2.3 Is Required

✅ Yes

##### 5.8.3.2.4 Is Primary Key

❌ No

##### 5.8.3.2.5 Size

255

##### 5.8.3.2.6 Is Unique

✅ Yes

##### 5.8.3.2.7 Constraints

*No items available*

##### 5.8.3.2.8 Precision

0

##### 5.8.3.2.9 Scale

0

##### 5.8.3.2.10 Is Foreign Key

❌ No

#### 5.8.3.3.0 source_location

##### 5.8.3.3.1 Name

source_location

##### 5.8.3.3.2 Type

🔹 VARCHAR

##### 5.8.3.3.3 Is Required

✅ Yes

##### 5.8.3.3.4 Is Primary Key

❌ No

##### 5.8.3.3.5 Size

255

##### 5.8.3.3.6 Is Unique

❌ No

##### 5.8.3.3.7 Constraints

*No items available*

##### 5.8.3.3.8 Precision

0

##### 5.8.3.3.9 Scale

0

##### 5.8.3.3.10 Is Foreign Key

❌ No

#### 5.8.3.4.0 destination_location

##### 5.8.3.4.1 Name

destination_location

##### 5.8.3.4.2 Type

🔹 VARCHAR

##### 5.8.3.4.3 Is Required

✅ Yes

##### 5.8.3.4.4 Is Primary Key

❌ No

##### 5.8.3.4.5 Size

255

##### 5.8.3.4.6 Is Unique

❌ No

##### 5.8.3.4.7 Constraints

*No items available*

##### 5.8.3.4.8 Precision

0

##### 5.8.3.4.9 Scale

0

##### 5.8.3.4.10 Is Foreign Key

❌ No

#### 5.8.3.5.0 standard_distance_km

##### 5.8.3.5.1 Name

standard_distance_km

##### 5.8.3.5.2 Type

🔹 DECIMAL

##### 5.8.3.5.3 Is Required

✅ Yes

##### 5.8.3.5.4 Is Primary Key

❌ No

##### 5.8.3.5.5 Size

0

##### 5.8.3.5.6 Is Unique

❌ No

##### 5.8.3.5.7 Constraints

- POSITIVE_VALUE

##### 5.8.3.5.8 Precision

10

##### 5.8.3.5.9 Scale

2

##### 5.8.3.5.10 Is Foreign Key

❌ No

### 5.8.4.0.0 Primary Keys

- id

### 5.8.5.0.0 Unique Constraints

- {'name': 'uc_tms_route_name', 'columns': ['name']}

### 5.8.6.0.0 Indexes

*No items available*

## 5.9.0.0.0 tms_trip

### 5.9.1.0.0 Name

tms_trip

### 5.9.2.0.0 Description

The central entity representing a single transport job, tracking its entire lifecycle. REQ-1-004, REQ-1-102, REQ-1-103.

### 5.9.3.0.0 Attributes

#### 5.9.3.1.0 id

##### 5.9.3.1.1 Name

id

##### 5.9.3.1.2 Type

🔹 INT

##### 5.9.3.1.3 Is Required

✅ Yes

##### 5.9.3.1.4 Is Primary Key

✅ Yes

##### 5.9.3.1.5 Size

0

##### 5.9.3.1.6 Is Unique

✅ Yes

##### 5.9.3.1.7 Constraints

*No items available*

##### 5.9.3.1.8 Precision

0

##### 5.9.3.1.9 Scale

0

##### 5.9.3.1.10 Is Foreign Key

❌ No

#### 5.9.3.2.0 customer_id

##### 5.9.3.2.1 Name

customer_id

##### 5.9.3.2.2 Type

🔹 INT

##### 5.9.3.2.3 Is Required

✅ Yes

##### 5.9.3.2.4 Is Primary Key

❌ No

##### 5.9.3.2.5 Size

0

##### 5.9.3.2.6 Is Unique

❌ No

##### 5.9.3.2.7 Constraints

*No items available*

##### 5.9.3.2.8 Precision

0

##### 5.9.3.2.9 Scale

0

##### 5.9.3.2.10 Is Foreign Key

✅ Yes

#### 5.9.3.3.0 vehicle_id

##### 5.9.3.3.1 Name

vehicle_id

##### 5.9.3.3.2 Type

🔹 INT

##### 5.9.3.3.3 Is Required

❌ No

##### 5.9.3.3.4 Is Primary Key

❌ No

##### 5.9.3.3.5 Size

0

##### 5.9.3.3.6 Is Unique

❌ No

##### 5.9.3.3.7 Constraints

*No items available*

##### 5.9.3.3.8 Precision

0

##### 5.9.3.3.9 Scale

0

##### 5.9.3.3.10 Is Foreign Key

✅ Yes

#### 5.9.3.4.0 driver_id

##### 5.9.3.4.1 Name

driver_id

##### 5.9.3.4.2 Type

🔹 INT

##### 5.9.3.4.3 Is Required

❌ No

##### 5.9.3.4.4 Is Primary Key

❌ No

##### 5.9.3.4.5 Size

0

##### 5.9.3.4.6 Is Unique

❌ No

##### 5.9.3.4.7 Constraints

*No items available*

##### 5.9.3.4.8 Precision

0

##### 5.9.3.4.9 Scale

0

##### 5.9.3.4.10 Is Foreign Key

✅ Yes

#### 5.9.3.5.0 material_id

##### 5.9.3.5.1 Name

material_id

##### 5.9.3.5.2 Type

🔹 INT

##### 5.9.3.5.3 Is Required

✅ Yes

##### 5.9.3.5.4 Is Primary Key

❌ No

##### 5.9.3.5.5 Size

0

##### 5.9.3.5.6 Is Unique

❌ No

##### 5.9.3.5.7 Constraints

*No items available*

##### 5.9.3.5.8 Precision

0

##### 5.9.3.5.9 Scale

0

##### 5.9.3.5.10 Is Foreign Key

✅ Yes

#### 5.9.3.6.0 source

##### 5.9.3.6.1 Name

source

##### 5.9.3.6.2 Type

🔹 VARCHAR

##### 5.9.3.6.3 Is Required

✅ Yes

##### 5.9.3.6.4 Is Primary Key

❌ No

##### 5.9.3.6.5 Size

255

##### 5.9.3.6.6 Is Unique

❌ No

##### 5.9.3.6.7 Constraints

*No items available*

##### 5.9.3.6.8 Precision

0

##### 5.9.3.6.9 Scale

0

##### 5.9.3.6.10 Is Foreign Key

❌ No

#### 5.9.3.7.0 destination

##### 5.9.3.7.1 Name

destination

##### 5.9.3.7.2 Type

🔹 VARCHAR

##### 5.9.3.7.3 Is Required

✅ Yes

##### 5.9.3.7.4 Is Primary Key

❌ No

##### 5.9.3.7.5 Size

255

##### 5.9.3.7.6 Is Unique

❌ No

##### 5.9.3.7.7 Constraints

*No items available*

##### 5.9.3.7.8 Precision

0

##### 5.9.3.7.9 Scale

0

##### 5.9.3.7.10 Is Foreign Key

❌ No

#### 5.9.3.8.0 weight_tons

##### 5.9.3.8.1 Name

weight_tons

##### 5.9.3.8.2 Type

🔹 DECIMAL

##### 5.9.3.8.3 Is Required

✅ Yes

##### 5.9.3.8.4 Is Primary Key

❌ No

##### 5.9.3.8.5 Size

0

##### 5.9.3.8.6 Is Unique

❌ No

##### 5.9.3.8.7 Constraints

- POSITIVE_VALUE

##### 5.9.3.8.8 Precision

10

##### 5.9.3.8.9 Scale

3

##### 5.9.3.8.10 Is Foreign Key

❌ No

#### 5.9.3.9.0 rate

##### 5.9.3.9.1 Name

rate

##### 5.9.3.9.2 Type

🔹 DECIMAL

##### 5.9.3.9.3 Is Required

✅ Yes

##### 5.9.3.9.4 Is Primary Key

❌ No

##### 5.9.3.9.5 Size

0

##### 5.9.3.9.6 Is Unique

❌ No

##### 5.9.3.9.7 Constraints

- POSITIVE_VALUE

##### 5.9.3.9.8 Precision

12

##### 5.9.3.9.9 Scale

2

##### 5.9.3.9.10 Is Foreign Key

❌ No

#### 5.9.3.10.0 rate_type

##### 5.9.3.10.1 Name

rate_type

##### 5.9.3.10.2 Type

🔹 VARCHAR

##### 5.9.3.10.3 Is Required

✅ Yes

##### 5.9.3.10.4 Is Primary Key

❌ No

##### 5.9.3.10.5 Size

20

##### 5.9.3.10.6 Is Unique

❌ No

##### 5.9.3.10.7 Constraints

- ENUM('per_km', 'per_ton', 'fixed')

##### 5.9.3.10.8 Precision

0

##### 5.9.3.10.9 Scale

0

##### 5.9.3.10.10 Is Foreign Key

❌ No

#### 5.9.3.11.0 expected_delivery_date

##### 5.9.3.11.1 Name

expected_delivery_date

##### 5.9.3.11.2 Type

🔹 DateTime

##### 5.9.3.11.3 Is Required

✅ Yes

##### 5.9.3.11.4 Is Primary Key

❌ No

##### 5.9.3.11.5 Size

0

##### 5.9.3.11.6 Is Unique

❌ No

##### 5.9.3.11.7 Constraints

*No items available*

##### 5.9.3.11.8 Precision

0

##### 5.9.3.11.9 Scale

0

##### 5.9.3.11.10 Is Foreign Key

❌ No

#### 5.9.3.12.0 actual_delivery_date

##### 5.9.3.12.1 Name

actual_delivery_date

##### 5.9.3.12.2 Type

🔹 DateTime

##### 5.9.3.12.3 Is Required

❌ No

##### 5.9.3.12.4 Is Primary Key

❌ No

##### 5.9.3.12.5 Size

0

##### 5.9.3.12.6 Is Unique

❌ No

##### 5.9.3.12.7 Constraints

*No items available*

##### 5.9.3.12.8 Precision

0

##### 5.9.3.12.9 Scale

0

##### 5.9.3.12.10 Is Foreign Key

❌ No

#### 5.9.3.13.0 status

##### 5.9.3.13.1 Name

status

##### 5.9.3.13.2 Type

🔹 VARCHAR

##### 5.9.3.13.3 Is Required

✅ Yes

##### 5.9.3.13.4 Is Primary Key

❌ No

##### 5.9.3.13.5 Size

20

##### 5.9.3.13.6 Is Unique

❌ No

##### 5.9.3.13.7 Constraints

- ENUM('Planned', 'Assigned', 'In-Transit', 'On Hold', 'Delivered', 'Completed', 'Invoiced', 'Paid', 'Canceled')

##### 5.9.3.13.8 Precision

0

##### 5.9.3.13.9 Scale

0

##### 5.9.3.13.10 Is Foreign Key

❌ No

#### 5.9.3.14.0 create_date

##### 5.9.3.14.1 Name

create_date

##### 5.9.3.14.2 Type

🔹 DateTime

##### 5.9.3.14.3 Is Required

❌ No

##### 5.9.3.14.4 Is Primary Key

❌ No

##### 5.9.3.14.5 Size

0

##### 5.9.3.14.6 Is Unique

❌ No

##### 5.9.3.14.7 Constraints

*No items available*

##### 5.9.3.14.8 Precision

0

##### 5.9.3.14.9 Scale

0

##### 5.9.3.14.10 Is Foreign Key

❌ No

### 5.9.4.0.0 Primary Keys

- id

### 5.9.5.0.0 Unique Constraints

*No items available*

### 5.9.6.0.0 Indexes

#### 5.9.6.1.0 idx_tms_trip_status_expected_delivery_date

##### 5.9.6.1.1 Name

idx_tms_trip_status_expected_delivery_date

##### 5.9.6.1.2 Columns

- status
- expected_delivery_date

##### 5.9.6.1.3 Type

🔹 BTree

#### 5.9.6.2.0 idx_tms_trip_customer_id_status

##### 5.9.6.2.1 Name

idx_tms_trip_customer_id_status

##### 5.9.6.2.2 Columns

- customer_id
- status

##### 5.9.6.2.3 Type

🔹 BTree

#### 5.9.6.3.0 idx_tms_trip_driver_id_status

##### 5.9.6.3.1 Name

idx_tms_trip_driver_id_status

##### 5.9.6.3.2 Columns

- driver_id
- status

##### 5.9.6.3.3 Type

🔹 BTree

## 5.10.0.0.0 tms_expense

### 5.10.1.0.0 Name

tms_expense

### 5.10.2.0.0 Description

Records expenses submitted by drivers for a specific trip. REQ-1-107, REQ-1-108.

### 5.10.3.0.0 Attributes

#### 5.10.3.1.0 id

##### 5.10.3.1.1 Name

id

##### 5.10.3.1.2 Type

🔹 INT

##### 5.10.3.1.3 Is Required

✅ Yes

##### 5.10.3.1.4 Is Primary Key

✅ Yes

##### 5.10.3.1.5 Size

0

##### 5.10.3.1.6 Is Unique

✅ Yes

##### 5.10.3.1.7 Constraints

*No items available*

##### 5.10.3.1.8 Precision

0

##### 5.10.3.1.9 Scale

0

##### 5.10.3.1.10 Is Foreign Key

❌ No

#### 5.10.3.2.0 trip_id

##### 5.10.3.2.1 Name

trip_id

##### 5.10.3.2.2 Type

🔹 INT

##### 5.10.3.2.3 Is Required

✅ Yes

##### 5.10.3.2.4 Is Primary Key

❌ No

##### 5.10.3.2.5 Size

0

##### 5.10.3.2.6 Is Unique

❌ No

##### 5.10.3.2.7 Constraints

*No items available*

##### 5.10.3.2.8 Precision

0

##### 5.10.3.2.9 Scale

0

##### 5.10.3.2.10 Is Foreign Key

✅ Yes

#### 5.10.3.3.0 driver_id

##### 5.10.3.3.1 Name

driver_id

##### 5.10.3.3.2 Type

🔹 INT

##### 5.10.3.3.3 Is Required

✅ Yes

##### 5.10.3.3.4 Is Primary Key

❌ No

##### 5.10.3.3.5 Size

0

##### 5.10.3.3.6 Is Unique

❌ No

##### 5.10.3.3.7 Constraints

*No items available*

##### 5.10.3.3.8 Precision

0

##### 5.10.3.3.9 Scale

0

##### 5.10.3.3.10 Is Foreign Key

✅ Yes

#### 5.10.3.4.0 expense_type

##### 5.10.3.4.1 Name

expense_type

##### 5.10.3.4.2 Type

🔹 VARCHAR

##### 5.10.3.4.3 Is Required

✅ Yes

##### 5.10.3.4.4 Is Primary Key

❌ No

##### 5.10.3.4.5 Size

50

##### 5.10.3.4.6 Is Unique

❌ No

##### 5.10.3.4.7 Constraints

- ENUM('Diesel', 'Toll', 'Food', 'Repair', 'Other')

##### 5.10.3.4.8 Precision

0

##### 5.10.3.4.9 Scale

0

##### 5.10.3.4.10 Is Foreign Key

❌ No

#### 5.10.3.5.0 amount

##### 5.10.3.5.1 Name

amount

##### 5.10.3.5.2 Type

🔹 DECIMAL

##### 5.10.3.5.3 Is Required

✅ Yes

##### 5.10.3.5.4 Is Primary Key

❌ No

##### 5.10.3.5.5 Size

0

##### 5.10.3.5.6 Is Unique

❌ No

##### 5.10.3.5.7 Constraints

- POSITIVE_VALUE

##### 5.10.3.5.8 Precision

12

##### 5.10.3.5.9 Scale

2

##### 5.10.3.5.10 Is Foreign Key

❌ No

#### 5.10.3.6.0 receipt_url

##### 5.10.3.6.1 Name

receipt_url

##### 5.10.3.6.2 Type

🔹 VARCHAR

##### 5.10.3.6.3 Is Required

✅ Yes

##### 5.10.3.6.4 Is Primary Key

❌ No

##### 5.10.3.6.5 Size

512

##### 5.10.3.6.6 Is Unique

❌ No

##### 5.10.3.6.7 Constraints

*No items available*

##### 5.10.3.6.8 Precision

0

##### 5.10.3.6.9 Scale

0

##### 5.10.3.6.10 Is Foreign Key

❌ No

#### 5.10.3.7.0 status

##### 5.10.3.7.1 Name

status

##### 5.10.3.7.2 Type

🔹 VARCHAR

##### 5.10.3.7.3 Is Required

✅ Yes

##### 5.10.3.7.4 Is Primary Key

❌ No

##### 5.10.3.7.5 Size

20

##### 5.10.3.7.6 Is Unique

❌ No

##### 5.10.3.7.7 Constraints

- ENUM('Submitted', 'Approved', 'Rejected')

##### 5.10.3.7.8 Precision

0

##### 5.10.3.7.9 Scale

0

##### 5.10.3.7.10 Is Foreign Key

❌ No

#### 5.10.3.8.0 fuel_quantity_liters

##### 5.10.3.8.1 Name

fuel_quantity_liters

##### 5.10.3.8.2 Type

🔹 DECIMAL

##### 5.10.3.8.3 Is Required

❌ No

##### 5.10.3.8.4 Is Primary Key

❌ No

##### 5.10.3.8.5 Size

0

##### 5.10.3.8.6 Is Unique

❌ No

##### 5.10.3.8.7 Constraints

- POSITIVE_VALUE

##### 5.10.3.8.8 Precision

10

##### 5.10.3.8.9 Scale

2

##### 5.10.3.8.10 Is Foreign Key

❌ No

#### 5.10.3.9.0 odometer_reading

##### 5.10.3.9.1 Name

odometer_reading

##### 5.10.3.9.2 Type

🔹 INT

##### 5.10.3.9.3 Is Required

❌ No

##### 5.10.3.9.4 Is Primary Key

❌ No

##### 5.10.3.9.5 Size

0

##### 5.10.3.9.6 Is Unique

❌ No

##### 5.10.3.9.7 Constraints

- NON_NEGATIVE

##### 5.10.3.9.8 Precision

0

##### 5.10.3.9.9 Scale

0

##### 5.10.3.9.10 Is Foreign Key

❌ No

### 5.10.4.0.0 Primary Keys

- id

### 5.10.5.0.0 Unique Constraints

*No items available*

### 5.10.6.0.0 Indexes

- {'name': 'idx_tms_expense_trip_id_status', 'columns': ['trip_id', 'status'], 'type': 'BTree'}

## 5.11.0.0.0 Invoice (account.move)

### 5.11.1.0.0 Name

Invoice (account.move)

### 5.11.2.0.0 Description

Represents a GST-compliant invoice, extending Odoo's 'account.move' model. A trip invoice is created as a new 'account.move' record with TMS-specific data. REQ-1-005, REQ-1-006.

### 5.11.3.0.0 Attributes

#### 5.11.3.1.0 id

##### 5.11.3.1.1 Name

id

##### 5.11.3.1.2 Type

🔹 INT

##### 5.11.3.1.3 Is Required

✅ Yes

##### 5.11.3.1.4 Is Primary Key

✅ Yes

##### 5.11.3.1.5 Size

0

##### 5.11.3.1.6 Is Unique

✅ Yes

##### 5.11.3.1.7 Constraints

*No items available*

##### 5.11.3.1.8 Precision

0

##### 5.11.3.1.9 Scale

0

##### 5.11.3.1.10 Is Foreign Key

❌ No

#### 5.11.3.2.0 tms_trip_id

##### 5.11.3.2.1 Name

tms_trip_id

##### 5.11.3.2.2 Type

🔹 INT

##### 5.11.3.2.3 Is Required

❌ No

##### 5.11.3.2.4 Is Primary Key

❌ No

##### 5.11.3.2.5 Size

0

##### 5.11.3.2.6 Is Unique

✅ Yes

##### 5.11.3.2.7 Constraints

*No items available*

##### 5.11.3.2.8 Precision

0

##### 5.11.3.2.9 Scale

0

##### 5.11.3.2.10 Is Foreign Key

✅ Yes

#### 5.11.3.3.0 irn

##### 5.11.3.3.1 Name

irn

##### 5.11.3.3.2 Type

🔹 VARCHAR

##### 5.11.3.3.3 Is Required

❌ No

##### 5.11.3.3.4 Is Primary Key

❌ No

##### 5.11.3.3.5 Size

64

##### 5.11.3.3.6 Is Unique

✅ Yes

##### 5.11.3.3.7 Constraints

*No items available*

##### 5.11.3.3.8 Precision

0

##### 5.11.3.3.9 Scale

0

##### 5.11.3.3.10 Is Foreign Key

❌ No

#### 5.11.3.4.0 qr_code_data

##### 5.11.3.4.1 Name

qr_code_data

##### 5.11.3.4.2 Type

🔹 TEXT

##### 5.11.3.4.3 Is Required

❌ No

##### 5.11.3.4.4 Is Primary Key

❌ No

##### 5.11.3.4.5 Size

0

##### 5.11.3.4.6 Is Unique

❌ No

##### 5.11.3.4.7 Constraints

*No items available*

##### 5.11.3.4.8 Precision

0

##### 5.11.3.4.9 Scale

0

##### 5.11.3.4.10 Is Foreign Key

❌ No

### 5.11.4.0.0 Primary Keys

- id

### 5.11.5.0.0 Unique Constraints

- {'name': 'uc_account_move_tms_trip_id', 'columns': ['tms_trip_id']}

### 5.11.6.0.0 Indexes

*No items available*

## 5.12.0.0.0 tms_alert

### 5.12.1.0.0 Name

tms_alert

### 5.12.2.0.0 Description

Stores system-generated alerts for critical events like document expiry or low balances. REQ-1-010.

### 5.12.3.0.0 Attributes

#### 5.12.3.1.0 id

##### 5.12.3.1.1 Name

id

##### 5.12.3.1.2 Type

🔹 INT

##### 5.12.3.1.3 Is Required

✅ Yes

##### 5.12.3.1.4 Is Primary Key

✅ Yes

##### 5.12.3.1.5 Size

0

##### 5.12.3.1.6 Is Unique

✅ Yes

##### 5.12.3.1.7 Constraints

*No items available*

##### 5.12.3.1.8 Precision

0

##### 5.12.3.1.9 Scale

0

##### 5.12.3.1.10 Is Foreign Key

❌ No

#### 5.12.3.2.0 alert_type

##### 5.12.3.2.1 Name

alert_type

##### 5.12.3.2.2 Type

🔹 VARCHAR

##### 5.12.3.2.3 Is Required

✅ Yes

##### 5.12.3.2.4 Is Primary Key

❌ No

##### 5.12.3.2.5 Size

50

##### 5.12.3.2.6 Is Unique

❌ No

##### 5.12.3.2.7 Constraints

- ENUM('DocumentExpiry', 'LowBalance', 'CriticalTripEvent', 'Geofence')

##### 5.12.3.2.8 Precision

0

##### 5.12.3.2.9 Scale

0

##### 5.12.3.2.10 Is Foreign Key

❌ No

#### 5.12.3.3.0 message

##### 5.12.3.3.1 Name

message

##### 5.12.3.3.2 Type

🔹 TEXT

##### 5.12.3.3.3 Is Required

✅ Yes

##### 5.12.3.3.4 Is Primary Key

❌ No

##### 5.12.3.3.5 Size

0

##### 5.12.3.3.6 Is Unique

❌ No

##### 5.12.3.3.7 Constraints

*No items available*

##### 5.12.3.3.8 Precision

0

##### 5.12.3.3.9 Scale

0

##### 5.12.3.3.10 Is Foreign Key

❌ No

#### 5.12.3.4.0 res_model

##### 5.12.3.4.1 Name

res_model

##### 5.12.3.4.2 Type

🔹 VARCHAR

##### 5.12.3.4.3 Is Required

❌ No

##### 5.12.3.4.4 Is Primary Key

❌ No

##### 5.12.3.4.5 Size

100

##### 5.12.3.4.6 Is Unique

❌ No

##### 5.12.3.4.7 Constraints

*No items available*

##### 5.12.3.4.8 Precision

0

##### 5.12.3.4.9 Scale

0

##### 5.12.3.4.10 Is Foreign Key

❌ No

#### 5.12.3.5.0 res_id

##### 5.12.3.5.1 Name

res_id

##### 5.12.3.5.2 Type

🔹 INT

##### 5.12.3.5.3 Is Required

❌ No

##### 5.12.3.5.4 Is Primary Key

❌ No

##### 5.12.3.5.5 Size

0

##### 5.12.3.5.6 Is Unique

❌ No

##### 5.12.3.5.7 Constraints

*No items available*

##### 5.12.3.5.8 Precision

0

##### 5.12.3.5.9 Scale

0

##### 5.12.3.5.10 Is Foreign Key

❌ No

#### 5.12.3.6.0 status

##### 5.12.3.6.1 Name

status

##### 5.12.3.6.2 Type

🔹 VARCHAR

##### 5.12.3.6.3 Is Required

✅ Yes

##### 5.12.3.6.4 Is Primary Key

❌ No

##### 5.12.3.6.5 Size

20

##### 5.12.3.6.6 Is Unique

❌ No

##### 5.12.3.6.7 Constraints

- ENUM('New', 'Acknowledged', 'Resolved')

##### 5.12.3.6.8 Precision

0

##### 5.12.3.6.9 Scale

0

##### 5.12.3.6.10 Is Foreign Key

❌ No

### 5.12.4.0.0 Primary Keys

- id

### 5.12.5.0.0 Unique Constraints

*No items available*

### 5.12.6.0.0 Indexes

- {'name': 'idx_tms_alert_status_create_date', 'columns': ['status', 'create_date'], 'type': 'BTree'}

## 5.13.0.0.0 tms_geofence

### 5.13.1.0.0 Name

tms_geofence

### 5.13.2.0.0 Description

Defines geographical boundaries for monitoring vehicle entry and exit. Uses a GEOMETRY type for efficient spatial queries. REQ-1-106.

### 5.13.3.0.0 Attributes

#### 5.13.3.1.0 id

##### 5.13.3.1.1 Name

id

##### 5.13.3.1.2 Type

🔹 INT

##### 5.13.3.1.3 Is Required

✅ Yes

##### 5.13.3.1.4 Is Primary Key

✅ Yes

##### 5.13.3.1.5 Size

0

##### 5.13.3.1.6 Is Unique

✅ Yes

##### 5.13.3.1.7 Constraints

*No items available*

##### 5.13.3.1.8 Precision

0

##### 5.13.3.1.9 Scale

0

##### 5.13.3.1.10 Is Foreign Key

❌ No

#### 5.13.3.2.0 name

##### 5.13.3.2.1 Name

name

##### 5.13.3.2.2 Type

🔹 VARCHAR

##### 5.13.3.2.3 Is Required

✅ Yes

##### 5.13.3.2.4 Is Primary Key

❌ No

##### 5.13.3.2.5 Size

100

##### 5.13.3.2.6 Is Unique

✅ Yes

##### 5.13.3.2.7 Constraints

*No items available*

##### 5.13.3.2.8 Precision

0

##### 5.13.3.2.9 Scale

0

##### 5.13.3.2.10 Is Foreign Key

❌ No

#### 5.13.3.3.0 area

##### 5.13.3.3.1 Name

area

##### 5.13.3.3.2 Type

🔹 GEOMETRY

##### 5.13.3.3.3 Is Required

✅ Yes

##### 5.13.3.3.4 Is Primary Key

❌ No

##### 5.13.3.3.5 Size

0

##### 5.13.3.3.6 Is Unique

❌ No

##### 5.13.3.3.7 Constraints

- POLYGON or MULTIPOLYGON
- SRID=4326

##### 5.13.3.3.8 Precision

0

##### 5.13.3.3.9 Scale

0

##### 5.13.3.3.10 Is Foreign Key

❌ No

#### 5.13.3.4.0 active

##### 5.13.3.4.1 Name

active

##### 5.13.3.4.2 Type

🔹 BOOLEAN

##### 5.13.3.4.3 Is Required

✅ Yes

##### 5.13.3.4.4 Is Primary Key

❌ No

##### 5.13.3.4.5 Size

0

##### 5.13.3.4.6 Is Unique

❌ No

##### 5.13.3.4.7 Constraints

- DEFAULT true

##### 5.13.3.4.8 Precision

0

##### 5.13.3.4.9 Scale

0

##### 5.13.3.4.10 Is Foreign Key

❌ No

### 5.13.4.0.0 Primary Keys

- id

### 5.13.5.0.0 Unique Constraints

- {'name': 'uc_tms_geofence_name', 'columns': ['name']}

### 5.13.6.0.0 Indexes

- {'name': 'idx_tms_geofence_area', 'columns': ['area'], 'type': 'GiST'}

## 5.14.0.0.0 tms_card

### 5.14.1.0.0 Name

tms_card

### 5.14.2.0.0 Description

Manages FASTag and diesel cards, including manual balance tracking. REQ-1-110.

### 5.14.3.0.0 Attributes

#### 5.14.3.1.0 id

##### 5.14.3.1.1 Name

id

##### 5.14.3.1.2 Type

🔹 INT

##### 5.14.3.1.3 Is Required

✅ Yes

##### 5.14.3.1.4 Is Primary Key

✅ Yes

##### 5.14.3.1.5 Size

0

##### 5.14.3.1.6 Is Unique

✅ Yes

##### 5.14.3.1.7 Constraints

*No items available*

##### 5.14.3.1.8 Precision

0

##### 5.14.3.1.9 Scale

0

##### 5.14.3.1.10 Is Foreign Key

❌ No

#### 5.14.3.2.0 card_type

##### 5.14.3.2.1 Name

card_type

##### 5.14.3.2.2 Type

🔹 VARCHAR

##### 5.14.3.2.3 Is Required

✅ Yes

##### 5.14.3.2.4 Is Primary Key

❌ No

##### 5.14.3.2.5 Size

20

##### 5.14.3.2.6 Is Unique

❌ No

##### 5.14.3.2.7 Constraints

- ENUM('FASTag', 'Diesel')

##### 5.14.3.2.8 Precision

0

##### 5.14.3.2.9 Scale

0

##### 5.14.3.2.10 Is Foreign Key

❌ No

#### 5.14.3.3.0 card_number

##### 5.14.3.3.1 Name

card_number

##### 5.14.3.3.2 Type

🔹 VARCHAR

##### 5.14.3.3.3 Is Required

✅ Yes

##### 5.14.3.3.4 Is Primary Key

❌ No

##### 5.14.3.3.5 Size

50

##### 5.14.3.3.6 Is Unique

✅ Yes

##### 5.14.3.3.7 Constraints

*No items available*

##### 5.14.3.3.8 Precision

0

##### 5.14.3.3.9 Scale

0

##### 5.14.3.3.10 Is Foreign Key

❌ No

#### 5.14.3.4.0 assigned_vehicle_id

##### 5.14.3.4.1 Name

assigned_vehicle_id

##### 5.14.3.4.2 Type

🔹 INT

##### 5.14.3.4.3 Is Required

❌ No

##### 5.14.3.4.4 Is Primary Key

❌ No

##### 5.14.3.4.5 Size

0

##### 5.14.3.4.6 Is Unique

❌ No

##### 5.14.3.4.7 Constraints

*No items available*

##### 5.14.3.4.8 Precision

0

##### 5.14.3.4.9 Scale

0

##### 5.14.3.4.10 Is Foreign Key

✅ Yes

#### 5.14.3.5.0 balance

##### 5.14.3.5.1 Name

balance

##### 5.14.3.5.2 Type

🔹 DECIMAL

##### 5.14.3.5.3 Is Required

✅ Yes

##### 5.14.3.5.4 Is Primary Key

❌ No

##### 5.14.3.5.5 Size

0

##### 5.14.3.5.6 Is Unique

❌ No

##### 5.14.3.5.7 Constraints

*No items available*

##### 5.14.3.5.8 Precision

12

##### 5.14.3.5.9 Scale

2

##### 5.14.3.5.10 Is Foreign Key

❌ No

#### 5.14.3.6.0 low_balance_threshold

##### 5.14.3.6.1 Name

low_balance_threshold

##### 5.14.3.6.2 Type

🔹 DECIMAL

##### 5.14.3.6.3 Is Required

✅ Yes

##### 5.14.3.6.4 Is Primary Key

❌ No

##### 5.14.3.6.5 Size

0

##### 5.14.3.6.6 Is Unique

❌ No

##### 5.14.3.6.7 Constraints

*No items available*

##### 5.14.3.6.8 Precision

12

##### 5.14.3.6.9 Scale

2

##### 5.14.3.6.10 Is Foreign Key

❌ No

### 5.14.4.0.0 Primary Keys

- id

### 5.14.5.0.0 Unique Constraints

- {'name': 'uc_tms_card_card_number', 'columns': ['card_number']}

### 5.14.6.0.0 Indexes

*No items available*

## 5.15.0.0.0 tms_pod

### 5.15.1.0.0 Name

tms_pod

### 5.15.2.0.0 Description

Stores Proof of Delivery (POD) data, such as photos or e-signatures, for a trip. REQ-1-114.

### 5.15.3.0.0 Attributes

#### 5.15.3.1.0 id

##### 5.15.3.1.1 Name

id

##### 5.15.3.1.2 Type

🔹 INT

##### 5.15.3.1.3 Is Required

✅ Yes

##### 5.15.3.1.4 Is Primary Key

✅ Yes

##### 5.15.3.1.5 Size

0

##### 5.15.3.1.6 Is Unique

✅ Yes

##### 5.15.3.1.7 Constraints

*No items available*

##### 5.15.3.1.8 Precision

0

##### 5.15.3.1.9 Scale

0

##### 5.15.3.1.10 Is Foreign Key

❌ No

#### 5.15.3.2.0 trip_id

##### 5.15.3.2.1 Name

trip_id

##### 5.15.3.2.2 Type

🔹 INT

##### 5.15.3.2.3 Is Required

✅ Yes

##### 5.15.3.2.4 Is Primary Key

❌ No

##### 5.15.3.2.5 Size

0

##### 5.15.3.2.6 Is Unique

✅ Yes

##### 5.15.3.2.7 Constraints

*No items available*

##### 5.15.3.2.8 Precision

0

##### 5.15.3.2.9 Scale

0

##### 5.15.3.2.10 Is Foreign Key

✅ Yes

#### 5.15.3.3.0 pod_type

##### 5.15.3.3.1 Name

pod_type

##### 5.15.3.3.2 Type

🔹 VARCHAR

##### 5.15.3.3.3 Is Required

✅ Yes

##### 5.15.3.3.4 Is Primary Key

❌ No

##### 5.15.3.3.5 Size

20

##### 5.15.3.3.6 Is Unique

❌ No

##### 5.15.3.3.7 Constraints

- ENUM('Photo', 'eSignature')

##### 5.15.3.3.8 Precision

0

##### 5.15.3.3.9 Scale

0

##### 5.15.3.3.10 Is Foreign Key

❌ No

#### 5.15.3.4.0 pod_data_url

##### 5.15.3.4.1 Name

pod_data_url

##### 5.15.3.4.2 Type

🔹 VARCHAR

##### 5.15.3.4.3 Is Required

✅ Yes

##### 5.15.3.4.4 Is Primary Key

❌ No

##### 5.15.3.4.5 Size

512

##### 5.15.3.4.6 Is Unique

❌ No

##### 5.15.3.4.7 Constraints

*No items available*

##### 5.15.3.4.8 Precision

0

##### 5.15.3.4.9 Scale

0

##### 5.15.3.4.10 Is Foreign Key

❌ No

#### 5.15.3.5.0 recipient_name

##### 5.15.3.5.1 Name

recipient_name

##### 5.15.3.5.2 Type

🔹 VARCHAR

##### 5.15.3.5.3 Is Required

✅ Yes

##### 5.15.3.5.4 Is Primary Key

❌ No

##### 5.15.3.5.5 Size

255

##### 5.15.3.5.6 Is Unique

❌ No

##### 5.15.3.5.7 Constraints

*No items available*

##### 5.15.3.5.8 Precision

0

##### 5.15.3.5.9 Scale

0

##### 5.15.3.5.10 Is Foreign Key

❌ No

### 5.15.4.0.0 Primary Keys

- id

### 5.15.5.0.0 Unique Constraints

- {'name': 'uc_tms_pod_trip_id', 'columns': ['trip_id']}

### 5.15.6.0.0 Indexes

*No items available*

## 5.16.0.0.0 tms_trip_event_log

### 5.16.1.0.0 Name

tms_trip_event_log

### 5.16.2.0.0 Description

Logs events that occur during a trip, as reported by the driver. REQ-1-115.

### 5.16.3.0.0 Attributes

#### 5.16.3.1.0 id

##### 5.16.3.1.1 Name

id

##### 5.16.3.1.2 Type

🔹 INT

##### 5.16.3.1.3 Is Required

✅ Yes

##### 5.16.3.1.4 Is Primary Key

✅ Yes

##### 5.16.3.1.5 Size

0

##### 5.16.3.1.6 Is Unique

✅ Yes

##### 5.16.3.1.7 Constraints

*No items available*

##### 5.16.3.1.8 Precision

0

##### 5.16.3.1.9 Scale

0

##### 5.16.3.1.10 Is Foreign Key

❌ No

#### 5.16.3.2.0 trip_id

##### 5.16.3.2.1 Name

trip_id

##### 5.16.3.2.2 Type

🔹 INT

##### 5.16.3.2.3 Is Required

✅ Yes

##### 5.16.3.2.4 Is Primary Key

❌ No

##### 5.16.3.2.5 Size

0

##### 5.16.3.2.6 Is Unique

❌ No

##### 5.16.3.2.7 Constraints

*No items available*

##### 5.16.3.2.8 Precision

0

##### 5.16.3.2.9 Scale

0

##### 5.16.3.2.10 Is Foreign Key

✅ Yes

#### 5.16.3.3.0 driver_id

##### 5.16.3.3.1 Name

driver_id

##### 5.16.3.3.2 Type

🔹 INT

##### 5.16.3.3.3 Is Required

✅ Yes

##### 5.16.3.3.4 Is Primary Key

❌ No

##### 5.16.3.3.5 Size

0

##### 5.16.3.3.6 Is Unique

❌ No

##### 5.16.3.3.7 Constraints

*No items available*

##### 5.16.3.3.8 Precision

0

##### 5.16.3.3.9 Scale

0

##### 5.16.3.3.10 Is Foreign Key

✅ Yes

#### 5.16.3.4.0 event_type

##### 5.16.3.4.1 Name

event_type

##### 5.16.3.4.2 Type

🔹 VARCHAR

##### 5.16.3.4.3 Is Required

✅ Yes

##### 5.16.3.4.4 Is Primary Key

❌ No

##### 5.16.3.4.5 Size

50

##### 5.16.3.4.6 Is Unique

❌ No

##### 5.16.3.4.7 Constraints

- ENUM('Accident', 'Repair', 'Government Stoppage', 'Fueling', 'Trip Start')

##### 5.16.3.4.8 Precision

0

##### 5.16.3.4.9 Scale

0

##### 5.16.3.4.10 Is Foreign Key

❌ No

#### 5.16.3.5.0 event_timestamp

##### 5.16.3.5.1 Name

event_timestamp

##### 5.16.3.5.2 Type

🔹 DateTime

##### 5.16.3.5.3 Is Required

✅ Yes

##### 5.16.3.5.4 Is Primary Key

❌ No

##### 5.16.3.5.5 Size

0

##### 5.16.3.5.6 Is Unique

❌ No

##### 5.16.3.5.7 Constraints

*No items available*

##### 5.16.3.5.8 Precision

0

##### 5.16.3.5.9 Scale

0

##### 5.16.3.5.10 Is Foreign Key

❌ No

#### 5.16.3.6.0 photo_url

##### 5.16.3.6.1 Name

photo_url

##### 5.16.3.6.2 Type

🔹 VARCHAR

##### 5.16.3.6.3 Is Required

❌ No

##### 5.16.3.6.4 Is Primary Key

❌ No

##### 5.16.3.6.5 Size

512

##### 5.16.3.6.6 Is Unique

❌ No

##### 5.16.3.6.7 Constraints

*No items available*

##### 5.16.3.6.8 Precision

0

##### 5.16.3.6.9 Scale

0

##### 5.16.3.6.10 Is Foreign Key

❌ No

#### 5.16.3.7.0 notes

##### 5.16.3.7.1 Name

notes

##### 5.16.3.7.2 Type

🔹 TEXT

##### 5.16.3.7.3 Is Required

❌ No

##### 5.16.3.7.4 Is Primary Key

❌ No

##### 5.16.3.7.5 Size

0

##### 5.16.3.7.6 Is Unique

❌ No

##### 5.16.3.7.7 Constraints

*No items available*

##### 5.16.3.7.8 Precision

0

##### 5.16.3.7.9 Scale

0

##### 5.16.3.7.10 Is Foreign Key

❌ No

### 5.16.4.0.0 Primary Keys

- id

### 5.16.5.0.0 Unique Constraints

*No items available*

### 5.16.6.0.0 Indexes

- {'name': 'idx_tms_trip_event_log_trip_timestamp', 'columns': ['trip_id', 'event_timestamp'], 'type': 'BTree'}

## 5.17.0.0.0 tms_audit_log

### 5.17.1.0.0 Name

tms_audit_log

### 5.17.2.0.0 Description

Provides an immutable audit trail for all significant data changes in the system. REQ-1-207.

### 5.17.3.0.0 Attributes

#### 5.17.3.1.0 id

##### 5.17.3.1.1 Name

id

##### 5.17.3.1.2 Type

🔹 INT

##### 5.17.3.1.3 Is Required

✅ Yes

##### 5.17.3.1.4 Is Primary Key

✅ Yes

##### 5.17.3.1.5 Size

0

##### 5.17.3.1.6 Is Unique

✅ Yes

##### 5.17.3.1.7 Constraints

*No items available*

##### 5.17.3.1.8 Precision

0

##### 5.17.3.1.9 Scale

0

##### 5.17.3.1.10 Is Foreign Key

❌ No

#### 5.17.3.2.0 user_id

##### 5.17.3.2.1 Name

user_id

##### 5.17.3.2.2 Type

🔹 INT

##### 5.17.3.2.3 Is Required

✅ Yes

##### 5.17.3.2.4 Is Primary Key

❌ No

##### 5.17.3.2.5 Size

0

##### 5.17.3.2.6 Is Unique

❌ No

##### 5.17.3.2.7 Constraints

*No items available*

##### 5.17.3.2.8 Precision

0

##### 5.17.3.2.9 Scale

0

##### 5.17.3.2.10 Is Foreign Key

✅ Yes

#### 5.17.3.3.0 timestamp

##### 5.17.3.3.1 Name

timestamp

##### 5.17.3.3.2 Type

🔹 DateTime

##### 5.17.3.3.3 Is Required

✅ Yes

##### 5.17.3.3.4 Is Primary Key

❌ No

##### 5.17.3.3.5 Size

0

##### 5.17.3.3.6 Is Unique

❌ No

##### 5.17.3.3.7 Constraints

*No items available*

##### 5.17.3.3.8 Precision

0

##### 5.17.3.3.9 Scale

0

##### 5.17.3.3.10 Is Foreign Key

❌ No

#### 5.17.3.4.0 action_type

##### 5.17.3.4.1 Name

action_type

##### 5.17.3.4.2 Type

🔹 VARCHAR

##### 5.17.3.4.3 Is Required

✅ Yes

##### 5.17.3.4.4 Is Primary Key

❌ No

##### 5.17.3.4.5 Size

20

##### 5.17.3.4.6 Is Unique

❌ No

##### 5.17.3.4.7 Constraints

- ENUM('Create', 'Update', 'Delete')

##### 5.17.3.4.8 Precision

0

##### 5.17.3.4.9 Scale

0

##### 5.17.3.4.10 Is Foreign Key

❌ No

#### 5.17.3.5.0 model_name

##### 5.17.3.5.1 Name

model_name

##### 5.17.3.5.2 Type

🔹 VARCHAR

##### 5.17.3.5.3 Is Required

✅ Yes

##### 5.17.3.5.4 Is Primary Key

❌ No

##### 5.17.3.5.5 Size

100

##### 5.17.3.5.6 Is Unique

❌ No

##### 5.17.3.5.7 Constraints

*No items available*

##### 5.17.3.5.8 Precision

0

##### 5.17.3.5.9 Scale

0

##### 5.17.3.5.10 Is Foreign Key

❌ No

#### 5.17.3.6.0 record_id

##### 5.17.3.6.1 Name

record_id

##### 5.17.3.6.2 Type

🔹 INT

##### 5.17.3.6.3 Is Required

✅ Yes

##### 5.17.3.6.4 Is Primary Key

❌ No

##### 5.17.3.6.5 Size

0

##### 5.17.3.6.6 Is Unique

❌ No

##### 5.17.3.6.7 Constraints

*No items available*

##### 5.17.3.6.8 Precision

0

##### 5.17.3.6.9 Scale

0

##### 5.17.3.6.10 Is Foreign Key

❌ No

#### 5.17.3.7.0 changes

##### 5.17.3.7.1 Name

changes

##### 5.17.3.7.2 Type

🔹 JSON

##### 5.17.3.7.3 Is Required

❌ No

##### 5.17.3.7.4 Is Primary Key

❌ No

##### 5.17.3.7.5 Size

0

##### 5.17.3.7.6 Is Unique

❌ No

##### 5.17.3.7.7 Constraints

*No items available*

##### 5.17.3.7.8 Precision

0

##### 5.17.3.7.9 Scale

0

##### 5.17.3.7.10 Is Foreign Key

❌ No

### 5.17.4.0.0 Primary Keys

- id

### 5.17.5.0.0 Unique Constraints

*No items available*

### 5.17.6.0.0 Indexes

- {'name': 'idx_tms_audit_log_record_timestamp', 'columns': ['model_name', 'record_id', 'timestamp'], 'type': 'BTree'}


# 1 Entities

## 1.1 User

### 1.1.1 Name

User

### 1.1.2 Description

Represents system users, leveraging Odoo's 'res.users' model. Manages authentication and role assignments. REQ-1-008.

### 1.1.3 Attributes

#### 1.1.3.1 userId

##### 1.1.3.1.1 Name

userId

##### 1.1.3.1.2 Type

🔹 Guid

##### 1.1.3.1.3 Is Required

✅ Yes

##### 1.1.3.1.4 Is Primary Key

✅ Yes

##### 1.1.3.1.5 Is Unique

✅ Yes

##### 1.1.3.1.6 Index Type

UniqueIndex

##### 1.1.3.1.7 Size

0

##### 1.1.3.1.8 Constraints

*No items available*

##### 1.1.3.1.9 Default Value



##### 1.1.3.1.10 Is Foreign Key

❌ No

##### 1.1.3.1.11 Precision

0

##### 1.1.3.1.12 Scale

0

#### 1.1.3.2.0 name

##### 1.1.3.2.1 Name

name

##### 1.1.3.2.2 Type

🔹 VARCHAR

##### 1.1.3.2.3 Is Required

✅ Yes

##### 1.1.3.2.4 Is Primary Key

❌ No

##### 1.1.3.2.5 Is Unique

❌ No

##### 1.1.3.2.6 Index Type

Index

##### 1.1.3.2.7 Size

255

##### 1.1.3.2.8 Constraints

*No items available*

##### 1.1.3.2.9 Default Value



##### 1.1.3.2.10 Is Foreign Key

❌ No

##### 1.1.3.2.11 Precision

0

##### 1.1.3.2.12 Scale

0

#### 1.1.3.3.0 email

##### 1.1.3.3.1 Name

email

##### 1.1.3.3.2 Type

🔹 VARCHAR

##### 1.1.3.3.3 Is Required

✅ Yes

##### 1.1.3.3.4 Is Primary Key

❌ No

##### 1.1.3.3.5 Is Unique

✅ Yes

##### 1.1.3.3.6 Index Type

UniqueIndex

##### 1.1.3.3.7 Size

255

##### 1.1.3.3.8 Constraints

- EMAIL_FORMAT

##### 1.1.3.3.9 Default Value



##### 1.1.3.3.10 Is Foreign Key

❌ No

##### 1.1.3.3.11 Precision

0

##### 1.1.3.3.12 Scale

0

#### 1.1.3.4.0 passwordHash

##### 1.1.3.4.1 Name

passwordHash

##### 1.1.3.4.2 Type

🔹 VARCHAR

##### 1.1.3.4.3 Is Required

✅ Yes

##### 1.1.3.4.4 Is Primary Key

❌ No

##### 1.1.3.4.5 Is Unique

❌ No

##### 1.1.3.4.6 Index Type

None

##### 1.1.3.4.7 Size

255

##### 1.1.3.4.8 Constraints

*No items available*

##### 1.1.3.4.9 Default Value



##### 1.1.3.4.10 Is Foreign Key

❌ No

##### 1.1.3.4.11 Precision

0

##### 1.1.3.4.12 Scale

0

#### 1.1.3.5.0 roleId

##### 1.1.3.5.1 Name

roleId

##### 1.1.3.5.2 Type

🔹 Guid

##### 1.1.3.5.3 Is Required

✅ Yes

##### 1.1.3.5.4 Is Primary Key

❌ No

##### 1.1.3.5.5 Is Unique

❌ No

##### 1.1.3.5.6 Index Type

Index

##### 1.1.3.5.7 Size

0

##### 1.1.3.5.8 Constraints

*No items available*

##### 1.1.3.5.9 Default Value



##### 1.1.3.5.10 Is Foreign Key

✅ Yes

##### 1.1.3.5.11 Precision

0

##### 1.1.3.5.12 Scale

0

#### 1.1.3.6.0 isActive

##### 1.1.3.6.1 Name

isActive

##### 1.1.3.6.2 Type

🔹 BOOLEAN

##### 1.1.3.6.3 Is Required

✅ Yes

##### 1.1.3.6.4 Is Primary Key

❌ No

##### 1.1.3.6.5 Is Unique

❌ No

##### 1.1.3.6.6 Index Type

Index

##### 1.1.3.6.7 Size

0

##### 1.1.3.6.8 Constraints

*No items available*

##### 1.1.3.6.9 Default Value

true

##### 1.1.3.6.10 Is Foreign Key

❌ No

##### 1.1.3.6.11 Precision

0

##### 1.1.3.6.12 Scale

0

#### 1.1.3.7.0 createdAt

##### 1.1.3.7.1 Name

createdAt

##### 1.1.3.7.2 Type

🔹 DateTime

##### 1.1.3.7.3 Is Required

✅ Yes

##### 1.1.3.7.4 Is Primary Key

❌ No

##### 1.1.3.7.5 Is Unique

❌ No

##### 1.1.3.7.6 Index Type

Index

##### 1.1.3.7.7 Size

0

##### 1.1.3.7.8 Constraints

*No items available*

##### 1.1.3.7.9 Default Value

CURRENT_TIMESTAMP

##### 1.1.3.7.10 Is Foreign Key

❌ No

##### 1.1.3.7.11 Precision

0

##### 1.1.3.7.12 Scale

0

#### 1.1.3.8.0 updatedAt

##### 1.1.3.8.1 Name

updatedAt

##### 1.1.3.8.2 Type

🔹 DateTime

##### 1.1.3.8.3 Is Required

✅ Yes

##### 1.1.3.8.4 Is Primary Key

❌ No

##### 1.1.3.8.5 Is Unique

❌ No

##### 1.1.3.8.6 Index Type

None

##### 1.1.3.8.7 Size

0

##### 1.1.3.8.8 Constraints

*No items available*

##### 1.1.3.8.9 Default Value

CURRENT_TIMESTAMP

##### 1.1.3.8.10 Is Foreign Key

❌ No

##### 1.1.3.8.11 Precision

0

##### 1.1.3.8.12 Scale

0

### 1.1.4.0.0 Primary Keys

- userId

### 1.1.5.0.0 Unique Constraints

- {'name': 'UC_User_Email', 'columns': ['email']}

### 1.1.6.0.0 Indexes

#### 1.1.6.1.0 IX_User_RoleId

##### 1.1.6.1.1 Name

IX_User_RoleId

##### 1.1.6.1.2 Columns

- roleId

##### 1.1.6.1.3 Type

🔹 BTree

#### 1.1.6.2.0 IX_User_IsActive

##### 1.1.6.2.1 Name

IX_User_IsActive

##### 1.1.6.2.2 Columns

- isActive

##### 1.1.6.2.3 Type

🔹 BTree

## 1.2.0.0.0 Role

### 1.2.1.0.0 Name

Role

### 1.2.2.0.0 Description

Represents user roles (e.g., Admin, Dispatch Manager), leveraging Odoo's 'res.groups' model for access control. REQ-1-008.

### 1.2.3.0.0 Attributes

#### 1.2.3.1.0 roleId

##### 1.2.3.1.1 Name

roleId

##### 1.2.3.1.2 Type

🔹 Guid

##### 1.2.3.1.3 Is Required

✅ Yes

##### 1.2.3.1.4 Is Primary Key

✅ Yes

##### 1.2.3.1.5 Is Unique

✅ Yes

##### 1.2.3.1.6 Index Type

UniqueIndex

##### 1.2.3.1.7 Size

0

##### 1.2.3.1.8 Constraints

*No items available*

##### 1.2.3.1.9 Default Value



##### 1.2.3.1.10 Is Foreign Key

❌ No

##### 1.2.3.1.11 Precision

0

##### 1.2.3.1.12 Scale

0

#### 1.2.3.2.0 name

##### 1.2.3.2.1 Name

name

##### 1.2.3.2.2 Type

🔹 VARCHAR

##### 1.2.3.2.3 Is Required

✅ Yes

##### 1.2.3.2.4 Is Primary Key

❌ No

##### 1.2.3.2.5 Is Unique

✅ Yes

##### 1.2.3.2.6 Index Type

UniqueIndex

##### 1.2.3.2.7 Size

100

##### 1.2.3.2.8 Constraints

- ENUM('Admin', 'Dispatch Manager', 'Finance Officer', 'Driver')

##### 1.2.3.2.9 Default Value



##### 1.2.3.2.10 Is Foreign Key

❌ No

##### 1.2.3.2.11 Precision

0

##### 1.2.3.2.12 Scale

0

#### 1.2.3.3.0 description

##### 1.2.3.3.1 Name

description

##### 1.2.3.3.2 Type

🔹 TEXT

##### 1.2.3.3.3 Is Required

❌ No

##### 1.2.3.3.4 Is Primary Key

❌ No

##### 1.2.3.3.5 Is Unique

❌ No

##### 1.2.3.3.6 Index Type

None

##### 1.2.3.3.7 Size

0

##### 1.2.3.3.8 Constraints

*No items available*

##### 1.2.3.3.9 Default Value



##### 1.2.3.3.10 Is Foreign Key

❌ No

##### 1.2.3.3.11 Precision

0

##### 1.2.3.3.12 Scale

0

### 1.2.4.0.0 Primary Keys

- roleId

### 1.2.5.0.0 Unique Constraints

- {'name': 'UC_Role_Name', 'columns': ['name']}

### 1.2.6.0.0 Indexes

*No items available*

## 1.3.0.0.0 Customer

### 1.3.1.0.0 Name

Customer

### 1.3.2.0.0 Description

Represents a customer, extending Odoo's 'res.partner' model with TMS-specific attributes. REQ-1-003, REQ-1-012, REQ-1-205.

### 1.3.3.0.0 Attributes

#### 1.3.3.1.0 customerId

##### 1.3.3.1.1 Name

customerId

##### 1.3.3.1.2 Type

🔹 Guid

##### 1.3.3.1.3 Is Required

✅ Yes

##### 1.3.3.1.4 Is Primary Key

✅ Yes

##### 1.3.3.1.5 Is Unique

✅ Yes

##### 1.3.3.1.6 Index Type

UniqueIndex

##### 1.3.3.1.7 Size

0

##### 1.3.3.1.8 Constraints

*No items available*

##### 1.3.3.1.9 Default Value



##### 1.3.3.1.10 Is Foreign Key

❌ No

##### 1.3.3.1.11 Precision

0

##### 1.3.3.1.12 Scale

0

#### 1.3.3.2.0 name

##### 1.3.3.2.1 Name

name

##### 1.3.3.2.2 Type

🔹 VARCHAR

##### 1.3.3.2.3 Is Required

✅ Yes

##### 1.3.3.2.4 Is Primary Key

❌ No

##### 1.3.3.2.5 Is Unique

❌ No

##### 1.3.3.2.6 Index Type

Index

##### 1.3.3.2.7 Size

255

##### 1.3.3.2.8 Constraints

*No items available*

##### 1.3.3.2.9 Default Value



##### 1.3.3.2.10 Is Foreign Key

❌ No

##### 1.3.3.2.11 Precision

0

##### 1.3.3.2.12 Scale

0

#### 1.3.3.3.0 billingAddress

##### 1.3.3.3.1 Name

billingAddress

##### 1.3.3.3.2 Type

🔹 TEXT

##### 1.3.3.3.3 Is Required

✅ Yes

##### 1.3.3.3.4 Is Primary Key

❌ No

##### 1.3.3.3.5 Is Unique

❌ No

##### 1.3.3.3.6 Index Type

None

##### 1.3.3.3.7 Size

0

##### 1.3.3.3.8 Constraints

*No items available*

##### 1.3.3.3.9 Default Value



##### 1.3.3.3.10 Is Foreign Key

❌ No

##### 1.3.3.3.11 Precision

0

##### 1.3.3.3.12 Scale

0

#### 1.3.3.4.0 gstin

##### 1.3.3.4.1 Name

gstin

##### 1.3.3.4.2 Type

🔹 VARCHAR

##### 1.3.3.4.3 Is Required

❌ No

##### 1.3.3.4.4 Is Primary Key

❌ No

##### 1.3.3.4.5 Is Unique

✅ Yes

##### 1.3.3.4.6 Index Type

UniqueIndex

##### 1.3.3.4.7 Size

15

##### 1.3.3.4.8 Constraints

- GSTIN_FORMAT_VALIDATION

##### 1.3.3.4.9 Default Value



##### 1.3.3.4.10 Is Foreign Key

❌ No

##### 1.3.3.4.11 Precision

0

##### 1.3.3.4.12 Scale

0

#### 1.3.3.5.0 contactPerson

##### 1.3.3.5.1 Name

contactPerson

##### 1.3.3.5.2 Type

🔹 VARCHAR

##### 1.3.3.5.3 Is Required

❌ No

##### 1.3.3.5.4 Is Primary Key

❌ No

##### 1.3.3.5.5 Is Unique

❌ No

##### 1.3.3.5.6 Index Type

None

##### 1.3.3.5.7 Size

255

##### 1.3.3.5.8 Constraints

*No items available*

##### 1.3.3.5.9 Default Value



##### 1.3.3.5.10 Is Foreign Key

❌ No

##### 1.3.3.5.11 Precision

0

##### 1.3.3.5.12 Scale

0

#### 1.3.3.6.0 isActive

##### 1.3.3.6.1 Name

isActive

##### 1.3.3.6.2 Type

🔹 BOOLEAN

##### 1.3.3.6.3 Is Required

✅ Yes

##### 1.3.3.6.4 Is Primary Key

❌ No

##### 1.3.3.6.5 Is Unique

❌ No

##### 1.3.3.6.6 Index Type

Index

##### 1.3.3.6.7 Size

0

##### 1.3.3.6.8 Constraints

*No items available*

##### 1.3.3.6.9 Default Value

true

##### 1.3.3.6.10 Is Foreign Key

❌ No

##### 1.3.3.6.11 Precision

0

##### 1.3.3.6.12 Scale

0

#### 1.3.3.7.0 createdAt

##### 1.3.3.7.1 Name

createdAt

##### 1.3.3.7.2 Type

🔹 DateTime

##### 1.3.3.7.3 Is Required

✅ Yes

##### 1.3.3.7.4 Is Primary Key

❌ No

##### 1.3.3.7.5 Is Unique

❌ No

##### 1.3.3.7.6 Index Type

Index

##### 1.3.3.7.7 Size

0

##### 1.3.3.7.8 Constraints

*No items available*

##### 1.3.3.7.9 Default Value

CURRENT_TIMESTAMP

##### 1.3.3.7.10 Is Foreign Key

❌ No

##### 1.3.3.7.11 Precision

0

##### 1.3.3.7.12 Scale

0

#### 1.3.3.8.0 updatedAt

##### 1.3.3.8.1 Name

updatedAt

##### 1.3.3.8.2 Type

🔹 DateTime

##### 1.3.3.8.3 Is Required

✅ Yes

##### 1.3.3.8.4 Is Primary Key

❌ No

##### 1.3.3.8.5 Is Unique

❌ No

##### 1.3.3.8.6 Index Type

None

##### 1.3.3.8.7 Size

0

##### 1.3.3.8.8 Constraints

*No items available*

##### 1.3.3.8.9 Default Value

CURRENT_TIMESTAMP

##### 1.3.3.8.10 Is Foreign Key

❌ No

##### 1.3.3.8.11 Precision

0

##### 1.3.3.8.12 Scale

0

### 1.3.4.0.0 Primary Keys

- customerId

### 1.3.5.0.0 Unique Constraints

- {'name': 'UC_Customer_Gstin', 'columns': ['gstin']}

### 1.3.6.0.0 Indexes

#### 1.3.6.1.0 IX_Customer_Name

##### 1.3.6.1.1 Name

IX_Customer_Name

##### 1.3.6.1.2 Columns

- name

##### 1.3.6.1.3 Type

🔹 BTree

#### 1.3.6.2.0 IX_Customer_IsActive

##### 1.3.6.2.1 Name

IX_Customer_IsActive

##### 1.3.6.2.2 Columns

- isActive

##### 1.3.6.2.3 Type

🔹 BTree

## 1.4.0.0.0 Driver

### 1.4.1.0.0 Name

Driver

### 1.4.2.0.0 Description

Represents a driver, extending Odoo's 'hr.employee' model with TMS-specific attributes like license details. REQ-1-003, REQ-1-012, REQ-1-203.

### 1.4.3.0.0 Attributes

#### 1.4.3.1.0 driverId

##### 1.4.3.1.1 Name

driverId

##### 1.4.3.1.2 Type

🔹 Guid

##### 1.4.3.1.3 Is Required

✅ Yes

##### 1.4.3.1.4 Is Primary Key

✅ Yes

##### 1.4.3.1.5 Is Unique

✅ Yes

##### 1.4.3.1.6 Index Type

UniqueIndex

##### 1.4.3.1.7 Size

0

##### 1.4.3.1.8 Constraints

*No items available*

##### 1.4.3.1.9 Default Value



##### 1.4.3.1.10 Is Foreign Key

❌ No

##### 1.4.3.1.11 Precision

0

##### 1.4.3.1.12 Scale

0

#### 1.4.3.2.0 name

##### 1.4.3.2.1 Name

name

##### 1.4.3.2.2 Type

🔹 VARCHAR

##### 1.4.3.2.3 Is Required

✅ Yes

##### 1.4.3.2.4 Is Primary Key

❌ No

##### 1.4.3.2.5 Is Unique

❌ No

##### 1.4.3.2.6 Index Type

Index

##### 1.4.3.2.7 Size

255

##### 1.4.3.2.8 Constraints

*No items available*

##### 1.4.3.2.9 Default Value



##### 1.4.3.2.10 Is Foreign Key

❌ No

##### 1.4.3.2.11 Precision

0

##### 1.4.3.2.12 Scale

0

#### 1.4.3.3.0 contactNumber

##### 1.4.3.3.1 Name

contactNumber

##### 1.4.3.3.2 Type

🔹 VARCHAR

##### 1.4.3.3.3 Is Required

❌ No

##### 1.4.3.3.4 Is Primary Key

❌ No

##### 1.4.3.3.5 Is Unique

❌ No

##### 1.4.3.3.6 Index Type

Index

##### 1.4.3.3.7 Size

20

##### 1.4.3.3.8 Constraints

*No items available*

##### 1.4.3.3.9 Default Value



##### 1.4.3.3.10 Is Foreign Key

❌ No

##### 1.4.3.3.11 Precision

0

##### 1.4.3.3.12 Scale

0

#### 1.4.3.4.0 licenseNumber

##### 1.4.3.4.1 Name

licenseNumber

##### 1.4.3.4.2 Type

🔹 VARCHAR

##### 1.4.3.4.3 Is Required

✅ Yes

##### 1.4.3.4.4 Is Primary Key

❌ No

##### 1.4.3.4.5 Is Unique

✅ Yes

##### 1.4.3.4.6 Index Type

UniqueIndex

##### 1.4.3.4.7 Size

50

##### 1.4.3.4.8 Constraints

*No items available*

##### 1.4.3.4.9 Default Value



##### 1.4.3.4.10 Is Foreign Key

❌ No

##### 1.4.3.4.11 Precision

0

##### 1.4.3.4.12 Scale

0

#### 1.4.3.5.0 licenseExpiryDate

##### 1.4.3.5.1 Name

licenseExpiryDate

##### 1.4.3.5.2 Type

🔹 Date

##### 1.4.3.5.3 Is Required

✅ Yes

##### 1.4.3.5.4 Is Primary Key

❌ No

##### 1.4.3.5.5 Is Unique

❌ No

##### 1.4.3.5.6 Index Type

Index

##### 1.4.3.5.7 Size

0

##### 1.4.3.5.8 Constraints

*No items available*

##### 1.4.3.5.9 Default Value



##### 1.4.3.5.10 Is Foreign Key

❌ No

##### 1.4.3.5.11 Precision

0

##### 1.4.3.5.12 Scale

0

#### 1.4.3.6.0 isActive

##### 1.4.3.6.1 Name

isActive

##### 1.4.3.6.2 Type

🔹 BOOLEAN

##### 1.4.3.6.3 Is Required

✅ Yes

##### 1.4.3.6.4 Is Primary Key

❌ No

##### 1.4.3.6.5 Is Unique

❌ No

##### 1.4.3.6.6 Index Type

Index

##### 1.4.3.6.7 Size

0

##### 1.4.3.6.8 Constraints

*No items available*

##### 1.4.3.6.9 Default Value

true

##### 1.4.3.6.10 Is Foreign Key

❌ No

##### 1.4.3.6.11 Precision

0

##### 1.4.3.6.12 Scale

0

#### 1.4.3.7.0 createdAt

##### 1.4.3.7.1 Name

createdAt

##### 1.4.3.7.2 Type

🔹 DateTime

##### 1.4.3.7.3 Is Required

✅ Yes

##### 1.4.3.7.4 Is Primary Key

❌ No

##### 1.4.3.7.5 Is Unique

❌ No

##### 1.4.3.7.6 Index Type

Index

##### 1.4.3.7.7 Size

0

##### 1.4.3.7.8 Constraints

*No items available*

##### 1.4.3.7.9 Default Value

CURRENT_TIMESTAMP

##### 1.4.3.7.10 Is Foreign Key

❌ No

##### 1.4.3.7.11 Precision

0

##### 1.4.3.7.12 Scale

0

#### 1.4.3.8.0 updatedAt

##### 1.4.3.8.1 Name

updatedAt

##### 1.4.3.8.2 Type

🔹 DateTime

##### 1.4.3.8.3 Is Required

✅ Yes

##### 1.4.3.8.4 Is Primary Key

❌ No

##### 1.4.3.8.5 Is Unique

❌ No

##### 1.4.3.8.6 Index Type

None

##### 1.4.3.8.7 Size

0

##### 1.4.3.8.8 Constraints

*No items available*

##### 1.4.3.8.9 Default Value

CURRENT_TIMESTAMP

##### 1.4.3.8.10 Is Foreign Key

❌ No

##### 1.4.3.8.11 Precision

0

##### 1.4.3.8.12 Scale

0

### 1.4.4.0.0 Primary Keys

- driverId

### 1.4.5.0.0 Unique Constraints

- {'name': 'UC_Driver_LicenseNumber', 'columns': ['licenseNumber']}

### 1.4.6.0.0 Indexes

#### 1.4.6.1.0 IX_Driver_IsActive

##### 1.4.6.1.1 Name

IX_Driver_IsActive

##### 1.4.6.1.2 Columns

- isActive

##### 1.4.6.1.3 Type

🔹 BTree

#### 1.4.6.2.0 IX_Driver_LicenseExpiryDate

##### 1.4.6.2.1 Name

IX_Driver_LicenseExpiryDate

##### 1.4.6.2.2 Columns

- licenseExpiryDate

##### 1.4.6.2.3 Type

🔹 BTree

## 1.5.0.0.0 Vehicle

### 1.5.1.0.0 Name

Vehicle

### 1.5.2.0.0 Description

Represents a vehicle (truck) used for transport. REQ-1-200, REQ-1-202, REQ-1-900.

### 1.5.3.0.0 Attributes

#### 1.5.3.1.0 vehicleId

##### 1.5.3.1.1 Name

vehicleId

##### 1.5.3.1.2 Type

🔹 Guid

##### 1.5.3.1.3 Is Required

✅ Yes

##### 1.5.3.1.4 Is Primary Key

✅ Yes

##### 1.5.3.1.5 Is Unique

✅ Yes

##### 1.5.3.1.6 Index Type

UniqueIndex

##### 1.5.3.1.7 Size

0

##### 1.5.3.1.8 Constraints

*No items available*

##### 1.5.3.1.9 Default Value



##### 1.5.3.1.10 Is Foreign Key

❌ No

##### 1.5.3.1.11 Precision

0

##### 1.5.3.1.12 Scale

0

#### 1.5.3.2.0 truckNumber

##### 1.5.3.2.1 Name

truckNumber

##### 1.5.3.2.2 Type

🔹 VARCHAR

##### 1.5.3.2.3 Is Required

✅ Yes

##### 1.5.3.2.4 Is Primary Key

❌ No

##### 1.5.3.2.5 Is Unique

✅ Yes

##### 1.5.3.2.6 Index Type

UniqueIndex

##### 1.5.3.2.7 Size

20

##### 1.5.3.2.8 Constraints

- UNIQUE

##### 1.5.3.2.9 Default Value



##### 1.5.3.2.10 Is Foreign Key

❌ No

##### 1.5.3.2.11 Precision

0

##### 1.5.3.2.12 Scale

0

#### 1.5.3.3.0 model

##### 1.5.3.3.1 Name

model

##### 1.5.3.3.2 Type

🔹 VARCHAR

##### 1.5.3.3.3 Is Required

❌ No

##### 1.5.3.3.4 Is Primary Key

❌ No

##### 1.5.3.3.5 Is Unique

❌ No

##### 1.5.3.3.6 Index Type

None

##### 1.5.3.3.7 Size

100

##### 1.5.3.3.8 Constraints

*No items available*

##### 1.5.3.3.9 Default Value



##### 1.5.3.3.10 Is Foreign Key

❌ No

##### 1.5.3.3.11 Precision

0

##### 1.5.3.3.12 Scale

0

#### 1.5.3.4.0 capacityTons

##### 1.5.3.4.1 Name

capacityTons

##### 1.5.3.4.2 Type

🔹 DECIMAL

##### 1.5.3.4.3 Is Required

✅ Yes

##### 1.5.3.4.4 Is Primary Key

❌ No

##### 1.5.3.4.5 Is Unique

❌ No

##### 1.5.3.4.6 Index Type

None

##### 1.5.3.4.7 Size

0

##### 1.5.3.4.8 Constraints

- POSITIVE_VALUE

##### 1.5.3.4.9 Default Value

0

##### 1.5.3.4.10 Is Foreign Key

❌ No

##### 1.5.3.4.11 Precision

10

##### 1.5.3.4.12 Scale

2

#### 1.5.3.5.0 ownerDetails

##### 1.5.3.5.1 Name

ownerDetails

##### 1.5.3.5.2 Type

🔹 TEXT

##### 1.5.3.5.3 Is Required

❌ No

##### 1.5.3.5.4 Is Primary Key

❌ No

##### 1.5.3.5.5 Is Unique

❌ No

##### 1.5.3.5.6 Index Type

None

##### 1.5.3.5.7 Size

0

##### 1.5.3.5.8 Constraints

*No items available*

##### 1.5.3.5.9 Default Value



##### 1.5.3.5.10 Is Foreign Key

❌ No

##### 1.5.3.5.11 Precision

0

##### 1.5.3.5.12 Scale

0

#### 1.5.3.6.0 ownershipType

##### 1.5.3.6.1 Name

ownershipType

##### 1.5.3.6.2 Type

🔹 VARCHAR

##### 1.5.3.6.3 Is Required

✅ Yes

##### 1.5.3.6.4 Is Primary Key

❌ No

##### 1.5.3.6.5 Is Unique

❌ No

##### 1.5.3.6.6 Index Type

Index

##### 1.5.3.6.7 Size

20

##### 1.5.3.6.8 Constraints

- ENUM('Company-Owned', 'Outsourced')

##### 1.5.3.6.9 Default Value

'Company-Owned'

##### 1.5.3.6.10 Is Foreign Key

❌ No

##### 1.5.3.6.11 Precision

0

##### 1.5.3.6.12 Scale

0

#### 1.5.3.7.0 fuelType

##### 1.5.3.7.1 Name

fuelType

##### 1.5.3.7.2 Type

🔹 VARCHAR

##### 1.5.3.7.3 Is Required

❌ No

##### 1.5.3.7.4 Is Primary Key

❌ No

##### 1.5.3.7.5 Is Unique

❌ No

##### 1.5.3.7.6 Index Type

None

##### 1.5.3.7.7 Size

20

##### 1.5.3.7.8 Constraints

*No items available*

##### 1.5.3.7.9 Default Value



##### 1.5.3.7.10 Is Foreign Key

❌ No

##### 1.5.3.7.11 Precision

0

##### 1.5.3.7.12 Scale

0

#### 1.5.3.8.0 lastServiceDate

##### 1.5.3.8.1 Name

lastServiceDate

##### 1.5.3.8.2 Type

🔹 Date

##### 1.5.3.8.3 Is Required

❌ No

##### 1.5.3.8.4 Is Primary Key

❌ No

##### 1.5.3.8.5 Is Unique

❌ No

##### 1.5.3.8.6 Index Type

None

##### 1.5.3.8.7 Size

0

##### 1.5.3.8.8 Constraints

*No items available*

##### 1.5.3.8.9 Default Value



##### 1.5.3.8.10 Is Foreign Key

❌ No

##### 1.5.3.8.11 Precision

0

##### 1.5.3.8.12 Scale

0

#### 1.5.3.9.0 nextServiceDueDate

##### 1.5.3.9.1 Name

nextServiceDueDate

##### 1.5.3.9.2 Type

🔹 Date

##### 1.5.3.9.3 Is Required

❌ No

##### 1.5.3.9.4 Is Primary Key

❌ No

##### 1.5.3.9.5 Is Unique

❌ No

##### 1.5.3.9.6 Index Type

Index

##### 1.5.3.9.7 Size

0

##### 1.5.3.9.8 Constraints

*No items available*

##### 1.5.3.9.9 Default Value



##### 1.5.3.9.10 Is Foreign Key

❌ No

##### 1.5.3.9.11 Precision

0

##### 1.5.3.9.12 Scale

0

#### 1.5.3.10.0 status

##### 1.5.3.10.1 Name

status

##### 1.5.3.10.2 Type

🔹 VARCHAR

##### 1.5.3.10.3 Is Required

✅ Yes

##### 1.5.3.10.4 Is Primary Key

❌ No

##### 1.5.3.10.5 Is Unique

❌ No

##### 1.5.3.10.6 Index Type

Index

##### 1.5.3.10.7 Size

20

##### 1.5.3.10.8 Constraints

- ENUM('Active', 'Inactive', 'In-Maintenance')

##### 1.5.3.10.9 Default Value

'Active'

##### 1.5.3.10.10 Is Foreign Key

❌ No

##### 1.5.3.10.11 Precision

0

##### 1.5.3.10.12 Scale

0

#### 1.5.3.11.0 lastOdometerReading

##### 1.5.3.11.1 Name

lastOdometerReading

##### 1.5.3.11.2 Type

🔹 INT

##### 1.5.3.11.3 Is Required

❌ No

##### 1.5.3.11.4 Is Primary Key

❌ No

##### 1.5.3.11.5 Is Unique

❌ No

##### 1.5.3.11.6 Index Type

None

##### 1.5.3.11.7 Size

0

##### 1.5.3.11.8 Constraints

- NON_NEGATIVE

##### 1.5.3.11.9 Default Value

0

##### 1.5.3.11.10 Is Foreign Key

❌ No

##### 1.5.3.11.11 Precision

0

##### 1.5.3.11.12 Scale

0

#### 1.5.3.12.0 lastLatitude

##### 1.5.3.12.1 Name

lastLatitude

##### 1.5.3.12.2 Type

🔹 DECIMAL

##### 1.5.3.12.3 Is Required

❌ No

##### 1.5.3.12.4 Is Primary Key

❌ No

##### 1.5.3.12.5 Is Unique

❌ No

##### 1.5.3.12.6 Index Type

None

##### 1.5.3.12.7 Size

0

##### 1.5.3.12.8 Constraints

*No items available*

##### 1.5.3.12.9 Default Value

*Not specified*

##### 1.5.3.12.10 Is Foreign Key

❌ No

##### 1.5.3.12.11 Precision

9

##### 1.5.3.12.12 Scale

6

#### 1.5.3.13.0 lastLongitude

##### 1.5.3.13.1 Name

lastLongitude

##### 1.5.3.13.2 Type

🔹 DECIMAL

##### 1.5.3.13.3 Is Required

❌ No

##### 1.5.3.13.4 Is Primary Key

❌ No

##### 1.5.3.13.5 Is Unique

❌ No

##### 1.5.3.13.6 Index Type

None

##### 1.5.3.13.7 Size

0

##### 1.5.3.13.8 Constraints

*No items available*

##### 1.5.3.13.9 Default Value

*Not specified*

##### 1.5.3.13.10 Is Foreign Key

❌ No

##### 1.5.3.13.11 Precision

9

##### 1.5.3.13.12 Scale

6

#### 1.5.3.14.0 lastLocationTimestamp

##### 1.5.3.14.1 Name

lastLocationTimestamp

##### 1.5.3.14.2 Type

🔹 DateTime

##### 1.5.3.14.3 Is Required

❌ No

##### 1.5.3.14.4 Is Primary Key

❌ No

##### 1.5.3.14.5 Is Unique

❌ No

##### 1.5.3.14.6 Index Type

None

##### 1.5.3.14.7 Size

0

##### 1.5.3.14.8 Constraints

*No items available*

##### 1.5.3.14.9 Default Value

*Not specified*

##### 1.5.3.14.10 Is Foreign Key

❌ No

##### 1.5.3.14.11 Precision

0

##### 1.5.3.14.12 Scale

0

#### 1.5.3.15.0 createdAt

##### 1.5.3.15.1 Name

createdAt

##### 1.5.3.15.2 Type

🔹 DateTime

##### 1.5.3.15.3 Is Required

✅ Yes

##### 1.5.3.15.4 Is Primary Key

❌ No

##### 1.5.3.15.5 Is Unique

❌ No

##### 1.5.3.15.6 Index Type

Index

##### 1.5.3.15.7 Size

0

##### 1.5.3.15.8 Constraints

*No items available*

##### 1.5.3.15.9 Default Value

CURRENT_TIMESTAMP

##### 1.5.3.15.10 Is Foreign Key

❌ No

##### 1.5.3.15.11 Precision

0

##### 1.5.3.15.12 Scale

0

#### 1.5.3.16.0 updatedAt

##### 1.5.3.16.1 Name

updatedAt

##### 1.5.3.16.2 Type

🔹 DateTime

##### 1.5.3.16.3 Is Required

✅ Yes

##### 1.5.3.16.4 Is Primary Key

❌ No

##### 1.5.3.16.5 Is Unique

❌ No

##### 1.5.3.16.6 Index Type

None

##### 1.5.3.16.7 Size

0

##### 1.5.3.16.8 Constraints

*No items available*

##### 1.5.3.16.9 Default Value

CURRENT_TIMESTAMP

##### 1.5.3.16.10 Is Foreign Key

❌ No

##### 1.5.3.16.11 Precision

0

##### 1.5.3.16.12 Scale

0

### 1.5.4.0.0 Primary Keys

- vehicleId

### 1.5.5.0.0 Unique Constraints

- {'name': 'UC_Vehicle_TruckNumber', 'columns': ['truckNumber']}

### 1.5.6.0.0 Indexes

#### 1.5.6.1.0 IX_Vehicle_Status

##### 1.5.6.1.1 Name

IX_Vehicle_Status

##### 1.5.6.1.2 Columns

- status

##### 1.5.6.1.3 Type

🔹 BTree

#### 1.5.6.2.0 IX_Vehicle_OwnershipType

##### 1.5.6.2.1 Name

IX_Vehicle_OwnershipType

##### 1.5.6.2.2 Columns

- ownershipType

##### 1.5.6.2.3 Type

🔹 BTree

#### 1.5.6.3.0 IX_Vehicle_NextServiceDueDate

##### 1.5.6.3.1 Name

IX_Vehicle_NextServiceDueDate

##### 1.5.6.3.2 Columns

- nextServiceDueDate

##### 1.5.6.3.3 Type

🔹 BTree

## 1.6.0.0.0 VehicleDocument

### 1.6.1.0.0 Name

VehicleDocument

### 1.6.2.0.0 Description

Stores documents associated with a vehicle, such as RC, Insurance, etc., including their expiry dates. REQ-1-201.

### 1.6.3.0.0 Attributes

#### 1.6.3.1.0 vehicleDocumentId

##### 1.6.3.1.1 Name

vehicleDocumentId

##### 1.6.3.1.2 Type

🔹 Guid

##### 1.6.3.1.3 Is Required

✅ Yes

##### 1.6.3.1.4 Is Primary Key

✅ Yes

##### 1.6.3.1.5 Is Unique

✅ Yes

##### 1.6.3.1.6 Index Type

UniqueIndex

##### 1.6.3.1.7 Size

0

##### 1.6.3.1.8 Constraints

*No items available*

##### 1.6.3.1.9 Default Value



##### 1.6.3.1.10 Is Foreign Key

❌ No

##### 1.6.3.1.11 Precision

0

##### 1.6.3.1.12 Scale

0

#### 1.6.3.2.0 vehicleId

##### 1.6.3.2.1 Name

vehicleId

##### 1.6.3.2.2 Type

🔹 Guid

##### 1.6.3.2.3 Is Required

✅ Yes

##### 1.6.3.2.4 Is Primary Key

❌ No

##### 1.6.3.2.5 Is Unique

❌ No

##### 1.6.3.2.6 Index Type

Index

##### 1.6.3.2.7 Size

0

##### 1.6.3.2.8 Constraints

*No items available*

##### 1.6.3.2.9 Default Value



##### 1.6.3.2.10 Is Foreign Key

✅ Yes

##### 1.6.3.2.11 Precision

0

##### 1.6.3.2.12 Scale

0

#### 1.6.3.3.0 documentType

##### 1.6.3.3.1 Name

documentType

##### 1.6.3.3.2 Type

🔹 VARCHAR

##### 1.6.3.3.3 Is Required

✅ Yes

##### 1.6.3.3.4 Is Primary Key

❌ No

##### 1.6.3.3.5 Is Unique

❌ No

##### 1.6.3.3.6 Index Type

None

##### 1.6.3.3.7 Size

50

##### 1.6.3.3.8 Constraints

*No items available*

##### 1.6.3.3.9 Default Value



##### 1.6.3.3.10 Is Foreign Key

❌ No

##### 1.6.3.3.11 Precision

0

##### 1.6.3.3.12 Scale

0

#### 1.6.3.4.0 expiryDate

##### 1.6.3.4.1 Name

expiryDate

##### 1.6.3.4.2 Type

🔹 Date

##### 1.6.3.4.3 Is Required

✅ Yes

##### 1.6.3.4.4 Is Primary Key

❌ No

##### 1.6.3.4.5 Is Unique

❌ No

##### 1.6.3.4.6 Index Type

Index

##### 1.6.3.4.7 Size

0

##### 1.6.3.4.8 Constraints

*No items available*

##### 1.6.3.4.9 Default Value



##### 1.6.3.4.10 Is Foreign Key

❌ No

##### 1.6.3.4.11 Precision

0

##### 1.6.3.4.12 Scale

0

#### 1.6.3.5.0 attachmentUrl

##### 1.6.3.5.1 Name

attachmentUrl

##### 1.6.3.5.2 Type

🔹 VARCHAR

##### 1.6.3.5.3 Is Required

✅ Yes

##### 1.6.3.5.4 Is Primary Key

❌ No

##### 1.6.3.5.5 Is Unique

❌ No

##### 1.6.3.5.6 Index Type

None

##### 1.6.3.5.7 Size

512

##### 1.6.3.5.8 Constraints

*No items available*

##### 1.6.3.5.9 Default Value



##### 1.6.3.5.10 Is Foreign Key

❌ No

##### 1.6.3.5.11 Precision

0

##### 1.6.3.5.12 Scale

0

#### 1.6.3.6.0 createdAt

##### 1.6.3.6.1 Name

createdAt

##### 1.6.3.6.2 Type

🔹 DateTime

##### 1.6.3.6.3 Is Required

✅ Yes

##### 1.6.3.6.4 Is Primary Key

❌ No

##### 1.6.3.6.5 Is Unique

❌ No

##### 1.6.3.6.6 Index Type

Index

##### 1.6.3.6.7 Size

0

##### 1.6.3.6.8 Constraints

*No items available*

##### 1.6.3.6.9 Default Value

CURRENT_TIMESTAMP

##### 1.6.3.6.10 Is Foreign Key

❌ No

##### 1.6.3.6.11 Precision

0

##### 1.6.3.6.12 Scale

0

### 1.6.4.0.0 Primary Keys

- vehicleDocumentId

### 1.6.5.0.0 Unique Constraints

- {'name': 'UC_VehicleDocument_Vehicle_Type', 'columns': ['vehicleId', 'documentType']}

### 1.6.6.0.0 Indexes

- {'name': 'IX_VehicleDocument_ExpiryDate', 'columns': ['expiryDate'], 'type': 'BTree'}

## 1.7.0.0.0 Material

### 1.7.1.0.0 Name

Material

### 1.7.2.0.0 Description

Master data for types of materials being transported. REQ-1-003.

### 1.7.3.0.0 Attributes

#### 1.7.3.1.0 materialId

##### 1.7.3.1.1 Name

materialId

##### 1.7.3.1.2 Type

🔹 Guid

##### 1.7.3.1.3 Is Required

✅ Yes

##### 1.7.3.1.4 Is Primary Key

✅ Yes

##### 1.7.3.1.5 Is Unique

✅ Yes

##### 1.7.3.1.6 Index Type

UniqueIndex

##### 1.7.3.1.7 Size

0

##### 1.7.3.1.8 Constraints

*No items available*

##### 1.7.3.1.9 Default Value



##### 1.7.3.1.10 Is Foreign Key

❌ No

##### 1.7.3.1.11 Precision

0

##### 1.7.3.1.12 Scale

0

#### 1.7.3.2.0 name

##### 1.7.3.2.1 Name

name

##### 1.7.3.2.2 Type

🔹 VARCHAR

##### 1.7.3.2.3 Is Required

✅ Yes

##### 1.7.3.2.4 Is Primary Key

❌ No

##### 1.7.3.2.5 Is Unique

✅ Yes

##### 1.7.3.2.6 Index Type

UniqueIndex

##### 1.7.3.2.7 Size

100

##### 1.7.3.2.8 Constraints

*No items available*

##### 1.7.3.2.9 Default Value



##### 1.7.3.2.10 Is Foreign Key

❌ No

##### 1.7.3.2.11 Precision

0

##### 1.7.3.2.12 Scale

0

#### 1.7.3.3.0 description

##### 1.7.3.3.1 Name

description

##### 1.7.3.3.2 Type

🔹 TEXT

##### 1.7.3.3.3 Is Required

❌ No

##### 1.7.3.3.4 Is Primary Key

❌ No

##### 1.7.3.3.5 Is Unique

❌ No

##### 1.7.3.3.6 Index Type

None

##### 1.7.3.3.7 Size

0

##### 1.7.3.3.8 Constraints

*No items available*

##### 1.7.3.3.9 Default Value



##### 1.7.3.3.10 Is Foreign Key

❌ No

##### 1.7.3.3.11 Precision

0

##### 1.7.3.3.12 Scale

0

#### 1.7.3.4.0 isActive

##### 1.7.3.4.1 Name

isActive

##### 1.7.3.4.2 Type

🔹 BOOLEAN

##### 1.7.3.4.3 Is Required

✅ Yes

##### 1.7.3.4.4 Is Primary Key

❌ No

##### 1.7.3.4.5 Is Unique

❌ No

##### 1.7.3.4.6 Index Type

Index

##### 1.7.3.4.7 Size

0

##### 1.7.3.4.8 Constraints

*No items available*

##### 1.7.3.4.9 Default Value

true

##### 1.7.3.4.10 Is Foreign Key

❌ No

##### 1.7.3.4.11 Precision

0

##### 1.7.3.4.12 Scale

0

### 1.7.4.0.0 Primary Keys

- materialId

### 1.7.5.0.0 Unique Constraints

- {'name': 'UC_Material_Name', 'columns': ['name']}

### 1.7.6.0.0 Indexes

- {'name': 'IX_Material_IsActive', 'columns': ['isActive'], 'type': 'BTree'}

## 1.8.0.0.0 Route

### 1.8.1.0.0 Name

Route

### 1.8.2.0.0 Description

Master data for predefined transport routes. REQ-1-003, REQ-1-206.

### 1.8.3.0.0 Attributes

#### 1.8.3.1.0 routeId

##### 1.8.3.1.1 Name

routeId

##### 1.8.3.1.2 Type

🔹 Guid

##### 1.8.3.1.3 Is Required

✅ Yes

##### 1.8.3.1.4 Is Primary Key

✅ Yes

##### 1.8.3.1.5 Is Unique

✅ Yes

##### 1.8.3.1.6 Index Type

UniqueIndex

##### 1.8.3.1.7 Size

0

##### 1.8.3.1.8 Constraints

*No items available*

##### 1.8.3.1.9 Default Value



##### 1.8.3.1.10 Is Foreign Key

❌ No

##### 1.8.3.1.11 Precision

0

##### 1.8.3.1.12 Scale

0

#### 1.8.3.2.0 name

##### 1.8.3.2.1 Name

name

##### 1.8.3.2.2 Type

🔹 VARCHAR

##### 1.8.3.2.3 Is Required

✅ Yes

##### 1.8.3.2.4 Is Primary Key

❌ No

##### 1.8.3.2.5 Is Unique

✅ Yes

##### 1.8.3.2.6 Index Type

UniqueIndex

##### 1.8.3.2.7 Size

255

##### 1.8.3.2.8 Constraints

*No items available*

##### 1.8.3.2.9 Default Value



##### 1.8.3.2.10 Is Foreign Key

❌ No

##### 1.8.3.2.11 Precision

0

##### 1.8.3.2.12 Scale

0

#### 1.8.3.3.0 sourceLocation

##### 1.8.3.3.1 Name

sourceLocation

##### 1.8.3.3.2 Type

🔹 VARCHAR

##### 1.8.3.3.3 Is Required

✅ Yes

##### 1.8.3.3.4 Is Primary Key

❌ No

##### 1.8.3.3.5 Is Unique

❌ No

##### 1.8.3.3.6 Index Type

None

##### 1.8.3.3.7 Size

255

##### 1.8.3.3.8 Constraints

*No items available*

##### 1.8.3.3.9 Default Value



##### 1.8.3.3.10 Is Foreign Key

❌ No

##### 1.8.3.3.11 Precision

0

##### 1.8.3.3.12 Scale

0

#### 1.8.3.4.0 destinationLocation

##### 1.8.3.4.1 Name

destinationLocation

##### 1.8.3.4.2 Type

🔹 VARCHAR

##### 1.8.3.4.3 Is Required

✅ Yes

##### 1.8.3.4.4 Is Primary Key

❌ No

##### 1.8.3.4.5 Is Unique

❌ No

##### 1.8.3.4.6 Index Type

None

##### 1.8.3.4.7 Size

255

##### 1.8.3.4.8 Constraints

*No items available*

##### 1.8.3.4.9 Default Value



##### 1.8.3.4.10 Is Foreign Key

❌ No

##### 1.8.3.4.11 Precision

0

##### 1.8.3.4.12 Scale

0

#### 1.8.3.5.0 standardDistanceKm

##### 1.8.3.5.1 Name

standardDistanceKm

##### 1.8.3.5.2 Type

🔹 DECIMAL

##### 1.8.3.5.3 Is Required

✅ Yes

##### 1.8.3.5.4 Is Primary Key

❌ No

##### 1.8.3.5.5 Is Unique

❌ No

##### 1.8.3.5.6 Index Type

None

##### 1.8.3.5.7 Size

0

##### 1.8.3.5.8 Constraints

- POSITIVE_VALUE

##### 1.8.3.5.9 Default Value

0

##### 1.8.3.5.10 Is Foreign Key

❌ No

##### 1.8.3.5.11 Precision

10

##### 1.8.3.5.12 Scale

2

#### 1.8.3.6.0 estimatedTransitTimeHours

##### 1.8.3.6.1 Name

estimatedTransitTimeHours

##### 1.8.3.6.2 Type

🔹 DECIMAL

##### 1.8.3.6.3 Is Required

❌ No

##### 1.8.3.6.4 Is Primary Key

❌ No

##### 1.8.3.6.5 Is Unique

❌ No

##### 1.8.3.6.6 Index Type

None

##### 1.8.3.6.7 Size

0

##### 1.8.3.6.8 Constraints

- POSITIVE_VALUE

##### 1.8.3.6.9 Default Value

0

##### 1.8.3.6.10 Is Foreign Key

❌ No

##### 1.8.3.6.11 Precision

10

##### 1.8.3.6.12 Scale

2

#### 1.8.3.7.0 isActive

##### 1.8.3.7.1 Name

isActive

##### 1.8.3.7.2 Type

🔹 BOOLEAN

##### 1.8.3.7.3 Is Required

✅ Yes

##### 1.8.3.7.4 Is Primary Key

❌ No

##### 1.8.3.7.5 Is Unique

❌ No

##### 1.8.3.7.6 Index Type

Index

##### 1.8.3.7.7 Size

0

##### 1.8.3.7.8 Constraints

*No items available*

##### 1.8.3.7.9 Default Value

true

##### 1.8.3.7.10 Is Foreign Key

❌ No

##### 1.8.3.7.11 Precision

0

##### 1.8.3.7.12 Scale

0

### 1.8.4.0.0 Primary Keys

- routeId

### 1.8.5.0.0 Unique Constraints

- {'name': 'UC_Route_Name', 'columns': ['name']}

### 1.8.6.0.0 Indexes

- {'name': 'IX_Route_IsActive', 'columns': ['isActive'], 'type': 'BTree'}

## 1.9.0.0.0 Trip

### 1.9.1.0.0 Name

Trip

### 1.9.2.0.0 Description

The central entity representing a single transport job, tracking its entire lifecycle. REQ-1-004, REQ-1-102, REQ-1-103.

### 1.9.3.0.0 Attributes

#### 1.9.3.1.0 tripId

##### 1.9.3.1.1 Name

tripId

##### 1.9.3.1.2 Type

🔹 Guid

##### 1.9.3.1.3 Is Required

✅ Yes

##### 1.9.3.1.4 Is Primary Key

✅ Yes

##### 1.9.3.1.5 Is Unique

✅ Yes

##### 1.9.3.1.6 Index Type

UniqueIndex

##### 1.9.3.1.7 Size

0

##### 1.9.3.1.8 Constraints

*No items available*

##### 1.9.3.1.9 Default Value



##### 1.9.3.1.10 Is Foreign Key

❌ No

##### 1.9.3.1.11 Precision

0

##### 1.9.3.1.12 Scale

0

#### 1.9.3.2.0 customerId

##### 1.9.3.2.1 Name

customerId

##### 1.9.3.2.2 Type

🔹 Guid

##### 1.9.3.2.3 Is Required

✅ Yes

##### 1.9.3.2.4 Is Primary Key

❌ No

##### 1.9.3.2.5 Is Unique

❌ No

##### 1.9.3.2.6 Index Type

Index

##### 1.9.3.2.7 Size

0

##### 1.9.3.2.8 Constraints

*No items available*

##### 1.9.3.2.9 Default Value



##### 1.9.3.2.10 Is Foreign Key

✅ Yes

##### 1.9.3.2.11 Precision

0

##### 1.9.3.2.12 Scale

0

#### 1.9.3.3.0 vehicleId

##### 1.9.3.3.1 Name

vehicleId

##### 1.9.3.3.2 Type

🔹 Guid

##### 1.9.3.3.3 Is Required

❌ No

##### 1.9.3.3.4 Is Primary Key

❌ No

##### 1.9.3.3.5 Is Unique

❌ No

##### 1.9.3.3.6 Index Type

Index

##### 1.9.3.3.7 Size

0

##### 1.9.3.3.8 Constraints

*No items available*

##### 1.9.3.3.9 Default Value



##### 1.9.3.3.10 Is Foreign Key

✅ Yes

##### 1.9.3.3.11 Precision

0

##### 1.9.3.3.12 Scale

0

#### 1.9.3.4.0 driverId

##### 1.9.3.4.1 Name

driverId

##### 1.9.3.4.2 Type

🔹 Guid

##### 1.9.3.4.3 Is Required

❌ No

##### 1.9.3.4.4 Is Primary Key

❌ No

##### 1.9.3.4.5 Is Unique

❌ No

##### 1.9.3.4.6 Index Type

Index

##### 1.9.3.4.7 Size

0

##### 1.9.3.4.8 Constraints

*No items available*

##### 1.9.3.4.9 Default Value



##### 1.9.3.4.10 Is Foreign Key

✅ Yes

##### 1.9.3.4.11 Precision

0

##### 1.9.3.4.12 Scale

0

#### 1.9.3.5.0 materialId

##### 1.9.3.5.1 Name

materialId

##### 1.9.3.5.2 Type

🔹 Guid

##### 1.9.3.5.3 Is Required

✅ Yes

##### 1.9.3.5.4 Is Primary Key

❌ No

##### 1.9.3.5.5 Is Unique

❌ No

##### 1.9.3.5.6 Index Type

Index

##### 1.9.3.5.7 Size

0

##### 1.9.3.5.8 Constraints

*No items available*

##### 1.9.3.5.9 Default Value



##### 1.9.3.5.10 Is Foreign Key

✅ Yes

##### 1.9.3.5.11 Precision

0

##### 1.9.3.5.12 Scale

0

#### 1.9.3.6.0 customerName

##### 1.9.3.6.1 Name

customerName

##### 1.9.3.6.2 Type

🔹 VARCHAR

##### 1.9.3.6.3 Is Required

❌ No

##### 1.9.3.6.4 Is Primary Key

❌ No

##### 1.9.3.6.5 Is Unique

❌ No

##### 1.9.3.6.6 Index Type

None

##### 1.9.3.6.7 Size

255

##### 1.9.3.6.8 Constraints

*No items available*

##### 1.9.3.6.9 Default Value



##### 1.9.3.6.10 Is Foreign Key

❌ No

##### 1.9.3.6.11 Precision

0

##### 1.9.3.6.12 Scale

0

#### 1.9.3.7.0 vehicleTruckNumber

##### 1.9.3.7.1 Name

vehicleTruckNumber

##### 1.9.3.7.2 Type

🔹 VARCHAR

##### 1.9.3.7.3 Is Required

❌ No

##### 1.9.3.7.4 Is Primary Key

❌ No

##### 1.9.3.7.5 Is Unique

❌ No

##### 1.9.3.7.6 Index Type

None

##### 1.9.3.7.7 Size

20

##### 1.9.3.7.8 Constraints

*No items available*

##### 1.9.3.7.9 Default Value



##### 1.9.3.7.10 Is Foreign Key

❌ No

##### 1.9.3.7.11 Precision

0

##### 1.9.3.7.12 Scale

0

#### 1.9.3.8.0 driverName

##### 1.9.3.8.1 Name

driverName

##### 1.9.3.8.2 Type

🔹 VARCHAR

##### 1.9.3.8.3 Is Required

❌ No

##### 1.9.3.8.4 Is Primary Key

❌ No

##### 1.9.3.8.5 Is Unique

❌ No

##### 1.9.3.8.6 Index Type

None

##### 1.9.3.8.7 Size

255

##### 1.9.3.8.8 Constraints

*No items available*

##### 1.9.3.8.9 Default Value



##### 1.9.3.8.10 Is Foreign Key

❌ No

##### 1.9.3.8.11 Precision

0

##### 1.9.3.8.12 Scale

0

#### 1.9.3.9.0 source

##### 1.9.3.9.1 Name

source

##### 1.9.3.9.2 Type

🔹 VARCHAR

##### 1.9.3.9.3 Is Required

✅ Yes

##### 1.9.3.9.4 Is Primary Key

❌ No

##### 1.9.3.9.5 Is Unique

❌ No

##### 1.9.3.9.6 Index Type

None

##### 1.9.3.9.7 Size

255

##### 1.9.3.9.8 Constraints

*No items available*

##### 1.9.3.9.9 Default Value



##### 1.9.3.9.10 Is Foreign Key

❌ No

##### 1.9.3.9.11 Precision

0

##### 1.9.3.9.12 Scale

0

#### 1.9.3.10.0 destination

##### 1.9.3.10.1 Name

destination

##### 1.9.3.10.2 Type

🔹 VARCHAR

##### 1.9.3.10.3 Is Required

✅ Yes

##### 1.9.3.10.4 Is Primary Key

❌ No

##### 1.9.3.10.5 Is Unique

❌ No

##### 1.9.3.10.6 Index Type

None

##### 1.9.3.10.7 Size

255

##### 1.9.3.10.8 Constraints

*No items available*

##### 1.9.3.10.9 Default Value



##### 1.9.3.10.10 Is Foreign Key

❌ No

##### 1.9.3.10.11 Precision

0

##### 1.9.3.10.12 Scale

0

#### 1.9.3.11.0 weightTons

##### 1.9.3.11.1 Name

weightTons

##### 1.9.3.11.2 Type

🔹 DECIMAL

##### 1.9.3.11.3 Is Required

✅ Yes

##### 1.9.3.11.4 Is Primary Key

❌ No

##### 1.9.3.11.5 Is Unique

❌ No

##### 1.9.3.11.6 Index Type

None

##### 1.9.3.11.7 Size

0

##### 1.9.3.11.8 Constraints

- POSITIVE_VALUE

##### 1.9.3.11.9 Default Value

0

##### 1.9.3.11.10 Is Foreign Key

❌ No

##### 1.9.3.11.11 Precision

10

##### 1.9.3.11.12 Scale

3

#### 1.9.3.12.0 rate

##### 1.9.3.12.1 Name

rate

##### 1.9.3.12.2 Type

🔹 DECIMAL

##### 1.9.3.12.3 Is Required

✅ Yes

##### 1.9.3.12.4 Is Primary Key

❌ No

##### 1.9.3.12.5 Is Unique

❌ No

##### 1.9.3.12.6 Index Type

None

##### 1.9.3.12.7 Size

0

##### 1.9.3.12.8 Constraints

- POSITIVE_VALUE

##### 1.9.3.12.9 Default Value

0

##### 1.9.3.12.10 Is Foreign Key

❌ No

##### 1.9.3.12.11 Precision

12

##### 1.9.3.12.12 Scale

2

#### 1.9.3.13.0 rateType

##### 1.9.3.13.1 Name

rateType

##### 1.9.3.13.2 Type

🔹 VARCHAR

##### 1.9.3.13.3 Is Required

✅ Yes

##### 1.9.3.13.4 Is Primary Key

❌ No

##### 1.9.3.13.5 Is Unique

❌ No

##### 1.9.3.13.6 Index Type

None

##### 1.9.3.13.7 Size

20

##### 1.9.3.13.8 Constraints

- ENUM('per_km', 'per_ton', 'fixed')

##### 1.9.3.13.9 Default Value

'fixed'

##### 1.9.3.13.10 Is Foreign Key

❌ No

##### 1.9.3.13.11 Precision

0

##### 1.9.3.13.12 Scale

0

#### 1.9.3.14.0 expectedDeliveryDate

##### 1.9.3.14.1 Name

expectedDeliveryDate

##### 1.9.3.14.2 Type

🔹 DateTime

##### 1.9.3.14.3 Is Required

✅ Yes

##### 1.9.3.14.4 Is Primary Key

❌ No

##### 1.9.3.14.5 Is Unique

❌ No

##### 1.9.3.14.6 Index Type

Index

##### 1.9.3.14.7 Size

0

##### 1.9.3.14.8 Constraints

*No items available*

##### 1.9.3.14.9 Default Value



##### 1.9.3.14.10 Is Foreign Key

❌ No

##### 1.9.3.14.11 Precision

0

##### 1.9.3.14.12 Scale

0

#### 1.9.3.15.0 actualDeliveryDate

##### 1.9.3.15.1 Name

actualDeliveryDate

##### 1.9.3.15.2 Type

🔹 DateTime

##### 1.9.3.15.3 Is Required

❌ No

##### 1.9.3.15.4 Is Primary Key

❌ No

##### 1.9.3.15.5 Is Unique

❌ No

##### 1.9.3.15.6 Index Type

None

##### 1.9.3.15.7 Size

0

##### 1.9.3.15.8 Constraints

*No items available*

##### 1.9.3.15.9 Default Value



##### 1.9.3.15.10 Is Foreign Key

❌ No

##### 1.9.3.15.11 Precision

0

##### 1.9.3.15.12 Scale

0

#### 1.9.3.16.0 status

##### 1.9.3.16.1 Name

status

##### 1.9.3.16.2 Type

🔹 VARCHAR

##### 1.9.3.16.3 Is Required

✅ Yes

##### 1.9.3.16.4 Is Primary Key

❌ No

##### 1.9.3.16.5 Is Unique

❌ No

##### 1.9.3.16.6 Index Type

Index

##### 1.9.3.16.7 Size

20

##### 1.9.3.16.8 Constraints

- ENUM('Planned', 'Assigned', 'In-Transit', 'On Hold', 'Delivered', 'Completed', 'Invoiced', 'Paid', 'Canceled')

##### 1.9.3.16.9 Default Value

'Planned'

##### 1.9.3.16.10 Is Foreign Key

❌ No

##### 1.9.3.16.11 Precision

0

##### 1.9.3.16.12 Scale

0

#### 1.9.3.17.0 cancellationReason

##### 1.9.3.17.1 Name

cancellationReason

##### 1.9.3.17.2 Type

🔹 TEXT

##### 1.9.3.17.3 Is Required

❌ No

##### 1.9.3.17.4 Is Primary Key

❌ No

##### 1.9.3.17.5 Is Unique

❌ No

##### 1.9.3.17.6 Index Type

None

##### 1.9.3.17.7 Size

0

##### 1.9.3.17.8 Constraints

*No items available*

##### 1.9.3.17.9 Default Value



##### 1.9.3.17.10 Is Foreign Key

❌ No

##### 1.9.3.17.11 Precision

0

##### 1.9.3.17.12 Scale

0

#### 1.9.3.18.0 onHoldResolutionComment

##### 1.9.3.18.1 Name

onHoldResolutionComment

##### 1.9.3.18.2 Type

🔹 TEXT

##### 1.9.3.18.3 Is Required

❌ No

##### 1.9.3.18.4 Is Primary Key

❌ No

##### 1.9.3.18.5 Is Unique

❌ No

##### 1.9.3.18.6 Index Type

None

##### 1.9.3.18.7 Size

0

##### 1.9.3.18.8 Constraints

*No items available*

##### 1.9.3.18.9 Default Value



##### 1.9.3.18.10 Is Foreign Key

❌ No

##### 1.9.3.18.11 Precision

0

##### 1.9.3.18.12 Scale

0

#### 1.9.3.19.0 createdAt

##### 1.9.3.19.1 Name

createdAt

##### 1.9.3.19.2 Type

🔹 DateTime

##### 1.9.3.19.3 Is Required

✅ Yes

##### 1.9.3.19.4 Is Primary Key

❌ No

##### 1.9.3.19.5 Is Unique

❌ No

##### 1.9.3.19.6 Index Type

Index

##### 1.9.3.19.7 Size

0

##### 1.9.3.19.8 Constraints

*No items available*

##### 1.9.3.19.9 Default Value

CURRENT_TIMESTAMP

##### 1.9.3.19.10 Is Foreign Key

❌ No

##### 1.9.3.19.11 Precision

0

##### 1.9.3.19.12 Scale

0

#### 1.9.3.20.0 updatedAt

##### 1.9.3.20.1 Name

updatedAt

##### 1.9.3.20.2 Type

🔹 DateTime

##### 1.9.3.20.3 Is Required

✅ Yes

##### 1.9.3.20.4 Is Primary Key

❌ No

##### 1.9.3.20.5 Is Unique

❌ No

##### 1.9.3.20.6 Index Type

None

##### 1.9.3.20.7 Size

0

##### 1.9.3.20.8 Constraints

*No items available*

##### 1.9.3.20.9 Default Value

CURRENT_TIMESTAMP

##### 1.9.3.20.10 Is Foreign Key

❌ No

##### 1.9.3.20.11 Precision

0

##### 1.9.3.20.12 Scale

0

### 1.9.4.0.0 Primary Keys

- tripId

### 1.9.5.0.0 Unique Constraints

*No items available*

### 1.9.6.0.0 Indexes

#### 1.9.6.1.0 IX_Trip_Status_ExpectedDeliveryDate

##### 1.9.6.1.1 Name

IX_Trip_Status_ExpectedDeliveryDate

##### 1.9.6.1.2 Columns

- status
- expectedDeliveryDate

##### 1.9.6.1.3 Type

🔹 BTree

#### 1.9.6.2.0 IX_Trip_CustomerId_Status

##### 1.9.6.2.1 Name

IX_Trip_CustomerId_Status

##### 1.9.6.2.2 Columns

- customerId
- status

##### 1.9.6.2.3 Type

🔹 BTree

#### 1.9.6.3.0 IX_Trip_Driver_Status

##### 1.9.6.3.1 Name

IX_Trip_Driver_Status

##### 1.9.6.3.2 Columns

- driverId
- status

##### 1.9.6.3.3 Type

🔹 BTree

### 1.9.7.0.0 Partitioning

#### 1.9.7.1.0 Type

🔹 RANGE

#### 1.9.7.2.0 Columns

- createdAt

#### 1.9.7.3.0 Strategy

Yearly

## 1.10.0.0.0 TripExpense

### 1.10.1.0.0 Name

TripExpense

### 1.10.2.0.0 Description

Records expenses submitted by drivers for a specific trip. REQ-1-107, REQ-1-108.

### 1.10.3.0.0 Attributes

#### 1.10.3.1.0 tripExpenseId

##### 1.10.3.1.1 Name

tripExpenseId

##### 1.10.3.1.2 Type

🔹 Guid

##### 1.10.3.1.3 Is Required

✅ Yes

##### 1.10.3.1.4 Is Primary Key

✅ Yes

##### 1.10.3.1.5 Is Unique

✅ Yes

##### 1.10.3.1.6 Index Type

UniqueIndex

##### 1.10.3.1.7 Size

0

##### 1.10.3.1.8 Constraints

*No items available*

##### 1.10.3.1.9 Default Value



##### 1.10.3.1.10 Is Foreign Key

❌ No

##### 1.10.3.1.11 Precision

0

##### 1.10.3.1.12 Scale

0

#### 1.10.3.2.0 tripId

##### 1.10.3.2.1 Name

tripId

##### 1.10.3.2.2 Type

🔹 Guid

##### 1.10.3.2.3 Is Required

✅ Yes

##### 1.10.3.2.4 Is Primary Key

❌ No

##### 1.10.3.2.5 Is Unique

❌ No

##### 1.10.3.2.6 Index Type

Index

##### 1.10.3.2.7 Size

0

##### 1.10.3.2.8 Constraints

*No items available*

##### 1.10.3.2.9 Default Value



##### 1.10.3.2.10 Is Foreign Key

✅ Yes

##### 1.10.3.2.11 Precision

0

##### 1.10.3.2.12 Scale

0

#### 1.10.3.3.0 driverId

##### 1.10.3.3.1 Name

driverId

##### 1.10.3.3.2 Type

🔹 Guid

##### 1.10.3.3.3 Is Required

✅ Yes

##### 1.10.3.3.4 Is Primary Key

❌ No

##### 1.10.3.3.5 Is Unique

❌ No

##### 1.10.3.3.6 Index Type

Index

##### 1.10.3.3.7 Size

0

##### 1.10.3.3.8 Constraints

*No items available*

##### 1.10.3.3.9 Default Value



##### 1.10.3.3.10 Is Foreign Key

✅ Yes

##### 1.10.3.3.11 Precision

0

##### 1.10.3.3.12 Scale

0

#### 1.10.3.4.0 expenseType

##### 1.10.3.4.1 Name

expenseType

##### 1.10.3.4.2 Type

🔹 VARCHAR

##### 1.10.3.4.3 Is Required

✅ Yes

##### 1.10.3.4.4 Is Primary Key

❌ No

##### 1.10.3.4.5 Is Unique

❌ No

##### 1.10.3.4.6 Index Type

Index

##### 1.10.3.4.7 Size

50

##### 1.10.3.4.8 Constraints

- ENUM('Diesel', 'Toll', 'Food', 'Repair', 'Other')

##### 1.10.3.4.9 Default Value



##### 1.10.3.4.10 Is Foreign Key

❌ No

##### 1.10.3.4.11 Precision

0

##### 1.10.3.4.12 Scale

0

#### 1.10.3.5.0 amount

##### 1.10.3.5.1 Name

amount

##### 1.10.3.5.2 Type

🔹 DECIMAL

##### 1.10.3.5.3 Is Required

✅ Yes

##### 1.10.3.5.4 Is Primary Key

❌ No

##### 1.10.3.5.5 Is Unique

❌ No

##### 1.10.3.5.6 Index Type

None

##### 1.10.3.5.7 Size

0

##### 1.10.3.5.8 Constraints

- POSITIVE_VALUE

##### 1.10.3.5.9 Default Value

0

##### 1.10.3.5.10 Is Foreign Key

❌ No

##### 1.10.3.5.11 Precision

12

##### 1.10.3.5.12 Scale

2

#### 1.10.3.6.0 receiptUrl

##### 1.10.3.6.1 Name

receiptUrl

##### 1.10.3.6.2 Type

🔹 VARCHAR

##### 1.10.3.6.3 Is Required

✅ Yes

##### 1.10.3.6.4 Is Primary Key

❌ No

##### 1.10.3.6.5 Is Unique

❌ No

##### 1.10.3.6.6 Index Type

None

##### 1.10.3.6.7 Size

512

##### 1.10.3.6.8 Constraints

*No items available*

##### 1.10.3.6.9 Default Value



##### 1.10.3.6.10 Is Foreign Key

❌ No

##### 1.10.3.6.11 Precision

0

##### 1.10.3.6.12 Scale

0

#### 1.10.3.7.0 status

##### 1.10.3.7.1 Name

status

##### 1.10.3.7.2 Type

🔹 VARCHAR

##### 1.10.3.7.3 Is Required

✅ Yes

##### 1.10.3.7.4 Is Primary Key

❌ No

##### 1.10.3.7.5 Is Unique

❌ No

##### 1.10.3.7.6 Index Type

Index

##### 1.10.3.7.7 Size

20

##### 1.10.3.7.8 Constraints

- ENUM('Submitted', 'Approved', 'Rejected')

##### 1.10.3.7.9 Default Value

'Submitted'

##### 1.10.3.7.10 Is Foreign Key

❌ No

##### 1.10.3.7.11 Precision

0

##### 1.10.3.7.12 Scale

0

#### 1.10.3.8.0 rejectionReason

##### 1.10.3.8.1 Name

rejectionReason

##### 1.10.3.8.2 Type

🔹 TEXT

##### 1.10.3.8.3 Is Required

❌ No

##### 1.10.3.8.4 Is Primary Key

❌ No

##### 1.10.3.8.5 Is Unique

❌ No

##### 1.10.3.8.6 Index Type

None

##### 1.10.3.8.7 Size

0

##### 1.10.3.8.8 Constraints

*No items available*

##### 1.10.3.8.9 Default Value



##### 1.10.3.8.10 Is Foreign Key

❌ No

##### 1.10.3.8.11 Precision

0

##### 1.10.3.8.12 Scale

0

#### 1.10.3.9.0 fuelQuantityLiters

##### 1.10.3.9.1 Name

fuelQuantityLiters

##### 1.10.3.9.2 Type

🔹 DECIMAL

##### 1.10.3.9.3 Is Required

❌ No

##### 1.10.3.9.4 Is Primary Key

❌ No

##### 1.10.3.9.5 Is Unique

❌ No

##### 1.10.3.9.6 Index Type

None

##### 1.10.3.9.7 Size

0

##### 1.10.3.9.8 Constraints

- POSITIVE_VALUE

##### 1.10.3.9.9 Default Value

0

##### 1.10.3.9.10 Is Foreign Key

❌ No

##### 1.10.3.9.11 Precision

10

##### 1.10.3.9.12 Scale

2

#### 1.10.3.10.0 odometerReading

##### 1.10.3.10.1 Name

odometerReading

##### 1.10.3.10.2 Type

🔹 INT

##### 1.10.3.10.3 Is Required

❌ No

##### 1.10.3.10.4 Is Primary Key

❌ No

##### 1.10.3.10.5 Is Unique

❌ No

##### 1.10.3.10.6 Index Type

None

##### 1.10.3.10.7 Size

0

##### 1.10.3.10.8 Constraints

- NON_NEGATIVE

##### 1.10.3.10.9 Default Value

0

##### 1.10.3.10.10 Is Foreign Key

❌ No

##### 1.10.3.10.11 Precision

0

##### 1.10.3.10.12 Scale

0

#### 1.10.3.11.0 submittedAt

##### 1.10.3.11.1 Name

submittedAt

##### 1.10.3.11.2 Type

🔹 DateTime

##### 1.10.3.11.3 Is Required

✅ Yes

##### 1.10.3.11.4 Is Primary Key

❌ No

##### 1.10.3.11.5 Is Unique

❌ No

##### 1.10.3.11.6 Index Type

Index

##### 1.10.3.11.7 Size

0

##### 1.10.3.11.8 Constraints

*No items available*

##### 1.10.3.11.9 Default Value

CURRENT_TIMESTAMP

##### 1.10.3.11.10 Is Foreign Key

❌ No

##### 1.10.3.11.11 Precision

0

##### 1.10.3.11.12 Scale

0

### 1.10.4.0.0 Primary Keys

- tripExpenseId

### 1.10.5.0.0 Unique Constraints

*No items available*

### 1.10.6.0.0 Indexes

#### 1.10.6.1.0 IX_TripExpense_TripId_Status

##### 1.10.6.1.1 Name

IX_TripExpense_TripId_Status

##### 1.10.6.1.2 Columns

- tripId
- status

##### 1.10.6.1.3 Type

🔹 BTree

#### 1.10.6.2.0 IX_TripExpense_Status_SubmittedAt

##### 1.10.6.2.1 Name

IX_TripExpense_Status_SubmittedAt

##### 1.10.6.2.2 Columns

- status
- submittedAt

##### 1.10.6.2.3 Type

🔹 BTree

## 1.11.0.0.0 Invoice

### 1.11.1.0.0 Name

Invoice

### 1.11.2.0.0 Description

Represents a GST-compliant invoice generated for a trip. REQ-1-005, REQ-1-006.

### 1.11.3.0.0 Attributes

#### 1.11.3.1.0 invoiceId

##### 1.11.3.1.1 Name

invoiceId

##### 1.11.3.1.2 Type

🔹 Guid

##### 1.11.3.1.3 Is Required

✅ Yes

##### 1.11.3.1.4 Is Primary Key

✅ Yes

##### 1.11.3.1.5 Is Unique

✅ Yes

##### 1.11.3.1.6 Index Type

UniqueIndex

##### 1.11.3.1.7 Size

0

##### 1.11.3.1.8 Constraints

*No items available*

##### 1.11.3.1.9 Default Value



##### 1.11.3.1.10 Is Foreign Key

❌ No

##### 1.11.3.1.11 Precision

0

##### 1.11.3.1.12 Scale

0

#### 1.11.3.2.0 tripId

##### 1.11.3.2.1 Name

tripId

##### 1.11.3.2.2 Type

🔹 Guid

##### 1.11.3.2.3 Is Required

✅ Yes

##### 1.11.3.2.4 Is Primary Key

❌ No

##### 1.11.3.2.5 Is Unique

✅ Yes

##### 1.11.3.2.6 Index Type

UniqueIndex

##### 1.11.3.2.7 Size

0

##### 1.11.3.2.8 Constraints

*No items available*

##### 1.11.3.2.9 Default Value



##### 1.11.3.2.10 Is Foreign Key

✅ Yes

##### 1.11.3.2.11 Precision

0

##### 1.11.3.2.12 Scale

0

#### 1.11.3.3.0 customerId

##### 1.11.3.3.1 Name

customerId

##### 1.11.3.3.2 Type

🔹 Guid

##### 1.11.3.3.3 Is Required

✅ Yes

##### 1.11.3.3.4 Is Primary Key

❌ No

##### 1.11.3.3.5 Is Unique

❌ No

##### 1.11.3.3.6 Index Type

Index

##### 1.11.3.3.7 Size

0

##### 1.11.3.3.8 Constraints

*No items available*

##### 1.11.3.3.9 Default Value



##### 1.11.3.3.10 Is Foreign Key

✅ Yes

##### 1.11.3.3.11 Precision

0

##### 1.11.3.3.12 Scale

0

#### 1.11.3.4.0 invoiceNumber

##### 1.11.3.4.1 Name

invoiceNumber

##### 1.11.3.4.2 Type

🔹 VARCHAR

##### 1.11.3.4.3 Is Required

✅ Yes

##### 1.11.3.4.4 Is Primary Key

❌ No

##### 1.11.3.4.5 Is Unique

✅ Yes

##### 1.11.3.4.6 Index Type

UniqueIndex

##### 1.11.3.4.7 Size

50

##### 1.11.3.4.8 Constraints

*No items available*

##### 1.11.3.4.9 Default Value



##### 1.11.3.4.10 Is Foreign Key

❌ No

##### 1.11.3.4.11 Precision

0

##### 1.11.3.4.12 Scale

0

#### 1.11.3.5.0 invoiceDate

##### 1.11.3.5.1 Name

invoiceDate

##### 1.11.3.5.2 Type

🔹 Date

##### 1.11.3.5.3 Is Required

✅ Yes

##### 1.11.3.5.4 Is Primary Key

❌ No

##### 1.11.3.5.5 Is Unique

❌ No

##### 1.11.3.5.6 Index Type

Index

##### 1.11.3.5.7 Size

0

##### 1.11.3.5.8 Constraints

*No items available*

##### 1.11.3.5.9 Default Value



##### 1.11.3.5.10 Is Foreign Key

❌ No

##### 1.11.3.5.11 Precision

0

##### 1.11.3.5.12 Scale

0

#### 1.11.3.6.0 dueDate

##### 1.11.3.6.1 Name

dueDate

##### 1.11.3.6.2 Type

🔹 Date

##### 1.11.3.6.3 Is Required

✅ Yes

##### 1.11.3.6.4 Is Primary Key

❌ No

##### 1.11.3.6.5 Is Unique

❌ No

##### 1.11.3.6.6 Index Type

Index

##### 1.11.3.6.7 Size

0

##### 1.11.3.6.8 Constraints

*No items available*

##### 1.11.3.6.9 Default Value



##### 1.11.3.6.10 Is Foreign Key

❌ No

##### 1.11.3.6.11 Precision

0

##### 1.11.3.6.12 Scale

0

#### 1.11.3.7.0 totalAmount

##### 1.11.3.7.1 Name

totalAmount

##### 1.11.3.7.2 Type

🔹 DECIMAL

##### 1.11.3.7.3 Is Required

✅ Yes

##### 1.11.3.7.4 Is Primary Key

❌ No

##### 1.11.3.7.5 Is Unique

❌ No

##### 1.11.3.7.6 Index Type

None

##### 1.11.3.7.7 Size

0

##### 1.11.3.7.8 Constraints

*No items available*

##### 1.11.3.7.9 Default Value

0

##### 1.11.3.7.10 Is Foreign Key

❌ No

##### 1.11.3.7.11 Precision

14

##### 1.11.3.7.12 Scale

2

#### 1.11.3.8.0 gstAmount

##### 1.11.3.8.1 Name

gstAmount

##### 1.11.3.8.2 Type

🔹 DECIMAL

##### 1.11.3.8.3 Is Required

✅ Yes

##### 1.11.3.8.4 Is Primary Key

❌ No

##### 1.11.3.8.5 Is Unique

❌ No

##### 1.11.3.8.6 Index Type

None

##### 1.11.3.8.7 Size

0

##### 1.11.3.8.8 Constraints

*No items available*

##### 1.11.3.8.9 Default Value

0

##### 1.11.3.8.10 Is Foreign Key

❌ No

##### 1.11.3.8.11 Precision

14

##### 1.11.3.8.12 Scale

2

#### 1.11.3.9.0 status

##### 1.11.3.9.1 Name

status

##### 1.11.3.9.2 Type

🔹 VARCHAR

##### 1.11.3.9.3 Is Required

✅ Yes

##### 1.11.3.9.4 Is Primary Key

❌ No

##### 1.11.3.9.5 Is Unique

❌ No

##### 1.11.3.9.6 Index Type

Index

##### 1.11.3.9.7 Size

20

##### 1.11.3.9.8 Constraints

- ENUM('Draft', 'Sent', 'Paid', 'Partially Paid', 'Canceled')

##### 1.11.3.9.9 Default Value

'Draft'

##### 1.11.3.9.10 Is Foreign Key

❌ No

##### 1.11.3.9.11 Precision

0

##### 1.11.3.9.12 Scale

0

#### 1.11.3.10.0 irn

##### 1.11.3.10.1 Name

irn

##### 1.11.3.10.2 Type

🔹 VARCHAR

##### 1.11.3.10.3 Is Required

❌ No

##### 1.11.3.10.4 Is Primary Key

❌ No

##### 1.11.3.10.5 Is Unique

✅ Yes

##### 1.11.3.10.6 Index Type

UniqueIndex

##### 1.11.3.10.7 Size

64

##### 1.11.3.10.8 Constraints

*No items available*

##### 1.11.3.10.9 Default Value



##### 1.11.3.10.10 Is Foreign Key

❌ No

##### 1.11.3.10.11 Precision

0

##### 1.11.3.10.12 Scale

0

#### 1.11.3.11.0 qrCodeData

##### 1.11.3.11.1 Name

qrCodeData

##### 1.11.3.11.2 Type

🔹 TEXT

##### 1.11.3.11.3 Is Required

❌ No

##### 1.11.3.11.4 Is Primary Key

❌ No

##### 1.11.3.11.5 Is Unique

❌ No

##### 1.11.3.11.6 Index Type

None

##### 1.11.3.11.7 Size

0

##### 1.11.3.11.8 Constraints

*No items available*

##### 1.11.3.11.9 Default Value



##### 1.11.3.11.10 Is Foreign Key

❌ No

##### 1.11.3.11.11 Precision

0

##### 1.11.3.11.12 Scale

0

#### 1.11.3.12.0 customerNameSnapshot

##### 1.11.3.12.1 Name

customerNameSnapshot

##### 1.11.3.12.2 Type

🔹 VARCHAR

##### 1.11.3.12.3 Is Required

✅ Yes

##### 1.11.3.12.4 Is Primary Key

❌ No

##### 1.11.3.12.5 Is Unique

❌ No

##### 1.11.3.12.6 Index Type

None

##### 1.11.3.12.7 Size

255

##### 1.11.3.12.8 Constraints

*No items available*

##### 1.11.3.12.9 Default Value



##### 1.11.3.12.10 Is Foreign Key

❌ No

##### 1.11.3.12.11 Precision

0

##### 1.11.3.12.12 Scale

0

#### 1.11.3.13.0 billingAddressSnapshot

##### 1.11.3.13.1 Name

billingAddressSnapshot

##### 1.11.3.13.2 Type

🔹 TEXT

##### 1.11.3.13.3 Is Required

✅ Yes

##### 1.11.3.13.4 Is Primary Key

❌ No

##### 1.11.3.13.5 Is Unique

❌ No

##### 1.11.3.13.6 Index Type

None

##### 1.11.3.13.7 Size

0

##### 1.11.3.13.8 Constraints

*No items available*

##### 1.11.3.13.9 Default Value



##### 1.11.3.13.10 Is Foreign Key

❌ No

##### 1.11.3.13.11 Precision

0

##### 1.11.3.13.12 Scale

0

#### 1.11.3.14.0 gstinSnapshot

##### 1.11.3.14.1 Name

gstinSnapshot

##### 1.11.3.14.2 Type

🔹 VARCHAR

##### 1.11.3.14.3 Is Required

❌ No

##### 1.11.3.14.4 Is Primary Key

❌ No

##### 1.11.3.14.5 Is Unique

❌ No

##### 1.11.3.14.6 Index Type

None

##### 1.11.3.14.7 Size

15

##### 1.11.3.14.8 Constraints

*No items available*

##### 1.11.3.14.9 Default Value



##### 1.11.3.14.10 Is Foreign Key

❌ No

##### 1.11.3.14.11 Precision

0

##### 1.11.3.14.12 Scale

0

#### 1.11.3.15.0 createdAt

##### 1.11.3.15.1 Name

createdAt

##### 1.11.3.15.2 Type

🔹 DateTime

##### 1.11.3.15.3 Is Required

✅ Yes

##### 1.11.3.15.4 Is Primary Key

❌ No

##### 1.11.3.15.5 Is Unique

❌ No

##### 1.11.3.15.6 Index Type

Index

##### 1.11.3.15.7 Size

0

##### 1.11.3.15.8 Constraints

*No items available*

##### 1.11.3.15.9 Default Value

CURRENT_TIMESTAMP

##### 1.11.3.15.10 Is Foreign Key

❌ No

##### 1.11.3.15.11 Precision

0

##### 1.11.3.15.12 Scale

0

### 1.11.4.0.0 Primary Keys

- invoiceId

### 1.11.5.0.0 Unique Constraints

#### 1.11.5.1.0 UC_Invoice_TripId

##### 1.11.5.1.1 Name

UC_Invoice_TripId

##### 1.11.5.1.2 Columns

- tripId

#### 1.11.5.2.0 UC_Invoice_InvoiceNumber

##### 1.11.5.2.1 Name

UC_Invoice_InvoiceNumber

##### 1.11.5.2.2 Columns

- invoiceNumber

#### 1.11.5.3.0 UC_Invoice_Irn

##### 1.11.5.3.1 Name

UC_Invoice_Irn

##### 1.11.5.3.2 Columns

- irn

### 1.11.6.0.0 Indexes

#### 1.11.6.1.0 IX_Invoice_CustomerId_Status

##### 1.11.6.1.1 Name

IX_Invoice_CustomerId_Status

##### 1.11.6.1.2 Columns

- customerId
- status

##### 1.11.6.1.3 Type

🔹 BTree

#### 1.11.6.2.0 IX_Invoice_Status_DueDate

##### 1.11.6.2.1 Name

IX_Invoice_Status_DueDate

##### 1.11.6.2.2 Columns

- status
- dueDate

##### 1.11.6.2.3 Type

🔹 BTree

#### 1.11.6.3.0 IX_Invoice_PaidStatus_DueDate

##### 1.11.6.3.1 Name

IX_Invoice_PaidStatus_DueDate

##### 1.11.6.3.2 Columns

- status
- dueDate

##### 1.11.6.3.3 Type

🔹 BTree

##### 1.11.6.3.4 Where

status IN ('Paid', 'Partially Paid')

## 1.12.0.0.0 Payment

### 1.12.1.0.0 Name

Payment

### 1.12.2.0.0 Description

Records payments received from customers against invoices. REQ-1-005.

### 1.12.3.0.0 Attributes

#### 1.12.3.1.0 paymentId

##### 1.12.3.1.1 Name

paymentId

##### 1.12.3.1.2 Type

🔹 Guid

##### 1.12.3.1.3 Is Required

✅ Yes

##### 1.12.3.1.4 Is Primary Key

✅ Yes

##### 1.12.3.1.5 Is Unique

✅ Yes

##### 1.12.3.1.6 Index Type

UniqueIndex

##### 1.12.3.1.7 Size

0

##### 1.12.3.1.8 Constraints

*No items available*

##### 1.12.3.1.9 Default Value



##### 1.12.3.1.10 Is Foreign Key

❌ No

##### 1.12.3.1.11 Precision

0

##### 1.12.3.1.12 Scale

0

#### 1.12.3.2.0 invoiceId

##### 1.12.3.2.1 Name

invoiceId

##### 1.12.3.2.2 Type

🔹 Guid

##### 1.12.3.2.3 Is Required

✅ Yes

##### 1.12.3.2.4 Is Primary Key

❌ No

##### 1.12.3.2.5 Is Unique

❌ No

##### 1.12.3.2.6 Index Type

Index

##### 1.12.3.2.7 Size

0

##### 1.12.3.2.8 Constraints

*No items available*

##### 1.12.3.2.9 Default Value



##### 1.12.3.2.10 Is Foreign Key

✅ Yes

##### 1.12.3.2.11 Precision

0

##### 1.12.3.2.12 Scale

0

#### 1.12.3.3.0 customerId

##### 1.12.3.3.1 Name

customerId

##### 1.12.3.3.2 Type

🔹 Guid

##### 1.12.3.3.3 Is Required

✅ Yes

##### 1.12.3.3.4 Is Primary Key

❌ No

##### 1.12.3.3.5 Is Unique

❌ No

##### 1.12.3.3.6 Index Type

Index

##### 1.12.3.3.7 Size

0

##### 1.12.3.3.8 Constraints

*No items available*

##### 1.12.3.3.9 Default Value



##### 1.12.3.3.10 Is Foreign Key

✅ Yes

##### 1.12.3.3.11 Precision

0

##### 1.12.3.3.12 Scale

0

#### 1.12.3.4.0 paymentDate

##### 1.12.3.4.1 Name

paymentDate

##### 1.12.3.4.2 Type

🔹 Date

##### 1.12.3.4.3 Is Required

✅ Yes

##### 1.12.3.4.4 Is Primary Key

❌ No

##### 1.12.3.4.5 Is Unique

❌ No

##### 1.12.3.4.6 Index Type

Index

##### 1.12.3.4.7 Size

0

##### 1.12.3.4.8 Constraints

*No items available*

##### 1.12.3.4.9 Default Value



##### 1.12.3.4.10 Is Foreign Key

❌ No

##### 1.12.3.4.11 Precision

0

##### 1.12.3.4.12 Scale

0

#### 1.12.3.5.0 amount

##### 1.12.3.5.1 Name

amount

##### 1.12.3.5.2 Type

🔹 DECIMAL

##### 1.12.3.5.3 Is Required

✅ Yes

##### 1.12.3.5.4 Is Primary Key

❌ No

##### 1.12.3.5.5 Is Unique

❌ No

##### 1.12.3.5.6 Index Type

None

##### 1.12.3.5.7 Size

0

##### 1.12.3.5.8 Constraints

- POSITIVE_VALUE

##### 1.12.3.5.9 Default Value

0

##### 1.12.3.5.10 Is Foreign Key

❌ No

##### 1.12.3.5.11 Precision

14

##### 1.12.3.5.12 Scale

2

#### 1.12.3.6.0 paymentMethod

##### 1.12.3.6.1 Name

paymentMethod

##### 1.12.3.6.2 Type

🔹 VARCHAR

##### 1.12.3.6.3 Is Required

❌ No

##### 1.12.3.6.4 Is Primary Key

❌ No

##### 1.12.3.6.5 Is Unique

❌ No

##### 1.12.3.6.6 Index Type

Index

##### 1.12.3.6.7 Size

50

##### 1.12.3.6.8 Constraints

*No items available*

##### 1.12.3.6.9 Default Value



##### 1.12.3.6.10 Is Foreign Key

❌ No

##### 1.12.3.6.11 Precision

0

##### 1.12.3.6.12 Scale

0

#### 1.12.3.7.0 transactionReference

##### 1.12.3.7.1 Name

transactionReference

##### 1.12.3.7.2 Type

🔹 VARCHAR

##### 1.12.3.7.3 Is Required

❌ No

##### 1.12.3.7.4 Is Primary Key

❌ No

##### 1.12.3.7.5 Is Unique

❌ No

##### 1.12.3.7.6 Index Type

Index

##### 1.12.3.7.7 Size

100

##### 1.12.3.7.8 Constraints

*No items available*

##### 1.12.3.7.9 Default Value



##### 1.12.3.7.10 Is Foreign Key

❌ No

##### 1.12.3.7.11 Precision

0

##### 1.12.3.7.12 Scale

0

#### 1.12.3.8.0 createdAt

##### 1.12.3.8.1 Name

createdAt

##### 1.12.3.8.2 Type

🔹 DateTime

##### 1.12.3.8.3 Is Required

✅ Yes

##### 1.12.3.8.4 Is Primary Key

❌ No

##### 1.12.3.8.5 Is Unique

❌ No

##### 1.12.3.8.6 Index Type

Index

##### 1.12.3.8.7 Size

0

##### 1.12.3.8.8 Constraints

*No items available*

##### 1.12.3.8.9 Default Value

CURRENT_TIMESTAMP

##### 1.12.3.8.10 Is Foreign Key

❌ No

##### 1.12.3.8.11 Precision

0

##### 1.12.3.8.12 Scale

0

### 1.12.4.0.0 Primary Keys

- paymentId

### 1.12.5.0.0 Unique Constraints

*No items available*

### 1.12.6.0.0 Indexes

#### 1.12.6.1.0 IX_Payment_InvoiceId

##### 1.12.6.1.1 Name

IX_Payment_InvoiceId

##### 1.12.6.1.2 Columns

- invoiceId

##### 1.12.6.1.3 Type

🔹 BTree

#### 1.12.6.2.0 IX_Payment_CustomerId_PaymentDate

##### 1.12.6.2.1 Name

IX_Payment_CustomerId_PaymentDate

##### 1.12.6.2.2 Columns

- customerId
- paymentDate

##### 1.12.6.2.3 Type

🔹 BTree

## 1.13.0.0.0 VehicleLocation

### 1.13.1.0.0 Name

VehicleLocation

### 1.13.2.0.0 Description

Stores time-series GPS location data for each vehicle. This is a high-volume table. REQ-1-007, REQ-1-105.

### 1.13.3.0.0 Attributes

#### 1.13.3.1.0 vehicleLocationId

##### 1.13.3.1.1 Name

vehicleLocationId

##### 1.13.3.1.2 Type

🔹 Guid

##### 1.13.3.1.3 Is Required

✅ Yes

##### 1.13.3.1.4 Is Primary Key

✅ Yes

##### 1.13.3.1.5 Is Unique

✅ Yes

##### 1.13.3.1.6 Index Type

UniqueIndex

##### 1.13.3.1.7 Size

0

##### 1.13.3.1.8 Constraints

*No items available*

##### 1.13.3.1.9 Default Value



##### 1.13.3.1.10 Is Foreign Key

❌ No

##### 1.13.3.1.11 Precision

0

##### 1.13.3.1.12 Scale

0

#### 1.13.3.2.0 vehicleId

##### 1.13.3.2.1 Name

vehicleId

##### 1.13.3.2.2 Type

🔹 Guid

##### 1.13.3.2.3 Is Required

✅ Yes

##### 1.13.3.2.4 Is Primary Key

❌ No

##### 1.13.3.2.5 Is Unique

❌ No

##### 1.13.3.2.6 Index Type

Index

##### 1.13.3.2.7 Size

0

##### 1.13.3.2.8 Constraints

*No items available*

##### 1.13.3.2.9 Default Value



##### 1.13.3.2.10 Is Foreign Key

✅ Yes

##### 1.13.3.2.11 Precision

0

##### 1.13.3.2.12 Scale

0

#### 1.13.3.3.0 latitude

##### 1.13.3.3.1 Name

latitude

##### 1.13.3.3.2 Type

🔹 DECIMAL

##### 1.13.3.3.3 Is Required

✅ Yes

##### 1.13.3.3.4 Is Primary Key

❌ No

##### 1.13.3.3.5 Is Unique

❌ No

##### 1.13.3.3.6 Index Type

None

##### 1.13.3.3.7 Size

0

##### 1.13.3.3.8 Constraints

*No items available*

##### 1.13.3.3.9 Default Value



##### 1.13.3.3.10 Is Foreign Key

❌ No

##### 1.13.3.3.11 Precision

9

##### 1.13.3.3.12 Scale

6

#### 1.13.3.4.0 longitude

##### 1.13.3.4.1 Name

longitude

##### 1.13.3.4.2 Type

🔹 DECIMAL

##### 1.13.3.4.3 Is Required

✅ Yes

##### 1.13.3.4.4 Is Primary Key

❌ No

##### 1.13.3.4.5 Is Unique

❌ No

##### 1.13.3.4.6 Index Type

None

##### 1.13.3.4.7 Size

0

##### 1.13.3.4.8 Constraints

*No items available*

##### 1.13.3.4.9 Default Value



##### 1.13.3.4.10 Is Foreign Key

❌ No

##### 1.13.3.4.11 Precision

9

##### 1.13.3.4.12 Scale

6

#### 1.13.3.5.0 timestamp

##### 1.13.3.5.1 Name

timestamp

##### 1.13.3.5.2 Type

🔹 DateTime

##### 1.13.3.5.3 Is Required

✅ Yes

##### 1.13.3.5.4 Is Primary Key

❌ No

##### 1.13.3.5.5 Is Unique

❌ No

##### 1.13.3.5.6 Index Type

Index

##### 1.13.3.5.7 Size

0

##### 1.13.3.5.8 Constraints

*No items available*

##### 1.13.3.5.9 Default Value



##### 1.13.3.5.10 Is Foreign Key

❌ No

##### 1.13.3.5.11 Precision

0

##### 1.13.3.5.12 Scale

0

#### 1.13.3.6.0 locationGeom

##### 1.13.3.6.1 Name

locationGeom

##### 1.13.3.6.2 Type

🔹 GEOMETRY

##### 1.13.3.6.3 Is Required

❌ No

##### 1.13.3.6.4 Is Primary Key

❌ No

##### 1.13.3.6.5 Is Unique

❌ No

##### 1.13.3.6.6 Index Type

Spatial

##### 1.13.3.6.7 Size

0

##### 1.13.3.6.8 Constraints

- SRID=4326

##### 1.13.3.6.9 Default Value

*Not specified*

##### 1.13.3.6.10 Is Foreign Key

❌ No

##### 1.13.3.6.11 Precision

0

##### 1.13.3.6.12 Scale

0

### 1.13.4.0.0 Primary Keys

- vehicleLocationId

### 1.13.5.0.0 Unique Constraints

*No items available*

### 1.13.6.0.0 Indexes

#### 1.13.6.1.0 IX_VehicleLocation_Vehicle_Timestamp

##### 1.13.6.1.1 Name

IX_VehicleLocation_Vehicle_Timestamp

##### 1.13.6.1.2 Columns

- vehicleId
- timestamp

##### 1.13.6.1.3 Type

🔹 BTree

#### 1.13.6.2.0 IX_VehicleLocation_Geom

##### 1.13.6.2.1 Name

IX_VehicleLocation_Geom

##### 1.13.6.2.2 Columns

- locationGeom

##### 1.13.6.2.3 Type

🔹 GiST

### 1.13.7.0.0 Partitioning

#### 1.13.7.1.0 Type

🔹 RANGE

#### 1.13.7.2.0 Columns

- timestamp

#### 1.13.7.3.0 Strategy

Monthly

## 1.14.0.0.0 Alert

### 1.14.1.0.0 Name

Alert

### 1.14.2.0.0 Description

Stores system-generated alerts for critical events like document expiry or low balances. REQ-1-010.

### 1.14.3.0.0 Attributes

#### 1.14.3.1.0 alertId

##### 1.14.3.1.1 Name

alertId

##### 1.14.3.1.2 Type

🔹 Guid

##### 1.14.3.1.3 Is Required

✅ Yes

##### 1.14.3.1.4 Is Primary Key

✅ Yes

##### 1.14.3.1.5 Is Unique

✅ Yes

##### 1.14.3.1.6 Index Type

UniqueIndex

##### 1.14.3.1.7 Size

0

##### 1.14.3.1.8 Constraints

*No items available*

##### 1.14.3.1.9 Default Value



##### 1.14.3.1.10 Is Foreign Key

❌ No

##### 1.14.3.1.11 Precision

0

##### 1.14.3.1.12 Scale

0

#### 1.14.3.2.0 alertType

##### 1.14.3.2.1 Name

alertType

##### 1.14.3.2.2 Type

🔹 VARCHAR

##### 1.14.3.2.3 Is Required

✅ Yes

##### 1.14.3.2.4 Is Primary Key

❌ No

##### 1.14.3.2.5 Is Unique

❌ No

##### 1.14.3.2.6 Index Type

Index

##### 1.14.3.2.7 Size

50

##### 1.14.3.2.8 Constraints

- ENUM('DocumentExpiry', 'LowBalance', 'CriticalTripEvent', 'Geofence')

##### 1.14.3.2.9 Default Value



##### 1.14.3.2.10 Is Foreign Key

❌ No

##### 1.14.3.2.11 Precision

0

##### 1.14.3.2.12 Scale

0

#### 1.14.3.3.0 message

##### 1.14.3.3.1 Name

message

##### 1.14.3.3.2 Type

🔹 TEXT

##### 1.14.3.3.3 Is Required

✅ Yes

##### 1.14.3.3.4 Is Primary Key

❌ No

##### 1.14.3.3.5 Is Unique

❌ No

##### 1.14.3.3.6 Index Type

None

##### 1.14.3.3.7 Size

0

##### 1.14.3.3.8 Constraints

*No items available*

##### 1.14.3.3.9 Default Value



##### 1.14.3.3.10 Is Foreign Key

❌ No

##### 1.14.3.3.11 Precision

0

##### 1.14.3.3.12 Scale

0

#### 1.14.3.4.0 relatedModel

##### 1.14.3.4.1 Name

relatedModel

##### 1.14.3.4.2 Type

🔹 VARCHAR

##### 1.14.3.4.3 Is Required

❌ No

##### 1.14.3.4.4 Is Primary Key

❌ No

##### 1.14.3.4.5 Is Unique

❌ No

##### 1.14.3.4.6 Index Type

None

##### 1.14.3.4.7 Size

100

##### 1.14.3.4.8 Constraints

*No items available*

##### 1.14.3.4.9 Default Value



##### 1.14.3.4.10 Is Foreign Key

❌ No

##### 1.14.3.4.11 Precision

0

##### 1.14.3.4.12 Scale

0

#### 1.14.3.5.0 relatedRecordId

##### 1.14.3.5.1 Name

relatedRecordId

##### 1.14.3.5.2 Type

🔹 Guid

##### 1.14.3.5.3 Is Required

❌ No

##### 1.14.3.5.4 Is Primary Key

❌ No

##### 1.14.3.5.5 Is Unique

❌ No

##### 1.14.3.5.6 Index Type

Index

##### 1.14.3.5.7 Size

0

##### 1.14.3.5.8 Constraints

*No items available*

##### 1.14.3.5.9 Default Value



##### 1.14.3.5.10 Is Foreign Key

❌ No

##### 1.14.3.5.11 Precision

0

##### 1.14.3.5.12 Scale

0

#### 1.14.3.6.0 status

##### 1.14.3.6.1 Name

status

##### 1.14.3.6.2 Type

🔹 VARCHAR

##### 1.14.3.6.3 Is Required

✅ Yes

##### 1.14.3.6.4 Is Primary Key

❌ No

##### 1.14.3.6.5 Is Unique

❌ No

##### 1.14.3.6.6 Index Type

Index

##### 1.14.3.6.7 Size

20

##### 1.14.3.6.8 Constraints

- ENUM('New', 'Acknowledged', 'Resolved')

##### 1.14.3.6.9 Default Value

'New'

##### 1.14.3.6.10 Is Foreign Key

❌ No

##### 1.14.3.6.11 Precision

0

##### 1.14.3.6.12 Scale

0

#### 1.14.3.7.0 severity

##### 1.14.3.7.1 Name

severity

##### 1.14.3.7.2 Type

🔹 VARCHAR

##### 1.14.3.7.3 Is Required

✅ Yes

##### 1.14.3.7.4 Is Primary Key

❌ No

##### 1.14.3.7.5 Is Unique

❌ No

##### 1.14.3.7.6 Index Type

Index

##### 1.14.3.7.7 Size

20

##### 1.14.3.7.8 Constraints

- ENUM('Low', 'Medium', 'High', 'Critical')

##### 1.14.3.7.9 Default Value

'Medium'

##### 1.14.3.7.10 Is Foreign Key

❌ No

##### 1.14.3.7.11 Precision

0

##### 1.14.3.7.12 Scale

0

#### 1.14.3.8.0 createdAt

##### 1.14.3.8.1 Name

createdAt

##### 1.14.3.8.2 Type

🔹 DateTime

##### 1.14.3.8.3 Is Required

✅ Yes

##### 1.14.3.8.4 Is Primary Key

❌ No

##### 1.14.3.8.5 Is Unique

❌ No

##### 1.14.3.8.6 Index Type

Index

##### 1.14.3.8.7 Size

0

##### 1.14.3.8.8 Constraints

*No items available*

##### 1.14.3.8.9 Default Value

CURRENT_TIMESTAMP

##### 1.14.3.8.10 Is Foreign Key

❌ No

##### 1.14.3.8.11 Precision

0

##### 1.14.3.8.12 Scale

0

### 1.14.4.0.0 Primary Keys

- alertId

### 1.14.5.0.0 Unique Constraints

*No items available*

### 1.14.6.0.0 Indexes

#### 1.14.6.1.0 IX_Alert_Status_CreatedAt

##### 1.14.6.1.1 Name

IX_Alert_Status_CreatedAt

##### 1.14.6.1.2 Columns

- status
- createdAt

##### 1.14.6.1.3 Type

🔹 BTree

#### 1.14.6.2.0 IX_Alert_RelatedRecord

##### 1.14.6.2.1 Name

IX_Alert_RelatedRecord

##### 1.14.6.2.2 Columns

- relatedModel
- relatedRecordId

##### 1.14.6.2.3 Type

🔹 BTree

#### 1.14.6.3.0 IX_Alert_Dashboard

##### 1.14.6.3.1 Name

IX_Alert_Dashboard

##### 1.14.6.3.2 Columns

- status
- severity
- createdAt DESC

##### 1.14.6.3.3 Type

🔹 BTree

## 1.15.0.0.0 Geofence

### 1.15.1.0.0 Name

Geofence

### 1.15.2.0.0 Description

Defines geographical boundaries for monitoring vehicle entry and exit. REQ-1-106.

### 1.15.3.0.0 Attributes

#### 1.15.3.1.0 geofenceId

##### 1.15.3.1.1 Name

geofenceId

##### 1.15.3.1.2 Type

🔹 Guid

##### 1.15.3.1.3 Is Required

✅ Yes

##### 1.15.3.1.4 Is Primary Key

✅ Yes

##### 1.15.3.1.5 Is Unique

✅ Yes

##### 1.15.3.1.6 Index Type

UniqueIndex

##### 1.15.3.1.7 Size

0

##### 1.15.3.1.8 Constraints

*No items available*

##### 1.15.3.1.9 Default Value



##### 1.15.3.1.10 Is Foreign Key

❌ No

##### 1.15.3.1.11 Precision

0

##### 1.15.3.1.12 Scale

0

#### 1.15.3.2.0 name

##### 1.15.3.2.1 Name

name

##### 1.15.3.2.2 Type

🔹 VARCHAR

##### 1.15.3.2.3 Is Required

✅ Yes

##### 1.15.3.2.4 Is Primary Key

❌ No

##### 1.15.3.2.5 Is Unique

✅ Yes

##### 1.15.3.2.6 Index Type

UniqueIndex

##### 1.15.3.2.7 Size

100

##### 1.15.3.2.8 Constraints

*No items available*

##### 1.15.3.2.9 Default Value



##### 1.15.3.2.10 Is Foreign Key

❌ No

##### 1.15.3.2.11 Precision

0

##### 1.15.3.2.12 Scale

0

#### 1.15.3.3.0 coordinates

##### 1.15.3.3.1 Name

coordinates

##### 1.15.3.3.2 Type

🔹 JSON

##### 1.15.3.3.3 Is Required

✅ Yes

##### 1.15.3.3.4 Is Primary Key

❌ No

##### 1.15.3.3.5 Is Unique

❌ No

##### 1.15.3.3.6 Index Type

None

##### 1.15.3.3.7 Size

0

##### 1.15.3.3.8 Constraints

*No items available*

##### 1.15.3.3.9 Default Value



##### 1.15.3.3.10 Is Foreign Key

❌ No

##### 1.15.3.3.11 Precision

0

##### 1.15.3.3.12 Scale

0

#### 1.15.3.4.0 isActive

##### 1.15.3.4.1 Name

isActive

##### 1.15.3.4.2 Type

🔹 BOOLEAN

##### 1.15.3.4.3 Is Required

✅ Yes

##### 1.15.3.4.4 Is Primary Key

❌ No

##### 1.15.3.4.5 Is Unique

❌ No

##### 1.15.3.4.6 Index Type

Index

##### 1.15.3.4.7 Size

0

##### 1.15.3.4.8 Constraints

*No items available*

##### 1.15.3.4.9 Default Value

true

##### 1.15.3.4.10 Is Foreign Key

❌ No

##### 1.15.3.4.11 Precision

0

##### 1.15.3.4.12 Scale

0

### 1.15.4.0.0 Primary Keys

- geofenceId

### 1.15.5.0.0 Unique Constraints

- {'name': 'UC_Geofence_Name', 'columns': ['name']}

### 1.15.6.0.0 Indexes

- {'name': 'IX_Geofence_IsActive', 'columns': ['isActive'], 'type': 'BTree'}

## 1.16.0.0.0 GeofenceEvent

### 1.16.1.0.0 Name

GeofenceEvent

### 1.16.2.0.0 Description

Logs when a vehicle enters or exits a defined geofence. REQ-1-106.

### 1.16.3.0.0 Attributes

#### 1.16.3.1.0 geofenceEventId

##### 1.16.3.1.1 Name

geofenceEventId

##### 1.16.3.1.2 Type

🔹 Guid

##### 1.16.3.1.3 Is Required

✅ Yes

##### 1.16.3.1.4 Is Primary Key

✅ Yes

##### 1.16.3.1.5 Is Unique

✅ Yes

##### 1.16.3.1.6 Index Type

UniqueIndex

##### 1.16.3.1.7 Size

0

##### 1.16.3.1.8 Constraints

*No items available*

##### 1.16.3.1.9 Default Value



##### 1.16.3.1.10 Is Foreign Key

❌ No

##### 1.16.3.1.11 Precision

0

##### 1.16.3.1.12 Scale

0

#### 1.16.3.2.0 geofenceId

##### 1.16.3.2.1 Name

geofenceId

##### 1.16.3.2.2 Type

🔹 Guid

##### 1.16.3.2.3 Is Required

✅ Yes

##### 1.16.3.2.4 Is Primary Key

❌ No

##### 1.16.3.2.5 Is Unique

❌ No

##### 1.16.3.2.6 Index Type

Index

##### 1.16.3.2.7 Size

0

##### 1.16.3.2.8 Constraints

*No items available*

##### 1.16.3.2.9 Default Value



##### 1.16.3.2.10 Is Foreign Key

✅ Yes

##### 1.16.3.2.11 Precision

0

##### 1.16.3.2.12 Scale

0

#### 1.16.3.3.0 vehicleId

##### 1.16.3.3.1 Name

vehicleId

##### 1.16.3.3.2 Type

🔹 Guid

##### 1.16.3.3.3 Is Required

✅ Yes

##### 1.16.3.3.4 Is Primary Key

❌ No

##### 1.16.3.3.5 Is Unique

❌ No

##### 1.16.3.3.6 Index Type

Index

##### 1.16.3.3.7 Size

0

##### 1.16.3.3.8 Constraints

*No items available*

##### 1.16.3.3.9 Default Value



##### 1.16.3.3.10 Is Foreign Key

✅ Yes

##### 1.16.3.3.11 Precision

0

##### 1.16.3.3.12 Scale

0

#### 1.16.3.4.0 eventType

##### 1.16.3.4.1 Name

eventType

##### 1.16.3.4.2 Type

🔹 VARCHAR

##### 1.16.3.4.3 Is Required

✅ Yes

##### 1.16.3.4.4 Is Primary Key

❌ No

##### 1.16.3.4.5 Is Unique

❌ No

##### 1.16.3.4.6 Index Type

None

##### 1.16.3.4.7 Size

10

##### 1.16.3.4.8 Constraints

- ENUM('Entry', 'Exit')

##### 1.16.3.4.9 Default Value



##### 1.16.3.4.10 Is Foreign Key

❌ No

##### 1.16.3.4.11 Precision

0

##### 1.16.3.4.12 Scale

0

#### 1.16.3.5.0 timestamp

##### 1.16.3.5.1 Name

timestamp

##### 1.16.3.5.2 Type

🔹 DateTime

##### 1.16.3.5.3 Is Required

✅ Yes

##### 1.16.3.5.4 Is Primary Key

❌ No

##### 1.16.3.5.5 Is Unique

❌ No

##### 1.16.3.5.6 Index Type

Index

##### 1.16.3.5.7 Size

0

##### 1.16.3.5.8 Constraints

*No items available*

##### 1.16.3.5.9 Default Value

CURRENT_TIMESTAMP

##### 1.16.3.5.10 Is Foreign Key

❌ No

##### 1.16.3.5.11 Precision

0

##### 1.16.3.5.12 Scale

0

### 1.16.4.0.0 Primary Keys

- geofenceEventId

### 1.16.5.0.0 Unique Constraints

*No items available*

### 1.16.6.0.0 Indexes

#### 1.16.6.1.0 IX_GeofenceEvent_Vehicle_Timestamp

##### 1.16.6.1.1 Name

IX_GeofenceEvent_Vehicle_Timestamp

##### 1.16.6.1.2 Columns

- vehicleId
- timestamp

##### 1.16.6.1.3 Type

🔹 BTree

#### 1.16.6.2.0 IX_GeofenceEvent_Geofence_Timestamp

##### 1.16.6.2.1 Name

IX_GeofenceEvent_Geofence_Timestamp

##### 1.16.6.2.2 Columns

- geofenceId
- timestamp

##### 1.16.6.2.3 Type

🔹 BTree

## 1.17.0.0.0 Card

### 1.17.1.0.0 Name

Card

### 1.17.2.0.0 Description

Manages FASTag and diesel cards, including manual balance tracking. REQ-1-110.

### 1.17.3.0.0 Attributes

#### 1.17.3.1.0 cardId

##### 1.17.3.1.1 Name

cardId

##### 1.17.3.1.2 Type

🔹 Guid

##### 1.17.3.1.3 Is Required

✅ Yes

##### 1.17.3.1.4 Is Primary Key

✅ Yes

##### 1.17.3.1.5 Is Unique

✅ Yes

##### 1.17.3.1.6 Index Type

UniqueIndex

##### 1.17.3.1.7 Size

0

##### 1.17.3.1.8 Constraints

*No items available*

##### 1.17.3.1.9 Default Value



##### 1.17.3.1.10 Is Foreign Key

❌ No

##### 1.17.3.1.11 Precision

0

##### 1.17.3.1.12 Scale

0

#### 1.17.3.2.0 cardType

##### 1.17.3.2.1 Name

cardType

##### 1.17.3.2.2 Type

🔹 VARCHAR

##### 1.17.3.2.3 Is Required

✅ Yes

##### 1.17.3.2.4 Is Primary Key

❌ No

##### 1.17.3.2.5 Is Unique

❌ No

##### 1.17.3.2.6 Index Type

Index

##### 1.17.3.2.7 Size

20

##### 1.17.3.2.8 Constraints

- ENUM('FASTag', 'Diesel')

##### 1.17.3.2.9 Default Value



##### 1.17.3.2.10 Is Foreign Key

❌ No

##### 1.17.3.2.11 Precision

0

##### 1.17.3.2.12 Scale

0

#### 1.17.3.3.0 cardNumber

##### 1.17.3.3.1 Name

cardNumber

##### 1.17.3.3.2 Type

🔹 VARCHAR

##### 1.17.3.3.3 Is Required

✅ Yes

##### 1.17.3.3.4 Is Primary Key

❌ No

##### 1.17.3.3.5 Is Unique

✅ Yes

##### 1.17.3.3.6 Index Type

UniqueIndex

##### 1.17.3.3.7 Size

50

##### 1.17.3.3.8 Constraints

*No items available*

##### 1.17.3.3.9 Default Value



##### 1.17.3.3.10 Is Foreign Key

❌ No

##### 1.17.3.3.11 Precision

0

##### 1.17.3.3.12 Scale

0

#### 1.17.3.4.0 provider

##### 1.17.3.4.1 Name

provider

##### 1.17.3.4.2 Type

🔹 VARCHAR

##### 1.17.3.4.3 Is Required

❌ No

##### 1.17.3.4.4 Is Primary Key

❌ No

##### 1.17.3.4.5 Is Unique

❌ No

##### 1.17.3.4.6 Index Type

None

##### 1.17.3.4.7 Size

100

##### 1.17.3.4.8 Constraints

*No items available*

##### 1.17.3.4.9 Default Value



##### 1.17.3.4.10 Is Foreign Key

❌ No

##### 1.17.3.4.11 Precision

0

##### 1.17.3.4.12 Scale

0

#### 1.17.3.5.0 assignedVehicleId

##### 1.17.3.5.1 Name

assignedVehicleId

##### 1.17.3.5.2 Type

🔹 Guid

##### 1.17.3.5.3 Is Required

❌ No

##### 1.17.3.5.4 Is Primary Key

❌ No

##### 1.17.3.5.5 Is Unique

❌ No

##### 1.17.3.5.6 Index Type

Index

##### 1.17.3.5.7 Size

0

##### 1.17.3.5.8 Constraints

*No items available*

##### 1.17.3.5.9 Default Value



##### 1.17.3.5.10 Is Foreign Key

✅ Yes

##### 1.17.3.5.11 Precision

0

##### 1.17.3.5.12 Scale

0

#### 1.17.3.6.0 balance

##### 1.17.3.6.1 Name

balance

##### 1.17.3.6.2 Type

🔹 DECIMAL

##### 1.17.3.6.3 Is Required

✅ Yes

##### 1.17.3.6.4 Is Primary Key

❌ No

##### 1.17.3.6.5 Is Unique

❌ No

##### 1.17.3.6.6 Index Type

None

##### 1.17.3.6.7 Size

0

##### 1.17.3.6.8 Constraints

*No items available*

##### 1.17.3.6.9 Default Value

0

##### 1.17.3.6.10 Is Foreign Key

❌ No

##### 1.17.3.6.11 Precision

12

##### 1.17.3.6.12 Scale

2

#### 1.17.3.7.0 lowBalanceThreshold

##### 1.17.3.7.1 Name

lowBalanceThreshold

##### 1.17.3.7.2 Type

🔹 DECIMAL

##### 1.17.3.7.3 Is Required

✅ Yes

##### 1.17.3.7.4 Is Primary Key

❌ No

##### 1.17.3.7.5 Is Unique

❌ No

##### 1.17.3.7.6 Index Type

None

##### 1.17.3.7.7 Size

0

##### 1.17.3.7.8 Constraints

*No items available*

##### 1.17.3.7.9 Default Value

0

##### 1.17.3.7.10 Is Foreign Key

❌ No

##### 1.17.3.7.11 Precision

12

##### 1.17.3.7.12 Scale

2

#### 1.17.3.8.0 isActive

##### 1.17.3.8.1 Name

isActive

##### 1.17.3.8.2 Type

🔹 BOOLEAN

##### 1.17.3.8.3 Is Required

✅ Yes

##### 1.17.3.8.4 Is Primary Key

❌ No

##### 1.17.3.8.5 Is Unique

❌ No

##### 1.17.3.8.6 Index Type

Index

##### 1.17.3.8.7 Size

0

##### 1.17.3.8.8 Constraints

*No items available*

##### 1.17.3.8.9 Default Value

true

##### 1.17.3.8.10 Is Foreign Key

❌ No

##### 1.17.3.8.11 Precision

0

##### 1.17.3.8.12 Scale

0

### 1.17.4.0.0 Primary Keys

- cardId

### 1.17.5.0.0 Unique Constraints

- {'name': 'UC_Card_CardNumber', 'columns': ['cardNumber']}

### 1.17.6.0.0 Indexes

#### 1.17.6.1.0 IX_Card_AssignedVehicleId

##### 1.17.6.1.1 Name

IX_Card_AssignedVehicleId

##### 1.17.6.1.2 Columns

- assignedVehicleId

##### 1.17.6.1.3 Type

🔹 BTree

#### 1.17.6.2.0 IX_Card_IsActive

##### 1.17.6.2.1 Name

IX_Card_IsActive

##### 1.17.6.2.2 Columns

- isActive

##### 1.17.6.2.3 Type

🔹 BTree

## 1.18.0.0.0 ProofOfDelivery

### 1.18.1.0.0 Name

ProofOfDelivery

### 1.18.2.0.0 Description

Stores Proof of Delivery (POD) data, such as photos or e-signatures, for a trip. REQ-1-114.

### 1.18.3.0.0 Attributes

#### 1.18.3.1.0 podId

##### 1.18.3.1.1 Name

podId

##### 1.18.3.1.2 Type

🔹 Guid

##### 1.18.3.1.3 Is Required

✅ Yes

##### 1.18.3.1.4 Is Primary Key

✅ Yes

##### 1.18.3.1.5 Is Unique

✅ Yes

##### 1.18.3.1.6 Index Type

UniqueIndex

##### 1.18.3.1.7 Size

0

##### 1.18.3.1.8 Constraints

*No items available*

##### 1.18.3.1.9 Default Value



##### 1.18.3.1.10 Is Foreign Key

❌ No

##### 1.18.3.1.11 Precision

0

##### 1.18.3.1.12 Scale

0

#### 1.18.3.2.0 tripId

##### 1.18.3.2.1 Name

tripId

##### 1.18.3.2.2 Type

🔹 Guid

##### 1.18.3.2.3 Is Required

✅ Yes

##### 1.18.3.2.4 Is Primary Key

❌ No

##### 1.18.3.2.5 Is Unique

✅ Yes

##### 1.18.3.2.6 Index Type

UniqueIndex

##### 1.18.3.2.7 Size

0

##### 1.18.3.2.8 Constraints

*No items available*

##### 1.18.3.2.9 Default Value



##### 1.18.3.2.10 Is Foreign Key

✅ Yes

##### 1.18.3.2.11 Precision

0

##### 1.18.3.2.12 Scale

0

#### 1.18.3.3.0 podType

##### 1.18.3.3.1 Name

podType

##### 1.18.3.3.2 Type

🔹 VARCHAR

##### 1.18.3.3.3 Is Required

✅ Yes

##### 1.18.3.3.4 Is Primary Key

❌ No

##### 1.18.3.3.5 Is Unique

❌ No

##### 1.18.3.3.6 Index Type

None

##### 1.18.3.3.7 Size

20

##### 1.18.3.3.8 Constraints

- ENUM('Photo', 'eSignature')

##### 1.18.3.3.9 Default Value



##### 1.18.3.3.10 Is Foreign Key

❌ No

##### 1.18.3.3.11 Precision

0

##### 1.18.3.3.12 Scale

0

#### 1.18.3.4.0 podDataUrl

##### 1.18.3.4.1 Name

podDataUrl

##### 1.18.3.4.2 Type

🔹 VARCHAR

##### 1.18.3.4.3 Is Required

✅ Yes

##### 1.18.3.4.4 Is Primary Key

❌ No

##### 1.18.3.4.5 Is Unique

❌ No

##### 1.18.3.4.6 Index Type

None

##### 1.18.3.4.7 Size

512

##### 1.18.3.4.8 Constraints

*No items available*

##### 1.18.3.4.9 Default Value



##### 1.18.3.4.10 Is Foreign Key

❌ No

##### 1.18.3.4.11 Precision

0

##### 1.18.3.4.12 Scale

0

#### 1.18.3.5.0 recipientName

##### 1.18.3.5.1 Name

recipientName

##### 1.18.3.5.2 Type

🔹 VARCHAR

##### 1.18.3.5.3 Is Required

✅ Yes

##### 1.18.3.5.4 Is Primary Key

❌ No

##### 1.18.3.5.5 Is Unique

❌ No

##### 1.18.3.5.6 Index Type

None

##### 1.18.3.5.7 Size

255

##### 1.18.3.5.8 Constraints

*No items available*

##### 1.18.3.5.9 Default Value



##### 1.18.3.5.10 Is Foreign Key

❌ No

##### 1.18.3.5.11 Precision

0

##### 1.18.3.5.12 Scale

0

#### 1.18.3.6.0 submittedAt

##### 1.18.3.6.1 Name

submittedAt

##### 1.18.3.6.2 Type

🔹 DateTime

##### 1.18.3.6.3 Is Required

✅ Yes

##### 1.18.3.6.4 Is Primary Key

❌ No

##### 1.18.3.6.5 Is Unique

❌ No

##### 1.18.3.6.6 Index Type

Index

##### 1.18.3.6.7 Size

0

##### 1.18.3.6.8 Constraints

*No items available*

##### 1.18.3.6.9 Default Value

CURRENT_TIMESTAMP

##### 1.18.3.6.10 Is Foreign Key

❌ No

##### 1.18.3.6.11 Precision

0

##### 1.18.3.6.12 Scale

0

### 1.18.4.0.0 Primary Keys

- podId

### 1.18.5.0.0 Unique Constraints

- {'name': 'UC_ProofOfDelivery_TripId', 'columns': ['tripId']}

### 1.18.6.0.0 Indexes

*No items available*

## 1.19.0.0.0 TripEventLog

### 1.19.1.0.0 Name

TripEventLog

### 1.19.2.0.0 Description

Logs events that occur during a trip, as reported by the driver. REQ-1-115.

### 1.19.3.0.0 Attributes

#### 1.19.3.1.0 tripEventLogId

##### 1.19.3.1.1 Name

tripEventLogId

##### 1.19.3.1.2 Type

🔹 Guid

##### 1.19.3.1.3 Is Required

✅ Yes

##### 1.19.3.1.4 Is Primary Key

✅ Yes

##### 1.19.3.1.5 Is Unique

✅ Yes

##### 1.19.3.1.6 Index Type

UniqueIndex

##### 1.19.3.1.7 Size

0

##### 1.19.3.1.8 Constraints

*No items available*

##### 1.19.3.1.9 Default Value



##### 1.19.3.1.10 Is Foreign Key

❌ No

##### 1.19.3.1.11 Precision

0

##### 1.19.3.1.12 Scale

0

#### 1.19.3.2.0 tripId

##### 1.19.3.2.1 Name

tripId

##### 1.19.3.2.2 Type

🔹 Guid

##### 1.19.3.2.3 Is Required

✅ Yes

##### 1.19.3.2.4 Is Primary Key

❌ No

##### 1.19.3.2.5 Is Unique

❌ No

##### 1.19.3.2.6 Index Type

Index

##### 1.19.3.2.7 Size

0

##### 1.19.3.2.8 Constraints

*No items available*

##### 1.19.3.2.9 Default Value



##### 1.19.3.2.10 Is Foreign Key

✅ Yes

##### 1.19.3.2.11 Precision

0

##### 1.19.3.2.12 Scale

0

#### 1.19.3.3.0 driverId

##### 1.19.3.3.1 Name

driverId

##### 1.19.3.3.2 Type

🔹 Guid

##### 1.19.3.3.3 Is Required

✅ Yes

##### 1.19.3.3.4 Is Primary Key

❌ No

##### 1.19.3.3.5 Is Unique

❌ No

##### 1.19.3.3.6 Index Type

Index

##### 1.19.3.3.7 Size

0

##### 1.19.3.3.8 Constraints

*No items available*

##### 1.19.3.3.9 Default Value



##### 1.19.3.3.10 Is Foreign Key

✅ Yes

##### 1.19.3.3.11 Precision

0

##### 1.19.3.3.12 Scale

0

#### 1.19.3.4.0 eventType

##### 1.19.3.4.1 Name

eventType

##### 1.19.3.4.2 Type

🔹 VARCHAR

##### 1.19.3.4.3 Is Required

✅ Yes

##### 1.19.3.4.4 Is Primary Key

❌ No

##### 1.19.3.4.5 Is Unique

❌ No

##### 1.19.3.4.6 Index Type

Index

##### 1.19.3.4.7 Size

50

##### 1.19.3.4.8 Constraints

- ENUM('Accident', 'Repair', 'Government Stoppage', 'Fueling', 'Trip Start')

##### 1.19.3.4.9 Default Value



##### 1.19.3.4.10 Is Foreign Key

❌ No

##### 1.19.3.4.11 Precision

0

##### 1.19.3.4.12 Scale

0

#### 1.19.3.5.0 eventTimestamp

##### 1.19.3.5.1 Name

eventTimestamp

##### 1.19.3.5.2 Type

🔹 DateTime

##### 1.19.3.5.3 Is Required

✅ Yes

##### 1.19.3.5.4 Is Primary Key

❌ No

##### 1.19.3.5.5 Is Unique

❌ No

##### 1.19.3.5.6 Index Type

Index

##### 1.19.3.5.7 Size

0

##### 1.19.3.5.8 Constraints

*No items available*

##### 1.19.3.5.9 Default Value

CURRENT_TIMESTAMP

##### 1.19.3.5.10 Is Foreign Key

❌ No

##### 1.19.3.5.11 Precision

0

##### 1.19.3.5.12 Scale

0

#### 1.19.3.6.0 photoUrl

##### 1.19.3.6.1 Name

photoUrl

##### 1.19.3.6.2 Type

🔹 VARCHAR

##### 1.19.3.6.3 Is Required

❌ No

##### 1.19.3.6.4 Is Primary Key

❌ No

##### 1.19.3.6.5 Is Unique

❌ No

##### 1.19.3.6.6 Index Type

None

##### 1.19.3.6.7 Size

512

##### 1.19.3.6.8 Constraints

*No items available*

##### 1.19.3.6.9 Default Value



##### 1.19.3.6.10 Is Foreign Key

❌ No

##### 1.19.3.6.11 Precision

0

##### 1.19.3.6.12 Scale

0

#### 1.19.3.7.0 notes

##### 1.19.3.7.1 Name

notes

##### 1.19.3.7.2 Type

🔹 TEXT

##### 1.19.3.7.3 Is Required

❌ No

##### 1.19.3.7.4 Is Primary Key

❌ No

##### 1.19.3.7.5 Is Unique

❌ No

##### 1.19.3.7.6 Index Type

None

##### 1.19.3.7.7 Size

0

##### 1.19.3.7.8 Constraints

*No items available*

##### 1.19.3.7.9 Default Value



##### 1.19.3.7.10 Is Foreign Key

❌ No

##### 1.19.3.7.11 Precision

0

##### 1.19.3.7.12 Scale

0

### 1.19.4.0.0 Primary Keys

- tripEventLogId

### 1.19.5.0.0 Unique Constraints

*No items available*

### 1.19.6.0.0 Indexes

- {'name': 'IX_TripEventLog_Trip_Timestamp', 'columns': ['tripId', 'eventTimestamp'], 'type': 'BTree'}

## 1.20.0.0.0 AuditLog

### 1.20.1.0.0 Name

AuditLog

### 1.20.2.0.0 Description

Provides an immutable audit trail for all significant data changes in the system. REQ-1-207.

### 1.20.3.0.0 Attributes

#### 1.20.3.1.0 auditLogId

##### 1.20.3.1.1 Name

auditLogId

##### 1.20.3.1.2 Type

🔹 Guid

##### 1.20.3.1.3 Is Required

✅ Yes

##### 1.20.3.1.4 Is Primary Key

✅ Yes

##### 1.20.3.1.5 Is Unique

✅ Yes

##### 1.20.3.1.6 Index Type

UniqueIndex

##### 1.20.3.1.7 Size

0

##### 1.20.3.1.8 Constraints

*No items available*

##### 1.20.3.1.9 Default Value



##### 1.20.3.1.10 Is Foreign Key

❌ No

##### 1.20.3.1.11 Precision

0

##### 1.20.3.1.12 Scale

0

#### 1.20.3.2.0 userId

##### 1.20.3.2.1 Name

userId

##### 1.20.3.2.2 Type

🔹 Guid

##### 1.20.3.2.3 Is Required

✅ Yes

##### 1.20.3.2.4 Is Primary Key

❌ No

##### 1.20.3.2.5 Is Unique

❌ No

##### 1.20.3.2.6 Index Type

Index

##### 1.20.3.2.7 Size

0

##### 1.20.3.2.8 Constraints

*No items available*

##### 1.20.3.2.9 Default Value



##### 1.20.3.2.10 Is Foreign Key

✅ Yes

##### 1.20.3.2.11 Precision

0

##### 1.20.3.2.12 Scale

0

#### 1.20.3.3.0 timestamp

##### 1.20.3.3.1 Name

timestamp

##### 1.20.3.3.2 Type

🔹 DateTime

##### 1.20.3.3.3 Is Required

✅ Yes

##### 1.20.3.3.4 Is Primary Key

❌ No

##### 1.20.3.3.5 Is Unique

❌ No

##### 1.20.3.3.6 Index Type

Index

##### 1.20.3.3.7 Size

0

##### 1.20.3.3.8 Constraints

*No items available*

##### 1.20.3.3.9 Default Value

CURRENT_TIMESTAMP

##### 1.20.3.3.10 Is Foreign Key

❌ No

##### 1.20.3.3.11 Precision

0

##### 1.20.3.3.12 Scale

0

#### 1.20.3.4.0 actionType

##### 1.20.3.4.1 Name

actionType

##### 1.20.3.4.2 Type

🔹 VARCHAR

##### 1.20.3.4.3 Is Required

✅ Yes

##### 1.20.3.4.4 Is Primary Key

❌ No

##### 1.20.3.4.5 Is Unique

❌ No

##### 1.20.3.4.6 Index Type

Index

##### 1.20.3.4.7 Size

20

##### 1.20.3.4.8 Constraints

- ENUM('Create', 'Update', 'Delete')

##### 1.20.3.4.9 Default Value



##### 1.20.3.4.10 Is Foreign Key

❌ No

##### 1.20.3.4.11 Precision

0

##### 1.20.3.4.12 Scale

0

#### 1.20.3.5.0 modelName

##### 1.20.3.5.1 Name

modelName

##### 1.20.3.5.2 Type

🔹 VARCHAR

##### 1.20.3.5.3 Is Required

✅ Yes

##### 1.20.3.5.4 Is Primary Key

❌ No

##### 1.20.3.5.5 Is Unique

❌ No

##### 1.20.3.5.6 Index Type

None

##### 1.20.3.5.7 Size

100

##### 1.20.3.5.8 Constraints

*No items available*

##### 1.20.3.5.9 Default Value



##### 1.20.3.5.10 Is Foreign Key

❌ No

##### 1.20.3.5.11 Precision

0

##### 1.20.3.5.12 Scale

0

#### 1.20.3.6.0 recordId

##### 1.20.3.6.1 Name

recordId

##### 1.20.3.6.2 Type

🔹 Guid

##### 1.20.3.6.3 Is Required

✅ Yes

##### 1.20.3.6.4 Is Primary Key

❌ No

##### 1.20.3.6.5 Is Unique

❌ No

##### 1.20.3.6.6 Index Type

Index

##### 1.20.3.6.7 Size

0

##### 1.20.3.6.8 Constraints

*No items available*

##### 1.20.3.6.9 Default Value



##### 1.20.3.6.10 Is Foreign Key

❌ No

##### 1.20.3.6.11 Precision

0

##### 1.20.3.6.12 Scale

0

#### 1.20.3.7.0 changes

##### 1.20.3.7.1 Name

changes

##### 1.20.3.7.2 Type

🔹 JSON

##### 1.20.3.7.3 Is Required

❌ No

##### 1.20.3.7.4 Is Primary Key

❌ No

##### 1.20.3.7.5 Is Unique

❌ No

##### 1.20.3.7.6 Index Type

None

##### 1.20.3.7.7 Size

0

##### 1.20.3.7.8 Constraints

*No items available*

##### 1.20.3.7.9 Default Value



##### 1.20.3.7.10 Is Foreign Key

❌ No

##### 1.20.3.7.11 Precision

0

##### 1.20.3.7.12 Scale

0

### 1.20.4.0.0 Primary Keys

- auditLogId

### 1.20.5.0.0 Unique Constraints

*No items available*

### 1.20.6.0.0 Indexes

#### 1.20.6.1.0 IX_AuditLog_Record_Timestamp

##### 1.20.6.1.1 Name

IX_AuditLog_Record_Timestamp

##### 1.20.6.1.2 Columns

- modelName
- recordId
- timestamp

##### 1.20.6.1.3 Type

🔹 BTree

#### 1.20.6.2.0 IX_AuditLog_UserId_Timestamp

##### 1.20.6.2.1 Name

IX_AuditLog_UserId_Timestamp

##### 1.20.6.2.2 Columns

- userId
- timestamp

##### 1.20.6.2.3 Type

🔹 BTree

### 1.20.7.0.0 Partitioning

#### 1.20.7.1.0 Type

🔹 RANGE

#### 1.20.7.2.0 Columns

- timestamp

#### 1.20.7.3.0 Strategy

Quarterly

# 2.0.0.0.0 Relations

## 2.1.0.0.0 RoleHasUsers

### 2.1.1.0.0 Name

RoleHasUsers

### 2.1.2.0.0 Id

REL_ROLE_USER_001

### 2.1.3.0.0 Source Entity

Role

### 2.1.4.0.0 Target Entity

User

### 2.1.5.0.0 Type

🔹 OneToMany

### 2.1.6.0.0 Source Multiplicity

1

### 2.1.7.0.0 Target Multiplicity

0..*

### 2.1.8.0.0 Cascade Delete

❌ No

### 2.1.9.0.0 Is Identifying

❌ No

### 2.1.10.0.0 On Delete

Restrict

### 2.1.11.0.0 On Update

Cascade

## 2.2.0.0.0 VehicleHasDocuments

### 2.2.1.0.0 Name

VehicleHasDocuments

### 2.2.2.0.0 Id

REL_VEHICLE_VEHICLEDOCUMENT_001

### 2.2.3.0.0 Source Entity

Vehicle

### 2.2.4.0.0 Target Entity

VehicleDocument

### 2.2.5.0.0 Type

🔹 OneToMany

### 2.2.6.0.0 Source Multiplicity

1

### 2.2.7.0.0 Target Multiplicity

0..*

### 2.2.8.0.0 Cascade Delete

✅ Yes

### 2.2.9.0.0 Is Identifying

❌ No

### 2.2.10.0.0 On Delete

Cascade

### 2.2.11.0.0 On Update

Cascade

## 2.3.0.0.0 CustomerHasTrips

### 2.3.1.0.0 Name

CustomerHasTrips

### 2.3.2.0.0 Id

REL_CUSTOMER_TRIP_001

### 2.3.3.0.0 Source Entity

Customer

### 2.3.4.0.0 Target Entity

Trip

### 2.3.5.0.0 Type

🔹 OneToMany

### 2.3.6.0.0 Source Multiplicity

1

### 2.3.7.0.0 Target Multiplicity

0..*

### 2.3.8.0.0 Cascade Delete

❌ No

### 2.3.9.0.0 Is Identifying

❌ No

### 2.3.10.0.0 On Delete

Restrict

### 2.3.11.0.0 On Update

Cascade

## 2.4.0.0.0 VehiclePerformsTrips

### 2.4.1.0.0 Name

VehiclePerformsTrips

### 2.4.2.0.0 Id

REL_VEHICLE_TRIP_001

### 2.4.3.0.0 Source Entity

Vehicle

### 2.4.4.0.0 Target Entity

Trip

### 2.4.5.0.0 Type

🔹 OneToMany

### 2.4.6.0.0 Source Multiplicity

1

### 2.4.7.0.0 Target Multiplicity

0..*

### 2.4.8.0.0 Cascade Delete

❌ No

### 2.4.9.0.0 Is Identifying

❌ No

### 2.4.10.0.0 On Delete

SetNull

### 2.4.11.0.0 On Update

Cascade

## 2.5.0.0.0 DriverAssignedToTrips

### 2.5.1.0.0 Name

DriverAssignedToTrips

### 2.5.2.0.0 Id

REL_DRIVER_TRIP_001

### 2.5.3.0.0 Source Entity

Driver

### 2.5.4.0.0 Target Entity

Trip

### 2.5.5.0.0 Type

🔹 OneToMany

### 2.5.6.0.0 Source Multiplicity

1

### 2.5.7.0.0 Target Multiplicity

0..*

### 2.5.8.0.0 Cascade Delete

❌ No

### 2.5.9.0.0 Is Identifying

❌ No

### 2.5.10.0.0 On Delete

SetNull

### 2.5.11.0.0 On Update

Cascade

## 2.6.0.0.0 MaterialTransportedInTrips

### 2.6.1.0.0 Name

MaterialTransportedInTrips

### 2.6.2.0.0 Id

REL_MATERIAL_TRIP_001

### 2.6.3.0.0 Source Entity

Material

### 2.6.4.0.0 Target Entity

Trip

### 2.6.5.0.0 Type

🔹 OneToMany

### 2.6.6.0.0 Source Multiplicity

1

### 2.6.7.0.0 Target Multiplicity

0..*

### 2.6.8.0.0 Cascade Delete

❌ No

### 2.6.9.0.0 Is Identifying

❌ No

### 2.6.10.0.0 On Delete

Restrict

### 2.6.11.0.0 On Update

Cascade

## 2.7.0.0.0 TripHasExpenses

### 2.7.1.0.0 Name

TripHasExpenses

### 2.7.2.0.0 Id

REL_TRIP_TRIPEXPENSE_001

### 2.7.3.0.0 Source Entity

Trip

### 2.7.4.0.0 Target Entity

TripExpense

### 2.7.5.0.0 Type

🔹 OneToMany

### 2.7.6.0.0 Source Multiplicity

1

### 2.7.7.0.0 Target Multiplicity

0..*

### 2.7.8.0.0 Cascade Delete

✅ Yes

### 2.7.9.0.0 Is Identifying

❌ No

### 2.7.10.0.0 On Delete

Cascade

### 2.7.11.0.0 On Update

Cascade

## 2.8.0.0.0 DriverSubmitsExpenses

### 2.8.1.0.0 Name

DriverSubmitsExpenses

### 2.8.2.0.0 Id

REL_DRIVER_TRIPEXPENSE_001

### 2.8.3.0.0 Source Entity

Driver

### 2.8.4.0.0 Target Entity

TripExpense

### 2.8.5.0.0 Type

🔹 OneToMany

### 2.8.6.0.0 Source Multiplicity

1

### 2.8.7.0.0 Target Multiplicity

0..*

### 2.8.8.0.0 Cascade Delete

❌ No

### 2.8.9.0.0 Is Identifying

❌ No

### 2.8.10.0.0 On Delete

Restrict

### 2.8.11.0.0 On Update

Cascade

## 2.9.0.0.0 TripGeneratesInvoice

### 2.9.1.0.0 Name

TripGeneratesInvoice

### 2.9.2.0.0 Id

REL_TRIP_INVOICE_001

### 2.9.3.0.0 Source Entity

Trip

### 2.9.4.0.0 Target Entity

Invoice

### 2.9.5.0.0 Type

🔹 OneToOne

### 2.9.6.0.0 Source Multiplicity

1

### 2.9.7.0.0 Target Multiplicity

0..1

### 2.9.8.0.0 Cascade Delete

❌ No

### 2.9.9.0.0 Is Identifying

❌ No

### 2.9.10.0.0 On Delete

Restrict

### 2.9.11.0.0 On Update

Cascade

## 2.10.0.0.0 CustomerReceivesInvoices

### 2.10.1.0.0 Name

CustomerReceivesInvoices

### 2.10.2.0.0 Id

REL_CUSTOMER_INVOICE_001

### 2.10.3.0.0 Source Entity

Customer

### 2.10.4.0.0 Target Entity

Invoice

### 2.10.5.0.0 Type

🔹 OneToMany

### 2.10.6.0.0 Source Multiplicity

1

### 2.10.7.0.0 Target Multiplicity

0..*

### 2.10.8.0.0 Cascade Delete

❌ No

### 2.10.9.0.0 Is Identifying

❌ No

### 2.10.10.0.0 On Delete

Restrict

### 2.10.11.0.0 On Update

Cascade

## 2.11.0.0.0 InvoiceHasPayments

### 2.11.1.0.0 Name

InvoiceHasPayments

### 2.11.2.0.0 Id

REL_INVOICE_PAYMENT_001

### 2.11.3.0.0 Source Entity

Invoice

### 2.11.4.0.0 Target Entity

Payment

### 2.11.5.0.0 Type

🔹 OneToMany

### 2.11.6.0.0 Source Multiplicity

1

### 2.11.7.0.0 Target Multiplicity

0..*

### 2.11.8.0.0 Cascade Delete

❌ No

### 2.11.9.0.0 Is Identifying

❌ No

### 2.11.10.0.0 On Delete

Restrict

### 2.11.11.0.0 On Update

Cascade

## 2.12.0.0.0 CustomerMakesPayments

### 2.12.1.0.0 Name

CustomerMakesPayments

### 2.12.2.0.0 Id

REL_CUSTOMER_PAYMENT_001

### 2.12.3.0.0 Source Entity

Customer

### 2.12.4.0.0 Target Entity

Payment

### 2.12.5.0.0 Type

🔹 OneToMany

### 2.12.6.0.0 Source Multiplicity

1

### 2.12.7.0.0 Target Multiplicity

0..*

### 2.12.8.0.0 Cascade Delete

❌ No

### 2.12.9.0.0 Is Identifying

❌ No

### 2.12.10.0.0 On Delete

Restrict

### 2.12.11.0.0 On Update

Cascade

## 2.13.0.0.0 VehicleHasLocations

### 2.13.1.0.0 Name

VehicleHasLocations

### 2.13.2.0.0 Id

REL_VEHICLE_VEHICLELOCATION_001

### 2.13.3.0.0 Source Entity

Vehicle

### 2.13.4.0.0 Target Entity

VehicleLocation

### 2.13.5.0.0 Type

🔹 OneToMany

### 2.13.6.0.0 Source Multiplicity

1

### 2.13.7.0.0 Target Multiplicity

0..*

### 2.13.8.0.0 Cascade Delete

✅ Yes

### 2.13.9.0.0 Is Identifying

❌ No

### 2.13.10.0.0 On Delete

Cascade

### 2.13.11.0.0 On Update

Cascade

## 2.14.0.0.0 GeofenceHasEvents

### 2.14.1.0.0 Name

GeofenceHasEvents

### 2.14.2.0.0 Id

REL_GEOFENCE_GEOFENCEEVENT_001

### 2.14.3.0.0 Source Entity

Geofence

### 2.14.4.0.0 Target Entity

GeofenceEvent

### 2.14.5.0.0 Type

🔹 OneToMany

### 2.14.6.0.0 Source Multiplicity

1

### 2.14.7.0.0 Target Multiplicity

0..*

### 2.14.8.0.0 Cascade Delete

✅ Yes

### 2.14.9.0.0 Is Identifying

❌ No

### 2.14.10.0.0 On Delete

Cascade

### 2.14.11.0.0 On Update

Cascade

## 2.15.0.0.0 VehicleTriggersGeofenceEvents

### 2.15.1.0.0 Name

VehicleTriggersGeofenceEvents

### 2.15.2.0.0 Id

REL_VEHICLE_GEOFENCEEVENT_001

### 2.15.3.0.0 Source Entity

Vehicle

### 2.15.4.0.0 Target Entity

GeofenceEvent

### 2.15.5.0.0 Type

🔹 OneToMany

### 2.15.6.0.0 Source Multiplicity

1

### 2.15.7.0.0 Target Multiplicity

0..*

### 2.15.8.0.0 Cascade Delete

✅ Yes

### 2.15.9.0.0 Is Identifying

❌ No

### 2.15.10.0.0 On Delete

Cascade

### 2.15.11.0.0 On Update

Cascade

## 2.16.0.0.0 VehicleAssignedCards

### 2.16.1.0.0 Name

VehicleAssignedCards

### 2.16.2.0.0 Id

REL_VEHICLE_CARD_001

### 2.16.3.0.0 Source Entity

Vehicle

### 2.16.4.0.0 Target Entity

Card

### 2.16.5.0.0 Type

🔹 OneToMany

### 2.16.6.0.0 Source Multiplicity

1

### 2.16.7.0.0 Target Multiplicity

0..*

### 2.16.8.0.0 Cascade Delete

❌ No

### 2.16.9.0.0 Is Identifying

❌ No

### 2.16.10.0.0 On Delete

SetNull

### 2.16.11.0.0 On Update

Cascade

## 2.17.0.0.0 TripHasProofOfDelivery

### 2.17.1.0.0 Name

TripHasProofOfDelivery

### 2.17.2.0.0 Id

REL_TRIP_PROOFOFDELIVERY_001

### 2.17.3.0.0 Source Entity

Trip

### 2.17.4.0.0 Target Entity

ProofOfDelivery

### 2.17.5.0.0 Type

🔹 OneToOne

### 2.17.6.0.0 Source Multiplicity

1

### 2.17.7.0.0 Target Multiplicity

0..1

### 2.17.8.0.0 Cascade Delete

✅ Yes

### 2.17.9.0.0 Is Identifying

❌ No

### 2.17.10.0.0 On Delete

Cascade

### 2.17.11.0.0 On Update

Cascade

## 2.18.0.0.0 TripHasEventLogs

### 2.18.1.0.0 Name

TripHasEventLogs

### 2.18.2.0.0 Id

REL_TRIP_TRIPEVENTLOG_001

### 2.18.3.0.0 Source Entity

Trip

### 2.18.4.0.0 Target Entity

TripEventLog

### 2.18.5.0.0 Type

🔹 OneToMany

### 2.18.6.0.0 Source Multiplicity

1

### 2.18.7.0.0 Target Multiplicity

0..*

### 2.18.8.0.0 Cascade Delete

✅ Yes

### 2.18.9.0.0 Is Identifying

❌ No

### 2.18.10.0.0 On Delete

Cascade

### 2.18.11.0.0 On Update

Cascade

## 2.19.0.0.0 DriverLogsTripEvents

### 2.19.1.0.0 Name

DriverLogsTripEvents

### 2.19.2.0.0 Id

REL_DRIVER_TRIPEVENTLOG_001

### 2.19.3.0.0 Source Entity

Driver

### 2.19.4.0.0 Target Entity

TripEventLog

### 2.19.5.0.0 Type

🔹 OneToMany

### 2.19.6.0.0 Source Multiplicity

1

### 2.19.7.0.0 Target Multiplicity

0..*

### 2.19.8.0.0 Cascade Delete

❌ No

### 2.19.9.0.0 Is Identifying

❌ No

### 2.19.10.0.0 On Delete

Restrict

### 2.19.11.0.0 On Update

Cascade

## 2.20.0.0.0 UserCreatesAuditLogs

### 2.20.1.0.0 Name

UserCreatesAuditLogs

### 2.20.2.0.0 Id

REL_USER_AUDITLOG_001

### 2.20.3.0.0 Source Entity

User

### 2.20.4.0.0 Target Entity

AuditLog

### 2.20.5.0.0 Type

🔹 OneToMany

### 2.20.6.0.0 Source Multiplicity

1

### 2.20.7.0.0 Target Multiplicity

0..*

### 2.20.8.0.0 Cascade Delete

❌ No

### 2.20.9.0.0 Is Identifying

❌ No

### 2.20.10.0.0 On Delete

SetNull

### 2.20.11.0.0 On Update

NoAction


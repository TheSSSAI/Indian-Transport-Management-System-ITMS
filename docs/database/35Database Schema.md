# 1 Title

TMS High-Volume Telemetry Database

# 2 Name

tms_telemetry_db

# 3 Db Type

- timeseries

# 4 Db Technology

Amazon Timestream

# 5 Entities

## 5.1 VehicleLocation

### 5.1.1 Name

VehicleLocation

### 5.1.2 Description

Stores time-series GPS location data for each vehicle, optimized for high-volume ingestion and time-based queries. REQ-1-007, REQ-1-105. This table is a 'hypertable' in TimescaleDB or a table in Timestream.

### 5.1.3 Attributes

#### 5.1.3.1 time

##### 5.1.3.1.1 Name

time

##### 5.1.3.1.2 Type

🔹 DateTime

##### 5.1.3.1.3 Is Required

✅ Yes

##### 5.1.3.1.4 Is Primary Key

✅ Yes

##### 5.1.3.1.5 Size

0

##### 5.1.3.1.6 Is Unique

❌ No

##### 5.1.3.1.7 Constraints

- This is the primary time index for the time-series data.

##### 5.1.3.1.8 Precision

0

##### 5.1.3.1.9 Scale

0

##### 5.1.3.1.10 Is Foreign Key

❌ No

#### 5.1.3.2.0 vehicle_id

##### 5.1.3.2.1 Name

vehicle_id

##### 5.1.3.2.2 Type

🔹 INT

##### 5.1.3.2.3 Is Required

✅ Yes

##### 5.1.3.2.4 Is Primary Key

✅ Yes

##### 5.1.3.2.5 Size

0

##### 5.1.3.2.6 Is Unique

❌ No

##### 5.1.3.2.7 Constraints

- This is a 'dimension' or 'tag' for partitioning and filtering data.

##### 5.1.3.2.8 Precision

0

##### 5.1.3.2.9 Scale

0

##### 5.1.3.2.10 Is Foreign Key

✅ Yes

#### 5.1.3.3.0 latitude

##### 5.1.3.3.1 Name

latitude

##### 5.1.3.3.2 Type

🔹 DECIMAL

##### 5.1.3.3.3 Is Required

✅ Yes

##### 5.1.3.3.4 Is Primary Key

❌ No

##### 5.1.3.3.5 Size

0

##### 5.1.3.3.6 Is Unique

❌ No

##### 5.1.3.3.7 Constraints

- This is a 'measure' or 'field'.

##### 5.1.3.3.8 Precision

9

##### 5.1.3.3.9 Scale

6

##### 5.1.3.3.10 Is Foreign Key

❌ No

#### 5.1.3.4.0 longitude

##### 5.1.3.4.1 Name

longitude

##### 5.1.3.4.2 Type

🔹 DECIMAL

##### 5.1.3.4.3 Is Required

✅ Yes

##### 5.1.3.4.4 Is Primary Key

❌ No

##### 5.1.3.4.5 Size

0

##### 5.1.3.4.6 Is Unique

❌ No

##### 5.1.3.4.7 Constraints

- This is a 'measure' or 'field'.

##### 5.1.3.4.8 Precision

9

##### 5.1.3.4.9 Scale

6

##### 5.1.3.4.10 Is Foreign Key

❌ No

#### 5.1.3.5.0 speed_kmh

##### 5.1.3.5.1 Name

speed_kmh

##### 5.1.3.5.2 Type

🔹 DECIMAL

##### 5.1.3.5.3 Is Required

❌ No

##### 5.1.3.5.4 Is Primary Key

❌ No

##### 5.1.3.5.5 Size

0

##### 5.1.3.5.6 Is Unique

❌ No

##### 5.1.3.5.7 Constraints

*No items available*

##### 5.1.3.5.8 Precision

5

##### 5.1.3.5.9 Scale

2

##### 5.1.3.5.10 Is Foreign Key

❌ No

### 5.1.4.0.0 Primary Keys

- time
- vehicle_id

### 5.1.5.0.0 Unique Constraints

*No items available*

### 5.1.6.0.0 Indexes

- {'name': 'idx_vehicle_location_vehicle_time', 'columns': ['vehicle_id', 'time DESC'], 'type': 'BTree'}

## 5.2.0.0.0 GeofenceEvent

### 5.2.1.0.0 Name

GeofenceEvent

### 5.2.2.0.0 Description

Logs when a vehicle enters or exits a defined geofence. Stored in the time-series DB to correlate with location data. REQ-1-106.

### 5.2.3.0.0 Attributes

#### 5.2.3.1.0 time

##### 5.2.3.1.1 Name

time

##### 5.2.3.1.2 Type

🔹 DateTime

##### 5.2.3.1.3 Is Required

✅ Yes

##### 5.2.3.1.4 Is Primary Key

✅ Yes

##### 5.2.3.1.5 Size

0

##### 5.2.3.1.6 Is Unique

❌ No

##### 5.2.3.1.7 Constraints

*No items available*

##### 5.2.3.1.8 Precision

0

##### 5.2.3.1.9 Scale

0

##### 5.2.3.1.10 Is Foreign Key

❌ No

#### 5.2.3.2.0 vehicle_id

##### 5.2.3.2.1 Name

vehicle_id

##### 5.2.3.2.2 Type

🔹 INT

##### 5.2.3.2.3 Is Required

✅ Yes

##### 5.2.3.2.4 Is Primary Key

✅ Yes

##### 5.2.3.2.5 Size

0

##### 5.2.3.2.6 Is Unique

❌ No

##### 5.2.3.2.7 Constraints

- This is a 'dimension' or 'tag'.

##### 5.2.3.2.8 Precision

0

##### 5.2.3.2.9 Scale

0

##### 5.2.3.2.10 Is Foreign Key

✅ Yes

#### 5.2.3.3.0 geofence_id

##### 5.2.3.3.1 Name

geofence_id

##### 5.2.3.3.2 Type

🔹 INT

##### 5.2.3.3.3 Is Required

✅ Yes

##### 5.2.3.3.4 Is Primary Key

❌ No

##### 5.2.3.3.5 Size

0

##### 5.2.3.3.6 Is Unique

❌ No

##### 5.2.3.3.7 Constraints

- This is a 'dimension' or 'tag'.

##### 5.2.3.3.8 Precision

0

##### 5.2.3.3.9 Scale

0

##### 5.2.3.3.10 Is Foreign Key

✅ Yes

#### 5.2.3.4.0 event_type

##### 5.2.3.4.1 Name

event_type

##### 5.2.3.4.2 Type

🔹 VARCHAR

##### 5.2.3.4.3 Is Required

✅ Yes

##### 5.2.3.4.4 Is Primary Key

❌ No

##### 5.2.3.4.5 Size

10

##### 5.2.3.4.6 Is Unique

❌ No

##### 5.2.3.4.7 Constraints

- ENUM('Entry', 'Exit')

##### 5.2.3.4.8 Precision

0

##### 5.2.3.4.9 Scale

0

##### 5.2.3.4.10 Is Foreign Key

❌ No

### 5.2.4.0.0 Primary Keys

- time
- vehicle_id

### 5.2.5.0.0 Unique Constraints

*No items available*

### 5.2.6.0.0 Indexes

#### 5.2.6.1.0 idx_geofence_event_vehicle_time

##### 5.2.6.1.1 Name

idx_geofence_event_vehicle_time

##### 5.2.6.1.2 Columns

- vehicle_id
- time DESC

##### 5.2.6.1.3 Type

🔹 BTree

#### 5.2.6.2.0 idx_geofence_event_geofence_time

##### 5.2.6.2.1 Name

idx_geofence_event_geofence_time

##### 5.2.6.2.2 Columns

- geofence_id
- time DESC

##### 5.2.6.2.3 Type

🔹 BTree


# 1 Overview

## 1.1 Diagram Id

SEQ-UJ-006

## 1.2 Name

Driver Logs Critical Event, Triggering 'On Hold' Status

## 1.3 Description

During an 'In-Transit' trip, a driver uses their mobile portal to log a critical event (e.g., 'Accident', 'Repair'). This action automatically changes the trip's status to 'On Hold' and generates a high-priority alert for management.

## 1.4 Type

🔹 UserJourney

## 1.5 Purpose

To enable drivers to immediately report significant operational disruptions, ensuring managers are notified promptly to take necessary corrective action and to maintain an accurate trip history.

## 1.6 Complexity

Medium

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-DRV-UI
- REPO-TMS-CORE

## 1.10 Key Interactions

- Driver selects their active trip within the REPO-DRV-UI portal.
- Driver navigates to and selects the 'Log Event' or 'Report Halt' option.
- Driver chooses a critical event type from a predefined list ('Accident', 'Repair', 'Government Stoppage').
- Driver provides a mandatory text description of the event and optionally attaches a photo.
- Upon submission to REPO-TMS-CORE, Business Rule BR-005 is executed.
- The trip record's status is programmatically changed from 'In-Transit' to 'On Hold'.
- A high-priority alert is generated and displayed on the Admin/Manager dashboard.

## 1.11 Triggers

- An unforeseen critical event (accident, breakdown, etc.) occurs during a trip.

## 1.12 Outcomes

- The trip is officially paused within the system and flagged for managerial attention.
- An immutable, timestamped log of the event is created and permanently associated with the trip record.

## 1.13 Business Rules

- BR-005: The logging of critical events ('Accident', 'Repair', 'Government Stoppage') by a driver shall automatically change the trip status to 'On Hold'.

## 1.14 Error Scenarios

- The driver attempts to log an event but has no active 'In-Transit' trip.
- The driver tries to submit the event log without providing a mandatory reason.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-US-092

## 2.2 Name

Driver: Access Self-Service Training Materials

## 2.3 Description

Implementation-ready sequence diagram detailing the user journey of a driver accessing the 'Help & Training' section in their mobile portal. It covers fetching training material metadata from the Odoo backend, rendering the UI component's states, and initiating content playback/download from Amazon S3.

## 2.4 Participants

### 2.4.1 UI Component

#### 2.4.1.1 Repository Id

REPO-DRV-UI

#### 2.4.1.2 Display Name

Driver Portal UI (Browser/OWL Component)

#### 2.4.1.3 Type

🔹 UI Component

#### 2.4.1.4 Technology

Odoo Web Library (OWL) 2.0, JavaScript

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #4CAF50 |
| Stereotype | User Interface |

### 2.4.2.0 Business Logic Layer

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

TMS Core Backend

#### 2.4.2.3 Type

🔹 Business Logic Layer

#### 2.4.2.4 Technology

Odoo 18, Python 3.11

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #2196F3 |
| Stereotype | Odoo Controller/Model |

### 2.4.3.0 Object Storage

#### 2.4.3.1 Repository Id

AMAZON-S3

#### 2.4.3.2 Display Name

Amazon S3

#### 2.4.3.3 Type

🔹 Object Storage

#### 2.4.3.4 Technology

AWS S3

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #FF9800 |
| Stereotype | External Service |

## 2.5.0.0 Interactions

### 2.5.1.0 User Interaction

#### 2.5.1.1 Source Id

REPO-DRV-UI

#### 2.5.1.2 Target Id

REPO-DRV-UI

#### 2.5.1.3 Message

User with 'Driver' role taps 'Help & Training' navigation item.

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 User Interaction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

❌ No

#### 2.5.1.10 Technical Details

##### 2.5.1.10.1 Protocol

UI Event

##### 2.5.1.10.2 Method

onClick

##### 2.5.1.10.3 Parameters

Event object

##### 2.5.1.10.4 Authentication

N/A

##### 2.5.1.10.5 Error Handling

N/A

##### 2.5.1.10.6 Performance

###### 2.5.1.10.6.1 Latency

<50ms

### 2.5.2.0.0.0 State Change

#### 2.5.2.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.2.2.0.0 Target Id

REPO-DRV-UI

#### 2.5.2.3.0.0 Message

Navigate to Training Materials view. Set component state to 'loading' and render a loading indicator (e.g., spinner).

#### 2.5.2.4.0.0 Sequence Number

2

#### 2.5.2.5.0.0 Type

🔹 State Change

#### 2.5.2.6.0.0 Is Synchronous

✅ Yes

#### 2.5.2.7.0.0 Return Message



#### 2.5.2.8.0.0 Has Return

❌ No

#### 2.5.2.9.0.0 Is Activation

❌ No

#### 2.5.2.10.0.0 Technical Details

##### 2.5.2.10.1.0 Protocol

OWL Framework

##### 2.5.2.10.2.0 Method

this.state.status = 'loading'

##### 2.5.2.10.3.0 Parameters

*No items available*

##### 2.5.2.10.4.0 Authentication

N/A

##### 2.5.2.10.5.0 Error Handling

The component lifecycle hook (onWillStart) triggers the subsequent API call.

##### 2.5.2.10.6.0 Performance

###### 2.5.2.10.6.1 Latency

Immediate visual feedback required.

### 2.5.3.0.0.0 API Call

#### 2.5.3.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.3.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.3.3.0.0 Message

Asynchronously fetch list of available training materials.

#### 2.5.3.4.0.0 Sequence Number

3

#### 2.5.3.5.0.0 Type

🔹 API Call

#### 2.5.3.6.0.0 Is Synchronous

❌ No

#### 2.5.3.7.0.0 Return Message

Returns 200 OK with JSON array of training materials or an empty array if none exist. Returns 403/500 on error.

#### 2.5.3.8.0.0 Has Return

✅ Yes

#### 2.5.3.9.0.0 Is Activation

✅ Yes

#### 2.5.3.10.0.0 Technical Details

##### 2.5.3.10.1.0 Protocol

HTTP/1.1 (JSON-RPC)

##### 2.5.3.10.2.0 Method

GET /tms/training/materials

##### 2.5.3.10.3.0 Parameters

*No items available*

##### 2.5.3.10.4.0 Authentication

Requires valid Odoo session cookie. Backend controller verifies user and role.

##### 2.5.3.10.5.0 Error Handling

JS Promise `catch` block handles network errors and non-200 status codes.

##### 2.5.3.10.6.0 Performance

###### 2.5.3.10.6.1 Latency

<500ms

#### 2.5.3.11.0.0 Nested Interactions

##### 2.5.3.11.1.0 Security Check

###### 2.5.3.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.3.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.3.11.1.3 Message

Verify user session and check if user has 'Driver' role using `request.env.user.has_group('tms_management.group_tms_driver')`.

###### 2.5.3.11.1.4 Sequence Number

3.1

###### 2.5.3.11.1.5 Type

🔹 Security Check

###### 2.5.3.11.1.6 Is Synchronous

✅ Yes

###### 2.5.3.11.1.7 Return Message

Proceeds on success, returns 403 Forbidden on failure.

###### 2.5.3.11.1.8 Has Return

✅ Yes

###### 2.5.3.11.1.9 Is Activation

❌ No

###### 2.5.3.11.1.10 Technical Details

####### 2.5.3.11.1.10.1 Protocol

Odoo Framework

####### 2.5.3.11.1.10.2 Method

odoo.http.route(..., auth='user')

####### 2.5.3.11.1.10.3 Parameters

*No items available*

####### 2.5.3.11.1.10.4 Authentication

Odoo session validation.

####### 2.5.3.11.1.10.5 Error Handling

Odoo framework raises werkzeug.exceptions.Forbidden.

####### 2.5.3.11.1.10.6 Performance

######## 2.5.3.11.1.10.6.1 Latency

<20ms

##### 2.5.3.11.2.0.0.0 Database Query

###### 2.5.3.11.2.1.0.0 Source Id

REPO-TMS-CORE

###### 2.5.3.11.2.2.0.0 Target Id

REPO-TMS-CORE

###### 2.5.3.11.2.3.0.0 Message

Query `tms.training.material` model for all active records. `search_read([('active', '=', True)], ['title', 'type', 'url'])`

###### 2.5.3.11.2.4.0.0 Sequence Number

3.2

###### 2.5.3.11.2.5.0.0 Type

🔹 Database Query

###### 2.5.3.11.2.6.0.0 Is Synchronous

✅ Yes

###### 2.5.3.11.2.7.0.0 Return Message

Returns a list of Odoo record objects.

###### 2.5.3.11.2.8.0.0 Has Return

✅ Yes

###### 2.5.3.11.2.9.0.0 Is Activation

❌ No

###### 2.5.3.11.2.10.0.0 Technical Details

####### 2.5.3.11.2.10.1.0 Protocol

Odoo ORM

####### 2.5.3.11.2.10.2.0 Method

search_read

####### 2.5.3.11.2.10.3.0 Parameters

Domain filter, fields list.

####### 2.5.3.11.2.10.4.0 Authentication

N/A

####### 2.5.3.11.2.10.5.0 Error Handling

ORM may raise exceptions for database issues, caught by the controller to return a 500 error.

####### 2.5.3.11.2.10.6.0 Performance

######## 2.5.3.11.2.10.6.1 Latency

<50ms

### 2.5.4.0.0.0.0.0 State Change

#### 2.5.4.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.4.2.0.0.0.0 Target Id

REPO-DRV-UI

#### 2.5.4.3.0.0.0.0 Message

On API success, process response. If data array is not empty, set state to 'loaded'. If empty, set state to 'empty'.

#### 2.5.4.4.0.0.0.0 Sequence Number

4

#### 2.5.4.5.0.0.0.0 Type

🔹 State Change

#### 2.5.4.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.4.7.0.0.0.0 Return Message



#### 2.5.4.8.0.0.0.0 Has Return

❌ No

#### 2.5.4.9.0.0.0.0 Is Activation

❌ No

#### 2.5.4.10.0.0.0.0 Technical Details

##### 2.5.4.10.1.0.0.0 Protocol

OWL Framework

##### 2.5.4.10.2.0.0.0 Method

this.state.status = (data.length > 0) ? 'loaded' : 'empty'; this.state.materials = data;

##### 2.5.4.10.3.0.0.0 Parameters

API response payload

##### 2.5.4.10.4.0.0.0 Authentication

N/A

##### 2.5.4.10.5.0.0.0 Error Handling

N/A

##### 2.5.4.10.6.0.0.0 Performance

###### 2.5.4.10.6.1.0.0 Latency

Immediate

### 2.5.5.0.0.0.0.0 UI Render

#### 2.5.5.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.5.2.0.0.0.0 Target Id

REPO-DRV-UI

#### 2.5.5.3.0.0.0.0 Message

Render view based on state: Display list of material cards/links for 'loaded' state, or 'No materials available' message for 'empty' state. Hide loading indicator.

#### 2.5.5.4.0.0.0.0 Sequence Number

5

#### 2.5.5.5.0.0.0.0 Type

🔹 UI Render

#### 2.5.5.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.5.7.0.0.0.0 Return Message



#### 2.5.5.8.0.0.0.0 Has Return

❌ No

#### 2.5.5.9.0.0.0.0 Is Activation

❌ No

#### 2.5.5.10.0.0.0.0 Technical Details

##### 2.5.5.10.1.0.0.0 Protocol

OWL Framework

##### 2.5.5.10.2.0.0.0 Method

render()

##### 2.5.5.10.3.0.0.0 Parameters

*No items available*

##### 2.5.5.10.4.0.0.0 Authentication

N/A

##### 2.5.5.10.5.0.0.0 Error Handling

OWL handles rendering exceptions.

##### 2.5.5.10.6.0.0.0 Performance

###### 2.5.5.10.6.1.0.0 Latency

Component re-render should be <100ms

### 2.5.6.0.0.0.0.0 User Interaction

#### 2.5.6.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.6.2.0.0.0.0 Target Id

REPO-DRV-UI

#### 2.5.6.3.0.0.0.0 Message

User taps on a video tutorial item.

#### 2.5.6.4.0.0.0.0 Sequence Number

6

#### 2.5.6.5.0.0.0.0 Type

🔹 User Interaction

#### 2.5.6.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.6.7.0.0.0.0 Return Message



#### 2.5.6.8.0.0.0.0 Has Return

❌ No

#### 2.5.6.9.0.0.0.0 Is Activation

❌ No

#### 2.5.6.10.0.0.0.0 Technical Details

##### 2.5.6.10.1.0.0.0 Protocol

UI Event

##### 2.5.6.10.2.0.0.0 Method

onClick

##### 2.5.6.10.3.0.0.0 Parameters

Event object containing material URL.

##### 2.5.6.10.4.0.0.0 Authentication

N/A

##### 2.5.6.10.5.0.0.0 Error Handling

N/A

##### 2.5.6.10.6.0.0.0 Performance

###### 2.5.6.10.6.1.0.0 Latency

<50ms

### 2.5.7.0.0.0.0.0 UI Render

#### 2.5.7.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.7.2.0.0.0.0 Target Id

REPO-DRV-UI

#### 2.5.7.3.0.0.0.0 Message

Render an embedded HTML5 `<video>` player within the component, setting the `src` attribute to the material's S3 URL.

#### 2.5.7.4.0.0.0.0 Sequence Number

7

#### 2.5.7.5.0.0.0.0 Type

🔹 UI Render

#### 2.5.7.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.7.7.0.0.0.0 Return Message



#### 2.5.7.8.0.0.0.0 Has Return

❌ No

#### 2.5.7.9.0.0.0.0 Is Activation

❌ No

#### 2.5.7.10.0.0.0.0 Technical Details

##### 2.5.7.10.1.0.0.0 Protocol

DOM Manipulation

##### 2.5.7.10.2.0.0.0 Method

N/A

##### 2.5.7.10.3.0.0.0 Parameters

src URL

##### 2.5.7.10.4.0.0.0 Authentication

N/A

##### 2.5.7.10.5.0.0.0 Error Handling

The `<video>` element's `onerror` event can be handled to display a failure message.

##### 2.5.7.10.6.0.0.0 Performance

###### 2.5.7.10.6.1.0.0 Latency

Immediate rendering of the player frame.

### 2.5.8.0.0.0.0.0 Content Request

#### 2.5.8.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.8.2.0.0.0.0 Target Id

AMAZON-S3

#### 2.5.8.3.0.0.0.0 Message

Browser initiates an HTTP GET request to stream the video content from the provided S3 URL.

#### 2.5.8.4.0.0.0.0 Sequence Number

8

#### 2.5.8.5.0.0.0.0 Type

🔹 Content Request

#### 2.5.8.6.0.0.0.0 Is Synchronous

❌ No

#### 2.5.8.7.0.0.0.0 Return Message

Returns video stream chunk by chunk.

#### 2.5.8.8.0.0.0.0 Has Return

✅ Yes

#### 2.5.8.9.0.0.0.0 Is Activation

✅ Yes

#### 2.5.8.10.0.0.0.0 Technical Details

##### 2.5.8.10.1.0.0.0 Protocol

HTTPS

##### 2.5.8.10.2.0.0.0 Method

GET

##### 2.5.8.10.3.0.0.0 Parameters

Video file path

##### 2.5.8.10.4.0.0.0 Authentication

The S3 object must have public-read permissions.

##### 2.5.8.10.5.0.0.0 Error Handling

Browser handles HTTP errors (e.g., 404 Not Found), which can be caught by the video element's `onerror` event.

##### 2.5.8.10.6.0.0.0 Performance

###### 2.5.8.10.6.1.0.0 Latency

Time to first byte depends on network conditions and CDN caching.

### 2.5.9.0.0.0.0.0 User Interaction

#### 2.5.9.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.9.2.0.0.0.0 Target Id

REPO-DRV-UI

#### 2.5.9.3.0.0.0.0 Message

User taps on the Quick-Reference Guide (QRG) link.

#### 2.5.9.4.0.0.0.0 Sequence Number

9

#### 2.5.9.5.0.0.0.0 Type

🔹 User Interaction

#### 2.5.9.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.9.7.0.0.0.0 Return Message



#### 2.5.9.8.0.0.0.0 Has Return

❌ No

#### 2.5.9.9.0.0.0.0 Is Activation

❌ No

#### 2.5.9.10.0.0.0.0 Technical Details

##### 2.5.9.10.1.0.0.0 Protocol

UI Event

##### 2.5.9.10.2.0.0.0 Method

onClick

##### 2.5.9.10.3.0.0.0 Parameters

Event object containing material URL for the PDF.

##### 2.5.9.10.4.0.0.0 Authentication

N/A

##### 2.5.9.10.5.0.0.0 Error Handling

N/A

##### 2.5.9.10.6.0.0.0 Performance

###### 2.5.9.10.6.1.0.0 Latency

<50ms

### 2.5.10.0.0.0.0.0 Content Request

#### 2.5.10.1.0.0.0.0 Source Id

REPO-DRV-UI

#### 2.5.10.2.0.0.0.0 Target Id

AMAZON-S3

#### 2.5.10.3.0.0.0.0 Message

Browser opens a new tab and initiates an HTTP GET request to download/display the PDF from the S3 URL.

#### 2.5.10.4.0.0.0.0 Sequence Number

10

#### 2.5.10.5.0.0.0.0 Type

🔹 Content Request

#### 2.5.10.6.0.0.0.0 Is Synchronous

❌ No

#### 2.5.10.7.0.0.0.0 Return Message

Returns PDF content.

#### 2.5.10.8.0.0.0.0 Has Return

✅ Yes

#### 2.5.10.9.0.0.0.0 Is Activation

✅ Yes

#### 2.5.10.10.0.0.0.0 Technical Details

##### 2.5.10.10.1.0.0.0 Protocol

HTTPS

##### 2.5.10.10.2.0.0.0 Method

GET

##### 2.5.10.10.3.0.0.0 Parameters

PDF file path

##### 2.5.10.10.4.0.0.0 Authentication

The S3 object must have public-read permissions.

##### 2.5.10.10.5.0.0.0 Error Handling

Browser handles HTTP errors (e.g., 404 displays a browser error page).

##### 2.5.10.10.6.0.0.0 Performance

###### 2.5.10.10.6.1.0.0 Latency

File download time depends on size and network conditions.

## 2.6.0.0.0.0.0.0 Notes

### 2.6.1.0.0.0.0.0 Content

#### 2.6.1.1.0.0.0.0 Content

Error Handling: If the API call at step 3 fails (e.g., network error, 500 response), the UI component's state should change to 'error' and display a user-friendly error message, as per AC-006.

#### 2.6.1.2.0.0.0.0 Position

bottom

#### 2.6.1.3.0.0.0.0 Participant Id

REPO-DRV-UI

#### 2.6.1.4.0.0.0.0 Sequence Number

3

### 2.6.2.0.0.0.0.0 Content

#### 2.6.2.1.0.0.0.0 Content

Data Dependency: This entire flow depends on an Admin user having already populated the `tms.training.material` model with valid titles and S3 URLs.

#### 2.6.2.2.0.0.0.0 Position

top

#### 2.6.2.3.0.0.0.0 Participant Id

*Not specified*

#### 2.6.2.4.0.0.0.0 Sequence Number

0

## 2.7.0.0.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The Odoo controller at `/tms/training/materials` M... |
| Performance Targets | The training materials page should achieve a Large... |
| Error Handling Strategy | The OWL component must manage four distinct states... |
| Testing Considerations | 1. Unit test the Odoo controller to verify correct... |
| Monitoring Requirements | The `/tms/training/materials` endpoint should be m... |
| Deployment Considerations | Training content (videos, PDF) should be uploaded ... |


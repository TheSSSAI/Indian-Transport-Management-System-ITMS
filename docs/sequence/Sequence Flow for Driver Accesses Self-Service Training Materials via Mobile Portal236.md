# 1 Overview

## 1.1 Diagram Id

SEQ-UJ-013

## 1.2 Name

Driver Accesses Self-Service Training Materials via Mobile Portal

## 1.3 Description

A driver, needing assistance with a feature, uses their mobile portal to navigate to the 'Help & Training' section. They can then browse and watch a video tutorial on how to perform a specific task, such as submitting an expense, or download a quick-reference guide.

## 1.4 Type

🔹 UserJourney

## 1.5 Purpose

To empower drivers with on-demand, self-service training resources, thereby reducing the support burden on managers, improving driver proficiency, and increasing user adoption of the system.

## 1.6 Complexity

Low

## 1.7 Priority

🟡 Medium

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-DRV-UI
- REPO-TMS-CORE

## 1.10 Key Interactions

- Driver logs into the portal (REPO-DRV-UI) and taps the 'Help & Training' menu item.
- The OWL component in REPO-DRV-UI makes an RPC call to a REPO-TMS-CORE controller to fetch available training materials.
- The controller queries the `tms.training.material` model for active records.
- The UI receives the list of materials (titles, URLs) and displays them in a mobile-friendly list.
- The driver taps on a video title (e.g., 'How to Submit an Expense').
- The OWL component renders an HTML5 video player, setting its source to the video's S3 URL, and begins playback within the portal.

## 1.11 Triggers

- A driver needs help or a reminder on how to use a specific feature of the application.

## 1.12 Outcomes

- The driver successfully finds and views the relevant training video without needing to contact support.
- The driver downloads the Quick-Reference Guide (QRG) PDF for offline reference.

## 1.13 Business Rules

- REQ-TRN-003: Drivers shall be provided with short video tutorials and a quick-reference guide (QRG) accessible via the web portal.

## 1.14 Error Scenarios

- No training materials have been uploaded by an Admin; the portal displays a friendly message like 'No training materials are available.'
- The S3 URL for a specific video is invalid or the file is missing; the UI shows a 'This content could not be loaded' error message.

## 1.15 Integration Points

- Cloud Service: Amazon S3 (for hosting video and PDF media files).

# 2.0 Details

## 2.1 Diagram Id

SEQ-UJ-013-IMPL

## 2.2 Name

Implementation: Driver Accesses Self-Service Training Materials

## 2.3 Description

Technical sequence for a driver using the mobile-friendly web portal to access self-service training materials. The sequence covers the UI event handling, asynchronous data fetching from the backend, state management in the OWL component, and rendering of media hosted on Amazon S3. It includes detailed error handling for API failures and missing content.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

User (Actor)

#### 2.4.1.2 Display Name

Driver (User)

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Human User

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E0E0E0 |
| Stereotype | User |

### 2.4.2.0 UI Component

#### 2.4.2.1 Repository Id

REPO-DRV-UI

#### 2.4.2.2 Display Name

Driver Portal UI (OWL)

#### 2.4.2.3 Type

🔹 UI Component

#### 2.4.2.4 Technology

Odoo 18, OWL 2.0, JavaScript

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | rectangle |
| Color | #D1F2EB |
| Stereotype | Frontend |

### 2.4.3.0 Business Logic

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

TMS Core (Odoo Controller)

#### 2.4.3.3 Type

🔹 Business Logic

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | rectangle |
| Color | #A9CCE3 |
| Stereotype | Backend |

### 2.4.4.0 External Service

#### 2.4.4.1 Repository Id

Amazon S3

#### 2.4.4.2 Display Name

Amazon S3

#### 2.4.4.3 Type

🔹 External Service

#### 2.4.4.4 Technology

Cloud Object Storage

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #FAD7A0 |
| Stereotype | External Storage |

## 2.5.0.0 Interactions

### 2.5.1.0 UI Event

#### 2.5.1.1 Source Id

User (Actor)

#### 2.5.1.2 Target Id

REPO-DRV-UI

#### 2.5.1.3 Message

1. Tap 'Help & Training' menu item.

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 UI Event

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | User Interaction |
| Method | onClick |
| Parameters | Event object |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Immediate UI feedback (<100ms) |

### 2.5.2.0 State Change

#### 2.5.2.1 Source Id

REPO-DRV-UI

#### 2.5.2.2 Target Id

REPO-DRV-UI

#### 2.5.2.3 Message

2. Mount 'TrainingMaterials' OWL component and display loading state.

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 State Change

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message



#### 2.5.2.8 Has Return

❌ No

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | OWL Lifecycle |
| Method | onWillStart / onMounted |
| Parameters | None |
| Authentication | N/A |
| Error Handling | Component rendering errors are caught by OWL's err... |
| Performance | Component should render placeholder/spinner immedi... |

### 2.5.3.0 RPC

#### 2.5.3.1 Source Id

REPO-DRV-UI

#### 2.5.3.2 Target Id

REPO-TMS-CORE

#### 2.5.3.3 Message

3. Fetch training materials list.

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 RPC

#### 2.5.3.6 Is Synchronous

❌ No

#### 2.5.3.7 Return Message

4. Return JSON list of materials or empty list.

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/1.1 |
| Method | POST /tms/training_materials |
| Parameters | Payload: { jsonrpc: '2.0', method: 'call', params:... |
| Authentication | Odoo session cookie (`session_id`) required. |
| Error Handling | Client-side `try...catch` block handles network er... |
| Performance | Controller response time target < 300ms. Keep DB q... |

#### 2.5.3.11 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '3.1. Query for active training materials.', 'sequenceNumber': 3.1, 'type': 'Internal Call', 'isSynchronous': True, 'returnMessage': 'Return list of `tms.training.material` records.', 'hasReturn': True, 'isActivation': False, 'technicalDetails': {'protocol': 'Odoo ORM', 'method': "self.env['tms.training.material'].search_read([('active', '=', True)], ['title', 'type', 'url'])", 'parameters': 'Domain, Fields', 'authentication': 'Internal, based on user context.', 'errorHandling': 'Standard Odoo exceptions (e.g., AccessError) are caught and converted to a 500 HTTP response.', 'performance': 'Query must use indexed fields for optimal performance.'}}

### 2.5.4.0 State Change

#### 2.5.4.1 Source Id

REPO-DRV-UI

#### 2.5.4.2 Target Id

REPO-DRV-UI

#### 2.5.4.3 Message

5. Update state and render list of materials or 'No materials' message.

#### 2.5.4.4 Sequence Number

5

#### 2.5.4.5 Type

🔹 State Change

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message



#### 2.5.4.8 Has Return

❌ No

#### 2.5.4.9 Is Activation

❌ No

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | OWL State Management |
| Method | this.state.materials = rpcResult |
| Parameters | Array of material objects |
| Authentication | N/A |
| Error Handling | Conditional rendering (`t-if`) in OWL template han... |
| Performance | Reactive re-render should complete in <50ms. |

### 2.5.5.0 UI Event

#### 2.5.5.1 Source Id

User (Actor)

#### 2.5.5.2 Target Id

REPO-DRV-UI

#### 2.5.5.3 Message

6. Tap on a video tutorial item.

#### 2.5.5.4 Sequence Number

6

#### 2.5.5.5 Type

🔹 UI Event

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
| Protocol | User Interaction |
| Method | onClick |
| Parameters | Event object containing selected video data (e.g.,... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Immediate UI feedback. |

### 2.5.6.0 State Change

#### 2.5.6.1 Source Id

REPO-DRV-UI

#### 2.5.6.2 Target Id

REPO-DRV-UI

#### 2.5.6.3 Message

7. Render HTML5 video player component with S3 URL.

#### 2.5.6.4 Sequence Number

7

#### 2.5.6.5 Type

🔹 State Change

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
| Protocol | OWL Rendering |
| Method | Update state to show video player, set `<video src... |
| Parameters | S3 URL of the selected video. |
| Authentication | N/A |
| Error Handling | Attach `onerror` event listener to the `<video>` e... |
| Performance | Player component should render instantly. |

### 2.5.7.0 HTTP Request

#### 2.5.7.1 Source Id

REPO-DRV-UI

#### 2.5.7.2 Target Id

Amazon S3

#### 2.5.7.3 Message

8. Browser requests video stream.

#### 2.5.7.4 Sequence Number

8

#### 2.5.7.5 Type

🔹 HTTP Request

#### 2.5.7.6 Is Synchronous

❌ No

#### 2.5.7.7 Return Message

9. Stream video data chunks.

#### 2.5.7.8 Has Return

✅ Yes

#### 2.5.7.9 Is Activation

✅ Yes

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | GET |
| Parameters | URL path to video object in S3 bucket. |
| Authentication | Public read access on S3 object or pre-signed URL. |
| Error Handling | S3 returns 403/404 on invalid URL/permissions. Thi... |
| Performance | Leverages S3's high bandwidth and global distribut... |

### 2.5.8.0 UI Display

#### 2.5.8.1 Source Id

REPO-DRV-UI

#### 2.5.8.2 Target Id

User (Actor)

#### 2.5.8.3 Message

10. Play video for the driver.

#### 2.5.8.4 Sequence Number

10

#### 2.5.8.5 Type

🔹 UI Display

#### 2.5.8.6 Is Synchronous

✅ Yes

#### 2.5.8.7 Return Message



#### 2.5.8.8 Has Return

❌ No

#### 2.5.8.9 Is Activation

❌ No

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Browser Media Playback |
| Method | video.play() |
| Parameters | None |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Playback starts as soon as enough data is buffered... |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

AC-005 & AC-006: Error handling for 'No Materials' is implemented in step 5 by the UI. Error handling for 'Content Load Failure' is implemented by attaching an event listener in step 7 and reacting to S3 errors from step 8.

#### 2.6.1.2 Position

bottom

#### 2.6.1.3 Participant Id

REPO-DRV-UI

#### 2.6.1.4 Sequence Number

5

### 2.6.2.0 Content

#### 2.6.2.1 Content

REQ-TRN-003: The controller in step 3.1 is responsible for fetching the URLs for both video tutorials and the QRG document as stored in the backend model.

#### 2.6.2.2 Position

right

#### 2.6.2.3 Participant Id

REPO-TMS-CORE

#### 2.6.2.4 Sequence Number

3.1

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The controller at `/tms/training_materials` MUST b... |
| Performance Targets | P95 for `/tms/training_materials` API endpoint mus... |
| Error Handling Strategy | The OWL component is responsible for all user-faci... |
| Testing Considerations | 1. **Unit Tests (Python)**: Test the `/tms/trainin... |
| Monitoring Requirements | 1. **Metrics (Prometheus)**: Monitor the HTTP requ... |
| Deployment Considerations | The `tms.training.material` model must be created ... |


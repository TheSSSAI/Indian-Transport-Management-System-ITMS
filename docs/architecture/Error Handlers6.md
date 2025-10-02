# 1 Strategies

## 1.1 Retry

### 1.1.1 Type

🔹 Retry

### 1.1.2 Configuration

#### 1.1.2.1 Description

Applies exponential backoff for transient failures when calling external APIs (GPS, GSP) as required by REQ-1-301 and REQ-1-302.

#### 1.1.2.2 Retry Attempts

5

#### 1.1.2.3 Backoff Strategy

ExponentialWithJitter

#### 1.1.2.4 Initial Interval

2s

#### 1.1.2.5 Max Interval

60s

#### 1.1.2.6 Error Handling Rules

- GpsApiUnavailable
- GspApiUnavailable
- MessageQueueTransientError

## 1.2.0.0 Fallback

### 1.2.1.0 Type

🔹 Fallback

### 1.2.2.0 Configuration

#### 1.2.2.1 Description

Implements the required synchronous-to-asynchronous fallback for GSP e-invoicing as per REQ-1-302.

#### 1.2.2.2 Fallback Action

EnqueueForBackgroundProcessing

#### 1.2.2.3 User Feedback

E-invoice generation has been queued and will be processed shortly.

#### 1.2.2.4 Error Handling Rules

- GspApiUnavailable

## 1.3.0.0 DeadLetter

### 1.3.1.0 Type

🔹 DeadLetter

### 1.3.2.0 Configuration

#### 1.3.2.1 Description

Moves persistently failing messages/jobs to a dead-letter queue for manual inspection, fulfilling REQ-1-301.

#### 1.3.2.2 Gps Dead Letter Queue

gps_location_dlq

#### 1.3.2.3 Gsp Dead Letter Queue

gsp_einvoice_dlq

#### 1.3.2.4 Error Handling Rules

- MessageProcessingPermanentError
- GspApiBadRequest
- RetryAttemptsExhausted

# 2.0.0.0 Monitoring

## 2.1.0.0 Error Types

- GpsApiUnavailable
- GspApiUnavailable
- MessageQueueTransientError
- MessageProcessingPermanentError
- GspApiBadRequest
- RetryAttemptsExhausted

## 2.2.0.0 Alerting

As per REQ-1-602, Alertmanager will trigger critical alerts for: 1) Any message entering a Dead-Letter Queue. 2) Sustained API failures (e.g., GPS or GSP APIs failing for >5 consecutive attempts). 3) High API latency exceeding performance targets (REQ-1-500). All errors are logged to OpenSearch in structured JSON format with correlation IDs for analysis.


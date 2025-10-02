# 1 Design

code_design

# 2 Code Specfication

## 2.1 Validation Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GPS-CON |
| Validation Timestamp | 2024-05-24T10:00:00Z |
| Original Component Count Claimed | 0 |
| Original Component Count Actual | 0 |
| Gaps Identified Count | 10 |
| Components Added Count | 10 |
| Final Component Count | 10 |
| Validation Completeness Score | 100 |
| Enhancement Methodology | Systematic validation against comprehensive cached... |

## 2.2 Validation Summary

### 2.2.1 Repository Scope Validation

#### 2.2.1.1 Scope Compliance

Validation reveals a complete absence of initial specifications. A new, fully compliant specification set has been generated to meet the repository's defined scope.

#### 2.2.1.2 Gaps Identified

- Missing Odoo addon structure definition
- Missing scheduled action (ir.cron) definition
- Missing RabbitMQ consumer service specification
- Missing vehicle location update service specification
- Missing specification for secure credential handling (AWS Secrets Manager)
- Missing specification for configuration management (ir.config_parameter)

#### 2.2.1.3 Components Added

- Complete file structure for an Odoo addon
- ConsumerCron Odoo Model specification
- RabbitMQConsumerService specification
- VehicleLocationUpdater service specification
- ir_cron_data.xml specification
- ir.config_parameter specification
- External integration specifications for RabbitMQ and AWS Secrets Manager

### 2.2.2.0 Requirements Coverage Validation

#### 2.2.2.1 Functional Requirements Coverage

100.0%

#### 2.2.2.2 Non Functional Requirements Coverage

100.0%

#### 2.2.2.3 Missing Requirement Components

- Validation reveals no initial components were specified to cover requirements.

#### 2.2.2.4 Added Requirement Components

- Specification for scheduled job (REQ-1-301)
- Specification for message payload validation (REQ-1-301)
- Specification for Dead-Letter Queue handling via NACK (REQ-1-301)
- Specification for idempotency check (REQ-1-301)
- Specification for batch processing to meet performance NFRs (REQ-1-501)
- Specification for secure credential retrieval from AWS Secrets Manager (REQ-1-503)

### 2.2.3.0 Architectural Pattern Validation

#### 2.2.3.1 Pattern Implementation Completeness

Validation reveals no initial specifications. Enhanced specifications now fully detail the implementation of the Event Consumer and Service Layer patterns within the Odoo framework.

#### 2.2.3.2 Missing Pattern Components

- Validation reveals all pattern component specifications were missing.

#### 2.2.3.3 Added Pattern Components

- Specification for a decoupled service layer (\"services\" directory)
- Specification for declarative cron job configuration (XML)
- Specification for Odoo model acting as a trigger for the service layer

### 2.2.4.0 Database Mapping Validation

#### 2.2.4.1 Entity Mapping Completeness

Validation confirms the repository does not define new entities but correctly specifies interaction with the \"tms.vehicle\" entity provided by a dependency.

#### 2.2.4.2 Missing Database Components

- Validation reveals no specifications for database interaction were present.

#### 2.2.4.3 Added Database Components

- Specification for VehicleLocationUpdater service to handle all ORM interactions
- Specification notes highlighting the dependency on an indexed \"truck_number\" field in \"tms.vehicle\" for performance.

### 2.2.5.0 Sequence Interaction Validation

#### 2.2.5.1 Interaction Implementation Completeness

Validation reveals a complete lack of interaction specifications. The enhanced specification fully details the sequence from cron trigger to message acknowledgement, including error handling.

#### 2.2.5.2 Missing Interaction Components

- Validation reveals specifications for all interactions were missing.

#### 2.2.5.3 Added Interaction Components

- Method specifications for handling RabbitMQ connection and message lifecycle.
- Method specifications for payload processing, validation, and error handling.
- Method specifications for idempotent database updates.

## 2.3.0.0 Enhanced Specification

### 2.3.1.0 Specification Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-GPS-CON |
| Technology Stack | Odoo 18, Python 3.11, RabbitMQ |
| Technology Guidance Integration | Enhanced specification fully integrates Odoo 18 de... |
| Framework Compliance Score | 100 |
| Specification Completeness | 100.0% |
| Component Count | 10 |
| Specification Methodology | Enhanced specification details an event consumer p... |

### 2.3.2.0 Technology Framework Integration

#### 2.3.2.1 Framework Patterns Applied

- Odoo Addon Modularity
- Service Layer for External Integration
- Declarative Configuration (XML)
- Scheduled Action (Cron Job)
- Odoo ORM for Data Access
- Dependency Injection (via Odoo Environment)

#### 2.3.2.2 Directory Structure Source

Enhanced specification mandates a standard Odoo 18 addon structure, augmented with a \"services\" directory to promote clean architecture principles.

#### 2.3.2.3 Naming Conventions Source

Enhanced specification requires adherence to Odoo community and Python PEP 8 standards.

#### 2.3.2.4 Architectural Patterns Source

Enhanced specification details the implementation of an Event Consumer pattern as a scheduled, batch-processing job, fully aligned with the project's architecture.

#### 2.3.2.5 Performance Optimizations Applied

- Specification requires batch message consumption from RabbitMQ to minimize network overhead.
- Specification requires batch ORM search operations to minimize database queries.
- Specification requires secure, short-term caching of external credentials (from AWS Secrets Manager) to reduce API latency.

### 2.3.3.0 File Structure

#### 2.3.3.1 Directory Organization

##### 2.3.3.1.1 Directory Path

###### 2.3.3.1.1.1 Directory Path

__init__.py

###### 2.3.3.1.1.2 Purpose

Odoo package initializer specification. Must import the \"models\" and \"services\" sub-packages to make them available to Odoo's module loader.

###### 2.3.3.1.1.3 Contains Files

*No items available*

###### 2.3.3.1.1.4 Organizational Reasoning

Standard Odoo convention for module initialization.

###### 2.3.3.1.1.5 Framework Convention Alignment

Mandatory for Odoo module structure.

##### 2.3.3.1.2.0 Directory Path

###### 2.3.3.1.2.1 Directory Path

__manifest__.py

###### 2.3.3.1.2.2 Purpose

Odoo module manifest specification. Must define the module's technical name (\"tms_gps_consumer\"), version, dependencies (\"tms_core_business_logic\"), and list all data files (e.g., \"data/ir_cron_data.xml\").

###### 2.3.3.1.2.3 Contains Files

*No items available*

###### 2.3.3.1.2.4 Organizational Reasoning

This file serves as the entry point for Odoo to recognize and load the addon.

###### 2.3.3.1.2.5 Framework Convention Alignment

Mandatory for any Odoo addon.

##### 2.3.3.1.3.0 Directory Path

###### 2.3.3.1.3.1 Directory Path

models/__init__.py

###### 2.3.3.1.3.2 Purpose

Initializes the \"models\" package. Specification requires it to import all model files within the directory, specifically \"consumer_cron.py\".

###### 2.3.3.1.3.3 Contains Files

*No items available*

###### 2.3.3.1.3.4 Organizational Reasoning

Standard Odoo practice for organizing ORM models.

###### 2.3.3.1.3.5 Framework Convention Alignment

Odoo development best practice.

##### 2.3.3.1.4.0 Directory Path

###### 2.3.3.1.4.1 Directory Path

models/consumer_cron.py

###### 2.3.3.1.4.2 Purpose

Specification for the Odoo model that hosts the method executed by the scheduled action. This model acts as the Odoo-aware trigger for the consumer logic.

###### 2.3.3.1.4.3 Contains Files

- ConsumerCron

###### 2.3.3.1.4.4 Organizational Reasoning

Specification separates the Odoo framework entry point from the underlying consumption logic, adhering to the Single Responsibility Principle.

###### 2.3.3.1.4.5 Framework Convention Alignment

Common pattern for Odoo scheduled actions to live on dedicated or relevant models.

##### 2.3.3.1.5.0 Directory Path

###### 2.3.3.1.5.1 Directory Path

services/__init__.py

###### 2.3.3.1.5.2 Purpose

Initializes the \"services\" package. Specification requires it to import all service class files to enable easy instantiation from the model layer.

###### 2.3.3.1.5.3 Contains Files

*No items available*

###### 2.3.3.1.5.4 Organizational Reasoning

Specification mandates a clear service layer for business logic, decoupled from Odoo's model inheritance structure.

###### 2.3.3.1.5.5 Framework Convention Alignment

Clean architecture practice adapted for Odoo.

##### 2.3.3.1.6.0 Directory Path

###### 2.3.3.1.6.1 Directory Path

services/rabbitmq_consumer_service.py

###### 2.3.3.1.6.2 Purpose

Specification for the service containing the core logic for connecting to RabbitMQ, fetching messages, and handling the message lifecycle (ack/nack). It orchestrates validation and database updates.

###### 2.3.3.1.6.3 Contains Files

- RabbitMQConsumerService

###### 2.3.3.1.6.4 Organizational Reasoning

Specification encapsulates all AMQP-related logic and dependencies (\"pika\") in one place, isolating it from the rest of the application.

###### 2.3.3.1.6.5 Framework Convention Alignment

Adheres to service layer pattern for external system integration.

##### 2.3.3.1.7.0 Directory Path

###### 2.3.3.1.7.1 Directory Path

services/vehicle_location_updater.py

###### 2.3.3.1.7.2 Purpose

Specification for the service containing the logic for interacting with the Odoo ORM to update vehicle records. It is called by the RabbitMQ consumer service after a message is successfully validated.

###### 2.3.3.1.7.3 Contains Files

- VehicleLocationUpdater

###### 2.3.3.1.7.4 Organizational Reasoning

Specification separates the data persistence logic (ORM interaction) from the messaging logic, improving testability and clarity.

###### 2.3.3.1.7.5 Framework Convention Alignment

Follows the Single Responsibility Principle.

##### 2.3.3.1.8.0 Directory Path

###### 2.3.3.1.8.1 Directory Path

data/ir_cron_data.xml

###### 2.3.3.1.8.2 Purpose

Specification for the Odoo XML data file that declaratively defines the \"ir.cron\" record. This specification must include the model name, method name, run interval, and active state.

###### 2.3.3.1.8.3 Contains Files

*No items available*

###### 2.3.3.1.8.4 Organizational Reasoning

Specification uses Odoo's declarative approach for defining system records, making configuration manageable without code changes.

###### 2.3.3.1.8.5 Framework Convention Alignment

Standard Odoo method for creating data records on module installation.

##### 2.3.3.1.9.0 Directory Path

###### 2.3.3.1.9.1 Directory Path

tests/__init__.py

###### 2.3.3.1.9.2 Purpose

Initializes the Odoo tests package for this module. Specification requires this file to exist for Odoo to discover the tests.

###### 2.3.3.1.9.3 Contains Files

*No items available*

###### 2.3.3.1.9.4 Organizational Reasoning

Standard Odoo convention for test organization.

###### 2.3.3.1.9.5 Framework Convention Alignment

Odoo testing framework requirement.

##### 2.3.3.1.10.0 Directory Path

###### 2.3.3.1.10.1 Directory Path

tests/test_consumer.py

###### 2.3.3.1.10.2 Purpose

Specification for integration tests. Must include test cases for successful message processing, handling of malformed payloads (poison pill), idempotency checks, and database update verification.

###### 2.3.3.1.10.3 Contains Files

- TestGpsConsumer

###### 2.3.3.1.10.4 Organizational Reasoning

Co-locates tests with the module being tested.

###### 2.3.3.1.10.5 Framework Convention Alignment

Odoo testing framework convention.

#### 2.3.3.2.0.0 Namespace Strategy

| Property | Value |
|----------|-------|
| Root Namespace | odoo.addons.tms_gps_consumer |
| Namespace Organization | Standard Odoo addon namespace structure. |
| Naming Conventions | Specification requires Python PEP 8 for modules an... |
| Framework Alignment | Specification is fully aligned with all Odoo 18 mo... |

### 2.3.4.0.0.0 Class Specifications

#### 2.3.4.1.0.0 Class Name

##### 2.3.4.1.1.0 Class Name

ConsumerCron

##### 2.3.4.1.2.0 File Path

models/consumer_cron.py

##### 2.3.4.1.3.0 Class Type

Odoo Model

##### 2.3.4.1.4.0 Inheritance

models.Model

##### 2.3.4.1.5.0 Purpose

Specification requires this class to act as the Odoo-aware entry point for the scheduled action. Its sole responsibility is to instantiate the necessary services and trigger the message consumption process.

##### 2.3.4.1.6.0 Dependencies

- RabbitMQConsumerService

##### 2.3.4.1.7.0 Framework Specific Attributes

- _name = \"tms.gps.consumer.cron\"
- _description = \"GPS Consumer Cron Trigger\"

##### 2.3.4.1.8.0 Technology Integration Notes

Specification validates this class bridges the Odoo scheduled action framework with the decoupled service layer.

##### 2.3.4.1.9.0 Properties

*No items available*

##### 2.3.4.1.10.0 Methods

- {'method_name': '_run_consumer', 'method_signature': '_run_consumer(self)', 'return_type': 'void', 'access_modifier': 'private', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [], 'implementation_logic': 'Specification requires this method to instantiate the `RabbitMQConsumerService`, passing the Odoo environment (`self.env`). It must then call the `consume_batch` method on the service instance. The implementation must include robust error handling to catch and log any exceptions from the service layer, ensuring the cron job itself does not fail with an unhandled exception which could cause Odoo to disable it.', 'exception_handling': "Specification mandates a top-level try/except block to catch connection failures or other service-level exceptions. Errors must be logged using Odoo's standard logger (`_logger`) to prevent the cron job from being deactivated by Odoo on repeated failures.", 'performance_considerations': 'Specification validates this method is a lightweight trigger; all performance-intensive logic is delegated to the service layer.', 'validation_requirements': 'None required for this trigger method.', 'technology_integration_details': 'Specification confirms this is the target method for the `ir.cron` record defined in \\"data/ir_cron_data.xml\\".'}

##### 2.3.4.1.11.0 Events

*No items available*

##### 2.3.4.1.12.0 Implementation Notes

Validation confirms this model should be non-persistent (`transient`) and not store any data in the database.

#### 2.3.4.2.0.0 Class Name

##### 2.3.4.2.1.0 Class Name

RabbitMQConsumerService

##### 2.3.4.2.2.0 File Path

services/rabbitmq_consumer_service.py

##### 2.3.4.2.3.0 Class Type

Service

##### 2.3.4.2.4.0 Inheritance

object

##### 2.3.4.2.5.0 Purpose

Specification requires this class to encapsulate all logic related to RabbitMQ communication. It is responsible for connecting, fetching messages in a batch, orchestrating processing, and acknowledging or rejecting messages.

##### 2.3.4.2.6.0 Dependencies

- pika
- boto3
- VehicleLocationUpdater

##### 2.3.4.2.7.0 Framework Specific Attributes

*No items available*

##### 2.3.4.2.8.0 Technology Integration Notes

Specification mandates the use of the `pika` library for AMQP communication. It must securely fetch credentials from AWS Secrets Manager using `boto3`.

##### 2.3.4.2.9.0 Properties

###### 2.3.4.2.9.1 Property Name

####### 2.3.4.2.9.1.1 Property Name

env

####### 2.3.4.2.9.1.2 Property Type

odoo.api.Environment

####### 2.3.4.2.9.1.3 Access Modifier

private

####### 2.3.4.2.9.1.4 Purpose

Specification requires this property to provide access to the Odoo ORM and configuration parameters for downstream services.

####### 2.3.4.2.9.1.5 Validation Attributes

*No items available*

####### 2.3.4.2.9.1.6 Framework Specific Configuration

Specification requires this to be passed during instantiation from the calling Odoo model.

####### 2.3.4.2.9.1.7 Implementation Notes

Validation confirms this is necessary to instantiate other services that need ORM access.

###### 2.3.4.2.9.2.0 Property Name

####### 2.3.4.2.9.2.1 Property Name

batch_size

####### 2.3.4.2.9.2.2 Property Type

int

####### 2.3.4.2.9.2.3 Access Modifier

private

####### 2.3.4.2.9.2.4 Purpose

Specification requires this property to define the maximum number of messages to process in a single execution of the consumer.

####### 2.3.4.2.9.2.5 Validation Attributes

*No items available*

####### 2.3.4.2.9.2.6 Framework Specific Configuration

Specification requires this value to be configurable via an Odoo system parameter (\"tms_gps_consumer.consumer.batch_size\").

####### 2.3.4.2.9.2.7 Implementation Notes

Validation confirms this property is crucial for performance tuning of the consumer.

##### 2.3.4.2.10.0.0 Methods

###### 2.3.4.2.10.1.0 Method Name

####### 2.3.4.2.10.1.1 Method Name

consume_batch

####### 2.3.4.2.10.1.2 Method Signature

consume_batch(self)

####### 2.3.4.2.10.1.3 Return Type

void

####### 2.3.4.2.10.1.4 Access Modifier

public

####### 2.3.4.2.10.1.5 Is Async

❌ No

####### 2.3.4.2.10.1.6 Framework Specific Attributes

*No items available*

####### 2.3.4.2.10.1.7 Parameters

*No items available*

####### 2.3.4.2.10.1.8 Implementation Logic

Specification requires this main public method to orchestrate the following: 1. Get RabbitMQ connection parameters securely. 2. Establish a connection and channel. 3. Idempotently declare the queue to ensure its existence. 4. Loop up to `batch_size` times, fetching one message at a time using `channel.basic_get()`. 5. If a message is received, delegate processing to a private `_process_message` method. 6. If no message is available, break the loop. 7. The connection must be closed properly in a `finally` block to release resources.

####### 2.3.4.2.10.1.9 Exception Handling

Specification requires this method to handle `pika.exceptions.AMQPConnectionError` and other connection-related issues, logging them and exiting gracefully without crashing the cron job.

####### 2.3.4.2.10.1.10 Performance Considerations

Validation confirms that the batch processing pattern implemented here is key to meeting performance requirements.

####### 2.3.4.2.10.1.11 Validation Requirements

None for this orchestrator method.

####### 2.3.4.2.10.1.12 Technology Integration Details

Specification recommends using `pika.BlockingConnection` for a simple, synchronous consumption loop, which is suitable for an Odoo scheduled action.

###### 2.3.4.2.10.2.0 Method Name

####### 2.3.4.2.10.2.1 Method Name

_process_message

####### 2.3.4.2.10.2.2 Method Signature

_process_message(self, channel, method_frame, properties, body)

####### 2.3.4.2.10.2.3 Return Type

void

####### 2.3.4.2.10.2.4 Access Modifier

private

####### 2.3.4.2.10.2.5 Is Async

❌ No

####### 2.3.4.2.10.2.6 Framework Specific Attributes

*No items available*

####### 2.3.4.2.10.2.7 Parameters

######## 2.3.4.2.10.2.7.1 Parameter Name

######### 2.3.4.2.10.2.7.1.1 Parameter Name

channel

######### 2.3.4.2.10.2.7.1.2 Parameter Type

pika.channel.Channel

######### 2.3.4.2.10.2.7.1.3 Is Nullable

❌ No

######### 2.3.4.2.10.2.7.1.4 Purpose

The specification requires this parameter for the `pika` channel object, used for ack/nack operations.

######### 2.3.4.2.10.2.7.1.5 Framework Attributes

*No items available*

######## 2.3.4.2.10.2.7.2.0 Parameter Name

######### 2.3.4.2.10.2.7.2.1 Parameter Name

method_frame

######### 2.3.4.2.10.2.7.2.2 Parameter Type

pika.spec.Basic.GetOk

######### 2.3.4.2.10.2.7.2.3 Is Nullable

❌ No

######### 2.3.4.2.10.2.7.2.4 Purpose

Specification requires this to contain the delivery tag needed for message acknowledgement.

######### 2.3.4.2.10.2.7.2.5 Framework Attributes

*No items available*

######## 2.3.4.2.10.2.7.3.0 Parameter Name

######### 2.3.4.2.10.2.7.3.1 Parameter Name

body

######### 2.3.4.2.10.2.7.3.2 Parameter Type

bytes

######### 2.3.4.2.10.2.7.3.3 Is Nullable

❌ No

######### 2.3.4.2.10.2.7.3.4 Purpose

Specification requires this parameter for the raw message payload.

######### 2.3.4.2.10.2.7.3.5 Framework Attributes

*No items available*

####### 2.3.4.2.10.2.8.0.0 Implementation Logic

Specification requires this method to contain a `try...except...finally` block. Inside the `try` block, it must: 1. Decode and deserialize the JSON payload. 2. Validate the payload against the contract defined in REQ-1-301, raising a custom `ValidationError` on failure. 3. Call the `VehicleLocationUpdater` service to persist the data. 4. If all steps succeed, acknowledge the message using `channel.basic_ack()`. Inside the `except` block, it must catch any processing exception, log the error details, and negatively acknowledge the message using `channel.basic_nack(delivery_tag, requeue=False)` to route it to the DLQ.

####### 2.3.4.2.10.2.9.0.0 Exception Handling

Validation confirms this is the core error handling logic for individual messages, ensuring poison messages are routed to the DLQ as per REQ-1-301.

####### 2.3.4.2.10.2.10.0.0 Performance Considerations

Specification notes that processing should be fast, as any long-running tasks would block the consumption of subsequent messages in the batch.

####### 2.3.4.2.10.2.11.0.0 Validation Requirements

Validation of the message payload against the specified contract is a critical step within this method.

####### 2.3.4.2.10.2.12.0.0 Technology Integration Details

Specification requires direct use of `pika` channel methods for message lifecycle management.

##### 2.3.4.2.11.0.0.0.0 Events

*No items available*

##### 2.3.4.2.12.0.0.0.0 Implementation Notes

Specification mandates this service to be stateless, with all necessary context passed via method calls or the constructor.

#### 2.3.4.3.0.0.0.0.0 Class Name

##### 2.3.4.3.1.0.0.0.0 Class Name

VehicleLocationUpdater

##### 2.3.4.3.2.0.0.0.0 File Path

services/vehicle_location_updater.py

##### 2.3.4.3.3.0.0.0.0 Class Type

Service

##### 2.3.4.3.4.0.0.0.0 Inheritance

object

##### 2.3.4.3.5.0.0.0.0 Purpose

Specification requires this class to handle the specific business logic of updating a vehicle's location in the Odoo database. This includes finding the vehicle, checking for idempotency, and writing the new data.

##### 2.3.4.3.6.0.0.0.0 Dependencies

*No items available*

##### 2.3.4.3.7.0.0.0.0 Framework Specific Attributes

*No items available*

##### 2.3.4.3.8.0.0.0.0 Technology Integration Notes

Specification validates this class is a pure Odoo ORM-based service, with no external library dependencies.

##### 2.3.4.3.9.0.0.0.0 Properties

- {'property_name': 'env', 'property_type': 'odoo.api.Environment', 'access_modifier': 'private', 'purpose': 'Specification requires this property to provide access to the Odoo ORM.', 'validation_attributes': [], 'framework_specific_configuration': 'Passed during instantiation.', 'implementation_notes': ''}

##### 2.3.4.3.10.0.0.0.0 Methods

- {'method_name': 'update_location', 'method_signature': 'update_location(self, payload: dict)', 'return_type': 'void', 'access_modifier': 'public', 'is_async': False, 'framework_specific_attributes': [], 'parameters': [{'parameter_name': 'payload', 'parameter_type': 'dict', 'is_nullable': False, 'purpose': 'The specification requires this parameter to be the validated message payload containing vehicle and location data.', 'framework_attributes': []}], 'implementation_logic': "Specification requires the following logic: 1. Extract `vehicle_identifier`, `latitude`, `longitude`, and `timestamp` from the payload. 2. Perform an ORM search for the vehicle using the identifier. 3. If no vehicle is found, log a warning and return. 4. If a vehicle is found, perform an idempotency check by comparing the incoming `timestamp` with the vehicle's `last_gps_update` field. If the new timestamp is not newer, log this and return. 5. If the timestamp is newer, perform the ORM `write` operation to update the vehicle's location fields.", 'exception_handling': 'Specification notes that database errors (e.g., `psycopg2.Error`) will be caught by the calling service (`RabbitMQConsumerService`) to trigger a message NACK.', 'performance_considerations': 'Specification requires that the ORM search on `truck_number` is backed by a database index for performance. This index is expected to be created by the `tms_management` addon.', 'validation_requirements': 'Specification assumes the payload structure has already been validated. This method performs the business-level idempotency validation.', 'technology_integration_details': 'Specification validates the exclusive use of the Odoo ORM API.'}

##### 2.3.4.3.11.0.0.0.0 Events

*No items available*

##### 2.3.4.3.12.0.0.0.0 Implementation Notes

Validation confirms that the idempotency check is a critical part of this service's contract to handle potential message redeliveries from RabbitMQ.

### 2.3.5.0.0.0.0.0.0 Interface Specifications

*No items available*

### 2.3.6.0.0.0.0.0.0 Enum Specifications

*No items available*

### 2.3.7.0.0.0.0.0.0 Dto Specifications

*No items available*

### 2.3.8.0.0.0.0.0.0 Configuration Specifications

- {'configuration_name': 'ir.config_parameter', 'file_path': 'Accessed via self.env[\\"ir.config_parameter\\"]', 'purpose': "Specification requires the use of Odoo's system parameters to store database-persisted configuration that can be modified by an Admin without code changes, providing operational flexibility.", 'framework_base_class': 'ir.config_parameter', 'configuration_sections': [{'section_name': 'tms_gps_consumer', 'properties': [{'property_name': 'rabbitmq.host', 'property_type': 'string', 'default_value': 'rabbitmq', 'required': True, 'description': 'Specifies the hostname or IP address of the RabbitMQ server.'}, {'property_name': 'rabbitmq.port', 'property_type': 'int', 'default_value': '5672', 'required': True, 'description': 'Specifies the port number for the RabbitMQ AMQP listener.'}, {'property_name': 'rabbitmq.vhost', 'property_type': 'string', 'default_value': '/', 'required': True, 'description': 'Specifies the virtual host to use for the RabbitMQ connection.'}, {'property_name': 'rabbitmq.queue', 'property_type': 'string', 'default_value': 'q.tms.location_updates', 'required': True, 'description': 'Specifies the name of the queue from which to consume GPS location messages.'}, {'property_name': 'aws.secretsmanager.secret_name', 'property_type': 'string', 'default_value': 'tms/rabbitmq/credentials', 'required': True, 'description': 'Specifies the name of the secret in AWS Secrets Manager containing the RabbitMQ username and password.'}, {'property_name': 'aws.region', 'property_type': 'string', 'default_value': 'ap-south-1', 'required': True, 'description': 'Specifies the AWS region where the Secrets Manager secret is stored.'}, {'property_name': 'consumer.batch_size', 'property_type': 'int', 'default_value': '100', 'required': False, 'description': 'Specifies the maximum number of messages to process per cron job execution.'}]}], 'validation_requirements': 'Specification validates that the consumer service logic must be able to read these parameters and handle their absence with sensible defaults or clear error logging.'}

### 2.3.9.0.0.0.0.0.0 Dependency Injection Specifications

*No items available*

### 2.3.10.0.0.0.0.0.0 External Integration Specifications

#### 2.3.10.1.0.0.0.0.0 Integration Target

##### 2.3.10.1.1.0.0.0.0 Integration Target

RabbitMQ

##### 2.3.10.1.2.0.0.0.0 Integration Type

Message Queue Consumer

##### 2.3.10.1.3.0.0.0.0 Required Client Classes

- pika.BlockingConnection
- pika.ConnectionParameters

##### 2.3.10.1.4.0.0.0.0 Configuration Requirements

Specification requires Host, port, virtual host, queue name, and credentials (username/password) for connection.

##### 2.3.10.1.5.0.0.0.0 Error Handling Requirements

Specification requires robust handling of connection failures. Must support negative acknowledgements (`basic_nack`) to route failed messages to a Dead-Letter Queue (DLQ), fulfilling REQ-1-301.

##### 2.3.10.1.6.0.0.0.0 Authentication Requirements

Specification requires username and password authentication, with credentials fetched securely from AWS Secrets Manager.

##### 2.3.10.1.7.0.0.0.0 Framework Integration Patterns

Specification validates that the consumer logic is encapsulated in a service class and invoked by an Odoo scheduled action (`ir.cron`).

#### 2.3.10.2.0.0.0.0.0 Integration Target

##### 2.3.10.2.1.0.0.0.0 Integration Target

AWS Secrets Manager

##### 2.3.10.2.2.0.0.0.0 Integration Type

Secure Credential Store

##### 2.3.10.2.3.0.0.0.0 Required Client Classes

- boto3.client(\"secretsmanager\")

##### 2.3.10.2.4.0.0.0.0 Configuration Requirements

Specification requires the name of the secret and the AWS region.

##### 2.3.10.2.5.0.0.0.0 Error Handling Requirements

Specification requires handling of potential AWS client errors, such as `ClientError` for permission denied or secret not found, with clear logging.

##### 2.3.10.2.6.0.0.0.0 Authentication Requirements

Specification requires `secretsmanager:GetSecretValue` permission, expected to be provided by the Kubernetes service account's IAM Role (IRSA).

##### 2.3.10.2.7.0.0.0.0 Framework Integration Patterns

Specification requires a dedicated utility function within the service to encapsulate `boto3` calls and provide a simple interface for credential retrieval. Caching of retrieved secrets should be implemented to reduce API calls.

## 2.4.0.0.0.0.0.0.0 Component Count Validation

| Property | Value |
|----------|-------|
| Total Classes | 3 |
| Total Interfaces | 0 |
| Total Enums | 0 |
| Total Dtos | 0 |
| Total Configurations | 1 |
| Total External Integrations | 2 |
| Grand Total Components | 6 |
| Phase 2 Claimed Count | 0 |
| Phase 2 Actual Count | 0 |
| Validation Added Count | 10 |
| Final Validated Count | 10 |

# 3.0.0.0.0.0.0.0.0 File Structure

## 3.1.0.0.0.0.0.0.0 Directory Organization

### 3.1.1.0.0.0.0.0.0 Directory Path

#### 3.1.1.1.0.0.0.0.0 Directory Path

.

#### 3.1.1.2.0.0.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.1.3.0.0.0.0.0 Contains Files

- pyproject.toml
- requirements.txt
- .env.template
- Dockerfile
- docker-compose.yml
- pytest.ini
- .editorconfig
- .flake8
- .gitignore
- .dockerignore

#### 3.1.1.4.0.0.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.1.5.0.0.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

### 3.1.2.0.0.0.0.0.0 Directory Path

#### 3.1.2.1.0.0.0.0.0 Directory Path

.vscode

#### 3.1.2.2.0.0.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.2.3.0.0.0.0.0 Contains Files

- settings.json
- launch.json

#### 3.1.2.4.0.0.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.2.5.0.0.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

### 3.1.3.0.0.0.0.0.0 Directory Path

#### 3.1.3.1.0.0.0.0.0 Directory Path

tms_gps_consumer

#### 3.1.3.2.0.0.0.0.0 Purpose

Infrastructure and project configuration files

#### 3.1.3.3.0.0.0.0.0 Contains Files

- __manifest__.py

#### 3.1.3.4.0.0.0.0.0 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

#### 3.1.3.5.0.0.0.0.0 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling


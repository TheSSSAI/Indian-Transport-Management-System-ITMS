# 1 Technologies

## 1.1 Python

### 1.1.1 Id

tech-python

### 1.1.2 Name

Python

### 1.1.3 Version

3.11

### 1.1.4 Category

🔹 Backend Language

### 1.1.5 Features

- Mature ecosystem for web development
- Strong data processing libraries
- Primary language for Odoo and FastAPI development

### 1.1.6 Requirements

- REQ-1-015
- REQ-1-402

### 1.1.7 Configuration

*No data available*

### 1.1.8 License

#### 1.1.8.1 Type

🔹 Python Software Foundation License

#### 1.1.8.2 Cost

Free

## 1.2.0.0 Odoo

### 1.2.1.0 Id

tech-odoo

### 1.2.2.0 Name

Odoo

### 1.2.3.0 Version

18 Enterprise Edition

### 1.2.4.0 Category

🔹 ERP Framework

### 1.2.5.0 Features

- Integrated ORM, views, and business logic layers
- Modular architecture (addons)
- Built-in user management and security
- Comprehensive business application suite

### 1.2.6.0 Requirements

- REQ-1-002
- REQ-1-015
- REQ-1-402

### 1.2.7.0 Configuration

*No data available*

### 1.2.8.0 License

#### 1.2.8.1 Type

🔹 Odoo Enterprise Edition License

#### 1.2.8.2 Cost

Commercial

## 1.3.0.0 FastAPI

### 1.3.1.0 Id

tech-fastapi

### 1.3.2.0 Name

FastAPI

### 1.3.3.0 Version

0.111.x (latest stable)

### 1.3.4.0 Category

🔹 Microservice Framework

### 1.3.5.0 Features

- High-performance async web framework
- Automatic API documentation (Swagger UI, ReDoc)
- Type hints and data validation via Pydantic
- Ideal for lightweight, single-purpose services

### 1.3.6.0 Requirements

- REQ-1-401
- REQ-1-402

### 1.3.7.0 Configuration

*No data available*

### 1.3.8.0 License

#### 1.3.8.1 Type

🔹 MIT

#### 1.3.8.2 Cost

Free

## 1.4.0.0 Odoo Web Library (OWL)

### 1.4.1.0 Id

tech-owl

### 1.4.2.0 Name

Odoo Web Library (OWL)

### 1.4.3.0 Version

2.0

### 1.4.4.0 Category

🔹 Frontend Framework

### 1.4.5.0 Features

- Component-based architecture
- Reactive rendering for dynamic UIs
- Deep integration with the Odoo framework
- Used for custom views like the Driver Portal

### 1.4.6.0 Requirements

- REQ-1-300
- REQ-1-112
- REQ-1-402

### 1.4.7.0 Configuration

*No data available*

### 1.4.8.0 License

#### 1.4.8.1 Type

🔹 LGPL-3.0

#### 1.4.8.2 Cost

Free

## 1.5.0.0 PostgreSQL

### 1.5.1.0 Id

tech-postgresql

### 1.5.2.0 Name

PostgreSQL

### 1.5.3.0 Version

16

### 1.5.4.0 Category

🔹 Database

### 1.5.5.0 Features

- Relational database system (RDBMS)
- High reliability and data integrity
- Support for complex queries and indexing
- Native JSON and GIS (PostGIS) support

### 1.5.6.0 Requirements

- REQ-1-014
- REQ-1-402

### 1.5.7.0 Configuration

#### 1.5.7.1 Hosting

Managed via Amazon RDS for high availability and automated backups.

### 1.5.8.0 License

#### 1.5.8.1 Type

🔹 PostgreSQL License

#### 1.5.8.2 Cost

Free

## 1.6.0.0 RabbitMQ

### 1.6.1.0 Id

tech-rabbitmq

### 1.6.2.0 Name

RabbitMQ

### 1.6.3.0 Version

3.13.x (latest stable)

### 1.6.4.0 Category

🔹 Message Broker

### 1.6.5.0 Features

- Implements AMQP protocol
- Supports message queuing for asynchronous communication
- Features like exchanges, dead-letter queues (DLQ), and routing
- Decouples microservice from the Odoo monolith

### 1.6.6.0 Requirements

- REQ-1-301
- REQ-1-402

### 1.6.7.0 Configuration

#### 1.6.7.1 Hosting

Managed via Amazon MQ for simplified setup and maintenance.

### 1.6.8.0 License

#### 1.6.8.1 Type

🔹 Mozilla Public License 2.0

#### 1.6.8.2 Cost

Free

## 1.7.0.0 Redis

### 1.7.1.0 Id

tech-redis

### 1.7.2.0 Name

Redis

### 1.7.3.0 Version

7.2.x (latest stable)

### 1.7.4.0 Category

🔹 In-Memory Data Store

### 1.7.5.0 Features

- Key-value store
- Used for caching and session management in Odoo
- High-speed read/write operations
- Improves application performance

### 1.7.6.0 Requirements

- REQ-1-402

### 1.7.7.0 Configuration

#### 1.7.7.1 Hosting

Managed via Amazon ElastiCache for scalability and reliability.

### 1.7.8.0 License

#### 1.7.8.1 Type

🔹 BSD 3-Clause

#### 1.7.8.2 Cost

Free

## 1.8.0.0 Nginx

### 1.8.1.0 Id

tech-nginx

### 1.8.2.0 Name

Nginx

### 1.8.3.0 Version

1.26.x (latest stable mainline)

### 1.8.4.0 Category

🔹 Web Server / Reverse Proxy

### 1.8.5.0 Features

- High-performance HTTP server
- Reverse proxying to Odoo application servers
- Load balancing and SSL termination
- Serving static assets

### 1.8.6.0 Requirements

- REQ-1-400
- REQ-1-402

### 1.8.7.0 Configuration

*No data available*

### 1.8.8.0 License

#### 1.8.8.1 Type

🔹 2-Clause BSD-like

#### 1.8.8.2 Cost

Free

## 1.9.0.0 Docker

### 1.9.1.0 Id

tech-docker

### 1.9.2.0 Name

Docker

### 1.9.3.0 Version

26.x (latest stable)

### 1.9.4.0 Category

🔹 Containerization

### 1.9.5.0 Features

- OS-level virtualization
- Packages applications and dependencies into portable images
- Ensures consistent environments across development, staging, and production

### 1.9.6.0 Requirements

- REQ-1-014
- REQ-1-401
- REQ-1-402

### 1.9.7.0 Configuration

*No data available*

### 1.9.8.0 License

#### 1.9.8.1 Type

🔹 Apache 2.0

#### 1.9.8.2 Cost

Free

## 1.10.0.0 Amazon Elastic Kubernetes Service (EKS)

### 1.10.1.0 Id

tech-aws-eks

### 1.10.2.0 Name

Amazon Elastic Kubernetes Service (EKS)

### 1.10.3.0 Version

1.30 (latest stable)

### 1.10.4.0 Category

🔹 Container Orchestration

### 1.10.5.0 Features

- Managed Kubernetes service
- Automates deployment, scaling, and management of containerized applications
- Provides high availability and fault tolerance

### 1.10.6.0 Requirements

- REQ-1-014
- REQ-1-402

### 1.10.7.0 Configuration

*No data available*

### 1.10.8.0 License

#### 1.10.8.1 Type

🔹 Commercial

#### 1.10.8.2 Cost

Usage-based

## 1.11.0.0 Amazon S3

### 1.11.1.0 Id

tech-aws-s3

### 1.11.2.0 Name

Amazon S3

### 1.11.3.0 Version

N/A

### 1.11.4.0 Category

🔹 Object Storage

### 1.11.5.0 Features

- Scalable object storage for unstructured data
- Durable storage for file attachments (PODs, receipts)
- Secure access control policies

### 1.11.6.0 Requirements

- REQ-1-014
- REQ-1-402

### 1.11.7.0 Configuration

*No data available*

### 1.11.8.0 License

#### 1.11.8.1 Type

🔹 Commercial

#### 1.11.8.2 Cost

Usage-based

## 1.12.0.0 AWS Secrets Manager

### 1.12.1.0 Id

tech-aws-secrets-manager

### 1.12.2.0 Name

AWS Secrets Manager

### 1.12.3.0 Version

N/A

### 1.12.4.0 Category

🔹 Secrets Management

### 1.12.5.0 Features

- Securely stores and manages secrets (API keys, passwords)
- Enables dynamic injection of secrets into runtime environments
- Prevents hardcoding of sensitive credentials

### 1.12.6.0 Requirements

- REQ-1-503
- REQ-1-402

### 1.12.7.0 Configuration

*No data available*

### 1.12.8.0 License

#### 1.12.8.1 Type

🔹 Commercial

#### 1.12.8.2 Cost

Usage-based

## 1.13.0.0 AWS API Gateway

### 1.13.1.0 Id

tech-aws-api-gateway

### 1.13.2.0 Name

AWS API Gateway

### 1.13.3.0 Version

N/A

### 1.13.4.0 Category

🔹 API Management

### 1.13.5.0 Features

- Creates, publishes, and secures APIs
- Provides a secure endpoint for the GPS ingestion microservice
- Handles traffic management, authorization, and monitoring

### 1.13.6.0 Requirements

- REQ-1-400
- REQ-1-402

### 1.13.7.0 Configuration

*No data available*

### 1.13.8.0 License

#### 1.13.8.1 Type

🔹 Commercial

#### 1.13.8.2 Cost

Usage-based

## 1.14.0.0 Terraform

### 1.14.1.0 Id

tech-terraform

### 1.14.2.0 Name

Terraform

### 1.14.3.0 Version

1.8.x (latest stable)

### 1.14.4.0 Category

🔹 Infrastructure as Code (IaC)

### 1.14.5.0 Features

- Defines and provisions infrastructure using declarative configuration files
- Enables versioning and automation of cloud infrastructure
- Manages AWS resources (EKS, RDS, S3, etc.)

### 1.14.6.0 Requirements

- REQ-1-402

### 1.14.7.0 Configuration

*No data available*

### 1.14.8.0 License

#### 1.14.8.1 Type

🔹 Business Source License 1.1

#### 1.14.8.2 Cost

Free

## 1.15.0.0 GitHub Actions

### 1.15.1.0 Id

tech-github-actions

### 1.15.2.0 Name

GitHub Actions

### 1.15.3.0 Version

N/A

### 1.15.4.0 Category

🔹 CI/CD

### 1.15.5.0 Features

- Automates software workflows directly within GitHub
- Builds, tests, and deploys code
- Integrates with code quality and testing tools

### 1.15.6.0 Requirements

- REQ-1-402
- REQ-1-504

### 1.15.7.0 Configuration

*No data available*

### 1.15.8.0 License

#### 1.15.8.1 Type

🔹 Commercial

#### 1.15.8.2 Cost

Usage-based (includes free tier)

## 1.16.0.0 Pytest

### 1.16.1.0 Id

tech-pytest

### 1.16.2.0 Name

Pytest

### 1.16.3.0 Version

8.2.x (latest stable)

### 1.16.4.0 Category

🔹 Testing Framework

### 1.16.5.0 Features

- Powerful and simple framework for writing Python tests
- Extensive plugin ecosystem (e.g., pytest-cov for coverage)
- Used for unit testing custom business logic

### 1.16.6.0 Requirements

- REQ-1-504
- REQ-1-402

### 1.16.7.0 Configuration

*No data available*

### 1.16.8.0 License

#### 1.16.8.1 Type

🔹 MIT

#### 1.16.8.2 Cost

Free

## 1.17.0.0 Black, Flake8, isort

### 1.17.1.0 Id

tech-code-quality-tools

### 1.17.2.0 Name

Black, Flake8, isort

### 1.17.3.0 Version

latest stable

### 1.17.4.0 Category

🔹 Code Quality

### 1.17.5.0 Features

- Automated code formatting (Black)
- Code linting and style guide enforcement (Flake8)
- Automatic sorting of imports (isort)
- Ensures consistent and readable codebase

### 1.17.6.0 Requirements

- REQ-1-402

### 1.17.7.0 Configuration

*No data available*

### 1.17.8.0 License

#### 1.17.8.1 Type

🔹 MIT

#### 1.17.8.2 Cost

Free

## 1.18.0.0 Prometheus

### 1.18.1.0 Id

tech-prometheus

### 1.18.2.0 Name

Prometheus

### 1.18.3.0 Version

2.53.x (latest stable)

### 1.18.4.0 Category

🔹 Monitoring & Alerting

### 1.18.5.0 Features

- Time-series database for collecting metrics
- Powerful query language (PromQL)
- Scrapes metrics from application and infrastructure endpoints

### 1.18.6.0 Requirements

- REQ-1-602

### 1.18.7.0 Configuration

*No data available*

### 1.18.8.0 License

#### 1.18.8.1 Type

🔹 Apache 2.0

#### 1.18.8.2 Cost

Free

## 1.19.0.0 Grafana

### 1.19.1.0 Id

tech-grafana

### 1.19.2.0 Name

Grafana

### 1.19.3.0 Version

11.1.x (latest stable)

### 1.19.4.0 Category

🔹 Monitoring & Visualization

### 1.19.5.0 Features

- Data visualization and dashboarding tool
- Integrates with Prometheus (metrics) and OpenSearch (logs)
- Creates dashboards for monitoring system health and KPIs

### 1.19.6.0 Requirements

- REQ-1-602

### 1.19.7.0 Configuration

*No data available*

### 1.19.8.0 License

#### 1.19.8.1 Type

🔹 AGPL-3.0

#### 1.19.8.2 Cost

Free

## 1.20.0.0 Fluent Bit

### 1.20.1.0 Id

tech-fluentbit

### 1.20.2.0 Name

Fluent Bit

### 1.20.3.0 Version

3.0.x (latest stable)

### 1.20.4.0 Category

🔹 Log Collection

### 1.20.5.0 Features

- Lightweight and high-performance log processor and forwarder
- Collects logs from all containers
- Forwards structured logs to OpenSearch

### 1.20.6.0 Requirements

- REQ-1-602

### 1.20.7.0 Configuration

*No data available*

### 1.20.8.0 License

#### 1.20.8.1 Type

🔹 Apache 2.0

#### 1.20.8.2 Cost

Free

## 1.21.0.0 OpenSearch

### 1.21.1.0 Id

tech-opensearch

### 1.21.2.0 Name

OpenSearch

### 1.21.3.0 Version

2.15.x (latest stable)

### 1.21.4.0 Category

🔹 Log Aggregation & Search

### 1.21.5.0 Features

- Distributed search and analytics engine
- Centralized storage for application and system logs
- Enables searching, analyzing, and visualizing log data

### 1.21.6.0 Requirements

- REQ-1-602

### 1.21.7.0 Configuration

*No data available*

### 1.21.8.0 License

#### 1.21.8.1 Type

🔹 Apache 2.0

#### 1.21.8.2 Cost

Free

# 2.0.0.0 Configuration

*No data available*


# TMS GPS Ingestion Service

This repository contains the standalone, decoupled microservice responsible for ingesting real-time GPS data for the Transport Management System (TMS).

## Overview

Built with FastAPI for high performance, its function is to poll a third-party GPS provider's API, validate the received data against a strict contract, and publish it as a standardized `VehicleLocationUpdated` event to a RabbitMQ message queue.

This service is a critical component of the system's real-time tracking feature, designed for high throughput and resilience. Its isolation from the core Odoo monolith is a key architectural decision to prevent performance degradation of the main application from high-frequency I/O operations.

### Architectural Context

- **Pattern**: Decoupled Microservice, Event Producer
- **Framework**: FastAPI (Python 3.11)
- **Communication**: Asynchronous (AMQP via RabbitMQ)
- **Deployment**: Docker container on Amazon EKS

This service fulfills the requirements specified in `REQ-1-013`, `REQ-1-301`, and `REQ-1-401` of the System Requirements Specification.

## Prerequisites

- Docker and Docker Compose
- Python 3.11 (for local non-Docker development)
- Poetry (for managing Python dependencies)

## Local Development Setup

The most straightforward way to run the service locally is using Docker Compose, which will spin up both the FastAPI application and a RabbitMQ instance.

### 1. Configure Environment Variables

Create a `.env` file in the project root by copying the example file:

```bash
cp .env.example .env
```

Now, edit the `.env` file with your local configuration. For local development, the default RabbitMQ URL should work. You will need to provide a valid URL and API key for the GPS provider.

```
# .env
LOG_LEVEL=DEBUG
GPS_PROVIDER_API_URL=https://your-provider.api/locations
GPS_PROVIDER_API_KEY="your-secret-api-key"
POLLING_INTERVAL_SECONDS=15
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
# ... other variables
```

### 2. Run with Docker Compose

From the project root, run the following command:

```bash
docker-compose up --build
```

This will:
1.  Build the Docker image for the `gps-ingestion-service`.
2.  Start a RabbitMQ container.
3.  Start the `gps-ingestion-service` container, which will begin polling the GPS provider.

The service will be available at `http://localhost:8000`.

-   **Health Check**: `http://localhost:8000/health`
-   **Metrics**: `http://localhost:8000/metrics`
-   **RabbitMQ Management UI**: `http://localhost:15672` (user: `guest`, pass: `guest`)

## Running Tests

Tests are written using `pytest`. You can run them inside the Docker container or in a local virtual environment.

### Running tests via Docker Compose

```bash
docker-compose exec gps-ingestion-service poetry run pytest
```

### Running tests locally

1.  Install dependencies:
    ```bash
    poetry install
    ```
2.  Run tests:
    ```bash
    poetry run pytest
    ```

## Code Quality

This project uses `black` for formatting, `isort` for import sorting, and `flake8` for linting.

-   **Check formatting**: `poetry run black --check .`
-   **Apply formatting**: `poetry run black .`
-   **Check imports**: `poetry run isort --check .`
-   **Apply import sorting**: `poetry run isort .`
-   **Run linter**: `poetry run flake8 .`

## Building for Production

To build the standalone Docker image for production deployment, run:

```bash
docker build -t tms-gps-ingestion-service:latest .
```

The resulting image is optimized for size and security, ready to be pushed to a container registry like Amazon ECR. In a production environment (EKS), environment variables will be injected via Kubernetes secrets or a ConfigMap, and the `GPS_PROVIDER_API_KEY` will typically be an ARN for a secret in AWS Secrets Manager.
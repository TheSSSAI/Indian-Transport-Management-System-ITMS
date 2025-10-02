# Stage 1: Build stage with development dependencies
FROM python:3.11-slim as builder

WORKDIR /opt/poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry==1.8.2

COPY pyproject.toml poetry.lock ./

# Install dependencies, excluding development ones, into the project's venv
RUN poetry install --no-dev --no-root


# Stage 2: Final production stage
FROM python:3.11-slim as final

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Set path to the virtual environment created in the build stage
    PATH="/opt/poetry/.venv/bin:$PATH"

# Create a non-root user for security
RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

WORKDIR /app

# Copy the virtual environment with dependencies from the build stage
COPY --from=builder /opt/poetry/.venv .venv

# Copy the application source code
COPY ./src ./src

# Change ownership of the application directory
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose the port the application will run on
EXPOSE 80

# Command to run the application using Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
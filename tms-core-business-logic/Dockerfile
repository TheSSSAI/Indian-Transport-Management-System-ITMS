# Use a multi-stage build to keep the final image small and secure.
# Stage 1: Builder - Install system dependencies and Python packages
FROM python:3.11-slim-bookworm as builder

# Set environment variables to prevent interactive prompts during package installation
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install essential system dependencies for Odoo
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libxslt1-dev \
    libzip-dev \
    libldap2-dev \
    libsasl2-dev \
    libjpeg62-turbo-dev \
    libffi-dev \
    libxml2-dev \
    wkhtmltopdf && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements files
COPY requirements.txt requirements-dev.txt /app/
WORKDIR /app

# Install Python dependencies into the virtual environment
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Image - Copy only what's necessary
FROM python:3.11-slim-bookworm

LABEL maintainer="Master Software Architect"
LABEL description="Production image for TMS Odoo Core Business Logic"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    ODOO_RC=/etc/odoo/odoo.conf

# Install runtime system dependencies (fewer than the builder)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    libxslt1.1 \
    libzip4 \
    libldap-2.5-0 \
    libsasl2-2 \
    libjpeg62-turbo \
    libffi8 \
    libxml2 \
    wkhtmltopdf && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user for Odoo
RUN useradd -m -d /home/odoo -r -s /bin/bash odoo

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy Odoo configuration template
COPY odoo.conf.template /etc/odoo/

# Copy the custom addons
COPY --chown=odoo:odoo ./tms_core /mnt/extra-addons/tms_core

# Set up directories and permissions
RUN mkdir -p /var/lib/odoo && \
    chown -R odoo:odoo /var/lib/odoo /mnt/extra-addons /etc/odoo

# Switch to the non-root user
USER odoo

# Expose the Odoo port
EXPOSE 8069
EXPOSE 8072 # Longpolling port

# Set the default command to run Odoo
CMD ["odoo", "--config", "/etc/odoo/odoo.conf"]
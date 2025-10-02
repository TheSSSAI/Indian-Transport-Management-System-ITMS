# Use the official Odoo 18 image as the base
FROM odoo:18.0

# Set environment variables to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install system dependencies
USER root

# Install system dependencies required for Python packages and development
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    # Add other system dependencies here if needed
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
# Copy requirements first to leverage Docker layer caching
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Copy Odoo configuration file
# This can be overridden by docker-compose volumes or environment variables
COPY ./odoo.conf /etc/odoo/odoo.conf
RUN chown odoo:odoo /etc/odoo/odoo.conf

# Copy custom addons into the designated addons path
# Note: In a dev setup, this is often handled by docker-compose volumes
# but we include it here for a self-contained production-ready image.
COPY ./tms_gps_consumer /mnt/extra-addons/tms_gps_consumer
# Add other dependent custom addons here if they exist in the repo
# e.g. COPY ./tms_core_business_logic /mnt/extra-addons/tms_core_business_logic
RUN chown -R odoo:odoo /mnt/extra-addons

# Expose Odoo port and debugpy port
EXPOSE 8069
EXPOSE 5678

# Switch back to the odoo user
USER odoo

# The CMD is inherited from the base odoo image, which is `["odoo"]`.
# It will automatically use the /etc/odoo/odoo.conf file.
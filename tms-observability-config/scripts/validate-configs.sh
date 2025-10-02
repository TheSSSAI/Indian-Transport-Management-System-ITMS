#!/bin/bash

# ==============================================================================
# TMS Observability Configuration Validator
#
# This script validates all configuration files within the tms-observability-config
# repository to ensure syntactic correctness and adherence to tool-specific schemas.
# It is designed to be run locally by developers and in the CI/CD pipeline
# before any changes are merged.
#
# Exits with a non-zero status code if any validation fails.
#
# Prerequisites:
#   - promtool (part of Prometheus)
#   - fluent-bit
#   - yamllint
#   - jq
# ==============================================================================

# --- Strict Mode ---
# Exit immediately if a command exits with a non-zero status.
# Treat unset variables as an error.
# Pipelines fail if any command fails, not just the last one.
set -euo pipefail

# --- Color Definitions ---
COLOR_GREEN='\033[0;32m'
COLOR_YELLOW='\033[0;33m'
COLOR_RED='\033[0;31m'
COLOR_RESET='\033[0m'

# --- Helper Functions ---
function info() {
    echo -e "${COLOR_YELLOW}[INFO] $1${COLOR_RESET}"
}

function success() {
    echo -e "${COLOR_GREEN}[SUCCESS] $1${COLOR_RESET}"
}

function error() {
    echo -e "${COLOR_RED}[ERROR] $1${COLOR_RESET}" >&2
    exit 1
}

function check_command() {
    if ! command -v "$1" &> /dev/null; then
        error "Required command '$1' is not installed or not in PATH. Please install it to proceed."
    fi
}

# --- Validation Functions ---

function validate_yaml_files() {
    info "Running yamllint on all YAML files..."
    if ! yamllint . ; then
        error "YAMLLint found issues. Please fix the files listed above."
    fi
    success "All YAML files passed yamllint."
}

function validate_prometheus_configs() {
    info "Validating Prometheus main configuration and Alertmanager configuration..."
    if ! promtool check config prometheus.yml; then
        error "Prometheus main configuration (prometheus.yml) is invalid."
    fi
    if ! promtool check config prometheus/alertmanager/alertmanager.yml; then
        error "Alertmanager configuration (alertmanager.yml) is invalid."
    fi
    success "Prometheus and Alertmanager main configurations are valid."
}

function validate_prometheus_rules() {
    info "Validating all Prometheus rule files (*.rules.yml)..."
    local rule_files
    rule_files=$(find prometheus/rules -type f -name "*.rules.yml")

    if [ -z "$rule_files" ]; then
        info "No Prometheus rule files found to validate."
        return
    fi

    for file in $rule_files; do
        info "Checking rule file: $file"
        if ! promtool check rules "$file"; then
            error "Validation failed for Prometheus rule file: $file"
        fi
    done
    success "All Prometheus rule files are valid."
}

function validate_grafana_dashboards() {
    info "Validating all Grafana dashboard JSON files (*.json)..."
    local dashboard_files
    dashboard_files=$(find grafana/dashboards -type f -name "*.json")

    if [ -z "$dashboard_files" ]; then
        info "No Grafana dashboard JSON files found to validate."
        return
    fi

    for file in $dashboard_files; do
        info "Checking JSON syntax for dashboard: $file"
        if ! jq . "$file" > /dev/null; then
            error "Invalid JSON syntax in Grafana dashboard file: $file"
        fi
    done
    success "All Grafana dashboard JSON files have valid syntax."
}

function validate_fluentbit_configs() {
    info "Validating Fluent Bit configuration pipeline..."
    # Fluent Bit's --dry-run validates the main config and all its @INCLUDE directives.
    if ! fluent-bit --dry-run --quiet -c fluent-bit.conf; then
        error "Fluent Bit configuration validation failed. Check the main config and included files."
    fi
    success "Fluent Bit configuration pipeline is valid."
}

# --- Main Execution ---

function main() {
    info "Starting TMS Observability Configuration Validation..."
    
    # Go to the repository root directory to ensure paths are correct
    cd "$(dirname "$0")/.."

    # Check for presence of required tools
    check_command "yamllint"
    check_command "promtool"
    check_command "jq"
    check_command "fluent-bit"
    
    # Run all validation steps
    validate_yaml_files
    validate_prometheus_configs
    validate_prometheus_rules
    validate_grafana_dashboards
    validate_fluentbit_configs

    success "All observability configurations have been successfully validated!"
}

# --- Script Entrypoint ---
main
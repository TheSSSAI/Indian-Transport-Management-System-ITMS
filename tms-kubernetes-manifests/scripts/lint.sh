#!/usr/bin/env bash
#
# scripts/lint.sh
#
# This script performs static analysis and linting on the Kubernetes manifests.
# It ensures that all YAML files adhere to defined style guides and that all
# Helm charts follow best practices. This script is a critical quality gate
# in the CI/CD pipeline.

set -euo pipefail

# --- Configuration ---
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "${SCRIPT_DIR}/.." && pwd)

YAMLLINT_CONFIG="${REPO_ROOT}/.yamllint"

# --- Main Logic ---
main() {
    echo -e "${YELLOW}Running YAML and Helm Chart Linter...${NC}"

    local failed=0

    # Step 1: Lint all YAML files
    lint_yaml_files || failed=1
    
    # Step 2: Lint all Helm charts
    lint_helm_charts || failed=1

    if [[ ${failed} -eq 0 ]]; then
        echo -e "\n${GREEN}✔ All YAML files and Helm charts passed linting.${NC}"
        exit 0
    else
        echo -e "\n${RED}✖ Linting failed. Please check the errors above.${NC}"
        exit 1
    fi
}

# --- Helper Functions ---

# lint_yaml_files
#
# Uses yamllint to check all .yaml and .yml files in the repository for
# syntax correctness and style consistency based on the .yamllint config file.
lint_yaml_files() {
    echo -e "\n${YELLOW}Running yamllint on all YAML files...${NC}"
    if ! command -v yamllint &> /dev/null; then
        echo -e "${RED}Error: yamllint is not installed. Please install it to continue.${NC}"
        return 1
    fi

    if [[ ! -f "${YAMLLINT_CONFIG}" ]]; then
        echo -e "${RED}Error: .yamllint config file not found at ${YAMLLINT_CONFIG}${NC}"
        return 1
    fi

    if yamllint --config-file "${YAMLLINT_CONFIG}" "${REPO_ROOT}"; then
        echo -e "${GREEN}✔ YAML linting passed.${NC}"
        return 0
    else
        echo -e "${RED}✖ YAML linting failed.${NC}"
        return 1
    fi
}

# lint_helm_charts
#
# Finds all Helm charts in the 'charts/' directory and runs 'helm lint' on each.
# This validates the chart's structure and templates against Helm best practices.
lint_helm_charts() {
    echo -e "\n${YELLOW}Running helm lint on all charts...${NC}"
    if ! command -v helm &> /dev/null; then
        echo -e "${RED}Error: helm is not installed. Please install it to continue.${NC}"
        return 1
    fi

    local charts_dir="${REPO_ROOT}/charts"
    if [[ ! -d "${charts_dir}" ]]; then
        echo -e "${YELLOW}No 'charts' directory found. Skipping helm lint.${NC}"
        return 0
    fi
    
    local chart_lint_failed=0
    
    # Use find to locate all Chart.yaml files and lint their parent directories
    find "${charts_dir}" -name "Chart.yaml" | while read -r chart_file; do
        local chart_path
        chart_path=$(dirname "${chart_file}")
        echo -e "\nLinting chart: ${YELLOW}${chart_path}${NC}"
        
        if helm lint "${chart_path}"; then
            echo -e "${GREEN}✔ Helm lint passed for ${chart_path}${NC}"
        else
            echo -e "${RED}✖ Helm lint failed for ${chart_path}${NC}"
            chart_lint_failed=1
        fi
    done
    
    # Handle subshell variable issue
    if [[ ${chart_lint_failed} -eq 1 ]]; then
        return 1
    fi

    echo -e "\n${GREEN}✔ All Helm charts passed linting.${NC}"
    return 0
}

# --- Execution ---
main "$@"
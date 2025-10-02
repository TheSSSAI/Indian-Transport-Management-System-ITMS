#!/usr/bin/env bash
#
# scripts/validate.sh
#
# This script validates the Kustomize overlays by attempting to build them.
# A successful build confirms that the base, components, and patches are
# syntactically correct and can be rendered into valid Kubernetes manifests.
# This is a critical check to prevent deployment failures due to configuration errors.

set -euo pipefail

# --- Configuration ---
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "${SCRIPT_DIR}/.." && pwd)

# --- Main Logic ---
main() {
    echo -e "${YELLOW}Running Kustomize Build Validator...${NC}"

    if ! command -v kustomize &> /dev/null; then
        echo -e "${RED}Error: kustomize is not installed. Please install it to continue.${NC}"
        exit 1
    fi

    local failed=0

    validate_overlays || failed=1

    if [[ ${failed} -eq 0 ]]; then
        echo -e "\n${GREEN}✔ All Kustomize overlays built successfully.${NC}"
        exit 0
    else
        echo -e "\n${RED}✖ Kustomize validation failed. Please check the errors above.${NC}"
        exit 1
    fi
}

# validate_overlays
#
# Finds all Kustomize overlays in the 'overlays/' directory and runs
# 'kustomize build' on each. The output is discarded, as we only care
# about the exit code. A non-zero exit code will cause the script to fail.
validate_overlays() {
    local overlays_dir="${REPO_ROOT}/overlays"

    if [[ ! -d "${overlays_dir}" ]]; then
        echo -e "${YELLOW}No 'overlays' directory found. Skipping validation.${NC}"
        return 0
    fi
    
    local validation_failed=0

    # Find all kustomization.yaml files within the overlays directory
    find "${overlays_dir}" -name "kustomization.yaml" | while read -r kustomization_file; do
        local overlay_path
        overlay_path=$(dirname "${kustomization_file}")
        
        echo -e "\nValidating overlay: ${YELLOW}${overlay_path}${NC}"
        
        # We pipe to /dev/null because we only care about the exit code.
        # 'set -e' will cause the script to exit if kustomize build fails.
        if kustomize build "${overlay_path}" > /dev/null; then
            echo -e "${GREEN}✔ Build successful for ${overlay_path}${NC}"
        else
            echo -e "${RED}✖ Build failed for ${overlay_path}${NC}"
            # Use a file to communicate failure out of the subshell
            touch /tmp/kustomize_failed
        fi
    done
    
    if [ -f /tmp/kustomize_failed ]; then
        rm /tmp/kustomize_failed
        return 1
    fi

    return 0
}

# --- Execution ---
main "$@"
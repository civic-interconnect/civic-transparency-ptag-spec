#!/usr/bin/env python
"""Simple OpenAPI validation for pre-commit."""

import sys
import yaml
from pathlib import Path


def validate_openapi_file(api_path):
    """Validate OpenAPI file."""
    try:
        with open(api_path, "r") as f:
            spec = yaml.safe_load(f)

        # Basic checks
        if "openapi" not in spec:
            print(f"ERROR: {api_path}: Missing openapi field")
            return False

        if "info" not in spec or "version" not in spec["info"]:
            print(f"ERROR: {api_path}: Missing info.version")
            return False

        version = spec["info"]["version"]
        print(f"SUCCESS: {api_path}: Valid (version {version})")
        return True

    except yaml.YAMLError as e:
        print(f"ERROR: {api_path}: Invalid YAML - {e}")
        return False
    except Exception as e:
        print(f"ERROR: {api_path}: Error - {e}")
        return False


def main():
    schema_dir = Path("src/ci/transparency/spec/schemas")
    api_files = list(schema_dir.glob("*.openapi.yaml"))

    if not api_files:
        print("No OpenAPI files found")
        return

    all_valid = True
    for api_file in api_files:
        if not validate_openapi_file(api_file):
            all_valid = False

    if not all_valid:
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Simple OpenAPI validation for pre-commit."""

from pathlib import Path
import sys

import yaml


def validate_openapi_file(api_path: str):
    """Validate OpenAPI file."""
    try:
        with Path(api_path).open() as f:
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
    """Find and validate all OpenAPI files in the schema directory."""
    schema_dir = Path("src/ci/transparency/ptag/spec/schemas")
    api_files = list(schema_dir.glob("*.openapi.yaml"))

    if not api_files:
        print("No OpenAPI files found")
        return

    all_valid = True
    for api_file in api_files:
        if not validate_openapi_file(str(api_file)):
            all_valid = False

    if not all_valid:
        sys.exit(1)


if __name__ == "__main__":
    main()

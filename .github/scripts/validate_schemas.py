#!/usr/bin/env python
"""Simple JSON Schema validation for pre-commit."""

import json
from pathlib import Path
import sys


def validate_schema_file(schema_path: str | Path):
    """Validate a single schema file."""
    try:
        with Path(schema_path).open() as f:
            schema = json.load(f)

        # Basic checks
        if "$schema" not in schema:
            print(f"ERROR: {schema_path}: Missing $schema")
            return False

        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            print(f"ERROR: {schema_path}: Wrong $schema version")
            return False

        # Check required fields exist
        required_fields = ["$id", "title", "type"]
        for field in required_fields:
            if field not in schema:
                print(f"ERROR: {schema_path}: Missing {field}")
                return False

        print(f"SUCCESS: {schema_path}: Valid")
        return True

    except json.JSONDecodeError as e:
        print(f"ERROR: {schema_path}: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"ERROR: {schema_path}: Error - {e}")
        return False


def main():
    """Validate all JSON schema files in the specified directory."""
    schema_dir = Path("src/ci/transparency/ptag/spec/schemas")
    schema_files = list(schema_dir.glob("*.schema.json"))

    if not schema_files:
        print("No schema files found")
        return

    all_valid = True
    for schema_file in schema_files:
        if not validate_schema_file(schema_file):
            all_valid = False

    if not all_valid:
        sys.exit(1)


if __name__ == "__main__":
    main()

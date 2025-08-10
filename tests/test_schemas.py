# tests/test_schemas.py
import json
import glob
import pathlib
from jsonschema import Draft7Validator, ValidationError


def test_json_schemas_are_valid():
    """
    Test that all JSON schemas in the schemas directory are valid.
    """
    schema_files = glob.glob(str(pathlib.Path(__file__).parents[1] / "src" / "ci" / "transparency" / "spec" / "schemas" / "*.json"))
    for schema_file in schema_files:
        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)
        try:
            Draft7Validator.check_schema(schema)
        except ValidationError as e:
            raise AssertionError(f"Schema {schema_file} is invalid: {e.message}")
        except Exception as e:
            raise AssertionError(
                f"An error occurred while validating schema {schema_file}: {str(e)}"
            )
        print(f"Schema {schema_file} is valid.")

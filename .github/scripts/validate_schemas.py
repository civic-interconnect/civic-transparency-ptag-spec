# .github/scripts/validate_schemas.py
import json
import sys
import glob
from jsonschema import Draft7Validator

bad = False
for path in glob.glob("spec/schemas/*.schema.json"):
    with open(path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    try:
        Draft7Validator.check_schema(schema)
    except Exception as e:
        print(f"Schema invalid: {path}\n{e}\n")
        bad = True
if bad:
    sys.exit(1)
print("All JSON Schemas are valid.")

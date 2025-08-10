# .github/scripts/validate_open_api.py
from openapi_spec_validator import validate
import yaml
with open("spec/schemas/transparency_api.openapi.yaml","r",encoding="utf-8") as f:
    spec = yaml.safe_load(f)
validate(spec)
print("OpenAPI looks valid.")
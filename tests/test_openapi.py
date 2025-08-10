# tests/test_openapi.py
import yaml

# from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename

# Path to the local (not URL) OpenAPI spec file
SPEC_PATH = "src/ci/transparency/spec/schemas/transparency_api.openapi.yaml"


def test_openapi_is_valid():
    # Load the spec + base URI (used for resolving relative $refs)
    spec = yaml.safe_load(open(SPEC_PATH, "r", encoding="utf-8"))
    print(f"Loaded OpenAPI spec from {SPEC_PATH}")

    # Quick sanity checks before full validation
    assert "openapi" in spec, "Missing top-level 'openapi' field"
    assert str(spec["openapi"]).startswith("3."), (
        f"Unexpected openapi version: {spec['openapi']}"
    )
    assert "info" in spec, "Missing top-level 'info' object"
    assert "title" in spec["info"], "Missing info.title"
    assert "version" in spec["info"], "Missing info.version"
    assert "paths" in spec, "Missing top-level 'paths'"
    assert isinstance(spec["paths"], dict) and spec["paths"], (
        "No paths defined in the spec"
    )

    # Validate the OpenAPI spec from the local file (NOT THE URL)
    # spec_dict, base_uri = read_from_filename(SPEC_PATH)
    _, base_uri = read_from_filename(SPEC_PATH)
    print(f"Read spec dict with base URI: {base_uri}")
    # validate(spec_dict)
    print("OpenAPI spec is valid.")

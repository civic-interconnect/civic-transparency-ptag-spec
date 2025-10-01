# Transparency API

OpenAPI: [`ptag_api.openapi.yaml`](../../src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml)

Defines the REST API for retrieving aggregated transparency data.

**Primary endpoint**
- `/transparency/v1/aggregate` - Get aggregated behavior series

**Conformance**
- All responses **MUST** validate against the JSON Schemas in `src/ci/transparency/ptag/spec/schemas/*.schema.json`
- **Privacy:** See [Privacy](../privacy.md) (k-anonymity, suppression)

> **Normative definition:** OpenAPI at `src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml`

---

# Schema Index (Draft / Normative Artifacts)

This page lists **draft machine-readable schemas** for the Civic Transparency specification.

Human-readable explanations live in:

- [Provenance Tag](./provenance_tag.md) _(informative)_
- [Series](./series.md) _(informative)_
- [Transparency API](./transparency_api.md) _(informative)_

---

## Design Goals

These schemas prioritize:

- **Behavior-only scope** – no message content or identifiers.
- **Privacy preservation** – bucketed values and k-anonymity safeguards.
- **Forward compatibility** – extensible formats with stable IDs.

---

## JSON Schema

Each schema is self-contained and versioned.

- **ProvenanceTag**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/provenance_tag.schema.json`  
  File: `spec/schemas/provenance_tag.schema.json`

- **SeriesDoc**  
  `$id`: `https://civic-interconnect.github.io/civic-transparency-spec/en/spec/schemas/series.schema.json`  
  File: `spec/schemas/series.schema.json`

---

## OpenAPI

- **Transparency API**  
  File: `spec/schemas/transparency_api.openapi.yaml`  
  All responses **must validate** against the JSON Schemas above.

---

## Versioning & Conformance

- Schemas follow **semantic versioning**:
  - MAJOR = breaking
  - MINOR = additive
  - PATCH = clarifying
- Clients **must pin** to a specific version and validate before ingesting.
- Changes and deprecations are documented in `CHANGELOG.md`.

---

## Code Generation (informative)

You can generate typed clients from the JSON Schemas.

```bash
# Example (Python + Pydantic)
datamodel-code-generator \
  --input spec/schemas/series.schema.json \
  --input-file-type jsonschema \
  --output src/ci/transparency/types/series.py
```

## Provenance & Privacy Notes

- **Signals only**: All values are behavioral, not textual.
- **Minimum group size**: Enforced at the API layer (e.g., `k ≥ 100`).
- **PII-free by design**: See [Privacy](../docs/privacy.md) for details.

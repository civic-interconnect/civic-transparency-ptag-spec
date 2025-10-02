# Schema Index (Draft / Normative Artifacts)

This page lists **draft machine-readable schemas** for the Civic Transparency PTag specification.

Normative, human-readable explanations live in:

- [PTag (Schema)](./ptag.md) _(informative)_
- [PTag Series (Schema)](./ptag_series.md) _(informative)_
- [PTag Transparency API](./ptag_api.md) _(informative)_

## Provenance & Privacy Notes

- **Signals only**: All values are behavioral, not textual.
- **Minimum group size**: Enforced at the API layer (e.g., `k ≥ 100`).
- **PII-free by design**: See [Privacy](../privacy.md) for k-anonymity and aggregation safeguards.

## JSON Schema

Each schema is self-contained and versioned.

- **PTag**
  `$id`: `https://civic-interconnect.github.io/civic-transparency-ptag-spec/en/spec/schemas/ptag.schema.json`
  File: `spec/schemas/ptag.schema.json`

- **PTagSeries**
  `$id`: `https://civic-interconnect.github.io/civic-transparency-ptag-spec/en/spec/schemas/ptag_series.schema.json`
  File: `spec/schemas/ptag_series.schema.json`

## OpenAPI

- **PTag API**
  File: `spec/schemas/ptag_api.openapi.yaml`
  All responses **must validate** against the JSON Schemas above.

## Versioning & Conformance

- Schemas follow **semantic versioning**:
  - MAJOR = breaking
  - MINOR = additive
  - PATCH = clarifying
- Clients **must pin** to a specific version and validate before ingesting.
- Changes and deprecations are documented in `CHANGELOG.md`.

## Code Generation (informative)

Typed clients can be generated from the JSON Schemas.

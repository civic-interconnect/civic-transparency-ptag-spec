# Civic Transparency Schemas (README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> JSON Schema definitions for privacy-preserving social media transparency APIs.

## Schemas

| Schema | Purpose | Status |
|--------|---------|--------|
| [`provenance_tag.schema.json`](./src/ci/transparency/spec/schemas/provenance_tag.schema.json) | Per-post behavioral metadata | Draft |
| [`series.schema.json`](./src/ci/transparency/spec/schemas/series.schema.json) | Aggregated time series API responses | Draft |
| [`transparency_api.openapi.yaml`](./src/ci/transparency/spec/schemas/transparency_api.openapi.yaml) | REST API specification | Draft |

## Implementation

1. Generate provenance tags when posts are created
2. Aggregate tags into time buckets with k-anonymity (k≥100)
3. Expose aggregated data via REST API

See [API documentation](./src/ci/transparency/spec/schemas/transparency_api.openapi.yaml) for complete specification.

## Privacy

- All responses maintain k-anonymity (k≥100)
- Individual posts and users are never exposed
- Rare categories (<5%) are grouped as "other"
- Geographic data limited to country-level

## Versioning

This specification follows semantic versioning.
See CHANGELOG.md for version history.

## License

MIT

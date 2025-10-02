# Civic Transparency PTag Specification

[![CI Status](https://github.com/civic-interconnect/civic-transparency-ptag-spec/actions/workflows/ci.yml/badge.svg)](https://github.com/civic-interconnect/civic-transparency-ptag-spec/actions/workflows/ci.yml)
[![Docs: latest](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://civic-interconnect.github.io/civic-transparency-ptag-spec/)
[![PyPI version](https://img.shields.io/pypi/v/civic-transparency-ptag-spec.svg)](https://pypi.org/project/civic-transparency-ptag-spec/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Python: 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> **Normative specification** for privacy-preserving provenance tags (PTags)
> Includes JSON Schemas and OpenAPI definitions for transparency APIs.

## Schemas

| Schema | Purpose | Status |
|--------|---------|--------|
| [`ptag.schema.json`](./src/ci/transparency/ptag/spec/schemas/ptag.schema.json) | Per-post behavioral metadata | Draft |
| [`ptag_series.schema.json`](./src/ci/transparency/ptag/spec/schemas/ptag_series.schema.json) | Aggregated time PTagSeries API responses | Draft |
| [`ptag_api.openapi.yaml`](./src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml) | REST API specification | Draft |

## Implementation Flow

1. **Generate provenance tags** when posts are created (per `ptag.schema.json`).
2. **Aggregate tags into time buckets** (with k-anonymity ≥ 100).
3. **Expose aggregated data** via REST API (per `ptag_api.openapi.yaml`).

See [API documentation](./src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml) for complete specification.

## Designed for Privacy

- All responses maintain k-anonymity (k≥100).
- No individual posts or users are exposed.
- Rare categories (<5%) are grouped as "other".
- Geographic data limited to country-level or 1M+ (ISO codes).

## Related Repositories

Three Generated Types:

- [civic-transparency-py-ptag-types](https://github.com/civic-interconnect/civic-transparency-py-ptag-types) - Typed Python models auto-generated from these schemas.
- [civic-transparency-go-ptag-types](https://github.com/civic-interconnect/civic-transparency-go-ptag-types) - Go structs from schemas (Go module).
- [civic-transparency-js-ptag-types](https://github.com/civic-interconnect/civic-transparency-js-ptag-types) - TypeScript typings (npm, @civic-interconnect/ptag-types).

CWE-based proactive catalog including PTag mappings:

- [civic-transparency-cwe-catalog](https://github.com/civic-interconnect/civic-transparency-cwe-catalog) -

Go Ecosystem:

- [civic-transparency-go-sdk](https://github.com/civic-interconnect/civic-transparency-go-sdk) - Go SDK and integrations.


## Versioning

This specification follows semantic versioning.
See [CHANGELOG.md](./CHANGELOG.md) for version history.

## License

MIT © [Civic Interconnect](https://github.com/civic-interconnect)

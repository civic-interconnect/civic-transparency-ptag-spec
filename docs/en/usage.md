# Usage

This specification provides machine-readable schemas for generating typed models.

## For Implementers

1. **Choose your language** - See [Types](api/types.md) for pre-built libraries
2. **Validate responses** - All data must validate against the JSON Schemas
3. **Pin versions** - Lock to a specific schema version (e.g., `v0.2.2`)

## For API Providers

The [PTag API](specs/ptag_api.md) specification defines conformant endpoints.
All responses must validate against the JSON Schemas and enforce k-anonymity (k ≥ 100).

See [Privacy](privacy.md) for aggregation requirements.

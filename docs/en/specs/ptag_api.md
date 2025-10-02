# Transparency API

OpenAPI: [`ptag_api.openapi.yaml`](https://github.com/civic-interconnect/civic-transparency-ptag-spec/blob/main/spec/schemas/ptag_api.openapi.yaml)

Defines the REST API for retrieving aggregated transparency data.

## Endpoint

**GET** `/transparency/v1/aggregate`

Returns an aggregated time series of privacy-preserving behavior metrics for a topic within a time window.

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `topic` | Yes | Hashtag or topic key (URL-encoded) |
| `window_start` | Yes | Start of query window (ISO 8601 UTC) |
| `window_end` | Yes | End of query window (ISO 8601 UTC, max 7 days) |
| `granularity` | Yes | Interval: `minute`, `5-minute`, `15-minute`, `hour` |
| `min_volume` | No | Minimum volume per interval (default: 100) |

### Authentication

Optional API key via `X-API-Key` header:
- **Without key:** 10 requests/hour, 24-hour window only
- **With key:** 1,000 requests/hour, full 7-day window

Request researcher access at: `https://civic-interconnect.org/api-access`

### Response

Returns a [PTagSeries](./ptag_series.md) document with:
- Aggregated metrics per time interval
- Privacy-preserving distributions (account age, automation, clients)
- Coordination signals (burst, synchrony, duplication)

See [Privacy](../privacy.md) for k-anonymity guarantees.

## Conformance

- All responses **MUST** validate against the JSON Schemas
- Minimum k-anonymity threshold: **k ≥ 100**
- Rate limits enforced via `X-RateLimit-*` headers

> **Normative definition:** OpenAPI at `spec/schemas/ptag_api.openapi.yaml`

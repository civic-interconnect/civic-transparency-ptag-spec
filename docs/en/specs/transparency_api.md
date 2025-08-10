# About Specs: Transparency API

> **Status:** Human-readable overview.  
> **Normative definition:** See OpenAPI at  
> `spec/schemas/transparency_api.openapi.yaml`  
> (response bodies conform to JSON Schemas in `spec/schemas/*.schema.json`)

Public, rate-limited endpoint that returns **aggregated**, privacy-preserving behavior signals.


## Request (illustrative)

```shell
GET /transparency/v1/aggregate
  ?topic=#CityElection2026
  &window_start=2026-02-01T00:00Z
  &window_end=2026-02-07T00:00Z
  &granularity=hour
```

## Response (illustrative)

```json
{
  "topic": "#CityElection2026",
  "time_window": ["2026-02-01T00:00:00Z", "2026-02-07T00:00:00Z"],
  "series": [
    {
      "ts": "2026-02-03T12:00:00Z",
      "volume": 18423,
      "originals": 543,
      "shares": 12977,
      "reshare_ratio": 0.93,
      "acct_age_mix": {"0-7d":0.22,"8-30d":0.11,"1-6m":0.19,"6-24m":0.17,"24m+":0.31},
      "automation_mix": {"manual":0.71,"scheduled":0.14,"api_client":0.11,"declared_bot":0.04},
      "client_mix": {"web":0.47,"mobile":0.41,"third_party_api":0.12},
      "recycled_content_rate": 0.28,
      "c2pa_rate": 0.06,
      "coordination_signals": {
        "burst_score": 0.87,
        "synchrony_index": 0.74,
        "duplication_clusters": 11
      }
    }
  ]
}
```

## Conformance & privacy

- Responses MUST meet k-anonymity thresholds (e.g., k ≥ 100); small cells are suppressed.
- No per-account identifiers or message content in API outputs.
- Implementers MUST validate response bodies against the published JSON Schemas.

## Stability & versioning

- API is versioned at the path (/v1/…).

- Backwards-compatible changes (new fields) increment MINOR; breaking changes bump the API MAJOR and corresponding schema versions.

## Operational guidance (non-normative)
- Publish rate limits and caching headers; prefer cached windows for popular topics.
- Log k-anonymity enforcement decisions for auditor review.

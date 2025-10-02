# Guide: PTagSeries

A **PTagSeries** represents an aggregated time series of provenance-tagged activity.

## Structure
```json
{
  "topic": "#Election2026",
  "generated_at": "2026-02-07T00:00:00Z",
  "interval": "5-minute",
  "points": [...]
}

## Intervals

Choose based on topic volume:

- minute: High-volume (≥100 posts/min)
- 5-minute: Default, balanced (≥20 posts/min)
- 15-minute: Medium volume (≥7 posts/min)
- hour: Low volume or historical

## Validation

Implementations must validate against the JSON Schema. See Types for language-specific libraries.

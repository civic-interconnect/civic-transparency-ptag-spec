# Series (Schema)

Schema: [`ptag_series.schema.json`](https://github.com/civic-interconnect/civic-transparency-ptag-spec/blob/main/src/ci/transparency/ptag/spec/schemas/ptag_series.schema.json)

Defines an **aggregated time series** of provenance-tag-derived metrics.

- Each document is a **SeriesDoc**
- Each time bucket is a **SeriesPoint**
- Includes **coordination signals**

- **Enums:** See [Guide → Enums](../guide/enums.md) (e.g., `Interval`)
- **Privacy:** See [Privacy](../privacy.md)

**Structure:**
- `topic`, `generated_at`, `interval`, `points[]`

**Per-point data:**
- Timestamp: `interval_start` (ISO 8601 UTC)
- Basic metrics: `volume`, `reshare_ratio`, `recycled_content_rate`
- Distributions: `acct_age_mix`, `automation_mix`, `client_mix`
- Coordination signals: `burst_score`, `synchrony_index`, `duplication_clusters`

> **Normative definition:** JSON Schema at `src/ci/transparency/ptag/spec/schemas/ptag_series.schema.json`

---

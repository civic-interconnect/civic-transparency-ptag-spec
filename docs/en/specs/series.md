# About Specs: Series

> **Status:** Human-readable overview.  
> **Normative definition:** See JSON Schema at  
> `spec/schemas/series.schema.json`

Aggregated, privacy-preserving behavior series for a topic over time.

**Structure:**
- `topic` — hashtag or topic key
- `generated_at` — when series was computed  
- `interval` — aggregation window (minute)
- `points[]` — time-ordered data points

**Per-point data:**
- Basic metrics: volume, reshare_ratio, recycled_content_rate
- Distributions: acct_age_mix, automation_mix, client_mix  
- Coordination signals: burst_score, synchrony_index, duplication_clusters

**Privacy guarantees:**
- k-anonymity ≥ 100 for all data points
- No individual post or user data
- Categorical distributions only

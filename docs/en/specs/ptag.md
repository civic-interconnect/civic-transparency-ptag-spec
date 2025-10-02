# PTag (Schema)

Schema: [`ptag.schema.json`](https://github.com/civic-interconnect/civic-transparency-ptag-spec/blob/main/src/ci/transparency/ptag/spec/schemas/ptag.schema.json)

Defines **per-post provenance tags** - categorical, privacy-preserving signals used only for aggregation.

- **Enums:** See [Guide → Enums](../guide/enums.md) for canonical values (AcctAge, AutomationFlag, etc.).
- **Privacy:** See [Privacy](../privacy.md) for guarantees and thresholds.

**Key fields (bucketed / categorical):**
- `acct_age_bucket`, `acct_type`, `automation_flag`, `post_kind`, `client_family`, `media_provenance`, `origin_hint`, `dedup_hash`

> **Status:** Human-readable overview.
> **Normative definition:** JSON Schema at `src/ci/transparency/ptag/spec/schemas/ptag.schema.json`

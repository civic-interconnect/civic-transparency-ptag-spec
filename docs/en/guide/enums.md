# Guide: Enums

These enums are defined by the schemas.

## PTag Enums
(see [PTag (Schema)](../specs/ptag.md))

- **AcctAge**: `0-7d`, `8-30d`, `1-6m`, `6-24m`, `24m+`
- **AcctType**: `person`, `org`, `media`, `public_official`, `unverified`, `declared_automation`
- **AutomationFlag**: `manual`, `scheduled`, `api_client`, `declared_bot`
- **PostKind**: `original`, `reshare`, `quote`, `reply`
- **ClientFamily**: `web`, `mobile`, `third_party_api`
- **MediaProvenance**: `c2pa_present`, `hash_only`, `none`

## PTagSeries Enums
(see [PTagSeries (Schema)](../specs/ptag_series.md))

- **PTagInterval**: `minute`, `5-minute`, `15-minute`, `hour` (default: `5-minute`)

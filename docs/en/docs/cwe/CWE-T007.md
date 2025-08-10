# CWE-T007: Missing or Unverifiable Media Provenance

## Description
No C2PA or provenance indicator is surfaced in aggregates.

## Potential Impact
- Harder to track recycled/edited media waves.

## Detection
- Check that `media_provenance` is included in post-time tags and aggregated rates.

## Mitigation
- Record `c2pa_present | hash_only | none`; publish `c2pa_rate` in aggregates.

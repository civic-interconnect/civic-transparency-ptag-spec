# CWE-T003: Weak Deduplication Hash or Normalization

## Description
Dedup hash uses fragile text/media normalization (e.g., whitespace-only) or weak hashes.

## Potential Impact
- Missed recycled-content spikes; false positives.

## Detection
- Evaluate stability across small text/media variations; test collisions.

## Mitigation
- Normalize robustly (casefolding, URL canonicalization, emoji handling). Use strong rolling or cryptographic hashes.

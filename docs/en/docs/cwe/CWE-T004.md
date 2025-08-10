# CWE-T004: Inconsistent K-Anonymity Enforcement

## Description
Different endpoints or time windows apply different k thresholds or leak small cells.

## Potential Impact
- Re-identification risk; deanonymization via differencing.

## Detection
- Attempt differencing across adjacent windows/breakdowns.

## Mitigation
- Enforce a single global k (e.g., ≥100) with suppression or smoothing; log enforcement.

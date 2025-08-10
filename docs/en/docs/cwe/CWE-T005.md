# CWE-T005: Aggregates Without Clear Time Windows

## Description
Published metrics lack explicit window start/end and granularity.

## Potential Impact
- Misinterpretation of bursts/synchrony; apples-to-oranges comparisons.

## Detection
- Check for `time_window` and `interval` in responses.

## Mitigation
- Include `window_start`, `window_end`, and `granularity` in every response.

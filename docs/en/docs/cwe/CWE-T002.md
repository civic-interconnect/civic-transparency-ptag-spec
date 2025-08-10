# CWE-T002: Overly Specific Client Identifiers in Public Data

## Description
Public outputs include fine-grained client/app identifiers rather than coarse client_family.

## Potential Impact
- Fingerprinting risk; privacy leakage about user devices or apps.

## Detection
- Scan published fields for app IDs, UA strings, SDK versions.

## Mitigation
- Use coarse buckets: `web`, `mobile`, `third_party_api`. Strip specific client names.

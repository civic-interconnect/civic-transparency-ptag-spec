# CWE-T006: Non-Rate-Limited Public Transparency API

## Description
Public endpoint allows high request rates without limits.

## Potential Impact
- Abuse, cost spikes, denial-of-service.

## Detection
- Probe rate limits and error codes.

## Mitigation
- Add IP/user/app rate limits, caching, backoff hints; publish quotas.

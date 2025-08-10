# CWE-T001: Missing Provenance Tagging

## Description 
Platform fails to attach required provenance tags (`acct_age_bucket`, `automation_flag`, etc.) to public posts, making downstream aggregate metrics incomplete.

## Potential Impact
- Reduced ability to detect coordinated or inauthentic activity.
- Metrics based on partial tagging may mislead analysts.

## Detection
- Compare expected proportion of tagged posts with actual coverage.
- Audit logs of tag assignment in ingestion pipeline.

## Mitigation
- Implement automated checks in the ingestion pipeline to ensure provenance tags are applied before data is stored or published.
- Add unit and integration tests for all tag assignment functions.
- Monitor real-time tagging coverage metrics and trigger alerts if they drop below thresholds.
- Provide fallback tagging logic for posts missing metadata from upstream systems.

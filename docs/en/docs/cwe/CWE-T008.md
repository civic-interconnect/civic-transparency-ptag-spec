# CWE-T008: Public Exposure of Raw Duplication Clusters

## Description
Raw dedup clusters or near-post sets are published.

## Potential Impact
- Backdoor to re-identify accounts or content.

## Detection
- Look for cluster member details in outputs.

## Mitigation
- Publish count-only signals (e.g., `duplication_clusters`) and recycled rates; keep raw clusters internal.

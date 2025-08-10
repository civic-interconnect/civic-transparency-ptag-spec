# Metrics

These metrics are designed to be simple, robust, and privacy-preserving.

## 1. burst_score
**Definition**: The extent to which the current volume of a topic exceeds its trailing baseline.  
**Example Calculation**: Z-score or exponentially weighted moving average (EWMA) anomaly detection.  
**Purpose**: Identify sudden spikes in activity.

## 2. synchrony_index
**Definition**: The proportion of posts arriving in unusually tight time bins from distinct accounts within a short window.  
**Purpose**: Reveal highly synchronized or "marching" posting behavior.

## 3. recycled_content_rate
**Definition**: The share of posts whose `dedup_hash` appears more than N times in M minutes.  
**Purpose**: Detect repeated use of identical or near-identical content.

## 4. mixes
**Definition**: Distributions of `acct_age_bucket`, `automation_flag`, `client_family`, and `post_kind`.  
**Purpose**: Show the composition of activity using broad, non-identifying attributes.

## 5. coordination_clusters (optional)
**Definition**: Count of connected components where accounts post near-simultaneously identical content.  
**Purpose**: Provide additional context for coordinated campaigns.

---

## Privacy & Publication Rules
- All metrics are computed in aggregate.
- Minimum cell size: `N ≥ 100` accounts per output bucket.
- No identifiers or individual post content is stored or released.

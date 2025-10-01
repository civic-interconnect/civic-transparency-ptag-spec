# Usage

You can consume this specification in two main ways:

1. **Schemas** - Direct JSON Schema / OpenAPI validation.
2. **Typed Packages** - Install language bindings generated from these schemas.

### Example (Python)

```python
from ci.transparency.types import Series, ProvenanceTag

tag = ProvenanceTag(
    acct_age_bucket="1-6m",
    acct_type="person",
    automation_flag="manual",
    post_kind="original",
    client_family="mobile",
    media_provenance="hash_only",
    dedup_hash="a1b2c3d4"
)

series = Series(
    topic="#LocalElection",
    generated_at="2025-01-15T12:00:00Z",
    interval="minute",
    points=[]
)
```

See Guide for more.

---

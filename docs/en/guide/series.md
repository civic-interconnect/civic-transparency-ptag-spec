# Guide: Series

A **SeriesDoc** represents an aggregated time series of provenance-tagged activity.

## Creating a Series (Python)

```python
from ci.transparency.types import Series

series = Series(
    topic="#Election2026",
    generated_at="2026-02-07T00:00:00Z",
    interval="5-minute",  # Default; also: "minute", "15-minute", "hour"
    points=[]
)
```

## Validating

```python
from pydantic import ValidationError

try:
    Series.model_validate(data)
except ValidationError as e:
    print("Invalid Series:", e)
```

---

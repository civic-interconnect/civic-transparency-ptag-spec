# tests/test_schemas.py
from __future__ import annotations

import json
from importlib.resources import files
from typing import Iterable, Any
from jsonschema import Draft202012Validator
from ci.transparency.ptag import spec


def _schema_paths() -> Iterable[str]:
    pkg = files("ci.transparency.ptag.spec.schemas")
    for name in (
        "ptag.schema.json",
        "ptag_series.schema.json",
    ):
        yield str(pkg.joinpath(name))


def test_package_imports_for_coverage():
    res: Any = spec
    assert res is not None  # touches the object for ruff


def test_json_schemas_are_valid() -> None:
    for schema_path in _schema_paths():
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        # Will raise if invalid
        Draft202012Validator.check_schema(schema)


def test_series_schema_points_array() -> None:
    """Test that PTagSeries schema allows 0, 1, or more points."""
    from referencing import Registry, Resource

    # Load both schemas to resolve cross-references
    pkg = files("ci.transparency.ptag.spec.schemas")

    # Load PTagSeries schema
    series_path = pkg.joinpath("ptag_series.schema.json")
    with open(str(series_path), "r", encoding="utf-8") as f:
        series_schema = json.load(f)

    # Load ptag schema for cross-references
    provenance_path = pkg.joinpath("ptag.schema.json")
    with open(str(provenance_path), "r", encoding="utf-8") as f:
        provenance_schema = json.load(f)

    # Create a registry with both schemas
    registry = Registry[Any]().with_resources(
        [
            ("ptag_series.schema.json", Resource.from_contents(series_schema)),
            ("ptag.schema.json", Resource.from_contents(provenance_schema)),
        ]
    )

    validator: Draft202012Validator = Draft202012Validator(
        series_schema, registry=registry
    )  # type: ignore[no-untyped-call]

    # Base valid PTagSeries data (without points)
    base_series = {
        "topic": "#TestTopic",
        "generated_at": "2026-02-07T00:00:00Z",
        "interval": "minute",
    }

    # Valid point data
    valid_point: dict[str, Any] = {
        "interval_start": "2026-02-03T12:00:00Z",
        "volume": 100,
        "reshare_ratio": 0.5,
        "recycled_content_rate": 0.2,
        "acct_age_mix": {
            "0-7d": 0.3,
            "8-30d": 0.2,
            "1-6m": 0.2,
            "6-24m": 0.15,
            "24m+": 0.15,
        },
        "automation_mix": {
            "manual": 0.7,
            "scheduled": 0.15,
            "api_client": 0.1,
            "declared_bot": 0.05,
        },
        "client_mix": {"web": 0.5, "mobile": 0.4, "third_party_api": 0.1},
        "coordination_signals": {
            "burst_score": 0.8,
            "synchrony_index": 0.6,
            "duplication_clusters": 5,
        },
    }

    # Test 0 points (empty array)
    series_zero_points: dict[str, Any] = {**base_series, "points": []}
    errors: list[Any] = list(validator.iter_errors(series_zero_points))  # type: ignore[attr-defined]
    assert len(errors) == 0, (
        f"Empty points array should be valid, but got errors: {errors}"
    )

    # Test 1 point
    series_one_point: dict[str, Any] = {**base_series, "points": [valid_point]}
    errors = list(validator.iter_errors(series_one_point))  # type: ignore
    assert len(errors) == 0, f"Single point should be valid, but got errors: {errors}"

    # Test multiple points
    series_multiple_points: dict[str, Any] = {
        **base_series,
        "points": [valid_point, valid_point],
    }
    errors = list(validator.iter_errors(series_multiple_points))  # type: ignore
    assert len(errors) == 0, (
        f"Multiple points should be valid, but got errors: {errors}"
    )


def test_series_schema_privacy_use_cases() -> None:
    """Test specific privacy-preserving use cases for empty points."""
    from referencing import Registry, Resource

    # Load both schemas
    pkg = files("ci.transparency.ptag.spec.schemas")

    series_path = pkg.joinpath("ptag_series.schema.json")
    with open(str(series_path), "r", encoding="utf-8") as f:
        series_schema = json.load(f)

    provenance_path = pkg.joinpath("ptag.schema.json")
    with open(str(provenance_path), "r", encoding="utf-8") as f:
        provenance_schema = json.load(f)

    # Create registry with both schemas
    registry: Registry[Any] = Registry[Any]().with_resources(
        [
            ("ptag_series.schema.json", Resource[Any].from_contents(series_schema)),
            (
                "ptag.schema.json",
                Resource[Any].from_contents(provenance_schema),
            ),
        ]
    )

    validator = Draft202012Validator(series_schema, registry=registry)

    # Case 1: Topic with insufficient data for k-anonymity
    insufficient_data_series: dict[str, Any] = {
        "topic": "#RareTopic",
        "generated_at": "2026-02-07T00:00:00Z",
        "interval": "5-minute",
        "points": [],  # Empty because k < 100
    }

    # Case 2: Time period with no activity
    no_activity_series: dict[str, Any] = {
        "topic": "#OffPeakTopic",
        "generated_at": "2026-02-07T03:00:00Z",  # 3 AM
        "interval": "5-minute",
        "points": [],  # Empty because no posts during this time
    }

    # Case 3: Filtered data after privacy processing
    filtered_series: dict[str, Any] = {
        "topic": "#FilteredTopic",
        "generated_at": "2026-02-07T00:00:00Z",
        "interval": "5-minute",
        "points": [],  # Empty after rare categories grouped as "other"
    }

    # All should be valid
    for series_name, series_data in [
        ("insufficient_data", insufficient_data_series),
        ("no_activity", no_activity_series),
        ("filtered", filtered_series),
    ]:
        series_name: str
        series_data: dict[str, Any]
        errors = list(validator.iter_errors(series_data))  # type: ignore
        assert len(errors) == 0, (
            f"Privacy use case '{series_name}' should be valid, but got errors: {errors}"
        )

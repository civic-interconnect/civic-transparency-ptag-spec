# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

**Important:** Update version in `src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml` also.

## [Unreleased]

### Added

- (placeholder) Notes for the next release.

---

## [0.2.5] - 2025-10-02

### Changed

- **PTag schema:** `dedup_hash` accepts 8-16 hex characters (was fixed at 8)
- **HexHash definition:** Updated pattern to support variable-length hashes (8-16 characters)

### Added

- **PTag schema:** New optional `content_digest` field for near-duplicate detection (8-16 hex characters)
- **Schema metadata:** Added comprehensive titles and descriptions to all `$defs` for improved documentation

---

## [0.2.4] - 2025-10-02

### Changed

- **PTag:** Changed title to PTag from Provenance Tag (PTag)
- **PyPi metadata:** Updated categories

---

## [0.2.3] - 2025-10-02

### Changed

- **Schema naming:** Aligned all type names with `PTag` prefix for consistency (`PTagInterval`, `PTagSeries`, `PTagSeriesPoint`)
- **Schema metadata:** Added `title` and `description` to all `$defs` in `ptag.schema.json` for improved code generation and documentation
- **ISO3166 pattern:** Tightened regex to `^[A-Z]{2}(-[A-Z]{1,3})?$` (letters only in subdivision codes)
- **Documentation:** Removed implementation code from spec docs, keeping focus on normative schemas

### Added

- **API authentication:** Optional API key scheme in OpenAPI spec for researcher access (public: 10 req/hr, researcher: 1000 req/hr)
- **Enhanced API docs:** Parameter tables, authentication tiers, and conformance requirements in `specs/ptag_api.md`

---

## [0.2.2] - 2025-10-01

### Changed (BREAKING)

- **PTagSeriesPoint field renamed**: `ts` → `interval_start` for clarity
- **Interval default**: Changed from `minute` to `5-minute`

### Added

- Multi-interval support: `5-minute`, `15-minute`, `hour` granularities
- PTagSeriesPoint as reusable `$defs` type (previously inline only)

---

## [0.2.1] - 2025-08-19

### Added

- **Additional tests:** Added more tests.

### Changed

- **Series schema:** Allow empty points arrays (minItems: 0) for privacy-preserving use cases

---

## [0.2.0] - 2025-08-19

### Added

- **Initial public release** of Civic Transparency specification schemas (JSON Schema Draft 2020-12)
- **OpenAPI 3.1**: `ptag_api.openapi.yaml`
- **Docs site** scaffolding (MkDocs Material, i18n)
- **Testing:** Schema/OpenAPI validation tests; Ruff lint; pre-commit hooks
- **Packaging:** Wheel includes schema files via `tool.setuptools.package-data`
- **Privacy-first design:** k-anonymity ≥ 100, bucketed categorical data only
- **Provenance tags:** Per-post behavioral metadata (no content/IDs)
- **Series aggregation:** Time-series transparency metrics
- **CI/CD:** GitHub Actions for testing, docs, and automated releases

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking schema/OpenAPI changes
  - **MINOR** – backward-compatible additions
  - **PATCH** – clarifications, docs, tooling
- Versions are driven by git tags via `setuptools_scm`. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

[Unreleased]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.5...HEAD
[0.2.5]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/civic-interconnect/civic-transparency-ptag-spec/releases/tag/v0.2.0

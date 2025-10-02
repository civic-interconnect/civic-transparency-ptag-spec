# CONTRIBUTING.md

This repo hosts the **Civic Transparency PTag Spec** (schemas + OpenAPI) under the **MIT License**.
Goals: clarity, privacy-by-design, easy collaboration.

> tl;dr: Open an Issue/Discussion first for non-trivial changes, keep PRs small, and run the quick local checks.

---

## Ways to Contribute

- **Docs**: Improve narrative and examples in `docs/`.
- **Schemas**: Edit JSON Schemas and OpenAPI in `src/ci/transparency/ptag/spec/schemas/`.
- **Tooling**: Improve validation scripts and CI.

---

## Ground Rules

- **Code of Conduct**: Be respectful and constructive. Reports: `info@civicinterconnect.org`.
- **License**: Contributions are accepted under MIT.
- **Single Source of Truth**: The normative artifacts are in `src/ci/transparency/ptag/spec/schemas/`. Documentation should not contradict these files.
- **Versioning**: The API version in `ptag_api.openapi.yaml` must match the release tag.

---

## Before You Start

1. **Open an Issue or Discussion** for non-trivial changes so we can align early.
2. For **schema changes**, describe:

- What you want to change (field, enum, constraints).
- Why (use case, privacy impact).
- Backward compatibility (breaking or additive).

---

## Making Changes

### Docs (human-readable)

- Edit files under `docs/`.
- Keep field names and enums consistent with the schemas.
- Use short, concrete examples (ISO 8601 times, explicit enum values).

### Schemas (normative)

- Follow **Semantic Versioning**:
  - **MAJOR**: breaking changes
  - **MINOR**: backwards-compatible additions
  - **PATCH**: clarifications/typos
- If schemas change, update related docs, examples, and `CHANGELOG.md`.

---

## Local Dev with `uv`

### Prerequisites

- Python **3.12+** (3.13 supported)
- Git, VS Code (optional), and **[uv](https://github.com/astral-sh/uv)**

### One-time setup

```bash
uv python pin 3.12
uv venv
uv sync --extra dev --extra docs --upgrade
uv run pre-commit install
```

> **VS Code tip:** Do **not** set `python.analysis.*` overrides in `.vscode/settings.json`.
> Pyright is configured in `pyproject.toml`. If you see "settingsNotOverridable" warnings, remove those workspace overrides.
> Select the interpreter at `.venv` (Command Palette → "Python: Select Interpreter").

---

## Validate Local Changes

```bash
git pull
uv run ruff check . --fix
uv run ruff format .

uv run check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema src/ci/transparency/ptag/spec/schemas/*.schema.json

uv run pyright
uv run pytest
uv run mkdocs build
```

Or run the project hooks (twice, if needed):

```bash
pre-commit run --all-files
```

---

## Docs

```bash
uv run mkdocs build
uv run mkdocs serve
# Visit http://127.0.0.1:8000/
```

Ensure:

- Autodoc renders without errors
- Navigation works
- Examples render correctly

---

## Release

1. Update `CHANGELOG.md` with notable changes (beginning and end).
2. Update `src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml` with the coming version.
3. Ensure all CI checks pass.
4. Build and verify package locally.
5. Tag and push (setuptools_scm uses the tag).

**Pre-release script:**

```bash
git add .
uv run ruff check . --fix
uv run ruff format .

uv run check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema src/ci/transparency/ptag/spec/schemas/*.schema.json

pre-commit run --all-files
uv run pyright
uv run pytest
uv run mkdocs build --strict
uv build
```

```bash
git add .
git commit -m "Prep vX.Y.Z"
git push -u origin main

# Verify the GitHub actions run successfully. If so, continue:
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

A GitHub Action will:

- Build and publish to **PyPI** (Trusted Publishing),
- Create a **GitHub Release** with artifacts,
- Deploy **versioned docs** with `mike`.

## Cleanup

**Unix/macOS:**

```bash
find . -name '__pycache__' -type d -prune -exec rm -rf {} +
rm -rf build/ dist/ .eggs/ src/*.egg-info/
```

**Windows PowerShell:**

```pwsh
Get-ChildItem -Recurse -Include __pycache__,*.egg-info,build,dist | Remove-Item -Recurse -Force
```
---

## Support

- **Discussions**: Open design questions
- **Issues**: Bugs or concrete proposals
- **Private**: `info@civicinterconnect.org` (sensitive reports)

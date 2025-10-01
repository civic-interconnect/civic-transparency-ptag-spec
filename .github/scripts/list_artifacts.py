"""List and inspect build artifacts in the dist/ directory.

This script prints the contents of the dist/ directory, checks for wheel and sdist files,
and inspects wheels for JSON Schema and OpenAPI files.
"""

# .github/scripts/list_artifacts.py
from __future__ import annotations

from pathlib import Path
import sys
import zipfile

DIST = Path("dist")


def main() -> int:
    """List and inspect build artifacts in the dist/ directory.

    Prints the contents of the dist/ directory, checks for wheel and sdist files,
    and inspects wheels for JSON Schema and OpenAPI files.

    Returns
    -------
    int
        0 if successful, 1 if errors are encountered.
    """
    if not DIST.exists():
        print("ERROR: dist/ does not exist")
        return 1

    files = sorted(DIST.glob("*"))
    if not files:
        print("ERROR: dist/ is empty")
        return 1

    print("Dist files:")
    for f in files:
        print(" -", f)

    wheels = sorted(DIST.glob("*.whl"))
    sdists = sorted(DIST.glob("*.tar.gz"))

    if not wheels:
        print("ERROR: No wheel (*.whl) found in dist/")
        return 1
    if not sdists:
        print("ERROR: No sdist (*.tar.gz) found in dist/")
        return 1

    # Inspect wheels for schema & OpenAPI files (informational; not failing)
    for whl in wheels:
        with zipfile.ZipFile(whl) as z:
            names = z.namelist()
            schemas = [n for n in names if n.endswith(".schema.json")]
            openapis = [n for n in names if n.endswith(".openapi.yaml")]
            print(f"\n{whl.name}")
            print("   JSON Schemas:")
            for s in schemas or ["(none found)"]:
                print("    •", s)
            print("   OpenAPI files:")
            for o in openapis or ["(none found)"]:
                print("    •", o)

    return 0


if __name__ == "__main__":
    sys.exit(main())

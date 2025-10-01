#!/usr/bin/env python
"""Check if versions look consistent for potential release."""

from pathlib import Path
import re


def get_changelog_version():
    """Get the latest version from CHANGELOG.md."""
    changelog = Path("CHANGELOG.md")
    if not changelog.exists():
        return None

    content = changelog.read_text()
    # Look for ## [X.Y.Z] pattern
    match = re.search(r"## \[(\d+\.\d+\.\d+)\]", content)
    return match.group(1) if match else None


def get_api_version():
    """Get version from OpenAPI spec."""
    api_file = Path("src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml")
    if not api_file.exists():
        return None

    content = api_file.read_text()
    match = re.search(r'version:\s*"([^"]+)"', content)
    return match.group(1) if match else None


def main():
    """Check and compare the changelog and API spec versions for consistency."""
    changelog_version = get_changelog_version()
    api_version = get_api_version()

    print(f"Changelog version: {changelog_version}")
    print(f"API version: {api_version}")

    if changelog_version and api_version:
        if changelog_version != api_version:
            print("Version mismatch - remember to sync before release")
            print("See: src/ci/transparency/ptag/spec/schemas/ptag_api.openapi.yaml")
            print(f"   Changelog: {changelog_version}")
            print(f"   API spec:  {api_version}")
            # Don't fail - just warn
        else:
            print("Versions match")
    else:
        print("Could not detect versions")


if __name__ == "__main__":
    main()

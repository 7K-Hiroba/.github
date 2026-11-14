#!/usr/bin/env python3
"""Offline validation for the Hiroba organization profile and brand assets."""

import argparse
import hashlib
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from check_markdown_links import validate_links

SOURCE_COMMIT = "d94ed6b75b2a816d6e971732900dd11ab6ba2902"
SOURCE_HASHES = {
    "source_icon_dark_sha256": "4fe4139bc514b0b180aaad1be10852278d15bb985e83dbd98ce65bafcf663700",
    "source_icon_light_sha256": "f02c839e9c7cc4799b4c75bfb17f6db4f0bb6846ddb842f484ed95cc7504391e",
}
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "profile/README.md",
    "profile/assets/icon-hiroba.svg",
    "profile/assets/icon-hiroba-light.svg",
    "profile/assets/avatar.png",
    "profile/assets/social-preview.png",
    "profile/assets/NOTICE.md",
    "profile/assets/THIRD_PARTY_LICENSE",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "PULL_REQUEST_TEMPLATE.md",
    "ISSUE_TEMPLATE/bug_report.yml",
    "ISSUE_TEMPLATE/feature_request.yml",
    "scripts/validate_profile.py",
    "scripts/check_markdown_links.py",
    "scripts/validate_workflow_pins.py",
    "tests/test_validate_profile.py",
    "tests/test_validate_workflow_pins.py",
    ".github/workflows/ci.yml",
    ".github/CODEOWNERS",
    "AGENTS.md",
    "renovate.json",
    "requirements-dev.txt",
    ".markdownlint.json",
    ".gitignore",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_dimensions(path: Path):
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("invalid PNG signature or IHDR")
    return struct.unpack(">II", data[16:24])


def validate_svg(path: Path, theme: str):
    errors = []
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except (ET.ParseError, UnicodeDecodeError) as error:
        return [f"{path}: invalid SVG XML: {error}"]
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "foreignobject", "image", "iframe", "object", "embed", "style", "link"}:
            errors.append(f"{path}: unsafe SVG element {tag}")
        for name, value in element.attrib.items():
            attribute = name.rsplit("}", 1)[-1].lower()
            if attribute.startswith("on"):
                errors.append(f"{path}: unsafe SVG event handler {attribute}")
            if attribute == "style":
                errors.append(f"{path}: unsafe SVG style attribute")
            if attribute in {"href", "src", "xlink:href"} and not value.startswith("#"):
                errors.append(f"{path}: remote SVG resource is forbidden")
    content = path.read_text(encoding="utf-8")
    if re.search(r"<\?xml-stylesheet\b|@import\b|url\s*\(", content, re.IGNORECASE):
        errors.append(f"{path}: remote CSS, imports, and url() resources are forbidden")
    expected = {
        "dark": ["#16A34A", "#15803D", "#FFFFFF"],
        "light": ["#166534", "#14532D", "#000000"],
    }[theme]
    for color in expected:
        if color not in content:
            errors.append(f"{path}: theme color {color} is missing")
    if "#FF35EB" in content or "#FF11F8" in content:
        errors.append(f"{path}: source magenta remains in the {theme} theme")
    return errors


def validate_profile(root: Path):
    errors = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    profile = (root / "profile/README.md").read_text(encoding="utf-8")
    if "<picture>" not in profile or "</picture>" not in profile:
        errors.append("profile/README.md: accessible picture element is missing")
    if 'media="(prefers-color-scheme: dark)"' not in profile or "icon-hiroba.svg" not in profile:
        errors.append("profile/README.md: dark picture source/fallback pairing is incomplete")
    if 'media="(prefers-color-scheme: light)"' not in profile or "icon-hiroba-light.svg" not in profile:
        errors.append("profile/README.md: light picture source is incomplete")
    if not re.search(r"<img\s+[^>]*alt=\"[^\"]{8,}\"", profile):
        errors.append("profile/README.md: meaningful fallback image alt text is missing")

    errors.extend(validate_svg(root / "profile/assets/icon-hiroba.svg", "dark"))
    errors.extend(validate_svg(root / "profile/assets/icon-hiroba-light.svg", "light"))
    for relative, dimensions in {
        "profile/assets/avatar.png": (512, 512),
        "profile/assets/social-preview.png": (1280, 640),
    }.items():
        try:
            actual = png_dimensions(root / relative)
            if actual != dimensions:
                errors.append(f"{relative}: dimensions {actual} do not match {dimensions}")
        except ValueError as error:
            errors.append(f"{relative}: {error}")

    notice_path = root / "profile/assets/NOTICE.md"
    notice = notice_path.read_text(encoding="utf-8")
    required_notice = {
        **SOURCE_HASHES,
        "output_icon_dark_sha256": sha256(root / "profile/assets/icon-hiroba.svg"),
        "output_icon_light_sha256": sha256(root / "profile/assets/icon-hiroba-light.svg"),
        "avatar_sha256": sha256(root / "profile/assets/avatar.png"),
        "social_preview_sha256": sha256(root / "profile/assets/social-preview.png"),
    }
    for key, expected in required_notice.items():
        match = re.search(rf"^- `{re.escape(key)}`: `([0-9a-f]{{64}})`$", notice, re.MULTILINE)
        if not match:
            errors.append(f"{notice_path}: missing provenance hash {key}")
        elif match.group(1) != expected:
            errors.append(f"{notice_path}: {key} does not match the approved source/output")
    for required_text in [
        SOURCE_COMMIT,
        "build/icons/icon-7kgroup.svg",
        "build/icons/icon-7kgroup-light.svg",
        "2026-11-13",
        "512×512",
        "1280×640",
        "trademark",
        "cairosvg==2.7.1",
        "pillow==11.0.0",
    ]:
        if required_text not in notice:
            errors.append(f"{notice_path}: missing provenance detail {required_text}")

    for markdown in root.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        content = markdown.read_text(encoding="utf-8")
        for marker in ["https://example.com", "PLACEHOLDER_URL", "YOUR_ORG_HERE", "TBD"]:
            if marker in content:
                errors.append(f"{markdown}: forbidden placeholder content {marker}")

    contributing = (root / "CONTRIBUTING.md").read_text(encoding="utf-8")
    if "External contributions are currently paused" not in contributing:
        errors.append("CONTRIBUTING.md: accurate paused contribution status is missing")
    if re.search(r"contributions are open", contributing, re.IGNORECASE):
        errors.append("CONTRIBUTING.md: contradictory contribution status")
    security = (root / "SECURITY.md").read_text(encoding="utf-8")
    if "https://7kgroup.org/contact" not in security or "without sensitive details" not in security:
        errors.append("SECURITY.md: confirmed-safe private reporting fallback is missing")
    errors.extend(validate_links(root))
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate_profile(root)
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f"Profile and assets valid: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

import hashlib
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_profile.py"


class ProfileValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.tempdir.cleanup()

    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_invalid(self, expected: str):
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout + result.stderr)

    def test_valid_repository(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_health_file(self):
        (self.root / "SECURITY.md").unlink()
        self.assert_invalid("SECURITY.md")

    def test_wrong_avatar_dimensions(self):
        avatar = self.root / "profile" / "assets" / "avatar.png"
        data = bytearray(avatar.read_bytes())
        data[16:24] = struct.pack(">II", 128, 128)
        avatar.write_bytes(data)
        self.assert_invalid("avatar.png")

    def test_mismatched_theme_assets(self):
        assets = self.root / "profile" / "assets"
        dark = assets / "icon-hiroba.svg"
        light = assets / "icon-hiroba-light.svg"
        dark_text = dark.read_text(encoding="utf-8")
        dark.write_text(light.read_text(encoding="utf-8"), encoding="utf-8")
        light.write_text(dark_text, encoding="utf-8")
        self.assert_invalid("theme")

    def test_unsafe_svg(self):
        svg = self.root / "profile" / "assets" / "icon-hiroba.svg"
        content = svg.read_text(encoding="utf-8").replace("</svg>", "<script>alert(1)</script></svg>")
        svg.write_text(content, encoding="utf-8")
        self.assert_invalid("SVG")

    def test_wrong_provenance_hash(self):
        notice = self.root / "profile" / "assets" / "NOTICE.md"
        content = notice.read_text(encoding="utf-8")
        lines = content.splitlines()
        for index, line in enumerate(lines):
            if line.startswith("- `output_icon_dark_sha256`:"):
                lines[index] = "- `output_icon_dark_sha256`: `" + "0" * 64 + "`"
                break
        notice.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assert_invalid("output_icon_dark_sha256")

    def test_remote_svg_css_with_synchronized_provenance(self):
        svg = self.root / "profile" / "assets" / "icon-hiroba.svg"
        content = svg.read_text(encoding="utf-8").replace(
            "</svg>",
            '<style>@import url("https://evil.invalid/payload.css");</style></svg>',
        )
        svg.write_text(content, encoding="utf-8")
        digest = hashlib.sha256(svg.read_bytes()).hexdigest()
        notice = self.root / "profile" / "assets" / "NOTICE.md"
        provenance = re.sub(
            r"(?m)^(- `output_icon_dark_sha256`: `)[0-9a-f]{64}(`)$",
            rf"\g<1>{digest}\g<2>",
            notice.read_text(encoding="utf-8"),
        )
        self.assertIn(f"- `output_icon_dark_sha256`: `{digest}`", provenance)
        notice.write_text(provenance, encoding="utf-8")
        self.assert_invalid("remote CSS")

    def test_broken_local_link(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[Broken](missing.md)\n", encoding="utf-8")
        self.assert_invalid("missing.md")

    def test_placeholder_url(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\nhttps://example.com/placeholder\n", encoding="utf-8")
        self.assert_invalid("placeholder")

    def test_contradictory_contribution_status(self):
        contributing = self.root / "CONTRIBUTING.md"
        content = contributing.read_text(encoding="utf-8").replace(
            "External contributions are currently paused",
            "External contributions are open",
        )
        contributing.write_text(content, encoding="utf-8")
        self.assert_invalid("contribution")


if __name__ == "__main__":
    unittest.main()

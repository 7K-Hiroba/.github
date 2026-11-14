# Agent guidance

## Scope

This repository owns the Hiroba organization profile, approved brand assets, and default community health files. The `7K-Hiroba/community` repository owns governance and the canonical Hiroba CLA status hub. Do not duplicate legal agreement text here.

`7K-Group/7k-design-system` and every other source repository are read-only references. Never change organization visibility, avatar, social, featured-repository, Pages, CLA, GHCR, or production settings without the applicable explicit gate.

## Required checks

Run from the repository root before submitting changes:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_profile.py --root .
python3 scripts/check_markdown_links.py --root .
python3 scripts/validate_workflow_pins.py .github/workflows
git diff --check
```

All non-local `uses:` references require a full 40-character commit SHA and a human-readable version comment. Keep tokens read-only and never add publishing credentials or jobs.

## Brand and legal sources

Record the immutable design-system commit, source/output hashes, exact color or structural changes, rendering commands, and license/trademark notices in `profile/assets/NOTICE.md`. Do not recolor Inari artwork or introduce another source mark. Link the canonical Inari CLA overview and the Hiroba status hub; never collect signatures or signer data in git.

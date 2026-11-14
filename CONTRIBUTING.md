# Contributing to Hiroba

## Current status

**External contributions are currently paused.** Bug reports and feature requests may still be welcome, but maintainers must not merge external pull requests until the separate A6 contribution gate is complete. GitHub may still technically permit forks and pull requests; their existence is not eligibility for review or merge.

The canonical [ICLA](https://github.com/7K-Inari/inari-docs/blob/main/docs/legal/cla/icla.md), [CCLA](https://github.com/7K-Inari/inari-docs/blob/main/docs/legal/cla/ccla.md), and [CLA status](https://github.com/7K-Inari/inari-docs/blob/main/docs/legal/cla/README.md) remain draft/inactive for Hiroba pending owner/counsel confirmation of explicit `7K-Hiroba` coverage. Also see the Hiroba [CLA status hub](https://github.com/7K-Hiroba/community/blob/main/CLA.md). Do not duplicate legal agreement text into issues, pull requests, or this repository.

A future click-through CLA Assistant flow is **not live**. A DCO `Signed-off-by` line is not a substitute. Do not email signed agreements, attach them to issues or pull requests, or commit signer information.

## Maintainer-authored changes

While external contributions are paused, authorized maintainers should:

1. Create a focused branch from `main` and open a draft pull request.
2. Keep profile, asset, legal, security, and CI changes within their CODEOWNERS review areas.
3. Add or update tests and documentation for changed behavior.
4. Use Conventional Commit titles and record every validation command actually run, plus anything not run.
5. Confirm there are no secrets, personal/signer data, tenant details, or vulnerability reports in the change.

Run the checks documented in [AGENTS.md](AGENTS.md). Immutable full-SHA workflow references and read-only tokens are required.

## After external contributions reopen

Focused branches, tests, documentation, and Conventional Commits will remain required. Authors will then follow the activated CLA check and CODEOWNERS review process. Until that separate announcement, the paused status above remains authoritative.

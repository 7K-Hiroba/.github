<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/7K-Hiroba/.github/main/profile/assets/icon-hiroba.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/7K-Hiroba/.github/main/profile/assets/icon-hiroba-light.svg">
    <img alt="Hiroba community mark derived from the 7K Group logo in dark green" src="https://raw.githubusercontent.com/7K-Hiroba/.github/main/profile/assets/icon-hiroba.svg" width="144">
  </picture>

# Hiroba

  **The community home for Inari extensions, catalog packages, scaffold templates, Helm charts, and observability assets.**

  Pre-v1 · Active development · Apache-2.0
</div>

## A community built around applications

Hiroba follows a one-repository-per-application model. Each application can own its plugin, catalog packages, templates, OCI Helm charts, and observability assets with an independent lifecycle. Platform-critical packages remain in Inari core; community capabilities live here.

The shared [workflows library](https://github.com/7K-Hiroba/workflows) provides immutable, SHA-pinned CI/CD building blocks. The trusted-publishing direction uses signed OCI artifacts, verified identities, provenance, and test evidence; these capabilities are adopted only as the corresponding repositories and gates become available.

The `argocd` and `monitoring` applications are planned identities, not published application repositories. The private `community` and `.github` repositories will receive public links only after the separate public-launch gate.

## Documentation and community

- [Inari documentation](https://docs.7kgroup.org/inari/)
- [Contribution status and paused-contribution policy](../CONTRIBUTING.md)
- [Canonical CLA approval status](https://github.com/7K-Inari/inari-docs/blob/main/docs/legal/cla/README.md)
- [Security and private disclosure](../SECURITY.md)
- [Apache License 2.0](../LICENSE)
- [Brand asset provenance](assets/NOTICE.md)

Hiroba, Inari, and 7K names and marks remain subject to their owners' brand and trademark rights. The community trademark policy is maintained in `community/TRADEMARKS.md`; its public link will be added with the public launch. Asset licensing grants no trademark rights.

The legacy Hiroba website is not linked while its superseded content is being replaced. For current contact, use the [7K Group contact page](https://7kgroup.org/contact) or [7K Group on LinkedIn](https://www.linkedin.com/company/7kgroup).

## Contributing

**External contributions are currently paused.** Bug reports and focused feature requests may still be useful, but maintainers must not merge external pull requests before the separate contribution/CLA gate. The canonical ICLA/CCLA documents remain drafts and CLA Assistant is not active. Do not email or attach signed agreements.

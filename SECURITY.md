# Security policy

## Private reporting only

Report suspected vulnerabilities privately. Do **not** use public issues, discussions, or pull requests for vulnerability reports, exploit details, secrets, tenant data, or unredacted logs.

The `security@7kgroup.org` mailbox is not published as a confirmed channel while ORG-2 ownership verification is pending. Until its owner confirms it is live, use the [7K Group contact page](https://7kgroup.org/contact) for initial private coordination **without sensitive details**. Ask for a secure channel before sending reproduction material.

A useful initial report identifies the affected repository and version/commit, impact, high-level reproduction conditions, and a safe contact route. Do not include credentials or customer data. Coordinated disclosure timelines are agreed with the maintainers; no response-time SLA is invented here.

For vulnerabilities in third-party dependencies or services, report to the relevant upstream owner as well when appropriate, without duplicating sensitive details publicly.

## Supported versions

The organization-profile and governance repositories are unversioned: only `main` is supported. Independently versioned application repositories support the latest minor release of each component unless their own security policy states otherwise.

Hiroba is pre-v1 and under active development. Security review, provenance, and trusted-publishing requirements do not imply production readiness.

# Security Policy

## Reporting vulnerabilities

Please report vulnerabilities through GitHub Security Advisories when this
project is hosted on GitHub. If advisories are not enabled, open an issue that
describes the impact without publishing live credentials, exploit tokens, or
private target details.

## Scope

Relevant issues include:

- scanner bypasses that hide high-risk agent behavior
- rules that encourage unsafe remediation
- command execution or file write behavior introduced into the CLI
- supply-chain risks in project metadata, packaging, or CI
- examples that accidentally include real credentials

## Design constraints

The CLI should remain local-first, dependency-light, and transparent. It should
not upload repository contents or credentials to third-party services by
default.

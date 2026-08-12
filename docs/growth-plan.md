# Growth Plan

This project should earn attention by solving real maintainer problems, not by
inflating metrics.

## Target Users

- maintainers adding Codex, MCP, plugins, or skills to repositories
- security reviewers checking agent-related pull requests
- open source projects with CI scripts and contributor-submitted automation
- developers who want a local first-pass scanner before merging agent config

## Near-Term Work

1. Add SARIF output for GitHub code scanning.
2. Add diff-only scanning for pull requests.
3. Add policy packs for Codex, MCP, GitHub Actions, npm, and Python.
4. Publish examples of real attack surfaces using synthetic fixtures.
5. Improve false-positive handling with baselines and inline suppressions.

## Star-Worthy Positioning

The README should stay practical:

- show a command that works immediately
- show example findings
- explain why agent-enabled repositories have new review surfaces
- keep the project local-first and dependency-light
- avoid claiming adoption until it is publicly verifiable

## Outreach

- ask maintainers of agent tooling to try the scanner on non-sensitive repos
- share specific examples, not generic launch posts
- invite rule requests for ecosystems the scanner does not yet understand
- convert useful feedback into issues and merged PRs

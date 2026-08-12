# Agent Surface Auditor

<p align="center">
  <img src="assets/agent-surface-auditor-avatar.png" alt="Agent Surface Auditor logo" width="160">
</p>

Languages: [English](README.md) | [繁體中文](README.zh-TW.md)

Agent Surface Auditor is a small CLI for reviewing AI-agent-enabled repositories.
It scans codebases for files and patterns that can affect agent behavior: shell
commands, network access, filesystem writes, credential exposure, CI scripts,
Codex/Cursor/Claude-style instructions, MCP configs, plugins, and skills.

The goal is to give maintainers a fast first pass before merging third-party
contributions that change how coding agents read files, run commands, call APIs,
or handle secrets.

## Why this exists

AI coding agents increasingly execute repository instructions, local tools,
build scripts, MCP servers, and plugin-like extensions. A normal pull request can
therefore change more than application logic; it can alter what an agent is
allowed or encouraged to do.

This project focuses on practical review signals:

- prompt-injection text in repository instructions
- shell commands that delete, overwrite, download, or execute remote content
- CI or package scripts that run on contributor code
- suspicious credential patterns and committed environment files
- agent config files such as `AGENTS.md`, `.codex/config.toml`, MCP configs,
  skills, plugins, and tool manifests
- unreviewed network calls in scripts that agents may execute

## Install

```bash
python -m pip install -e .
```

No runtime dependency is required beyond Python 3.10+.

## Usage

```bash
agent-surface-auditor path/to/repo
agent-surface-auditor path/to/repo --format markdown
agent-surface-auditor path/to/repo --fail-on high
```

Example:

```bash
agent-surface-auditor . --format markdown
```

## Output

Findings include:

- severity: `info`, `low`, `medium`, `high`
- category: `agent-config`, `secret`, `shell-risk`, `network`, `ci`, or
  `prompt-injection`
- file and line number
- a short review recommendation

## Project Status

This is an early, intentionally small tool. The scanner is heuristic and meant
to support human review, not replace security analysis. False positives are
expected; rules should stay readable and easy to improve through pull requests.

## Roadmap

- baseline files for known findings
- GitHub Actions SARIF output
- rule tests for common agent frameworks
- diff-only scanning for pull requests
- policy packs for Codex, MCP, GitHub Actions, and npm/Python projects

## Contributing

Contributions are welcome when they improve review accuracy, reduce false
positives, or add coverage for agent/tool ecosystems. Please include tests for
new rules.

## License

MIT

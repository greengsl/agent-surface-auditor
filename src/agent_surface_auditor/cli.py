from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .scanner import Finding, scan


EXIT_BY_SEVERITY = {
    "info": {"info", "low", "medium", "high"},
    "low": {"low", "medium", "high"},
    "medium": {"medium", "high"},
    "high": {"high"},
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="agent-surface-auditor",
        description="Scan repositories for AI-agent attack-surface review signals.",
    )
    parser.add_argument("path", type=Path, help="Repository or directory to scan.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--fail-on", choices=("info", "low", "medium", "high"), default=None)
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"Path does not exist: {args.path}", file=sys.stderr)
        return 2

    findings = scan(args.path)
    if args.format == "markdown":
        print(format_markdown(findings))
    else:
        print(json.dumps([finding.to_dict() for finding in findings], indent=2))

    if args.fail_on and any(f.severity in EXIT_BY_SEVERITY[args.fail_on] for f in findings):
        return 1
    return 0


def format_markdown(findings: list[Finding]) -> str:
    if not findings:
        return "# Agent Surface Audit\n\nNo findings."

    lines = [
        "# Agent Surface Audit",
        "",
        "| Severity | Category | File | Line | Finding | Recommendation |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for finding in findings:
        lines.append(
            "| {severity} | {category} | `{path}` | {line} | {message} | {recommendation} |".format(
                severity=finding.severity,
                category=finding.category,
                path=finding.path,
                line=finding.line,
                message=escape_cell(finding.message),
                recommendation=escape_cell(finding.recommendation),
            )
        )
    return "\n".join(lines)


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


if __name__ == "__main__":
    raise SystemExit(main())

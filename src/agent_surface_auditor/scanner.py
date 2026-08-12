from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

from .rules import AGENT_CONFIG_NAMES, AGENT_CONFIG_PARTS, RULES, SCRIPT_SUFFIXES


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    category: str
    path: str
    line: int
    message: str
    recommendation: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
}


def scan(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []

    for file_path in iter_files(root):
        rel_path = file_path.relative_to(root).as_posix()
        if is_agent_surface(file_path, rel_path):
            findings.append(
                Finding(
                    rule_id="surface.agent-relevant-file",
                    severity="info",
                    category="agent-config",
                    path=rel_path,
                    line=1,
                    message="File can influence agents, tools, CI, or command execution.",
                    recommendation="Review changes to this file with agent behavior and maintainer trust in mind.",
                )
            )

        if should_scan_text(file_path):
            findings.extend(scan_text_file(file_path, rel_path))

    return sorted(findings, key=lambda item: (severity_rank(item.severity), item.path, item.line))


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.stat().st_size <= 1_000_000:
            yield path


def is_agent_surface(file_path: Path, rel_path: str) -> bool:
    if file_path.name in AGENT_CONFIG_NAMES:
        return True
    normalized = rel_path.replace("\\", "/")
    return any(part in normalized for part in AGENT_CONFIG_PARTS)


def should_scan_text(file_path: Path) -> bool:
    if file_path.name in AGENT_CONFIG_NAMES:
        return True
    if file_path.name in {".env", ".env.local", ".npmrc", ".pypirc"}:
        return True
    return file_path.suffix.lower() in SCRIPT_SUFFIXES or file_path.suffix.lower() in {".md", ".json", ".toml"}


def scan_text_file(file_path: Path, rel_path: str) -> list[Finding]:
    try:
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []

    findings: list[Finding] = []
    for index, line in enumerate(lines, start=1):
        for rule in RULES:
            if rule.pattern.search(line):
                findings.append(
                    Finding(
                        rule_id=rule.rule_id,
                        severity=rule.severity,
                        category=rule.category,
                        path=rel_path,
                        line=index,
                        message=rule.message,
                        recommendation=rule.recommendation,
                    )
                )
    return findings


def severity_rank(severity: str) -> int:
    return {"high": 0, "medium": 1, "low": 2, "info": 3}.get(severity, 9)

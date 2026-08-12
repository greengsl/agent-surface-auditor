from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    category: str
    pattern: re.Pattern[str]
    message: str
    recommendation: str


RULES: tuple[Rule, ...] = (
    Rule(
        "secret.generic-api-key",
        "high",
        "secret",
        re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
        "Possible hardcoded credential.",
        "Move secrets to a managed secret store and rotate exposed values.",
    ),
    Rule(
        "secret.openai-key",
        "high",
        "secret",
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        "Possible OpenAI API key.",
        "Remove the key from git history if real, rotate it, and load it from environment.",
    ),
    Rule(
        "shell.remote-exec",
        "high",
        "shell-risk",
        re.compile(r"(?i)(curl|wget|irm|iwr).*(\|\s*(sh|bash|pwsh|powershell|python|node)|Invoke-Expression|iex)"),
        "Remote content appears to be executed directly.",
        "Download, verify checksum/signature, and execute only reviewed local content.",
    ),
    Rule(
        "shell.destructive-delete",
        "high",
        "shell-risk",
        re.compile(r"(?i)(rm\s+-rf\s+[/~*$]|Remove-Item\s+.*-Recurse|del\s+/s\s+/q|rmdir\s+/s)"),
        "Destructive filesystem command.",
        "Constrain deletes to explicit workspace paths and add guard checks.",
    ),
    Rule(
        "network.exfiltration-shape",
        "medium",
        "network",
        re.compile(r"(?i)(curl|wget|fetch|requests\.(post|put)|axios\.(post|put)).*(env|\.env|token|secret|key)"),
        "Network request may include credentials or environment data.",
        "Confirm the destination, payload, and user consent before allowing this call.",
    ),
    Rule(
        "prompt.ignore-instructions",
        "medium",
        "prompt-injection",
        re.compile(r"(?i)(ignore|bypass|override).{0,40}(previous|system|developer|safety|instructions)"),
        "Instruction text resembles prompt injection.",
        "Review whether this file can be read by agents and rewrite untrusted instructions as data.",
    ),
    Rule(
        "prompt.secret-request",
        "medium",
        "prompt-injection",
        re.compile(r"(?i)(print|reveal|exfiltrate|send|upload).{0,50}(secret|token|api key|credential|\.env)"),
        "Instruction text may try to expose secrets.",
        "Treat this as untrusted content and prevent agents from following it as an instruction.",
    ),
)


AGENT_CONFIG_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursorrules",
    "mcp.json",
    "skill.json",
    "plugin.json",
    "SKILL.md",
}

AGENT_CONFIG_PARTS = {
    ".codex",
    ".cursor",
    ".github/workflows",
    "skills",
    "plugins",
    "mcp",
}

SCRIPT_SUFFIXES = {
    ".bat",
    ".cmd",
    ".js",
    ".mjs",
    ".ps1",
    ".py",
    ".sh",
    ".ts",
    ".yml",
    ".yaml",
}

# OpenAI Codex for Open Source Application Draft

This draft is intentionally conservative. Replace the placeholders after the
GitHub repository is public and has verifiable public metrics.

## Repository

- GitHub repository: `TODO: https://github.com/<user-or-org>/agent-surface-auditor`
- GitHub username: `TODO`
- Role: `Creator and primary maintainer`
- Public metrics: `TODO: stars, forks, contributors, open issues, merged PRs`

## 1. Explain Your Role

### Recommended English

I am the creator and primary maintainer of this repository. I maintain the
scanner rules, CLI behavior, documentation, issue triage, release process, and
review of third-party contributions.

### 中文翻譯

我是這個倉庫的創建者與主要維護者。我負責掃描規則、CLI 行為、文件、issue
整理、發布流程，以及第三方貢獻的審查。

### Why This Works

It states concrete maintainer responsibilities without overstating community
size.

## 2. Why This Repository Qualifies

### Recommended English

Agent Surface Auditor is an open source CLI that helps maintainers review
AI-agent-enabled repositories. It detects risky agent instructions, MCP/plugin
configs, CI scripts, shell commands, network calls, and possible secrets before
they are merged. Its value is practical review support for projects adopting
Codex, MCP, skills, plugins, and similar agent tooling.

### 中文翻譯

Agent Surface Auditor 是一個開源 CLI，幫助維護者審查啟用 AI agent 的倉庫。
它會在合併前偵測高風險 agent 指令、MCP/plugin 設定、CI 腳本、shell 命令、
網路請求與疑似憑證。它的價值是支援正在導入 Codex、MCP、skills、plugins
等 agent 工具的專案做實際審查。

### Why This Works

It describes the repo's purpose, target ecosystem, and concrete functionality.

## 3. Why The Project Needs Codex Security

### Recommended English

This project reviews files that can influence agent behavior and maintainer
automation, including repository instructions, CI, scripts, MCP configs, skills,
and plugin manifests. A malicious contribution could hide prompt injection,
remote command execution, credential exfiltration, destructive filesystem
actions, or unsafe network calls inside examples or rules. Codex Security would
help review these attack surfaces before releases.

### 中文翻譯

這個專案審查會影響 agent 行為與維護自動化的檔案，包括倉庫指令、CI、腳本、
MCP 設定、skills 與 plugin manifests。惡意貢獻可能在範例或規則中藏入
prompt injection、遠端命令執行、憑證外洩、破壞性檔案操作或不安全網路請求。
Codex Security 可協助在發布前審查這些攻擊面。

### Why This Works

It names specific attack paths rather than saying only "improve security."

## 4. How API Credits Will Be Used

### Recommended English

I would use API credits for maintainer automation: summarizing pull requests,
classifying rule changes by risk, generating regression tests for new attack
patterns, producing security-review notes for CI findings, and drafting release
notes from merged changes. These workflows would support review quality while
keeping final decisions with maintainers.

### 中文翻譯

我會把 API 額度用於維護自動化：整理 pull requests、依風險分類規則變更、為新
攻擊模式產生回歸測試、根據 CI findings 產生安全審查備註，以及從已合併變更
草擬 release notes。這些流程會提升審查品質，但最終決策仍由維護者負責。

### Why This Works

It gives concrete, bounded API use cases tied to open source maintenance.

## 5. Anything Else To Add

### Recommended English

The project is early-stage and does not claim package downloads or adoption that
cannot be verified. I plan to track public signals such as stars, forks,
contributors, issues, merged PRs, and real integrations as the basis for future
maintenance and application updates.

### 中文翻譯

這個專案仍在早期階段，不會宣稱無法驗證的套件下載量或採用數據。我會以 stars、
forks、contributors、issues、merged PRs 與真實整合作為後續維護和更新申請資料
的依據。

### Why This Works

It is honest about the current stage and avoids inflated metrics.

## Most Recommended Submission Version

### Explain Your Role

I am the creator and primary maintainer of this repository. I maintain the
scanner rules, CLI behavior, documentation, issue triage, release process, and
review of third-party contributions.

### Why This Repository Qualifies

Agent Surface Auditor is an open source CLI that helps maintainers review
AI-agent-enabled repositories. It detects risky agent instructions, MCP/plugin
configs, CI scripts, shell commands, network calls, and possible secrets before
they are merged. Its value is practical review support for projects adopting
Codex, MCP, skills, plugins, and similar agent tooling.

### Why The Project Needs Codex Security

This project reviews files that can influence agent behavior and maintainer
automation, including repository instructions, CI, scripts, MCP configs, skills,
and plugin manifests. A malicious contribution could hide prompt injection,
remote command execution, credential exfiltration, destructive filesystem
actions, or unsafe network calls inside examples or rules. Codex Security would
help review these attack surfaces before releases.

### How API Credits Will Be Used

I would use API credits for maintainer automation: summarizing pull requests,
classifying rule changes by risk, generating regression tests for new attack
patterns, producing security-review notes for CI findings, and drafting release
notes from merged changes. These workflows would support review quality while
keeping final decisions with maintainers.

### Anything Else

The project is early-stage and does not claim package downloads or adoption that
cannot be verified. I plan to track public signals such as stars, forks,
contributors, issues, merged PRs, and real integrations as the basis for future
maintenance and application updates.

# Agent Surface Auditor

語言：[English](README.md) | [繁體中文](README.zh-TW.md)

Agent Surface Auditor 是一個小型 CLI，用來協助審查已導入 AI agent 的程式碼倉庫。
它會掃描可能影響 agent 行為的檔案與模式，例如 shell 命令、網路存取、檔案系統寫入、
憑證暴露、CI 腳本、Codex/Cursor/Claude 類型的倉庫指令、MCP 設定、plugins 與
skills。

這個工具的目標，是讓維護者在合併第三方貢獻前，先快速檢查那些可能改變 coding
agent 如何讀取檔案、執行命令、呼叫 API 或處理 secrets 的變更。

## 為什麼需要這個工具

AI coding agents 越來越常執行倉庫內的指令、local tools、build scripts、MCP servers
與類 plugin 擴充。因此，一個普通 pull request 可能改變的不只是應用程式邏輯，也可能
改變 agent 被允許或被引導去做的事情。

這個專案專注在實務審查訊號：

- 倉庫指令中的 prompt injection 文字
- 會刪除、覆寫、下載或執行遠端內容的 shell 命令
- 會在貢獻者程式碼上執行的 CI 或 package scripts
- 可疑的憑證模式與被提交的環境設定檔
- `AGENTS.md`、`.codex/config.toml`、MCP configs、skills、plugins 與 tool manifests
  等 agent 設定檔
- agent 可能執行的 scripts 中尚未審查的網路請求

## 安裝

```bash
python -m pip install -e .
```

除了 Python 3.10+ 之外，執行時不需要額外依賴。

## 使用方式

```bash
agent-surface-auditor path/to/repo
agent-surface-auditor path/to/repo --format markdown
agent-surface-auditor path/to/repo --fail-on high
```

範例：

```bash
agent-surface-auditor . --format markdown
```

## 輸出

每個 finding 會包含：

- 嚴重程度：`info`、`low`、`medium`、`high`
- 分類：`agent-config`、`secret`、`shell-risk`、`network`、`ci` 或 `prompt-injection`
- 檔案與行號
- 簡短的審查建議

## 專案狀態

這是一個早期、刻意保持小範圍的工具。掃描器採用 heuristic 規則，目的是輔助人工審查，
不是取代完整安全分析。誤報是預期中的情況；規則應保持可讀、可討論，並能透過 pull
requests 持續改進。

## Roadmap

- 已知 findings 的 baseline 檔案
- GitHub Actions SARIF 輸出
- 常見 agent frameworks 的規則測試
- pull request 的 diff-only 掃描
- Codex、MCP、GitHub Actions、npm 與 Python 專案的 policy packs

## 貢獻

如果貢獻能提升審查準確度、降低誤報，或增加 agent/tool 生態的覆蓋範圍，歡迎提出。
新增規則時，請一併附上測試。

## 授權

MIT

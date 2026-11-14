# 每日更新作業手冊（給 AI Agent）

本 repo 是繁體中文的 AI Agent / MCP 開源專案精選清單。每天的排程任務照以下步驟執行。

## 檔案

- `data/projects.yml`：唯一資料來源。**只改這裡**，README 與網站由 `scripts/build.py` 產生。
- `data/stats.json`：星星數等數據，由 `python scripts/build.py --refresh` 從 GitHub API 取得，**不可手動編寫**。
- `daily/YYYY-MM-DD.md`：每日更新文章（台北時間日期）。
- `weekly/YYYY-Www.md`：每週精選（每週日產出）。

## 每日流程

1. **同步**：`git fetch origin main && git checkout -B daily/YYYY-MM-DD origin/main`。
2. **蒐集候選**（目標 15～30 個）：
   - GitHub Search API：`created:>{7天前} stars:>200`，加上 topic 條件如 `topic:mcp-server`、`topic:ai-agents`、`topic:agent-framework`、`topic:coding-agent`、`topic:browser-automation`、`topic:agent-skills`。
   - 再用網路搜尋看 Hacker News、Reddit（r/LocalLLaMA、r/ClaudeAI）、官方部落格近 2 天提到的 Agent／MCP 專案。
3. **篩選**，全部符合才收錄：
   - 跟 AI Agent、MCP、Agent 工具鏈直接相關
   - 未封存、最近 30 天有 commit、有授權條款、README 有說明用途
   - 不在 `projects.yml` 裡（repo 名稱不分大小寫比對）
   - 排除：外洩的系統提示、繞過付費或服務條款的工具、自動海投履歷、未授權下載影音、加密貨幣炒作、明顯的灌星專案
4. **挑 3～5 個**最值得介紹的，閱讀 README 後撰寫：
   - `summary`：一句話，說清楚它做什麼。用自己的話寫，不要翻譯或複製 README。
   - `for`：適合誰。
   - `note`：有需要才寫（AGPL 授權、需要付費 API、有安全風險、仍在早期開發等）。
   - 加進 `projects.yml` 最合適的分類，`added` 填當天日期。真的沒有合適分類才新增。
5. **寫每日文章** `daily/YYYY-MM-DD.md`，格式參考 `daily/2026-11-10.md`：
   - 標題：`# YYYY-MM-DD 一句話點出今日主題`
   - 一段引言（2～3 句）說明今天的趨勢或亮點
   - 「今日新收錄」：每個專案 2～3 句短評，說明為什麼值得看、跟現有工具比有什麼不同
   - 可選「值得一提」：已收錄專案的重大版本更新
6. **產生並檢查**：`python scripts/build.py --check && python scripts/build.py --refresh`，確認沒有錯誤，也沒有「找不到」的警告。這一步只是驗證，產生的檔案不提交。
7. **提交**：只 commit 人工編寫的檔案：`data/projects.yml`、`daily/`、`weekly/`（以及本次有改到的 `AGENTS.md`、`scripts/`）。**不要提交** `README.md`、`data/stats.json`、`docs/`，先用 `git checkout -- README.md data/stats.json docs/ && git clean -fd docs/` 還原。這些檔案由 GitHub Actions（`.github/workflows/build.yml`）在合併到 main 後自動重新產生；PR 若一起提交，main 每天 08:17 的定時更新就會跟它衝突。
   - commit 訊息用 `daily: YYYY-MM-DD 新增 N 個專案`，推送分支並開 PR 到 main，PR 描述列出新增的專案和簡短理由。
   - repo 設定改為「自動發布」後，改成直接推送到 main。

## 每週日額外工作

- 寫 `weekly/YYYY-Www.md`：本週新收錄中最值得看的 5 個，再加一段趨勢觀察。
- 清理：stats 標示 `archived: true` 的專案從清單移除；超過 180 天沒更新的專案評估是否移除，或在 `note` 註明。

## 寫作風格

- 台灣用語、繁體中文：程式碼、伺服器、資料庫、函式庫、介面、預設、支援。
- 專有名詞保留英文：Agent、MCP、RAG、LLM、token。
- 中英文之間不刻意加空格，跟現有內容保持一致。
- 不誇大、不行銷腔。不確定的事不寫。

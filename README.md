# Awesome AI Agents 繁體中文精選

> 精選 AI Agent、MCP 與相關開源工具，每天更新，附繁體中文導讀。

目前收錄 **87** 個專案 · 數據更新：2026-11-27 · [網站版](https://markforcode.github.io/awesome-ai-agents/) · [RSS](https://markforcode.github.io/awesome-ai-agents/feed.xml)

每個專案都附「一句話介紹」和「適合誰」。⭐ 星星數、授權與更新狀態每天由 GitHub API 自動同步。

## 🆕 最近更新

- [2026-11-17](daily/2026-11-17.md)
- [2026-11-16](daily/2026-11-16.md)
- [2026-11-15](daily/2026-11-15.md)
- [2026-11-14](daily/2026-11-14.md)
- [2026-11-13](daily/2026-11-13.md)
- [2026-11-12](daily/2026-11-12.md)
- [2026-11-11](daily/2026-11-11.md)

## 目錄

- [入門學習](#learn)（7）
- [Agent 開發框架](#frameworks)（11）
- [程式開發 Agent](#coding)（12）
- [瀏覽器與電腦操作](#browser)（12）
- [MCP 伺服器與 SDK](#mcp)（12）
- [記憶與上下文](#memory)（6）
- [網頁資料擷取](#scraping)（3）
- [無程式碼平台與自架介面](#platforms)（8）
- [研究與通用 Agent](#research)（4）
- [外掛、技能與其他清單](#lists)（12）

<a id="learn"></a>

## 入門學習

從零開始理解 AI Agent 與 MCP 的課程、教材與指南。

- **[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** · ⭐ 81.1k · Jupyter Notebook · MIT  
  微軟出的 18 堂 AI Agent 入門課，每堂都有講義和可執行的範例程式。  
  👤 **適合**：第一次接觸 Agent、想有系統學起來的開發者
- **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** · ⭐ 81.0k · Python · MIT  
  從零打造一個類似 Claude Code 的迷你 Agent，一步步拆解「Agent 外殼」是怎麼運作的。  
  👤 **適合**：好奇程式碼 Agent 內部原理的人
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · ⭐ 80.4k · MDX · MIT · 💤 半年未更新  
  提示工程經典指南，內容已擴充到 context engineering、RAG 與 Agent。  
  👤 **適合**：所有要跟 LLM 打交道的人　⚠️ 2026 年 3 月後就沒有新的 commit，較新的技巧可能還沒收進來
- **[huggingface/agents-course](https://github.com/huggingface/agents-course)** · ⭐ 35.5k · MDX · Apache-2.0  
  Hugging Face 的免費 Agent 課程，涵蓋 smolagents、LangChain、LlamaIndex 等主流工具。  
  👤 **適合**：想邊學邊動手、順便比較不同框架的人
- **[NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)** · ⭐ 25.1k · Jupyter Notebook  
  50 多個 Agent 技巧的教學與實作，從簡單的聊天機器人到複雜的多 Agent 系統都有。  
  👤 **適合**：想找具體範例參考的開發者
- **[NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)** · ⭐ 22.0k · Jupyter Notebook  
  以程式碼為主的教學，示範 Agent 從原型走到正式上線要處理的部署、監控、安全等問題。  
  👤 **適合**：準備把 Agent 放進正式產品的團隊
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · ⭐ 17.7k · Jupyter Notebook · MIT  
  MCP（Model Context Protocol）入門教材，用 Python、TypeScript、Java、C# 等多種語言示範怎麼寫 MCP server 和 client。  
  👤 **適合**：想自己寫 MCP 工具的開發者

<a id="frameworks"></a>

## Agent 開發框架

用程式碼打造自己的 Agent。

- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · ⭐ 150.1k · Python · MIT  
  最多人用的 LLM 應用框架，串接模型、工具、資料來源的生態系最完整。  
  👤 **適合**：需要大量現成整合的專案　⚠️ 抽象層較多，簡單需求可能殺雞用牛刀
- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · ⭐ 71.5k · Python · MIT · 💤 半年未更新  
  模擬一間軟體公司，讓產品經理、架構師、工程師等 Agent 協作寫出軟體。  
  👤 **適合**：研究多 Agent 角色分工的人　⚠️ 2026 年 1 月後就沒有新的 commit，維護狀況不明，正式專案使用前先評估
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · ⭐ 62.0k · Python · CC-BY-4.0 · 🗄️ 已封存  
  微軟的多 Agent 對話框架，學術界和研究原型常用。  
  👤 **適合**：研究多 Agent 互動的開發者
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · ⭐ 61.3k · Python · MIT  
  讓多個扮演不同角色的 Agent 分工合作，例如研究員＋寫手＋審稿員。  
  👤 **適合**：想快速做出多 Agent 協作的人
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · ⭐ 45.5k · Python · MIT  
  用「圖」來描述 Agent 流程，能精準控制每一步、支援中斷與恢復。  
  👤 **適合**：流程複雜、需要可靠性的 Agent
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · ⭐ 43.3k · Python · Apache-2.0  
  輕量、速度快的 Python Agent 框架，內建記憶、知識庫與多 Agent 團隊。  
  👤 **適合**：想要簡潔 API 的 Python 開發者
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · ⭐ 36.8k · Python · Apache-2.0  
  阿里巴巴開源的多 Agent 框架，強調流程透明、可觀察，支援 MCP。  
  👤 **適合**：需要看清楚 Agent 每一步在做什麼的人
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · ⭐ 27.1k · Python · Apache-2.0  
  以模組化管線為核心的框架，特別擅長檢索（RAG）和可控的 Agent 流程。  
  👤 **適合**：以文件檢索為主的企業應用
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · ⭐ 25.6k · Apache-2.0  
  前身是 MemGPT，打造有長期記憶、會隨使用持續學習的 Agent。  
  👤 **適合**：需要 Agent 記住使用者的應用
- **[google/adk-python](https://github.com/google/adk-python)** · ⭐ 22.4k · Python · Apache-2.0  
  Google 官方 Agent Development Kit，涵蓋開發、評估到部署。  
  👤 **適合**：使用 Gemini 或 Google Cloud 的團隊
- **[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)** · ⭐ 21.4k · Python · MIT  
  Pydantic 團隊出品，從輸入到輸出都有完整型別檢查的 Agent 框架。  
  👤 **適合**：重視型別安全、習慣 FastAPI 風格的人

<a id="coding"></a>

## 程式開發 Agent

在終端機或編輯器裡幫你寫程式的 Agent。

- **[stablyai/orca](https://github.com/stablyai/orca)** · ⭐ 141.3k · TypeScript · MIT  
  同時管理一整隊程式 Agent（Claude Code、Codex 等），用你自己的訂閱，支援桌面、手機與遠端執行。  
  👤 **適合**：想讓多個 Agent 平行工作的人
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · ⭐ 109.2k · TypeScript · Apache-2.0  
  Google 開源的終端機 Agent，直接在命令列用 Gemini 讀寫程式碼、執行指令。  
  👤 **適合**：想要免費額度、在終端機工作的開發者
- **[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)** · ⭐ 69.0k · Rust · Apache-2.0  
  老牌開源專案，現在定位為給開源模型（Kimi、GLM 等）用的程式 Agent，以 Rust 改寫。  
  👤 **適合**：想在本機用開源模型寫程式的人
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · ⭐ 57.1k · Rust · Apache-2.0  
  可擴充的開源 Agent，不只建議程式碼，還能安裝套件、執行、測試，支援任何 LLM 與 MCP。  
  👤 **適合**：想要不綁定模型廠商的程式 Agent
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · ⭐ 41.1k · TypeScript · MIT  
  Claude Code 的多 Agent 協作外掛，讓多個 Agent 分工處理大型任務。  
  👤 **適合**：重度 Claude Code 使用者
- **[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)** · ⭐ 31.0k · TypeScript · Apache-2.0  
  通義千問團隊的終端機程式 Agent，針對 Qwen 系列模型最佳化。  
  👤 **適合**：想用開源模型寫程式的人
- **[charmbracelet/crush](https://github.com/charmbracelet/crush)** · ⭐ 29.2k · Go  
  Charm 團隊出品、介面很漂亮的終端機程式 Agent，支援多家模型。  
  👤 **適合**：重視終端機體驗的開發者
- **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** · ⭐ 6.7k · TypeScript · MIT  
  讓 Claude Code、Codex 等命令列 Agent 依規則在背景接手定時任務或 GitHub issue 等事件，需要人決定時才推卡片到飛書、Slack、Discord 或桌面通知。  
  👤 **適合**：想讓命令列 Agent 在沒人盯著時持續工作的人　⚠️ 文件以簡體中文為主；需要 Node 24 以上
- **[alexeyw/lot-map](https://github.com/alexeyw/lot-map)** · ⭐ 1.2k · TypeScript · MIT  
  Claude Code 外掛，在對話旁開一個即時地圖，工具呼叫、模型請求、hook、技能和子 Agent 執行時會亮起對應的站點，也顯示 context 用量與錯誤。  
  👤 **適合**：想一眼看懂 Claude Code 正在做什麼、卡在哪裡的人　⚠️ 作者在 macOS 上開發測試；終端機版需要至少 144 欄寬
- **[devvmhq/devvm](https://github.com/devvmhq/devvm)** · ⭐ 814 · Go · MIT  
  每個專案資料夾開一台獨立的 Lima 虛擬機，自動偵測需要的工具鏈，讓 Claude Code、Codex 等 Agent 在裡面工作，預設只能連到允許的網域。  
  👤 **適合**：想讓程式 Agent 放手做事、又不想讓它碰到本機的人　⚠️ 支援 macOS 13 以上與 Linux；作者提醒沙盒無法堵住所有漏洞，使用前先看安全說明
- **[leostera/git-twig](https://github.com/leostera/git-twig)** · ⭐ 305 · Rust · MIT  
  git 子指令，在 APFS、Btrfs 等支援寫入時複製的檔案系統上建立共用檔案內容的 worktree，讓多個 Agent 各開一份工作目錄時不必重複佔用硬碟空間。  
  👤 **適合**：常讓多個程式 Agent 同時在不同 worktree 工作、大型 repo 很吃空間的人　⚠️ 一般 ext4 不支援，會改用原本的 git worktree；小型 repo 建立速度反而比較慢
- **[stevenmichaelthomas/numbrone](https://github.com/stevenmichaelthomas/numbrone)** · ⭐ 146 · Shell · MIT  
  架在 herdr 上的 Agent 分工 Skill：你只跟一個總管 Agent 下需求，它判斷屬於哪個專案再交給該專案的經理 Agent，經理開工人 Agent 各自在獨立 worktree 做事並回報。  
  👤 **適合**：同時維護好幾個專案、想讓程式 Agent 平行處理多件事的人　⚠️ 需要先安裝 herdr，只支援 macOS 與 Linux；同時跑多個 Agent 會比較耗 token

<a id="browser"></a>

## 瀏覽器與電腦操作

讓 Agent 操作網頁、桌面應用程式。

- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · ⭐ 122.2k · Python · MIT  
  讓 AI 操作瀏覽器的 Python 函式庫，能點擊、填表、跨網頁完成任務。  
  👤 **適合**：想自動化網頁操作的開發者
- **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · ⭐ 59.5k · TypeScript · Apache-2.0  
  Chrome 官方 DevTools MCP，讓程式 Agent 能看 console、網路請求、效能數據來除錯。  
  👤 **適合**：前端開發者
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · ⭐ 40.2k · TypeScript · Apache-2.0  
  微軟官方 Playwright MCP server，讓 Agent 透過結構化的頁面資訊操作瀏覽器。  
  👤 **適合**：想讓 Claude、Cursor 等工具操作網頁的人
- **[trycua/cua](https://github.com/trycua/cua)** · ⭐ 33.1k · Rust · MIT  
  電腦操作（computer-use）Agent 的基礎設施，提供跨作業系統沙盒、驅動程式和評測基準。  
  👤 **適合**：開發或訓練桌面操作 Agent 的人
- **[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)** · ⭐ 23.6k · Python · AGPL-3.0  
  結合 LLM 與視覺辨識的瀏覽器自動化，網站改版也不容易壞。  
  👤 **適合**：需要長期跑表單、下單等網頁流程的團隊　⚠️ AGPL-3.0 授權，商用前要留意
- **[browser-use/browser-harness](https://github.com/browser-use/browser-harness)** · ⭐ 19.3k · Python · MIT  
  讓 Claude Code、Codex、Cursor 直接使用你已登入的 Chrome，一個提示就能設定好。  
  👤 **適合**：想讓程式 Agent 存取需要登入的網站　⚠️ Agent 會以你的身分操作，要留意權限
- **[DIYgod/pinky](https://github.com/DIYgod/pinky)** · ⭐ 2.8k · Go · Apache-2.0  
  透過 MCP 讓 Agent 操作真實的 iPhone 或 Android 手機，付款等高風險步驟要你在電腦上按允許才會執行，並保留每一步的截圖與錄影。  
  👤 **適合**：想讓 Agent 代操手機 App、又要保留控制權的人　⚠️ 仍在 pre-alpha 階段
- **[vostride/agent-qa](https://github.com/vostride/agent-qa)** · ⭐ 825 · TypeScript  
  用自然語言描述使用流程，由 Agent 在網頁、Android 或 iOS 上實際操作測試，失敗時留下對應步驟的截圖；可從 CLI、儀表板或透過 MCP 從程式 Agent 呼叫，並把測試中學到的經驗存成 repo 裡可審查的檔案。  
  👤 **適合**：想讓程式 Agent 跑端對端測試的開發者與 QA 工程師　⚠️ FSL-1.1-ALv2 授權（原始碼公開，兩年後轉為 Apache-2.0，期間限制競爭用途），不是 OSI 認可的開源授權；需要 Node.js 24 以上，模型費用另計
- **[lxe/phoneuse](https://github.com/lxe/phoneuse)** · ⭐ 720 · Python · MIT  
  不越獄、不接線，用 AirPlay 把 iPhone 畫面鏡像到電腦，再讓電腦假裝成藍牙滑鼠鍵盤來操作，你或 Claude Code 等 Agent 都能點擊、輸入。  
  👤 **適合**：想讓 Agent 操作 iPhone、又不想在手機上裝特殊工具的人　⚠️ 仍是 alpha；以 Linux 為主，Mac 版需另購一塊 LilyGO T-Display 開發板當橋接器，Windows 要從原始碼安裝；手機和電腦須在同一個 Wi-Fi
- **[hridaya423/phonedriver](https://github.com/hridaya423/phonedriver)** · ⭐ 405 · Rust · AGPL-3.0  
  MCP 伺服器與 CLI，把 Android 或 iOS 畫面轉成編號清單讓 Agent 點選操作，遇到付款、刪除帳號等按鈕會先暫停問你。  
  👤 **適合**：想讓 Claude Code、Codex 等 Agent 操作手機或測試自家 App 的人　⚠️ AGPL-3.0 授權；iPhone 實機需要 Mac、Xcode 與 Apple 開發者憑證；付款按鈕偵測靠文字標籤，只有圖示的按鈕抓不到
- **[paul-nameless/agweb](https://github.com/paul-nameless/agweb)** · ⭐ 299 · Swift · MIT  
  以 WebKit 打造、專給程式 Agent 用的 macOS 瀏覽器，Agent 從終端機下類似 playwright-cli 的指令操作，視窗不搶鍵盤焦點，多個 Agent 的分頁集中在一個儀表板即時顯示。  
  👤 **適合**：同時跑好幾個程式 Agent、受不了 Playwright 視窗搶焦點的 Mac 使用者　⚠️ 需要 macOS 26 以上；只支援 WebKit，沒有 Chrome DevTools Protocol
- **[Tthanh2k6/turbo-browser-mcp](https://github.com/Tthanh2k6/turbo-browser-mcp)** · ⭐ 153 · JavaScript · MIT  
  以 Playwright 為基礎的瀏覽器 MCP 伺服器，把幾十個細碎操作合併成 10 個批次工具，只回傳頁面變動的部分，一次呼叫就能填完整份表單，以減少 token 和來回次數。  
  👤 **適合**：覺得瀏覽器 MCP 太耗 token、回合數太多的 Agent 開發者　⚠️ 個人專案、剛發布不久；效能數字來自作者自己的基準測試

<a id="mcp"></a>

## MCP 伺服器與 SDK

用 MCP 幫 Agent 接上各種工具與服務。

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · ⭐ 92.3k · TypeScript  
  MCP 官方的參考伺服器合集，包含檔案系統、Git、網頁擷取等範例。  
  👤 **適合**：想看標準寫法或找基本工具的人
- **[upstash/context7](https://github.com/upstash/context7)** · ⭐ 65.5k · TypeScript · MIT  
  即時提供最新版函式庫文件給 Agent，減少 AI 寫出舊版或不存在的 API。  
  👤 **適合**：所有用 AI 寫程式的人
- **[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)** · ⭐ 37.2k · TypeScript · Apache-2.0  
  用聊天的方式畫 draw.io 圖表，有網頁版、桌面版，也有 MCP server。  
  👤 **適合**：常畫架構圖、流程圖的人
- **[ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** · ⭐ 36.0k · Python · MIT  
  用自然語言操作 Blender 建 3D 模型（社群外掛，非官方）。  
  👤 **適合**：3D 創作者
- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · ⭐ 34.8k · Go · MIT  
  GitHub 官方 MCP server，讓 Agent 讀寫 issue、PR、程式碼與 Actions。  
  👤 **適合**：想讓 Agent 幫忙管理 GitHub 的人
- **[oraios/serena](https://github.com/oraios/serena)** · ⭐ 31.7k · Python  
  提供語意層級的程式碼搜尋與編輯，讓 Agent 像用 IDE 一樣理解大型專案。  
  👤 **適合**：在大型程式碼庫裡用 Agent 的人
- **[ComposioHQ/composio](https://github.com/ComposioHQ/composio)** · ⭐ 31.3k · TypeScript · MIT  
  一次接上 1000 多種 SaaS 工具，並處理好授權登入，省去逐一串接的麻煩。  
  👤 **適合**：要讓 Agent 操作大量外部服務的開發者
- **[modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)** · ⭐ 25.0k · Python · MIT  
  MCP 官方 Python SDK，寫 MCP server 或 client 的首選。  
  👤 **適合**：Python 開發者
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · ⭐ 23.3k · TypeScript · MIT  
  讓 Claude、Cursor 等工具直接幫你設計 n8n 自動化流程。  
  👤 **適合**：n8n 使用者
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · ⭐ 13.8k · TypeScript  
  MCP 官方 TypeScript SDK。  
  👤 **適合**：JavaScript / TypeScript 開發者
- **[shanselman/sandbox-mcp](https://github.com/shanselman/sandbox-mcp)** · ⭐ 497 · JavaScript · MIT  
  用 Windows Sandbox 開一台全新、用完即丟的 Windows 11，讓 Agent 部署並操作你的桌面程式、記錄當機與缺少的相依套件，有 CLI 也有 MCP 介面。  
  👤 **適合**：開發 Windows 桌面應用程式、想在乾淨環境測試的人　⚠️ 需要 Windows 11 24H2 以上的 Pro、Enterprise 或 Education 版
- **[claynicholson/copper-kicad-mcp](https://github.com/claynicholson/copper-kicad-mcp)** · ⭐ 123 · Python · MIT  
  把 KiCad 接上 AI 的 MCP 伺服器，讓 Agent 畫電路圖、到 LCSC 找現貨零件、佈線，每次修改後重跑 ERC/DRC，最後輸出可以送 JLCPCB 等廠商打樣的製造檔。  
  👤 **適合**：想用 AI 輔助設計 PCB 的硬體開發者與創客　⚠️ 需要 KiCad 10；Windows 測試最完整，macOS 和 Linux 安裝方式較新

<a id="memory"></a>

## 記憶與上下文

讓 Agent 記得更多、用更少 token。

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · ⭐ 120.1k · TypeScript · Apache-2.0  
  自動記錄 Agent 每次工作的內容並壓縮，下次開新對話時帶回相關記憶。  
  👤 **適合**：覺得 Claude Code 每次都「失憶」的人
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · ⭐ 81.0k · Python · Apache-2.0  
  在工具輸出、日誌、檔案送進 LLM 前先壓縮，有函式庫、代理伺服器和 MCP 三種用法。  
  👤 **適合**：想省 token 費用的人
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · ⭐ 69.5k · Python · Apache-2.0  
  Agent 的記憶層，自動記住使用者偏好與對話重點，可直接嵌入現有應用。  
  👤 **適合**：做個人化助理或客服的人
- **[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)** · ⭐ 63.8k · Python · MIT  
  會從經驗中學習的 Agent 記憶系統。  
  👤 **適合**：研究長期記憶的開發者
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · ⭐ 40.8k · Python · MIT  
  不用向量資料庫的 RAG，把文件建成目錄樹，讓 LLM 像人一樣翻目錄找答案。  
  👤 **適合**：處理長篇報告、財報、法規文件的人
- **[gogoymh/auto-ontology-mcp](https://github.com/gogoymh/auto-ontology-mcp)** · ⭐ 550 · Python · Apache-2.0  
  把 NVIDIA Auto Ontology 的語意層包成 MCP 伺服器，由你的 Agent 建立資料庫的業務詞彙並寫出經過檢查的唯讀 SQL，也能當個人知識庫用。  
  👤 **適合**：想用自然語言查公司資料庫，或想建立可查詢個人知識庫的人

<a id="scraping"></a>

## 網頁資料擷取

把網頁變成 Agent 讀得懂的資料。

- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · ⭐ 211.2k · TypeScript · AGPL-3.0  
  把整個網站爬下來轉成乾淨的 Markdown 或結構化資料，專為 LLM 設計。  
  👤 **適合**：需要餵網頁資料給 AI 的人　⚠️ AGPL-3.0 授權，也有付費雲端版
- **[D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)** · ⭐ 106.1k · Python · BSD-3-Clause  
  Python 爬蟲框架，從單一請求到大規模爬取都能處理，網站結構改變時能自動調整。  
  👤 **適合**：需要穩定爬蟲的 Python 開發者　⚠️ 請遵守目標網站的使用條款
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · ⭐ 88.0k · Python · Apache-2.0  
  開源、對 LLM 友善的爬蟲，輸出 Markdown，可以自己架設。  
  👤 **適合**：想免費自架爬蟲的開發者

<a id="platforms"></a>

## 無程式碼平台與自架介面

不太寫程式也能打造 Agent，或自架 AI 介面。

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · ⭐ 212.4k · TypeScript  
  視覺化工作流程自動化平台，內建 AI 節點，有 400 多種整合，可以自架。  
  👤 **適合**：想把 AI 接進日常工作流程的人　⚠️ fair-code 授權，不是完全的開源授權
- **[langgenius/dify](https://github.com/langgenius/dify)** · ⭐ 162.0k · Python  
  拖拉式打造 Agent 流程和 RAG 知識庫的平台，可自架或用雲端版。  
  👤 **適合**：想快速做出企業內部 AI 應用的團隊
- **[open-webui/open-webui](https://github.com/open-webui/open-webui)** · ⭐ 159.7k · Svelte  
  最受歡迎的自架 AI 聊天介面，支援 Ollama 本地模型和 OpenAI 相容 API。  
  👤 **適合**：想在本機或公司內部架 ChatGPT 的人
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · ⭐ 94.8k · Go · Apache-2.0  
  以深度文件理解為核心的 RAG 引擎，擅長處理表格、PDF 等複雜格式。  
  👤 **適合**：要做企業知識庫的團隊
- **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** · ⭐ 68.7k · JavaScript · MIT  
  本機優先的全功能 AI 應用，可以跟文件對話、執行 Agent，不必把資料交給雲端。  
  👤 **適合**：重視隱私的個人與小團隊
- **[LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)** · ⭐ 47.6k · TypeScript · MIT  
  功能完整的開源 ChatGPT 替代介面，一個介面切換多家模型，支援 Agent、MCP 與 Skills。  
  👤 **適合**：想統一管理多家模型的團隊
- **[activepieces/activepieces](https://github.com/activepieces/activepieces)** · ⭐ 25.8k · TypeScript  
  開源的 Zapier 替代品，內建約 400 個 MCP server。  
  👤 **適合**：想要開源自動化平台的人
- **[agentes-chat/agentes-chat](https://github.com/agentes-chat/agentes-chat)** · ⭐ 2.1k · TypeScript · AGPL-3.0  
  可自架的團隊聊天軟體，Agent 是頻道成員，各有負責人和每月預算，能用 MCP 工具、自己的電腦和瀏覽器，合併、部署等敏感動作要人在聊天室核准。  
  👤 **適合**：想讓團隊和 Agent 在同一個地方協作、又想自己掌握伺服器的團隊　⚠️ AGPL-3.0 授權；需要自備模型 API 金鑰；瀏覽器、手機與桌面 App 等功能仍在 beta

<a id="research"></a>

## 研究與通用 Agent

能自主研究、多步驟完成任務的 Agent。

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · ⭐ 85.9k · Python · MIT  
  字節跳動開源的長任務 Agent，結合沙盒、記憶、技能和子 Agent，能研究、寫程式、產出內容。  
  👤 **適合**：想研究「超級 Agent」架構的人
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · ⭐ 30.9k · Python · Apache-2.0  
  自動上網研究任何主題，彙整成附來源的報告，支援各家 LLM。  
  👤 **適合**：需要快速做背景研究的人
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · ⭐ 18.0k · Go · Apache-2.0  
  給 AI Agent 用的安全沙盒執行環境，可部署在 Kubernetes 上。  
  👤 **適合**：需要讓 Agent 安全執行程式碼的團隊
- **[pmndrs/pine](https://github.com/pmndrs/pine)**  
  以事件驅動的終端機 Agent，除了聊天和寫程式，還能訂閱資料夾、網頁、webhook、MQTT 等事件來源，事件發生時自動醒來處理；設定都由主 Agent 透過對話建立。  
  👤 **適合**：想讓 Agent 在背景盯著檔案、網站或裝置並自動反應的人　⚠️ 支援 macOS 與 Linux，Windows 需透過 Docker；電腦操作功能只支援 macOS

<a id="lists"></a>

## 外掛、技能與其他清單

更多擴充資源。

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · ⭐ 98.6k · MIT  
  最大的 MCP server 清單（英文）。  
  👤 **適合**：想找特定 MCP 工具的人
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · ⭐ 58.9k · Python  
  精選的 Claude Code 資源清單：指令、工作流程、外掛等。  
  👤 **適合**：Claude Code 使用者
- **[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** · ⭐ 48.4k · Python · Apache-2.0  
  Anthropic 官方維護的 Claude Code 外掛目錄。  
  👤 **適合**：Claude Code 使用者
- **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** · ⭐ 37.6k · MIT  
  收錄 1000 多個 Agent Skills，相容 Claude Code、Codex、Gemini CLI、Cursor 等。  
  👤 **適合**：想擴充 Agent 能力的人
- **[sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill)** · ⭐ 2.8k · Python · MIT  
  帶 Agent 一步步調快本機 LLM 推論伺服器的 Skill，先算出理論上限，每次只改一個設定並與對照組比較，最後用長 context 測試確認沒有變笨或當掉。  
  👤 **適合**：自己架 vLLM、SGLang、llama.cpp 等推論伺服器、想榨出更多速度的人
- **[JDhruv14/line-art-animation](https://github.com/JDhruv14/line-art-animation)** · ⭐ 1.3k · TypeScript · MIT  
  一個 Claude Skill 加上小型 TypeScript 函式庫，讓 Agent 用 SVG 做出會走路、會互動、有日夜變化的線稿風格動畫元件，也能逐格輸出成影片。  
  👤 **適合**：想在網頁加手繪風動畫插圖、或用 Agent 做動態視覺的前端開發者
- **[Dodaios/ste80-humanizer](https://github.com/Dodaios/ste80-humanizer)** · ⭐ 1.2k · Python · MIT  
  改寫文字的 Agent Skill，先刪掉常見的 AI 寫作痕跡，再依航太維修手冊用的簡化技術英文（ASD-STE100）規則把句子改短、改主動語態，事實不增不減。  
  👤 **適合**：常要讀或改 AI 產出的英文文件、想讓內容更好讀的人　⚠️ 只針對英文
- **[Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill)** · ⭐ 1.1k · Python · MIT  
  讓程式 Agent 寫腳本、錄旁白、從 Wikimedia Commons 找公有領域圖片並記錄授權，再用 Python 程式碼逐格畫出一鏡到底的解說影片。  
  👤 **適合**：想用 Agent 做紀錄片風格短片或產品介紹影片的人　⚠️ 需要 Python、ffmpeg；最終配音可接任何 TTS 或真人錄音
- **[op7418/guizang-game-skill](https://github.com/op7418/guizang-game-skill)** · ⭐ 514 · JavaScript · AGPL-3.0  
  讓 Claude Code、Codex 等 Agent 照一套實際走過的流程，從規劃、美術素材、動作手感到打包，做出能在瀏覽器玩的 3D 動作遊戲。  
  👤 **適合**：想用 Agent 做網頁遊戲原型、但沒有遊戲開發經驗的人　⚠️ AGPL-3.0 授權；搭配 Tripo、即夢等素材生成服務效果較好，這些服務可能要付費；README 以簡體中文為主
- **[erkamyaman/unslopovich](https://github.com/erkamyaman/unslopovich)** · ⭐ 284 · JavaScript · MIT  
  檢查 App 和網站介面的 Agent Skill 加靜態偵測工具，找出「一看就是 AI 做的」設計和常見使用痛點，可以只出診斷報告，也可以直接修改。  
  👤 **適合**：用 AI 寫前端、覺得成品長得都一樣或不好用的開發者　⚠️ 只讀程式碼與畫面，不會實際測效能或修 bug
- **[nishuzumi/show-me-you-want-skill](https://github.com/nishuzumi/show-me-you-want-skill)** · ⭐ 249 · HTML · MIT  
  讓程式 Agent 動手寫程式前，先把要改的畫面和介面畫成單檔 HTML 線框原型，用顏色標出新增、修改、刪除的地方，你在圖上拖動、批注後把意見貼回去，確認後才開始寫程式。  
  👤 **適合**：常跟 Agent 對不上需求、改完介面才發現不是自己要的開發者　⚠️ 需要 Node 18 以上；README 以簡體中文為主
- **[bookleme/bookleme](https://github.com/bookleme/bookleme)** · ⭐ 249 · Python · MIT  
  把一本書（PDF、EPUB、DOCX 等）轉成可安裝的 Agent Skill，可以是能查詢的知識包，也可以是照書中流程一問一答的教練，並逐字檢查引文是否真的出自原文。  
  👤 **適合**：想把書裡的方法論變成 Agent 能照著做的流程的人　⚠️ 仍在早期開發，部分體裁尚未實作；用第三方書籍產生的 Skill 預設不公開，散布前要自行確認著作權

## 參與貢獻

歡迎推薦專案！請開 issue 或 PR，修改 `data/projects.yml` 即可，README 會自動產生。詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

本清單內容以 [CC0 1.0](LICENSE) 釋出。各專案版權屬於原作者。

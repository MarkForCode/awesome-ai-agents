# Awesome AI Agents 繁體中文精選

> 精選 AI Agent、MCP 與相關開源工具，每天更新，附繁體中文導讀。

目前收錄 **69** 個專案 · 數據更新：2026-11-13 · [網站版](https://markforcode.github.io/awesome-ai-agents/) · [RSS](https://markforcode.github.io/awesome-ai-agents/feed.xml)

每個專案都附「一句話介紹」和「適合誰」。⭐ 星星數、授權與更新狀態每天由 GitHub API 自動同步。

## 🆕 最近更新

- [2026-11-12](daily/2026-11-12.md)
- [2026-11-11](daily/2026-11-11.md)
- [2026-11-10](daily/2026-11-10.md)

## 目錄

- [入門學習](#learn)（7）
- [Agent 開發框架](#frameworks)（11）
- [程式開發 Agent](#coding)（9）
- [瀏覽器與電腦操作](#browser)（8）
- [MCP 伺服器與 SDK](#mcp)（11）
- [記憶與上下文](#memory)（6）
- [網頁資料擷取](#scraping)（3）
- [無程式碼平台與自架介面](#platforms)（7）
- [研究與通用 Agent](#research)（3）
- [外掛、技能與其他清單](#lists)（4）

<a id="learn"></a>

## 入門學習

從零開始理解 AI Agent 與 MCP 的課程、教材與指南。

- **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** · ⭐ 80.4k · Python · MIT  
  從零打造一個類似 Claude Code 的迷你 Agent，一步步拆解「Agent 外殼」是怎麼運作的。  
  👤 **適合**：好奇程式碼 Agent 內部原理的人
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · ⭐ 80.0k · MDX · MIT · 💤 半年未更新  
  提示工程經典指南，內容已擴充到 context engineering、RAG 與 Agent。  
  👤 **適合**：所有要跟 LLM 打交道的人
- **[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** · ⭐ 79.5k · Jupyter Notebook · MIT  
  微軟出的 18 堂 AI Agent 入門課，每堂都有講義和可執行的範例程式。  
  👤 **適合**：第一次接觸 Agent、想有系統學起來的開發者
- **[huggingface/agents-course](https://github.com/huggingface/agents-course)** · ⭐ 34.8k · MDX · Apache-2.0  
  Hugging Face 的免費 Agent 課程，涵蓋 smolagents、LangChain、LlamaIndex 等主流工具。  
  👤 **適合**：想邊學邊動手、順便比較不同框架的人
- **[NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)** · ⭐ 24.9k · Jupyter Notebook  
  50 多個 Agent 技巧的教學與實作，從簡單的聊天機器人到複雜的多 Agent 系統都有。  
  👤 **適合**：想找具體範例參考的開發者
- **[NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)** · ⭐ 21.9k · Jupyter Notebook  
  以程式碼為主的教學，示範 Agent 從原型走到正式上線要處理的部署、監控、安全等問題。  
  👤 **適合**：準備把 Agent 放進正式產品的團隊
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · ⭐ 17.6k · Jupyter Notebook · MIT  
  MCP（Model Context Protocol）入門教材，用 Python、TypeScript、Java、C# 等多種語言示範怎麼寫 MCP server 和 client。  
  👤 **適合**：想自己寫 MCP 工具的開發者

<a id="frameworks"></a>

## Agent 開發框架

用程式碼打造自己的 Agent。

- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · ⭐ 149.4k · Python · MIT  
  最多人用的 LLM 應用框架，串接模型、工具、資料來源的生態系最完整。  
  👤 **適合**：需要大量現成整合的專案　⚠️ 抽象層較多，簡單需求可能殺雞用牛刀
- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · ⭐ 71.3k · Python · MIT · 💤 半年未更新  
  模擬一間軟體公司，讓產品經理、架構師、工程師等 Agent 協作寫出軟體。  
  👤 **適合**：研究多 Agent 角色分工的人
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · ⭐ 61.8k · Python · CC-BY-4.0  
  微軟的多 Agent 對話框架，學術界和研究原型常用。  
  👤 **適合**：研究多 Agent 互動的開發者
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · ⭐ 60.8k · Python · MIT  
  讓多個扮演不同角色的 Agent 分工合作，例如研究員＋寫手＋審稿員。  
  👤 **適合**：想快速做出多 Agent 協作的人
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · ⭐ 44.9k · Python · MIT  
  用「圖」來描述 Agent 流程，能精準控制每一步、支援中斷與恢復。  
  👤 **適合**：流程複雜、需要可靠性的 Agent
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · ⭐ 43.2k · Python · Apache-2.0  
  輕量、速度快的 Python Agent 框架，內建記憶、知識庫與多 Agent 團隊。  
  👤 **適合**：想要簡潔 API 的 Python 開發者
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · ⭐ 35.9k · Python · Apache-2.0  
  阿里巴巴開源的多 Agent 框架，強調流程透明、可觀察，支援 MCP。  
  👤 **適合**：需要看清楚 Agent 每一步在做什麼的人
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · ⭐ 27.0k · Python · Apache-2.0  
  以模組化管線為核心的框架，特別擅長檢索（RAG）和可控的 Agent 流程。  
  👤 **適合**：以文件檢索為主的企業應用
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · ⭐ 25.4k · Apache-2.0  
  前身是 MemGPT，打造有長期記憶、會隨使用持續學習的 Agent。  
  👤 **適合**：需要 Agent 記住使用者的應用
- **[google/adk-python](https://github.com/google/adk-python)** · ⭐ 22.2k · Python · Apache-2.0  
  Google 官方 Agent Development Kit，涵蓋開發、評估到部署。  
  👤 **適合**：使用 Gemini 或 Google Cloud 的團隊
- **[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)** · ⭐ 21.2k · Python · MIT  
  Pydantic 團隊出品，從輸入到輸出都有完整型別檢查的 Agent 框架。  
  👤 **適合**：重視型別安全、習慣 FastAPI 風格的人

<a id="coding"></a>

## 程式開發 Agent

在終端機或編輯器裡幫你寫程式的 Agent。

- **[stablyai/orca](https://github.com/stablyai/orca)** · ⭐ 123.7k · TypeScript · MIT  
  同時管理一整隊程式 Agent（Claude Code、Codex 等），用你自己的訂閱，支援桌面、手機與遠端執行。  
  👤 **適合**：想讓多個 Agent 平行工作的人
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · ⭐ 108.8k · TypeScript · Apache-2.0  
  Google 開源的終端機 Agent，直接在命令列用 Gemini 讀寫程式碼、執行指令。  
  👤 **適合**：想要免費額度、在終端機工作的開發者
- **[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)** · ⭐ 68.9k · Rust · Apache-2.0  
  老牌開源專案，現在定位為給開源模型（Kimi、GLM 等）用的程式 Agent，以 Rust 改寫。  
  👤 **適合**：想在本機用開源模型寫程式的人
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · ⭐ 56.5k · Rust · Apache-2.0  
  可擴充的開源 Agent，不只建議程式碼，還能安裝套件、執行、測試，支援任何 LLM 與 MCP。  
  👤 **適合**：想要不綁定模型廠商的程式 Agent
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · ⭐ 40.8k · TypeScript · MIT  
  Claude Code 的多 Agent 協作外掛，讓多個 Agent 分工處理大型任務。  
  👤 **適合**：重度 Claude Code 使用者
- **[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)** · ⭐ 30.0k · TypeScript · Apache-2.0  
  通義千問團隊的終端機程式 Agent，針對 Qwen 系列模型最佳化。  
  👤 **適合**：想用開源模型寫程式的人
- **[charmbracelet/crush](https://github.com/charmbracelet/crush)** · ⭐ 29.1k · Go  
  Charm 團隊出品、介面很漂亮的終端機程式 Agent，支援多家模型。  
  👤 **適合**：重視終端機體驗的開發者
- **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** · ⭐ 4.9k · TypeScript · MIT  
  讓 Claude Code、Codex 等命令列 Agent 依規則在背景接手定時任務或 GitHub issue 等事件，需要人決定時才推卡片到飛書、Slack、Discord 或桌面通知。  
  👤 **適合**：想讓命令列 Agent 在沒人盯著時持續工作的人　⚠️ 文件以簡體中文為主；需要 Node 24 以上
- **[devvmhq/devvm](https://github.com/devvmhq/devvm)** · ⭐ 600 · Go · MIT  
  每個專案資料夾開一台獨立的 Lima 虛擬機，自動偵測需要的工具鏈，讓 Claude Code、Codex 等 Agent 在裡面工作，預設只能連到允許的網域。  
  👤 **適合**：想讓程式 Agent 放手做事、又不想讓它碰到本機的人　⚠️ 支援 macOS 13 以上與 Linux；作者提醒沙盒無法堵住所有漏洞，使用前先看安全說明

<a id="browser"></a>

## 瀏覽器與電腦操作

讓 Agent 操作網頁、桌面應用程式。

- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · ⭐ 120.9k · Python · MIT  
  讓 AI 操作瀏覽器的 Python 函式庫，能點擊、填表、跨網頁完成任務。  
  👤 **適合**：想自動化網頁操作的開發者
- **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · ⭐ 55.2k · TypeScript · Apache-2.0  
  Chrome 官方 DevTools MCP，讓程式 Agent 能看 console、網路請求、效能數據來除錯。  
  👤 **適合**：前端開發者
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · ⭐ 39.6k · TypeScript · Apache-2.0  
  微軟官方 Playwright MCP server，讓 Agent 透過結構化的頁面資訊操作瀏覽器。  
  👤 **適合**：想讓 Claude、Cursor 等工具操作網頁的人
- **[trycua/cua](https://github.com/trycua/cua)** · ⭐ 32.3k · Rust · MIT  
  電腦操作（computer-use）Agent 的基礎設施，提供跨作業系統沙盒、驅動程式和評測基準。  
  👤 **適合**：開發或訓練桌面操作 Agent 的人
- **[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)** · ⭐ 23.4k · Python · AGPL-3.0  
  結合 LLM 與視覺辨識的瀏覽器自動化，網站改版也不容易壞。  
  👤 **適合**：需要長期跑表單、下單等網頁流程的團隊　⚠️ AGPL-3.0 授權，商用前要留意
- **[browser-use/browser-harness](https://github.com/browser-use/browser-harness)** · ⭐ 19.1k · Python · MIT  
  讓 Claude Code、Codex、Cursor 直接使用你已登入的 Chrome，一個提示就能設定好。  
  👤 **適合**：想讓程式 Agent 存取需要登入的網站　⚠️ Agent 會以你的身分操作，要留意權限
- **[DIYgod/pinky](https://github.com/DIYgod/pinky)** · ⭐ 2.0k · Go · Apache-2.0  
  透過 MCP 讓 Agent 操作真實的 iPhone 或 Android 手機，付款等高風險步驟要你在電腦上按允許才會執行，並保留每一步的截圖與錄影。  
  👤 **適合**：想讓 Agent 代操手機 App、又要保留控制權的人　⚠️ 仍在 pre-alpha 階段
- **[vostride/agent-qa](https://github.com/vostride/agent-qa)** · ⭐ 856 · TypeScript  
  用自然語言描述使用流程，由 Agent 在網頁、Android 或 iOS 上實際操作測試，失敗時留下對應步驟的截圖；可從 CLI、儀表板或透過 MCP 從程式 Agent 呼叫，並把測試中學到的經驗存成 repo 裡可審查的檔案。  
  👤 **適合**：想讓程式 Agent 跑端對端測試的開發者與 QA 工程師　⚠️ FSL-1.1-ALv2 授權（原始碼公開，兩年後轉為 Apache-2.0，期間限制競爭用途），不是 OSI 認可的開源授權；需要 Node.js 24 以上，模型費用另計

<a id="mcp"></a>

## MCP 伺服器與 SDK

用 MCP 幫 Agent 接上各種工具與服務。

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · ⭐ 92.0k · TypeScript  
  MCP 官方的參考伺服器合集，包含檔案系統、Git、網頁擷取等範例。  
  👤 **適合**：想看標準寫法或找基本工具的人
- **[upstash/context7](https://github.com/upstash/context7)** · ⭐ 64.7k · TypeScript · MIT  
  即時提供最新版函式庫文件給 Agent，減少 AI 寫出舊版或不存在的 API。  
  👤 **適合**：所有用 AI 寫程式的人
- **[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)** · ⭐ 36.9k · TypeScript · Apache-2.0  
  用聊天的方式畫 draw.io 圖表，有網頁版、桌面版，也有 MCP server。  
  👤 **適合**：常畫架構圖、流程圖的人
- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · ⭐ 34.4k · Go · MIT  
  GitHub 官方 MCP server，讓 Agent 讀寫 issue、PR、程式碼與 Actions。  
  👤 **適合**：想讓 Agent 幫忙管理 GitHub 的人
- **[ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)** · ⭐ 34.2k · Python · MIT  
  用自然語言操作 Blender 建 3D 模型（社群外掛，非官方）。  
  👤 **適合**：3D 創作者
- **[oraios/serena](https://github.com/oraios/serena)** · ⭐ 31.3k · Python  
  提供語意層級的程式碼搜尋與編輯，讓 Agent 像用 IDE 一樣理解大型專案。  
  👤 **適合**：在大型程式碼庫裡用 Agent 的人
- **[ComposioHQ/composio](https://github.com/ComposioHQ/composio)** · ⭐ 31.1k · TypeScript · MIT  
  一次接上 1000 多種 SaaS 工具，並處理好授權登入，省去逐一串接的麻煩。  
  👤 **適合**：要讓 Agent 操作大量外部服務的開發者
- **[modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)** · ⭐ 24.8k · Python · MIT  
  MCP 官方 Python SDK，寫 MCP server 或 client 的首選。  
  👤 **適合**：Python 開發者
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · ⭐ 23.3k · TypeScript · MIT  
  讓 Claude、Cursor 等工具直接幫你設計 n8n 自動化流程。  
  👤 **適合**：n8n 使用者
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · ⭐ 13.8k · TypeScript  
  MCP 官方 TypeScript SDK。  
  👤 **適合**：JavaScript / TypeScript 開發者
- **[shanselman/sandbox-mcp](https://github.com/shanselman/sandbox-mcp)** · ⭐ 422 · JavaScript · MIT  
  用 Windows Sandbox 開一台全新、用完即丟的 Windows 11，讓 Agent 部署並操作你的桌面程式、記錄當機與缺少的相依套件，有 CLI 也有 MCP 介面。  
  👤 **適合**：開發 Windows 桌面應用程式、想在乾淨環境測試的人　⚠️ 需要 Windows 11 24H2 以上的 Pro、Enterprise 或 Education 版

<a id="memory"></a>

## 記憶與上下文

讓 Agent 記得更多、用更少 token。

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · ⭐ 116.6k · TypeScript · Apache-2.0  
  自動記錄 Agent 每次工作的內容並壓縮，下次開新對話時帶回相關記憶。  
  👤 **適合**：覺得 Claude Code 每次都「失憶」的人
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · ⭐ 79.5k · Python · Apache-2.0  
  在工具輸出、日誌、檔案送進 LLM 前先壓縮，有函式庫、代理伺服器和 MCP 三種用法。  
  👤 **適合**：想省 token 費用的人
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · ⭐ 68.9k · Python · Apache-2.0  
  Agent 的記憶層，自動記住使用者偏好與對話重點，可直接嵌入現有應用。  
  👤 **適合**：做個人化助理或客服的人
- **[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)** · ⭐ 60.8k · Python · MIT  
  會從經驗中學習的 Agent 記憶系統。  
  👤 **適合**：研究長期記憶的開發者
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · ⭐ 40.4k · Python · MIT  
  不用向量資料庫的 RAG，把文件建成目錄樹，讓 LLM 像人一樣翻目錄找答案。  
  👤 **適合**：處理長篇報告、財報、法規文件的人
- **[gogoymh/auto-ontology-mcp](https://github.com/gogoymh/auto-ontology-mcp)** · ⭐ 383 · Python · Apache-2.0  
  把 NVIDIA Auto Ontology 的語意層包成 MCP 伺服器，由你的 Agent 建立資料庫的業務詞彙並寫出經過檢查的唯讀 SQL，也能當個人知識庫用。  
  👤 **適合**：想用自然語言查公司資料庫，或想建立可查詢個人知識庫的人

<a id="scraping"></a>

## 網頁資料擷取

把網頁變成 Agent 讀得懂的資料。

- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · ⭐ 201.4k · TypeScript · AGPL-3.0  
  把整個網站爬下來轉成乾淨的 Markdown 或結構化資料，專為 LLM 設計。  
  👤 **適合**：需要餵網頁資料給 AI 的人　⚠️ AGPL-3.0 授權，也有付費雲端版
- **[D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)** · ⭐ 102.3k · Python · BSD-3-Clause  
  Python 爬蟲框架，從單一請求到大規模爬取都能處理，網站結構改變時能自動調整。  
  👤 **適合**：需要穩定爬蟲的 Python 開發者　⚠️ 請遵守目標網站的使用條款
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · ⭐ 87.3k · Python · Apache-2.0  
  開源、對 LLM 友善的爬蟲，輸出 Markdown，可以自己架設。  
  👤 **適合**：想免費自架爬蟲的開發者

<a id="platforms"></a>

## 無程式碼平台與自架介面

不太寫程式也能打造 Agent，或自架 AI 介面。

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · ⭐ 210.3k · TypeScript  
  視覺化工作流程自動化平台，內建 AI 節點，有 400 多種整合，可以自架。  
  👤 **適合**：想把 AI 接進日常工作流程的人　⚠️ fair-code 授權，不是完全的開源授權
- **[langgenius/dify](https://github.com/langgenius/dify)** · ⭐ 161.1k · Python  
  拖拉式打造 Agent 流程和 RAG 知識庫的平台，可自架或用雲端版。  
  👤 **適合**：想快速做出企業內部 AI 應用的團隊
- **[open-webui/open-webui](https://github.com/open-webui/open-webui)** · ⭐ 158.5k · Svelte  
  最受歡迎的自架 AI 聊天介面，支援 Ollama 本地模型和 OpenAI 相容 API。  
  👤 **適合**：想在本機或公司內部架 ChatGPT 的人
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · ⭐ 94.1k · Go · Apache-2.0  
  以深度文件理解為核心的 RAG 引擎，擅長處理表格、PDF 等複雜格式。  
  👤 **適合**：要做企業知識庫的團隊
- **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** · ⭐ 68.2k · JavaScript · MIT  
  本機優先的全功能 AI 應用，可以跟文件對話、執行 Agent，不必把資料交給雲端。  
  👤 **適合**：重視隱私的個人與小團隊
- **[LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)** · ⭐ 47.1k · TypeScript · MIT  
  功能完整的開源 ChatGPT 替代介面，一個介面切換多家模型，支援 Agent、MCP 與 Skills。  
  👤 **適合**：想統一管理多家模型的團隊
- **[activepieces/activepieces](https://github.com/activepieces/activepieces)** · ⭐ 25.5k · TypeScript  
  開源的 Zapier 替代品，內建約 400 個 MCP server。  
  👤 **適合**：想要開源自動化平台的人

<a id="research"></a>

## 研究與通用 Agent

能自主研究、多步驟完成任務的 Agent。

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · ⭐ 85.3k · Python · MIT  
  字節跳動開源的長任務 Agent，結合沙盒、記憶、技能和子 Agent，能研究、寫程式、產出內容。  
  👤 **適合**：想研究「超級 Agent」架構的人
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · ⭐ 30.7k · Python · Apache-2.0  
  自動上網研究任何主題，彙整成附來源的報告，支援各家 LLM。  
  👤 **適合**：需要快速做背景研究的人
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · ⭐ 17.3k · Go · Apache-2.0  
  給 AI Agent 用的安全沙盒執行環境，可部署在 Kubernetes 上。  
  👤 **適合**：需要讓 Agent 安全執行程式碼的團隊

<a id="lists"></a>

## 外掛、技能與其他清單

更多擴充資源。

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · ⭐ 97.7k · MIT  
  最大的 MCP server 清單（英文）。  
  👤 **適合**：想找特定 MCP 工具的人
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · ⭐ 57.9k · Python  
  精選的 Claude Code 資源清單：指令、工作流程、外掛等。  
  👤 **適合**：Claude Code 使用者
- **[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** · ⭐ 47.1k · Python · Apache-2.0  
  Anthropic 官方維護的 Claude Code 外掛目錄。  
  👤 **適合**：Claude Code 使用者
- **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** · ⭐ 37.1k · MIT  
  收錄 1000 多個 Agent Skills，相容 Claude Code、Codex、Gemini CLI、Cursor 等。  
  👤 **適合**：想擴充 Agent 能力的人

## 參與貢獻

歡迎推薦專案！請開 issue 或 PR，修改 `data/projects.yml` 即可，README 會自動產生。詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

本清單內容以 [CC0 1.0](LICENSE) 釋出。各專案版權屬於原作者。

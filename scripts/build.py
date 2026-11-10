#!/usr/bin/env python3
"""從 data/projects.yml 產生 README.md、docs/index.html、docs/feed.xml。

用法：
  python scripts/build.py            # 只用現有的 data/stats.json 產生
  python scripts/build.py --refresh  # 先用 GitHub API 更新星星數等資料再產生
  python scripts/build.py --check    # 檢查資料格式與重複，不寫檔

GitHub Actions 中會自動帶入 GITHUB_TOKEN 以提高 API 額度。
"""
import argparse, datetime as dt, html, json, os, pathlib, re, sys, time
import urllib.parse, urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.yml"
STATS = ROOT / "data" / "stats.json"
DAILY = ROOT / "daily"
DOCS = ROOT / "docs"
SITE_URL = "https://markforcode.github.io/awesome-ai-agents/"
REPO_URL = "https://github.com/markforcode/awesome-ai-agents"
TZ = dt.timezone(dt.timedelta(hours=8))
REQUIRED = ("repo", "summary", "for", "added")


def load():
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def all_projects(data):
    for cat in data["categories"]:
        for p in cat["projects"]:
            yield cat, p


def check(data):
    errors, seen = [], set()
    for cat, p in all_projects(data):
        for k in REQUIRED:
            if not p.get(k):
                errors.append(f"[{cat['id']}] {p.get('repo')} 缺少欄位 {k}")
        r = str(p.get("repo", "")).lower()
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", r):
            errors.append(f"[{cat['id']}] repo 格式錯誤：{p.get('repo')}")
        if r in seen:
            errors.append(f"重複收錄：{p['repo']}")
        seen.add(r)
    return errors


def gh_search(q):
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": q, "per_page": 100})
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "awesome-ai-agents-build"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["items"]


def refresh(data):
    repos = [p["repo"] for _, p in all_projects(data)]
    stats = json.loads(STATS.read_text()) if STATS.exists() else {}
    # 搜尋 API 的 q 上限 256 字元，把多個 repo: 條件分批組合
    batch, batches = [], []
    for r in repos:
        if len(" ".join(batch + [f"repo:{r}"])) > 240:
            batches.append(batch); batch = []
        batch.append(f"repo:{r}")
    if batch:
        batches.append(batch)
    found = set()
    for i, b in enumerate(batches):
        for it in gh_search(" ".join(b)):
            key = it["full_name"].lower()
            found.add(key)
            stats[key] = {
                "full_name": it["full_name"],
                "stars": it["stargazers_count"],
                "language": it["language"],
                "license": (it.get("license") or {}).get("spdx_id"),
                "pushed_at": it["pushed_at"],
                "archived": it["archived"],
                "description": it["description"],
            }
        if i < len(batches) - 1:
            time.sleep(2.5)  # 未登入時搜尋 API 每分鐘 10 次
    missing = [r for r in repos if r.lower() not in found]
    if missing:
        print("⚠️ 找不到（可能已改名、刪除或轉私有）：", ", ".join(missing), file=sys.stderr)
    stats["_updated"] = dt.datetime.now(TZ).isoformat(timespec="minutes")
    STATS.write_text(json.dumps(stats, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return stats


def fmt_stars(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


def stale(s, days=180):
    t = dt.datetime.fromisoformat(s["pushed_at"].replace("Z", "+00:00"))
    return (dt.datetime.now(dt.timezone.utc) - t).days > days


def badges(s):
    if not s:
        return ""
    parts = [f"⭐ {fmt_stars(s['stars'])}"]
    if s.get("language"):
        parts.append(s["language"])
    if s.get("license") and s["license"] != "NOASSERTION":
        parts.append(s["license"])
    if s.get("archived"):
        parts.append("🗄️ 已封存")
    elif stale(s):
        parts.append("💤 半年未更新")
    return " · ".join(parts)


def daily_files():
    return sorted(DAILY.glob("????-??-??.md"), reverse=True) if DAILY.exists() else []


def build_readme(data, stats):
    total = sum(len(c["projects"]) for c in data["categories"])
    updated = stats.get("_updated", "")[:10]
    out = [
        "# Awesome AI Agents 繁體中文精選",
        "",
        "> 精選 AI Agent、MCP 與相關開源工具，每天更新，附繁體中文導讀。",
        "",
        f"目前收錄 **{total}** 個專案 · 數據更新：{updated} · [網站版]({SITE_URL}) · [RSS]({SITE_URL}feed.xml)",
        "",
        "每個專案都附「一句話介紹」和「適合誰」。⭐ 星星數、授權與更新狀態每天由 GitHub API 自動同步。",
        "",
    ]
    days = daily_files()[:7]
    if days:
        out += ["## 🆕 最近更新", ""]
        for f in days:
            out.append(f"- [{f.stem}](daily/{f.name})")
        out.append("")
    out += ["## 目錄", ""]
    for c in data["categories"]:
        out.append(f"- [{c['name']}](#{c['id']})（{len(c['projects'])}）")
    out.append("")
    for c in data["categories"]:
        out += [f'<a id="{c["id"]}"></a>', "", f"## {c['name']}", "", c.get("desc", ""), ""]
        projs = sorted(c["projects"], key=lambda p: -(stats.get(p["repo"].lower(), {}).get("stars", 0)))
        for p in projs:
            s = stats.get(p["repo"].lower())
            b = badges(s)
            out.append(f"- **[{p['repo']}](https://github.com/{p['repo']})**" + (f" · {b}" if b else "") + "  ")
            out.append(f"  {p['summary']}  ")
            line = f"  👤 **適合**：{p['for']}"
            if p.get("note"):
                line += f"　⚠️ {p['note']}"
            out.append(line)
        out.append("")
    out += [
        "## 參與貢獻",
        "",
        "歡迎推薦專案！請開 issue 或 PR，修改 `data/projects.yml` 即可，README 會自動產生。詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。",
        "",
        "## 授權",
        "",
        "本清單內容以 [CC0 1.0](LICENSE) 釋出。各專案版權屬於原作者。",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")


def md_inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(.+?)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(md):
    """足夠用的簡易 Markdown 轉換（標題、清單、引言、段落）。"""
    out, in_list = [], False
    for line in md.splitlines():
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{md_inline(line[2:])}</li>"); continue
        if in_list and not line.startswith("  "):
            out.append("</ul>"); in_list = False
        if line.startswith("  ") and in_list:
            out[-1] = out[-1][:-5] + "<br>" + md_inline(line.strip()) + "</li>"
        elif m := re.match(r"(#{1,4}) (.*)", line):
            n = len(m.group(1)) + 1
            out.append(f"<h{n}>{md_inline(m.group(2))}</h{n}>")
        elif line.startswith("> "):
            out.append(f"<blockquote>{md_inline(line[2:])}</blockquote>")
        elif line.strip():
            out.append(f"<p>{md_inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--mut:#6b6a65;--line:#e6e3dc;--acc:#0b6e4f;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#ecebe6;--mut:#9b9a94;--line:#2c2b28;--acc:#5ccf9f;--card:#1c1c1a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}
.wrap{max-width:880px;margin:0 auto;padding:40px 20px 80px}
header h1{font-size:2rem;margin:0 0 6px;letter-spacing:-.01em}header p{color:var(--mut);margin:0}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 8px}
nav a{border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:.9rem;text-decoration:none;color:var(--fg)}
nav a:hover{border-color:var(--acc);color:var(--acc)}
h2{margin:48px 0 4px;font-size:1.35rem}h2+p.desc{color:var(--mut);margin:0 0 16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:10px 0}
.card a.name{font-weight:600;color:var(--acc);text-decoration:none}.meta{color:var(--mut);font-size:.85rem;margin-left:6px}
.card p{margin:6px 0 0}.for{color:var(--mut);font-size:.92rem}.note{color:#b4590a;font-size:.92rem}
a{color:var(--acc)}.daily li{margin:6px 0}footer{margin-top:60px;color:var(--mut);font-size:.85rem}
input#q{width:100%;padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);font-size:1rem;margin-top:16px}
"""


def page(title, body, desc="精選 AI Agent、MCP 與相關開源工具，每天更新，附繁體中文導讀。"):
    return f"""<!DOCTYPE html>
<html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="alternate" type="application/rss+xml" title="Awesome AI Agents 繁中" href="{SITE_URL}feed.xml">
<style>{CSS}</style></head><body><div class="wrap">{body}
<footer>由 <a href="{REPO_URL}">markforcode/awesome-ai-agents</a> 自動產生 · 內容以 CC0 釋出</footer></div></body></html>
"""


def build_site(data, stats):
    DOCS.mkdir(exist_ok=True)
    (DOCS / "daily").mkdir(exist_ok=True)
    total = sum(len(c["projects"]) for c in data["categories"])
    b = [f'<header><h1>Awesome AI Agents 繁體中文精選</h1><p>收錄 {total} 個專案 · 每天更新 · '
         f'<a href="{REPO_URL}">GitHub</a> · <a href="feed.xml">RSS</a></p></header>',
         '<input id="q" placeholder="搜尋專案、用途…" oninput="f(this.value)">', "<nav>"]
    b += [f'<a href="#{c["id"]}">{html.escape(c["name"])}</a>' for c in data["categories"]]
    days = daily_files()
    if days:
        b.append('<a href="#daily">🆕 每日更新</a>')
    b.append("</nav>")
    for c in data["categories"]:
        b.append(f'<section><h2 id="{c["id"]}">{html.escape(c["name"])}</h2><p class="desc">{html.escape(c.get("desc",""))}</p>')
        for p in sorted(c["projects"], key=lambda p: -(stats.get(p["repo"].lower(), {}).get("stars", 0))):
            s = stats.get(p["repo"].lower())
            note = f'<div class="note">⚠️ {html.escape(p["note"])}</div>' if p.get("note") else ""
            b.append(f'<div class="card"><a class="name" href="https://github.com/{p["repo"]}">{p["repo"]}</a>'
                     f'<span class="meta">{html.escape(badges(s))}</span><p>{html.escape(p["summary"])}</p>'
                     f'<div class="for">👤 適合：{html.escape(p["for"])}</div>{note}</div>')
        b.append("</section>")
    if days:
        b.append('<h2 id="daily">🆕 每日更新</h2><ul class="daily">')
        b += [f'<li><a href="daily/{f.stem}.html">{f.stem}</a></li>' for f in days[:30]]
        b.append("</ul>")
    b.append("""<script>function f(q){q=q.toLowerCase();document.querySelectorAll('.card').forEach(c=>{c.style.display=c.textContent.toLowerCase().includes(q)?'':'none'});document.querySelectorAll('section').forEach(s=>{s.style.display=[...s.querySelectorAll('.card')].some(c=>c.style.display!=='none')?'':'none'})}</script>""")
    (DOCS / "index.html").write_text(page("Awesome AI Agents 繁體中文精選", "\n".join(b)), encoding="utf-8")

    items = []
    for f in days:
        md = f.read_text(encoding="utf-8")
        body = md_to_html(md)
        (DOCS / "daily" / f"{f.stem}.html").write_text(
            page(f"{f.stem} 每日 AI Agent 精選", f'<p><a href="../">← 回到清單</a></p>{body}'), encoding="utf-8")
        d = dt.datetime.fromisoformat(f.stem).replace(hour=9, tzinfo=TZ)
        items.append(f"<item><title>{f.stem} 每日 AI Agent 精選</title><link>{SITE_URL}daily/{f.stem}.html</link>"
                     f"<guid>{SITE_URL}daily/{f.stem}.html</guid><pubDate>{d.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>"
                     f"<description>{html.escape(body)}</description></item>")
    feed = (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Awesome AI Agents 繁體中文精選</title>'
            f"<link>{SITE_URL}</link><description>每天精選 AI Agent 與 MCP 開源專案</description><language>zh-TW</language>"
            + "".join(items[:30]) + "</channel></rss>\n")
    (DOCS / "feed.xml").write_text(feed, encoding="utf-8")
    (DOCS / ".nojekyll").write_text("")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    data = load()
    errs = check(data)
    if errs:
        print("\n".join(errs), file=sys.stderr); sys.exit(1)
    if a.check:
        print("OK"); return
    stats = refresh(data) if a.refresh else (json.loads(STATS.read_text()) if STATS.exists() else {})
    build_readme(data, stats)
    build_site(data, stats)
    print("built", sum(1 for _ in all_projects(data)), "projects")


if __name__ == "__main__":
    main()

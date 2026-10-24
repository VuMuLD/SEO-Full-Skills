# SEO All-in-One — bộ skill SEO hợp nhất (cập nhật 10/2026)

Một skill duy nhất tên **`seo`** cho Claude Code, gộp và loại trùng toàn bộ tài liệu trong thư mục
`Skill learn` (claude-seo, Agentic-SEO-Skill, marketingskills, seo CLI, google-indexing-script,
seo-audits-toolkit). Thông tin đã được đối chiếu và sửa theo trạng thái Google mới nhất (09-10/2026).

## Có gì bên trong

| Thành phần | Số lượng | Ghi chú |
|---|---|---|
| `SKILL.md` | 1 | Bộ định tuyến: quy tắc chung, bảng lệnh → module, chấm điểm, các “sự thật 2026” |
| Module (`references/*.md`) | 32 | Mỗi lệnh một playbook, không trùng nhau (gồm `vn-playbook` rút từ 23 case thực tế) |
| Tài liệu tham chiếu phụ | 139 | Theo thư mục của từng module + `references/core/` dùng chung |
| Agent con (`agents/`) | 23 | Prompt vai trò để chạy audit song song (technical, content, schema, geo, verifier...) |
| Script Python (`scripts/`) | 143 | Đã gộp, bỏ trùng, sửa lỗi Windows; danh mục: `references/core/script-catalog.md` |
| FLOW prompts | 41 | Find · Leverage · Optimize · Win · Local |
| Template | 15+ | Kế hoạch theo ngành, bài viết, báo cáo, GitHub, sơ đồ cluster HTML, tracker CSV |

### 32 module

| Nhóm | Module |
|---|---|
| Kiểm tra | `audit` (toàn site), `page` (+ chế độ article), `technical`, `content`, `schema`, `sitemap`, `images`, `hreflang`, `sxo` |
| Nội dung & từ khoá | `cluster` (nghiên cứu từ khoá, cụm SERP), `content-brief`, `content-strategy`, `plan`, `site-architecture`, `programmatic`, `competitor-pages` |
| AI Search | `geo` (AI Overviews, AI Mode, ChatGPT, Perplexity, Copilot), `aeo` (featured snippet, PAA, knowledge panel), `agentic` (agent readiness, llms.txt, WebMCP) |
| Local & thương mại | `local`, `maps`, `ecommerce` |
| Off-page | `backlinks`, `directories` |
| Dữ liệu & giám sát | `google` (GSC, URL Inspection, PSI/CrUX, Indexing API, GA4, báo cáo PDF), `drift`, `dataforseo`, `providers` (Ahrefs, Bing/IndexNow, Firecrawl, Matomo, SE Ranking, Profound, Unlighthouse, seo CLI) |
| Khác | `image-gen` (ảnh OG/hero bằng Gemini), `flow` (thư viện prompt), `github` (SEO cho repo) |
| Thực chiến Việt Nam | `vn-playbook` — 7 quy luật, bảng đánh giá chiến thuật (textlink báo, traffic user, social entity...), lộ trình 6 tháng, khung theo ngành, cách cam kết KPI; chi tiết 23 case ở `references/vn-cases/case-index.md` |

## Cài đặt

**Windows (PowerShell):**

```powershell
cd "C:\Users\phong\OneDrive\Documents\CodeVUi\Seo\Skill learn\All in Skills Seo\seo"
powershell -ExecutionPolicy Bypass -File .\install.ps1            # bản cơ bản
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Optional  # + Playwright, Google APIs, PDF
```

**macOS / Linux:** `bash install.sh` (thêm `--optional` nếu cần).

Trình cài đặt sẽ: chép thư mục vào `~/.claude/skills/seo` (sao lưu bản cũ nếu có), tạo môi trường
ảo `.venv` riêng và cài thư viện. Không cài gì vào Python toàn cục. Sau đó **khởi động lại Claude Code**.

Chỉ muốn chép file, không cài Python: thêm `-NoVenv` / `--no-venv`, hoặc tự chép thư mục `seo`
vào `%USERPROFILE%\.claude\skills\` (hoặc `.claude/skills/` trong một dự án).

**API key (tuỳ chọn):** chép `.env.example` thành `.env` rồi điền key cần dùng, hoặc chạy
`python scripts/google_auth.py --setup` và `python scripts/backlinks_auth.py --setup`.
Không có key vẫn chạy được phần lớn: crawl, on-page, schema, robots, AI crawler, Common Crawl...

## Cách dùng

Gõ lệnh hoặc nói tự nhiên (tiếng Việt được):

```text
/seo audit https://example.com            # audit toàn site + điểm SEO Health 0-100
/seo page https://example.com/bai-viet     # phân tích sâu 1 trang
/seo article https://example.com/blog/x    # viết lại title/meta/đoạn văn dạng trước → sau
/seo technical https://example.com
/seo geo https://example.com               # tối ưu cho AI Overviews / ChatGPT / Perplexity
/seo cluster "phần mềm bán hàng"           # nghiên cứu & gom cụm từ khoá
/seo content-brief "cách chọn máy lọc nước"
/seo schema https://example.com/san-pham
/seo local https://phongkhamabc.vn
/seo plan saas
/seo backlinks https://example.com
/seo google gsc sc-domain:example.com      # cần cấu hình Search Console
/seo updates --since 2026-01               # lịch sử cập nhật thuật toán Google
/seo report https://example.com            # dashboard HTML 1 lệnh
/seo vn                                    # lộ trình & kinh nghiệm thực chiến thị trường Việt Nam
```

Ví dụ câu tự nhiên: *“Kiểm tra SEO website abc.vn và lập kế hoạch sửa”*, *“Vì sao traffic tháng
này giảm?”*, *“Làm sao để thương hiệu xuất hiện trong câu trả lời của ChatGPT?”*.

Kết quả audit luôn có `FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md`; mỗi phát hiện kèm **bằng chứng,
mức độ (Critical/High/Medium/Low/Info) và độ tin cậy (Confirmed/Likely/Hypothesis)**.

## Đã tối ưu gì so với các bộ gốc

**Loại trùng lặp**

- 61 file skill SEO chồng chéo (35 của claude-seo, 17 của Agentic, 8 của marketingskills, 1 của seo CLI;
  ví dụ 3 bản `seo-audit`, 3 bản `schema`, 3 bản `programmatic`, 2 bản technical/content/geo/hreflang/
  sitemap/images/plan...) → **31 module, mỗi chủ đề một chỗ**.
- 42 skill marketing không thuộc SEO trong `marketingskills` (quảng cáo, email, pricing, onboarding,
  CRO, social...) được **cố ý không đưa vào** để bộ skill tập trung vào SEO.
- 5 script trùng tên → giữ bản tốt hơn; `parse_html.py` được **hợp nhất** từ 2 bản (đủ cả lazy-load,
  srcset, @graph của claude-seo lẫn lang, viewport, h4-h6, pagination, resource hints, `--fetch` của Agentic).
  `lcp_subparts` của Agentic là chức năng khác nên giữ dưới tên `lcp_lab_estimate.py`.
- 2 thang điểm khác nhau → **1 thang điểm chuẩn**; 2 hệ mức độ → **1 rubric** (`core/audit-rubric.md`).
- 8 extension (Ahrefs, Bing, Firecrawl, Matomo, Profound, SE Ranking, Unlighthouse, DataForSEO)
  + seo CLI → gom về `providers.md` / `dataforseo.md`.

**Sửa thông tin lỗi thời (các bộ cũ còn khuyên sai)**

- FAQ rich results đã bị Google **bỏ hoàn toàn từ 07/05/2026** (bộ cũ: “chỉ cho site chính phủ/y tế”).
- Sitelinks search box đã bỏ từ 11/2024; HowTo bỏ từ 2023; `speakable` vẫn là beta.
- Phân biệt đúng bot **huấn luyện** (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended) và bot
  **trích dẫn/tìm kiếm** (OAI-SearchBot, Claude-SearchBot, PerplexityBot); bỏ token `anthropic-ai`
  không có thật; Google-Extended **không** ảnh hưởng AI Overviews.
- HARO đã đóng cửa (12/2024) → thay bằng Qwoted, Featured, Source of Sources.
- Cortana đã khai tử; bỏ các số liệu “word count tối thiểu là yếu tố xếp hạng”.

**Sửa lỗi script (kiểm chứng bằng test)**

- Console Windows tiếng Việt (cp1258) làm script **crash khi in emoji** → ép UTF-8 cho cả 143 script.
- `seo_common.load_html` coi đường dẫn file Windows (`C:\...\a.html`) là URL → đã sửa (lỗi có sẵn ở repo gốc).
- `generate_report.py` crash khi trang không có canonical → đã sửa.
- Kết quả kiểm thử: **34/34** test của Agentic-SEO và **638** test script của claude-seo pass trên bộ
  đã gộp (các test còn lại chỉ kiểm tra cấu trúc thư mục của repo gốc nên không áp dụng).

## Cấu trúc thư mục

```text
seo/
├── SKILL.md                 # bộ định tuyến (đọc đầu tiên)
├── references/              # 31 module + thư mục tài liệu theo module
│   └── core/                # rubric, danh mục script, Google essentials, CWV, E-E-A-T, schema types...
├── agents/                  # 23 prompt agent con
├── scripts/                 # 143 script Python (+ image_gen/, lib/)
├── assets/                  # schema templates.json, scoring.json
├── data/google-updates.json # sổ cái cập nhật Google (nguồn chính thức)
├── templates/               # plans/, content/, reports/, github/, cluster-map.html, tracker CSV
├── requirements*.txt, .env.example, install.ps1, install.sh
└── NOTICE.md                # bản quyền & nguồn gốc
```

## Bảo trì

- Google thay đổi liên tục: khi có cập nhật lớn, sửa `data/google-updates.json`,
  `references/core/schema-types.md`, `references/core/cwv-thresholds.md` trước.
- Mẹo Windows: đặt biến môi trường `PYTHONUTF8=1` để hiển thị tiếng Việt/emoji sạch nhất.
- Kiểm tra nhanh môi trường: `python scripts/google_auth.py --check --json`,
  `python scripts/backlinks_auth.py --check --json`.

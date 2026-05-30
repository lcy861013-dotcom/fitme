#!/usr/bin/env python3
"""Reorder index.html: blog + edu before guide + analysis; compact guide teaser."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

MARKERS = [
    ("guide", "<!-- GUIDE -->"),
    ("blog", "<!-- BLOG -->"),
    ("analysis", "<!-- MAIN ANALYSIS -->"),
    ("edu", "<!-- EDUCATIONAL CONTENT SECTION (SEO & USER VALUE) -->"),
]

GUIDE_TEASER = """    <p class="guide-teaser" data-i18n="guide-teaser" style="max-width:720px;margin:12px auto 24px;font-size:15px;line-height:1.75;color:var(--muted);text-align:center;padding:0 16px;">손뼘·어깨·다리 라인 — 한 번만 재두면 직구·쇼핑몰에서 사이즈 추측이 줄어듭니다. 단계별 글은 블로그에 모아 두었어요.</p>
    <div class="guide-quick-links" style="max-width:640px;margin:0 auto 20px;padding:0 16px;">
      <div id="guide-links-title" style="font-size:10px;letter-spacing:2.5px;text-transform:uppercase;color:var(--muted);margin-bottom:10px;text-align:center;">📸 Visual Measurement Guides</div>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:8px;">
        <a href="/blog/blog20" onclick="goBlog(event,'blog20')" style="display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--text);transition:border-color 0.2s;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'">
          <span style="font-size:20px;">✋</span><div><div id="guide-link1-title" style="font-size:13px;font-weight:600;">Hand Span Baseline</div><div id="guide-link1-sub" style="font-size:11px;color:var(--muted);">Essential first step</div></div>
        </a>
        <a href="/blog/blog21" onclick="goBlog(event,'blog21')" style="display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--text);transition:border-color 0.2s;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'">
          <span style="font-size:20px;">🦴</span><div><div id="guide-link2-title" style="font-size:13px;font-weight:600;">Shoulder Width</div><div id="guide-link2-sub" style="font-size:11px;color:var(--muted);">Acromion + self-measuring method</div></div>
        </a>
        <a href="/blog/blog22" onclick="goBlog(event,'blog22')" style="display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--text);transition:border-color 0.2s;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'">
          <span style="font-size:20px;">💪</span><div><div id="guide-link3-title" style="font-size:13px;font-weight:600;">Arm Length</div><div id="guide-link3-sub" style="font-size:11px;color:var(--muted);">Upper + forearm in 2 steps</div></div>
        </a>
        <a href="/blog/blog23" onclick="goBlog(event,'blog23')" style="display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--text);transition:border-color 0.2s;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'">
          <span style="font-size:20px;">🦵</span><div><div id="guide-link4-title" style="font-size:13px;font-weight:600;">Leg Length</div><div id="guide-link4-sub" style="font-size:11px;color:var(--muted);">Hip bone → ankle in 2 steps</div></div>
        </a>
        <a href="/blog/blog24" onclick="goBlog(event,'blog24')" style="display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--text);transition:border-color 0.2s;grid-column:span 2;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'">
          <span style="font-size:20px;">🍑</span><div><div id="guide-link5-title" style="font-size:13px;font-weight:600;">Hip Circumference</div><div id="guide-link5-sub" style="font-size:11px;color:var(--muted);">Two hands, solo measurement</div></div>
        </a>
      </div>
      <p style="text-align:center;margin-top:18px;"><a href="/blog/" class="blog-view-all" data-i18n="guide-view-all" style="display:inline-block;">전체 측정·스타일 가이드 보기 →</a></p>
    </div>
    <details class="guide-full-details" style="max-width:1040px;margin:0 auto 8px;padding:0 16px;">
      <summary data-i18n="guide-full-summary" style="cursor:pointer;font-size:13px;color:var(--accent);letter-spacing:0.3px;margin-bottom:12px;list-style:none;text-align:center;">메인에서 자세한 측정 방법 펼치기</summary>
"""


def extract_section(text: str, start_marker: str, next_markers: list[str]) -> tuple[str, str]:
    start = text.index(start_marker)
    end = len(text)
    for nm in next_markers:
        pos = text.find(nm, start + len(start_marker))
        if pos != -1 and pos < end:
            end = pos
    return text[start:end], text[:start] + text[end:]


def compact_guide(guide_block: str) -> str:
    """Insert teaser + collapse heavy guide-grid inside details."""
    header_end = guide_block.find('<div class="guide-grid">')
    if header_end == -1:
        return guide_block
    header = guide_block[:header_end]
    rest = guide_block[header_end:]
    closing = rest.rfind("</section>")
    grid_and_close = rest[:closing]
    return header + GUIDE_TEASER + grid_and_close + "\n    </details>\n  </section>\n"


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    story_end = text.index("  </section>\n\n  <!-- GUIDE -->")
    prefix = text[: story_end + len("  </section>\n\n")]
    tail_marker = "  <div class=\"fitme-ad-slot\""
    tail_start = text.index(tail_marker)
    suffix = text[tail_start:]

    remaining = text[story_end + len("  </section>\n\n") : tail_start]
    sections = {}
    order = [m[0] for m in MARKERS]
    markers_only = [m[1] for m in MARKERS]
    for i, (key, marker) in enumerate(MARKERS):
        nxt = [markers_only[j] for j in range(i + 1, len(markers_only))]
        block, remaining = extract_section(remaining, marker, nxt)
        sections[key] = block

    if remaining.strip():
        raise SystemExit(f"Unparsed content before tail: {remaining[:120]!r}")

    sections["guide"] = compact_guide(sections["guide"])
    new_body = (
        sections["blog"]
        + "\n"
        + sections["edu"]
        + "\n"
        + sections["guide"]
        + "\n"
        + sections["analysis"]
        + "\n"
    )
    INDEX.write_text(prefix + new_body + suffix, encoding="utf-8")
    print("Reordered: story -> blog -> edu -> guide(compact) -> analysis")


if __name__ == "__main__":
    main()

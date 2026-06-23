#!/usr/bin/env python3
"""Move #analysis directly under a compact hero; guides/content below."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "index.html"
html = p.read_text(encoding="utf-8")


def slice_between(text: str, start: str, end: str) -> tuple[str, int, int]:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j], i, j


hero_start = "  <!-- HERO — guides first, calculator second -->"
story_start = "  <!-- STORY (founder — above tool) -->"
analysis_start = "<!-- MAIN ANALYSIS -->"
analysis_end = '  <div class="fitme-ad-slot"'

_, h0, _ = slice_between(html, hero_start, story_start)
middle_block, _, _ = slice_between(html, story_start, analysis_start)
analysis_block, a0, a1 = slice_between(html, analysis_start, analysis_end)
tail = html[a1:]
prefix = html[:h0]

new_hero = """  <!-- HERO — calculator first -->
  <div class="hero hero--calc-first">
    <div class="hero-social-proof">
      <span class="sp-dot"></span>
      <span data-i18n="hero-live-suffix">📷 No Photos · Measurements Only · 100% Private</span>
    </div>
    <div class="hero-tag" data-i18n="hero-tag-calc">FREE TOOL · NO PHOTOS</div>
    <h1 class="hero-headline hero-headline--static" id="hero-headline-text" data-i18n="hero-headline-calc">Enter height, weight &amp; waist.<br><em>See your ratios instantly.</em></h1>
    <p class="hero-positioning" data-i18n="hero-positioning">When the size tag fits but clothes don&rsquo;t — measure shoulder, waist, and hip <em>ratios</em>, not just S/M/L.</p>
    <div class="hero-calc-bar">
      <button type="button" class="hero-sample-btn" onclick="trySampleValues()" data-i18n="sample-btn">👀 Try Sample Results First</button>
      <div class="hero-trust hero-trust--inline" data-i18n-trust>
        <span data-i18n="hero-trust1">No photos required</span>
        <span data-i18n="hero-trust2">No signup</span>
        <span data-i18n="hero-trust3">100% private</span>
      </div>
    </div>
    <p class="hero-privacy-note" data-i18n="hero-privacy-note">No selfies · No uploads · Your data never leaves this page</p>
    <div class="hero-scroll-hint" onclick="document.getElementById('analysis').scrollIntoView({behavior:'smooth'})">
      <span data-i18n="hero-scroll-hint-calc">Tap a body part below to enter numbers</span>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
    </div>
  </div>

"""

guides_hub = """
  <section class="guides-hub-section" id="guides-hub-section" aria-label="Fit guides">
    <div class="guides-hub" id="guides-hub">
      <p class="guides-hub-label" data-i18n="guides-hub-label">Start here — featured guides</p>
      <div class="guides-hub-grid">
        <a href="/blog/blog26-en" class="guides-hub-card">
          <span class="guides-hub-kicker" data-i18n="guides-hub-1-kicker">Online sizing</span>
          <span class="guides-hub-title" data-i18n="guides-hub-1-title">2XL oversize still fits wrong? Measure first</span>
          <span class="guides-hub-desc" data-i18n="guides-hub-1-desc">For you if: 2XL/oversize fits on the chart but shoulders or waist still feel off.</span>
        </a>
        <a href="/blog/blog8-en" class="guides-hub-card">
          <span class="guides-hub-kicker" data-i18n="guides-hub-2-kicker">WHR</span>
          <span class="guides-hub-title" data-i18n="guides-hub-2-title">How to measure waist-to-hip ratio</span>
          <span class="guides-hub-desc" data-i18n="guides-hub-2-desc">For you if: jeans fit at the hips but gape at the waist — over and over.</span>
        </a>
        <a href="/blog/blog18-en" class="guides-hub-card">
          <span class="guides-hub-kicker" data-i18n="guides-hub-3-kicker">Pear body</span>
          <span class="guides-hub-title" data-i18n="guides-hub-3-title">Dressing a pear / fuller-hip shape</span>
          <span class="guides-hub-desc" data-i18n="guides-hub-3-desc">For you if: hips feel wide, waist is narrow, and pants are the hardest buy.</span>
        </a>
      </div>
    </div>
    <div class="hero-cta-row guides-hub-cta">
      <a class="hero-btn" href="#blog-section" data-home-anchor="blog-section" data-i18n="hero-btn-guides">Browse all fit guides →</a>
      <a class="hero-btn hero-btn--outline" href="/demo-video" data-i18n="hero-demo-watch">Watch demo video →</a>
    </div>
    <p class="hero-publisher-links">
      <a href="/editorial-standards" data-i18n="hero-link-editorial">Editorial standards</a>
      <span aria-hidden="true"> · </span>
      <a href="/how-it-works" data-i18n="hero-link-how">How the tool works</a>
    </p>
  </section>

"""

tool_marker = "<!-- FREE CALCULATOR INTRO -->"
if tool_marker in middle_block:
    middle_block = middle_block[: middle_block.index(tool_marker)].rstrip() + "\n\n"

new_html = prefix + new_hero + analysis_block + guides_hub + middle_block + tail
p.write_text(new_html, encoding="utf-8")
print("Reordered index.html:", len(new_html), "chars")

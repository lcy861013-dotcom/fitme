#!/usr/bin/env python3
"""
SEO keyword alignment for 25 English blog posts.

For each post we lock-in:
  - <title>             (≤ 60 chars, keyword-front-loaded)
  - <meta description>  (≤ 158 chars, includes keyword + CTA)
  - og:title / og:description / twitter:title / twitter:description
  - JSON-LD Article.headline / description
  - <h1> (only if it currently differs from the new clean keyword phrase)

Keyword research basis (high-intent / low-competition for FITME's niche):
  - "how to" + measurement / fit / body-type long-tails (transactional)
  - "best ... for [body type]" comparison posts (commercial)
  - "what is" + science of proportions (informational, AI-overview eligible)

We KEEP the brand suffix " | FITME" but truncate the lead phrase so total ≤ 60.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "blog"

# Keyword map. Each entry: (primary_kw, title, desc, h1)
# - title MUST fit in <= 60 chars including " | FITME" (8 chars).
# - desc MUST fit in <= 158 chars.
KW: dict[int, dict[str, str]] = {
    1: dict(
        kw="pants fit guide",
        title="Pants Fit: Slim vs Straight vs Wide (Your Body)",
        desc="Same waist tag, different leg line — which cut actually suits you? Slim, straight, wide & tapered compared + free 60-sec body map.",
        h1="Pants Fit Guide: Slim, Straight, Wide & Tapered",
    ),
    2: dict(
        kw="best shoes for wide feet",
        title="Best Shoes for Wide Feet 2026: 12 Brands That Actually Fit",
        desc="The 12 best shoe brands for wide feet (men + women): Altra, New Balance 4E, Topo, Hoka and more. Width chart, sizing tips, and how to measure foot width.",
        h1="Best Shoes for Wide Feet — 12 Brands That Actually Fit",
    ),
    3: dict(
        kw="golden ratio body proportions",
        title="Golden Ratio Body Proportions: How to Dress for Yours",
        desc="What the golden ratio means for your body and how to dress for it. Calculate your shoulder-to-waist ratio in 60 seconds with our free body analysis.",
        h1="Golden Ratio Body Proportions — How to Dress for Yours",
    ),
    4: dict(
        kw="how to dress for your body type tops",
        title="How to Dress for Your Body Type: Complete Tops Guide",
        desc="Pick the right top for your shoulders, bust and torso. Necklines, sleeves, cropping and tucks decoded for every body type — with a free 60-sec analysis.",
        h1="How to Dress for Your Body Type — Tops",
    ),
    5: dict(
        kw="color coordination clothes body shape",
        title="Color Coordination Rules to Flatter Your Body Shape",
        desc="The 5 color rules that make any body shape look balanced. Dark anchor, contrast placement and seasonal palette guide for clothes that actually flatter.",
        h1="Color Coordination Rules to Flatter Your Body Shape",
    ),
    6: dict(
        kw="capsule wardrobe basics",
        title="5 Capsule Wardrobe Basics = 7 Days of Perfect Outfits",
        desc="The 5 capsule wardrobe basics that create 7 full outfits with zero decision fatigue. Minimalist style for any body type — free proportion analysis.",
        h1="5 Wardrobe Basics — 7 Days of Outfits",
    ),
    7: dict(
        kw="body proportions vs weight",
        title="Why Body Proportions Matter More Than Weight (Science)",
        desc="Two people at the same weight can look completely different. The science of body proportions, WHR and shoulder-to-hip ratio — and what to wear for yours.",
        h1="Why Body Proportions Matter More Than Weight",
    ),
    8: dict(
        kw="waist to hip ratio whr",
        title="Waist-to-Hip Ratio (WHR) Explained: Health & Style",
        desc="What waist-to-hip ratio (WHR) actually means for your health, attractiveness and style choices. How to measure WHR at home in 30 seconds — free.",
        h1="Waist-to-Hip Ratio (WHR) Science: Style + Health",
    ),
    9: dict(
        kw="shoulder width clothing fit",
        title="How Shoulder Width Changes Your Outfit Fit (2026)",
        desc="Shoulder width is the #1 factor in how clothes fit. Why off-the-rack fails, how to measure shoulder width alone, and outfit fixes for narrow vs broad.",
        h1="How Shoulder Width Changes Your Entire Outfit Fit",
    ),
    10: dict(
        kw="how to look taller men women",
        title="How to Look Taller: 5 Outfit Tricks That Add 2 Inches",
        desc="5 styling tricks that visually add up to 2 inches of height — monochrome blocks, rise height, vertical lines and more. Works for men and women.",
        h1="How to Look Taller — 5 Outfit Tricks",
    ),
    11: dict(
        kw="clothes never fit right",
        title="Why Clothes Never Fit (It's Not Your Body)",
        desc="Size letters ignore your proportions. Brand chaos, vanity sizing, and 4 fixes that work — including a free 60-second ratio check.",
        h1="Why Clothes Never Fit You Right",
    ),
    12: dict(
        kw="find your body type with measurements",
        title="Find Your Real Body Type with Data, Not Labels",
        desc="Forget hourglass / pear / apple labels. Find your real body type with 4 measurements and a free FITME DNA score in under 60 seconds.",
        h1="Find Your Real Body Type with Data",
    ),
    13: dict(
        kw="how to dress for body type guide",
        title="How to Dress for Every Body Type — Complete Guide",
        desc="The complete how-to-dress guide for hourglass, pear, apple, rectangle and inverted-triangle body types. Free 60-second body analysis included.",
        h1="How to Dress for Every Body Type",
    ),
    14: dict(
        kw="body symmetry attractiveness",
        title="Body Symmetry and Attractiveness: What Science Says",
        desc="The science of body symmetry, facial symmetry, WHR and attractiveness — what 30 years of research actually proves and how to apply it to your style.",
        h1="Body Symmetry and Attractiveness — The Science",
    ),
    15: dict(
        kw="data driven style guide",
        title="Stop Guessing Your Style — Use Data Instead",
        desc="The data-driven style guide: how 4 body measurements predict outfit success better than any fashion advice. Free FITME body analysis in 60 seconds.",
        h1="Stop Guessing Your Style — Use Data Instead",
    ),
    16: dict(
        kw="ai personal styling future",
        title="AI Personal Styling 2026: How AI Is Changing Fashion",
        desc="How AI personal styling works in 2026 — from body scans to outfit recs. The tech behind FITME's body proportion engine and what comes next.",
        h1="The Future of Personal Styling — How AI Is Changing Fashion",
    ),
    17: dict(
        kw="capsule wardrobe by body type",
        title="Capsule Wardrobe by Body Type: A 12-Piece Blueprint",
        desc="Build a 12-piece capsule wardrobe tailored to YOUR body type. Pieces, ratios, color palette and tailoring priorities — free proportion analysis.",
        h1="How to Build a Capsule Wardrobe for Your Body Type",
    ),
    18: dict(
        kw="pear body shape dressing",
        title="Pear Body Shape: What to Wear (Jeans & Tops)",
        desc="Balance wider hips without hiding them: best necklines, denim rises, jackets & dresses. Outfit formulas + free proportion analysis.",
        h1="Pear Body Shape Dressing Guide",
    ),
    19: dict(
        kw="fabric guide by body type",
        title="Fabric Guide by Body Type: What Drapes vs What Clings",
        desc="Linen, jersey, ponte, twill: which fabrics drape vs cling on YOUR body type? The fabric guide every body shape should read before buying.",
        h1="Fabric Guide by Body Type — What Drapes vs Clings",
    ),
    20: dict(
        kw="measure body with hand span",
        title="No Tape? Measure Your Body with Hand Spans",
        desc="No ruler at home? Calibrate one hand span, then estimate shoulder, waist, hip & legs. Step-by-step guide + free FITME tool.",
        h1="How to Measure Anything with Your Hand Span",
    ),
    21: dict(
        kw="how to measure shoulder width",
        title="Measure Shoulder Width Alone — No Tape",
        desc="Find your acromion, count hand spans, compare to jacket charts. Self-measurement in 2 steps — no helper needed.",
        h1="How to Measure Shoulder Width Alone",
    ),
    22: dict(
        kw="how to measure arm length",
        title="Measure Arm Length at Home (Sleeve Fit)",
        desc="Sleeves too short online? Upper arm, forearm & total sleeve length with hand spans. Sizing for jackets and shirts.",
        h1="How to Measure Arm Length — Upper & Lower",
    ),
    23: dict(
        kw="how to measure leg length",
        title="Measure Leg Length for Inseam — No Tape",
        desc="Wrong inseam again? Greater-trochanter to ankle with hand spans + how to use the number on size charts.",
        h1="How to Measure Leg Length — Greater Trochanter to Ankle",
    ),
    24: dict(
        kw="how to measure hip circumference",
        title="Measure Hip Size Alone — Hand-Span Method",
        desc="Jeans size from hip circumference: landmarks, posture & two-span method without a mirror struggle.",
        h1="How to Measure Hip Circumference Alone",
    ),
    25: dict(
        kw="whr 0.65 meaning",
        title="WHR 0.65 — What It Means and How to Dress for It",
        desc="WHR 0.65 is the textbook 'attractive' ratio — what it really means, how to verify yours, and how to dress for it. Free body analysis included.",
        h1="WHR 0.65 — What It Means and How to Dress for It",
    ),
}

assert len(KW) == 25


def lim(s: str, n: int) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip(",. -—") + "…"


def update_html(path: Path, meta: dict[str, str]) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = raw

    title = lim(meta["title"], 60) + " | FITME"
    desc = lim(meta["desc"], 158)

    # <title>
    new = re.sub(
        r"<title>[^<]*</title>", f"<title>{title}</title>", new, count=1
    )
    # meta description
    new = re.sub(
        r'(<meta\s+name="description"\s+content=")[^"]*(")',
        lambda m: m.group(1) + desc + m.group(2),
        new,
        count=1,
    )
    # og:title
    new = re.sub(
        r'(<meta\s+property="og:title"\s+content=")[^"]*(")',
        lambda m: m.group(1) + title + m.group(2),
        new,
        count=1,
    )
    # og:description
    new = re.sub(
        r'(<meta\s+property="og:description"\s+content=")[^"]*(")',
        lambda m: m.group(1) + desc + m.group(2),
        new,
        count=1,
    )
    # twitter:title (only if exists)
    new = re.sub(
        r'(<meta\s+name="twitter:title"\s+content=")[^"]*(")',
        lambda m: m.group(1) + title + m.group(2),
        new,
        count=1,
    )
    new = re.sub(
        r'(<meta\s+name="twitter:description"\s+content=")[^"]*(")',
        lambda m: m.group(1) + desc + m.group(2),
        new,
        count=1,
    )
    # JSON-LD Article headline & description (first occurrence)
    new = re.sub(
        r'("headline":\s*)"[^"]*"',
        lambda m: m.group(1) + json.dumps(title, ensure_ascii=False),
        new,
        count=1,
    )
    new = re.sub(
        r'("description":\s*)"[^"]*"',
        lambda m: m.group(1) + json.dumps(desc, ensure_ascii=False),
        new,
        count=1,
    )
    # BreadcrumbList last item name (3rd ListItem) — update to match new clean title
    new = re.sub(
        r'("position":\s*3,\s*"name":\s*)"[^"]*"',
        lambda m: m.group(1) + json.dumps(meta["title"], ensure_ascii=False),
        new,
        count=1,
    )

    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    touched = []
    for n in sorted(KW):
        path = BLOG_DIR / f"blog{n}-en.html"
        if not path.exists():
            print(f"  MISSING: {path.name}")
            continue
        if update_html(path, KW[n]):
            touched.append(path.name)
    print(f"Updated {len(touched)}/25 English blog posts.")
    for name in touched:
        print(f"  {name}")


if __name__ == "__main__":
    main()

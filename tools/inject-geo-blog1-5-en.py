#!/usr/bin/env python3
"""GEO pack for blog1-en .. blog5-en. Idempotent."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
MODIFIED = "2026-05-18"

GEO_CSS = (
    ".lead-answer{font-size:16px;line-height:1.85;color:var(--text);margin-bottom:28px;"
    "padding:16px 18px;background:rgba(212,168,75,0.06);border-left:3px solid var(--accent);"
    "border-radius:0 8px 8px 0;}"
    ".faq-block{margin:36px 0 8px;}"
    ".faq-block h3{font-family:'DM Sans',sans-serif;font-size:16px;font-weight:700;"
    "margin:22px 0 8px;color:var(--text);}"
    ".faq-block p{font-size:15px;line-height:1.85;color:#d0d0d0;margin-bottom:14px;}"
)

POSTS: dict[str, dict] = {
    "blog1-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog1-en",
        "lead": (
            '<p class="lead-answer"><strong>The four main pants fits are slim, straight, wide-leg, and tapered — '
            "each changes your silhouette even at the same waist size.</strong> Slim emphasizes the leg line; "
            "straight is the most versatile default; wide-leg needs a tucked or cropped top; tapered balances "
            "a fuller thigh with a refined ankle. Match hem length to shoes: cropped for sneakers, grazing for "
            "loafers, slightly stacked over boots.</p>"
        ),
        "faqs": [
            (
                "Why do pants fit my hips but gap at the waist?",
                "This is a common low waist-to-hip ratio (WHR) issue: pants are sized to hip circumference, "
                "so the waistband can be loose at the natural waist. Size to your hips first, then have the "
                "waist taken in (waist suppression) — a low-cost alteration with high impact.",
            ),
            (
                "Should I size up or down when pants fit in one area but not another?",
                "Size to the largest measurement that must fit (usually hips), then alter down. Reducing "
                "waist, tapering the leg, or hemming is reliable; adding fabric is limited by seam allowance.",
            ),
            (
                "Which pants fit is best for wide hips?",
                "High-rise straight or wide-leg in structured fabric works well: the rise lifts the visual waist, "
                "and a consistent leg line avoids clinging at the thigh. Avoid low-rise skinny cuts that "
                "emphasize hip width.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Pants Fit Questions</h2>\s*'
            r'<p><strong>Q\. Why do pants always fit my hips but gap at the waist\?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Should I size up or down when pants fit in one area but not another\?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog2-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog2-en",
        "lead": (
            '<p class="lead-answer"><strong>Wide feet need shoes built on E, 2E, or 4E width lasts — not just a longer size.</strong> '
            "Going up half a size adds length but rarely fixes ball-of-foot width. Brands such as New Balance, "
            "Brooks, Altra, and Clarks often stock true wide widths; lace-up styles (Derby, sneakers) adjust better "
            "than fixed slip-ons.</p>"
        ),
        "faqs": [
            (
                "Can I buy a half-size up instead of wide width?",
                "Only partially. A larger size adds length and some width at the ball, but the widest point of the "
                "shoe may no longer align with your foot. A true wide last addresses width directly; try your "
                "correct length in E or 2E width.",
            ),
            (
                "Which shoe styles are most forgiving for wide feet?",
                "Laced shoes (Oxford, Derby, sneakers) are most adjustable. Slip-ons and narrow loafers are least "
                "forgiving. Chelsea boots with elastic gussets sit in between.",
            ),
            (
                "What do E, 2E, and 4E mean in shoe width?",
                "They mark width steps above standard D (medium): E (wide), 2E (extra wide), 4E (double extra wide). "
                "Each step is roughly 4–6 mm wider at the ball of the foot.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Wide Feet Shopping</h2>\s*'
            r'<p><strong>Q\. Can I just buy a half-size up instead of wide width\?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Which shoe styles are most forgiving for wide feet\?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog3-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog3-en",
        "lead": (
            '<p class="lead-answer"><strong>The golden ratio (about 1.618) describes proportional balance between '
            "upper and lower body in clothing — not a rule to copy literally.</strong> In practice, styling uses it "
            "to place visual weight: high-rise bottoms and defined waistlines lengthen the leg; shoulder emphasis "
            "or lower-body volume balances an inverted triangle. Monochrome dressing creates one continuous vertical "
            "line without color breaks.</p>"
        ),
        "faqs": [
            (
                "Is the golden ratio measurable in clothing?",
                "Yes, in visual terms. One application is the relationship between your perceived waistline and "
                "the lengths above and below it — high-waist bottoms with a shorter-looking torso and longer leg "
                "often read as more balanced.",
            ),
            (
                "Why do some outfits look right without following rules?",
                "You may be landing near classical proportions by instinct. Measuring your ratios (shoulder, waist, "
                "hip, leg) lets you repeat what works instead of guessing.",
            ),
            (
                "Does the golden ratio apply to every body type?",
                "The ideal is a guide, not a mandate. Hourglass shapes are often closest; pear, apple, rectangle, "
                "and inverted-triangle types use the same levers (rise, tuck, color placement) in opposite directions.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Golden Ratio Styling Questions</h2>\s*'
            r'<p><strong>Q\. Is the golden ratio actually measurable in clothing.*?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Why do some outfits.*?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog4-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog4-en",
        "lead": (
            '<p class="lead-answer"><strong>Tops should be chosen by shoulder fit first, then neckline and length — '
            "not by chest or waist alone.</strong> The shoulder seam must sit at the acromion (outer shoulder bone); "
            "altering shoulders is costly, waist suppression is cheap. Wide shoulders suit V-necks; narrow shoulders "
            "suit boat and square necklines; pear shapes benefit from volume and detail on top with cleaner bottoms.</p>"
        ),
        "faqs": [
            (
                "Should I size up for shoulders or down for waist?",
                "Size to shoulders always. Take in the waist or sides afterward. Shoulder alterations are the most "
                "expensive and complex change on a woven top.",
            ),
            (
                "Why do fitted tops pull or gap at the back?",
                "Usually shoulder width (too narrow pulls the back; too wide sags) or posture (rounded shoulders "
                "shift the seam). If the back hem rides up when you stand straight, the shoulder is likely too small.",
            ),
            (
                "Which neckline is best for wide shoulders?",
                "V-necks, deep scoop, and U-necks draw the eye inward and down. Avoid boat necks and wide square "
                "necklines that extend the horizontal shoulder line.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Common Tops Fit Questions</h2>\s*'
            r'<p><strong>Q\. Should I size up to accommodate my shoulders.*?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Why do fitted tops look fine from the front.*?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog5-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog5-en",
        "lead": (
            '<p class="lead-answer"><strong>Color placement changes perceived body width: dark tones recede, light '
            "and bright tones advance.</strong> Put darker colors where you want less visual emphasis and lighter "
            "or saturated colors where you want attention. Tonal (monochrome) dressing removes horizontal breaks and "
            "elongates; strong top/bottom contrast creates a waist line at the color boundary.</p>"
        ),
        "faqs": [
            (
                "Does wearing all black make you look thinner?",
                "All black removes color-based horizontal breaks, which elongates the silhouette — it does not "
                "magically shrink body mass. Seams, texture changes, or a contrasting belt can still create width "
                "perception.",
            ),
            (
                "Can I wear bright colors to minimize width in one area?",
                "Yes, with placement. Bright color on top draws attention up; on bottoms, down. To minimize hip "
                "width, use a darker, muted bottom and keep brightness on the upper body.",
            ),
            (
                "What is tonal dressing?",
                "Wearing the same or closely related shades head to toe. It creates one vertical line with fewer "
                "horizontal divisions — one of the most reliable ways to look taller and leaner in photos and mirrors.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Color and Proportion Questions</h2>\s*'
            r'<p><strong>Q\. Does wearing all black actually make you look thinner\?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Can I wear bright colors if my goal is to minimize.*?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
}


def faq_html_block(title: str, faqs: list[tuple[str, str]]) -> str:
    lines = [f"  <h2>{title}</h2>", '  <div class="faq-block">']
    for q, a in faqs:
        lines.append(f"    <h3>{q}</h3>")
        lines.append(f"    <p>{a}</p>")
    lines.append("  </div>")
    return "\n".join(lines)


FAQ_TITLES = {
    "blog1-en.html": "FAQ: Pants Fit Questions",
    "blog2-en.html": "FAQ: Wide Feet Shopping",
    "blog3-en.html": "FAQ: Golden Ratio Styling Questions",
    "blog4-en.html": "FAQ: Common Tops Fit Questions",
    "blog5-en.html": "FAQ: Color and Proportion Questions",
}


def faq_schema(canonical: str, faqs: list[tuple[str, str]]) -> str:
    entities = []
    for q, a in faqs:
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
        "url": canonical,
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


def inject_css(raw: str) -> str:
    if ".lead-answer" in raw:
        return raw
    return raw.replace(
        ".guide-img{width:100%;border-radius:12px;margin:28px 0;border:1px solid var(--border);}",
        ".guide-img{width:100%;border-radius:12px;margin:28px 0;border:1px solid var(--border);}\n"
        + GEO_CSS,
        1,
    )


def inject_lead(raw: str, lead: str) -> str:
    if 'class="lead-answer"' in raw:
        return raw
    m = re.search(r'(<img[^>]*class="guide-img"[^>]*>\s*)', raw, re.I)
    if not m:
        return raw
    return raw[: m.end()] + lead + "\n\n" + raw[m.end() :]


def inject_faq_schema(raw: str, schema: str) -> str:
    if '"@type": "FAQPage"' in raw:
        return raw
    return raw.replace(
        "</script>\n  <link rel=\"stylesheet\" href=\"/assets/satellite-pages-theme.css",
        "</script>\n" + schema + "\n  <link rel=\"stylesheet\" href=\"/assets/satellite-pages-theme.css",
        1,
    )


def inject_faq_body(raw: str, path_name: str, meta: dict) -> str:
    if 'class="faq-block"' in raw:
        return raw
    title = FAQ_TITLES[path_name]
    new_block = faq_html_block(title, meta["faqs"])
    m = meta["faq_old"].search(raw)
    if not m:
        return raw
    return raw[: m.start()] + new_block + "\n\n" + raw[m.end() :]


def bump_modified(raw: str) -> str:
    return re.sub(
        r'"dateModified":\s*"[^"]*"',
        f'"dateModified": "{MODIFIED}"',
        raw,
        count=1,
    )


def process(path: Path) -> bool:
    name = path.name
    if name not in POSTS:
        return False
    meta = POSTS[name]
    raw = path.read_text(encoding="utf-8")
    new = raw
    new = inject_css(new)
    new = inject_lead(new, meta["lead"])
    new = inject_faq_body(new, name, meta)
    new = inject_faq_schema(new, faq_schema(meta["canonical"], meta["faqs"]))
    new = bump_modified(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    touched = []
    for name in POSTS:
        p = BLOG / name
        if process(p):
            touched.append(name)
    print(f"Updated {len(touched)} files: {', '.join(touched)}")


if __name__ == "__main__":
    main()

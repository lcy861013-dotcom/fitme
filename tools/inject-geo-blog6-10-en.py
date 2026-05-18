#!/usr/bin/env python3
"""GEO pack for blog6-en .. blog10-en. Idempotent."""
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

FAQ_TITLES = {
    "blog6-en.html": "FAQ: Capsule Wardrobe",
    "blog7-en.html": "FAQ: Body Proportion Analysis",
    "blog8-en.html": "FAQ: WHR and Clothing Fit",
    "blog9-en.html": "FAQ: Shoulder Fit Questions",
    "blog10-en.html": "FAQ: Height and Proportions",
}

POSTS: dict[str, dict] = {
    "blog6-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog6-en",
        "lead": (
            '<p class="lead-answer"><strong>A five-piece capsule wardrobe can cover a full week '
            "when every item mixes with at least three others.</strong> Start with a white tee, "
            "black straight trousers, denim jacket, khaki chinos, and one wide-leg jean — then "
            "match hem length to shoes and fit shoulders first on every new basic.</p>"
        ),
        "faqs": [
            (
                "How do I know if my capsule basics actually fit?",
                "A well-fitted basic disappears: the eye reads your silhouette, not the garment. "
                "If you notice pulling at the shoulder, seat, or chest, fix those points before "
                "buying more pieces. Shoulder seam position and trouser rise matter more than brand size.",
            ),
            (
                "Which capsule basics work for a larger hip-to-waist difference?",
                "High-rise trousers in straight or wide leg, sized to the hip with waist tailoring if needed. "
                "Tops with structure at the shoulder balance the lower body. Avoid low-rise skinny cuts that "
                "emphasize hip width.",
            ),
            (
                "How many outfits can five basics really make?",
                "With two shoe options (sneakers and loafers), five cross-compatible tops and bottoms typically "
                "yield seven distinct weekday looks. Each new piece should pair with at least three items already "
                "in the set.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Capsule Wardrobe</h2>\s*'
            r'<p><strong>Q\. How do I know if my capsule basics actually fit.*?</strong>.*?</p>\s*'
            r'<p><strong>Q\. I have a larger hip-to-waist difference.*?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog7-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog7-en",
        "lead": (
            '<p class="lead-answer"><strong>Body proportions — shoulder, waist, hip, and leg ratios — '
            "predict how clothes look more reliably than weight alone.</strong> Two people at the same "
            "weight can need opposite silhouettes. Measure ratios, then style to balance what the numbers show, "
            "not what the scale says.</p>"
        ),
        "faqs": [
            (
                "My weight is stable but clothes fit differently — why?",
                "Body composition shifts without large weight change: muscle and fat redistribute at shoulders, "
                "waist, and hips. Re-measure key ratios every 3–6 months instead of relying on scale weight alone.",
            ),
            (
                "Should I trust measured shoulder-to-hip ratio or mirror perception?",
                "Trust the measurement. Front-mirror views understate shoulder width versus how garments fit across "
                "the back. Apply styling rules for your measured ratio for one week and compare photos.",
            ),
            (
                "What is the most overlooked proportion for everyday styling?",
                "Leg-to-torso ratio (inseam ÷ height). Below 0.44 usually benefits from high-rise bottoms and "
                "cropped or tucked tops; above 0.47 can emphasize leg length with cleaner hems and vertical color.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Body Proportion Analysis</h2>\s*'
            r'<p><strong>Q\. My weight has stayed the same.*?</p>\s*'
            r'<p><strong>Q\. My SHR says.*?</p>',
            re.DOTALL,
        ),
    },
    "blog8-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog8-en",
        "lead": (
            '<p class="lead-answer"><strong>WHR (waist ÷ hips) describes body shape and drives how '
            "ready-to-wear fits at the waist and hip.</strong> Lower WHR suits defined-waist styles; "
            "higher WHR benefits from high-rise, A-line, and vertical color breaks. Measure at the "
            "narrowest waist and widest hip, then shop to both numbers.</p>"
        ),
        "faqs": [
            (
                "What is a healthy WHR for women and men?",
                "WHO guidelines often cite below 0.85 for women and below 0.90 for men as lower health risk. "
                "For styling, the useful question is where your WHR sits relative to standard pattern blocks (often ~0.72–0.78 for women's RTW).",
            ),
            (
                "Why do pants fit my hips but gap at the waist?",
                "Your WHR is lower than the pattern's: the garment is cut for more waist taper. Size to the hip, "
                "then alter the waist (waist suppression) — the most common fix for hourglass and pear proportions.",
            ),
            (
                "Can WHR change without weight loss?",
                "Yes. Hip muscle gain or waist recomposition changes the ratio even at stable weight. Track WHR monthly "
                "if you are training glutes or changing core habits.",
            ),
        ],
        "faq_insert_before": re.compile(r"\n    <div class=\"related\">"),
    },
    "blog9-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog9-en",
        "lead": (
            '<p class="lead-answer"><strong>Shoulder fit is the non-negotiable anchor for every top and jacket — '
            "the seam must sit on the acromion.</strong> Wide shoulders suit V-necks and raglan ease; narrow shoulders "
            "benefit from structure, boat necks, and light padding. Size to shoulder first; alter chest and waist second.</p>"
        ),
        "faqs": [
            (
                "Can I stretch a shoulder seam that is too small?",
                "No. Shoulder seams are reinforced; if the shoulder is too small, exchange the size. Meaningful shoulder "
                "alterations are expensive and rarely worth it on casual tops.",
            ),
            (
                "My shoulders are uneven — what should I do?",
                "Up to ~1 cm asymmetry is usually invisible. For larger gaps, fit structured pieces to the higher shoulder "
                "and use light padding or tailoring on the lower side.",
            ),
            (
                "Should I buy for shoulder width or chest measurement?",
                "Shoulder first. Chest can be taken in or let out; shoulder position cannot be fixed affordably.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Shoulder Fit Questions</h2>\s*'
            r'<p><strong>Q\. Can I stretch a shoulder seam.*?</strong>.*?</p>\s*'
            r'<p><strong>Q\. My shoulders are naturally uneven.*?</strong>.*?</p>\s*'
            r'<p><strong>Q\. Should I buy to fit my shoulder width.*?</strong>.*?</p>',
            re.DOTALL,
        ),
    },
    "blog10-en.html": {
        "canonical": "https://perfectfitme.com/blog/blog10-en",
        "lead": (
            '<p class="lead-answer"><strong>Perceived height comes from leg ratio and vertical lines — not only '
            "your measured height.</strong> High-rise bottoms, tonal dressing, and ankle breaks that match your shoes "
            "add 2–3 cm visually. Calculate inseam ÷ height; below 0.44 prioritize raising the visual waist.</p>"
        ),
        "faqs": [
            (
                "I'm average height but look shorter — why?",
                "Low leg-to-torso ratio drags the visual waist down. High-rise pants and tucked or cropped tops raise "
                "where the leg appears to start.",
            ),
            (
                "Do heels make a meaningful difference?",
                "Yes: literal height plus posture. Pointed flats in the same color as trousers achieve much of the "
                "continuous leg-line effect without a heel.",
            ),
            (
                "Do height tricks only work for short people?",
                "No. Tall people with long torsos benefit equally from high-rise and vertical monochrome to balance "
                "proportions.",
            ),
        ],
        "faq_old": re.compile(
            r'  <h2>FAQ: Common Questions About Height and Proportions</h2>\s*'
            r'(?:<p><strong>Q\..*?</p>\s*){3}',
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


def faq_schema(canonical: str, faqs: list[tuple[str, str]]) -> str:
    entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faqs
    ]
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
    m = meta.get("faq_old")
    if m:
        hit = m.search(raw)
        if hit:
            return raw[: hit.start()] + new_block + "\n\n" + raw[hit.end() :]
    before = meta.get("faq_insert_before")
    if before:
        hit = before.search(raw)
        if hit:
            return raw[: hit.start()] + "\n\n" + new_block + "\n" + raw[hit.start() :]
    return raw


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

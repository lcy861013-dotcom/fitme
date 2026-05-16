#!/usr/bin/env python3
"""
Rebuild the "Related Guides" block on every English blog post with a
topic-cluster-based mapping. Goals:
  - Improve internal link relevance (Google E-E-A-T topic-authority signal)
  - Increase pages/session and dwell time
  - Surface measurement guides from styling articles and vice versa
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

# Master link metadata: (slug, anchor_text) — anchor uses optimized SEO phrase, not raw title.
LINKS = {
    1:  ("/blog/blog1-en",  "Pants Fit Guide — Slim, Straight, Wide & Tapered"),
    2:  ("/blog/blog2-en",  "Best Shoes for Wide Feet — 12 Brands"),
    3:  ("/blog/blog3-en",  "Golden Ratio Body Proportions Explained"),
    4:  ("/blog/blog4-en",  "How to Dress for Your Body Type — Tops"),
    5:  ("/blog/blog5-en",  "Color Rules to Flatter Your Body Shape"),
    6:  ("/blog/blog6-en",  "5 Capsule Wardrobe Basics"),
    7:  ("/blog/blog7-en",  "Why Body Proportions Beat Weight"),
    8:  ("/blog/blog8-en",  "Waist-to-Hip Ratio (WHR) Explained"),
    9:  ("/blog/blog9-en",  "How Shoulder Width Changes Your Fit"),
    10: ("/blog/blog10-en", "How to Look Taller — 5 Outfit Tricks"),
    11: ("/blog/blog11-en", "Why Clothes Never Fit Right"),
    12: ("/blog/blog12-en", "Find Your Real Body Type with Data"),
    13: ("/blog/blog13-en", "Dress Every Body Type — Complete Guide"),
    14: ("/blog/blog14-en", "Body Symmetry and Attractiveness Science"),
    15: ("/blog/blog15-en", "Stop Guessing — Data-Driven Style"),
    16: ("/blog/blog16-en", "AI Personal Styling — How It Works"),
    17: ("/blog/blog17-en", "Capsule Wardrobe by Body Type — 12 Pieces"),
    18: ("/blog/blog18-en", "Pear Body Shape Dressing Guide"),
    19: ("/blog/blog19-en", "Fabric Guide by Body Type"),
    20: ("/blog/blog20-en", "Measure Anything with Hand Spans"),
    21: ("/blog/blog21-en", "How to Measure Shoulder Width Alone"),
    22: ("/blog/blog22-en", "How to Measure Arm Length"),
    23: ("/blog/blog23-en", "How to Measure Leg Length"),
    24: ("/blog/blog24-en", "How to Measure Hip Circumference"),
    25: ("/blog/blog25-en", "WHR 0.65 — Meaning & Styling"),
}

# Topic clusters: every post gets 4 related posts pulled from its primary cluster
# + 1 cross-cluster bridge (e.g., a styling post links to one measurement post and
# one body-type post). This builds a strong topic hub graph.
#
# Cluster A — Body type & fit (#1, 4, 13, 18, 17, 11, 19)
# Cluster B — Measurement how-to (#20, 21, 22, 23, 24)
# Cluster C — Science / proportion theory (#3, 7, 8, 14, 25)
# Cluster D — Outfit techniques (#5, 6, 9, 10, 16, 15)
# Cluster E — Wide-foot shoes (#2)
RELATED = {
    1:  [4, 23, 13, 17],       # pants fit -> tops, measure-leg, body-type, capsule
    2:  [9, 21, 13, 6],        # wide shoes -> shoulder-fit, shoulder-measure, body-type, basics
    3:  [8, 25, 7, 12],        # golden ratio -> whr, whr-0.65, proportions, find-type
    4:  [13, 1, 18, 9],        # tops -> body-type, pants, pear, shoulder-width
    5:  [13, 18, 10, 4],       # color -> body-type, pear, look-taller, tops
    6:  [17, 13, 4, 1],        # 5 basics -> capsule-by-type, body-type, tops, pants
    7:  [12, 8, 3, 25],        # proportions vs weight -> find-type, whr, golden, whr-0.65
    8:  [25, 3, 14, 24],       # whr -> whr-0.65, golden, symmetry, hip-measure
    9:  [21, 4, 11, 1],        # shoulder fit -> shoulder-measure, tops, never-fit, pants
    10: [3, 1, 12, 13],        # look taller -> golden, pants, find-type, body-type
    11: [12, 13, 17, 9],       # clothes never fit -> find-type, body-type, capsule, shoulder
    12: [13, 8, 3, 20],        # find body type -> dress-every-type, whr, golden, hand-span
    13: [4, 1, 18, 17],        # dress every body type -> tops, pants, pear, capsule
    14: [3, 8, 7, 25],         # symmetry -> golden, whr, proportions, whr-0.65
    15: [12, 16, 13, 7],       # data style -> find-type, ai, body-type, proportions
    16: [15, 12, 13, 7],       # AI styling -> data-style, find-type, body-type, proportions
    17: [13, 4, 1, 6],         # capsule by type -> body-type, tops, pants, basics
    18: [13, 5, 1, 4],         # pear -> body-type, color, pants, tops
    19: [13, 18, 17, 11],      # fabric -> body-type, pear, capsule, never-fit
    20: [21, 24, 23, 22],      # hand span -> all measurement guides
    21: [20, 22, 9, 24],       # shoulder measure -> hand-span, arm, shoulder-fit, hip
    22: [20, 21, 23, 24],      # arm -> all measurement guides
    23: [20, 24, 21, 1],       # leg -> hand-span, hip, shoulder-measure, pants
    24: [20, 23, 21, 8],       # hip -> hand-span, leg, shoulder-measure, whr
    25: [8, 3, 14, 12],        # whr 0.65 -> whr, golden, symmetry, find-type
}


def render_block(post_num: int) -> str:
    targets = RELATED[post_num]
    cards = []
    for t in targets:
        href, anchor = LINKS[t]
        cards.append(
            f'    <a href="{href}" class="related-card">{anchor}</a>'
        )
    return (
        '  <div class="related">\n'
        '    <div class="related-title">Related Guides</div>\n'
        '    <div class="related-grid">\n'
        + "\n".join(cards) + "\n"
        '    </div>\n'
        '  </div>'
    )


RELATED_RE = re.compile(
    r'<div class="related">.*?</div>\s*</div>',
    re.DOTALL,
)


def update_post(n: int) -> bool:
    path = BLOG / f"blog{n}-en.html"
    if not path.exists():
        return False
    raw = path.read_text(encoding="utf-8")
    new_block = render_block(n)
    new = RELATED_RE.sub(new_block, raw, count=1)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    touched = []
    for n in sorted(RELATED):
        if update_post(n):
            touched.append(n)
    print(f"Updated related-guides block on {len(touched)}/25 EN posts.")
    for n in touched:
        print(f"  blog{n}-en.html")


if __name__ == "__main__":
    main()

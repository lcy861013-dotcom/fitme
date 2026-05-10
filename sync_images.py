import os
import re

def translate_alt(alt_text, title):
    # Simple heuristic for translation or use title
    if "팬츠 핏" in alt_text: return "Pants fit types comparison chart - Slim, Straight, Wide, Tapered silhouettes"
    if "발 너비" in alt_text or "신발" in alt_text: return "Wide foot shoe fitting guide and measurements"
    if "황금비율" in alt_text: return "Golden ratio body proportions and vertical balance guide"
    if "상체" in alt_text: return "Upper body type and neckline styling guide"
    if "퍼스널 컬러" in alt_text: return "Personal color palette and coordination guide"
    if "기본템" in alt_text: return "Essential wardrobe basics for weekly coordination"
    if "체중" in alt_text or "비율" in alt_text: return "Body proportion vs weight visual comparison"
    if "WHR" in alt_text or "허리" in alt_text: return "Waist-to-hip ratio (WHR) measurement and health range guide"
    if "어깨 너비" in alt_text: return "Shoulder width measurement and styling impact"
    if "다리 길이" in alt_text: return "Leg length ratio and visual height secrets"
    if "핏 문제" in alt_text: return "Common fit problems and tailoring solutions"
    if "데이터" in alt_text: return "Body type data and measurement-based styling"
    if "4대 체형" in alt_text or "체형 종류" in alt_text: return "Four major body types classification and characteristics"
    if "대칭" in alt_text: return "Body symmetry and proportion balance analysis"
    if "데이터 스타일링" in alt_text: return "Data-driven styling and measurement reference"
    if "AI" in alt_text: return "AI-powered fashion and body analysis technology"
    if "캡슐" in alt_text: return "Capsule wardrobe planning for your body type"
    if "배형" in alt_text or "Pear" in alt_text: return "Pear body shape characteristics and balancing guide"
    if "소재" in alt_text or "원단" in alt_text: return "Fabric drape and structure guide for different body types"
    
    return f"Guide image for {title}"

def process_file(i):
    ko_file = f"blog/blog{i}.html"
    en_file = f"blog/blog{i}-en.html"
    
    if not os.path.exists(ko_file) or not os.path.exists(en_file):
        return

    with open(ko_file, 'r', encoding='utf-8') as f:
        ko_content = f.read()
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_content = f.read()

    # Skip if already has guide-img
    if 'class="guide-img"' in en_content or '.guide-img' in en_content:
        print(f"Skipping blog{i}-en.html (already has guide-img)")
        # Actually some might have one but not the other, but the user said "synchronize"
        # Let's check if it's really missing.
        # If it's in the missing list from grep, it's missing.

    # Extract img tag from KO
    img_match = re.search(r'<img[^>]+class="guide-img"[^>]*>', ko_content)
    if not img_match:
        print(f"No guide-img in {ko_file}")
        return

    img_tag = img_match.group(0)
    
    # Extract alt and translate
    alt_match = re.search(r'alt="([^"]*)"', img_tag)
    title_match = re.search(r'<title>([^|]*)\|', en_content)
    title = title_match.group(1).strip() if title_match else f"Blog {i}"
    
    if alt_match:
        old_alt = alt_match.group(1)
        new_alt = translate_alt(old_alt, title)
        img_tag = img_tag.replace(f'alt="{old_alt}"', f'alt="{new_alt}"')

    # Add CSS if missing
    css_rule = '.guide-img{width:100%;border-radius:12px;margin:28px 0;border:1px solid var(--border);}'
    if '.guide-img' not in en_content:
        en_content = en_content.replace('</style>', f'{css_rule}\n</style>')

    # Insert Image if missing
    if 'class="guide-img"' not in en_content:
        # Find meta div
        meta_pattern = r'(<div class="meta">.*?</div>)'
        en_content = re.sub(meta_pattern, rf'\1\n  {img_tag}', en_content, flags=re.DOTALL)

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(en_content)
    print(f"Processed blog{i}-en.html")

for i in range(1, 26):
    process_file(i)

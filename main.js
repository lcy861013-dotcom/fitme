// Translations Dictionary
const translations = {
  ko: {
    "nav-guide": "측정 가이드",
    "nav-analysis": "비율 분석",
    "nav-about": "About",
    "guide-title": "올바른 신체 치수 측정 가이드",
    "phone-guide-title": "📱 스마트폰 활용 측정법 (No Tape?)",
    "phone-guide-desc": "줄자가 없으신가요? 여러분의 스마트폰을 사용해 보세요! 최신 스마트폰의 평균 세로 길이는 약 15cm입니다. 무릎에서 골반까지 스마트폰이 약 3번 들어간다면 해당 부위의 길이는 약 45cm로 추정할 수 있습니다.",
    "head-guide-title": "🧢 머리 둘레 측정 꿀팁",
    "head-guide-desc": "곡선인 머리 둘레는 <b>충전 케이블</b>을 활용하세요! 케이블을 머리에 한 바퀴 두른 뒤, 그 길이를 스마트폰(15cm)으로 재보세요. 약 3.8번이면 57cm(보통), 4번이면 60cm(대형)입니다.",
    "pro-guide-title": "📏 전문가 권장 측정 자세",
    "pro-guide-desc": "정확한 비율 분석을 위해 거울 앞에서 바른 자세로 서서 측정하세요. 특히 키(Height)와 체중(Weight)은 신체 밸런스를 분석하는 핵심 데이터입니다.",
    "section-label": "부위를 클릭하여 측정값을 입력하세요",
    "panel-title": "신체 정보 입력",
    "panel-subtitle": "정확한 분석을 위해 치수를 입력해 주세요.",
    "placeholder-text": "왼쪽 인체 도형에서<br>부위를 클릭해 주세요",
    "form-title-height": "TOTAL HEIGHT / 키",
    "form-desc-height": "전체 키는 비율 분석의 핵심 데이터입니다.",
    "form-title-weight": "WEIGHT / 체중",
    "form-desc-weight": "정밀한 체형 및 BMI 분석을 위해 필요합니다.",
    "label-height": "키 (cm)",
    "label-weight": "체중 (kg)",
    "btn-save": "저장하기",
    "btn-analyze": "🔥 전문가 신체 비율 분석하기",
    "btn-reset": "초기화",
    "analysis-report-title": "전문가 분석 리포트",
    "analysis-note": "*위 분석은 입력된 수치 기반의 통계적 결과입니다.",
    "toast-save-suffix": " 저장 완료 ✓",
    "toast-input-req": "값을 입력해주세요!",
    "toast-analysis-req": "분석을 위해 [키, 체중, 대퇴, 하퇴] 값을 먼저 입력해주세요.",
    "analysis-long-legs": "전체 키 대비 다리가 매우 긴 **'서구형 롱다리 체형'**입니다. 어떤 옷을 입어도 비율이 돋보이는 모델 체형입니다.",
    "analysis-balanced": "키 대비 다리 비율이 매우 **'균형 잡힌 황금 비율'**을 가지고 계십니다. 훌륭한 비율입니다.",
    "analysis-classic": "전체 키 대비 상체가 발달한 **'안정적인 클래식 체형'**입니다. 하이웨이스트 스타일링을 추천합니다.",
    "bmi-under": "저체중 (BMI: ",
    "bmi-normal": "정상 (BMI: ",
    "bmi-over": "과체중 (BMI: ",
    "bmi-obese": "비만 (BMI: ",
    "form-title-head": "HEAD / 머리",
    "form-title-shoulder": "SHOULDER / 어깨",
    "form-title-chest": "CHEST / 가슴",
    "form-title-upper-arm": "SHOULDER TO ELBOW / 어깨~팔꿈치",
    "form-title-lower-arm": "ELBOW TO WRIST / 팔꿈치~손목",
    "form-title-waist": "WAIST / 허리",
    "form-title-hip": "HIP / 골반",
    "form-title-upper-leg": "HIP TO KNEE / 골반~무릎",
    "form-title-lower-leg": "KNEE TO ANKLE / 무릎~복숭아뼈",
    "form-title-foot": "FOOT / 발",
    "label-circ": "둘레 (cm)",
    "label-width": "너비 (cm)",
    "label-len": "길이 (cm)",
    "label-size": "사이즈 (mm)",
    "label-head-height": "세로 길이 (cm)",
    "form-desc-upper-arm": "어깨뼈에서 팔꿈치 중간까지의 길이입니다.",
    "form-desc-lower-arm": "팔꿈치 중간에서 손목뼈까지의 길이입니다.",
    "form-desc-upper-leg": "골반뼈 끝에서 무릎 중간까지의 길이입니다.",
    "form-desc-lower-leg": "무릎 중간에서 복숭아뼈까지의 길이입니다.",
    "style-best-title": "✨ BEST 스타일 추천",
    "style-worst-title": "⚠️ 주의할 스타일",
    "toast-share-success": "분석 결과 링크가 복사되었습니다!",
    "toast-image-save": "이미지 저장 기능을 준비 중입니다. (브라우저 스크린샷 권장)",
    "adv-report-title": "💎 FITME 프리미엄 분석 (v1.4)",
    "adv-identity-label": "체형 아이덴티티",
    "adv-head-label": "8등신 지수",
    "adv-leg-label": "다리 황금비율",
    "adv-balance-label": "상하체 밸런스",
    "adv-ranking-label": "글로벌 상위 비율",
    "adv-recommend-title": "👗 데이터 기반 추천 코디",
    "adv-shop-now": "Shop Now",
    "adv-ranking-suffix": "등급의 비율입니다!",
    "adv-identity-hourglass": "골반이 강조된 모래시계형",
    "adv-identity-pear": "부드러운 곡선의 하체 강조형",
    "adv-identity-inv": "활동적인 느낌의 상체 발달형",
    "adv-identity-rect": "도시적인 슬림 일자형",
    "adv-identity-apple": "건강미 넘치는 원형 체형",
    "adv-identity-default": "매력적인 유니크 체형"
  },
  en: {
    "nav-guide": "Guide",
    "nav-analysis": "Analysis",
    "nav-about": "About",
    "guide-title": "Body Measurement Guide",
    "phone-guide-title": "📱 Phone Scale Method",
    "phone-guide-desc": "No measuring tape? Use your smartphone!",
    "head-guide-title": "🧢 Head Size Tips",
    "head-guide-desc": "Use a <b>charging cable</b> for curves!",
    "pro-guide-title": "📏 Professional Posture",
    "pro-guide-desc": "Stand straight before a mirror.",
    "section-label": "Click a body part to enter measurements",
    "panel-title": "Body Measurements",
    "panel-subtitle": "Please enter your data for analysis.",
    "placeholder-text": "Click a body part<br>on the left figure",
    "form-title-height": "TOTAL HEIGHT",
    "form-title-weight": "WEIGHT",
    "label-height": "Height (cm)",
    "label-weight": "Weight (kg)",
    "btn-save": "Save",
    "btn-analyze": "🔥 Run Expert Analysis",
    "btn-reset": "Reset",
    "analysis-report-title": "Expert Analysis Report",
    "analysis-note": "*Results are statistical based on provided data.",
    "toast-save-suffix": " Saved ✓",
    "toast-input-req": "Please enter a value!",
    "toast-analysis-req": "Please enter [Height, Weight, Thigh, Shin] first.",
    "analysis-long-legs": "You have **'Model proportions'** with very long legs.",
    "analysis-balanced": "Your body has a **'Golden Ratio'**.",
    "analysis-classic": "You have an **'Stable Classic'** build.",
    "bmi-under": "Underweight (BMI: ",
    "bmi-normal": "Normal (BMI: ",
    "bmi-over": "Overweight (BMI: ",
    "bmi-obese": "Obese (BMI: ",
    "form-title-head": "HEAD",
    "form-title-neck": "NECK",
    "form-title-shoulder": "SHOULDER",
    "form-title-chest": "CHEST",
    "form-title-upper-arm": "UPPER ARM",
    "form-title-lower-arm": "LOWER ARM",
    "form-title-waist": "WAIST",
    "form-title-hip": "HIP",
    "form-title-upper-leg": "THIGH",
    "form-title-lower-leg": "SHIN",
    "form-title-foot": "FOOT",
    "label-circ": "Circumference (cm)",
    "label-width": "Width (cm)",
    "label-len": "Length (cm)",
    "label-size": "Size (mm)",
    "label-head-height": "Vertical Height (cm)",
    "style-best-title": "✨ BEST Style Picks",
    "style-worst-title": "⚠️ Styles to Avoid",
    "toast-share-success": "Link copied to clipboard!",
    "toast-image-save": "Preparing image save... (Use screenshot for now)",
    "adv-report-title": "💎 FITME Premium Analysis (v1.4)",
    "adv-identity-label": "Body Identity",
    "adv-head-label": "Figure Ratio",
    "adv-leg-label": "Leg Golden Ratio",
    "adv-balance-label": "Upper/Lower Balance",
    "adv-ranking-label": "Global Percentile",
    "adv-recommend-title": "👗 Data-Driven Style Guide",
    "adv-shop-now": "Shop Now",
    "adv-ranking-suffix": "tier proportions!",
    "adv-identity-hourglass": "Pelvis-Emphasized Hourglass",
    "adv-identity-pear": "Soft Curve Pear Shape",
    "adv-identity-inv": "Athletic Inverted Triangle",
    "adv-identity-rect": "Urban Slim Rectangle",
    "adv-identity-apple": "Healthy Rounded Apple",
    "adv-identity-default": "매력적인 유니크 체형",
    "unit-metric": "Metric (cm/kg)",
    "unit-imperial": "Imperial (in/lb)",
    "emblem-label": "신체 아이덴티티 등급",
    "emblem-s": "👑 Royal Frame",
    "emblem-ap": "✨ Elite Muse",
    "emblem-a": "💎 Classic Alpha",
    "emblem-bp": "🌟 Trendy Icon",
    "emblem-b": "🌿 Natural Fit",
    "emblem-c": "🎨 Unique Origin"
  },
  en: {
    "nav-guide": "Guide",
    "nav-analysis": "Analysis",
    "nav-about": "About",
    "guide-title": "Body Measurement Guide",
    "phone-guide-title": "📱 Phone Scale Method",
    "phone-guide-desc": "No measuring tape? Use your smartphone!",
    "head-guide-title": "🧢 Head Size Tips",
    "head-guide-desc": "Use a <b>charging cable</b> for curves!",
    "pro-guide-title": "📏 Professional Posture",
    "pro-guide-desc": "Stand straight before a mirror.",
    "section-label": "Click a body part to enter measurements",
    "panel-title": "Body Measurements",
    "panel-subtitle": "Please enter your data for analysis.",
    "placeholder-text": "Click a body part<br>on the left figure",
    "form-title-height": "TOTAL HEIGHT",
    "form-title-weight": "WEIGHT",
    "label-height": "Height",
    "label-weight": "Weight",
    "btn-save": "Save",
    "btn-analyze": "🔥 Run Expert Analysis",
    "btn-reset": "Reset",
    "analysis-report-title": "Expert Analysis Report",
    "analysis-note": "*Results are statistical based on provided data.",
    "toast-save-suffix": " Saved ✓",
    "toast-input-req": "Please enter a value!",
    "toast-analysis-req": "Please enter [Height, Weight, Thigh, Shin] first.",
    "analysis-long-legs": "You have **'Model proportions'** with very long legs.",
    "analysis-balanced": "Your body has a **'Golden Ratio'**.",
    "analysis-classic": "You have an **'Stable Classic'** build.",
    "bmi-under": "Underweight (BMI: ",
    "bmi-normal": "Normal (BMI: ",
    "bmi-over": "Overweight (BMI: ",
    "bmi-obese": "Obese (BMI: ",
    "form-title-head": "HEAD",
    "form-title-neck": "NECK",
    "form-title-shoulder": "SHOULDER",
    "form-title-chest": "CHEST",
    "form-title-upper-arm": "UPPER ARM",
    "form-title-lower-arm": "LOWER ARM",
    "form-title-waist": "WAIST",
    "form-title-hip": "HIP",
    "form-title-upper-leg": "THIGH",
    "form-title-lower-leg": "SHIN",
    "form-title-foot": "FOOT",
    "label-circ": "Circumference",
    "label-width": "Width",
    "label-len": "Length",
    "label-size": "Size (mm)",
    "label-head-height": "Vertical Height",
    "style-best-title": "✨ BEST Style Picks",
    "style-worst-title": "⚠️ Styles to Avoid",
    "toast-share-success": "Link copied to clipboard!",
    "toast-image-save": "Preparing image save... (Use screenshot for now)",
    "adv-report-title": "💎 FITME Premium Analysis (v1.4)",
    "adv-identity-label": "Body Identity",
    "adv-head-label": "Figure Ratio",
    "adv-leg-label": "Leg Golden Ratio",
    "adv-balance-label": "Upper/Lower Balance",
    "adv-ranking-label": "Global Percentile",
    "adv-recommend-title": "👗 Data-Driven Style Guide",
    "adv-shop-now": "Shop Now",
    "adv-ranking-suffix": "tier proportions!",
    "adv-identity-hourglass": "Pelvis-Emphasized Hourglass",
    "adv-identity-pear": "Soft Curve Pear Shape",
    "adv-identity-inv": "Athletic Inverted Triangle",
    "adv-identity-rect": "Urban Slim Rectangle",
    "adv-identity-apple": "Healthy Rounded Apple",
    "adv-identity-default": "Charming Unique Shape",
    "unit-metric": "Metric (cm/kg)",
    "unit-imperial": "Imperial (in/lb)",
    "emblem-label": "Body Identity Rank",
    "emblem-s": "👑 Royal Frame",
    "emblem-ap": "✨ Elite Muse",
    "emblem-a": "💎 Classic Alpha",
    "emblem-bp": "🌟 Trendy Icon",
    "emblem-b": "🌿 Natural Fit",
    "emblem-c": "🎨 Unique Origin"
  }
};

// State
let currentLang = 'ko';
let currentUnit = 'metric'; // 'metric' or 'imperial'
let measurements = JSON.parse(localStorage.getItem('fitme_measurements')) || {};

/**
 * Unit conversion helper
 */
function toggleUnit(unit) {
  if (currentUnit === unit) return;
  
  const oldUnit = currentUnit;
  currentUnit = unit;
  
  // Convert existing values in inputs
  document.querySelectorAll('.input-field').forEach(input => {
    const val = parseFloat(input.value);
    if (!isNaN(val)) {
      if (unit === 'imperial') { // cm -> in, kg -> lb
        if (input.id.includes('weight')) input.value = (val * 2.20462).toFixed(1);
        else if (input.id.includes('foot')) return; // foot size usually mm
        else input.value = (val / 2.54).toFixed(1);
      } else { // in -> cm, lb -> kg
        if (input.id.includes('weight')) input.value = (val / 2.20462).toFixed(1);
        else if (input.id.includes('foot')) return;
        else input.value = (val * 2.54).toFixed(1);
      }
    }
  });

  // Update labels
  document.querySelectorAll('.unit-toggle-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.unit === unit);
  });
  
  const labels = {
    metric: { h: 'cm', w: 'kg', l: 'cm' },
    imperial: { h: 'in', w: 'lb', l: 'in' }
  };
  
  // Update UI unit labels if any (e.g. "Height (cm)")
  setLanguage(currentLang); 
}

// UI Elements
const placeholder = document.getElementById('placeholder');
const analysisCard = document.getElementById('analysis-result');
const analysisText = document.getElementById('analysis-text');
const bmiText = document.getElementById('bmi-text');
const bestStyles = document.getElementById('best-styles');
const worstStyles = document.getElementById('worst-styles');

/**
 * Set Language and update UI
 */
function setLanguage(lang) {
  currentLang = lang;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang] && translations[lang][key]) {
      if (el.tagName === 'INPUT') el.placeholder = translations[lang][key];
      else el.innerHTML = translations[lang][key];
    }
  });
  document.documentElement.lang = lang;
}

/**
 * Select a body part to show its input form
 */
function selectPart(part) {
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  placeholder.style.display = 'none';
  const form = document.getElementById('form-' + part);
  
  if (form) {
    form.classList.add('visible');
    if (window.innerWidth <= 900) {
      document.querySelector('.panel').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
  
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('active'));
  const hs = document.getElementById('hs-' + part);
  if (hs) hs.classList.add('active');
}

/**
 * Save measurement for a specific part
 */
function savePart(part) {
  const fieldMappings = {
    height: ['input-height'],
    weight: ['input-weight'],
    head: ['head-circ', 'head-height'],
    neck: ['neck-circ'],
    shoulder: ['shoulder-width'],
    chest: ['chest-circ'],
    'upper-arm': ['upper-arm-len'],
    'lower-arm': ['lower-arm-len'],
    waist: ['waist-circ'],
    hip: ['hip-circ'],
    'upper-leg': ['upper-leg-len'],
    'lower-leg': ['lower-leg-len'],
    foot: ['foot-size']
  };
  
  const fields = fieldMappings[part];
  let allValid = true;

  fields.forEach(fId => {
    const el = document.getElementById(fId);
    const val = el ? el.value : null;
    if (!val) {
      allValid = false;
    } else {
      measurements[fId] = parseFloat(val);
    }
  });

  if (!allValid) {
    showToast(translations[currentLang]["toast-input-req"]);
    return;
  }

  // Save to LocalStorage
  localStorage.setItem('fitme_measurements', JSON.stringify(measurements));

  const hs = document.getElementById('hs-' + part);
  if (hs) hs.classList.add('filled');
  
  showToast(partTitle + translations[currentLang]["toast-save-suffix"]);
}

/**
 * Advanced Analysis Upgrade (v1.4)
 * Calculates high-precision metrics and generates detailed styling report.
 */
function runAdvancedAnalysis() {
  const t = (key) => translations[currentLang][key] || key;
  const getVal = (p, key) => {
    if (!measurements[p]) return NaN;
    const d = measurements[p];
    if (typeof d === 'object') return parseFloat(d[key] || d.val || d.width || d.circ || d.len || 0);
    return parseFloat(d);
  };

  const h = getVal('input-height'), 
        headH = getVal('head-height'),
        shoulder = getVal('shoulder-width'),
        hip = getVal('hip-circ'),
        uLeg = getVal('upper-leg-len'),
        lLeg = getVal('lower-leg-len'),
        waist = getVal('waist-circ');

  if (isNaN(h)) return;

  // 1. Identity & Metrics
  let bodyType = 'default';
  if (!isNaN(waist) && !isNaN(hip) && !isNaN(shoulder)) {
    const s = shoulder * 2;
    if (Math.abs(s - hip) < (hip * 0.05) && waist < (hip * 0.75)) bodyType = 'hourglass';
    else if (hip > (s * 1.05)) bodyType = 'pear';
    else if (s > (hip * 1.05)) bodyType = 'inv';
    else if (waist > (hip * 0.85)) bodyType = 'apple';
    else bodyType = 'rect';
  }

  // 8-head figure ratio
  const headRatio = !isNaN(headH) ? (h / headH).toFixed(1) : '-';
  const headDesc = headRatio >= 8 ? (currentLang === 'ko' ? '환상적인 모델 비율' : 'Perfect Model Ratio') : 
                   headRatio >= 7 ? (currentLang === 'ko' ? '이상적인 비율' : 'Ideal Ratio') : (currentLang === 'ko' ? '안정적인 비율' : 'Stable Ratio');

  // Leg golden ratio
  const legTotal = uLeg + lLeg;
  const legRatio = !isNaN(legTotal) ? (legTotal / h).toFixed(2) : '-';
  const legDesc = legRatio >= 0.5 ? (currentLang === 'ko' ? '서구형 롱다리' : 'Long Leg Type') : (currentLang === 'ko' ? '균형 잡힌 다리' : 'Balanced Leg');

  // Upper/Lower Balance
  const balance = (!isNaN(shoulder) && !isNaN(hip)) ? (shoulder * 2 / hip).toFixed(2) : '-';
  const balanceDesc = balance >= 1.1 ? (currentLang === 'ko' ? '상체 강조형' : 'Upper Emphasis') : 
                      balance <= 0.9 ? (currentLang === 'ko' ? '하체 강조형' : 'Lower Emphasis') : (currentLang === 'ko' ? '황금 밸런스' : 'Golden Balance');

  // Global Ranking (Simulated)
  const score = window._fitmeShareData ? window._fitmeShareData.score : 70;
  const percentile = Math.min(99, Math.round(score * 0.9 + 10));
  const grade = window._fitmeShareData ? window._fitmeShareData.grade : 'A';

  const emblemMap = {
    'S': t('emblem-s'), 'A+': t('emblem-ap'), 'A': t('emblem-a'),
    'B+': t('emblem-bp'), 'B': t('emblem-b'), 'C': t('emblem-c')
  };
  const emblem = emblemMap[grade] || emblemMap['B'];

  // Detailed Recommendations
  const itemsDB = {
    hourglass: [
      { name: 'Oversized Blazer', reason: currentLang === 'ko' ? '어깨와 골반의 조화를 강조하면서 허리 라인을 자연스럽게 살려줍니다.' : 'Emphasizes the harmony of shoulders and hips while naturally defining the waist.' },
      { name: 'High-Rise Flare Jeans', reason: currentLang === 'ko' ? '다리가 길어 보이고 모래시계형 실루엣을 극대화합니다.' : 'Makes legs look longer and maximizes the hourglass silhouette.' }
    ],
    pear: [
      { name: 'Crop Biker Jacket', reason: currentLang === 'ko' ? '상체에 볼륨을 더해 하체와의 균형을 맞춰줍니다.' : 'Adds volume to the upper body to balance with the lower body.' },
      { name: 'A-Line Midi Skirt', reason: currentLang === 'ko' ? '하체의 곡선을 부드럽게 감싸주어 체형을 보완합니다.' : 'Softly wraps around lower body curves to complement the shape.' }
    ],
    inv: [
      { name: 'V-Neck Wide Leg Jumpsuit', reason: currentLang === 'ko' ? 'V넥으로 시선을 분산시키고 와이드 하의로 하체 볼륨을 채워줍니다.' : 'Distracts attention with a V-neck and fills lower body volume with wide legs.' },
      { name: 'Low-Rise Cargo Pants', reason: currentLang === 'ko' ? '골반 라인을 확장시켜 상하체 비율을 맞춥니다.' : 'Expands the hip line to balance upper and lower body proportions.' }
    ],
    rect: [
      { name: 'Belted Trench Coat', reason: currentLang === 'ko' ? '허리 벨트로 인위적인 곡선을 만들어 페미닌한 무드를 더합니다.' : 'Creates artificial curves with a waist belt for a feminine mood.' },
      { name: 'Pleated Mini Skirt', reason: currentLang === 'ko' ? '하체에 볼륨감을 주어 직선적인 체형을 보완합니다.' : 'Adds volume to the lower body to complement a straight build.' }
    ],
    apple: [
      { name: 'Empire Waist Dress', reason: currentLang === 'ko' ? '가장 슬림한 가슴 아래 라인을 강조하여 날씬해 보이게 합니다.' : 'Highlights the slim line below the chest to look thinner.' },
      { name: 'Straight Cut Trousers', reason: currentLang === 'ko' ? '다리 라인을 수직으로 뻗게 하여 전체적인 슬림 효과를 줍니다.' : 'Makes the leg line extend vertically for an overall slimming effect.' }
    ],
    default: [
      { name: 'Classic Leather Jacket', reason: currentLang === 'ko' ? '어떤 체형에도 안정적인 실루엣을 제공합니다.' : 'Provides a stable silhouette for any body type.' },
      { name: 'Ribbed Bodysuit', reason: currentLang === 'ko' ? '신체 실루엣을 그대로 드러내어 장점을 강조합니다.' : 'Reveals the body silhouette to highlight your strengths.' }
    ]
  };

  const recommendedItems = itemsDB[bodyType] || itemsDB.default;

  // HTML Rendering
  const container = document.getElementById('advanced-analysis-section');
  if (!container) return;

  container.innerHTML = `
    <div class="adv-card">
      <div class="adv-header">
        <div class="adv-title">
          <span>${t('adv-report-title')}</span>
          <span class="adv-emblem-badge">${emblem}</span>
        </div>
        <div class="adv-identity">${t('adv-identity-' + bodyType)}</div>
      </div>

      <div class="adv-metrics-grid">
        <div class="adv-metric-item">
          <div class="adv-metric-label">${t('adv-head-label')}</div>
          <div class="adv-metric-val">${headRatio}</div>
          <div class="adv-metric-desc">${headDesc}</div>
        </div>
        <div class="adv-metric-item">
          <div class="adv-metric-label">${t('adv-leg-label')}</div>
          <div class="adv-metric-val">${legRatio}</div>
          <div class="adv-metric-desc">${legDesc}</div>
        </div>
        <div class="adv-metric-item">
          <div class="adv-metric-label">${t('adv-balance-label')}</div>
          <div class="adv-metric-val">${balance}</div>
          <div class="adv-metric-desc">${balanceDesc}</div>
        </div>
      </div>

      <div class="adv-ranking-box">
        <div class="adv-ranking-info">
          <div class="adv-ranking-label">${t('adv-ranking-label')}</div>
          <div class="adv-ranking-pct">TOP ${100 - percentile}%</div>
        </div>
        <div style="text-align: right;">
          <div style="font-size: 11px; color: var(--muted);">${t('emblem-label')}</div>
          <div style="font-size: 16px; color: var(--accent); font-weight: 700;">${emblem}</div>
        </div>
      </div>

      <div class="adv-recommend-title"><span>${t('adv-recommend-title')}</span></div>
      <div class="adv-item-list">
        ${recommendedItems.map(item => `
          <div class="adv-item-card">
            <div class="adv-item-info">
              <div class="adv-item-name">${item.name}</div>
              <div class="adv-item-reason">${item.reason}</div>
            </div>
            <a href="https://www.amazon.com/s?k=${encodeURIComponent(item.name)}" target="_blank" class="adv-shop-btn">${t('adv-shop-now')}</a>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

/**
 * Update SVG proportions based on measurements
 */
function updateVisuals() {
  const h = measurements['input-height'] || 180;
  
  // Head scaling (based on 8-head ratio standard)
  if (measurements['head-height']) {
    const headScale = (measurements['head-height'] / (h / 8));
    const headGroup = document.getElementById('svg-head');
    if (headGroup) headGroup.style.transform = `scale(${headScale})`;
  }

  // Arm scaling
  if (measurements['upper-arm-len']) {
    const armScale = (measurements['upper-arm-len'] / 30);
    ['svg-arm-l', 'svg-arm-r'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.style.transform = `scaleY(${armScale})`;
    });
  }

  // Leg scaling
  if (measurements['upper-leg-len'] || measurements['lower-leg-len']) {
    const uLeg = measurements['upper-leg-len'] || 42;
    const lLeg = measurements['lower-leg-len'] || 38;
    const totalLeg = uLeg + lLeg;
    const legScale = totalLeg / 80; // 80cm as base standard for 180cm height
    
    ['svg-leg-l-upper', 'svg-leg-l-lower', 'svg-leg-r-upper', 'svg-leg-r-lower'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.style.transform = `scaleY(${legScale})`;
    });
  }
}


/**
 * Share/Save Functions
 */
function shareResult() {
  const dummy = document.createElement('input');
  document.body.appendChild(dummy);
  dummy.value = window.location.href;
  dummy.select();
  document.execCommand('copy');
  document.body.removeChild(dummy);
  showToast(translations[currentLang]["toast-share-success"]);
}

function saveAsImage() {
  showToast(translations[currentLang]["toast-image-save"]);
}

/**
 * Reset All
 */
function resetAll() {
  if (!confirm('모든 데이터를 초기화하시겠습니까?')) return;
  measurements = {};
  localStorage.removeItem('fitme_measurements');
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('filled', 'active'));
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  document.querySelectorAll('.input-field').forEach(i => i.value = '');
  placeholder.style.display = 'flex';
  analysisCard.classList.remove('visible');
  
  // Reset SVG scaling
  document.querySelectorAll('g[id^="svg-"]').forEach(g => g.style.transform = "none");
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

// Initialization: Restore data if exists
window.onload = () => {
  if (Object.keys(measurements).length > 0) {
    Object.keys(measurements).forEach(key => {
      const el = document.getElementById(key);
      if (el) el.value = measurements[key];
    });
    updateVisuals();
  }
  setLanguage('ko');
};

/**
 * FITME Global Master Script (v1.5)
 * Handles measurements, unit conversion, and advanced analysis.
 */

// State - Use index.html's global state if available, or initialize
let currentLang = window.currentLang || 'en';
let currentUnit = (function() {
  const saved = localStorage.getItem('fitme_unit');
  if (saved) return saved;
  const nav = navigator.language || '';
  return (nav === 'en-US') ? 'imperial' : 'metric';
})();
let measurements = JSON.parse(localStorage.getItem('fitme_measurements')) || {};

/**
 * Helper to get translation from index.html's i18n object
 */
function t(key) {
  if (window.t) return window.t(key); // Use index.html's helper if available
  // Fallback
  return key;
}

/**
 * Auto-detect user's locale and units (v1.5)
 */
function initLocale() {
  const navLang = navigator.language || 'en-US';
  
  // Set Language (Only if not already set by index.html)
  if (!localStorage.getItem('fitme_lang')) {
    if (navLang.startsWith('ko')) currentLang = 'ko';
    else currentLang = 'en';
  } else {
    currentLang = localStorage.getItem('fitme_lang');
  }

  // Set Unit: USA defaults to Imperial
  if (!localStorage.getItem('fitme_unit')) {
    if (navLang === 'en-US') currentUnit = 'imperial';
    else currentUnit = 'metric';
  } else {
    currentUnit = localStorage.getItem('fitme_unit');
  }

  // Update UI (isInit = true to prevent double conversion)
  toggleUnit(currentUnit, true);
  if (window.setLanguage) window.setLanguage(currentLang);
}

/**
 * Unit conversion helper
 */
function toggleUnit(unit, isInit = false) {
  const oldUnit = currentUnit;
  currentUnit = unit;
  localStorage.setItem('fitme_unit', unit);
  
  // Convert existing values in inputs (Skip if initial load)
  if (!isInit && oldUnit !== unit) {
    document.querySelectorAll('.input-field').forEach(input => {
      const val = parseFloat(input.value);
      if (!isNaN(val)) {
        if (unit === 'imperial') { // cm -> in, kg -> lb
          if (input.id.includes('weight')) input.value = (val * 2.20462).toFixed(1);
          else if (input.id.includes('foot')) return;
          else input.value = (val / 2.54).toFixed(1);
        } else { // in -> cm, lb -> kg
          if (input.id.includes('weight')) input.value = (val / 2.20462).toFixed(1);
          else if (input.id.includes('foot')) return;
          else input.value = (val * 2.54).toFixed(1);
        }
      }
    });
  }

  // Update Toggle Buttons
  document.querySelectorAll('.unit-toggle-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.unit === unit);
  });
  
  // Refresh UI labels via index.html's applyTranslations
  if (window.currentUnit !== undefined) window.currentUnit = unit;
  if (window.applyTranslations) window.applyTranslations();
}

// UI Elements
const placeholder = document.getElementById('placeholder');
const analysisCard = document.getElementById('analysis-result');
const analysisText = document.getElementById('analysis-text');
const bmiText = document.getElementById('bmi-text');
const bestStyles = document.getElementById('best-styles');
const worstStyles = document.getElementById('worst-styles');

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
    shoulder: ['shoulder-width'],
    chest: ['chest-circ'],
    'upper-arm': ['upper-arm-len'],
    'lower-arm': ['lower-arm-len'],
    waist: ['waist-circ'],
    hip: ['hip-circ'],
    'upper-leg': ['upper-leg-len', 'upper-leg-circ'],
    'lower-leg': ['lower-leg-len'],
    foot: ['foot-size']
  };
  
  const fields = fieldMappings[part];
  let allValid = true;

  fields.forEach(fId => {
    const el = document.getElementById(fId);
    let val = el ? parseFloat(el.value) : null;
    if (isNaN(val)) {
      allValid = false;
    } else {
      // Internal storage always in METRIC
      if (currentUnit === 'imperial') {
        if (fId.includes('weight')) val = val / 2.20462;
        else if (fId.includes('foot')) { /* skip foot mm */ }
        else val = val * 2.54;
      }
      measurements[fId] = val;
    }
  });

  if (!allValid) {
    showToast(t('toast-enter-value'));
    return;
  }

  // Save to LocalStorage
  localStorage.setItem('fitme_measurements', JSON.stringify(measurements));

  const hs = document.getElementById('hs-' + part);
  if (hs) hs.classList.add('filled');
  
  updateVisuals();
  
  const parts = t('parts') || {};
  const partTitle = parts[part] || part;
  showToast(partTitle + t('toast-saved'));
}

/**
 * Advanced Analysis Upgrade (v1.4)
 */
function runAdvancedAnalysis() {
  // Use index.html's t() if possible
  const _t = (key) => t(key);
  
  const getVal = (p) => {
    return parseFloat(measurements[p] || 0);
  };

  const h = getVal('input-height'), 
        headH = getVal('head-height'),
        shoulder = getVal('shoulder-width'),
        hip = getVal('hip-circ'),
        uLeg = getVal('upper-leg-len'),
        lLeg = getVal('lower-leg-len'),
        waist = getVal('waist-circ');

  if (h <= 0) return;

  // 1. Identity & Metrics
  let bodyType = 'default';
  if (waist > 0 && hip > 0 && shoulder > 0) {
    const s = shoulder * 2;
    if (Math.abs(s - hip) < (hip * 0.05) && waist < (hip * 0.75)) bodyType = 'hourglass';
    else if (hip > (s * 1.05)) bodyType = 'pear';
    else if (s > (hip * 1.05)) bodyType = 'inv';
    else if (waist > (hip * 0.85)) bodyType = 'apple';
    else bodyType = 'rect';
  }

  // 8-head figure ratio
  const headRatio = headH > 0 ? (h / headH).toFixed(1) : '-';
  const headDesc = headRatio >= 8 ? (currentLang === 'ko' ? '환상적인 모델 비율' : 'Perfect Model Ratio') : 
                   headRatio >= 7 ? (currentLang === 'ko' ? '이상적인 비율' : 'Ideal Ratio') : (currentLang === 'ko' ? '안정적인 비율' : 'Stable Ratio');

  // Leg golden ratio
  const legTotal = uLeg + lLeg;
  const legRatio = legTotal > 0 ? (legTotal / h).toFixed(2) : '-';
  const legDesc = legRatio >= 0.5 ? (currentLang === 'ko' ? '서구형 롱다리' : 'Long Leg Type') : (currentLang === 'ko' ? '균형 잡힌 다리' : 'Balanced Leg');

  // Upper/Lower Balance
  const balance = (shoulder > 0 && hip > 0) ? (shoulder * 2 / hip).toFixed(2) : '-';
  const balanceDesc = balance >= 1.1 ? (currentLang === 'ko' ? '상체 강조형' : 'Upper Emphasis') : 
                      balance <= 0.9 ? (currentLang === 'ko' ? '하체 강조형' : 'Lower Emphasis') : (currentLang === 'ko' ? '황금 밸런스' : 'Golden Balance');

  // Global Ranking
  const shareData = window._fitmeShareData || { score: 70, grade: 'A' };
  const score = shareData.score;
  const percentile = Math.min(99, Math.round(score * 0.9 + 10));
  const grade = shareData.grade;

  const emblem = _t('emblem-' + (grade === 'A+' ? 'ap' : grade.toLowerCase())) || grade;

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
          <span>${_t('adv-report-title')}</span>
          <span class="adv-emblem-badge">${emblem}</span>
        </div>
        <div class="adv-identity">${_t('adv-identity-' + bodyType)}</div>
      </div>

      <div class="adv-metrics-grid">
        <div class="adv-metric-item">
          <div class="adv-metric-label">${_t('adv-head-label')}</div>
          <div class="adv-metric-val">${headRatio}</div>
          <div class="adv-metric-desc">${headDesc}</div>
        </div>
        <div class="adv-metric-item">
          <div class="adv-metric-label">${_t('adv-leg-label')}</div>
          <div class="adv-metric-val">${legRatio}</div>
          <div class="adv-metric-desc">${legDesc}</div>
        </div>
        <div class="adv-metric-item">
          <div class="adv-metric-label">${_t('adv-balance-label')}</div>
          <div class="adv-metric-val">${balance}</div>
          <div class="adv-metric-desc">${balanceDesc}</div>
        </div>
      </div>

      <div class="adv-ranking-box">
        <div class="adv-ranking-info">
          <div class="adv-ranking-label">${_t('adv-ranking-label')}</div>
          <div class="adv-ranking-pct">TOP ${100 - percentile}%</div>
        </div>
        <div style="text-align: right;">
          <div style="font-size: 11px; color: var(--muted);">${_t('emblem-label')}</div>
          <div style="font-size: 16px; color: var(--accent); font-weight: 700;">${emblem}</div>
        </div>
      </div>

      <div class="adv-recommend-title"><span>${_t('adv-recommend-title')}</span></div>
      <div class="adv-item-list">
        ${recommendedItems.map(item => `
          <div class="adv-item-card">
            <div class="adv-item-info">
              <div class="adv-item-name">${item.name}</div>
              <div class="adv-item-reason">${item.reason}</div>
            </div>
            <a href="https://www.amazon.com/s?k=${encodeURIComponent(item.name)}" target="_blank" class="adv-shop-btn">${_t('adv-shop-now')}</a>
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
  
  // Head scaling
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
    const legScale = totalLeg / 80;
    
    ['svg-leg-l-upper', 'svg-leg-l-lower', 'svg-leg-r-upper', 'svg-leg-r-lower'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.style.transform = `scaleY(${legScale})`;
    });
  }
}

/**
 * Toast and Reset
 */
function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

function resetAll() {
  if (!confirm(t('confirm-reset'))) return;
  measurements = {};
  localStorage.removeItem('fitme_measurements');
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('filled', 'active'));
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  document.querySelectorAll('.input-field').forEach(i => i.value = '');
  placeholder.style.display = 'flex';
  analysisCard.classList.remove('visible');
  document.querySelectorAll('g[id^="svg-"]').forEach(g => g.style.transform = "none");
  showToast(t('toast-reset'));
}

/**
 * SNS Functions
 */
function copyLink() {
  navigator.clipboard.writeText(window.location.href).then(() => showToast(t('toast-link')));
}

// Initialization: Restore data if exists
window.onload = () => {
  initLocale();
  if (Object.keys(measurements).length > 0) {
    Object.keys(measurements).forEach(key => {
      const el = document.getElementById(key);
      if (el) {
        let val = measurements[key];
        // Display conversion if imperial
        if (currentUnit === 'imperial') {
          if (key.includes('weight')) val = (val * 2.20462).toFixed(1);
          else if (key.includes('foot')) { /* skip */ }
          else val = (val / 2.54).toFixed(1);
        }
        el.value = val;
      }
    });
    updateVisuals();
  }
};

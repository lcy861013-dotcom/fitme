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
 * Personalized recommendations: body type × leg ratio × shoulder balance × arm ratio (v2.0)
 */
function getPersonalizedItems(bodyType, legRatio, balance, armRatio, headRatio, ko) {
  const items = [];
  const fmt2 = (n) => n !== null ? n.toFixed(2) : '?';
  const fmt1 = (n) => n !== null ? n.toFixed(1) : '?';

  // ── BOTTOMS: body type × leg ratio ──────────────────────────────────
  const legLong  = legRatio !== null && legRatio >= 0.50;
  const legShort = legRatio !== null && legRatio < 0.46;

  const bottomMap = {
    inv: {
      long:  { name: ko ? '와이드 카고 팬츠'             : 'Wide Leg Cargo Pants',
               reason: ko ? `다리 비율 ${fmt2(legRatio)} 롱다리를 살리면서 하체 볼륨을 채워 넓은 어깨와 균형을 맞춥니다.`
                          : `Leg ratio ${fmt2(legRatio)} (long legs) — wide legs fill lower body to balance broad shoulders.` },
      short: { name: ko ? '하이웨이스트 플리츠 스커트'   : 'High-Waist Pleated Skirt',
               reason: ko ? `다리 비율 ${fmt2(legRatio)}에서 하이웨이스트가 시각적으로 다리를 늘리고 하체에 볼륨을 더합니다.`
                          : `Leg ratio ${fmt2(legRatio)} — high waist visually lengthens legs and adds needed lower body volume.` },
      mid:   { name: ko ? '로우라이즈 와이드 팬츠'        : 'Low-Rise Wide Leg Pants',
               reason: ko ? `하체 실루엣을 풍성하게 만들어 넓은 어깨와의 비율을 자연스럽게 맞춥니다.`
                          : `Fuller lower silhouette naturally counterbalances broad shoulders.` }
    },
    pear: {
      long:  { name: ko ? '스트레이트 컷 데님'            : 'Straight Cut Denim',
               reason: ko ? `다리 비율 ${fmt2(legRatio)} 긴 다리를 스트레이트 핏으로 깔끔하게 살려줍니다.`
                          : `Leg ratio ${fmt2(legRatio)} (long legs) — straight cut lets your length shine.` },
      short: { name: ko ? '하이웨이스트 미디 팬츠'        : 'High-Waist Midi Pants',
               reason: ko ? `다리 비율 ${fmt2(legRatio)}에서 허리선을 올려 다리를 길어 보이게 합니다.`
                          : `Leg ratio ${fmt2(legRatio)} — raised waist line visually elongates your legs.` },
      mid:   { name: ko ? 'A라인 미디 스커트'             : 'A-Line Midi Skirt',
               reason: ko ? `하체 곡선을 부드럽게 감싸 자연스러운 실루엣을 만들어줍니다.`
                          : `Softly wraps lower body curves for a natural silhouette.` }
    },
    hourglass: {
      long:  { name: ko ? '하이라이즈 플레어 진'          : 'High-Rise Flare Jeans',
               reason: ko ? `다리 비율 ${fmt2(legRatio)} 롱다리에 플레어 라인이 더해져 모래시계 실루엣이 완성됩니다.`
                          : `Leg ratio ${fmt2(legRatio)} (long legs) + flare = perfect hourglass silhouette.` },
      short: { name: ko ? '벨티드 미디 랩 스커트'         : 'Belted Midi Wrap Skirt',
               reason: ko ? `다리 비율 ${fmt2(legRatio)}에서 미디 기장이 균형을 잡고 벨트가 허리를 강조합니다.`
                          : `Leg ratio ${fmt2(legRatio)} — midi length balances proportions while the belt highlights your waist.` },
      mid:   { name: ko ? '테일러드 와이드 슬랙스'        : 'Tailored Wide Slacks',
               reason: ko ? `균형 잡힌 비율을 살려주는 클래식한 선택입니다.`
                          : `A classic choice that honors your balanced silhouette.` }
    },
    rect: {
      long:  { name: ko ? '벨트 와이드 트라우저'          : 'Wide Leg Trousers + Belt',
               reason: ko ? `다리 비율 ${fmt2(legRatio)} 긴 다리와 벨트 조합으로 허리 라인을 만들어 직선 체형을 보완합니다.`
                          : `Leg ratio ${fmt2(legRatio)} (long legs) + belt creates the waist definition your frame needs.` },
      short: { name: ko ? '주름 미니스커트'               : 'Pleated Mini Skirt',
               reason: ko ? `다리 비율 ${fmt2(legRatio)}에서 미니 기장이 다리를 길어 보이게 하며 하체에 볼륨감을 줍니다.`
                          : `Leg ratio ${fmt2(legRatio)} — mini length creates a longer-leg illusion and adds lower body volume.` },
      mid:   { name: ko ? '크롭 재킷 + 하이웨이스트 팬츠' : 'Cropped Jacket + High-Waist Pants',
               reason: ko ? `허리 라인을 강조해 직선 체형에 곡선미를 더합니다.`
                          : `Emphasizes the waist to bring curves to a straight frame.` }
    },
    apple: {
      long:  { name: ko ? '스트레이트 컷 트라우저'        : 'Straight Cut Trousers',
               reason: ko ? `다리 비율 ${fmt2(legRatio)} 다리를 수직으로 뻗게 해 복부에서 시선을 분산시킵니다.`
                          : `Leg ratio ${fmt2(legRatio)} — vertical leg line draws attention away from the midsection.` },
      short: { name: ko ? '하이웨이스트 스트레이트 팬츠'  : 'High-Waist Straight Pants',
               reason: ko ? `다리 비율 ${fmt2(legRatio)}에서 하이웨이스트가 다리를 시각적으로 늘리고 복부 라인을 정리합니다.`
                          : `Leg ratio ${fmt2(legRatio)} — high waist visually lengthens legs and smooths the midsection.` },
      mid:   { name: ko ? '플로우 미디 스커트'            : 'Flowy Midi Skirt',
               reason: ko ? `자연스럽게 흘러내리는 실루엣이 복부 라인을 부드럽게 감춰줍니다.`
                          : `Flowing silhouette gently skims the midsection.` }
    },
    default: {
      long:  { name: ko ? '스트레이트 데님'               : 'Straight Denim',
               reason: ko ? `롱다리를 살리는 깔끔한 기본 아이템입니다.`
                          : `A clean basic that lets long legs shine.` },
      short: { name: ko ? '하이웨이스트 스키니'           : 'High-Waist Skinny Jeans',
               reason: ko ? `하이웨이스트로 다리 라인을 최대한 활용합니다.`
                          : `High waist maximizes the leg line.` },
      mid:   { name: ko ? '클래식 스트레이트 진'          : 'Classic Straight Jeans',
               reason: ko ? `어떤 체형에도 안정적인 실루엣을 제공합니다.`
                          : `Provides a reliable silhouette for any body type.` }
    }
  };

  const bt = bottomMap[bodyType] || bottomMap.default;
  items.push(legLong ? bt.long : legShort ? bt.short : bt.mid);

  // ── TOPS: shoulder-hip balance × body type ───────────────────────────
  const shoulderWide   = balance !== null && balance >= 1.1;
  const shoulderNarrow = balance !== null && balance <= 0.9;

  if (shoulderWide) {
    if (bodyType === 'inv') {
      items.push({
        name: ko ? 'V넥 드롭숄더 니트' : 'V-Neck Drop Shoulder Knit',
        reason: ko ? `어깨-골반 비율 ${fmt2(balance)}로 어깨가 넓습니다. V넥이 시선을 아래로 유도하고 드롭숄더가 어깨 너비를 부드럽게 줄여줍니다.`
                   : `Shoulder-hip ratio ${fmt2(balance)} — broad shoulders. V-neck draws eye down; drop shoulder softens the width.`
      });
    } else {
      items.push({
        name: ko ? '오프숄더 탑' : 'Off-Shoulder Top',
        reason: ko ? `어깨-골반 비율 ${fmt2(balance)}의 넓은 어깨를 당당하게 활용해 자신감 있는 실루엣을 만듭니다.`
                   : `Shoulder-hip ratio ${fmt2(balance)} — turn wide shoulders into a confident statement.`
      });
    }
  } else if (shoulderNarrow) {
    items.push({
      name: ko ? '보트넥 퍼프슬리브 탑' : 'Boat Neck Puff Sleeve Top',
      reason: ko ? `어깨-골반 비율 ${fmt2(balance)}로 어깨가 좁은 편입니다. 보트넥과 퍼프 슬리브가 어깨에 볼륨을 더해 비율을 균형 있게 만듭니다.`
                 : `Shoulder-hip ratio ${fmt2(balance)} — narrower shoulders. Boat neck + puff sleeve adds volume and improves balance.`
    });
  } else {
    const topByType = {
      hourglass: { name: ko ? '오버사이즈 블레이저'      : 'Oversized Blazer',
                   reason: ko ? `어깨-골반 비율 ${fmt2(balance)} 황금 밸런스. 블레이저가 허리 라인을 자연스럽게 드러냅니다.`
                              : `Golden shoulder-hip ratio ${fmt2(balance)} — an oversized blazer naturally reveals your waist.` },
      pear:      { name: ko ? '크롭 바이커 재킷'         : 'Crop Biker Jacket',
                   reason: ko ? `어깨-골반 비율 ${fmt2(balance)}에서 크롭 재킷이 상체에 포인트를 주어 상하체 균형을 맞춥니다.`
                              : `At ratio ${fmt2(balance)}, a crop jacket puts focus on the upper body for better balance.` },
      inv:       { name: ko ? 'V넥 와이드레그 점프수트'  : 'V-Neck Wide Leg Jumpsuit',
                   reason: ko ? `V넥으로 시선을 분산시키고 와이드 하의로 하체 볼륨을 채워 비율을 완성합니다.`
                              : `V-neck distributes attention while wide legs fill lower body volume.` },
      rect:      { name: ko ? '벨티드 트렌치코트'        : 'Belted Trench Coat',
                   reason: ko ? `허리 벨트로 인위적인 곡선을 만들어 직선 체형에 페미닌한 무드를 더합니다.`
                              : `Waist belt creates curves, adding feminine mood to a straight frame.` },
      apple:     { name: ko ? '엠파이어 웨이스트 드레스' : 'Empire Waist Dress',
                   reason: ko ? `가슴 아래 가장 슬림한 라인을 강조하여 자연스럽게 날씬해 보이게 합니다.`
                              : `Highlights the slimmest point below the chest for a naturally slimming look.` },
      default:   { name: ko ? '리브드 바디수트'          : 'Ribbed Bodysuit',
                   reason: ko ? `신체 실루엣을 그대로 드러내어 장점을 강조합니다.`
                              : `Reveals your natural silhouette to highlight your strengths.` }
    };
    items.push(topByType[bodyType] || topByType.default);
  }

  // ── BONUS: arm length tip ─────────────────────────────────────────────
  if (armRatio !== null) {
    if (armRatio < 0.30) {
      items.push({
        name: ko ? '7부 소매 재킷' : '3/4 Sleeve Jacket',
        reason: ko ? `팔 비율 ${fmt2(armRatio)}로 팔이 짧은 편입니다. 7부 소매가 손목을 노출시켜 팔을 시각적으로 길어 보이게 합니다.`
                   : `Arm ratio ${fmt2(armRatio)} (shorter arms) — a 3/4 sleeve exposes the wrist and visually lengthens the arm.`
      });
    } else if (armRatio > 0.36) {
      items.push({
        name: ko ? '오버사이즈 롤업 셔츠' : 'Oversized Roll-Up Shirt',
        reason: ko ? `팔 비율 ${fmt2(armRatio)}로 팔이 긴 편입니다. 소매를 롤업하면 긴 팔의 장점을 자연스럽게 살릴 수 있습니다.`
                   : `Arm ratio ${fmt2(armRatio)} (longer arms) — rolling up sleeves leans into the length effortlessly.`
      });
    }
  }

  // ── BONUS: model proportions tip ────────────────────────────────────
  if (headRatio !== null && headRatio >= 8) {
    items.push({
      name: ko ? '심플 골드 체인 목걸이' : 'Minimal Gold Chain Necklace',
      reason: ko ? `두신비율 ${fmt1(headRatio)}등신의 모델 비율입니다. 심플한 액세서리 하나로도 완성도 높은 룩이 연출됩니다.`
                 : `Head ratio ${fmt1(headRatio)} — model-level proportions. A single minimal accessory completes the look effortlessly.`
    });
  }

  return items;
}

/**
 * Advanced Analysis (v2.0)
 */
function runAdvancedAnalysis() {
  const _t = (key) => t(key);
  const ko = currentLang === 'ko';

  const getVal = (p) => parseFloat(measurements[p] || 0);

  const h        = getVal('input-height'),
        headH    = getVal('head-height'),
        shoulder = getVal('shoulder-width'),
        hip      = getVal('hip-circ'),
        uLeg     = getVal('upper-leg-len'),
        lLeg     = getVal('lower-leg-len'),
        waist    = getVal('waist-circ'),
        uArm     = getVal('upper-arm-len'),
        lArm     = getVal('lower-arm-len');

  if (h <= 0) return;

  // Body Type
  let bodyType = 'default';
  if (waist > 0 && hip > 0 && shoulder > 0) {
    const s = shoulder * 2;
    if (Math.abs(s - hip) < (hip * 0.05) && waist < (hip * 0.75)) bodyType = 'hourglass';
    else if (hip > (s * 1.05))     bodyType = 'pear';
    else if (s > (hip * 1.05))     bodyType = 'inv';
    else if (waist > (hip * 0.85)) bodyType = 'apple';
    else bodyType = 'rect';
  }

  // Metrics (number for logic, string for display)
  const headRatioNum = headH > 0 ? h / headH : null;
  const headRatio    = headRatioNum !== null ? headRatioNum.toFixed(1) : '-';
  const headDesc     = headRatioNum >= 8 ? (ko ? '환상적인 모델 비율' : 'Perfect Model Ratio')
                     : headRatioNum >= 7 ? (ko ? '이상적인 비율'      : 'Ideal Ratio')
                     :                     (ko ? '안정적인 비율'      : 'Stable Ratio');

  const legTotal    = uLeg + lLeg;
  const legRatioNum = legTotal > 0 ? legTotal / h : null;
  const legRatio    = legRatioNum !== null ? legRatioNum.toFixed(2) : '-';
  const legDesc     = legRatioNum >= 0.5 ? (ko ? '서구형 롱다리' : 'Long Leg Type')
                                         : (ko ? '균형 잡힌 다리' : 'Balanced Leg');

  const balanceNum  = (shoulder > 0 && hip > 0) ? shoulder * 2 / hip : null;
  const balance     = balanceNum !== null ? balanceNum.toFixed(2) : '-';
  const balanceDesc = balanceNum >= 1.1 ? (ko ? '상체 강조형' : 'Upper Emphasis')
                    : balanceNum <= 0.9  ? (ko ? '하체 강조형' : 'Lower Emphasis')
                    :                      (ko ? '황금 밸런스' : 'Golden Balance');

  const armTotal    = uArm + lArm;
  const armRatioNum = armTotal > 0 ? armTotal / h : null;

  // Grade
  const shareData  = window._fitmeShareData || { score: 70, grade: 'A' };
  const score      = shareData.score;
  const percentile = Math.min(99, Math.round(score * 0.9 + 10));
  const grade      = shareData.grade;
  const emblem     = _t('emblem-' + (grade === 'A+' ? 'ap' : grade.toLowerCase())) || grade;

  // Personalized Recommendations
  const recommendedItems = getPersonalizedItems(bodyType, legRatioNum, balanceNum, armRatioNum, headRatioNum, ko);

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

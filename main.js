// State
const measurements = {};
const partNames = {
  height: '키',
  head: '머리',
  shoulder: '어깨',
  chest: '가슴',
  arm: '팔',
  waist: '허리',
  hip: '골반',
  thigh: '정강이',
  knee: '허벅지',
  foot: '발'
};

// UI Elements
const placeholder = document.getElementById('placeholder');
const analysisCard = document.getElementById('analysis-result');
const analysisText = document.getElementById('analysis-text');

/**
 * Select a body part to show its input form
 */
function selectPart(part) {
  // Hide all forms and placeholder
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  placeholder.style.display = 'none';

  // Show selected form
  const form = document.getElementById('form-' + part);
  if (form) form.classList.add('visible');

  // Update hotspot active state
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('active'));
  document.getElementById('hs-' + part).classList.add('active');
}

/**
 * Save measurement for a specific part
 */
function savePart(part) {
  let val = '';
  
  if (part === 'height') val = document.getElementById('input-height').value;
  else if (part === 'head') val = document.getElementById('head-circ').value;
  else if (part === 'shoulder') val = document.getElementById('shoulder-width').value;
  else if (part === 'chest') val = document.getElementById('chest-circ').value;
  else if (part === 'arm') val = document.getElementById('arm-len').value;
  else if (part === 'waist') val = document.getElementById('waist-circ').value;
  else if (part === 'hip') val = document.getElementById('hip-circ').value;
  else if (part === 'thigh') val = document.getElementById('thigh-len').value;
  else if (part === 'knee') val = document.getElementById('knee-len').value;
  else if (part === 'foot') val = document.getElementById('foot-size').value;

  if (!val) {
    showToast('값을 입력해주세요!');
    return;
  }

  measurements[part] = parseFloat(val);
  document.getElementById('hs-' + part).classList.add('filled');
  showToast(partNames[part] + ' 저장 완료 ✓');
}

/**
 * Run Expert Analysis based on height and leg length
 */
function runExpertAnalysis() {
  const height = measurements['height'];
  const legLower = measurements['thigh']; // Shin
  const legUpper = measurements['knee'];  // Thigh
  
  if (!height || !legLower || !legUpper) {
    showToast('분석을 위해 [키, 정강이, 허벅지] 값을 먼저 입력해주세요.');
    if (!height) selectPart('height');
    else if (!legLower) selectPart('thigh');
    else if (!legUpper) selectPart('knee');
    return;
  }

  const totalLeg = legLower + legUpper;
  const ratio = (totalLeg / height) * 100;
  
  let feedback = '';
  if (ratio > 49) {
    feedback = `전체 키(${height}cm) 대비 다리 길이(${totalLeg}cm)가 압도적으로 긴 **'서구형 롱다리 체형'**입니다. 상체가 짧아 보이며 어떤 옷을 입어도 비율이 돋보이는 모델 체형입니다.`;
  } else if (ratio > 46) {
    feedback = `키(${height}cm) 대비 다리 비율이 약 ${ratio.toFixed(1)}%로 매우 **'균형 잡힌 황금 비율'**을 가지고 계십니다. 대다수의 기성복이 잘 어울리는 표준 이상의 훌륭한 비율입니다.`;
  } else {
    feedback = `전체 키(${height}cm) 대비 상체가 발달한 **'안정적인 클래식 체형'**입니다. 하이웨이스트 팬츠나 짧은 아우터를 매치하면 다리가 더 길어 보이는 드라마틱한 스타일링이 가능합니다.`;
  }

  analysisText.innerHTML = feedback;
  analysisCard.classList.add('visible');
  showToast('신체 비율 분석이 완료되었습니다!');
  
  // Scroll to result
  analysisCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/**
 * Reset all data
 */
function resetAll() {
  if (!confirm('모든 데이터를 초기화할까요?')) return;
  Object.keys(measurements).forEach(key => delete measurements[key]);
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('filled', 'active'));
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  placeholder.style.display = 'flex';
  analysisCard.classList.remove('visible');
  showToast('초기화 완료');
}

/**
 * Show Toast Message
 */
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

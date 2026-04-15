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
    "form-title-neck": "NECK / 목",
    "form-title-shoulder": "SHOULDER / 어깨",
    "form-title-chest": "CHEST / 가슴",
    "form-title-upper-arm": "UPPER ARM / 상완",
    "form-title-lower-arm": "LOWER ARM / 하완",
    "form-title-waist": "WAIST / 허리",
    "form-title-hip": "HIP / 골반",
    "form-title-upper-leg": "THIGH / 대퇴",
    "form-title-lower-leg": "SHIN / 하퇴",
    "form-title-foot": "FOOT / 발",
    "label-circ": "둘레 (cm)",
    "label-width": "너비 (cm)",
    "label-len": "길이 (cm)",
    "label-size": "사이즈 (mm)",
    "label-head-height": "세로 길이 (cm)",
    "form-desc-upper-arm": "어깨뼈에서 팔꿈치 중간까지의 길이입니다.",
    "form-desc-lower-arm": "팔꿈치 중간에서 손목뼈까지의 길이입니다.",
    "form-desc-upper-leg": "골반뼈 끝에서 무릎 중간까지의 길이입니다.",
    "form-desc-lower-leg": "무릎 중간에서 복숭아뼈까지의 길이입니다."
  },
  en: {
    "nav-guide": "Guide",
    "nav-analysis": "Analysis",
    "nav-about": "About",
    "guide-title": "Body Measurement Guide",
    "phone-guide-title": "📱 Phone Scale Method",
    "phone-guide-desc": "No measuring tape? Use your smartphone! A modern phone is about 15cm long. If a body part is 3 phones long, it's roughly 45cm.",
    "head-guide-title": "🧢 Head Size Tips",
    "head-guide-desc": "Use a <b>charging cable</b> for curves! Wrap it around your head, then measure its length with your phone (15cm).",
    "pro-guide-title": "📏 Professional Posture",
    "pro-guide-desc": "Stand straight before a mirror. Height and Weight are critical for accurate body balance and BMI analysis.",
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
    "form-desc-upper-arm": "Shoulder to mid-elbow.",
    "form-desc-lower-arm": "Mid-elbow to wrist.",
    "form-desc-upper-leg": "Hip to mid-knee.",
    "form-desc-lower-leg": "Mid-knee to ankle."
  },
  jp: {
    "nav-guide": "ガイド",
    "nav-analysis": "比率分析",
    "nav-about": "About",
    "guide-title": "身体測定ガイド",
    "phone-guide-title": "📱 スマホ活用測定法",
    "phone-guide-desc": "メジャーがありませんか？スマホを使ってみましょう！最新のスマホは約15cm입니다.",
    "head-guide-title": "🧢 頭囲測定のコツ",
    "head-guide-desc": "曲線には<b>充電ケーブル</b>を使用してください！ケーブル을頭に巻きつけ, スマホで測ります.",
    "pro-guide-title": "📏 推奨される測定姿勢",
    "pro-guide-desc": "鏡の前で正しい姿勢で測定してください. 身長と体重は核心データです.",
    "section-label": "部位をクリックして入力してください",
    "panel-title": "身体情報の入力",
    "panel-subtitle": "正確な分析のために数値を入力してください.",
    "placeholder-text": "左の人体図から<br>部位を選択してください",
    "form-title-height": "身長",
    "form-title-weight": "体重",
    "btn-save": "保存する",
    "btn-analyze": "🔥 専門家比率分析を実行",
    "btn-reset": "初期化",
    "analysis-report-title": "専門家分析レポート",
    "analysis-long-legs": "非常に脚が長い**「モデル体型」**です.",
    "analysis-balanced": "非常に**「バランスの取れた黄金比」**입니다.",
    "analysis-classic": "上半身が発達した**「安定した体型」**입니다.",
    "form-title-head": "頭部",
    "form-title-neck": "首",
    "form-title-shoulder": "肩",
    "form-title-chest": "胸部",
    "form-title-upper-arm": "上腕",
    "form-title-lower-arm": "下腕",
    "form-title-waist": "ウエスト",
    "form-title-hip": "ヒップ",
    "form-title-upper-leg": "大腿",
    "form-title-lower-leg": "下腿",
    "form-title-foot": "足",
    "label-circ": "周囲 (cm)",
    "label-width": "幅 (cm)",
    "label-len": "長さ (cm)",
    "label-size": "サイズ (mm)",
    "label-head-height": "垂直方向の高さ (cm)"
  },
  cn: {
    "nav-guide": "测量指南",
    "nav-analysis": "比例分析",
    "nav-about": "关于",
    "guide-title": "身体测量指南",
    "phone-guide-title": "📱 智能手机测量法",
    "phone-guide-desc": "没有皮尺？使用您的手机！手机长度约为15厘米。",
    "head-guide-title": "🧢 头围测量技巧",
    "head-guide-desc": "对于曲线, 请使用<b>充电线</b>！将线绕头一圈, 然后用手机测量。",
    "pro-guide-title": "📏 专家建议姿势",
    "pro-guide-desc": "请在镜子前保持正确姿势测量. 身高和体重是核心数据。",
    "section-label": "点击身体部位输入测量值",
    "panel-title": "输入身体信息",
    "panel-subtitle": "请输入数值以进行准确分析.",
    "placeholder-text": "请点击左侧<br>人体图的部位",
    "form-title-height": "身高",
    "form-title-weight": "体重",
    "btn-save": "保存",
    "btn-analyze": "🔥 运行专家比例分析",
    "btn-reset": "重置",
    "analysis-report-title": "专家分析报告",
    "analysis-long-legs": "您的腿部比例极高, 属于**“模特身材”**.",
    "analysis-balanced": "您的比例非常**“均衡, 接近黄金比例”**.",
    "analysis-classic": "您的上半身较为发达, 属于**“稳重经典体型”**.",
    "form-title-head": "头部",
    "form-title-neck": "颈部",
    "form-title-shoulder": "肩部",
    "form-title-chest": "胸部",
    "form-title-upper-arm": "上臂",
    "form-title-lower-arm": "前臂",
    "form-title-waist": "腰部",
    "form-title-hip": "臀部",
    "form-title-upper-leg": "大腿",
    "form-title-lower-leg": "小腿",
    "form-title-foot": "足部",
    "label-circ": "周长 (cm)",
    "label-width": "宽度 (cm)",
    "label-len": "长度 (cm)",
    "label-size": "尺码 (mm)",
    "label-head-height": "垂直高度 (cm)"
  }
};

// State
let currentLang = 'ko';
const measurements = {};

// UI Elements
const placeholder = document.getElementById('placeholder');
const analysisCard = document.getElementById('analysis-result');
const analysisText = document.getElementById('analysis-text');
const bmiText = document.getElementById('bmi-text');

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
    // 모바일 자동 스크롤 로직 추가
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

  const hs = document.getElementById('hs-' + part);
  if (hs) hs.classList.add('filled');
  
  const partTitle = translations[currentLang]["form-title-" + part] || part;
  showToast(partTitle + translations[currentLang]["toast-save-suffix"]);
}

/**
 * Run Expert Analysis
 */
function runExpertAnalysis() {
  const h = measurements['input-height'];
  const w = measurements['input-weight'];
  const lUpper = measurements['upper-leg-len'];
  const lLower = measurements['lower-leg-len'];
  
  if (!h || !w || !lUpper || !lLower) {
    showToast(translations[currentLang]["toast-analysis-req"]);
    return;
  }

  // 1. Leg Ratio Analysis
  const totalLeg = lUpper + lLower;
  const legRatio = (totalLeg / h) * 100;
  const shinRatio = (lLower / totalLeg) * 100; 
  
  let feedback = "";
  
  if (legRatio > 49) feedback = translations[currentLang]["analysis-long-legs"];
  else if (legRatio > 46) feedback = translations[currentLang]["analysis-balanced"];
  else feedback = translations[currentLang]["analysis-classic"];

  // 상세 분석 추가
  feedback += "<br><br><b style='color:var(--accent); font-size:16px;'>[상세 비율 분석]</b><br>";
  
  // 종아리 vs 허벅지
  if (shinRatio > 48) feedback += "• 전체 다리 길이 중 종아리가 길어 무릎 위치가 높습니다. 하이힐이나 스니커즈 등 어떤 신발도 잘 어울리는 **'슬림 하체'**입니다.<br>";
  else feedback += "• 허벅지가 탄탄하게 발달한 **'파워 하체'** 체형입니다. 테이퍼드 핏이나 와이드 팬츠로 스타일을 살릴 수 있습니다.<br>";

  // 팔 비율
  const aUpper = measurements['upper-arm-len'];
  const aLower = measurements['lower-arm-len'];
  if (aUpper && aLower) {
    const armTotal = aUpper + aLower;
    if (armTotal / h > 0.38) feedback += "• 키 대비 팔이 길어 상체가 시원해 보입니다. 오버사이즈 상의도 멋지게 소화 가능합니다.<br>";
  }

  // 머리 크기 및 등신 분석
  const headH = measurements['head-height'];
  if (headH) {
    const bodyCount = (h / headH).toFixed(1);
    feedback += `• 현재 고객님은 약 **${bodyCount}등신** 비율을 가지고 계십니다. `;
    if (bodyCount >= 8) feedback += "신이 내린 황금 비율입니다! ✨";
    else if (bodyCount >= 7) feedback += "표준보다 뛰어난 아주 훌륭한 비율입니다. 👍";
    feedback += "<br>";
  }

  // 목 두께
  const neckC = measurements['neck-circ'];
  if (neckC) {
    if (neckC > 40) feedback += "• 목이 건장하고 두꺼운 편입니다. 오픈 칼라 셔츠나 V넥 상의로 답답함을 해소하는 스타일링을 추천합니다.<br>";
  }

  // 2. BMI Analysis
  const bmi = w / ((h / 100) ** 2);
  let bmiStatus = '';
  if (bmi < 18.5) bmiStatus = translations[currentLang]["bmi-under"];
  else if (bmi < 25) bmiStatus = translations[currentLang]["bmi-normal"];
  else if (bmi < 30) bmiStatus = translations[currentLang]["bmi-over"];
  else bmiStatus = translations[currentLang]["bmi-obese"];

  analysisText.innerHTML = feedback;
  bmiText.innerHTML = `${bmiStatus}${bmi.toFixed(1)})`;
  analysisCard.classList.add('visible');
  analysisCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function resetAll() {
  if (!confirm('모든 데이터를 초기화하시겠습니까?')) return;
  Object.keys(measurements).forEach(k => delete measurements[k]);
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('filled', 'active'));
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  document.querySelectorAll('.input-field').forEach(i => i.value = '');
  placeholder.style.display = 'flex';
  analysisCard.classList.remove('visible');
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

// Init language
setLanguage('ko');

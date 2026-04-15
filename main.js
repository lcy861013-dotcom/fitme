// Translations Dictionary
const translations = {
  ko: {
    "nav-guide": "측정 가이드",
    "nav-analysis": "비율 분석",
    "nav-about": "About",
    "guide-title": "올바른 신체 치수 측정 가이드",
    "phone-guide-title": "📱 스마트폰 활용 측정법 (No Tape?)",
    "phone-guide-desc": "줄자가 없으신가요? 여러분의 스마트폰을 사용해 보세요! 최신 스마트폰의 평균 세로 길이는 약 15cm입니다. 예를 들어, 무릎에서 골반까지 스마트폰이 약 3번 들어간다면 해당 부위의 길이는 약 45cm로 추정할 수 있습니다.",
    "pro-guide-title": "📏 전문가 권장 측정 자세",
    "pro-guide-desc": "정확한 비율 분석을 위해 거울 앞에서 바른 자세로 서서 측정하세요. 특히 키(Height)와 체질량(Weight)은 신체 밸런스를 분석하는 핵심 데이터입니다.",
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
    "toast-analysis-req": "분석을 위해 [키, 체중, 정강이, 허벅지] 값을 먼저 입력해주세요.",
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
    "form-title-arm": "ARM / 팔",
    "form-title-waist": "WAIST / 허리",
    "form-title-hip": "HIP / 골반",
    "form-title-thigh": "SHIN / 정강이",
    "form-title-knee": "THIGH / 허벅지",
    "form-title-foot": "FOOT / 발",
    "label-circ": "둘레 (cm)",
    "label-width": "너비 (cm)",
    "label-len": "길이 (cm)",
    "label-size": "사이즈 (mm)"
  },
  en: {
    "nav-guide": "Guide",
    "nav-analysis": "Analysis",
    "nav-about": "About",
    "guide-title": "Body Measurement Guide",
    "phone-guide-title": "📱 Phone Scale Method (No Tape?)",
    "phone-guide-desc": "No measuring tape? Use your smartphone! A modern phone is about 15cm long. If a body part is 3 phones long, it's roughly 45cm.",
    "pro-guide-title": "📏 Professional Posture",
    "pro-guide-desc": "Stand straight before a mirror. Height and Weight are critical for accurate body balance and BMI analysis.",
    "section-label": "Click a body part to enter measurements",
    "panel-title": "Body Measurements",
    "panel-subtitle": "Please enter your data for analysis.",
    "placeholder-text": "Click a body part<br>on the left figure",
    "form-title-height": "TOTAL HEIGHT",
    "form-desc-height": "Height is the baseline for all proportions.",
    "form-title-weight": "WEIGHT",
    "form-desc-weight": "Required for body type and BMI analysis.",
    "label-height": "Height (cm)",
    "label-weight": "Weight (kg)",
    "btn-save": "Save",
    "btn-analyze": "🔥 Run Expert Analysis",
    "btn-reset": "Reset",
    "analysis-report-title": "Expert Analysis Report",
    "analysis-note": "*Results are statistical based on provided data.",
    "toast-save-suffix": " Saved ✓",
    "toast-input-req": "Please enter a value!",
    "toast-analysis-req": "Please enter [Height, Weight, Shin, Thigh] first.",
    "analysis-long-legs": "You have **'Model proportions'** with very long legs. Clothing will look exceptional on your frame.",
    "analysis-balanced": "Your body has a **'Golden Ratio'**. Very well-balanced proportions.",
    "analysis-classic": "You have an **'Stable Classic'** build. High-waisted styling is recommended.",
    "bmi-under": "Underweight (BMI: ",
    "bmi-normal": "Normal (BMI: ",
    "bmi-over": "Overweight (BMI: ",
    "bmi-obese": "Obese (BMI: ",
    "form-title-head": "HEAD",
    "form-title-shoulder": "SHOULDER",
    "form-title-chest": "CHEST",
    "form-title-arm": "ARM",
    "form-title-waist": "WAIST",
    "form-title-hip": "HIP",
    "form-title-thigh": "SHIN",
    "form-title-knee": "THIGH",
    "form-title-foot": "FOOT",
    "label-circ": "Circumference (cm)",
    "label-width": "Width (cm)",
    "label-len": "Length (cm)",
    "label-size": "Size (mm)"
  },
  jp: {
    "nav-guide": "ガイド",
    "nav-analysis": "比率分析",
    "nav-about": "About",
    "guide-title": "身体測定ガイド",
    "phone-guide-title": "📱 スマホ活用測定法",
    "phone-guide-desc": "メジャーがありませんか？スマホを使ってみましょう！最新のスマホは約15cmです。スマホ3台分なら約45cmと推測できます。",
    "pro-guide-title": "📏 推奨される測定姿勢",
    "pro-guide-desc": "鏡の前で正しい姿勢で測定してください。身長と体重は分析の核心データです。",
    "section-label": "部位をクリックして入力してください",
    "panel-title": "身体情報の入力",
    "panel-subtitle": "正確な分析のために数値を入力してください。",
    "placeholder-text": "左の人体図から<br>部位を選択してください",
    "form-title-height": "身長",
    "form-desc-height": "身長はすべての比率の基準となります。",
    "form-title-weight": "体重",
    "form-desc-weight": "体型とBMI分析のために必要です。",
    "label-height": "身長 (cm)",
    "label-weight": "体重 (kg)",
    "btn-save": "保存する",
    "btn-analyze": "🔥 専門家比率分析を実行",
    "btn-reset": "初期化",
    "analysis-report-title": "専門家分析レポート",
    "analysis-long-legs": "非常に脚が長い**「モデル体型」**です。どんな服も似合う素晴らしい比率です。",
    "analysis-balanced": "非常に**「バランスの取れた黄金比」**です。理想的なスタイルです。",
    "analysis-classic": "上半身が発達した**「安定した体型」**です。ハイウエストのスタイリングをお勧めします。",
    "bmi-under": "低体重 (BMI: ",
    "bmi-normal": "普通体重 (BMI: ",
    "bmi-over": "肥満(1度) (BMI: ",
    "bmi-obese": "肥満 (BMI: "
  },
  cn: {
    "nav-guide": "测量指南",
    "nav-analysis": "比例分析",
    "nav-about": "关于",
    "guide-title": "身体测量指南",
    "phone-guide-title": "📱 智能手机测量法",
    "phone-guide-desc": "没有皮尺？使用您的手机！手机长度约为15厘米。如果某个部位长3个手机，则约为45厘米。",
    "pro-guide-title": "📏 专家建议姿势",
    "pro-guide-desc": "请在镜子前保持正确姿势测量。身高和体重是分析的核心数据。",
    "section-label": "点击身体部位输入测量值",
    "panel-title": "输入身体信息",
    "panel-subtitle": "请输入数值以进行准确分析。",
    "placeholder-text": "请点击左侧<br>人体图的部位",
    "form-title-height": "身高",
    "form-title-weight": "体重",
    "label-height": "身高 (cm)",
    "label-weight": "体重 (kg)",
    "btn-save": "保存",
    "btn-analyze": "🔥 运行专家比例分析",
    "btn-reset": "重置",
    "analysis-long-legs": "您的腿部比例极高，属于**“模特身材”**。任何衣服都能穿出美感。",
    "analysis-balanced": "您的比例非常**“均衡，接近黄金比例”**。非常理想。",
    "analysis-classic": "您的上半身较为发达，属于**“稳重经典体型”**。建议尝试高腰搭配。"
  }
};

// State
let currentLang = 'ko';
const measurements = {};
const partNames = {
  height: 'height', weight: 'weight', head: 'head', shoulder: 'shoulder', chest: 'chest', 
  arm: 'arm', waist: 'waist', hip: 'hip', thigh: 'thigh', knee: 'knee', foot: 'foot'
};

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
    if (translations[lang][key]) {
      if (el.tagName === 'INPUT') el.placeholder = translations[lang][key];
      else el.innerHTML = translations[lang][key];
    }
  });
  // Update document lang
  document.documentElement.lang = lang;
}

/**
 * Select a body part to show its input form
 */
function selectPart(part) {
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
  placeholder.style.display = 'none';
  const form = document.getElementById('form-' + part);
  if (form) form.classList.add('visible');
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('active'));
  document.getElementById('hs-' + part).classList.add('active');
}

/**
 * Save measurement for a specific part
 */
function savePart(part) {
  let val = '';
  const fields = {
    height: 'input-height', weight: 'input-weight', head: 'head-circ', shoulder: 'shoulder-width',
    chest: 'chest-circ', arm: 'arm-len', waist: 'waist-circ', hip: 'hip-circ', 
    thigh: 'thigh-len', knee: 'knee-len', foot: 'foot-size'
  };
  
  val = document.getElementById(fields[part]).value;

  if (!val) {
    showToast(translations[currentLang]["toast-input-req"]);
    return;
  }

  measurements[part] = parseFloat(val);
  document.getElementById('hs-' + part).classList.add('filled');
  showToast((translations[currentLang]["form-title-" + part] || part) + translations[currentLang]["toast-save-suffix"]);
}

/**
 * Run Expert Analysis (Leg Ratio + BMI)
 */
function runExpertAnalysis() {
  const h = measurements['height'];
  const w = measurements['weight'];
  const lLower = measurements['thigh'];
  const lUpper = measurements['knee'];
  
  if (!h || !lLower || !lUpper || !w) {
    showToast(translations[currentLang]["toast-analysis-req"]);
    return;
  }

  // 1. Leg Ratio Analysis
  const totalLeg = lLower + lUpper;
  const ratio = (totalLeg / h) * 100;
  let feedback = '';
  if (ratio > 49) feedback = translations[currentLang]["analysis-long-legs"];
  else if (ratio > 46) feedback = translations[currentLang]["analysis-balanced"];
  else feedback = translations[currentLang]["analysis-classic"];

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
  if (!confirm('Reset all?')) return;
  Object.keys(measurements).forEach(k => delete measurements[k]);
  document.querySelectorAll('.hotspot').forEach(h => h.classList.remove('filled', 'active'));
  document.querySelectorAll('.measurement-form').forEach(f => f.classList.remove('visible'));
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

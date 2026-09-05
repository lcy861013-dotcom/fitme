/* FITME size checker — compares listed garment charts against saved body/reference
   numbers. Circumference fields double on flat charts; widths/lengths do not.
   Supports saving multiple candidate garments and sharing a result via URL hash. */
(function () {
  'use strict';

  var LANG = (document.documentElement.lang || 'en').slice(0, 2) === 'ko' ? 'ko' : 'en';
  var PROFILE_KEY = 'fitme_size_profile';
  var GARMENTS_KEY = 'fitme_size_garments';
  var MAX_SAVED = 6;

  var HALVED = { chest: true, waist: true, hip: true, thigh: true };

  var RULES = {
    top: {
      shoulder: { basis: 'body', key: 'shoulder', ranges: { slim: [-1, 0.5], regular: [-0.5, 1.5], oversize: [2, 6] } },
      chest: { basis: 'body', key: 'chest', ranges: { slim: [4, 9], regular: [8, 15], oversize: [14, 30] } },
      length: { basis: 'ref', key: 'topLength', ranges: { slim: [-2, 2], regular: [-2, 2], oversize: [0, 6] } },
      sleeve: { basis: 'ref', key: 'topSleeve', ranges: { slim: [-2, 2], regular: [-2, 2], oversize: [-1, 4] } }
    },
    pants: {
      waist: { basis: 'body', key: 'waist', ranges: { slim: [-1, 2], regular: [0, 3], relaxed: [1, 5] } },
      hip: { basis: 'body', key: 'hip', ranges: { slim: [2, 7], regular: [4, 10], relaxed: [6, 14] } },
      thigh: { basis: 'body', key: 'thigh', ranges: { slim: [3, 8], regular: [5, 12], relaxed: [8, 18] } },
      rise: { basis: 'ref', key: 'pantsRise', ranges: { slim: [-1.5, 1.5], regular: [-1.5, 1.5], relaxed: [-1, 2.5] } },
      inseam: { basis: 'ref', key: 'pantsInseam', ranges: { slim: [-2, 2], regular: [-2, 2], relaxed: [-2, 3] } }
    }
  };

  var TOP_FIELDS = ['shoulder', 'chest', 'length', 'sleeve'];
  var PANTS_FIELDS = ['waist', 'hip', 'thigh', 'rise', 'inseam'];
  var PROFILE_FIELDS = [
    'shoulder', 'chest', 'waist', 'hip', 'thigh',
    'topLength', 'topSleeve', 'pantsRise', 'pantsInseam'
  ];

  var STR = {
    ko: {
      labels: {
        shoulder: '어깨', chest: '가슴', length: '총장', sleeve: '소매',
        waist: '허리', hip: '엉덩이', thigh: '허벅지', rise: '밑위', inseam: '인심'
      },
      verdictGood: '적정', verdictTight: '끼임', verdictLoose: '헐렁', verdictShort: '짧음', verdictLong: '김',
      needProfile: '먼저 위에서 내 치수를 입력해 주세요.',
      needGarment: '상품 실측 숫자를 하나 이상 입력해 주세요.',
      noOverlap: '입력한 항목에 대응하는 내 치수가 없습니다. 위에서 해당 항목을 채워 주세요.',
      missingMine: '내 치수 없음',
      saved: '내 치수를 저장했습니다. 다음 방문에도 남아 있습니다.',
      cleared: '저장한 치수를 지웠습니다.',
      garmentSaved: '후보에 저장했습니다.',
      garmentLimit: '후보는 최대 6개까지입니다. 하나를 지운 뒤 다시 저장하세요.',
      needName: '후보 이름을 적어 주세요 (예: 브랜드 L호).',
      linkCopied: '결과 링크를 복사했습니다.',
      linkFailed: '복사에 실패했습니다. 주소창의 # 뒤 주소를 직접 복사하세요.',
      compareSaved: '저장한 후보 비교',
      emptySaved: '저장한 후보가 없습니다. 아래에서 숫자를 넣고 “후보로 저장”을 누르세요.',
      remove: '삭제',
      load: '불러오기',
      easeWord: '여유',
      diffWord: '차이',
      summaryPass: '입력한 항목이 모두 적정 범위입니다.',
      summaryWarn: '주의 항목이 있습니다 — 아래 설명을 보세요.',
      summaryFail: '실패 가능성이 높은 항목이 있습니다.',
      note: {
        shoulderTight: '어깨 솔기가 어깨뼈보다 안쪽에 앉습니다. 어깨는 수선이 가장 어려운 부위라 다른 사이즈나 다른 브랜드를 보는 편이 낫습니다.',
        shoulderGood: '어깨 솔기가 어깨뼈에 얹힙니다. 여기가 맞으면 가슴·기장은 수선으로 잡을 수 있습니다.',
        shoulderLoose: '어깨가 내려옵니다. 의도한 드롭숄더면 괜찮지만, 아니면 “박시”가 아니라 “처짐”으로 보입니다.',
        chestTight: '가슴 여유가 부족해 앞판이 당기거나 단추가 벌어질 수 있습니다.',
        chestGood: '가슴 여유가 적당합니다.',
        chestLoose: '가슴이 많이 남습니다. 오버핏 의도가 아니면 상체가 무거워 보입니다.',
        lengthShort: '기장이 평소 옷보다 짧습니다. 상의가 짧으면 허리선이 드러나 다리가 길어 보이는 쪽입니다.',
        lengthGood: '기장이 평소 옷과 비슷합니다.',
        lengthLong: '기장이 깁니다. 허벅지 중간까지 내려오면 다리 시작점이 아래로 밀려 짧아 보입니다.',
        sleeveShort: '소매가 짧습니다. 손목뼈보다 위로 올라오면 작아 보입니다.',
        sleeveGood: '소매 길이가 적당합니다.',
        sleeveLong: '소매가 깁니다. 어깨가 맞는다면 소매는 수선이 쉽습니다.',
        waistTight: '허리가 조입니다. 스트레치가 없으면 앉을 때 불편합니다.',
        waistGood: '허리 여유가 적당합니다.',
        waistLoose: '허리가 뜹니다. 벨트나 수선이 필요할 수 있습니다 — 엉덩이·허벅지가 맞으면 수선이 정답인 경우가 많습니다.',
        hipTight: '엉덩이가 끼어 앉을 때 뒤판이 팽팽해집니다.',
        hipGood: '엉덩이 여유가 적당합니다.',
        hipLoose: '엉덩이가 남습니다. 뒤판이 처져 보일 수 있습니다.',
        thighTight: '허벅지가 끼어 걷거나 앉을 때 앞판이 당깁니다. 사이즈를 올리기 전에 스트레이트·테이퍼드를 보세요.',
        thighGood: '허벅지 여유가 적당합니다.',
        thighLoose: '허벅지가 넉넉합니다. 와이드 의도면 괜찮습니다.',
        riseShort: '밑위가 짧습니다. 앉을 때 가랑이가 당기는 대표 신호입니다.',
        riseGood: '밑위가 평소 바지와 비슷합니다.',
        riseLong: '밑위가 깁니다. 하이라이즈 의도면 허리선이 올라가 다리가 길어 보입니다.',
        inseamShort: '기장이 짧습니다. 밑단이 발목 위로 뜨면 와이드일수록 더 티가 납니다.',
        inseamGood: '기장이 평소 바지와 비슷합니다.',
        inseamLong: '기장이 깁니다. 밑단이 접히며 두꺼워 보이기 전에 수선을 계산하세요.'
      },
      fitNames: { slim: '슬림하게', regular: '기본', oversize: '오버핏', relaxed: '넉넉하게' }
    },
    en: {
      labels: {
        shoulder: 'Shoulder', chest: 'Chest', length: 'Length', sleeve: 'Sleeve',
        waist: 'Waist', hip: 'Hip', thigh: 'Thigh', rise: 'Rise', inseam: 'Inseam'
      },
      verdictGood: 'Good', verdictTight: 'Tight', verdictLoose: 'Loose', verdictShort: 'Short', verdictLong: 'Long',
      needProfile: 'Enter your own measurements above first.',
      needGarment: 'Enter at least one number from the listing.',
      noOverlap: 'None of the fields you entered have one of your measurements to compare against. Fill those in above.',
      missingMine: 'no saved value',
      saved: 'Saved. Your measurements will still be here next visit.',
      cleared: 'Saved measurements cleared.',
      garmentSaved: 'Saved as a candidate.',
      garmentLimit: 'You can keep up to 6 candidates. Remove one, then save again.',
      needName: 'Name this candidate (e.g. Brand L).',
      linkCopied: 'Result link copied.',
      linkFailed: 'Copy failed — copy the #… part of the address bar instead.',
      compareSaved: 'Saved candidates',
      emptySaved: 'No saved candidates yet. Enter numbers below and tap “Save as candidate”.',
      remove: 'Remove',
      load: 'Load',
      easeWord: 'ease',
      diffWord: 'diff',
      summaryPass: 'Every field you entered is within range.',
      summaryWarn: 'Some fields need a second look — see the notes below.',
      summaryFail: 'At least one field is likely to fail.',
      note: {
        shoulderTight: 'The shoulder seam would sit inside your shoulder bone. Shoulders are the hardest thing to alter, so a different size or brand is usually the better call.',
        shoulderGood: 'The shoulder seam lands on the bone. Once this is right, chest and length can be tailored.',
        shoulderLoose: 'The seam drops off your shoulder. Fine if the drop is intentional; otherwise it reads slouchy rather than boxy.',
        chestTight: 'Not enough chest ease — expect pulling across the front or gaping between buttons.',
        chestGood: 'Chest ease is in a comfortable range.',
        chestLoose: 'A lot of spare room through the chest. Unless you want oversize, it makes the torso read heavier.',
        lengthShort: 'Shorter than the top you already wear. A shorter hem exposes the waistline, which lengthens the leg line.',
        lengthGood: 'Length is close to the top you already wear.',
        lengthLong: 'Longer than usual. A hem reaching mid-thigh pushes the apparent start of your leg downward.',
        sleeveShort: 'Sleeves run short. Landing above the wrist bone reads undersized.',
        sleeveGood: 'Sleeve length is about right.',
        sleeveLong: 'Sleeves run long. If the shoulder fits, sleeves are an easy alteration.',
        waistTight: 'The waist would grip. Without stretch this gets uncomfortable when you sit.',
        waistGood: 'Waist ease is in a comfortable range.',
        waistLoose: 'The waist would gape. Expect a belt or a tailor — and if hip and thigh fit, tailoring is usually the right answer.',
        hipTight: 'The seat would be tight and go taut when you sit down.',
        hipGood: 'Hip ease is in a comfortable range.',
        hipLoose: 'Spare room through the seat, which can look saggy at the back.',
        thighTight: 'The thigh would pull when you walk or sit. Look at straight or tapered cuts before sizing up.',
        thighGood: 'Thigh ease is in a comfortable range.',
        thighLoose: 'Generous through the thigh — fine if you want a wide leg.',
        riseShort: 'A shorter rise than you normally wear. This is the classic cause of crotch pull when sitting.',
        riseGood: 'Rise is close to the pants you already wear.',
        riseLong: 'A longer rise. If high-rise is the intent, it raises the waistline and lengthens the leg.',
        inseamShort: 'Shorter than usual. A hem floating above the ankle shows more on a wide leg.',
        inseamGood: 'Inseam is close to the pants you already wear.',
        inseamLong: 'Longer than usual. Budget for hemming before the extra length stacks at the ankle.'
      },
      fitNames: { slim: 'Slim', regular: 'Regular', oversize: 'Oversize', relaxed: 'Relaxed' }
    }
  };

  var S = STR[LANG];

  function $(id) { return document.getElementById(id); }

  function num(el) {
    if (!el) return NaN;
    var raw = String(el.value).trim().replace(',', '.');
    if (!raw) return NaN;
    var v = parseFloat(raw);
    return isFinite(v) ? v : NaN;
  }

  function round(v) { return Math.round(v * 10) / 10; }

  function toast(msg) {
    var el = $('sc-toast');
    if (!el) return;
    el.textContent = msg;
    el.hidden = false;
    clearTimeout(el._t);
    el._t = setTimeout(function () { el.hidden = true; }, 6000);
  }

  function showError(msg) {
    var el = $('sc-error');
    if (el) { el.textContent = msg; el.hidden = false; }
    toast(msg);
  }

  function clearError() {
    var el = $('sc-error');
    if (el) { el.textContent = ''; el.hidden = true; }
  }

  /* ---------- profile ---------- */

  function readProfileInputs() {
    var out = {};
    PROFILE_FIELDS.forEach(function (f) {
      var v = num($('me-' + f));
      if (!isNaN(v) && v > 0) out[f] = v;
    });
    return out;
  }

  function loadProfile() {
    try {
      var raw = localStorage.getItem(PROFILE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  function saveProfile() {
    var data = readProfileInputs();
    try { localStorage.setItem(PROFILE_KEY, JSON.stringify(data)); } catch (e) { /* ignore */ }
    toast(S.saved);
    return data;
  }

  function fillProfileInputs(data) {
    PROFILE_FIELDS.forEach(function (f) {
      var el = $('me-' + f);
      if (el && data[f] != null) el.value = data[f];
    });
  }

  function clearProfile() {
    try { localStorage.removeItem(PROFILE_KEY); } catch (e) { /* ignore */ }
    PROFILE_FIELDS.forEach(function (f) {
      var el = $('me-' + f);
      if (el) el.value = '';
    });
    toast(S.cleared);
  }

  /* ---------- garment options / inputs ---------- */

  function chartMode() {
    var checked = document.querySelector('input[name="sc-chart-unit"]:checked');
    return checked ? checked.value : 'flat';
  }

  function inInches() {
    var el = $('sc-inches');
    return !!(el && el.checked);
  }

  function fitIntent() {
    var el = $('sc-fit');
    return el ? el.value : 'regular';
  }

  function garmentType() {
    var checked = document.querySelector('input[name="sc-type"]:checked');
    return checked ? checked.value : 'top';
  }

  function setRadio(name, value) {
    document.querySelectorAll('input[name="' + name + '"]').forEach(function (el) {
      el.checked = el.value === value;
    });
  }

  function readGarmentInputs() {
    var type = garmentType();
    var fields = type === 'top' ? TOP_FIELDS : PANTS_FIELDS;
    var measures = {};
    fields.forEach(function (f) {
      var v = num($('g-' + f));
      if (!isNaN(v) && v > 0) measures[f] = v;
    });
    return {
      name: (($('sc-gname') && $('sc-gname').value) || '').trim(),
      type: type,
      chart: chartMode(),
      inches: inInches(),
      fit: fitIntent(),
      measures: measures
    };
  }

  function fillGarmentInputs(g) {
    if (!g) return;
    setRadio('sc-type', g.type || 'top');
    syncTypeFields();
    setRadio('sc-chart-unit', g.chart || 'flat');
    var inch = $('sc-inches');
    if (inch) inch.checked = !!g.inches;
    var fit = $('sc-fit');
    if (fit && g.fit) fit.value = g.fit;
    var name = $('sc-gname');
    if (name) name.value = g.name || '';
    var fields = (g.type === 'pants' ? PANTS_FIELDS : TOP_FIELDS).concat(
      g.type === 'pants' ? TOP_FIELDS : PANTS_FIELDS
    );
    fields.forEach(function (f) {
      var el = $('g-' + f);
      if (!el) return;
      el.value = (g.measures && g.measures[f] != null) ? g.measures[f] : '';
    });
  }

  function normalise(raw, field, opts) {
    var v = raw;
    if (opts.inches) v = v * 2.54;
    if (HALVED[field] && opts.chart === 'flat') v = v * 2;
    return v;
  }

  /* ---------- verdict engine ---------- */

  function classify(field, delta, range, basis) {
    var lo = range[0], hi = range[1];
    var lengthish = (basis === 'ref');
    if (delta < lo) {
      return {
        cls: delta < lo - 2 ? 'bad' : 'warn',
        label: lengthish ? S.verdictShort : S.verdictTight,
        note: S.note[field + (lengthish ? 'Short' : 'Tight')]
      };
    }
    if (delta > hi) {
      return {
        cls: delta > hi + 4 ? 'bad' : 'warn',
        label: lengthish ? S.verdictLong : S.verdictLoose,
        note: S.note[field + (lengthish ? 'Long' : 'Loose')]
      };
    }
    return { cls: 'good', label: S.verdictGood, note: S.note[field + 'Good'] };
  }

  function evaluate(profile, garment) {
    var rules = RULES[garment.type] || RULES.top;
    var fit = garment.fit || 'regular';
    var opts = { chart: garment.chart || 'flat', inches: !!garment.inches };
    var rows = [];
    var entered = 0;
    var compared = 0;
    var worst = 'good';

    Object.keys(rules).forEach(function (field) {
      var raw = garment.measures && garment.measures[field];
      if (raw == null || !(raw > 0)) return;
      entered++;
      var garmentCm = normalise(raw, field, opts);
      var rule = rules[field];
      var mine = profile[rule.key];

      if (mine == null) {
        rows.push({
          field: field, listed: raw, garment: garmentCm,
          mine: null, delta: null, cls: 'info', label: S.missingMine, note: ''
        });
        return;
      }

      var delta = garmentCm - mine;
      var range = rule.ranges[fit] || rule.ranges.regular;
      var verdict = classify(field, delta, range, rule.basis);
      compared++;
      if (verdict.cls === 'bad') worst = 'bad';
      else if (verdict.cls === 'warn' && worst !== 'bad') worst = 'warn';

      rows.push({
        field: field, listed: raw, garment: garmentCm, mine: mine,
        delta: delta, basis: rule.basis,
        cls: verdict.cls, label: verdict.label, note: verdict.note
      });
    });

    return { rows: rows, entered: entered, compared: compared, worst: worst };
  }

  function run() {
    clearError();
    var profile = readProfileInputs();
    var garment = readGarmentInputs();
    if (!Object.keys(profile).length) { showError(S.needProfile); return; }
    var result = evaluate(profile, garment);
    if (!result.entered) { showError(S.needGarment); return; }
    if (!result.compared) { showError(S.noOverlap); return; }
    renderSingle(result.rows, result.worst, garment.name);
    updateShareLink(profile, [garment]);
  }

  function renderSingle(rows, worst, title) {
    var panel = $('sc-result');
    var tbody = $('sc-result-body');
    var summary = $('sc-summary');
    var notes = $('sc-notes');
    var multi = $('sc-multi');
    if (!panel || !tbody) return;
    if (multi) { multi.innerHTML = ''; multi.hidden = true; }

    tbody.innerHTML = '';
    notes.innerHTML = '';

    rows.forEach(function (r) {
      var tr = document.createElement('tr');
      var label = S.labels[r.field];
      var converted = (r.garment !== r.listed)
        ? round(r.listed) + ' → ' + round(r.garment)
        : round(r.listed);
      var deltaTxt = '—';
      if (r.delta != null) {
        var word = r.basis === 'ref' ? S.diffWord : S.easeWord;
        deltaTxt = (r.delta >= 0 ? '+' : '') + round(r.delta) + ' cm ' + word;
      }
      tr.innerHTML =
        '<td><strong>' + label + '</strong></td>' +
        '<td>' + converted + '</td>' +
        '<td>' + (r.mine != null ? round(r.mine) : '—') + '</td>' +
        '<td>' + deltaTxt + '</td>' +
        '<td><span class="sc-badge sc-' + r.cls + '">' + r.label + '</span></td>';
      tbody.appendChild(tr);

      if (r.note) {
        var li = document.createElement('li');
        li.className = 'sc-note sc-note-' + r.cls;
        li.innerHTML = '<strong>' + label + '</strong> — ' + r.note;
        notes.appendChild(li);
      }
    });

    var head = worst === 'bad' ? S.summaryFail : (worst === 'warn' ? S.summaryWarn : S.summaryPass);
    if (title) head = title + ' — ' + head;
    summary.textContent = head;
    summary.className = 'sc-summary sc-' + worst;

    var tableWrap = tbody.closest('table');
    if (tableWrap) tableWrap.hidden = false;

    panel.hidden = false;
    panel.setAttribute('aria-hidden', 'false');
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  /* ---------- saved candidates ---------- */

  function loadGarments() {
    try {
      var raw = localStorage.getItem(GARMENTS_KEY);
      var list = raw ? JSON.parse(raw) : [];
      return Array.isArray(list) ? list : [];
    } catch (e) { return []; }
  }

  function saveGarments(list) {
    try { localStorage.setItem(GARMENTS_KEY, JSON.stringify(list)); } catch (e) { /* ignore */ }
  }

  function saveCandidate() {
    clearError();
    var g = readGarmentInputs();
    if (!g.name) { showError(S.needName); return; }
    if (!Object.keys(g.measures).length) { showError(S.needGarment); return; }
    var list = loadGarments();
    if (list.length >= MAX_SAVED) { showError(S.garmentLimit); return; }
    g.id = Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
    list.push(g);
    saveGarments(list);
    toast(S.garmentSaved);
    renderSavedList();
  }

  function removeCandidate(id) {
    var list = loadGarments().filter(function (g) { return g.id !== id; });
    saveGarments(list);
    renderSavedList();
  }

  function renderSavedList() {
    var box = $('sc-saved');
    if (!box) return;
    var list = loadGarments();
    box.innerHTML = '';
    if (!list.length) {
      box.innerHTML = '<p class="sc-muted">' + S.emptySaved + '</p>';
      return;
    }
    var ul = document.createElement('ul');
    ul.className = 'sc-saved-list';
    list.forEach(function (g) {
      var li = document.createElement('li');
      var bits = Object.keys(g.measures || {}).map(function (k) {
        return S.labels[k] + ' ' + g.measures[k];
      }).slice(0, 3).join(' · ');
      li.innerHTML =
        '<div><strong></strong><span class="sc-muted"></span></div>' +
        '<div class="sc-saved-actions"></div>';
      li.querySelector('strong').textContent = g.name;
      li.querySelector('.sc-muted').textContent = ' — ' + (g.type === 'pants' ? (LANG === 'ko' ? '바지' : 'Pants') : (LANG === 'ko' ? '상의' : 'Top')) + (bits ? ' · ' + bits : '');
      var actions = li.querySelector('.sc-saved-actions');
      var loadBtn = document.createElement('button');
      loadBtn.type = 'button';
      loadBtn.textContent = S.load;
      loadBtn.addEventListener('click', function () {
        fillGarmentInputs(g);
        run();
      });
      var delBtn = document.createElement('button');
      delBtn.type = 'button';
      delBtn.textContent = S.remove;
      delBtn.addEventListener('click', function () { removeCandidate(g.id); });
      actions.appendChild(loadBtn);
      actions.appendChild(delBtn);
      ul.appendChild(li);
    });
    box.appendChild(ul);

    if (list.length >= 2) {
      var cmp = document.createElement('button');
      cmp.type = 'button';
      cmp.className = 'primary';
      cmp.textContent = S.compareSaved;
      cmp.addEventListener('click', compareAllSaved);
      box.appendChild(cmp);
    }
  }

  function compareAllSaved() {
    clearError();
    var profile = readProfileInputs();
    if (!Object.keys(profile).length) { showError(S.needProfile); return; }
    var list = loadGarments();
    if (list.length < 2) { showError(S.emptySaved); return; }

    var panel = $('sc-result');
    var multi = $('sc-multi');
    var summary = $('sc-summary');
    var notes = $('sc-notes');
    var tbody = $('sc-result-body');
    if (!panel || !multi) return;

    if (tbody) {
      var table = tbody.closest('table');
      if (table) table.hidden = true;
    }
    if (notes) notes.innerHTML = '';

    multi.innerHTML = '';
    multi.hidden = false;
    var anyBad = false;
    var anyWarn = false;

    list.forEach(function (g) {
      var result = evaluate(profile, g);
      if (!result.compared) return;
      if (result.worst === 'bad') anyBad = true;
      else if (result.worst === 'warn') anyWarn = true;

      var card = document.createElement('div');
      card.className = 'sc-multi-card';
      var h = document.createElement('h3');
      h.textContent = g.name;
      card.appendChild(h);
      var badge = document.createElement('span');
      badge.className = 'sc-badge sc-' + result.worst;
      badge.textContent = result.worst === 'bad' ? S.summaryFail : (result.worst === 'warn' ? S.summaryWarn : S.summaryPass);
      card.appendChild(badge);

      var table = document.createElement('table');
      table.innerHTML = '<thead><tr><th>' + (LANG === 'ko' ? '항목' : 'Field') + '</th><th>' + (LANG === 'ko' ? '차이' : 'Diff') + '</th><th>' + (LANG === 'ko' ? '판정' : 'Verdict') + '</th></tr></thead>';
      var tb = document.createElement('tbody');
      result.rows.forEach(function (r) {
        if (r.delta == null) return;
        var tr = document.createElement('tr');
        var word = r.basis === 'ref' ? S.diffWord : S.easeWord;
        tr.innerHTML =
          '<td>' + S.labels[r.field] + '</td>' +
          '<td>' + (r.delta >= 0 ? '+' : '') + round(r.delta) + ' cm ' + word + '</td>' +
          '<td><span class="sc-badge sc-' + r.cls + '">' + r.label + '</span></td>';
        tb.appendChild(tr);
      });
      table.appendChild(tb);
      card.appendChild(table);
      multi.appendChild(card);
    });

    var worst = anyBad ? 'bad' : (anyWarn ? 'warn' : 'good');
    summary.textContent = S.compareSaved + ' — ' + (worst === 'bad' ? S.summaryFail : (worst === 'warn' ? S.summaryWarn : S.summaryPass));
    summary.className = 'sc-summary sc-' + worst;

    panel.hidden = false;
    panel.setAttribute('aria-hidden', 'false');
    updateShareLink(profile, list);
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  /* ---------- URL share ---------- */

  function encodeState(profile, garments) {
    var payload = { v: 1, p: profile, g: garments.map(function (g) {
      return {
        n: g.name, t: g.type, c: g.chart, i: g.inches ? 1 : 0, f: g.fit, m: g.measures
      };
    }) };
    try {
      return btoa(unescape(encodeURIComponent(JSON.stringify(payload))))
        .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    } catch (e) { return ''; }
  }

  function decodeState(hash) {
    if (!hash) return null;
    var raw = hash.replace(/^#?s=/, '');
    if (!raw) return null;
    try {
      var pad = raw.length % 4 === 0 ? '' : '===='.slice(raw.length % 4);
      var json = decodeURIComponent(escape(atob(raw.replace(/-/g, '+').replace(/_/g, '/') + pad)));
      var data = JSON.parse(json);
      if (!data || data.v !== 1) return null;
      return {
        profile: data.p || {},
        garments: (data.g || []).map(function (g) {
          return {
            name: g.n || '',
            type: g.t || 'top',
            chart: g.c || 'flat',
            inches: !!g.i,
            fit: g.f || 'regular',
            measures: g.m || {}
          };
        })
      };
    } catch (e) { return null; }
  }

  function updateShareLink(profile, garments) {
    var token = encodeState(profile, garments);
    if (!token) return;
    var url = location.origin + location.pathname + '#s=' + token;
    try { history.replaceState(null, '', '#s=' + token); } catch (e) { /* ignore */ }
    var out = $('sc-share-url');
    if (out) out.value = url;
  }

  function copyShareLink() {
    var out = $('sc-share-url');
    if (!out || !out.value) {
      var profile = readProfileInputs();
      var g = readGarmentInputs();
      updateShareLink(profile, [g]);
    }
    var text = out && out.value;
    if (!text) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { toast(S.linkCopied); }, function () { toast(S.linkFailed); });
    } else {
      out.select();
      try {
        document.execCommand('copy');
        toast(S.linkCopied);
      } catch (e) { toast(S.linkFailed); }
    }
  }

  function applySharedState() {
    var state = decodeState(location.hash);
    if (!state) return false;
    if (state.profile && Object.keys(state.profile).length) {
      fillProfileInputs(state.profile);
      try { localStorage.setItem(PROFILE_KEY, JSON.stringify(state.profile)); } catch (e) { /* ignore */ }
    }
    if (state.garments && state.garments.length) {
      if (state.garments.length === 1) {
        fillGarmentInputs(state.garments[0]);
        run();
      } else {
        fillGarmentInputs(state.garments[0]);
        var existing = loadGarments();
        if (!existing.length) {
          state.garments.forEach(function (g, i) {
            g.id = 'share' + i;
          });
          saveGarments(state.garments.slice(0, MAX_SAVED));
          renderSavedList();
          compareAllSaved();
        } else {
          run();
        }
      }
      return true;
    }
    return false;
  }

  /* ---------- wiring ---------- */

  function syncTypeFields() {
    var type = garmentType();
    document.querySelectorAll('[data-sc-group]').forEach(function (node) {
      node.hidden = node.getAttribute('data-sc-group') !== type;
    });
    var fitSel = $('sc-fit');
    if (!fitSel) return;
    var opts = type === 'top' ? ['slim', 'regular', 'oversize'] : ['slim', 'regular', 'relaxed'];
    var prev = fitSel.value;
    fitSel.innerHTML = '';
    opts.forEach(function (key) {
      var o = document.createElement('option');
      o.value = key;
      o.textContent = S.fitNames[key];
      fitSel.appendChild(o);
    });
    fitSel.value = opts.indexOf(prev) >= 0 ? prev : 'regular';
  }

  function init() {
    if (!$('sc-run')) return;
    fillProfileInputs(loadProfile());
    syncTypeFields();
    renderSavedList();

    $('sc-run').addEventListener('click', run);
    var saveBtn = $('sc-save');
    if (saveBtn) saveBtn.addEventListener('click', saveProfile);
    var clearBtn = $('sc-clear');
    if (clearBtn) clearBtn.addEventListener('click', clearProfile);
    var candBtn = $('sc-save-garment');
    if (candBtn) candBtn.addEventListener('click', saveCandidate);
    var shareBtn = $('sc-copy-link');
    if (shareBtn) shareBtn.addEventListener('click', copyShareLink);

    document.querySelectorAll('input[name="sc-type"]').forEach(function (el) {
      el.addEventListener('change', syncTypeFields);
    });

    document.querySelectorAll('#sc-garment input').forEach(function (el) {
      el.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter') { ev.preventDefault(); run(); }
      });
    });

    applySharedState();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

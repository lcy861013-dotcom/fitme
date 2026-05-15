(function () {
  var KEY = 'fitme_cookie_consent';
  var CLIENT_ID = 'ca-pub-6377720400458954';

  function ensureCss() {
    if (document.querySelector('link[data-fitme="ccss"]')) return;
    var l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = '/cookie-consent.css';
    l.setAttribute('data-fitme', 'ccss');
    document.head.appendChild(l);
  }

  function applyConsentGranted() {
    if (typeof gtag === 'function') {
      gtag('consent', 'update', {
        ad_storage: 'granted',
        ad_user_data: 'granted',
        ad_personalization: 'granted',
        analytics_storage: 'granted',
      });
    }
  }

  function loadAdSense() {
    if (document.querySelector('script[data-fitme="adsense"]')) return;
    if (
      document.querySelector(
        'script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]'
      )
    )
      return;
    var s = document.createElement('script');
    s.async = true;
    s.crossOrigin = 'anonymous';
    s.dataset.fitme = 'adsense';
    s.src =
      'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
      encodeURIComponent(CLIENT_ID);
    document.head.appendChild(s);
  }

  function loadClarity() {
    if (document.querySelector('script[data-fitme="clarity"]')) return;
    (function (c, l, a, r, i, t, y) {
      c[a] =
        c[a] ||
        function () {
          (c[a].q = c[a].q || []).push(arguments);
        };
      t = l.createElement(r);
      t.async = 1;
      t.dataset.fitme = 'clarity';
      t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0];
      y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', 'wk36ynf43e');
  }

  function setupCtaTracking() {
    if (window.__fitmeCtaTrackingBound) return;
    window.__fitmeCtaTrackingBound = true;
    document.addEventListener(
      'click',
      function (ev) {
        var el = ev.target && ev.target.closest ? ev.target.closest('a,button') : null;
        if (!el) return;

        var consent = '';
        try {
          consent = localStorage.getItem(KEY) || '';
        } catch (e) {}
        if (consent !== 'all') return;

        var track = false;
        var href = '';
        if (el.tagName === 'A') href = el.getAttribute('href') || '';

        if (el.id === 'btn-analyze' || el.id === 'btn-analyze-mobile') track = true;
        if (el.classList && (el.classList.contains('hero-btn') || el.classList.contains('cta-btn'))) track = true;
        if (!track && el.tagName === 'A' && (href === '/' || href === '/#analysis')) track = true;
        if (!track) return;

        var ctaId = el.id || (el.className || '').toString().split(' ')[0] || 'cta';
        var label = (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80);
        if (typeof window.fitmeGaEvent === 'function') {
          window.fitmeGaEvent('cta_click', {
            cta_id: ctaId,
            cta_label: label,
            target_url: href || '',
            page_path: location.pathname,
            page_title: document.title || '',
          });
        }
      },
      true
    );
  }

  function removeBanner() {
    var el = document.getElementById('fitme-cc-banner');
    if (el) el.remove();
  }

  function notifyCookieResolved() {
    try {
      document.dispatchEvent(new CustomEvent('fitme-cookie-resolved'));
    } catch (e) {}
  }

  window.fitmeAcceptAllCookies = function () {
    try {
      localStorage.setItem(KEY, 'all');
    } catch (e) {}
    applyConsentGranted();
    loadAdSense();
    loadClarity();
    if (typeof window.fitmeInitAdSlots === 'function') {
      window.fitmeInitAdSlots();
    }
    removeBanner();
    notifyCookieResolved();
  };

  window.fitmeRejectNonEssential = function () {
    try {
      localStorage.setItem(KEY, 'essential');
    } catch (e) {}
    if (typeof gtag === 'function') {
      gtag('consent', 'update', {
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied',
        analytics_storage: 'denied',
      });
    }
    removeBanner();
    notifyCookieResolved();
  };

  function bannerCopy() {
    var lang = 'en';
    try {
      lang = localStorage.getItem('fitme_lang') || '';
    } catch (e) {}
    if (!lang) {
      var nav = (navigator.language || '').slice(0, 2).toLowerCase();
      if (nav === 'ko') lang = 'ko';
      else if (nav === 'ja') lang = 'ja';
      else if (nav === 'zh') lang = 'zh';
      else lang = 'en';
    }
    var T = {
      ko: {
        lead:
          '<strong>쿠키·개인화 광고</strong> 서비스 운영 및 Google Analytics, Microsoft Clarity, <strong>Google AdSense 맞춤 광고</strong>를 위해 쿠키가 사용될 수 있습니다. 세부 내용은 <a href="/privacy.html">개인정보처리방침</a>을 확인하세요. Publisher ID(Public): <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
        sub:
          '<strong>Cookies</strong> Analytics and personalised ads (Google AdSense) may use cookies. See our <a href="/privacy.html">Privacy Policy</a>.',
        ok: '동의합니다 · Accept all',
        min: '필수만 (광고·분석 거부) · Essential only',
      },
      ja: {
        lead:
          '<strong>クッキー・パーソナライズ広告</strong> サイト運営のため、Google Analytics / Microsoft Clarity / <strong>Google AdSense</strong> に関連するクッキーを使用する場合があります。詳細は <a href="/privacy.html">プライバシーポリシー</a> をご確認ください。Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
        sub:
          '<strong>Cookies</strong> 分析およびパーソナライズ広告にクッキーを使用することがあります。<a href="/privacy.html">Privacy Policy</a> をご覧ください。',
        ok: '同意する · Accept all',
        min: '必須のみ · Essential only',
      },
      zh: {
        lead:
          '<strong>Cookie 与个性化广告</strong> 为运营本站及 Google Analytics、Microsoft Clarity、<strong>Google AdSense</strong> 定向广告，我们可能使用 Cookie。详情请阅读 <a href="/privacy.html">隐私政策</a>。Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
        sub:
          '<strong>Cookies</strong> 我们可能将 Cookie 用于分析与个性化广告。请参阅 <a href="/privacy.html">Privacy Policy</a>。',
        ok: '同意 · Accept all',
        min: '仅必要 · Essential only',
      },
      en: {
        lead:
          '<strong>Cookies & personalised ads</strong> We may use cookies for site operations, Google Analytics, Microsoft Clarity, and <strong>Google AdSense</strong>. See our <a href="/privacy.html">Privacy Policy</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
        sub:
          '<strong>Note</strong> Non-essential cookies load only if you accept below.',
        ok: 'Accept all',
        min: 'Essential only',
      },
    };
    var row = T[lang] || T.en;
    return {
      html:
        '<div class="fitme-cc-inner">' +
        '<p class="fitme-cc-msg">' +
        row.lead +
        '</p>' +
        '<p class="fitme-cc-msg fitme-cc-en">' +
        row.sub +
        '</p>' +
        '<div class="fitme-cc-btns">' +
        '<button type="button" class="fitme-cc-btn fitme-cc-accept">' +
        row.ok +
        '</button>' +
        '<button type="button" class="fitme-cc-btn fitme-cc-min">' +
        row.min +
        '</button>' +
        '</div></div>',
    };
  }

  function restoreGrantedConsent() {
    applyConsentGranted();
    loadAdSense();
    loadClarity();
    if (typeof window.fitmeInitAdSlots === 'function') {
      window.fitmeInitAdSlots();
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    ensureCss();
    setupCtaTracking();
    var consent = '';
    try {
      consent = localStorage.getItem(KEY) || '';
    } catch (e) {}
    if (consent === 'all') {
      restoreGrantedConsent();
      return;
    }
    if (consent === 'essential') return;

    var b = document.createElement('aside');
    b.id = 'fitme-cc-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', 'Cookie notice');
    b.innerHTML = bannerCopy().html;
    document.body.appendChild(b);

    b.querySelector('.fitme-cc-accept').addEventListener('click', fitmeAcceptAllCookies);
    b.querySelector('.fitme-cc-min').addEventListener('click', fitmeRejectNonEssential);
  });
})();

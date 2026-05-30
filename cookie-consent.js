(function () {
  var KEY = 'fitme_cookie_consent';
  var CLIENT_ID = 'ca-pub-6377720400458954';
  var LOCALES =
    'ko|en|ja|pt|es|zh|fr|de|it|ru|ar|hi|th|id|vi'.split('|');

  function ensureCss() {
    if (document.querySelector('link[data-fitme="ccss"]')) return;
    var l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = '/cookie-consent.css?v=8';
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
    var s = document.createElement('script');
    s.async = true;
    s.crossOrigin = 'anonymous';
    s.dataset.fitme = 'adsense';
    s.src =
      'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
      encodeURIComponent(CLIENT_ID);
    s.onload = function () {
      s.dataset.fitmeLoaded = '1';
      if (typeof window.fitmeInitAdSlots === 'function') {
        window.fitmeInitAdSlots();
      }
    };
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
        if (el.classList && (el.classList.contains('hero-btn') || el.classList.contains('cta-btn')))
          track = true;
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

  function normalizeHtmlLang(raw) {
    var x = (raw || 'en').toLowerCase().replace(/_/g, '-');
    if (x.indexOf('zh') === 0) return 'zh';
    if (x.indexOf('pt') === 0) return 'pt';
    if (x === 'ar' || x.indexOf('ar-') === 0) return 'ar';
    var base = x.split('-')[0];
    if (LOCALES.indexOf(base) >= 0) return base;
    return 'en';
  }

  /** Page language: URL /{locale}/… first, then <html lang>, then browser. */
  function detectBannerLang() {
    var path = location.pathname || '/';
    var m = path.match(/^\/(ko|en|ja|pt|es|zh|fr|de|it|ru|ar|hi|th|id|vi)(?:\/|$)/);
    if (m) return m[1];
    return normalizeHtmlLang(document.documentElement.lang);
  }

  var COPY = {
    en: {
      aria: 'Cookie notice',
      lead:
        '<strong>Cookies.</strong> Analytics and personalised ads (Google AdSense) may use cookies for site operations, Google Analytics, Microsoft Clarity, and Google AdSense. See our <a href="/privacy">Privacy Policy</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Accept all',
      min: 'Essential only',
    },
    ko: {
      aria: '쿠키 안내',
      lead:
        '<strong>쿠키·개인화 광고</strong> 서비스 운영 및 Google Analytics, Microsoft Clarity, <strong>Google AdSense</strong> 맞춤 광고를 위해 쿠키가 사용될 수 있습니다. 세부 내용은 <a href="/privacy">개인정보처리방침</a>을 확인하세요. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: '동의합니다',
      min: '필수만',
    },
    ja: {
      aria: 'クッキーに関するお知らせ',
      lead:
        '<strong>クッキー</strong> サイト運営、Google Analytics、Microsoft Clarity、<strong>Google AdSense</strong> のパーソナライズ広告のために使用される場合があります。詳細は <a href="/privacy">プライバシーポリシー</a> をご確認ください。Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: '同意する',
      min: '必須のみ',
    },
    pt: {
      aria: 'Aviso de cookies',
      lead:
        '<strong>Cookies.</strong> Análises e anúncios personalizados (Google AdSense) podem usar cookies para o funcionamento do site, Google Analytics, Microsoft Clarity e Google AdSense. Consulte a <a href="/privacy">Política de Privacidade</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Aceitar tudo',
      min: 'Somente essenciais',
    },
    es: {
      aria: 'Aviso de cookies',
      lead:
        '<strong>Cookies.</strong> El análisis y los anuncios personalizados (Google AdSense) pueden usar cookies para el sitio, Google Analytics, Microsoft Clarity y Google AdSense. Consulte la <a href="/privacy">Política de privacidad</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Aceptar todo',
      min: 'Solo esenciales',
    },
    zh: {
      aria: 'Cookie 提示',
      lead:
        '<strong>Cookie。</strong> 为网站运营、Google Analytics、Microsoft Clarity 与 Google AdSense 个性化广告，我们可能使用 Cookie。详见 <a href="/privacy">隐私政策</a>。Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: '全部接受',
      min: '仅必要',
    },
    fr: {
      aria: 'Avis sur les cookies',
      lead:
        '<strong>Cookies.</strong> Les analyses et publicités personnalisées (Google AdSense) peuvent utiliser des cookies pour le site, Google Analytics, Microsoft Clarity et Google AdSense. Voir la <a href="/privacy">politique de confidentialité</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Tout accepter',
      min: 'Essentiels uniquement',
    },
    de: {
      aria: 'Cookie-Hinweis',
      lead:
        '<strong>Cookies.</strong> Analyse und personalisierte Werbung (Google AdSense) können Cookies für den Betrieb, Google Analytics, Microsoft Clarity und Google AdSense nutzen. Siehe <a href="/privacy">Datenschutz</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Alle akzeptieren',
      min: 'Nur notwendige',
    },
    it: {
      aria: 'Informativa sui cookie',
      lead:
        '<strong>Cookie.</strong> Analisi e annunci personalizzati (Google AdSense) possono usare cookie per il sito, Google Analytics, Microsoft Clarity e Google AdSense. Vedi <a href="/privacy">Privacy Policy</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Accetta tutto',
      min: 'Solo essenziali',
    },
    ru: {
      aria: 'Уведомление о cookie',
      lead:
        '<strong>Cookie.</strong> Аналитика и персонализированная реклама (Google AdSense) могут использовать cookie для работы сайта, Google Analytics, Microsoft Clarity и Google AdSense. См. <a href="/privacy">политику конфиденциальности</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Принять все',
      min: 'Только необходимые',
    },
    ar: {
      aria: 'إشعار ملفات تعريف الارتباط',
      lead:
        '<strong>ملفات تعريف الارتباط.</strong> قد تُستخدم للتشغيل والتحليلات والإعلانات المخصصة (Google AdSense) وGoogle Analytics وMicrosoft Clarity وGoogle AdSense. راجع <a href="/privacy">سياسة الخصوصية</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'قبول الكل',
      min: 'الأساسية فقط',
    },
    hi: {
      aria: 'कुकी सूचना',
      lead:
        '<strong>कुकीज़.</strong> विश्लेषण और व्यक्तिगत विज्ञापन (Google AdSense) साइट संचालन, Google Analytics, Microsoft Clarity और Google AdSense के लिए कुकीज़ उपयोग कर सकते हैं। <a href="/privacy">गोपनीयता नीति</a> देखें। Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'सभी स्वीकार करें',
      min: 'केवल आवश्यक',
    },
    th: {
      aria: 'ประกาศคุกกี้',
      lead:
        '<strong>คุกกี้</strong> การวิเคราะห์และโฆษณาเฉพาะบุคคล (Google AdSense) อาจใช้คุกกี้สำหรับการทำงานของไซต์ Google Analytics Microsoft Clarity และ Google AdSense ดู <a href="/privacy">นโยบายความเป็นส่วนตัว</a> Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'ยอมรับทั้งหมด',
      min: 'เฉพาะที่จำเป็น',
    },
    id: {
      aria: 'Pemberitahuan cookie',
      lead:
        '<strong>Cookie.</strong> Analitik dan iklan personal (Google AdSense) dapat menggunakan cookie untuk operasi situs, Google Analytics, Microsoft Clarity, dan Google AdSense. Lihat <a href="/privacy">Kebijakan Privasi</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Terima semua',
      min: 'Hanya esensial',
    },
    vi: {
      aria: 'Thông báo cookie',
      lead:
        '<strong>Cookie.</strong> Phân tích và quảng cáo cá nhân hóa (Google AdSense) có thể dùng cookie cho vận hành site, Google Analytics, Microsoft Clarity và Google AdSense. Xem <a href="/privacy">Chính sách quyền riêng tư</a>. Publisher ID: <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a>',
      ok: 'Chấp nhận tất cả',
      min: 'Chỉ cần thiết',
    },
  };

  function bannerCopy() {
    var lang = detectBannerLang();
    var row = COPY[lang] || COPY.en;
    return {
      lang: lang,
      html:
        '<div class="fitme-cc-inner">' +
        '<p class="fitme-cc-msg">' +
        row.lead +
        '</p>' +
        '<div class="fitme-cc-btns">' +
        '<button type="button" class="fitme-cc-btn fitme-cc-accept">' +
        row.ok +
        '</button>' +
        '<button type="button" class="fitme-cc-btn fitme-cc-min">' +
        row.min +
        '</button>' +
        '</div></div>',
      aria: row.aria,
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

    var copy = bannerCopy();
    var b = document.createElement('aside');
    b.id = 'fitme-cc-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', copy.aria);
    b.setAttribute('lang', copy.lang);
    if (copy.lang === 'ar') {
      b.setAttribute('dir', 'rtl');
    }
    b.innerHTML = copy.html;
    document.body.appendChild(b);

    b.querySelector('.fitme-cc-accept').addEventListener('click', fitmeAcceptAllCookies);
    b.querySelector('.fitme-cc-min').addEventListener('click', fitmeRejectNonEssential);
  });
})();

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

  document.addEventListener('DOMContentLoaded', function () {
    ensureCss();
    var consent = '';
    try {
      consent = localStorage.getItem(KEY) || '';
    } catch (e) {}
    if (consent === 'all') {
      loadAdSense();
      loadClarity();
      return;
    }
    if (consent === 'essential') return;

    var b = document.createElement('aside');
    b.id = 'fitme-cc-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', 'Cookie notice');
    b.innerHTML =
      '<div class="fitme-cc-inner">' +
      '<p class="fitme-cc-msg"><strong>쿠키·개인화 광고</strong> 서비스 운영 및 Google Analytics, Microsoft Clarity, <strong>Google AdSense 맞춤 광고</strong>를 위해 쿠키가 사용될 수 있습니다. 세부 내용은 <a href="/privacy.html">개인정보처리방침</a>을 확인하세요. Publisher ID(Public): <code>pub-6377720400458954</code> · <a href="/ads.txt">ads.txt</a></p>' +
      '<p class="fitme-cc-msg fitme-cc-en"><strong>Cookies</strong> We may use cookies for analytics and personalised ads (Google AdSense). See our <a href="/privacy.html">Privacy Policy</a>.</p>' +
      '<div class="fitme-cc-btns">' +
      '<button type="button" class="fitme-cc-btn fitme-cc-accept">동의합니다 · Accept</button>' +
      '<button type="button" class="fitme-cc-btn fitme-cc-min">필수만 (광고·분석 거부) · Essential only</button>' +
      '</div></div>';
    document.body.appendChild(b);

    b.querySelector('.fitme-cc-accept').addEventListener('click', fitmeAcceptAllCookies);
    b.querySelector('.fitme-cc-min').addEventListener('click', fitmeRejectNonEssential);
  });
})();

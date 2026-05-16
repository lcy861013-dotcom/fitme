(function () {
  try {
    var t = localStorage.getItem('fitme_theme');
    document.documentElement.setAttribute('data-theme', t === 'light' ? 'light' : 'dark');
  } catch (e) {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
})();

window.fitmeToggleTheme = function () {
  var curr = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  var next = curr === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next);
  try { localStorage.setItem('fitme_theme', next); } catch (e) {}
};

(function injectSatelliteThemeToggle() {
  if (window.location.pathname === '/' || /\/index\.html?$/.test(window.location.pathname)) return;

  function build() {
    if (document.getElementById('fitme-theme-mini')) return;
    var header = document.querySelector('header');
    if (!header) return;
    var btn = document.createElement('button');
    btn.id = 'fitme-theme-mini';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Toggle theme');
    btn.title = 'Theme';
    btn.innerHTML =
      '<svg class="ico-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
      '<circle cx="12" cy="12" r="4"/><path stroke-linecap="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.36 6.36l-.71-.71M6.34 6.34l-.7-.71m12.72 0l-.71.71M6.34 17.66l-.7.71"/></svg>' +
      '<svg class="ico-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
      '<path stroke-linecap="round" stroke-linejoin="round" d="M20.35 15.35A9 9 0 018.65 3.65 9 9 0 1020.35 15.35z"/></svg>';
    btn.style.cssText =
      'display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;' +
      'margin-left:auto;padding:0;border:1px solid var(--border, #2a2724);border-radius:9px;' +
      'background:var(--card, #1c1a18);color:var(--text, #e0dcd8);cursor:pointer;flex-shrink:0;' +
      'transition:border-color .2s, color .2s;';
    btn.addEventListener('mouseenter', function () { btn.style.borderColor = 'var(--accent, #d4a84b)'; btn.style.color = 'var(--accent, #d4a84b)'; });
    btn.addEventListener('mouseleave', function () { btn.style.borderColor = 'var(--border, #2a2724)'; btn.style.color = 'var(--text, #e0dcd8)'; });
    btn.addEventListener('click', window.fitmeToggleTheme);
    header.appendChild(btn);
    var style = document.createElement('style');
    style.textContent =
      '#fitme-theme-mini .ico-moon{display:none;}' +
      'html[data-theme="light"] #fitme-theme-mini .ico-sun{display:none;}' +
      'html[data-theme="light"] #fitme-theme-mini .ico-moon{display:block;}' +
      'html[data-theme="light"] #fitme-theme-mini{background:#fff;color:#11100f;border-color:rgba(0,0,0,0.1);box-shadow:0 1px 2px rgba(0,0,0,0.05);}';
    document.head.appendChild(style);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();

window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
(function () {
  var granted = false;
  try {
    granted = localStorage.getItem('fitme_cookie_consent') === 'all';
  } catch (e) {}
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    wait_for_update: 500,
  });
  if (granted) {
    gtag('consent', 'update', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted',
      analytics_storage: 'granted',
    });
  }
})();

/** Fire GA4 events only when user accepted analytics cookies (aligned with cta_click). */
window.fitmeGaEvent = function (name, params) {
  try {
    if (localStorage.getItem('fitme_cookie_consent') !== 'all') return;
  } catch (e) {
    return;
  }
  if (typeof gtag !== 'function') return;
  gtag('event', name, params || {});
};

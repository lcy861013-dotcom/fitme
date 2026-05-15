(function () {
  try {
    var t = localStorage.getItem('fitme_theme');
    document.documentElement.setAttribute('data-theme', t === 'light' ? 'light' : 'dark');
  } catch (e) {
    document.documentElement.setAttribute('data-theme', 'dark');
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

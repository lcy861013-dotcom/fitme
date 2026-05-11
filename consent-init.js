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

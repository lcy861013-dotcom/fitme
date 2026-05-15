/**
 * AdSense display slots — enable after site approval.
 * Set FITME_ADS_LIVE to true in this file, then deploy.
 */
(function () {
  var LIVE = false;
  var CLIENT = 'ca-pub-6377720400458954';
  var pushed = false;

  function hasConsent() {
    try {
      return localStorage.getItem('fitme_cookie_consent') === 'all';
    } catch (e) {
      return false;
    }
  }

  function adsScriptReady() {
    return !!document.querySelector('script[data-fitme="adsense"]');
  }

  function pushAds() {
    if (!LIVE || !hasConsent() || pushed) return;
    if (!adsScriptReady()) return;
    var slots = document.querySelectorAll('.fitme-ad-slot ins.adsbygoogle');
    if (!slots.length) return;
    document.querySelectorAll('.fitme-ad-slot').forEach(function (wrap) {
      wrap.hidden = false;
      wrap.removeAttribute('aria-hidden');
    });
    try {
      slots.forEach(function () {
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      });
      pushed = true;
    } catch (e) {}
  }

  window.fitmeInitAdSlots = function () {
    if (!LIVE) return;
    pushAds();
    if (!pushed && adsScriptReady()) {
      var t = 0;
      var iv = setInterval(function () {
        pushAds();
        t += 1;
        if (pushed || t > 20) clearInterval(iv);
      }, 250);
    }
  };

  document.addEventListener('DOMContentLoaded', function () {
    if (LIVE && hasConsent()) window.fitmeInitAdSlots();
  });
})();

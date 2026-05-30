/**
 * AdSense display slots — enable after site approval.
 * Set LIVE to true in this file, then deploy.
 * Script loads only after cookie consent (see cookie-consent.js).
 */
(function () {
  var LIVE = false;
  var pushed = false;

  function hasConsent() {
    try {
      return localStorage.getItem('fitme_cookie_consent') === 'all';
    } catch (e) {
      return false;
    }
  }

  function findAdScript() {
    return (
      document.querySelector('script[data-fitme="adsense"]') ||
      document.querySelector(
        'script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]'
      )
    );
  }

  function whenAdsScriptReady(cb) {
    var s = findAdScript();
    if (!s) {
      cb(false);
      return;
    }
    if (s.dataset.fitmeLoaded === '1') {
      cb(true);
      return;
    }
    s.addEventListener(
      'load',
      function () {
        s.dataset.fitmeLoaded = '1';
        cb(true);
      },
      { once: true }
    );
    setTimeout(function () {
      cb(true);
    }, 2500);
  }

  function revealSlots() {
    document.querySelectorAll('.fitme-ad-slot').forEach(function (wrap) {
      wrap.hidden = false;
      wrap.removeAttribute('aria-hidden');
    });
  }

  function pushAds() {
    if (!LIVE || !hasConsent() || pushed) return;
    var slots = document.querySelectorAll('.fitme-ad-slot ins.adsbygoogle');
    if (!slots.length) return;
    if (!findAdScript()) return;

    whenAdsScriptReady(function (ok) {
      if (!ok || pushed || !LIVE || !hasConsent()) return;
      revealSlots();
      try {
        slots.forEach(function () {
          (window.adsbygoogle = window.adsbygoogle || []).push({});
        });
        pushed = true;
      } catch (e) {}
    });
  }

  window.fitmeInitAdSlots = function () {
    if (!LIVE) return;
    pushAds();
    if (!pushed) {
      var t = 0;
      var iv = setInterval(function () {
        pushAds();
        t += 1;
        if (pushed || t > 24) clearInterval(iv);
      }, 250);
    }
  };

  document.addEventListener('DOMContentLoaded', function () {
    if (LIVE && hasConsent()) window.fitmeInitAdSlots();
  });

  document.addEventListener('fitme-cookie-resolved', function () {
    if (LIVE && hasConsent()) window.fitmeInitAdSlots();
  });
})();

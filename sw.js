/* FITME — lightweight offline/cache for static assets only (HTML stays network-first). */
var CACHE = 'fitme-static-v2';

self.addEventListener('install', function (e) {
  self.skipWaiting();
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys
          .filter(function (k) {
            return k !== CACHE && k.indexOf('fitme-static-') === 0;
          })
          .map(function (k) {
            return caches.delete(k);
          })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  /* Never cache-first for full page loads — extensionless URLs like /blog/blog20-en must hit the network. */
  if (req.mode === 'navigate' || req.destination === 'document') return;
  var url;
  try {
    url = new URL(req.url);
  } catch (err) {
    return;
  }
  if (url.origin !== self.location.origin) return;
  var path = url.pathname;
  if (path === '/' || path.endsWith('.html')) return;

  e.respondWith(
    caches.open(CACHE).then(function (cache) {
      return cache.match(req).then(function (hit) {
        if (hit) return hit;
        return fetch(req).then(function (res) {
          if (res && res.ok && res.type === 'basic') {
            try {
              cache.put(req, res.clone());
            } catch (err) {}
          }
          return res;
        });
      });
    })
  );
});

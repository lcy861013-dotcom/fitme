/* FITME — lightweight offline/cache for static assets only (HTML stays network-first). */
var CACHE = 'fitme-static-v1';

self.addEventListener('install', function (e) {
  self.skipWaiting();
});

self.addEventListener('activate', function (e) {
  e.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
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

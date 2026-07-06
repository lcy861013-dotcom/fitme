// Catch-all middleware: aliases + scanner paths that exceed _redirects deploy cap (~125 rules).
// Converts noisy 404s into 301/302 so Cloudflare Analytics 4xx rate drops.

const HOME = 'https://perfectfitme.com/';

/** @type {Record<string, string>} */
const ALIASES_301 = {
  '/feed': '/feed.xml',
  '/atom.xml': '/feed.xml',
  '/rss.xml': '/feed.xml',
  '/sitemap_index.xml': '/sitemap.xml',
  '/sitemap-index.xml': '/sitemap.xml',
  '/sitemap.xml.gz': '/sitemap.xml',
  '/manifest.json': '/site.webmanifest',
  '/apple-touch-icon-precomposed.png': '/icon-192.png',
};

/** @type {Set<string>} */
const SCANNER_302 = new Set([
  '/admin',
  '/administrator',
  '/phpmyadmin',
  '/.env',
  '/login',
  '/register',
  '/manager',
  '/console',
  '/actuator',
  '/server-status',
  '/backup.sql',
  '/database.sql',
  '/humans.txt',
  '/security.txt',
  '/crossdomain.xml',
  '/browserconfig.xml',
]);

/** @type {string[]} */
const SCANNER_PREFIX_302 = ['/.git/', '/wp-json/', '/cgi-bin/', '/api/'];

/** @param {{ request: Request; next: () => Promise<Response> }} context */
export function onRequest(context) {
  const url = new URL(context.request.url);
  const path = url.pathname;

  const alias = ALIASES_301[path];
  if (alias) {
    return Response.redirect(url.origin + alias, 301);
  }

  const lower = path.toLowerCase();

  if (
    SCANNER_302.has(lower) ||
    lower.endsWith('.php') ||
    SCANNER_PREFIX_302.some((prefix) => lower.startsWith(prefix))
  ) {
    return Response.redirect(HOME, 302);
  }

  return context.next();
}

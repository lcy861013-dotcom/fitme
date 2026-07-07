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
  '/signin',
  '/signup',
  '/user/login',
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
  '/readme.html',
  '/license.txt',
  '/config.json',
  '/debug',
  '/trace',
  '/graphql',
  '/swagger',
  '/swagger-ui',
  '/telescope',
  '/_profiler',
  '/shell',
  '/.aws/credentials',
]);

/** @type {string[]} */
const SCANNER_PREFIX_302 = [
  '/.git/',
  '/wp-json/',
  '/cgi-bin/',
  '/api/',
  '/vendor/',
  '/node_modules/',
  '/backup/',
  '/.well-known/security.txt',
];

/** @type {string[]} */
const SCANNER_FRAGMENT_302 = [
  '/wp-admin',
  '/wp-content',
  '/wp-includes',
  '/phpunit',
  '/eval-stdin',
  '/autoload.php',
  '/setup.php',
  '/install.php',
  '/xmlrpc.php',
];

/** @type {RegExp} */
const SCANNER_EXT_RE = /\.(php|asp|aspx|jsp|cgi|sql|bak|old|zip|tar|gz)$/i;

/**
 * @param {string} path
 * @returns {boolean}
 */
function isScannerLikePath(path) {
  const lower = path.toLowerCase();

  if (SCANNER_302.has(lower)) return true;
  if (SCANNER_PREFIX_302.some((prefix) => lower.startsWith(prefix))) return true;
  if (SCANNER_FRAGMENT_302.some((fragment) => lower.includes(fragment))) return true;
  if (SCANNER_EXT_RE.test(lower)) return true;
  if (lower.startsWith('/.env') || lower.startsWith('/.git')) return true;

  return false;
}

/** @param {{ request: Request; next: () => Promise<Response> }} context */
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const path = url.pathname;

  const alias = ALIASES_301[path];
  if (alias) {
    return Response.redirect(url.origin + alias, 301);
  }

  if (isScannerLikePath(path)) {
    return Response.redirect(HOME, 302);
  }

  const response = await context.next();

  // Free-plan analytics hide top 404 URLs — absorb obvious scanner misses post-hoc.
  if (response.status === 404 && isScannerLikePath(path)) {
    return Response.redirect(HOME, 302);
  }

  return response;
}

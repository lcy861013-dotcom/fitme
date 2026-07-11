// Catch-all middleware: aliases + scanner paths that exceed _redirects deploy cap (~125 rules).
// Converts noisy 404s into 301/302 so Cloudflare Analytics 4xx rate drops.
// Bot/scanner 404s get a tiny plain-text body instead of the full 404.html page.

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
  '/wp-login',
  '/manager',
  '/console',
  '/actuator',
  '/server-status',
  '/server-info',
  '/backup.sql',
  '/database.sql',
  '/dump.sql',
  '/humans.txt',
  '/security.txt',
  '/crossdomain.xml',
  '/browserconfig.xml',
  '/readme.html',
  '/readme.md',
  '/license.txt',
  '/config.json',
  '/config.yml',
  '/debug',
  '/trace',
  '/graphql',
  '/swagger',
  '/swagger-ui',
  '/swagger-ui.html',
  '/telescope',
  '/_profiler',
  '/shell',
  '/.aws/credentials',
  '/.dockerenv',
  '/docker-compose.yml',
  '/composer.json',
  '/package.json',
  '/web.config',
  '/elmah.axd',
  '/trace.axd',
  '/_ignition',
  '/horizon',
  '/nova',
  '/filament',
  '/telescope/requests',
  '/phpinfo',
  '/info.php',
  '/test.php',
  '/admin.php',
  '/wp.php',
  '/xmlrpc',
]);

/** @type {string[]} */
const SCANNER_PREFIX_302 = [
  '/.git/',
  '/.svn/',
  '/.hg/',
  '/wp-json/',
  '/cgi-bin/',
  '/api/',
  '/vendor/',
  '/node_modules/',
  '/backup/',
  '/backups/',
  '/old/',
  '/tmp/',
  '/temp/',
  '/.well-known/security.txt',
  '/.well-known/acme-challenge/',
  '/sites/default/files/',
  '/modules/',
  '/includes/',
  '/misc/',
  '/scripts/',
  '/alfa',
  '/c99',
  '/r57',
  '/wso',
];

/** @type {string[]} */
const SCANNER_FRAGMENT_302 = [
  '/wp-admin',
  '/wp-content',
  '/wp-includes',
  '/wordpress',
  '/phpunit',
  '/eval-stdin',
  '/autoload.php',
  '/setup.php',
  '/install.php',
  '/xmlrpc.php',
  '/wlwmanifest',
  '/timthumb',
  '/filemanager',
  '/fckeditor',
  '/ckeditor',
  '/phpmyadmin',
  '/pma/',
  '/myadmin',
  '/adminer',
  '/.env.',
  'wp-config',
];

/** @type {RegExp} */
const SCANNER_EXT_RE =
  /\.(php|asp|aspx|jsp|cgi|sql|bak|old|zip|tar|gz|rar|7z|env|ini|log|swp|dist)$/i;

/** Bot / scanner User-Agent fragments (lowercase). */
const BOT_UA_RE =
  /bot|crawl|spider|slurp|scrap|scan|probe|http.?client|python-requests|curl\/|wget|go-http|java\/|libwww|httpx|aiohttp|okhttp|axios\/|node-fetch|headless|phantom|selenium|puppeteer|playwright|zgrab|masscan|nmap|nikto|sqlmap|dirbuster|gobuster|nuclei|semrush|ahrefs|mj12|dotbot|petalbot|bytespider|gptbot|claudebot|ccbot|amazonbot|dataforseo|serpstat|screaming/i;

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

/**
 * @param {Request} request
 * @returns {boolean}
 */
function isBotLikeRequest(request) {
  const ua = request.headers.get('user-agent') || '';
  if (!ua || ua.length < 8) return true;
  if (BOT_UA_RE.test(ua)) return true;
  return false;
}

/** Tiny 404 — avoids shipping full 404.html to scanners (bandwidth + html noise). */
function lightweight404() {
  return new Response('Not Found', {
    status: 404,
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'no-store',
      'X-Robots-Tag': 'noindex',
    },
  });
}

/** Empty 404 for HEAD probes (common in NL/SG scanner bursts). */
function empty404() {
  return new Response(null, {
    status: 404,
    headers: {
      'Cache-Control': 'no-store',
      'X-Robots-Tag': 'noindex',
    },
  });
}

/** @param {{ request: Request; next: () => Promise<Response> }} context */
export async function onRequest(context) {
  const { request } = context;
  const url = new URL(request.url);
  const path = url.pathname;
  const method = request.method.toUpperCase();

  const alias = ALIASES_301[path];
  if (alias) {
    return Response.redirect(url.origin + alias, 301);
  }

  // Known scanner paths → 302 home (drops out of 4xx bucket entirely).
  if (isScannerLikePath(path)) {
    return Response.redirect(HOME, 302);
  }

  const response = await context.next();

  if (response.status !== 404) {
    return response;
  }

  // Post-hoc: scanner-shaped path that slipped through → still 302.
  if (isScannerLikePath(path)) {
    return Response.redirect(HOME, 302);
  }

  // HEAD probes: empty body (no 404.html).
  if (method === 'HEAD') {
    return empty404();
  }

  // Bot / empty-UA 404: tiny plain text instead of full HTML page.
  if (isBotLikeRequest(request)) {
    return lightweight404();
  }

  // Real browsers keep the styled 404.html from Pages.
  return response;
}

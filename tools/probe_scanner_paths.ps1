# Probe perfectfitme.com for status codes (run locally; safe read-only checks).
# Usage: powershell -File tools/probe_scanner_paths.ps1

$base = "https://perfectfitme.com"
$paths = @(
  "/wp-admin", "/wp-login.php", "/xmlrpc.php", "/.env", "/admin", "/login",
  "/favicon.ico", "/manifest.json", "/feed", "/sitemap.xml", "/ads.txt",
  "/blog/blog26", "/blog/blog26-en", "/ko/index", "/en/about",
  "/nonexistent-page-xyz"
)

foreach ($p in $paths) {
  try {
    $r = Invoke-WebRequest -Uri "$base$p" -Method Head -MaximumRedirection 0 -ErrorAction Stop
    $code = $r.StatusCode
  } catch {
    $resp = $_.Exception.Response
    if ($resp) { $code = [int]$resp.StatusCode } else { $code = "ERR" }
  }
  Write-Output ("{0,3} {1}" -f $code, $p)
}

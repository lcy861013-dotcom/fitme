/*
 * FITME — Universal share bar for blog posts.
 * Auto-injects a Pinterest / WhatsApp / X / Facebook / Copy bar at the end of <main>.
 * Uses page meta (og:title, og:image, canonical) for context.
 *
 * Why this matters:
 *  - Pinterest is the #1 organic traffic driver for fashion/style content globally.
 *  - WhatsApp share is critical for LATAM, India, MENA, Southeast Asia.
 *  - X (Twitter) keeps western tech-savvy fashion audience.
 *  - Native copy-link covers Reddit / Discord / DMs.
 */
(function () {
  function $meta(name) {
    var el = document.querySelector(
      'meta[property="' + name + '"], meta[name="' + name + '"]'
    );
    return el ? el.getAttribute('content') : '';
  }

  function pageContext() {
    var canonical = document.querySelector('link[rel="canonical"]');
    var url = canonical ? canonical.href : window.location.href.split('#')[0];
    var title = $meta('og:title') || document.title || 'FITME';
    var desc = $meta('og:description') || $meta('description') || '';
    var image =
      $meta('og:image') || (window.location.origin + '/assets/og-image-en.png');
    return {
      url: url,
      title: title,
      desc: desc,
      image: image,
    };
  }

  function buildBar(ctx) {
    var bar = document.createElement('div');
    bar.className = 'fitme-share-bar';
    bar.setAttribute('role', 'group');
    bar.setAttribute('aria-label', 'Share this article');
    var encodedUrl = encodeURIComponent(ctx.url);
    var encodedTitle = encodeURIComponent(ctx.title);
    var encodedDesc = encodeURIComponent(ctx.desc);
    var encodedImg = encodeURIComponent(ctx.image);
    var pinDesc = encodeURIComponent(ctx.title + ' — ' + ctx.desc);
    var lang = (document.documentElement.lang || '').toLowerCase();
    var shareLabel =
      lang.indexOf('ko') === 0
        ? '이 가이드 공유하기'
        : lang.indexOf('ja') === 0
          ? 'このガイドをシェア'
          : lang.indexOf('pt') === 0
            ? 'Compartilhar este guia'
            : 'Share this guide';

    bar.innerHTML =
      '<div class="fitme-share-label">' + shareLabel + '</div>' +
      '<div class="fitme-share-buttons">' +
      '<a class="fitme-share-btn pinterest" target="_blank" rel="noopener" ' +
      'href="https://www.pinterest.com/pin/create/button/?url=' +
      encodedUrl +
      '&media=' +
      encodedImg +
      '&description=' +
      pinDesc +
      '" aria-label="Save to Pinterest">' +
      '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">' +
      '<path d="M12 0C5.4 0 0 5.4 0 12c0 5 3 9.4 7.4 11.2-.1-.9-.2-2.4 0-3.5l1.4-6s-.4-.7-.4-1.8c0-1.7 1-3 2.2-3 1 0 1.5.8 1.5 1.7 0 1-.7 2.6-1 4 .3 1 1.3 1.9 2.6 1.9 3.2 0 5.4-3.4 5.4-7.5 0-3-2-5.3-5.7-5.3-4.2 0-6.7 3.1-6.7 6.4 0 1.3.5 2.7 1.1 3.4.1.1.2.2.1.3l-.3 1.3c-.1.2-.2.3-.4.2-1.7-.8-2.7-3.2-2.7-5.2 0-4.2 3-8 8.8-8 4.6 0 8.2 3.3 8.2 7.7 0 4.6-2.9 8.3-7 8.3-1.3 0-2.6-.7-3-1.5l-.8 3.2c-.3 1.2-1.1 2.6-1.7 3.5 1.3.4 2.6.6 4 .6 6.6 0 12-5.4 12-12S18.6 0 12 0z"/>' +
      '</svg>Pin</a>' +
      '<a class="fitme-share-btn whatsapp" target="_blank" rel="noopener" ' +
      'href="https://wa.me/?text=' +
      encodedTitle +
      '%20' +
      encodedUrl +
      '" aria-label="Share to WhatsApp">' +
      '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">' +
      '<path d="M17.5 14.4c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1-.2.2-.7.9-.8 1-.1.2-.3.2-.6.1-.3-.1-1.2-.5-2.4-1.5-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.4.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.8-2.1c-.2-.5-.4-.4-.6-.5h-.5c-.2 0-.5.1-.7.3-.3.3-1 1-1 2.5s1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.6-.6 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.1-.3-.2-.6-.4zm-5.5 7.4h-.1c-1.7 0-3.4-.5-4.9-1.4l-.4-.2-3.6.9.9-3.5-.2-.4c-1-1.6-1.5-3.4-1.5-5.2 0-5.4 4.5-9.8 10-9.8 2.7 0 5.2 1 7 2.9 1.9 1.9 2.9 4.4 2.9 7-.1 5.5-4.6 9.7-10.1 9.7zm8.4-18.1C18.1 1.3 15.1.1 12 .1c-6.6 0-12 5.4-12 12 0 2.1.6 4.1 1.6 5.9L0 24l6.2-1.6c1.7 1 3.7 1.4 5.7 1.4h.1c6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.5-8.5z"/>' +
      '</svg>WhatsApp</a>' +
      '<a class="fitme-share-btn x" target="_blank" rel="noopener" ' +
      'href="https://twitter.com/intent/tweet?url=' +
      encodedUrl +
      '&text=' +
      encodedTitle +
      '" aria-label="Share to X">' +
      '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">' +
      '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>' +
      '</svg>Post</a>' +
      '<a class="fitme-share-btn facebook" target="_blank" rel="noopener" ' +
      'href="https://www.facebook.com/sharer/sharer.php?u=' +
      encodedUrl +
      '" aria-label="Share to Facebook">' +
      '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">' +
      '<path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9V14.9H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v6.9C18.3 21.1 22 17 22 12z"/>' +
      '</svg>Share</a>' +
      '<button class="fitme-share-btn copy" type="button" data-copied="false" aria-label="Copy link">' +
      '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
      '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/>' +
      '</svg><span class="lbl">Copy link</span></button>' +
      '</div>';

    var copyBtn = bar.querySelector('.fitme-share-btn.copy');
    copyBtn.addEventListener('click', function () {
      var label = copyBtn.querySelector('.lbl');
      var resetTo = label.textContent;
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(ctx.url);
        } else {
          var ta = document.createElement('textarea');
          ta.value = ctx.url;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
        }
        label.textContent = 'Copied!';
        copyBtn.setAttribute('data-copied', 'true');
        setTimeout(function () {
          label.textContent = resetTo;
          copyBtn.setAttribute('data-copied', 'false');
        }, 1800);
      } catch (e) {}
    });

    return bar;
  }

  function ensureStyles() {
    if (document.getElementById('fitme-share-css')) return;
    var s = document.createElement('style');
    s.id = 'fitme-share-css';
    s.textContent = [
      '.fitme-share-bar{margin:48px 0 12px;padding:18px 18px 16px;background:rgba(212,168,75,0.05);border:1px solid rgba(212,168,75,0.22);border-radius:14px;}',
      '.fitme-share-label{font-size:11px;letter-spacing:2.5px;color:var(--muted, #8b8178);text-transform:uppercase;margin-bottom:12px;font-family:"DM Sans",sans-serif;font-weight:600;}',
      '.fitme-share-buttons{display:flex;flex-wrap:wrap;gap:8px;}',
      '.fitme-share-btn{display:inline-flex;align-items:center;gap:6px;padding:9px 14px;border-radius:8px;border:1px solid rgba(255,255,255,0.08);background:rgba(255,255,255,0.03);color:#e0dcd8;font-family:"DM Sans",sans-serif;font-size:13px;font-weight:600;text-decoration:none;cursor:pointer;transition:transform .15s,border-color .15s,background .15s;-webkit-tap-highlight-color:transparent;}',
      '.fitme-share-btn:hover{transform:translateY(-1px);border-color:var(--accent, #d4a84b);}',
      '.fitme-share-btn.pinterest{background:#E60023;color:#fff;border-color:#E60023;}',
      '.fitme-share-btn.pinterest:hover{background:#bb001c;}',
      '.fitme-share-btn.whatsapp{background:#25D366;color:#fff;border-color:#25D366;}',
      '.fitme-share-btn.whatsapp:hover{background:#1ebe5a;}',
      '.fitme-share-btn.x{background:#000;color:#fff;border-color:#222;}',
      '.fitme-share-btn.x:hover{background:#111;}',
      '.fitme-share-btn.facebook{background:#1877F2;color:#fff;border-color:#1877F2;}',
      '.fitme-share-btn.facebook:hover{background:#1560cc;}',
      '.fitme-share-btn.copy[data-copied="true"]{border-color:#47ff8a;color:#47ff8a;}',
      'html[data-theme="light"] .fitme-share-bar{background:rgba(166,124,24,0.08);border-color:rgba(166,124,24,0.25);}',
      'html[data-theme="light"] .fitme-share-label{color:#5e5a56;}',
      'html[data-theme="light"] .fitme-share-btn.copy{background:#fff;color:#11100f;border-color:rgba(0,0,0,0.1);box-shadow:0 1px 2px rgba(0,0,0,0.05);}',
      'html[data-theme="light"] .fitme-share-btn.copy:hover{border-color:#a67c18;}',
      'html[data-theme="light"] .fitme-share-btn.pinterest{background:#E60023;color:#fff;border-color:#E60023;}',
      'html[data-theme="light"] .fitme-share-btn.whatsapp{background:#25D366;color:#fff;border-color:#25D366;}',
      'html[data-theme="light"] .fitme-share-btn.x{background:#000;color:#fff;border-color:#222;}',
      'html[data-theme="light"] .fitme-share-btn.facebook{background:#1877F2;color:#fff;border-color:#1877F2;}',
      '@media (max-width:560px){.fitme-share-buttons{gap:6px;}.fitme-share-btn{font-size:12px;padding:8px 11px;}}',
    ].join('');
    document.head.appendChild(s);
  }

  function inject() {
    if (document.querySelector('.fitme-share-bar')) return;
    var main = document.querySelector('main');
    if (!main) return;
    ensureStyles();
    var ctx = pageContext();
    var bar = buildBar(ctx);
    var related = main.querySelector('.related');
    if (related) {
      related.parentNode.insertBefore(bar, related);
    } else {
      var cta = main.querySelector('.cta');
      if (cta) {
        cta.parentNode.insertBefore(bar, cta);
      } else {
        main.appendChild(bar);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();

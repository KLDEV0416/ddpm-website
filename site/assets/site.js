// DDP Management website: slideshow, language switch, dividend estimator, menu and enquiry form.
(() => {
  const T = window.DDPM_TEXT || {};
  let lang = 'en';
  const t = (k) => (T[k] && T[k][lang]) || '';

  // ---------- language (English / Bahasa Melayu) ----------
  function setLang(l) {
    lang = l === 'ms' ? 'ms' : 'en';
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach((el) => { const v = t(el.dataset.i18n); if (v) el.textContent = v; });
    document.querySelectorAll('[data-i18n-ph]').forEach((el) => { el.placeholder = t(el.dataset.i18nPh); });
    document.querySelectorAll('[data-i18n-label]').forEach((el) => {
      el.setAttribute('aria-label', t(el.dataset.i18nLabel) + (el.dataset.go !== undefined ? ' ' + (+el.dataset.go + 1) : ''));
    });
    document.querySelectorAll('.lang button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.lang === lang)));
    updatePauseLabel();
    try { localStorage.setItem('ddpm.lang', lang); } catch { /* private mode */ }
    calc();
  }
  document.querySelectorAll('.lang button').forEach((b) => b.addEventListener('click', () => setLang(b.dataset.lang)));

  // ---------- slideshow ----------
  const slides = [...document.querySelectorAll('.slide')];
  const dots = [...document.querySelectorAll('.dot')];
  const pauseBtn = document.getElementById('pause');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let cur = 0, timer = null, paused = reduce;

  function show(i) {
    cur = (i + slides.length) % slides.length;
    slides.forEach((s, k) => {
      const on = k === cur;
      s.classList.toggle('active', on);
      s.setAttribute('aria-hidden', String(!on));
      s.querySelectorAll('a, button').forEach((el) => { el.tabIndex = on ? 0 : -1; });
    });
    dots.forEach((d, k) => { d.classList.toggle('on', k === cur); d.setAttribute('aria-current', String(k === cur)); });
  }
  function start() { stop(); if (!paused) timer = setInterval(() => show(cur + 1), 7500); }
  function stop() { clearInterval(timer); timer = null; }
  function updatePauseLabel() {
    pauseBtn.setAttribute('aria-pressed', String(paused));
    pauseBtn.setAttribute('aria-label', t(paused ? 'slide.play' : 'slide.pause'));
  }
  document.getElementById('prev').addEventListener('click', () => { show(cur - 1); start(); });
  document.getElementById('next').addEventListener('click', () => { show(cur + 1); start(); });
  dots.forEach((d) => d.addEventListener('click', () => { show(+d.dataset.go); start(); }));
  pauseBtn.addEventListener('click', () => { paused = !paused; updatePauseLabel(); paused ? stop() : start(); });
  const hero = document.querySelector('.hero');
  hero.addEventListener('mouseenter', stop); hero.addEventListener('mouseleave', start);
  hero.addEventListener('focusin', stop); hero.addEventListener('focusout', start);
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));

  // ---------- dividend estimator ----------
  const $ = (id) => document.getElementById(id);
  const num = (s) => Number(String(s).replace(/[^\d.]/g, '')) || 0;
  const rm = (n) => 'RM ' + n.toLocaleString('en-MY', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const rmShort = (n) => 'RM ' + (n >= 1e6 ? (n / 1e6).toFixed(2) + 'm' : Math.round(n / 1000) + 'k');
  function calc() {
    const cap = num($('d-cap').value), mem = Math.max(1, num($('d-mem').value)), rate = Number($('d-rate').value);
    const total = cap * rate / 100;
    $('d-rate-out').textContent = rate.toFixed(2) + '%';
    $('d-total').textContent = rm(total);
    $('d-avg').textContent = rm(total / mem);
    const rates = [4, 5, 6, 7, 8];
    const max = cap * Math.max(8, rate) / 100 || 1;
    $('d-bars').innerHTML = rates.map((r) => {
      const v = cap * r / 100;
      return `<button type="button" class="bar-col${Math.abs(r - rate) < 0.01 ? ' cur' : ''}" data-r="${r}" aria-label="${r}%: ${rm(v)}">` +
             `<small>${rmShort(v)}</small><i style="height:${Math.max(6, (v / max) * 110)}px"></i><span>${r}%</span></button>`;
    }).join('');
  }
  ['d-cap', 'd-mem', 'd-rate'].forEach((id) => $(id).addEventListener('input', calc));
  ['d-cap', 'd-mem'].forEach((id) => $(id).addEventListener('blur', (e) => { const n = num(e.target.value); e.target.value = n ? n.toLocaleString('en-MY') : ''; calc(); }));
  $('d-bars').addEventListener('click', (e) => { const b = e.target.closest('.bar-col'); if (b) { $('d-rate').value = b.dataset.r; calc(); } });

  // ---------- menu, form, year ----------
  const menu = document.querySelector('.menu'), nav = $('nav');
  menu.addEventListener('click', () => { const o = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(o)); });
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); } });
  $('year').textContent = new Date().getFullYear();
  const form = $('enquiry'), err = $('q-err');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const f = Object.fromEntries(new FormData(form));
    if (!f.name.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email.trim()) || !f.message.trim()) { err.hidden = false; return; }
    err.hidden = true;
    const subject = `Enquiry: ${(f.org || '').trim() || f.name.trim()}`;
    const body = `${f.message.trim()}\n\nName: ${f.name.trim()}\nOrganisation: ${(f.org || '').trim() || '-'}\nPhone: ${(f.phone || '').trim() || '-'}\nEmail: ${f.email.trim()}`;
    window.location.href = `mailto:Kumaravel@ddpm.com.my?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });

  // ---------- start ----------
  let saved = null; try { saved = localStorage.getItem('ddpm.lang'); } catch { /* ignore */ }
  setLang(saved || 'en');
  show(0); start();
})();

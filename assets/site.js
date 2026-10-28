/* Shared chrome + behaviour. Each page loads:
   <script src="{root}assets/site.js?v=N" data-root="{root}" data-page="{key}"></script> */
(function () {
  const me = document.currentScript;
  const root = me.dataset.root || './';
  const page = me.dataset.page || 'about';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const LINKS = {
    email: 'mailto:sdmrnwashere@gmail.com',
    scholar: 'https://scholar.google.com/citations?user=nHt79bkAAAAJ&hl=en',
    github: 'https://github.com/sdmrnwashere',
    linkedin: 'https://www.linkedin.com/in/sadman-rahman-2412b0339/',
    researchgate: 'https://www.researchgate.net/profile/Sadman-Rahman-5',
    behance: 'https://www.behance.net/sadmanrahman1',
  };
  const ICON = {
    moon: '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    sun: '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    email: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    scholar: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M12 4 2 9.5 12 15l10-5.5L12 4z"/><path d="M6 12v4.5c0 1.4 2.7 3 6 3s6-1.6 6-3V12"/></svg>',
    github: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5a11.5 11.5 0 0 0-3.6 22.4c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .5z"/></svg>',
    linkedin: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 2H3.6C2.7 2 2 2.7 2 3.6v16.8c0 .9.7 1.6 1.6 1.6h16.8c.9 0 1.6-.7 1.6-1.6V3.6c0-.9-.7-1.6-1.6-1.6zM8 19H5V9.5h3V19zM6.5 8.2a1.7 1.7 0 1 1 0-3.5 1.7 1.7 0 0 1 0 3.5zM19 19h-3v-4.6c0-1.1 0-2.5-1.5-2.5S12.8 13 12.8 14.3V19h-3V9.5h2.9v1.3c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.6 2 3.6 4.6V19z"/></svg>',
    researchgate: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 2h18a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1zm6.9 6.2c-2 0-3.3 1.4-3.3 3.8v.5c0 2.4 1.3 3.8 3.3 3.8 1 0 1.8-.3 2.4-.9v-3.1H9.8v1.2h1.1v1.4c-.2.2-.6.3-1 .3-1.1 0-1.7-.9-1.7-2.6V12c0-1.7.6-2.6 1.7-2.6.8 0 1.2.4 1.3 1.2h1.5c-.2-1.5-1.2-2.4-2.8-2.4zm7.3-2.4c-1.3 0-2.1.8-2.1 2.1v.4h1.2v-.4c0-.6.3-1 .9-1s.9.3.9 1-.3 1-1.1 1.7l-1.8 1.6V12h4.2v-1.1h-2.4l1-.9c1.1-.9 1.6-1.6 1.6-2.5 0-1.1-.9-1.7-2.4-1.7z"/></svg>',
    behance: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 6h5.4c2 0 3.3 1 3.3 2.7 0 1-.5 1.8-1.4 2.2 1.2.4 1.9 1.3 1.9 2.6 0 2-1.5 3.1-3.7 3.1H2V6zm2.3 1.9v2.6h2.6c.9 0 1.4-.5 1.4-1.3s-.5-1.3-1.4-1.3H4.3zm0 4.4v3h2.9c1 0 1.6-.6 1.6-1.5s-.6-1.5-1.6-1.5H4.3zM15 6.6h5v1.3h-5V6.6zm2.6 2.6c2.3 0 3.6 1.6 3.5 4.2h-5.3c.1 1.2.8 1.9 1.9 1.9.8 0 1.3-.3 1.6-.9h1.7c-.4 1.5-1.6 2.4-3.3 2.4-2.2 0-3.6-1.5-3.6-3.8s1.4-3.8 3.5-3.8zm1.7 3c-.1-1-.7-1.6-1.7-1.6s-1.6.6-1.8 1.6h3.5z"/></svg>',
    search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  };
  window.SR_ICON = ICON;
  window.SR_LINKS = LINKS;

  // Tiny waveform glyphs, one per sensing modality (viewBox 0 0 80 24)
  const WAVE = {
    EEG: 'M0 12 L6 9 L10 15 L14 7 L18 14 L22 10 L26 16 L30 6 L34 13 L38 11 L42 17 L46 8 L50 12 L54 10 L58 15 L62 7 L66 13 L70 11 L74 14 L80 12',
    ECG: 'M0 14 H14 L17 11 L20 14 H26 L29 16 L32 2 L35 21 L38 14 H46 Q50 8 54 14 H80',
    Radar: 'M0 12 Q3 2 6 12 T12 12 Q14 4 16 12 T20 12 Q21 6 22 12 T25 12 Q26 8 27 12 T30 12 Q32 4 34 12 T38 12 Q41 2 44 12 T50 12 Q54 3 58 12 T66 12 Q71 2 76 12 L80 12',
    IMU: 'M0 18 C8 18 8 6 16 6 S24 18 32 18 S40 4 48 4 S56 16 64 16 S72 8 80 8',
    Audio: 'M4 10v4M10 6v12M16 9v6M22 3v18M28 7v10M34 10v4M40 5v14M46 8v8M52 2v20M58 9v6M64 6v12M70 10v4M76 8v8',
    Circuits: 'M0 18 H10 V6 H22 V18 H34 V6 H46 V18 H58 V6 H70 V18 H80',
    Control: 'M0 20 C6 20 8 2 14 4 S20 16 26 12 S32 7 38 10 S46 12 52 11 S70 11 80 11',
    Vision: 'M2 12 Q22 -2 40 12 Q58 26 78 12 M40 12 m-5 0 a5 5 0 1 0 10 0 a5 5 0 1 0 -10 0',
  };
  const glyph = m => `<svg viewBox="0 0 80 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${WAVE[m] || WAVE.EEG}"/></svg>`;
  window.SR_GLYPH = glyph;

  // ---------- Nav ----------
  const TABS = [['about', 'About', ''], ['publications', 'Papers', 'publications/'], ['cv', 'CV', 'cv/'], ['repositories', 'Code', 'repositories/'], ['misc', 'Misc', 'misc/']];
  const nav = document.createElement('nav');
  nav.className = 'nav'; nav.setAttribute('aria-label', 'Main');
  nav.innerHTML = `<a class="mono-logo" href="${root}" aria-label="Home">SR</a>` +
    TABS.map(([k, label, href], i) => `<a class="tab${k === page ? ' active' : ''}" href="${root}${href}"${k === page ? ' aria-current="page"' : ''}>${label}<sup>${i + 1}</sup></a>`).join('') +
    `<button class="theme" id="themeBtn" aria-label="Toggle dark mode" title="Theme (T)">${ICON.moon}${ICON.sun}</button>`;
  document.body.prepend(nav);

  const toast = document.createElement('div');
  toast.className = 'toast'; document.body.append(toast);
  let toastT;
  const say = msg => { toast.textContent = msg; toast.classList.add('show'); clearTimeout(toastT); toastT = setTimeout(() => toast.classList.remove('show'), 1600); };
  window.SR_SAY = say;

  const isDark = () => { const r = document.documentElement; return r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; };
  const toggleTheme = () => {
    const next = isDark() ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
    say(next === 'dark' ? '◐ lights off' : '◑ lights on');
    dispatchEvent(new Event('sr-theme'));
  };
  $('#themeBtn').addEventListener('click', toggleTheme);

  addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey || /input|textarea|select/i.test(e.target.tagName)) return;
    const n = parseInt(e.key, 10);
    if (n >= 1 && n <= TABS.length) location.href = root + TABS[n - 1][2];
    else if (e.key === 't' || e.key === 'T') toggleTheme();
    else if (e.key === '/' && $('#pubSearch')) { e.preventDefault(); $('#pubSearch').focus(); }
  });

  if (matchMedia('(min-width: 761px)').matches) {
    const hint = document.createElement('div');
    hint.className = 'hint';
    hint.innerHTML = '<kbd>1</kbd>–<kbd>5</kbd> jump · <kbd>T</kbd> theme';
    document.body.append(hint);
    setTimeout(() => hint.classList.add('gone'), 5000);
  }

  // ---------- Footer ----------
  const footer = document.createElement('footer');
  footer.className = 'foot-big';
  footer.innerHTML = `<div class="wrap">
    <span class="mono">§ end of transmission</span>
    <p class="say">Got a signal<br>worth <em>learning from?</em> <a href="${LINKS.email}">Say hi&nbsp;→</a></p>
    <div class="cta">
      <a class="btn solid" href="${LINKS.email}">${ICON.email} sdmrnwashere@gmail.com</a>
      <button class="btn" id="copyEmail" type="button">Copy email</button>
      <div class="icon-row">${['scholar', 'github', 'linkedin', 'researchgate', 'behance'].map(k => `<a href="${LINKS[k]}" target="_blank" rel="noopener" aria-label="${k}" title="${k}">${ICON[k]}</a>`).join('')}</div>
    </div>
    <svg class="pulse" viewBox="0 0 1200 50" preserveAspectRatio="none" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
      <path d="M0 30 H420 L432 30 L440 22 L448 30 H470 L478 34 L490 4 L502 46 L512 30 H540 Q556 18 572 30 H1200"/></svg>
    <div class="row"><span class="mono">© ${new Date().getFullYear()} Sadman Rahman · Dhaka, BD</span><span class="mono">Keys: 1–5 pages · T theme · / search papers</span></div>
  </div>`;
  document.body.append(footer);
  $('#copyEmail').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText('sdmrnwashere@gmail.com'); say('✓ email copied'); } catch (e) { location.href = LINKS.email; }
  });

  // ---------- Reveal on scroll ----------
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px' });
  $$('.rv').forEach(el => io.observe(el));

  // ---------- Signal scope (hero canvas) ----------
  const cv = $('#scope');
  if (cv) {
    const ctx = cv.getContext('2d');
    const CH = ['EEG', 'ECG', 'IMU', 'RADAR'];
    let W = 0, H = 0, dpr = 1, t = 0, running = true, colors = {};
    const mouse = { x: -1e3, y: -1e3, on: false };
    const spikes = [];
    const readColors = () => {
      const s = getComputedStyle(document.documentElement);
      colors = { ink: s.getPropertyValue('--trace').trim(), accent: s.getPropertyValue('--accent').trim(), rule: s.getPropertyValue('--rule').trim() };
    };
    const size = () => {
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    // deterministic pseudo-noise
    const n = x => Math.sin(x * 12.9898) * 43758.5453 % 1;
    const sig = [
      (x, t) => .45 * Math.sin(x * .09 + t * 2.1) + .3 * Math.sin(x * .23 - t * 3.3) + .18 * Math.sin(x * .61 + t * 5) + .12 * n(Math.floor(x + t * 60)),
      (x, t) => { const p = ((x + t * 70) % 150 + 150) % 150; return -1.2 * Math.exp(-((p - 60) ** 2) / 6) + .35 * Math.exp(-((p - 54) ** 2) / 4) + .28 * Math.exp(-((p - 66) ** 2) / 5) + .25 * Math.exp(-((p - 100) ** 2) / 80) - .12 * Math.exp(-((p - 25) ** 2) / 30); },
      (x, t) => .7 * Math.tanh(3 * Math.sin(x * .025 + t * 1.2)) + .1 * Math.sin(x * .3 + t * 4),
      (x, t) => .6 * Math.sin(x * .07 + 4 * Math.sin(x * .012 - t * 1.4)) * (.6 + .4 * Math.sin(x * .01 + t)),
    ];
    // The "model" lane: a toy attention map over the four channels, plus a fake classifier readout.
    const MODEL_H = 34;
    const CLASSES = [['alert', 'drowsy'], ['normal beat', 'ectopic beat'], ['walking', 'gesture'], ['still', 'posture change']];
    const predict = c => {
      const k = Math.sin(t * .45 + c * 1.7) > 0 ? 1 : 0;
      return `${CLASSES[c][k]} · p = ${(.72 + .27 * Math.abs(Math.sin(t * .8 + c))).toFixed(2)}`;
    };
    const attention = x => {
      let e = .6 * Math.abs(sig[0](x, t)) + .9 * Math.abs(sig[1](x, t)) + .3 * Math.abs(sig[2](x, t)) + .45 * Math.abs(sig[3](x, t));
      for (const s of spikes) { const d = (x - s.x) / 14; e += Math.abs(s.a) * Math.exp(-d * d); }
      if (mouse.on) { const d = (x - mouse.x) / 50; e += .8 * Math.exp(-d * d); }
      return Math.min(1, Math.max(0, (e - .35) / 1.1));
    };
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      const SH = H - MODEL_H, lane = SH / CH.length;
      // grid
      ctx.strokeStyle = colors.rule; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
      for (let gx = 80; gx < W; gx += 80) { ctx.beginPath(); ctx.moveTo(gx + .5, 0); ctx.lineTo(gx + .5, SH); ctx.stroke(); }
      ctx.setLineDash([]);
      // channel labels
      ctx.font = '500 10.5px "Geist Mono", ui-monospace, monospace'; ctx.textBaseline = 'middle';
      ctx.fillStyle = colors.ink; ctx.globalAlpha = .45;
      CH.forEach((name, c) => ctx.fillText(name === 'RADAR' ? 'RAD' : name, 14, lane * (c + .5)));
      ctx.fillText('MODEL', 14, SH + MODEL_H / 2); ctx.globalAlpha = 1;
      // model lane: attention cells
      ctx.strokeStyle = colors.rule; ctx.beginPath(); ctx.moveTo(0, SH + .5); ctx.lineTo(W, SH + .5); ctx.stroke();
      ctx.fillStyle = colors.accent;
      for (let x = 64; x < W - 4; x += 7) {
        ctx.globalAlpha = .08 + .85 * attention(x + 3);
        ctx.fillRect(x, SH + 9, 5, MODEL_H - 18);
      }
      ctx.globalAlpha = 1;
      for (let c = 0; c < CH.length; c++) {
        const cy = lane * (c + .5), amp = lane * .32;
        const near = mouse.on && Math.abs(mouse.y - cy) < lane / 2;
        ctx.beginPath();
        for (let x = 64; x <= W; x += 2) {
          let y = sig[c](x, t);
          if (mouse.on) { const d = (x - mouse.x) / 60; y *= 1 + (near ? 2.2 : .5) * Math.exp(-d * d); }
          for (const s of spikes) if (s.c === c) { const d = (x - s.x) / 6; y += s.a * Math.exp(-d * d) * Math.sin(d * 3); }
          const py = cy - y * amp;
          x === 64 ? ctx.moveTo(x, py) : ctx.lineTo(x, py);
        }
        ctx.strokeStyle = c === 0 || near ? colors.accent : colors.ink;
        ctx.globalAlpha = c === 0 || near ? 1 : .55;
        ctx.lineWidth = near ? 1.8 : 1.3;
        ctx.stroke(); ctx.globalAlpha = 1;
      }
      if (mouse.on) { // cursor line
        ctx.strokeStyle = colors.accent; ctx.globalAlpha = .4; ctx.beginPath(); ctx.moveTo(mouse.x + .5, 0); ctx.lineTo(mouse.x + .5, H); ctx.stroke(); ctx.globalAlpha = 1;
      }
    };
    const readout = $('#scopeReadout');
    const chanAt = y => Math.max(0, Math.min(CH.length - 1, Math.floor(y / ((H - MODEL_H) / CH.length))));
    let lastRead = 0;
    const updateReadout = () => {
      if (!readout) return;
      if (mouse.on) readout.textContent = `${CH[chanAt(mouse.y)]} · t = ${(mouse.x / 100).toFixed(2)} s → ${predict(chanAt(mouse.y))}`;
      else { const c = Math.floor(t / 1.6) % CH.length; readout.textContent = `model ▸ ${CH[c]}: ${predict(c)} · hover or click`; }
    };
    const loop = (now) => {
      if (running) {
        t += 0.012; for (const s of spikes) s.a *= .965; while (spikes.length && Math.abs(spikes[0].a) < .02) spikes.shift(); draw();
        if (now - lastRead > 250) { updateReadout(); lastRead = now; }
      }
      requestAnimationFrame(loop);
    };
    cv.addEventListener('pointermove', e => {
      const r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; mouse.on = true;
      if (reduce) { draw(); updateReadout(); }
    });
    cv.addEventListener('pointerleave', () => { mouse.on = false; if (reduce) { draw(); updateReadout(); } });
    cv.addEventListener('click', e => {
      const r = cv.getBoundingClientRect();
      spikes.push({ x: e.clientX - r.left, c: chanAt(e.clientY - r.top), a: 1.6 });
      if (reduce) draw();
    });
    new IntersectionObserver(([e]) => { running = e.isIntersecting && !reduce; }).observe(cv);
    addEventListener('resize', () => { size(); draw(); });
    addEventListener('sr-theme', () => { readColors(); draw(); });
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { readColors(); draw(); });
    readColors(); size(); draw(); updateReadout(); requestAnimationFrame(loop);
  }

  // ---------- Publications ----------
  const PUBS = [
    { y: 2026, m: 'EEG', type: 'journal', sel: true, q: 'Q1',
      title: 'Single-Channel Wearable EEG for ADL Recognition in Healthy and Epileptic Cohorts Using MODWT-MRA and Machine Learning',
      authors: 'Mahdia Binte Maksud, Sadman Rahman, Md. Mehedi Hasan Bhuiyan, Tahiya Iffat Majumder, Kazi Newaj Faisal',
      venue: 'Biomedical Signal Processing and Control', status: 'Accepted', url: 'https://www.sciencedirect.com/science/article/pii/S1746809426021580' },
    { y: 2026, m: 'IMU', type: 'journal', sel: true, q: 'Q1',
      title: 'Stacking Multi-Variate Time–Frequency Information: A Deep Learning Approach for IMU–MMG Based Hand Gesture Recognition',
      authors: 'Sadman Rahman, Md. Mehedi Hasan Bhuiyan, Nasiruddin Mahmud Himel, Rishi Raj Sharma, Kazi Newaj Faisal',
      venue: 'IEEE Sensors Journal', url: 'https://ieeexplore.ieee.org/abstract/document/11508135' },
    { y: 2026, m: 'EEG', type: 'journal', sel: true, q: 'Q1',
      title: 'HatSeqNet: A Sequence-Based Deep Learning Model for Cross-Subject Driver Drowsiness Detection Using Single-Channel EEG Signal',
      authors: 'Sadman Rahman, Saquib Farhan, Rishi Raj Sharma, Kazi Newaj Faisal',
      venue: 'IEEE Sensors Journal', url: 'https://ieeexplore.ieee.org/document/11459382' },
    { y: 2026, m: 'Radar', type: 'journal', sel: true, q: 'Q2',
      title: 'Radar-Based Sleep Posture Transition Sensing: An Efficient Deep Learning Hierarchical Temporal Architecture Utilizing Depthwise Convolution',
      authors: 'Sadman Rahman, Rishi Raj Sharma, Kazi Newaj Faisal',
      venue: 'IEEE Sensors Letters', url: 'https://ieeexplore.ieee.org/document/11594419/' },
    { y: 2026, m: 'Circuits', type: 'journal', q: 'Q3',
      title: 'A Comparative Logic-Style Framework for 8-Bit 12-Function Efficient ALU Design Using Transmission Gate and NMOS Pass Transistor Logic in 90-nm CMOS',
      authors: 'Saquib Farhan, Sadman Rahman, Sanjida Sultana, Md. Tawfiq Amin, Gourab Datta',
      venue: 'Analog Integrated Circuits and Signal Processing', url: 'https://link.springer.com/article/10.1007/s10470-026-02664-5' },
    { y: 2026, m: 'ECG', type: 'conference',
      title: 'Short-Term SVMD-Enhanced High-Resolution Time–Frequency Representation for ECG Signal Analysis',
      authors: 'Sadman Rahman, Kazi Newaj Faisal', venue: 'IEEE SPMB', status: 'Accepted' },
    { y: 2026, m: 'IMU', type: 'conference',
      title: 'FormSense: A Continuous Fatigue and Form Tracking Application for Resistance Workout Monitoring Utilizing Phase-Graded IMU Analysis',
      authors: 'Abdullah Al Mahi, Munawar Arif Nitol, Md Mehedi Hasan Bhuiyan, Sadman Rahman, Kazi Newaj Faisal', venue: 'IEEE ICACCESS', status: 'Accepted' },
    { y: 2026, m: 'Audio', type: 'conference', sel: true,
      title: 'VoxScope: A Deployment-Oriented Analysis Framework for Extreme Vocal Distortion Techniques in Heavy Metal',
      authors: 'Sadman Rahman, Kazi Newaj Faisal', venue: 'IEEE SPICSCON', status: 'Accepted' },
    { y: 2026, m: 'EEG', type: 'conference', award: 'Best Presenter',
      title: 'Exploring Gamma-Band Filtered Features and Machine Learning for Resource-Efficient Multi-Level Cognitive Load Classification Using EEG',
      authors: 'Nur Md. Atiquzzaman Rasel, Sadman Rahman*, Kazi Newaj Faisal', venue: 'IEEE QPAIN', url: 'https://ieeexplore.ieee.org/abstract/document/11545759' },
    { y: 2025, m: 'Radar', type: 'journal', q: 'Q2',
      title: 'Improved FMCW Radar Sensing for HAR Systems: Synchroextracting Transform-Enhanced Time–Frequency Representation and Custom Anisotropic CNN',
      authors: 'Arnob Ghosh, Sadman Rahman*, Labib Siddique Siam, Kazi Newaj Faisal',
      venue: 'IEEE Sensors Letters', url: 'https://ieeexplore.ieee.org/document/11419777' },
    { y: 2025, m: 'Audio', type: 'conference', sel: true, award: 'Best Paper',
      title: 'Leveraging Power-Spectrum-Based Features and Machine Learning for Resource-Efficient Cough Classification in Respiratory Disease Monitoring',
      authors: 'Sadman Rahman, Irtiza Mohtasim, Saquib Farhan, Kazi Newaj Faisal', venue: 'IEEE SPICSCON', url: 'https://ieeexplore.ieee.org/document/11504221' },
    { y: 2025, m: 'Control', type: 'conference',
      title: 'Neural Network Enhanced PID Control of Automatic Voltage Regulators: A Comparative Study with Classical and Regression Approaches',
      authors: 'Sadman Rahman, Saquib Farhan, Saiba Aabira, Sunjida Sultana', venue: 'IEEE PEEIACON', url: 'https://www.researchgate.net/publication/403049814' },
    { y: 2025, m: 'Vision', type: 'conference',
      title: 'GCAF-Net: An Attention-Enhanced Deep CNN Framework with Grad-CAM for Classifying Rare and Endangered Medicinal Plants in Bangladesh',
      authors: 'Sadman Rahman*, Saquib Farhan*, Saiba Aabira, Kazi Newaj Faisal', venue: 'IEEE QPAIN', url: 'https://ieeexplore.ieee.org/abstract/document/11171960' },
    { y: 2025, m: 'Circuits', type: 'conference',
      title: 'High-Speed, Low-Power 8-Bit 12-Function ALU Using Transmission Gate Logic in 90nm Technology',
      authors: 'Saquib Farhan*, Sadman Rahman*, Saiba Aabira, Gourab Datta, Sunjida Sultana, Md. Tawfiq Amin', venue: 'IEEE QPAIN', url: 'https://ieeexplore.ieee.org/document/11172017' },
  ];

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const pubHTML = p => {
    const authors = esc(p.authors).split(', ').map(a => a.startsWith('Sadman Rahman') ? `<b>${a}</b>` : a).join(', ');
    const title = p.url ? `<a href="${p.url}" target="_blank" rel="noopener">${esc(p.title)}</a>` : esc(p.title);
    return `<li class="pub">
      <div class="sig">${glyph(p.m)}<span>${p.m} · ${p.type === 'journal' ? 'Journal' : 'Conf.'}</span></div>
      <div><h3>${title}</h3><p class="authors">${authors}</p>
        <div class="venue"><i>${esc(p.venue)}</i>
          ${p.q ? `<span class="pill${p.q === 'Q1' ? ' q1' : ''}">${p.q}</span>` : ''}
          ${p.award ? `<span class="pill win">★ ${p.award}</span>` : ''}
          ${p.status ? `<span class="pill">${p.status}</span>` : ''}
        </div>
        ${p.url ? `<a class="go" href="${p.url}" target="_blank" rel="noopener">Read paper ↗</a>` : ''}
      </div>
      <span class="year">${p.y}</span></li>`;
  };

  const sel = $('#selectedPubs');
  if (sel) sel.innerHTML = PUBS.filter(p => p.sel).map(pubHTML).join('');

  const all = $('#allPubs');
  if (all) {
    const tools = $('#pubTools');
    const mods = ['EEG', 'Radar', 'IMU', 'ECG', 'Audio'];
    const count = f => PUBS.filter(f).length;
    const filters = [
      ['all', 'All', () => true], ['journal', 'Journals', p => p.type === 'journal'], ['conference', 'Conferences', p => p.type === 'conference'],
      ...mods.map(m => [m, m, p => p.m === m]), ['other', 'Other', p => !mods.includes(p.m)],
    ];
    tools.innerHTML = filters.map(([k, label, f], i) => `<button class="chip" data-k="${k}" aria-pressed="${i === 0}">${label}<em>${count(f)}</em></button>`).join('') +
      `<label class="search">${ICON.search}<input id="pubSearch" type="search" placeholder="Search titles, authors…  /" aria-label="Search publications"></label>`;
    let active = filters[0][2], query = '';
    const render = () => {
      const q = query.toLowerCase();
      const list = PUBS.filter(active).filter(p => !q || (p.title + ' ' + p.authors + ' ' + p.venue + ' ' + p.m).toLowerCase().includes(q));
      all.innerHTML = list.length ? list.map(pubHTML).join('') : `<li class="empty">No signal detected. Try another filter.</li>`;
      $('#pubCount').textContent = `${list.length} / ${PUBS.length}`;
    };
    $$('.chip', tools).forEach(b => b.addEventListener('click', () => {
      $$('.chip', tools).forEach(x => x.setAttribute('aria-pressed', x === b));
      active = filters.find(f => f[0] === b.dataset.k)[2]; render();
    }));
    $('#pubSearch').addEventListener('input', e => { query = e.target.value; render(); });
    render();
  }
})();

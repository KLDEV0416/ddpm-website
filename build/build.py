"""Builds site/index.html and site/assets/i18n.js for the DDP Management website.
Text lives in T below as (English, Bahasa Melayu). Run: python build/build.py"""
import json, os, re
from art import scene_members, scene_dividend, scene_loan, scene_payments, brand

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T = {
  'title': ('DDP Management: IT delivery and business automation for SMEs and financial services', 'DDP Management: penyampaian IT dan automasi perniagaan untuk PKS dan perkhidmatan kewangan'),
  'desc': ('DDP Management replaces paper-based, manual operations with automated digital platforms for SMEs and financial services companies in Malaysia, including a complete koperasi digital operations platform.',
           'DDP Management menggantikan operasi manual berasaskan kertas dengan platform digital automatik untuk PKS dan syarikat perkhidmatan kewangan di Malaysia, termasuk platform operasi digital koperasi yang lengkap.'),
  'brand.tag': ('IT Delivery & Business Automation', 'Penyampaian IT & Automasi Perniagaan'),
  'nav.services': ('Services', 'Perkhidmatan'),
  'nav.koperasi': ('Koperasi platform', 'Platform koperasi'),
  'nav.how': ('How we work', 'Cara kami bekerja'),
  'nav.contact': ('Contact', 'Hubungi'),
  'cta.talk': ('Talk to us', 'Hubungi kami'),
  'cta.services': ('See what we do', 'Lihat perkhidmatan kami'),
  'menu': ('Menu', 'Menu'),

  's1.h': ('Replace manual operations with automated digital platforms', 'Gantikan operasi manual dengan platform digital automatik'),
  's1.p': ('Purpose-built for SMEs and financial services companies in Malaysia. We design, build and support systems that cut cost, reduce error and free your people to focus on customers instead of paperwork.',
           'Dibina khusus untuk PKS dan syarikat perkhidmatan kewangan di Malaysia. Kami mereka bentuk, membina dan menyokong sistem yang mengurangkan kos, mengurangkan kesilapan dan membebaskan kakitangan anda untuk memberi tumpuan kepada pelanggan, bukan kertas kerja.'),
  's2.h': ('A complete digital platform for koperasi', 'Platform digital lengkap untuk koperasi'),
  's2.p': ('Member management, share capital and subscriptions, nominee records, PDPA consent, loans, dividends and Angkasa deductions, in one system members can use from their phone.',
           'Pengurusan ahli, modal syer dan yuran, rekod penama, persetujuan PDPA, pinjaman, dividen dan potongan Angkasa, dalam satu sistem yang boleh digunakan ahli melalui telefon.'),
  's3.h': ('Every payment matched automatically', 'Setiap bayaran dipadankan secara automatik'),
  's3.p': ('Salary deductions, online payments and receipts reconciled without manual matching, with a full record of every transaction.',
           'Potongan gaji, bayaran dalam talian dan resit dipadankan tanpa kerja manual, dengan rekod lengkap setiap transaksi.'),
  's4.h': ('Results your committee can see', 'Hasil yang dapat dilihat oleh jawatankuasa anda'),
  's4.p': ('More than 100 business processes automated and over RM1 million in manpower cost savings delivered through automation.',
           'Lebih 100 proses perniagaan diautomasikan dan lebih RM1 juta penjimatan kos tenaga kerja melalui automasi.'),
  'slide.prev': ('Previous slide', 'Slaid sebelumnya'),
  'slide.next': ('Next slide', 'Slaid seterusnya'),
  'slide.pause': ('Pause slides', 'Jeda slaid'),
  'slide.play': ('Play slides', 'Main slaid'),
  'slide.go': ('Show slide', 'Tunjuk slaid'),

  'stat1': ('Business processes automated across financial services engagements', 'Proses perniagaan diautomasikan dalam projek perkhidmatan kewangan'),
  'stat2': ('Manpower cost savings delivered through automation', 'Penjimatan kos tenaga kerja melalui automasi'),
  'stat3': ('Every platform is built around the governance, data-protection and reporting standards Malaysia\'s financial-services regulators expect, so compliance is designed in, not retrofitted.',
            'Setiap platform dibina berdasarkan piawaian tadbir urus, perlindungan data dan pelaporan yang diharapkan oleh pengawal selia perkhidmatan kewangan Malaysia, jadi pematuhan direka sejak awal, bukan ditambah kemudian.'),

  'svc.h': ('What we do', 'Apa yang kami lakukan'),
  'svc.p': ('From member management to claims-adjacent workflows, we take operations from paper to dependable digital platforms.',
            'Daripada pengurusan ahli hingga aliran kerja berkaitan tuntutan, kami membawa operasi daripada kertas kepada platform digital yang boleh dipercayai.'),
  'v1.h': ('Koperasi Digital Operations Platform', 'Platform Operasi Digital Koperasi'),
  'v1.p': ('A dedicated platform covering member management, share capital and subscriptions, statutory nominee records and PDPA consent, replacing manual, paper-based koperasi administration.',
           'Platform khusus merangkumi pengurusan ahli, modal syer dan yuran, rekod penama berkanun dan persetujuan PDPA, menggantikan pentadbiran koperasi manual berasaskan kertas.'),
  'v2.h': ('Business Process Automation', 'Automasi Proses Perniagaan'),
  'v2.p': ('End-to-end automation of high-volume, manual workflows across insurance and koperasi operations, cutting turnaround time and reducing dependence on manual headcount.',
           'Automasi menyeluruh aliran kerja manual bervolum tinggi dalam operasi insurans dan koperasi, memendekkan masa pemprosesan dan mengurangkan kebergantungan kepada tenaga kerja manual.'),
  'v3.h': ('Digital System Implementation', 'Pelaksanaan Sistem Digital'),
  'v3.p': ('Full-cycle implementation of digital systems, from requirements through go-live, sized to fit real operational capacity and budget, not a generic template.',
           'Pelaksanaan sistem digital kitaran penuh, daripada keperluan hingga mula guna, disesuaikan dengan kapasiti operasi dan bajet sebenar, bukan templat umum.'),
  'v4.h': ('Business-as-Usual Support', 'Sokongan Operasi Harian'),
  'v4.p': ('Ongoing support and system enhancements after go-live, flexing with day-to-day operational needs as your organisation and its customer or member base grow.',
           'Sokongan berterusan dan penambahbaikan sistem selepas mula guna, mengikut keperluan operasi harian seiring pertumbuhan organisasi serta pelanggan atau ahli anda.'),
  'v5.h': ('Process Re-engineering & Digitalisation', 'Penyusunan Semula Proses & Pendigitalan'),
  'v5.p': ('We redesign a process before we automate it, so digitalisation removes waste and manual steps rather than simply moving paper forms onto a screen.',
           'Kami mereka bentuk semula proses sebelum mengautomasikannya, supaya pendigitalan menghapuskan pembaziran dan langkah manual, bukan sekadar memindahkan borang kertas ke skrin.'),

  'who.h': ('Who we work with', 'Siapa yang kami bantu'),
  'who.1h': ('SMEs', 'PKS'), 'who.1p': ('Approvals, records and reporting moved off spreadsheets and paper.', 'Kelulusan, rekod dan laporan dipindahkan daripada hamparan dan kertas.'),
  'who.2h': ('Insurance', 'Insurans'), 'who.2p': ('High-volume, claims-adjacent workflows automated end to end.', 'Aliran kerja berkaitan tuntutan bervolum tinggi diautomasikan sepenuhnya.'),
  'who.3h': ('Koperasi', 'Koperasi'), 'who.3p': ('Members, shares, loans, dividends and Angkasa deductions in one platform.', 'Ahli, syer, pinjaman, dividen dan potongan Angkasa dalam satu platform.'),
  'who.4h': ('Financial services', 'Perkhidmatan kewangan'), 'who.4p': ('Systems built around governance, data protection and regulatory reporting.', 'Sistem dibina berasaskan tadbir urus, perlindungan data dan pelaporan kawal selia.'),

  'why.h': ('Why it works', 'Mengapa ia berkesan'),
  'why.p': ('We pair hands-on business analysis with delivery discipline. Every engagement starts by mapping your actual processes and regulatory obligations, then automates only what genuinely reduces cost and risk. The result is a system your committee can approve with confidence and your staff can actually run.',
            'Kami menggabungkan analisis perniagaan secara langsung dengan disiplin penyampaian. Setiap projek bermula dengan memetakan proses sebenar dan kewajipan kawal selia anda, kemudian mengautomasikan hanya perkara yang benar-benar mengurangkan kos dan risiko. Hasilnya, sistem yang boleh diluluskan oleh jawatankuasa dengan yakin dan benar-benar boleh digunakan oleh kakitangan anda.'),
  'how.h': ('How we work', 'Cara kami bekerja'),
  'how.1h': ('Map', 'Petakan'), 'how.1p': ('We map your actual processes, data and regulatory obligations with the people who do the work.', 'Kami memetakan proses, data dan kewajipan kawal selia sebenar bersama mereka yang melakukan kerja tersebut.'),
  'how.2h': ('Redesign', 'Reka semula'), 'how.2p': ('We remove waste and manual steps first, and agree where automation pays off.', 'Kami menghapuskan pembaziran dan langkah manual dahulu, dan bersetuju di mana automasi memberi pulangan.'),
  'how.3h': ('Build and implement', 'Bina dan laksana'), 'how.3p': ('We deliver in stages, test with your team, train your staff and go live alongside existing processes.', 'Kami menyampaikan secara berperingkat, menguji bersama pasukan anda, melatih kakitangan dan mula guna seiring proses sedia ada.'),
  'how.4h': ('Support and improve', 'Sokong dan tambah baik'), 'how.4p': ('Business-as-usual support and enhancements as your organisation grows.', 'Sokongan operasi harian dan penambahbaikan seiring pertumbuhan organisasi anda.'),

  'kp.h': ('Koperasi Digital Operations Platform', 'Platform Operasi Digital Koperasi'),
  'kp.p': ('Our flagship platform for koperasi: everything the office and the board run on, with a mobile app for every member. Modules are switched on in phases, as the koperasi is ready.',
           'Platform utama kami untuk koperasi: semua yang diperlukan pejabat dan lembaga, dengan aplikasi mudah alih untuk setiap ahli. Modul dihidupkan secara berperingkat, apabila koperasi bersedia.'),
  'k1': ('Member management and registration', 'Pengurusan dan pendaftaran ahli'),
  'k2': ('Share capital and subscriptions', 'Modal syer dan yuran'),
  'k3': ('Statutory nominee records and PDPA consent', 'Rekod penama berkanun dan persetujuan PDPA'),
  'k4': ('Loan applications, accounts and early settlement', 'Permohonan, akaun dan penyelesaian awal pinjaman'),
  'k5': ('Live dividend estimation for the board', 'Anggaran dividen secara langsung untuk lembaga'),
  'k6': ('Angkasa salary deduction integration', 'Integrasi potongan gaji Angkasa'),
  'k7': ('Online payment by FPX', 'Bayaran dalam talian melalui FPX'),
  'k8': ('Member app in BM, English and Tamil', 'Aplikasi ahli dalam BM, Inggeris dan Tamil'),
  'k9': ('Support desk, announcements and audit trail', 'Meja bantuan, pengumuman dan jejak audit'),

  'div.h': ('Try the dividend estimator', 'Cuba anggaran dividen'),
  'div.p': ('Move the rate and watch the payout change. In the platform the same estimate runs on each member\'s actual share balance, so the board decides faster.',
            'Gerakkan kadar dan lihat bayaran berubah. Dalam platform, anggaran yang sama dikira berdasarkan baki syer sebenar setiap ahli, supaya lembaga membuat keputusan lebih pantas.'),
  'div.capital': ('Total share capital (RM)', 'Jumlah modal syer (RM)'),
  'div.members': ('Number of members', 'Bilangan ahli'),
  'div.rate': ('Dividend rate', 'Kadar dividen'),
  'div.total': ('Total dividend payout', 'Jumlah bayaran dividen'),
  'div.avg': ('Average per member', 'Purata setiap ahli'),
  'div.compare': ('Compare rates', 'Bandingkan kadar'),
  'div.note': ('Example figures for illustration.', 'Angka contoh untuk ilustrasi.'),


  'contact.h': ('Let\'s talk about your operations', 'Mari berbincang tentang operasi anda'),
  'contact.p': ('A 30-minute conversation is usually enough to scope where automation pays off first.', 'Perbualan selama 30 minit biasanya mencukupi untuk mengenal pasti di mana automasi memberi pulangan terlebih dahulu.'),
  'c.email': ('Email', 'E-mel'), 'c.phone': ('Phone', 'Telefon'), 'c.office': ('Office', 'Pejabat'),
  'form.name': ('Your name', 'Nama anda'), 'form.org': ('Organisation', 'Organisasi'),
  'form.email': ('Email', 'E-mel'), 'form.phone': ('Phone (optional)', 'Telefon (pilihan)'),
  'form.msg': ('Which process would you like to automate?', 'Proses mana yang ingin anda automasikan?'),
  'form.ph': ('For example: loan approvals on paper, claims tracked in Excel, member records in files', 'Contoh: kelulusan pinjaman di atas kertas, tuntutan dijejak dalam Excel, rekod ahli dalam fail'),
  'form.send': ('Email us', 'E-mel kami'),
  'form.note': ('This opens your email app with the details filled in. Nothing is stored on this website.',
                'Ini membuka aplikasi e-mel anda dengan butiran telah diisi. Tiada maklumat disimpan di laman web ini.'),
  'form.err': ('Please add your name, a valid email and your message.', 'Sila isi nama, e-mel yang sah dan mesej anda.'),
  'foot.tag': ('Digital platforms and business process automation for SMEs and financial services', 'Platform digital dan automasi proses perniagaan untuk PKS dan perkhidmatan kewangan'),
}

def tx(key, tag='span', attrs=''):
    return f'<{tag} data-i18n="{key}"{(" " + attrs) if attrs else ""}>{T[key][0]}</{tag}>'

NAVY, BRONZE = '#16213e', '#a8762c'
LOGO_MARK = (f'<svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="{NAVY}"/>'
             f'<path d="M9 26 Q20 10 31 14" fill="none" stroke="#c99a4b" stroke-width="3.4" stroke-linecap="round"/><path d="M27 11.5 l5 2.5 l-3.5 4" fill="none" stroke="#c99a4b" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>'
             '<circle cx="12" cy="31" r="3" fill="#c99a4b"/><circle cx="20" cy="29.5" r="3" fill="#ffffff"/><circle cx="28" cy="31" r="3" fill="#c99a4b"/></svg>')

def logo(cls='brand'):
    return (f'<a class="{cls}" href="/" aria-label="DDP Management home">{LOGO_MARK}'
            f'<span class="word"><b>DDP Management</b><small data-i18n="brand.tag">{T["brand.tag"][0]}</small></span></a>')

ICONS = {
  'v1': '<circle cx="8" cy="8" r="3"/><circle cx="16" cy="9" r="2.5"/><path d="M3 19a5 5 0 0 1 10 0M13 19a4 4 0 0 1 8 0"/>',
  'v2': '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="12" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M8.5 6H12a3 3 0 0 1 3 3v.5M8.5 18H12a3 3 0 0 0 3-3v-.5"/>',
  'v3': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4M7 9l2 2 4-4"/>',
  'v4': '<path d="M4 12a8 8 0 0 1 16 0v4a2 2 0 0 1-2 2h-1v-6h3M4 12v4a2 2 0 0 0 2 2h1v-6H4"/>',
  'v5': '<path d="M4 4h7v7H4zM13 13h7v7h-7z"/><path d="M15 4h5v5M9 20H4v-5M20 4l-6 6M4 20l6-6"/>',
  'w1': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12h18"/>',
  'w2': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
  'w3': '<circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M2 20a6 6 0 0 1 12 0M10 20a6 6 0 0 1 12 0"/>',
  'w4': '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
}
def icon(k, cls='ico'):
    return f'<svg viewBox="0 0 24 24" class="{cls}" aria-hidden="true">{ICONS[k]}</svg>'

slides = [('s1', scene_loan()), ('s2', scene_members()), ('s3', scene_payments()), ('s4', scene_dividend())]
slides_html = ''.join(f"""
      <div class="slide{' active' if i == 0 else ''}" data-slide="{i}" aria-roledescription="slide" aria-label="{i+1} / {len(slides)}"{'' if i == 0 else ' aria-hidden="true"'}>
        <div class="wrap slide-grid">
          <div class="slide-text">
            {tx(k + '.h', 'h1' if i == 0 else 'h2', 'class="slide-h"')}
            {tx(k + '.p', 'p', 'class="slide-p"')}
            <div class="cta"><a class="btn big gold" href="#contact" data-i18n="cta.talk">{T['cta.talk'][0]}</a><a class="btn big ghost" href="#services" data-i18n="cta.services">{T['cta.services'][0]}</a></div>
          </div>
          <div class="slide-art">{brand(art)}</div>
        </div>
      </div>""" for i, (k, art) in enumerate(slides))

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title data-i18n="title">{T['title'][0]}</title>
  <meta name="description" content="{T['desc'][0]}">
  <link rel="canonical" href="https://ddpm.com.my/">
  <meta property="og:type" content="website"><meta property="og:url" content="https://ddpm.com.my/">
  <meta property="og:title" content="{T['title'][0]}"><meta property="og:description" content="{T['desc'][0]}">
  <meta name="theme-color" content="#16213e">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preload" href="/assets/fonts/source-serif-4-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="top">
    <div class="wrap bar">
      {logo()}
      <button class="menu" type="button" aria-expanded="false" aria-controls="nav" data-i18n="menu">Menu</button>
      <nav id="nav" aria-label="Main">
        <a href="#services" data-i18n="nav.services">{T['nav.services'][0]}</a>
        <a href="#koperasi" data-i18n="nav.koperasi">{T['nav.koperasi'][0]}</a>
        <a href="#how" data-i18n="nav.how">{T['nav.how'][0]}</a>
        <a href="#contact" data-i18n="nav.contact">{T['nav.contact'][0]}</a>
        <div class="lang" role="group" aria-label="Language"><button type="button" data-lang="ms" lang="ms">BM</button><button type="button" data-lang="en" lang="en" aria-pressed="true">EN</button></div>
        <a class="btn" href="#contact" data-i18n="cta.talk">{T['cta.talk'][0]}</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="hero" aria-roledescription="carousel" aria-label="DDP Management">
      <div class="slides" id="slides">{slides_html}
      </div>
      <div class="wrap controls">
        <button type="button" class="ctl" id="prev" data-i18n-label="slide.prev" aria-label="{T['slide.prev'][0]}"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
        <div class="dots" id="dots">{''.join(f'<button type="button" class="dot{" on" if i == 0 else ""}" data-go="{i}" data-i18n-label="slide.go" aria-label="{T["slide.go"][0]} {i+1}" aria-current="{"true" if i == 0 else "false"}"></button>' for i in range(len(slides)))}</div>
        <button type="button" class="ctl" id="next" data-i18n-label="slide.next" aria-label="{T['slide.next'][0]}"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
        <button type="button" class="ctl" id="pause" data-i18n-label="slide.pause" aria-label="{T['slide.pause'][0]}" aria-pressed="false"><svg viewBox="0 0 24 24" class="i-pause"><path d="M9 6v12M15 6v12"/></svg><svg viewBox="0 0 24 24" class="i-play"><path d="M8 5l11 7-11 7z"/></svg></button>
      </div>
    </section>

    <section class="results" aria-label="Results">
      <div class="wrap results-grid">
        <div class="stat"><b>100+</b>{tx('stat1', 'span')}</div>
        <div class="stat"><b>RM1M+</b>{tx('stat2', 'span')}</div>
        {tx('stat3', 'p', 'class="stat-note"')}
      </div>
    </section>

    <section id="services" class="band">
      <div class="wrap">
        <div class="head">{tx('svc.h', 'h2')}{tx('svc.p', 'p')}</div>
        <ul class="services">
          {''.join(f'<li>{icon(k, "sico")}<h3 data-i18n="{k}.h">{T[k + ".h"][0]}</h3>{tx(k + ".p", "p")}</li>' for k in ['v1', 'v2', 'v3', 'v4', 'v5'])}
        </ul>
      </div>
    </section>

    <section class="band soft">
      <div class="wrap">
        <div class="head">{tx('who.h', 'h2')}</div>
        <div class="who">{''.join(f'<div class="who-card">{icon("w" + str(i), "wico")}{tx(f"who.{i}h", "h3")}{tx(f"who.{i}p", "p")}</div>' for i in range(1, 5))}</div>
      </div>
    </section>

    <section id="how" class="band">
      <div class="wrap">
        <aside class="why">{tx('why.h', 'h2')}{tx('why.p', 'p')}</aside>
        <div class="head" style="margin-top:3.5rem">{tx('how.h', 'h2')}</div>
        <ol class="steps">{''.join(f'<li>{tx(f"how.{i}h", "h3")}{tx(f"how.{i}p", "p")}</li>' for i in range(1, 5))}</ol>
      </div>
    </section>

    <section id="koperasi" class="band soft">
      <div class="wrap">
        <div class="head">{tx('kp.h', 'h2')}{tx('kp.p', 'p')}</div>
        <ul class="modules">{''.join(f'<li>{tx(f"k{i}")}</li>' for i in range(1, 10))}</ul>
      </div>
    </section>

    <section id="dividend" class="band dark">
      <div class="wrap div-grid">
        <div>{tx('div.h', 'h2')}{tx('div.p', 'p', 'class="lede"')}
          <div class="calc-in">
            <div class="field"><label for="d-cap" data-i18n="div.capital">{T['div.capital'][0]}</label><input id="d-cap" type="text" inputmode="numeric" value="9,842,600"></div>
            <div class="field"><label for="d-mem" data-i18n="div.members">{T['div.members'][0]}</label><input id="d-mem" type="text" inputmode="numeric" value="1,204"></div>
            <div class="field wide"><label for="d-rate"><span data-i18n="div.rate">{T['div.rate'][0]}</span> <output id="d-rate-out" for="d-rate">5.50%</output></label>
              <input id="d-rate" type="range" min="0" max="12" step="0.25" value="5.5"></div>
          </div>
        </div>
        <div class="calc-out" aria-live="polite">
          <div class="big"><span data-i18n="div.total">{T['div.total'][0]}</span><b id="d-total">RM 541,343.00</b></div>
          <div class="small-out"><span data-i18n="div.avg">{T['div.avg'][0]}</span><b id="d-avg">RM 449.62</b></div>
          <div class="compare">{tx('div.compare', 'h3')}<div class="bars" id="d-bars"></div></div>
          {tx('div.note', 'p', 'class="note"')}
        </div>
      </div>
    </section>

    <section id="contact" class="band contact">
      <div class="wrap contact-grid">
        <div>{tx('contact.h', 'h2')}{tx('contact.p', 'p')}
          <dl class="reach">
            <dt data-i18n="c.email">Email</dt><dd><a href="mailto:Kumaravel@ddpm.com.my">Kumaravel@ddpm.com.my</a></dd>
            <dt data-i18n="c.phone">Phone</dt><dd><a href="tel:+60126915794">+60 12-691 5794</a></dd>
            <dt data-i18n="c.office">Office</dt><dd>No 14, Jalan Berlian 14,<br>Taman Berlian SG, Jelok,<br>43000 Kajang, Selangor, Malaysia</dd>
          </dl>
        </div>
        <form class="enquiry" id="enquiry" novalidate>
          <div class="field"><label for="q-name" data-i18n="form.name">{T['form.name'][0]}</label><input id="q-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="q-org" data-i18n="form.org">{T['form.org'][0]}</label><input id="q-org" name="org" autocomplete="organization"></div>
          <div class="field"><label for="q-email" data-i18n="form.email">{T['form.email'][0]}</label><input id="q-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="q-phone" data-i18n="form.phone">{T['form.phone'][0]}</label><input id="q-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field wide"><label for="q-msg" data-i18n="form.msg">{T['form.msg'][0]}</label><textarea id="q-msg" name="message" rows="4" required data-i18n-ph="form.ph" placeholder="{T['form.ph'][0]}"></textarea></div>
          <p class="err" id="q-err" role="alert" hidden data-i18n="form.err">{T['form.err'][0]}</p>
          <div class="wide"><button class="btn big gold" type="submit" data-i18n="form.send">{T['form.send'][0]}</button>{tx('form.note', 'p', 'class="small"')}</div>
        </form>
      </div>
    </section>
  </main>

  <footer class="foot">
    <div class="wrap foot-grid">
      <div>{logo('brand light')}{tx('foot.tag', 'p')}</div>
      <nav aria-label="Footer"><a href="#services" data-i18n="nav.services">{T['nav.services'][0]}</a><a href="#koperasi" data-i18n="nav.koperasi">{T['nav.koperasi'][0]}</a><a href="#how" data-i18n="nav.how">{T['nav.how'][0]}</a><a href="#contact" data-i18n="nav.contact">{T['nav.contact'][0]}</a></nav>
      <p class="copy">© <span id="year">2026</span> DDP Management</p>
    </div>
  </footer>
  <script src="/assets/i18n.js" defer></script>
  <script src="/assets/site.js" defer></script>
</body>
</html>
"""
open(os.path.join(ROOT, 'site/index.html'), 'w', encoding='utf-8').write(html)
js = 'window.DDPM_TEXT = ' + json.dumps({k: {'en': v[0], 'ms': v[1]} for k, v in T.items()}, ensure_ascii=False, indent=0) + ';\n'
open(os.path.join(ROOT, 'site/assets/i18n.js'), 'w', encoding='utf-8').write(js)
open(os.path.join(ROOT, 'site/favicon.svg'), 'w', encoding='utf-8').write(LOGO_MARK.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
missing = [k for k in re.findall(r'data-i18n(?:-label|-ph)?="([^"]+)"', html) if k not in T]
print('built', len(html), 'bytes; missing keys:', missing)

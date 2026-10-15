"""Builds site/index.html and site/assets/i18n.js for the DDP Management website.
Text lives in T below as (English, Bahasa Melayu). Run: python build/build.py"""
import json, os, re
from art import scene_members, scene_dividend, scene_loan, avatar

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T = {
  'title': ('DDP Management: koperasi systems for Malaysia', 'DDP Management: sistem koperasi untuk Malaysia'),
  'desc': ('DDP Management helps Malaysian koperasi go digital: member management, online loan applications, live dividend estimates and one app for every member.',
           'DDP Management membantu koperasi di Malaysia beralih ke digital: pengurusan ahli, permohonan pinjaman dalam talian, anggaran dividen secara langsung dan satu aplikasi untuk semua ahli.'),
  'nav.solutions': ('Solutions', 'Penyelesaian'),
  'nav.dividend': ('Dividend estimator', 'Anggaran dividen'),
  'nav.how': ('How it works', 'Cara ia berfungsi'),
  'nav.contact': ('Contact', 'Hubungi'),
  'cta.demo': ('Book a free demo', 'Tempah demo percuma'),
  'cta.how': ('See how it works', 'Lihat cara ia berfungsi'),
  'menu': ('Menu', 'Menu'),

  's1.h': ('Every member, one koperasi app', 'Semua ahli, satu aplikasi koperasi'),
  's1.p': ('Members check their membership, apply for loans and read announcements on their phone. Your office sees everything in one place.',
           'Ahli menyemak keahlian, memohon pinjaman dan membaca pengumuman di telefon. Pejabat anda melihat semuanya di satu tempat.'),
  's2.h': ('See the dividend before the meeting', 'Lihat dividen sebelum mesyuarat'),
  's2.p': ('Live dividend estimates let the board compare rates in minutes and decide with confidence.',
           'Anggaran dividen secara langsung membolehkan lembaga membandingkan kadar dalam beberapa minit dan membuat keputusan dengan yakin.'),
  's3.h': ('Loan applications without the paperwork', 'Permohonan pinjaman tanpa kertas'),
  's3.p': ('Members apply online, staff review and approve, and everyone can follow the status as it moves.',
           'Ahli memohon dalam talian, kakitangan menyemak dan meluluskan, dan semua orang boleh mengikuti status permohonan.'),
  'slide.prev': ('Previous slide', 'Slaid sebelumnya'),
  'slide.next': ('Next slide', 'Slaid seterusnya'),
  'slide.pause': ('Pause slides', 'Jeda slaid'),
  'slide.play': ('Play slides', 'Main slaid'),
  'slide.go': ('Show slide', 'Tunjuk slaid'),

  'mission': ('Our goal is simple: every koperasi in Malaysia, digital, so members are served faster and boards decide with real numbers.',
              'Matlamat kami mudah: setiap koperasi di Malaysia menjadi digital, supaya ahli dilayan lebih pantas dan lembaga membuat keputusan berdasarkan angka sebenar.'),

  'sol.h': ('Everything your koperasi runs on, in one system', 'Semua keperluan koperasi anda, dalam satu sistem'),
  'sol.p': ('Built for how Malaysian koperasi really work, including the paper forms that still come into the office.',
            'Dibina mengikut cara koperasi di Malaysia bekerja, termasuk borang kertas yang masih diterima di pejabat.'),
  'f1.h': ('Easy member management', 'Pengurusan ahli mudah'),
  'f1.p': ('Register members online or from paper forms. Keep IC, employer, bank details, nominees and status in one record, and find anyone in seconds.',
           'Daftar ahli dalam talian atau daripada borang kertas. Simpan IC, majikan, maklumat bank, penama dan status dalam satu rekod, dan cari sesiapa sahaja dalam beberapa saat.'),
  'f2.h': ('Easy loan applications', 'Permohonan pinjaman mudah'),
  'f2.p': ('Members apply from their phone; staff key in paper forms. Every application moves through review and approval with a clear record of who decided and why.',
           'Ahli memohon melalui telefon; kakitangan memasukkan borang kertas. Setiap permohonan melalui semakan dan kelulusan dengan rekod jelas siapa yang membuat keputusan dan sebabnya.'),
  'f3.h': ('Live dividend estimation', 'Anggaran dividen secara langsung'),
  'f3.p': ('Try different dividend rates on your real share balances and see the total payout and each member\'s dividend instantly. The board decides faster, with confidence.',
           'Cuba kadar dividen berbeza pada baki syer sebenar dan lihat jumlah bayaran serta dividen setiap ahli serta-merta. Lembaga membuat keputusan lebih pantas dan yakin.'),
  'f4.h': ('One app for every member', 'Satu aplikasi untuk semua ahli'),
  'f4.p': ('Web and mobile app in Bahasa Melayu, English and Tamil. Announcements reach every member, and help requests reach the right person in the office.',
           'Aplikasi web dan mudah alih dalam Bahasa Melayu, Inggeris dan Tamil. Pengumuman sampai kepada setiap ahli, dan permintaan bantuan sampai kepada orang yang betul di pejabat.'),
  'also.h': ('Also included', 'Turut disediakan'),
  'also.1': ('Announcements with notifications', 'Pengumuman dengan notifikasi'),
  'also.2': ('Member help desk and account unlock', 'Meja bantuan ahli dan buka kunci akaun'),
  'also.3': ('Staff roles and a full activity log', 'Peranan kakitangan dan log aktiviti penuh'),
  'also.4': ('Hosting in Malaysia with daily backups', 'Hos di Malaysia dengan sandaran harian'),
  'also.5': ('Request to leave, with open-loan checks', 'Permohonan berhenti, dengan semakan pinjaman tertunggak'),
  'also.6': ('Angkasa salary deductions (coming soon)', 'Potongan gaji Angkasa (akan datang)'),

  'div.h': ('Try the dividend estimator', 'Cuba anggaran dividen'),
  'div.p': ('Move the rate and watch the payout change. In the DDPM system the same estimate runs on each member\'s actual average share balance.',
            'Gerakkan kadar dan lihat bayaran berubah. Dalam sistem DDPM, anggaran yang sama dikira berdasarkan purata baki syer sebenar setiap ahli.'),
  'div.capital': ('Total share capital (RM)', 'Jumlah modal syer (RM)'),
  'div.members': ('Number of members', 'Bilangan ahli'),
  'div.rate': ('Dividend rate', 'Kadar dividen'),
  'div.total': ('Total dividend payout', 'Jumlah bayaran dividen'),
  'div.avg': ('Average per member', 'Purata setiap ahli'),
  'div.compare': ('Compare rates', 'Bandingkan kadar'),
  'div.note': ('Example figures for illustration.', 'Angka contoh untuk ilustrasi.'),

  'how.h': ('From paper to digital in four steps', 'Daripada kertas ke digital dalam empat langkah'),
  'how.1h': ('Free consultation', 'Konsultasi percuma'),
  'how.1p': ('We visit your koperasi, look at your forms and processes, and show you a working demo.',
             'Kami melawat koperasi anda, meneliti borang dan proses, dan menunjukkan demo sebenar.'),
  'how.2h': ('Set-up and data transfer', 'Persediaan dan pemindahan data'),
  'how.2p': ('We configure the system for your by-laws and move your member and loan records in.',
             'Kami menyediakan sistem mengikut undang-undang kecil anda dan memindahkan rekod ahli serta pinjaman.'),
  'how.3h': ('Training', 'Latihan'),
  'how.3p': ('Hands-on sessions for office staff and the board, plus simple guides for members.',
             'Sesi praktikal untuk kakitangan pejabat dan lembaga, serta panduan mudah untuk ahli.'),
  'how.4h': ('Go live with support', 'Mula guna dengan sokongan'),
  'how.4p': ('We launch alongside your paper process and stay with you with local support.',
             'Kami melancarkan sistem seiring dengan proses kertas anda dan terus memberi sokongan tempatan.'),

  'who.h': ('Made for everyone in the koperasi', 'Dibina untuk semua dalam koperasi'),
  'who.board.h': ('The board', 'Lembaga'),
  'who.board.p': ('Live figures on members, loans and dividends for faster, better-informed decisions.',
                  'Angka terkini tentang ahli, pinjaman dan dividen untuk keputusan yang lebih pantas dan tepat.'),
  'who.staff.h': ('Office staff', 'Kakitangan pejabat'),
  'who.staff.p': ('Less re-typing and chasing: one place for applications, approvals and member questions.',
                  'Kurang menaip semula dan mengejar dokumen: satu tempat untuk permohonan, kelulusan dan pertanyaan ahli.'),
  'who.member.h': ('Members', 'Ahli'),
  'who.member.p': ('Their membership, loans and koperasi news on their own phone, in their own language.',
                   'Keahlian, pinjaman dan berita koperasi di telefon sendiri, dalam bahasa sendiri.'),

  'case.h': ('Koperasi Guru-Guru Sekolah India Perak Berhad', 'Koperasi Guru-Guru Sekolah India Perak Berhad'),
  'case.p': ('A cooperative of more than 1,200 Tamil school teachers moved its membership, loans and member requests online, while the office keeps accepting paper forms.',
             'Sebuah koperasi dengan lebih 1,200 guru sekolah Tamil memindahkan keahlian, pinjaman dan permintaan ahli ke dalam talian, sementara pejabat masih menerima borang kertas.'),
  'case.label': ('Koperasi we serve', 'Koperasi yang kami bantu'),
  'case.1': ('Member portal, staff portal and public website', 'Portal ahli, portal kakitangan dan laman web awam'),
  'case.2': ('Bahasa Melayu, English and Tamil', 'Bahasa Melayu, Inggeris dan Tamil'),
  'case.3': ('Installable mobile app for members', 'Aplikasi mudah alih untuk ahli'),

  'contact.h': ('Let\'s digitalise your koperasi', 'Mari digitalkan koperasi anda'),
  'contact.p': ('Tell us about your koperasi and we will arrange a free demo at your office or online.',
                'Ceritakan tentang koperasi anda dan kami akan mengatur demo percuma di pejabat anda atau dalam talian.'),
  'c.email': ('Email', 'E-mel'), 'c.phone': ('Phone and WhatsApp', 'Telefon dan WhatsApp'), 'c.office': ('Office', 'Pejabat'),
  'form.name': ('Your name', 'Nama anda'), 'form.koperasi': ('Koperasi name', 'Nama koperasi'),
  'form.members': ('Number of members', 'Bilangan ahli'), 'form.email': ('Email', 'E-mel'),
  'form.msg': ('What would you like to improve?', 'Apa yang ingin anda perbaiki?'),
  'form.ph': ('For example: loan applications still on paper, dividend calculations in Excel', 'Contoh: permohonan pinjaman masih di atas kertas, pengiraan dividen dalam Excel'),
  'form.send': ('Email our team', 'E-mel pasukan kami'),
  'form.note': ('This opens your email app with the details filled in. Nothing is stored on this website.',
                'Ini membuka aplikasi e-mel anda dengan butiran telah diisi. Tiada maklumat disimpan di laman web ini.'),
  'form.err': ('Please add your name, a valid email and your message.', 'Sila isi nama, e-mel yang sah dan mesej anda.'),
  'foot.tag': ('Digitalising koperasi across Malaysia', 'Mendigitalkan koperasi di seluruh Malaysia'),
}

def tx(key, tag='span', attrs=''):
    return f'<{tag} data-i18n="{key}"{(" " + attrs) if attrs else ""}>{T[key][0]}</{tag}>'

LOGO_MARK = ('<svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true"><rect width="40" height="40" rx="11" fill="#0c4a45"/>'
             '<path d="M9 25 Q20 9 31 13" fill="none" stroke="#f4b63f" stroke-width="3.6" stroke-linecap="round"/><path d="M27 10.5 l5 2.5 l-3.5 4" fill="none" stroke="#f4b63f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
             '<circle cx="12" cy="31" r="3.2" fill="#2fb36b"/><circle cx="20" cy="29" r="3.2" fill="#ffffff"/><circle cx="28" cy="31" r="3.2" fill="#2fb36b"/></svg>')

def logo(cls='brand'):
    return (f'<a class="{cls}" href="/" aria-label="DDP Management home">{LOGO_MARK}'
            f'<span class="word"><b>DDPM</b><small>DDP Management</small></span></a>')

ICONS = {
  'f1': '<path d="M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM3 19a5 5 0 0 1 10 0M11 19a5 5 0 0 1 10 0"/>',
  'f2': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/><path d="M14 17l2 2 3-4"/>',
  'f3': '<path d="M4 19V9M10 19V5M16 19v-7M3 21h18"/><path d="M14 7l3-3 3 3"/>',
  'f4': '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/><circle cx="4" cy="8" r="1.5"/><circle cx="20" cy="8" r="1.5"/><circle cx="4" cy="15" r="1.5"/><circle cx="20" cy="15" r="1.5"/>',
}
def icon(k):
    return f'<svg viewBox="0 0 24 24" class="ico" aria-hidden="true">{ICONS[k]}</svg>'

slides = [('s1', scene_members()), ('s2', scene_dividend()), ('s3', scene_loan())]
slides_html = ''.join(f'''
      <div class="slide{' active' if i == 0 else ''}" data-slide="{i}" aria-roledescription="slide" aria-label="{i+1} / 3"{'' if i == 0 else ' aria-hidden="true"'}>
        <div class="wrap slide-grid">
          <div class="slide-text">
            {tx(k + '.h', 'h1' if i == 0 else 'h2', 'class="slide-h"')}
            {tx(k + '.p', 'p', 'class="slide-p"')}
            <div class="cta"><a class="btn big gold" href="#contact" data-i18n="cta.demo">{T['cta.demo'][0]}</a><a class="btn big ghost" href="#how" data-i18n="cta.how">{T['cta.how'][0]}</a></div>
          </div>
          <div class="slide-art">{art}</div>
        </div>
      </div>''' for i, (k, art) in enumerate(slides))

html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title data-i18n="title">{T['title'][0]}</title>
  <meta name="description" content="{T['desc'][0]}">
  <link rel="canonical" href="https://ddpm.com.my/">
  <meta property="og:type" content="website"><meta property="og:url" content="https://ddpm.com.my/">
  <meta property="og:title" content="{T['title'][0]}"><meta property="og:description" content="{T['desc'][0]}">
  <meta name="theme-color" content="#0c4a45">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preload" href="/assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
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
        <a href="#solutions" data-i18n="nav.solutions">{T['nav.solutions'][0]}</a>
        <a href="#dividend" data-i18n="nav.dividend">{T['nav.dividend'][0]}</a>
        <a href="#how" data-i18n="nav.how">{T['nav.how'][0]}</a>
        <a href="#contact" data-i18n="nav.contact">{T['nav.contact'][0]}</a>
        <div class="lang" role="group" aria-label="Language"><button type="button" data-lang="ms" lang="ms">BM</button><button type="button" data-lang="en" lang="en" aria-pressed="true">EN</button></div>
        <a class="btn" href="#contact" data-i18n="cta.demo">{T['cta.demo'][0]}</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="hero" aria-roledescription="carousel" aria-label="DDPM">
      <div class="slides" id="slides">{slides_html}
      </div>
      <div class="wrap controls">
        <button type="button" class="ctl" id="prev" data-i18n-label="slide.prev" aria-label="{T['slide.prev'][0]}"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
        <div class="dots" id="dots">{''.join(f'<button type="button" class="dot{" on" if i == 0 else ""}" data-go="{i}" data-i18n-label="slide.go" aria-label="{T["slide.go"][0]} {i+1}" aria-current="{"true" if i == 0 else "false"}"></button>' for i in range(3))}</div>
        <button type="button" class="ctl" id="next" data-i18n-label="slide.next" aria-label="{T['slide.next'][0]}"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
        <button type="button" class="ctl" id="pause" data-i18n-label="slide.pause" aria-label="{T['slide.pause'][0]}" aria-pressed="false"><svg viewBox="0 0 24 24" class="i-pause"><path d="M9 6v12M15 6v12"/></svg><svg viewBox="0 0 24 24" class="i-play"><path d="M8 5l11 7-11 7z"/></svg></button>
      </div>
    </section>

    <section class="mission"><div class="wrap">{tx('mission', 'p')}</div></section>

    <section id="solutions" class="band">
      <div class="wrap">
        <div class="head">{tx('sol.h', 'h2')}{tx('sol.p', 'p')}</div>
        <div class="features">
          {''.join(f'<article class="feature" data-f="{k}"><div class="badge">{icon(k)}</div>{tx(k + ".h", "h3")}{tx(k + ".p", "p")}</article>' for k in ['f1', 'f2', 'f3', 'f4'])}
        </div>
        <div class="also">{tx('also.h', 'h3')}<ul>{''.join(f'<li>{tx(f"also.{i}")}</li>' for i in range(1, 7))}</ul></div>
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

    <section id="how" class="band">
      <div class="wrap">
        <div class="head">{tx('how.h', 'h2')}</div>
        <ol class="steps">{''.join(f'<li>{tx(f"how.{i}h", "h3")}{tx(f"how.{i}p", "p")}</li>' for i in range(1, 5))}</ol>
      </div>
    </section>

    <section class="band soft">
      <div class="wrap">
        <div class="head">{tx('who.h', 'h2')}</div>
        <div class="who">{''.join(f'<div class="person-card">{avatar(k)}<div>{tx(f"who.{k}.h", "h3")}{tx(f"who.{k}.p", "p")}</div></div>' for k in ['board', 'staff', 'member'])}</div>
      </div>
    </section>

    <section class="band">
      <div class="wrap case">
        <div>{tx('case.label', 'p', 'class="case-label"')}{tx('case.h', 'h2')}{tx('case.p', 'p')}</div>
        <ul class="ticks">{''.join(f'<li>{tx(f"case.{i}")}</li>' for i in range(1, 4))}</ul>
      </div>
    </section>

    <section id="contact" class="band contact">
      <div class="wrap contact-grid">
        <div>{tx('contact.h', 'h2')}{tx('contact.p', 'p')}
          <dl class="reach">
            <dt data-i18n="c.email">Email</dt><dd><a href="mailto:info@ddpm.com.my">info@ddpm.com.my</a></dd>
            <dt data-i18n="c.phone">Phone and WhatsApp</dt><dd>[+60 X-XXX XXXX]</dd>
            <dt data-i18n="c.office">Office</dt><dd>[Address], Malaysia</dd>
          </dl>
        </div>
        <form class="enquiry" id="enquiry" novalidate>
          <div class="field"><label for="q-name" data-i18n="form.name">{T['form.name'][0]}</label><input id="q-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="q-kop" data-i18n="form.koperasi">{T['form.koperasi'][0]}</label><input id="q-kop" name="koperasi" autocomplete="organization"></div>
          <div class="field"><label for="q-email" data-i18n="form.email">{T['form.email'][0]}</label><input id="q-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="q-mem" data-i18n="form.members">{T['form.members'][0]}</label><input id="q-mem" name="members" inputmode="numeric"></div>
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
      <nav aria-label="Footer"><a href="#solutions" data-i18n="nav.solutions">{T['nav.solutions'][0]}</a><a href="#dividend" data-i18n="nav.dividend">{T['nav.dividend'][0]}</a><a href="#how" data-i18n="nav.how">{T['nav.how'][0]}</a><a href="#contact" data-i18n="nav.contact">{T['nav.contact'][0]}</a></nav>
      <p class="copy">© <span id="year">2026</span> DDP Management</p>
    </div>
  </footer>
  <script src="/assets/i18n.js" defer></script>
  <script src="/assets/site.js" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, 'site/index.html'), 'w').write(html)
js = 'window.DDPM_TEXT = ' + json.dumps({k: {'en': v[0], 'ms': v[1]} for k, v in T.items()}, ensure_ascii=False, indent=0) + ';\n'
open(os.path.join(ROOT, 'site/assets/i18n.js'), 'w').write(js)
open(os.path.join(ROOT, 'site/favicon.svg'), 'w').write(LOGO_MARK.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
missing = [k for k in re.findall(r'data-i18n(?:-label|-ph)?="([^"]+)"', html) if k not in T]
print('built', len(html), 'bytes; missing keys:', missing)

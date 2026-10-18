"""Cartoon koperasi members and the three animated hero scenes, as inline SVG.
Animation is done in CSS (see site.css): it plays when a slide becomes active and
is switched off for visitors who prefer reduced motion."""

INK = '#16213e'
SKIN = {'light': '#f6d2b0', 'tan': '#e2ad7f', 'brown': '#c58658', 'deep': '#8d5634'}


def person(x, y, s=1.0, skin='tan', top='#2fb36b', bottom='#20403b', hair='short', hair_color='#2a1c14',
           extra=None, wave=False, point=False, from_x=0, delay=0.0, cls='walker'):
    """A friendly flat-style person standing with feet at (x, y)."""
    sk = SKIN[skin]
    p = []
    # legs and shoes (a long dress covers them)
    if extra != 'dress':
        p.append(f'<rect x="-13" y="-50" width="11" height="48" rx="5" fill="{bottom}"/><rect x="2" y="-50" width="11" height="48" rx="5" fill="{bottom}"/>')
        p.append(f'<ellipse cx="-8" cy="-2" rx="9" ry="4" fill="{INK}"/><ellipse cx="8" cy="-2" rx="9" ry="4" fill="{INK}"/>')
        p.append(f'<path d="M-23 -50 Q-25 -93 0 -96 Q25 -93 23 -50 Z" fill="{top}"/>')
    else:
        p.append(f'<ellipse cx="-7" cy="-2" rx="8" ry="4" fill="{INK}"/><ellipse cx="7" cy="-2" rx="8" ry="4" fill="{INK}"/>')
        p.append(f'<path d="M-23 -6 Q-27 -92 0 -96 Q27 -92 23 -6 Q0 0 -23 -6 Z" fill="{top}"/>')
    # arms
    if wave:
        p.append(f'<rect x="15" y="-128" width="10" height="40" rx="5" fill="{top}" transform="rotate(20 20 -90)" class="wave-arm"/>'
                 f'<circle cx="31" cy="-130" r="6" fill="{sk}" class="wave-arm"/>')
    elif point:
        p.append(f'<rect x="18" y="-96" width="10" height="38" rx="5" fill="{top}" transform="rotate(-62 23 -92)"/><circle cx="52" cy="-104" r="5.5" fill="{sk}"/>')
    else:
        p.append(f'<rect x="17" y="-92" width="10" height="40" rx="5" fill="{top}" transform="rotate(-8 22 -92)"/><circle cx="24" cy="-52" r="5.5" fill="{sk}"/>')
    p.append(f'<rect x="-27" y="-92" width="10" height="40" rx="5" fill="{top}" transform="rotate(8 -22 -92)"/><circle cx="-24" cy="-52" r="5.5" fill="{sk}"/>')
    # neck and head, with hair or headwear
    if hair == 'tudung':
        p.append(f'<path d="M-25 -88 Q-28 -140 0 -140 Q28 -140 25 -88 Q12 -80 0 -80 Q-12 -80 -25 -88 Z" fill="{hair_color}"/>')
        p.append(f'<ellipse cx="0" cy="-112" rx="12.5" ry="14" fill="{sk}"/>')
    else:
        if hair == 'long':
            p.append(f'<path d="M-19 -116 Q-22 -88 -10 -86 L10 -86 Q22 -88 19 -116 Z" fill="{hair_color}"/>')
        p.append(f'<rect x="-6" y="-100" width="12" height="8" fill="{sk}"/>')
        p.append(f'<circle cx="0" cy="-114" r="17" fill="{sk}"/>')
        cap = f'<path d="M-17.5 -114 Q-19 -134 0 -134 Q19 -134 17.5 -114 Q11 -126 0 -124 Q-11 -126 -17.5 -114 Z" fill="{hair_color}"/>'
        if hair in ('short', 'long', 'songkok', 'bun'):
            p.append(cap)
        if hair == 'bun':
            p.append(f'<circle cx="0" cy="-136" r="8" fill="{hair_color}"/>')
        if hair == 'songkok':
            p.append(f'<rect x="-15" y="-142" width="30" height="16" rx="3" fill="#1b1b2a"/>')
        if hair == 'grey':
            p.append(f'<path d="M-17.5 -112 Q-19 -132 0 -132 Q19 -132 17.5 -112 Q11 -122 0 -121 Q-11 -122 -17.5 -112 Z" fill="#d9dde0"/>')
    # face
    fy = -112
    p.append(f'<circle cx="-5.5" cy="{fy}" r="1.9" fill="{INK}"/><circle cx="5.5" cy="{fy}" r="1.9" fill="{INK}"/>')
    p.append(f'<path d="M-5 {fy+7} Q0 {fy+11} 5 {fy+7}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>')
    if extra == 'glasses':
        p.append(f'<g fill="none" stroke="{INK}" stroke-width="1.4"><circle cx="-6" cy="{fy}" r="5"/><circle cx="6" cy="{fy}" r="5"/><path d="M-1 {fy} h2"/></g>')
    inner = ''.join(p)
    style = f'--from:{from_x}px;--d:{delay}s'
    return f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}" style="{style}">{inner}</g></g>'


def coin(x, y, r=22, cls='', style=''):
    return (f'<g transform="translate({x} {y})"><g class="{cls}" style="{style}">'
            f'<ellipse cx="0" cy="5" rx="{r}" ry="{r*0.38:.1f}" fill="#c98a12"/>'
            f'<rect x="{-r}" y="0" width="{2*r}" height="5" fill="#c98a12"/>'
            f'<ellipse cx="0" cy="0" rx="{r}" ry="{r*0.38:.1f}" fill="#f4b63f"/>'
            f'<ellipse cx="0" cy="0" rx="{r*0.68:.1f}" ry="{r*0.24:.1f}" fill="none" stroke="#fbd77f" stroke-width="2"/></g></g>')


def big_coin(x, y, cls='', style=''):
    return (f'<g transform="translate({x} {y})"><g class="{cls}" style="{style}"><circle r="24" fill="#c98a12"/><circle r="21" fill="#f4b63f"/>'
            f'<circle r="16" fill="none" stroke="#fbd77f" stroke-width="2"/>'
            f'<text x="0" y="6" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="15" fill="#7a4f05">RM</text></g></g>')


def scene_members():
    """Slide 1: members walk in from both sides and gather around the koperasi app."""
    phone = (
        '<g class="pop" style="--d:.15s">'
        '<rect x="258" y="70" width="124" height="240" rx="22" fill="#0c4a45"/>'
        '<rect x="267" y="84" width="106" height="212" rx="12" fill="#ffffff"/>'
        '<rect x="267" y="84" width="106" height="34" rx="12" fill="#0c4a45"/><rect x="267" y="104" width="106" height="14" fill="#0c4a45"/>'
        '<circle cx="283" cy="101" r="8" fill="#f4b63f"/><rect x="296" y="97" width="44" height="8" rx="4" fill="#2fb36b"/>'
        '<rect x="276" y="128" width="88" height="54" rx="9" fill="#0c4a45"/><rect x="276" y="128" width="5" height="54" rx="2" fill="#f4b63f"/>'
        '<rect x="288" y="138" width="40" height="6" rx="3" fill="#7fd0a8"/><rect x="288" y="152" width="60" height="10" rx="4" fill="#f4b63f"/><rect x="288" y="168" width="34" height="5" rx="2.5" fill="#7fd0a8"/>'
        + ''.join(f'<circle cx="286" cy="{198+i*28}" r="8" fill="{c}"/><rect x="300" y="{193+i*28}" width="{w}" height="6" rx="3" fill="#d5e7e1"/><rect x="300" y="{203+i*28}" width="{w-18}" height="5" rx="2.5" fill="#e9f3ef"/>'
                  for i, (c, w) in enumerate([('#2fb36b', 58), ('#f4b63f', 50), ('#5aa9e6', 62)]))
        + '</g>'
    )
    bell = ('<g class="pop" style="--d:1.5s"><circle cx="384" cy="74" r="20" fill="#f4b63f"/>'
            '<path d="M376 80 h16 l-2 -3 v-6 a6 6 0 0 0 -12 0 v6 z" fill="#ffffff"/><circle cx="384" cy="83" r="2.3" fill="#ffffff"/></g>')
    links = ''.join(f'<path class="flow" d="{d}" style="--d:{1.2+i*0.1}s"/>' for i, d in enumerate([
        'M150 270 Q200 200 262 190', 'M215 300 Q240 260 262 240', 'M490 270 Q440 200 378 190', 'M425 300 Q400 260 378 240']))
    people = [
        person(150, 400, 1.0, 'tan', '#2fb36b', '#20403b', 'tudung', '#0c4a45', extra='dress', from_x=-300, delay=.2),
        person(215, 418, 1.08, 'brown', '#f4b63f', '#24324a', 'songkok', '#1a1a1a', from_x=-300, delay=.35),
        person(80, 425, .95, 'light', '#5aa9e6', '#2b3a55', 'grey', extra='glasses', from_x=-300, delay=.5),
        person(490, 405, 1.02, 'light', '#e7578a', '#24324a', 'long', '#1d1410', from_x=300, delay=.25),
        person(560, 420, 1.06, 'deep', '#0c4a45', '#3b3b3b', 'short', '#120c08', wave=True, from_x=300, delay=.4),
        person(425, 425, .98, 'brown', '#8a5cd6', '#20403b', 'bun', '#1d1410', extra='dress', from_x=300, delay=.55),
    ]
    bubbles = ('<g class="pop" style="--d:1.8s"><rect x="100" y="230" width="44" height="30" rx="10" fill="#ffffff" stroke="#cfe6dc"/>'
               '<path d="M112 244 l6 6 l12 -12" fill="none" stroke="#2fb36b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'
               '<g class="pop" style="--d:2s"><rect x="508" y="240" width="48" height="30" rx="10" fill="#ffffff" stroke="#cfe6dc"/>'
               '<text x="532" y="261" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="15" fill="#c98a12">RM</text></g>')
    return (f'<svg viewBox="0 0 640 450" class="scene" aria-hidden="true">'
            f'<circle cx="320" cy="240" r="200" fill="#dff3ea"/><ellipse cx="320" cy="425" rx="290" ry="18" fill="#cfe9de"/>'
            f'{links}{phone}{bell}{"".join(people)}{bubbles}</svg>')


def scene_dividend(tag='RM1M+'):
    """Slide 2: bars rise, the growth line draws, coins stack up, the committee looks on."""
    bars, heights = [], [60, 92, 118, 150, 196]
    for i, h in enumerate(heights):
        x = 236 + i * 52
        bars.append(f'<rect class="grow" style="--d:{.25+i*.18:.2f}s" x="{x}" y="{330-h}" width="36" height="{h}" rx="6" fill="{"#2fb36b" if i < 4 else "#f4b63f"}"/>')
    tops = ' '.join(f'{254+i*52},{330-h-18}' for i, h in enumerate(heights))
    line = f'<polyline class="draw" style="--d:1.2s" points="{tops}" fill="none" stroke="#0c4a45" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    arrow = f'<path class="pop" style="--d:2s" d="M{254+4*52-14} {330-196-30} l18 -4 l-6 17 z" fill="#0c4a45"/>'
    panel = ('<rect x="210" y="96" width="292" height="252" rx="20" fill="#ffffff" stroke="#d2e8df"/>'
             '<path d="M226 330 H488" stroke="#d2e8df" stroke-width="2"/>')
    stack = ''.join(coin(570, 330 - i * 13, 26, 'drop', f'--d:{.6+i*.22:.2f}s') for i in range(7))
    floaters = big_coin(150, 140, 'float', '--d:2.2s') + big_coin(540, 120, 'float', '--d:2.5s')
    tag = ('<g class="pop" style="--d:2.1s"><rect x="404" y="66" width="124" height="44" rx="12" fill="#0c4a45"/>'
           f'<text x="466" y="95" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="21" fill="#f4b63f">{tag}</text></g>')
    people = [
        person(100, 425, 1.05, 'brown', '#0c4a45', '#24324a', 'songkok', '#111', point=True, from_x=-260, delay=.2),
        person(160, 432, 1.0, 'tan', '#f4b63f', '#20403b', 'tudung', '#2fb36b', extra='dress', from_x=-260, delay=.35),
        person(615, 432, .96, 'deep', '#5aa9e6', '#2b3a55', 'grey', extra='glasses', from_x=260, delay=.3),
    ]
    return (f'<svg viewBox="0 0 640 450" class="scene" aria-hidden="true">'
            f'<circle cx="360" cy="230" r="205" fill="#fff4dc"/><ellipse cx="330" cy="430" rx="300" ry="18" fill="#f6e5bb"/>'
            f'{panel}{"".join(bars)}{line}{arrow}{tag}{stack}{floaters}{"".join(people)}</svg>')


def scene_loan():
    """Slide 3: the loan form fills in, each step ticks, approval pops with confetti."""
    phone = ('<rect x="150" y="80" width="130" height="250" rx="22" fill="#0c4a45"/><rect x="159" y="94" width="112" height="222" rx="12" fill="#ffffff"/>'
             '<rect x="171" y="108" width="60" height="9" rx="4.5" fill="#0c4a45"/>')
    fields = ''.join(f'<rect x="171" y="{134+i*36}" width="88" height="24" rx="6" fill="#eef6f2"/>'
                     f'<rect class="fill" style="--d:{.3+i*.25:.2f}s" x="178" y="{143+i*36}" width="{w}" height="6" rx="3" fill="#2fb36b"/>'
                     for i, w in enumerate([60, 44, 70, 52]))
    button = '<rect class="pop" style="--d:1.35s" x="171" y="284" width="88" height="22" rx="11" fill="#f4b63f"/>'
    card = '<rect x="318" y="118" width="210" height="196" rx="18" fill="#ffffff" stroke="#d2e8df"/>'
    steps = ''
    for i in range(3):
        y = 152 + i * 56
        steps += (f'<circle cx="350" cy="{y}" r="15" fill="#e7f5ee"/>'
                  f'<path class="tick" style="--d:{1.6+i*.45:.2f}s" d="M343 {y} l5 5 l10 -11" fill="none" stroke="#2fb36b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
                  f'<rect x="376" y="{y-9}" width="{110-i*12}" height="8" rx="4" fill="#cfe2da"/><rect x="376" y="{y+4}" width="{70-i*8}" height="6" rx="3" fill="#e5efea"/>')
        if i < 2:
            steps += f'<path d="M350 {y+16} v24" stroke="#d2e8df" stroke-width="3" stroke-dasharray="3 4"/>'
    badge = ('<g class="bounce" style="--d:3s"><circle cx="520" cy="112" r="34" fill="#2fb36b"/>'
             '<path d="M503 112 l11 11 l21 -23" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
    colors = ['#f4b63f', '#2fb36b', '#e7578a', '#5aa9e6', '#0c4a45', '#8a5cd6']
    confetti = ''.join(f'<rect class="confetti" style="--d:{3.05+(i%5)*.12:.2f}s;--x:{(i*37)%120-60}px" x="{440+(i*29)%170}" y="40" width="{6+i%3*2}" height="{10+i%2*4}" rx="2" fill="{colors[i%6]}"/>'
                       for i in range(16))
    people = [
        person(95, 430, 1.05, 'tan', '#e7578a', '#20403b', 'tudung', '#5aa9e6', extra='dress', wave=True, from_x=-240, delay=.2),
        person(590, 432, 1.0, 'light', '#0c4a45', '#24324a', 'short', '#1d1410', from_x=240, delay=.3),
    ]
    return (f'<svg viewBox="0 0 640 450" class="scene" aria-hidden="true">'
            f'<circle cx="330" cy="230" r="205" fill="#e6f1fb"/><ellipse cx="330" cy="430" rx="300" ry="18" fill="#d3e5f3"/>'
            f'{phone}{fields}{button}{card}{steps}{"".join(people)}{badge}{confetti}</svg>')


def avatar(kind):
    """Small static portraits for the 'who it is for' section."""
    p = {
        'board': person(0, 0, 1, 'brown', '#0c4a45', '#24324a', 'songkok', '#111', extra='glasses', cls='still'),
        'staff': person(0, 0, 1, 'tan', '#2fb36b', '#20403b', 'tudung', '#f4b63f', extra='dress', cls='still'),
        'member': person(0, 0, 1, 'deep', '#5aa9e6', '#2b3a55', 'short', '#120c08', wave=True, cls='still'),
    }[kind]
    return f'<svg viewBox="-50 -150 100 156" class="avatar" aria-hidden="true">{p}</svg>'


def scene_payments():
    """Slide: Angkasa deductions and online payments fly into the koperasi; the account updates and ticks."""
    # koperasi building (centre)
    bx, by = 320, 300
    building = (f'<g class="pop" style="--d:.1s">'
                f'<path d="M{bx-95} {by-120} L{bx} {by-178} L{bx+95} {by-120} Z" fill="#0c4a45"/>'
                f'<rect x="{bx-86}" y="{by-120}" width="172" height="120" fill="#ffffff" stroke="#cfe6dc" stroke-width="3"/>'
                + ''.join(f'<rect x="{bx-74+i*40}" y="{by-108}" width="16" height="96" rx="4" fill="#dff3ea"/>' for i in range(4))
                + f'<rect x="{bx-20}" y="{by-56}" width="40" height="56" rx="6" fill="#0c4a45"/>'
                f'<rect x="{bx-52}" y="{by-152}" width="104" height="20" rx="6" fill="#f4b63f"/>'
                f'<text x="{bx}" y="{by-137}" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="13" fill="#13302c">KOPERASI</text>'
                f'<rect x="{bx-110}" y="{by}" width="220" height="10" rx="4" fill="#0c4a45"/></g>')
    # Angkasa payslip (left)
    slip = ('<g class="pop" style="--d:.3s"><rect x="36" y="120" width="132" height="168" rx="14" fill="#ffffff" stroke="#d2e8df" stroke-width="2"/>'
            '<rect x="52" y="138" width="60" height="9" rx="4.5" fill="#0c4a45"/>'
            + ''.join(f'<rect x="52" y="{164+i*22}" width="{w}" height="7" rx="3.5" fill="#dbe8e3"/><rect x="{132}" y="{164+i*22}" width="20" height="7" rx="3.5" fill="#dbe8e3"/>' for i, w in enumerate([56, 44, 62]))
            + '<rect x="46" y="226" width="112" height="26" rx="8" fill="#fff1d1"/>'
            '<text x="56" y="244" font-family="Figtree, sans-serif" font-weight="800" font-size="12" fill="#a06b06">ANGKASA</text>'
            '<rect x="124" y="235" width="26" height="8" rx="4" fill="#f4b63f"/></g>')
    # phone paying online (right)
    phone = ('<g class="pop" style="--d:.45s"><rect x="486" y="96" width="112" height="206" rx="20" fill="#0c4a45"/><rect x="494" y="109" width="96" height="180" rx="11" fill="#ffffff"/>'
             '<rect x="504" y="122" width="44" height="8" rx="4" fill="#0c4a45"/>'
             '<text x="542" y="172" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="20" fill="#0c4a45">RM 250</text>'
             '<rect x="506" y="186" width="72" height="22" rx="7" fill="#eef6f2"/><circle cx="518" cy="197" r="6" fill="#5aa9e6"/><rect x="530" y="193" width="38" height="7" rx="3.5" fill="#cfe2da"/>'
             '<rect x="506" y="216" width="72" height="22" rx="7" fill="#eef6f2"/><circle cx="518" cy="227" r="6" fill="#e7578a"/><rect x="530" y="223" width="32" height="7" rx="3.5" fill="#cfe2da"/>'
             '<rect class="press" style="--d:1.1s" x="506" y="250" width="72" height="26" rx="13" fill="#2fb36b"/>'
             '<path d="M533 263 l5 5 l9 -10" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>')
    # coins flying in from both sides, then the account updates
    def flyer(x, y, tx, ty, d):
        return (f'<g transform="translate({x} {y})"><g class="fly" style="--d:{d:.2f}s;--tx:{tx}px;--ty:{ty}px">'
                f'<circle r="15" fill="#c98a12"/><circle r="12.5" fill="#f4b63f"/>'
                f'<text y="4.5" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="800" font-size="10" fill="#7a4f05">RM</text></g></g>')
    coins = ''.join(flyer(150, 238, bx - 40 - 150, by - 90 - 238, 1.0 + i * .28) for i in range(3)) + \
            ''.join(flyer(540, 262, bx + 40 - 540, by - 90 - 262, 1.35 + i * .28) for i in range(3))
    trails = ('<path class="flow" style="--d:.9s" d="M168 236 Q230 170 282 196"/>'
              '<path class="flow" style="--d:1.2s" d="M486 250 Q420 170 358 196"/>')
    ledger = ('<g class="pop" style="--d:2.4s"><rect x="250" y="20" width="140" height="62" rx="14" fill="#ffffff" stroke="#d2e8df" stroke-width="2"/>'
              '<rect x="264" y="34" width="54" height="7" rx="3.5" fill="#cfe2da"/>'
              '<rect class="fill" style="--d:2.6s" x="264" y="52" width="84" height="12" rx="6" fill="#2fb36b"/></g>'
              '<g class="bounce" style="--d:2.9s"><circle cx="380" cy="34" r="20" fill="#2fb36b"/>'
              '<path d="M370 34 l7 7 l13 -14" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>')
    people = [
        person(100, 430, 1.0, 'brown', '#5aa9e6', '#24324a', 'songkok', '#111', from_x=-240, delay=.2),
        person(560, 432, 1.0, 'tan', '#8a5cd6', '#20403b', 'tudung', '#f4b63f', extra='dress', wave=True, from_x=240, delay=.3),
    ]
    return (f'<svg viewBox="0 0 640 450" class="scene" aria-hidden="true">'
            f'<circle cx="320" cy="220" r="205" fill="#eaf6ef"/><ellipse cx="320" cy="430" rx="300" ry="18" fill="#d3eadf"/>'
            f'{trails}{building}{slip}{phone}{coins}{ledger}{"".join(people)}</svg>')


PAL = {'#0c4a45': '#16213e', '#dff3ea': '#efe9dd', '#cfe9de': '#e3dccd', '#eaf6ef': '#efe9dd', '#d3eadf': '#e3dccd', '#fff4dc': '#f6eedd', '#f6e5bb': '#eadcbc', '#e6f1fb': '#e8ecf4', '#d3e5f3': '#d9dfeb', '#7fd0a8': '#c8b48e', '#cfe6dc': '#e3dccd'}

def brand(svg):
    for a, b in PAL.items():
        svg = svg.replace(a, b)
    return svg

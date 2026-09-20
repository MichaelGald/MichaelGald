#!/usr/bin/env python3
"""Genera los SVG estáticos del perfil: banner, stack tecnológico y separador.

Uso:  python scripts/build_assets.py
Edita STACK abajo para cambiar las tecnologías y vuelve a ejecutar.
"""
from pathlib import Path

from common import MONO, SANS, css, esc

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

# --------------------------------------------------------------------------- #
# Stack tecnológico (edita aquí)
# --------------------------------------------------------------------------- #
STACK = [
    ("Backend", ["C#", ".NET", "ASP.NET Core", "Web API REST", "Entity Framework Core",
                 "Node.js", "Express", "OpenAPI", "Hangfire", "HL7 FHIR R4"]),
    ("Frontend", ["TypeScript", "JavaScript", "React", "Next.js", "Vite", "HTML5", "CSS3",
                  "TanStack Query", "Zustand", "Vitest"]),
    ("Datos", ["PostgreSQL", "SQL Server", "MongoDB", "Modelado relacional",
               "Optimización de consultas"]),
    ("UI y móvil", ["Tailwind CSS", "shadcn/ui", "Ant Design", "React Native",
                    "React Native Reusables", "Figma", "Canva"]),
    ("Seguridad e identidad", ["Keycloak", "OpenID Connect", "JWT", "RBAC", "Pentesting",
                               "Hydra", "Análisis de malware"]),
    ("DevOps y sistemas", ["Docker", "Docker Compose", "Nginx", "Git", "OpenTelemetry",
                           "Tailscale VPN", "Linux", "Arch / CachyOS"]),
    ("Hardware, redes y modelado", ["Arduino UNO", "Sensores ultrasónicos", "AutoCAD",
                                    "Cisco Packet Tracer"]),
]


# --------------------------------------------------------------------------- #
# Banner
# --------------------------------------------------------------------------- #
def banner() -> str:
    W, H = 1000, 260
    code = [
        [("kw", "const "), ("vr", "michael"), ("txt", " = {")],
        [("txt", "  rol: "), ("st", '"Full-Stack Developer"'), ("txt", ",")],
        [("txt", "  backend: ["), ("st", '".NET"'), ("txt", ", "), ("st", '"Node.js"'), ("txt", "],")],
        [("txt", "  frontend: ["), ("st", '"React"'), ("txt", ", "), ("st", '"Next.js"'), ("txt", "],")],
        [("txt", "  enfoque: "), ("st", '"arquitectura + seguridad"'), ("txt", ",")],
        [("txt", "};")],
    ]
    lines = []
    y0 = 113
    for i, line in enumerate(code):
        spans = "".join(f'<tspan class="{c}">{esc(t)}</tspan>' for c, t in line)
        lines.append(f'<text x="612" y="{y0 + i * 22}" xml:space="preserve">{spans}</text>')
    cursor_y = y0 + 5 * 22
    extra = "@keyframes b{0%,49%{opacity:1}50%,100%{opacity:0}}.cur{animation:b 1.1s steps(1) infinite}"
    nl = "\n"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">Michael Galdámez, Desarrollador Full-Stack</title>
{css(extra)}
<defs>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" class="dot"/></pattern>
  <radialGradient id="glow" cx="0" cy="0" r="1" gradientTransform="translate(120 0) scale(620 330)" gradientUnits="userSpaceOnUse">
    <stop offset="0" class="gs" stop-opacity="0.30"/><stop offset="1" class="gs" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" class="bg"/>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" class="ln"/>

<text x="56" y="82" class="acc" font-family="{MONO}" font-size="13" letter-spacing="2">DESARROLLADOR FULL-STACK</text>
<text x="56" y="132" class="txt" font-family="{SANS}" font-size="46" font-weight="700" letter-spacing="-0.5">Michael Galdámez</text>
<text x="56" y="168" class="mut" font-family="{SANS}" font-size="18">APIs con .NET · Aplicaciones con React · Ciberseguridad</text>
<rect x="56" y="195" width="40" height="2" rx="1" class="acc"/>
<text x="56" y="224" class="mut" font-family="{SANS}" font-size="14">San Pedro Sula, Honduras  ·  Ingeniería en Sistemas, UNAH-CUROC</text>

<rect x="588" y="42" width="376" height="176" rx="10" class="win"/>
<path d="M588 52a10 10 0 0 1 10-10h356a10 10 0 0 1 10 10v22H588z" class="bar"/>
<line x1="588" y1="74" x2="964" y2="74" class="ln"/>
<circle cx="608" cy="58" r="5" fill="#ff5f56"/><circle cx="626" cy="58" r="5" fill="#ffbd2e"/><circle cx="644" cy="58" r="5" fill="#27c93f"/>
<text x="776" y="62" class="mut" font-family="{MONO}" font-size="11" text-anchor="middle">perfil.ts</text>
<g font-family="{MONO}" font-size="13">
{nl.join(lines)}
<rect x="{612 + 3 * 7.8:.1f}" y="{cursor_y - 12}" width="7" height="15" class="acc cur"/>
</g>
</svg>"""


# --------------------------------------------------------------------------- #
# Stack tecnológico (chips con salto de línea automático)
# --------------------------------------------------------------------------- #
def stack() -> str:
    W, PAD, GAP = 1000, 20, 20
    CARD_W = (W - 2 * PAD - GAP) // 2
    CH, CG, CHAR, CPAD = 28, 8, 7.5, 12   # alto chip, separación, ancho por carácter, relleno

    def flow(items, inner):
        rows, cur, x = [], [], 0
        for it in items:
            w = round(len(it) * CHAR + 2 * CPAD)
            if cur and x + w > inner:
                rows.append(cur)
                cur, x = [], 0
            cur.append((it, x, w))
            x += w + CG
        if cur:
            rows.append(cur)
        return rows

    def height(rows):
        return 46 + len(rows) * (CH + CG) + 8

    # Filas de dos tarjetas con la misma altura; si sobra una, ocupa todo el ancho.
    layout, y = [], PAD
    i = 0
    while i < len(STACK):
        pair = STACK[i:i + 2]
        if len(pair) == 2:
            data = [(t, flow(it, CARD_W - 36)) for t, it in pair]
            h = max(height(r) for _, r in data)
            for ci, (t, rows) in enumerate(data):
                layout.append((PAD + ci * (CARD_W + GAP), y, CARD_W, h, t, rows))
        else:
            t, it = pair[0]
            full = W - 2 * PAD
            rows = flow(it, full - 36)
            h = height(rows)
            layout.append((PAD, y, full, h, t, rows))
        y += h + GAP
        i += 2
    H = y - GAP + PAD

    parts = []
    for cx, cy, cw, h, title, rows in layout:
        parts.append(f'<rect x="{cx+.5}" y="{cy+.5}" width="{cw-1}" height="{h-1}" rx="12" class="panel"/>')
        parts.append(f'<text x="{cx+18}" y="{cy+29}" class="mut" font-family="{MONO}" font-size="11" letter-spacing="1.6">{esc(title.upper())}</text>')
        parts.append(f'<rect x="{cx+cw-34}" y="{cy+22}" width="16" height="2" rx="1" class="acc"/>')
        for ri, row in enumerate(rows):
            ry = cy + 46 + ri * (CH + CG)
            for it, x, w in row:
                rx_ = cx + 18 + x
                parts.append(f'<rect x="{rx_+.5}" y="{ry+.5}" width="{w-1}" height="{CH-1}" rx="7" class="chip"/>')
                parts.append(f'<text x="{rx_ + w/2:.1f}" y="{ry+18}" class="txt" font-family="{MONO}" font-size="12.5" text-anchor="middle">{esc(it)}</text>')
    body = "\n".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">Stack tecnológico</title>
{css()}
{body}
</svg>"""


def divider() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="2" viewBox="0 0 1000 2" role="presentation">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#4493f8" stop-opacity="0"/><stop offset="0.5" stop-color="#4493f8" stop-opacity="0.7"/><stop offset="1" stop-color="#4493f8" stop-opacity="0"/></linearGradient></defs>
<rect width="1000" height="2" fill="url(#g)"/></svg>"""


if __name__ == "__main__":
    (OUT / "banner.svg").write_text(banner(), encoding="utf-8")
    (OUT / "stack.svg").write_text(stack(), encoding="utf-8")
    (OUT / "divider.svg").write_text(divider(), encoding="utf-8")
    print("SVG generados en", OUT)

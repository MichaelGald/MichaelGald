#!/usr/bin/env python3
"""Genera assets/stats.svg con datos reales de GitHub (sin servicios externos).

Uso:
    python scripts/update_stats.py               # consulta la API de GitHub
    python scripts/update_stats.py --placeholder # tarjeta vacía (sin red)

Variables de entorno (todas opcionales):
    GH_TOKEN          Token de GitHub. Con él se pueden leer las contribuciones (GraphQL)
                      y se evita el límite de peticiones anónimas.
    STATS_USER        Usuario a consultar (por defecto: dueño del repositorio o MichaelGald).
    INCLUDE_PRIVATE   "1" para contar también repos privados (requiere un PAT con scope `repo`
                      del propio usuario en GH_TOKEN).
"""
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from common import MONO, SANS, css, esc

OUT = Path(__file__).resolve().parent.parent / "assets" / "stats.svg"
USER = os.environ.get("STATS_USER") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "MichaelGald"
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
INCLUDE_PRIVATE = os.environ.get("INCLUDE_PRIVATE") == "1"

LANG_COLORS = {
    "C#": "#178600", "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "HTML": "#e34c26",
    "CSS": "#8957e5", "Python": "#3572a5", "Shell": "#89e051", "Dockerfile": "#384d54",
    "PLpgSQL": "#336790", "TSQL": "#e38c00", "C++": "#f34b7d", "C": "#7d8590",
    "Java": "#b07219", "Kotlin": "#a97bff", "Dart": "#00b4ab", "SCSS": "#c6538c",
}
FALLBACK = ["#4493f8", "#39d0d8", "#a371f7", "#f778ba", "#ffa657", "#7ee787"]


# --------------------------------------------------------------------------- #
# API
# --------------------------------------------------------------------------- #
def request(url: str, payload: dict | None = None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def rest(path: str):
    return request(f"https://api.github.com{path}")


def fetch() -> dict:
    user = rest(f"/users/{USER}")

    repos, page = [], 1
    while True:
        if INCLUDE_PRIVATE and TOKEN:
            batch = rest(f"/user/repos?affiliation=owner&visibility=all&per_page=100&page={page}")
        else:
            batch = rest(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]

    langs: dict[str, int] = {}
    for r in own[:80]:
        try:
            for name, size in rest(f"/repos/{r['full_name']}/languages").items():
                langs[name] = langs.get(name, 0) + size
        except urllib.error.HTTPError:
            continue

    contributions = None
    if TOKEN:
        q = ('query($u:String!){user(login:$u){contributionsCollection{'
             'contributionCalendar{totalContributions}}}}')
        try:
            res = request("https://api.github.com/graphql", {"query": q, "variables": {"u": USER}})
            contributions = res["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
        except Exception as exc:  # noqa: BLE001
            print("Aviso: no se pudieron leer las contribuciones:", exc, file=sys.stderr)

    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: kv[1], reverse=True)[:6]
    langs_out = []
    for i, (name, size) in enumerate(top):
        langs_out.append((name, size / total * 100, LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])))

    return {
        "repos": user["public_repos"] if not INCLUDE_PRIVATE else len(own),
        "stars": sum(r["stargazers_count"] for r in own),
        "contribs": contributions,
        "followers": user["followers"],
        "langs": langs_out,
        "updated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
    }


# --------------------------------------------------------------------------- #
# SVG
# --------------------------------------------------------------------------- #
def fmt(n) -> str:
    return "—" if n is None else f"{n:,}".replace(",", ".")


def render(d: dict) -> str:
    W, H = 1000, 282
    kpis = [
        (d["repos"], "Repositorios públicos"),
        (d["stars"], "Estrellas recibidas"),
        (d["contribs"], "Contribuciones (12 meses)"),
        (d["followers"], "Seguidores"),
    ]
    cells = []
    cw = (W - 40) / 4
    for i, (val, label) in enumerate(kpis):
        x = 20 + i * cw + 16
        cells.append(f'<text x="{x:.0f}" y="76" class="txt" font-family="{SANS}" font-size="34" font-weight="700">{fmt(val)}</text>')
        cells.append(f'<text x="{x:.0f}" y="100" class="mut" font-family="{SANS}" font-size="13">{esc(label)}</text>')
        if i:
            cells.append(f'<line x1="{20 + i * cw:.0f}" y1="44" x2="{20 + i * cw:.0f}" y2="104" class="ln"/>')

    BAR_X, BAR_W = 36, W - 72
    langs = d["langs"]
    bar, legend = [], []
    if langs:
        x = BAR_X
        norm = sum(p for _, p, _ in langs)
        for name, pct, color in langs:
            w = BAR_W * pct / norm
            bar.append(f'<rect x="{x:.1f}" y="176" width="{w:.1f}" height="10" fill="{color}"/>')
            x += w
        for i, (name, pct, color) in enumerate(langs):
            col, row = i % 3, i // 3
            lx = BAR_X + col * (BAR_W / 3)
            ly = 214 + row * 24
            legend.append(f'<circle cx="{lx + 5:.0f}" cy="{ly - 4}" r="5" fill="{color}"/>')
            legend.append(f'<text x="{lx + 18:.0f}" y="{ly}" class="txt" font-family="{SANS}" font-size="13">{esc(name)}</text>')
            legend.append(f'<text x="{lx + BAR_W / 3 - 24:.0f}" y="{ly}" class="mut" font-family="{MONO}" font-size="12" text-anchor="end">{pct / norm * 100:.1f}%</text>')
    else:
        legend.append(f'<text x="{BAR_X}" y="214" class="mut" font-family="{SANS}" font-size="13">Se completará automáticamente con la primera ejecución del workflow.</text>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">Actividad en GitHub de {esc(USER)}</title>
{css()}
<defs><clipPath id="bar"><rect x="{BAR_X}" y="176" width="{BAR_W}" height="10" rx="5"/></clipPath></defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" class="panel"/>
{chr(10).join(cells)}
<line x1="36" y1="126" x2="{W-36}" y2="126" class="ln"/>
<text x="36" y="156" class="mut" font-family="{MONO}" font-size="11" letter-spacing="1.6">LENGUAJES MÁS USADOS</text>
<rect x="{BAR_X}" y="176" width="{BAR_W}" height="10" rx="5" class="track"/>
<g clip-path="url(#bar)">{"".join(bar)}</g>
{chr(10).join(legend)}
<text x="{W-24}" y="{H-12}" class="mut" font-family="{MONO}" font-size="10" text-anchor="end" opacity="0.8">actualizado {esc(d["updated"])}</text>
</svg>"""


def main() -> int:
    if "--placeholder" in sys.argv:
        data = {"repos": None, "stars": None, "contribs": None, "followers": None,
                "langs": [], "updated": "pendiente"}
    else:
        try:
            data = fetch()
        except Exception as exc:  # noqa: BLE001
            print("Error consultando GitHub:", exc, file=sys.stderr)
            return 1
    OUT.write_text(render(data), encoding="utf-8")
    print("Escrito", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Paleta y utilidades compartidas por los generadores de SVG.

Cada clase CSS define su color para tema oscuro (por defecto) y para tema claro
(@media prefers-color-scheme), de modo que los SVG se ven bien en ambos modos.
"""

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SF Mono', 'Cascadia Code', Consolas, 'Liberation Mono', Menlo, monospace"

# clase: (estilo oscuro, estilo claro)
THEME = {
    "bg":    ("fill:#0d1117;stroke:#30363d", "fill:#ffffff;stroke:#d0d7de"),
    "panel": ("fill:#161b22;stroke:#30363d", "fill:#f6f8fa;stroke:#d0d7de"),
    "chip":  ("fill:#21262d;stroke:#30363d", "fill:#ffffff;stroke:#d0d7de"),
    "win":   ("fill:#010409;stroke:#30363d", "fill:#ffffff;stroke:#d0d7de"),
    "bar":   ("fill:#161b22", "fill:#f6f8fa"),
    "txt":   ("fill:#e6edf3", "fill:#1f2328"),
    "mut":   ("fill:#8b949e", "fill:#656d76"),
    "acc":   ("fill:#4493f8", "fill:#0969da"),
    "dot":   ("fill:#21262d", "fill:#d8dee4"),
    "kw":    ("fill:#ff7b72", "fill:#cf222e"),
    "vr":    ("fill:#79c0ff", "fill:#0550ae"),
    "st":    ("fill:#a5d6ff", "fill:#0a3069"),
    "track": ("fill:#21262d", "fill:#e6eaef"),
    "gs":    ("stop-color:#4493f8", "stop-color:#0969da"),
    "ln":    ("stroke:#30363d", "stroke:#d0d7de"),
}


def css(extra: str = "") -> str:
    dark = "".join(f".{k}{{{v[0]}}}" for k, v in THEME.items())
    light = "".join(f".{k}{{{v[1]}}}" for k, v in THEME.items())
    return f"<style>{dark}@media (prefers-color-scheme: light){{{light}}}{extra}</style>"


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

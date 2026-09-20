# Scripts del perfil

| Script | Qué hace | Cuándo ejecutarlo |
|---|---|---|
| `build_assets.py` | Genera `banner.svg`, `stack.svg` y `divider.svg` | Cuando cambies tu stack o el texto del banner (edita la lista `STACK`) |
| `update_stats.py` | Genera `stats.svg` con datos reales de la API de GitHub | Automático cada día con `.github/workflows/stats.yml` |

Solo usan la biblioteca estándar de Python 3.10+. No hay dependencias externas ni servicios de terceros.

# Hiroba brand asset provenance

## Authorization and source

On **2026-11-13**, the user authorized a Hiroba derivative of the **7K Group mark with a dark-green thematic tint**, following the Inari project-color adaptation approach. No Inari artwork, other source mark, or unrecorded adaptation is used.

Both SVGs come from public [`7K-Group/7k-design-system`](https://github.com/7K-Group/7k-design-system) at immutable commit `d94ed6b75b2a816d6e971732900dd11ab6ba2902`:

| Output | Exact source path | Source SHA-256 |
| --- | --- | --- |
| `icon-hiroba.svg` | `build/icons/icon-7kgroup.svg` | `4fe4139bc514b0b180aaad1be10852278d15bb985e83dbd98ce65bafcf663700` |
| `icon-hiroba-light.svg` | `build/icons/icon-7kgroup-light.svg` | `f02c839e9c7cc4799b4c75bfb17f6db4f0bb6846ddb842f484ed95cc7504391e` |

Machine-readable source hashes:

- `source_icon_dark_sha256`: `4fe4139bc514b0b180aaad1be10852278d15bb985e83dbd98ce65bafcf663700`
- `source_icon_light_sha256`: `f02c839e9c7cc4799b4c75bfb17f6db4f0bb6846ddb842f484ed95cc7504391e`

The source MIT copyright and permission notice is preserved in `THIRD_PARTY_LICENSE`.

## Exact SVG transformations

The transformation fetched each source with `gh api -H 'Accept: application/vnd.github.raw+json'` at the commit above and performed only these literal color substitutions:

| Output | Substitution | Unchanged paths/colors |
| --- | --- | --- |
| `icon-hiroba.svg` (dark color scheme) | `#FF35EB` → `#16A34A`; `#FF11F8` → `#15803D` | All path `d` geometry, IDs, transforms, XML structure, and `#FFFFFF` foreground paths |
| `icon-hiroba-light.svg` (light color scheme) | `#FF35EB` → `#166534`; `#FF11F8` → `#14532D` | All path `d` geometry, IDs, transforms, XML structure, and `#000000` foreground paths |

Each source color occurred exactly once. Equal-length replacements preserved the source byte length; no scripts, event handlers, remote resources, embedded credentials, or unrelated geometry were added. Relative-luminance checks recorded `#16A34A` on `#071A12` at 5.47:1, `#15803D` on `#071A12` at 3.59:1, `#166534` on white at 7.13:1, and `#14532D` on white at 9.11:1. The dark-green strokes meet the 3:1 non-text contrast objective on their intended backgrounds.

Output SVG hashes:

- `output_icon_dark_sha256`: `3dd13638ea059e7d21f3b2165318ca43ebcabccfa24133a2cb999d82fce15882`
- `output_icon_light_sha256`: `5dbda9c68d654b84c54218f5d57e58257e94a21922cc78e3753b85b218ff0464`

## PNG rendering

Render from the repository root with the committed `scripts/render_assets.py` (SHA-256 `6dd86efee45ed7514e5c75cfc0442585e23ac512cd5141ad85cd7fec9453cc25`):

```bash
pipx install 'cairosvg==2.7.1'
pipx inject cairosvg 'pillow==11.0.0'
$HOME/.local/pipx/venvs/cairosvg/bin/python scripts/render_assets.py
```

The script uses **cairosvg==2.7.1**, **pillow==11.0.0**, and the local Liberation Sans fonts below. It embeds no remote resource.

| Input/composition | Exact values |
| --- | --- |
| `avatar.png` | **512×512** RGB PNG; `#071A12` rounded square, radius 72; icon rasterized at 384×382 and composited at `(64,65)` |
| `social-preview.png` | **1280×640** RGB PNG; `#071A12` background; `#0B251A` panel at `(48,48,1232,592)`, radius 36, 4-pixel `#15803D` outline; icon rasterized at 352×350 and composited at `(96,145)` |
| Social text | `Hiroba` at `(520,190)`, Liberation Sans Bold 116 px; subtitle at `(526,326)`, Liberation Sans Regular 34 px; `PRE-V1 · APACHE-2.0` at `(526,394)`, Liberation Sans Regular 25 px |
| Font inputs | `/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf` SHA-256 `f8ace1f892b2bd9dc1792ba7f097fa7588f84fed48321480e04de5390828221f`; `/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf` SHA-256 `361c61b82d575c5c35fd9157fda8b0194bcfcd0d88ea8521a4fb5dd53d33dddc` |
| PNG encoding | Pillow `save(..., format="PNG", optimize=False)`; no timestamp or remote metadata added |

Output PNG hashes:

- `avatar_sha256`: `81eea065b1ed67985aa996a4ed0f4e2bd1fed0ec8372b248ad0a6d47041266be`
- `social_preview_sha256`: `2b2f559c6be12a0eb2e30110058ac77c363a880fa32f43fdcbb0e603d0e2d635`

The rendered avatar and social preview were inspected for cropping, legibility, and dark-green fidelity. They remain private repository assets. Organization avatar upload, repository social-preview upload, and public visibility require the separate A5 gate.

## License and trademark

The design-system source is MIT-licensed; see `THIRD_PARTY_LICENSE`. Asset licensing does **not** grant trademark rights. Hiroba, Inari, 7K, and related names and marks remain subject to their owners' trademark and brand rights. This derivative does not imply endorsement, registration, or filing completion.

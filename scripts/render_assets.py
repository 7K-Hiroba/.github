#!/usr/bin/env python3
"""Render Hiroba PNG assets. Requires cairosvg==2.7.1 and pillow==11.0.0."""

import io
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parents[1] / "profile" / "assets"
REGULAR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def raster_icon(width: int, height: int) -> Image.Image:
    data = cairosvg.svg2png(
        url=str(ASSETS / "icon-hiroba.svg"),
        output_width=width,
        output_height=height,
    )
    return Image.open(io.BytesIO(data)).convert("RGBA")


def render_avatar() -> None:
    avatar = Image.new("RGBA", (512, 512), "#071A12")
    mask = Image.new("L", (512, 512), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 511, 511), radius=72, fill=255)
    avatar.putalpha(mask)
    avatar.alpha_composite(raster_icon(384, 382), (64, 65))
    avatar.convert("RGB").save(ASSETS / "avatar.png", format="PNG", optimize=False)


def render_social_preview() -> None:
    social = Image.new("RGB", (1280, 640), "#071A12")
    draw = ImageDraw.Draw(social)
    draw.rounded_rectangle(
        (48, 48, 1232, 592), radius=36, fill="#0B251A", outline="#15803D", width=4
    )
    social.paste(raster_icon(352, 350), (96, 145), raster_icon(352, 350))
    draw.text((520, 190), "Hiroba", font=ImageFont.truetype(BOLD, 116), fill="#FFFFFF")
    draw.text(
        (526, 326),
        "Inari community extensions and assets",
        font=ImageFont.truetype(REGULAR, 34),
        fill="#D1E7DB",
    )
    draw.text(
        (526, 394),
        "PRE-V1 · APACHE-2.0",
        font=ImageFont.truetype(REGULAR, 25),
        fill="#A7C9B8",
    )
    social.save(ASSETS / "social-preview.png", format="PNG", optimize=False)


if __name__ == "__main__":
    render_avatar()
    render_social_preview()

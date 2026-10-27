#!/usr/bin/env python3
"""Reproduce the Vigil Render splash from the vendored VigilTech brand files (needs Pillow)."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
BRAND = HERE / 'amerika_render/vigiltech'
WALLPAPER = HERE.parent / 'brand/vigiltech/wallpaper-night.png'


def splash():
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1002, 564
    wp = Image.open(WALLPAPER).convert('RGB')
    scale = max(W / wp.width, H / wp.height)
    wp = wp.resize((round(wp.width * scale), round(wp.height * scale)), Image.Resampling.LANCZOS)
    image = wp.crop(((wp.width - W) // 2, (wp.height - H) // 2, (wp.width - W) // 2 + W, (wp.height - H) // 2 + H))
    draw = ImageDraw.Draw(image)
    # Solid night card behind all text so contrast never depends on the wallpaper.
    card = (231, 62, 771, 502)
    draw.rounded_rectangle(card, radius=22, fill='#120a14', outline='#4a3453', width=1)
    mark = Image.open(BRAND / 'logos/mark/vigiltech-mark-512.png').convert('RGBA').resize((128, 128), Image.Resampling.LANCZOS)
    image.paste(mark, ((W - 128) // 2, 92), mark)
    regular = lambda size: ImageFont.truetype(str(BRAND / 'fonts/VigilSans-Regular.ttf'), size)
    bold = ImageFont.truetype(str(BRAND / 'fonts/VigilSans-Bold.ttf'), 40)
    draw.text((W // 2, 246), 'Vigil Render', fill='#f6f1f4', font=bold, anchor='mt')
    draw.text((W // 2, 304), 'Describe a model and watch it appear.', fill='#cdbfca', font=regular(20), anchor='mt')
    draw.text((W // 2, 410), 'A product of VigilTech, vigiltech.org', fill='#f6f1f4', font=regular(16), anchor='mt')
    draw.text((W // 2, 440), 'Powered by Blender. Original upstream notices retained.', fill='#cdbfca', font=regular(14), anchor='mt')
    out = HERE / 'data/splash.png'
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out)
    return out


if __name__ == '__main__':
    print(splash())

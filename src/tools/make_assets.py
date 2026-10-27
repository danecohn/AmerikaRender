#!/usr/bin/env python3
"""Reproduce Cohnsoft Render SVG and splash from original, locally vendored assets."""
from pathlib import Path
import shutil
HERE = Path(__file__).resolve().parent.parent
BRAND = HERE / 'amerika_render/cohnsoft'
def icon():
    source = HERE.parent / 'brand/product-icons/render.svg'
    out = HERE / 'icons/amerika-render.svg'
    shutil.copyfile(source, out)
    return out
def splash():
    from PIL import Image, ImageDraw, ImageFont
    image = Image.new('RGB', (1002, 564), '#1c1c1e')
    mark = Image.open(BRAND / 'logos/mark/cohnsoft-mark-512.png').convert('RGBA')
    mark = mark.resize((168, 168), Image.Resampling.LANCZOS)
    image.paste(mark, ((1002-168)//2, 84), mark)
    draw = ImageDraw.Draw(image)
    regular = lambda size: ImageFont.truetype(str(BRAND / 'fonts/CohnSans-Regular.ttf'), size)
    bold = ImageFont.truetype(str(BRAND / 'fonts/CohnSans-Bold.ttf'), 42)
    draw.text((501, 290), 'Cohnsoft Render', fill='#f2f2f7', font=bold, anchor='mt')
    draw.text((501, 354), 'Make room for the next dimension.', fill='#b4b4bb', font=regular(23), anchor='mt')
    draw.text((501, 478), 'A product of Cohnsoft', fill='#f2f2f7', font=regular(16), anchor='mt')
    draw.text((501, 507), 'Powered by Blender. Original upstream notices retained.', fill='#b4b4bb', font=regular(13), anchor='mt')
    out = HERE / 'data/splash.png'
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out)
    return out
if __name__ == '__main__':
    print(icon())
    print(splash())

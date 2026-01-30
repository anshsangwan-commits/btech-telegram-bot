from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

FONT_PATH = os.path.join(
    os.path.dirname(__file__),
    "PatrickHandSC-Regular.ttf"   # <-- font name yahin match karo
)

def generate_image(topic, content):
    img = Image.new("RGB", (900, 1200), "#fffef8")  # notebook color
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_PATH, 48)
    body_font = ImageFont.truetype(FONT_PATH, 34)

    # Title
    draw.text((80, 60), topic, fill="black", font=title_font)
    draw.line((80, 120, 820, 120), fill="black", width=2)

    y = 150
    margin_x = 90

    wrapped = textwrap.wrap(content, width=40)

    for line in wrapped:
        draw.text((margin_x, y), "• " + line, fill="black", font=body_font)
        y += 45

    path = f"{topic}_handwritten.png"
    img.save(path)
    return path

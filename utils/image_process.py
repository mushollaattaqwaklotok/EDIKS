from PIL import Image, ImageDraw, ImageFont
import io

def process_image(uploaded_file, nama, harga, output_path):
    image = Image.open(io.BytesIO(uploaded_file.read())).convert("RGB")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()

    text = f"{nama}\nRp {harga:,}"
    draw.rectangle(
        [(0, image.height - 80), (image.width, image.height)],
        fill=(0, 0, 0)
    )
    draw.text(
        (10, image.height - 70),
        text,
        fill=(255, 255, 255),
        font=font
    )

    image.save(output_path)

import tempfile
from PIL import Image


def resize_image(input_file, content_type, width, height, keep_aspect_ratio):
    output = tempfile.SpooledTemporaryFile()   # ✅ no "with"

    image = Image.open(input_file)

    if keep_aspect_ratio:
        image.thumbnail((width, height))
    else:
        image = image.resize((width, height))

    # Convert if needed
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    format_map = {
        "image/jpeg": "JPEG",
        "image/png": "PNG",
        "image/webp": "WEBP"
    }

    image_format = format_map.get(content_type, "JPEG")

    image.save(
        output,
        format=image_format,
        optimize=True
    )

    output.seek(0)
    return output
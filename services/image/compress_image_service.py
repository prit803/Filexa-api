import tempfile
from PIL import Image


def compress_image(input_file, content_type, quality):
    output = tempfile.SpooledTemporaryFile()   # ❗ NO "with"

    image = Image.open(input_file)

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
        quality=quality,
        optimize=True
    )

    output.seek(0)
    return output
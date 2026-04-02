import tempfile
from PIL import Image


def rotate_image(input_file, content_type, angle):
    output = tempfile.SpooledTemporaryFile()

    image = Image.open(input_file)

    # ✅ Normalize angle (like iLovePDF behavior)
    angle = angle % 360

    # ✅ Rotate (expand=True prevents cropping)
    rotated = image.rotate(-angle, expand=True)

    # Handle transparency
    if rotated.mode in ("RGBA", "P"):
        rotated = rotated.convert("RGB")

    format_map = {
        "image/jpeg": "JPEG",
        "image/png": "PNG",
        "image/webp": "WEBP"
    }

    image_format = format_map.get(content_type, "JPEG")

    rotated.save(
        output,
        format=image_format,
        optimize=True
    )

    output.seek(0)
    return output
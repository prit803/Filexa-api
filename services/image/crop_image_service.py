import tempfile
from PIL import Image


def crop_image(input_file, content_type, left, top, right, bottom):
    import tempfile
    from PIL import Image

    output = tempfile.SpooledTemporaryFile()

    image = Image.open(input_file)
    width, height = image.size

    # ✅ Fix reversed values (IMPORTANT)
    if left > right:
        left, right = right, left

    if top > bottom:
        top, bottom = bottom, top

    # ✅ Clamp values
    left = max(0, left)
    top = max(0, top)
    right = min(width, right)
    bottom = min(height, bottom)

    # ❌ Only invalid if equal
    if left == right or top == bottom:
        raise ValueError("Crop area too small")

    cropped = image.crop((left, top, right, bottom))

    if cropped.mode in ("RGBA", "P"):
        cropped = cropped.convert("RGB")

    format_map = {
        "image/jpeg": "JPEG",
        "image/png": "PNG",
        "image/webp": "WEBP"
    }

    image_format = format_map.get(content_type, "JPEG")

    cropped.save(output, format=image_format, optimize=True)

    output.seek(0)
    return output
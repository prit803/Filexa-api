import tempfile
from PIL import Image


def scan_to_pdf(image_files):
    images = []

    for file in image_files:
        img = Image.open(file).convert("RGB")
        images.append(img)

    if not images:
        raise Exception("No images provided")

    output_path = tempfile.mktemp(suffix=".pdf")

    # first image save + append others
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:]
    )

    return output_path
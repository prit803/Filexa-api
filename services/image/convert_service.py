import tempfile
import shutil
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()


def convert_image(input_file, output_format: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = f"{tmpdir}/input"
        output_path = f"{tmpdir}/output.{output_format}"

        # Save file
        with open(input_path, "wb") as f:
            shutil.copyfileobj(input_file, f)

        # Open image
        image = Image.open(input_path)

        output_format = output_format.lower()

        # Handle JPG (no transparency support)
        if output_format in ["jpg", "jpeg"]:
            image = image.convert("RGB")
            save_format = "JPEG"
        elif output_format == "png":
            save_format = "PNG"
        elif output_format == "webp":
            save_format = "WEBP"
        else:
            raise Exception("Unsupported format")

        # Save
        image.save(output_path, save_format)

        # Return file
        output = tempfile.SpooledTemporaryFile()
        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
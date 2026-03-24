import tempfile
import shutil
from PIL import Image


def jpg_to_pdf(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = f"{tmpdir}/input.jpg"
        output_path = f"{tmpdir}/output.pdf"

        # Save uploaded file
        with open(input_path, "wb") as f:
            shutil.copyfileobj(input_file, f)

        # Open image and convert to PDF
        image = Image.open(input_path)

        # Convert to RGB (important for JPG/PNG)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        image.save(output_path, "PDF", resolution=100.0)

        # Load into memory
        output = tempfile.SpooledTemporaryFile()
        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
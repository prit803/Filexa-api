import subprocess
import tempfile
import os
import shutil
import zipfile


def pdf_to_jpg(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.pdf")
        output_prefix = os.path.join(tmpdir, "page")

        # Save file
        with open(input_path, "wb") as f:
            shutil.copyfileobj(input_file, f)

        # Convert (high quality)
        command = [
            "pdftoppm",
            "-jpeg",
            "-r", "300",  # HD output
            input_path,
            output_prefix
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        # Get images only
        images = sorted([
            os.path.join(tmpdir, f)
            for f in os.listdir(tmpdir)
            if f.startswith("page") and f.endswith(".jpg")
        ])

        if not images:
            raise Exception("Conversion failed")

        # Single page
        if len(images) == 1:
            output = tempfile.SpooledTemporaryFile()
            with open(images[0], "rb") as f:
                shutil.copyfileobj(f, output)

            output.seek(0)
            return output, "image/jpeg"

        # Multi-page → zip
        zip_buffer = tempfile.SpooledTemporaryFile()

        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for i, img in enumerate(images, 1):
                zipf.write(img, f"page_{i}.jpg")

        zip_buffer.seek(0)
        return zip_buffer, "application/zip"
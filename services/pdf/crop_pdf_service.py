import tempfile
import os
import shutil
import fitz  # PyMuPDF


def crop_pdf(input_file, left, top, right, bottom):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.pdf")
        output_path = os.path.join(tmpdir, "output.pdf")

        # Save file
        with open(input_path, "wb") as f:
            f.write(input_file.read())

        doc = fitz.open(input_path)

        for page in doc:
            rect = page.rect

            new_rect = fitz.Rect(
                rect.x0 + left,
                rect.y0 + top,
                rect.x1 - right,
                rect.y1 - bottom
            )

            page.set_cropbox(new_rect)

        doc.save(output_path)
        doc.close()

        output = tempfile.SpooledTemporaryFile()

        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
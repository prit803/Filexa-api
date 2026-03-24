import tempfile
import shutil
from pypdf import PdfReader, PdfWriter


def unlock_pdf(input_file, password: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = f"{tmpdir}/input.pdf"
        output_path = f"{tmpdir}/output.pdf"

        # Save file
        with open(input_path, "wb") as f:
            shutil.copyfileobj(input_file, f)

        reader = PdfReader(input_path)

        # Decrypt
        if reader.is_encrypted:
            if not reader.decrypt(password):
                raise Exception("Invalid password")

        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Save unlocked PDF
        with open(output_path, "wb") as f:
            writer.write(f)

        # Return
        output = tempfile.SpooledTemporaryFile()
        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
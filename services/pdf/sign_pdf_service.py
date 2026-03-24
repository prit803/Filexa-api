import tempfile
import shutil
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


def sign_pdf(input_pdf, signature_image, page_number: int = 0, x: int = 100, y: int = 100):
    """
    Add signature image to PDF

    Args:
        page_number: 0-based index
        x, y: position of signature
    """

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, "input.pdf")
        sig_path = os.path.join(tmpdir, "sign.png")
        overlay_path = os.path.join(tmpdir, "overlay.pdf")
        output_path = os.path.join(tmpdir, "output.pdf")

        # Save files
        with open(pdf_path, "wb") as f:
            shutil.copyfileobj(input_pdf, f)

        with open(sig_path, "wb") as f:
            shutil.copyfileobj(signature_image, f)

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Create overlay PDF with signature
        c = canvas.Canvas(overlay_path)
        c.drawImage(sig_path, x, y, width=150, height=50)  # adjust size
        c.save()

        overlay_reader = PdfReader(overlay_path)
        overlay_page = overlay_reader.pages[0]

        # Merge signature into selected page
        for i, page in enumerate(reader.pages):
            if i == page_number:
                page.merge_page(overlay_page)
            writer.add_page(page)

        # Save final PDF
        with open(output_path, "wb") as f:
            writer.write(f)

        # Return file
        output = tempfile.SpooledTemporaryFile()
        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
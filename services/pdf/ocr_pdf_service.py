import tempfile
import os
import shutil
from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfMerger


def ocr_pdf(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.pdf")

        # Save uploaded file
        with open(input_path, "wb") as f:
            f.write(input_file.read())

        # Convert PDF → images
        images = convert_from_path(input_path)

        output_pdf_paths = []

        # OCR each page
        for i, image in enumerate(images):
            page_pdf_path = os.path.join(tmpdir, f"page_{i}.pdf")

            pdf_bytes = pytesseract.image_to_pdf_or_hocr(
                image,
                extension="pdf"
            )

            with open(page_pdf_path, "wb") as f:
                f.write(pdf_bytes)

            output_pdf_paths.append(page_pdf_path)

        # Merge all pages
        merger = PdfMerger()

        for pdf in output_pdf_paths:
            merger.append(pdf)

        final_output_path = os.path.join(tmpdir, "output.pdf")
        merger.write(final_output_path)
        merger.close()

        # Load into memory (same as your pattern)
        output = tempfile.SpooledTemporaryFile()

        with open(final_output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
import os
import tempfile
from pypdf import PdfReader, PdfWriter
from PIL import Image


class PDFOrganizer:

    @staticmethod
    def reorder_pages(input_pdf, page_order):
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for i in page_order:
            writer.add_page(reader.pages[i])

        return PDFOrganizer._save(writer)

    @staticmethod
    def delete_pages(input_pdf, pages_to_delete):
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            if i not in pages_to_delete:
                writer.add_page(page)

        return PDFOrganizer._save(writer)

    @staticmethod
    def rotate_pages(input_pdf, rotations: dict):
        """
        rotations = {0: 90, 2: 180}
        """
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            if i in rotations:
                page.rotate(rotations[i])
            writer.add_page(page)

        return PDFOrganizer._save(writer)

    @staticmethod
    def merge_pdfs(pdf_list):
        writer = PdfWriter()

        for pdf in pdf_list:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)

        return PDFOrganizer._save(writer)

    @staticmethod
    def split_pdf(input_pdf, split_after_pages):
        """
        split_after_pages = [2,5] → splits after page 2 and 5
        """
        reader = PdfReader(input_pdf)
        outputs = []

        start = 0
        for split in split_after_pages + [len(reader.pages)]:
            writer = PdfWriter()
            for i in range(start, split):
                writer.add_page(reader.pages[i])

            outputs.append(PDFOrganizer._save(writer))
            start = split

        return outputs

    @staticmethod
    def add_image_as_page(image_path):
        img = Image.open(image_path)
        pdf_path = tempfile.mktemp(suffix=".pdf")
        img.convert("RGB").save(pdf_path)

        return pdf_path

    @staticmethod
    def _save(writer):
        output_path = tempfile.mktemp(suffix=".pdf")
        with open(output_path, "wb") as f:
            writer.write(f)
        return output_path
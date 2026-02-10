import subprocess
import tempfile
import os
import shutil
from pdf2docx import Converter
from core.config import get_soffice_path

def pdf_to_word(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, "input.pdf")
        docx_path = os.path.join(tmpdir, "output.docx")

        with open(pdf_path, "wb") as f:
            f.write(input_file.read())

        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()

        output = tempfile.SpooledTemporaryFile()
        with open(docx_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
import subprocess
import tempfile
import os
import shutil

import shutil

soffice_path = shutil.which("soffice")

if not soffice_path:
    raise RuntimeError("LibreOffice (soffice) not found in system PATH")

def pdf_to_word(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, "input.pdf")
        docx_path = os.path.join(tmpdir, "input.docx")

        # write uploaded PDF
        with open(pdf_path, "wb") as f:
            f.write(input_file.read())

        # libreoffice command (cross-platform)
        command = [
            soffice_path,
            "--headless",
            "--convert-to",
            "docx",
            pdf_path,
            "--outdir",
            tmpdir
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        # load output to memory
        output = tempfile.SpooledTemporaryFile()
        with open(docx_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output

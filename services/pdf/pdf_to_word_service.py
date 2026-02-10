import subprocess
import tempfile
import os
import shutil

from core.config import get_soffice_path


def pdf_to_word(input_file):
    soffice = get_soffice_path()

    with tempfile.TemporaryDirectory() as tmpdir:
        # write uploaded PDF
        pdf_path = os.path.join(tmpdir, "input.pdf")
        with open(pdf_path, "wb") as f:
            f.write(input_file.read())

        # LibreOffice command
        command = [
            soffice,
            "--headless",
            "--nologo",
            "--nofirststartwizard",
            "--convert-to",
            "docx",
            pdf_path,
            "--outdir",
            tmpdir
        ]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"LibreOffice failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            )

        # 🔑 find actual output file
        outputs = [f for f in os.listdir(tmpdir) if f.endswith(".docx")]
        if not outputs:
            raise RuntimeError(
                f"LibreOffice did not create DOCX\nSTDERR:\n{result.stderr}"
            )

        docx_path = os.path.join(tmpdir, outputs[0])

        # load output to memory
        output = tempfile.SpooledTemporaryFile()
        with open(docx_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output

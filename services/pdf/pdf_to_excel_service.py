import subprocess
import tempfile
import os
import shutil



soffice_path = shutil.which("soffice")

if not soffice_path and os.path.exists("/usr/bin/soffice"):
    soffice_path = "/usr/bin/soffice"

if not soffice_path:
    raise RuntimeError("LibreOffice (soffice) not found")


def pdf_to_excel(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, "input.pdf")
        xlsx_path = os.path.join(tmpdir, "input.xlsx")

        # Write uploaded PDF to temp file
        with open(pdf_path, "wb") as f:
            f.write(input_file.read())

        # LibreOffice headless conversion
        command = [
            soffice_path,
            "--headless",
            "--convert-to",
            "xlsx",
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

        # Load result into memory
        output = tempfile.SpooledTemporaryFile()
        with open(xlsx_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output

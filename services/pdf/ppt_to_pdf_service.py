import subprocess
import tempfile
import os
import shutil


def ppt_to_pdf(input_file):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.pptx")
        output_path = os.path.join(tmpdir, "input.pdf")

        # Save uploaded file
        with open(input_path, "wb") as f:
            f.write(input_file.read())

        # LibreOffice conversion
        command = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            input_path,
            "--outdir",
            tmpdir
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        # Load output into memory
        output = tempfile.SpooledTemporaryFile()
        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
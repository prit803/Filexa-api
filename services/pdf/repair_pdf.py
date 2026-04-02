import subprocess
import tempfile


def repair_pdf(input_file):
    output_path = tempfile.mktemp(suffix="_repaired.pdf")

    command = [
        "gs",
        "-o", output_path,
        "-sDEVICE=pdfwrite",
        "-dPDFSETTINGS=/prepress",
        "-dNOPAUSE",
        "-dBATCH",
        "-dSAFER",
        input_file
    ]

    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if process.returncode != 0:
        raise Exception(process.stderr.decode())

    return output_path
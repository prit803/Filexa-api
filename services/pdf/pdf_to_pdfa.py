import subprocess
import tempfile
import os


def convert_to_pdfa(input_file):
    output_path = tempfile.mktemp(suffix="_pdfa.pdf")

    command = [
        "gs",
        "-dPDFA=2",  # PDF/A-2 (recommended)
        "-dBATCH",
        "-dNOPAUSE",
        "-dNOOUTERSAVE",
        "-sDEVICE=pdfwrite",
        "-sColorConversionStrategy=UseDeviceIndependentColor",
        "-sProcessColorModel=DeviceRGB",
        "-sPDFACompatibilityPolicy=1",
        f"-sOutputFile={output_path}",
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
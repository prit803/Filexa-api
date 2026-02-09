import shutil
import os
import subprocess

def get_soffice_path() -> str:
    soffice = (
        os.getenv("LIBREOFFICE_BIN")
        or shutil.which("soffice")
        or "/usr/bin/soffice"
    )

    if not os.path.exists(soffice):
        raise RuntimeError("LibreOffice (soffice) not found")

    # Final sanity check
    subprocess.run(
        [soffice, "--version"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    return soffice

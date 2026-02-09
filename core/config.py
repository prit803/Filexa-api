import shutil
import os
import subprocess

import os
import subprocess

SOFFICE_CANDIDATES = [
    os.getenv("LIBREOFFICE_BIN"),
    "/usr/lib/libreoffice/program/soffice",
    "/usr/bin/soffice",
]

def get_soffice_path() -> str:
    for path in SOFFICE_CANDIDATES:
        if path and os.path.isfile(path) and os.access(path, os.X_OK):
            try:
                subprocess.run(
                    [path, "--version"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True
                )
                return path
            except Exception:
                continue

    raise RuntimeError("LibreOffice not available in Termux Ubuntu")

import os
import subprocess
import shutil

def get_soffice_path() -> str:
    # First try system PATH
    path = shutil.which("soffice")
    if path:
        return path

    # Fallback manual paths
    candidates = [
        "/usr/bin/soffice",
        "/usr/lib/libreoffice/program/soffice",
    ]

    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    raise RuntimeError("LibreOffice not available in Ubuntu")
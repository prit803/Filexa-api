# import subprocess
# import tempfile
# import os
# import shutil

# from core.config import get_soffice_path


# def pdf_to_excel(input_file):
#     soffice = get_soffice_path()
#     with tempfile.TemporaryDirectory() as tmpdir:
#         pdf_path = os.path.join(tmpdir, "input.pdf")
#         xlsx_path = os.path.join(tmpdir, "input.xlsx")

#         # Write uploaded PDF to temp file
#         with open(pdf_path, "wb") as f:
#             f.write(input_file.read())

#         # LibreOffice headless conversion
#         command = [
#             soffice,
#             "--headless",
#             "--convert-to",
#             "xlsx",
#             pdf_path,
#             "--outdir",
#             tmpdir
#         ]

#         subprocess.run(
#             command,
#             stdout=subprocess.DEVNULL,
#             stderr=subprocess.DEVNULL,
#             check=True
#         )

#         # Load result into memory
#         output = tempfile.SpooledTemporaryFile()
#         with open(xlsx_path, "rb") as f:
#             shutil.copyfileobj(f, output)

#         output.seek(0)
#         return output




import pdfplumber
import pandas as pd
import tempfile
import shutil

def pdf_to_excel(input_file):
    all_tables = []

    with pdfplumber.open(input_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

    if not all_tables:
        raise Exception("No tables found in PDF")

    final_df = pd.concat(all_tables)

    output = tempfile.SpooledTemporaryFile()
    final_df.to_excel(output, index=False, engine="openpyxl")
    output.seek(0)

    return output
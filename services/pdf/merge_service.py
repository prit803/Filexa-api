from PyPDF2 import PdfMerger
from tempfile import SpooledTemporaryFile

def merge_pdfs(upload_files):
    merger = PdfMerger()

    for file in upload_files:
        merger.append(file.file)

    output = SpooledTemporaryFile()
    merger.write(output)
    merger.close()

    output.seek(0)
    return output

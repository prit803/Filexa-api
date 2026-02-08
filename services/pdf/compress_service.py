from pypdf import PdfReader, PdfWriter
from tempfile import SpooledTemporaryFile


def compress_pdf(file, level: str = "medium"):
    reader = PdfReader(file)
    writer = PdfWriter()

    # rewrite pages (important for compression)
    for page in reader.pages:
        writer.add_page(page)

    # metadata cleanup (helps size slightly)
    writer.add_metadata({})

    # compression behavior
    if level == "low":
        # minimal changes, safest
        writer.compress_content_streams = False

    elif level == "medium":
        # default safe compression
        writer.compress_content_streams = True

    elif level == "high":
        # aggressive stream compression (max allowed in pure python)
        writer.compress_content_streams = True

    output = SpooledTemporaryFile()
    writer.write(output)
    output.seek(0)

    return output

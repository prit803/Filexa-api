from pypdf import PdfReader, PdfWriter
from tempfile import SpooledTemporaryFile


def split_by_page(file):
    reader = PdfReader(file)
    outputs = []

    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        output = SpooledTemporaryFile()
        writer.write(output)
        output.seek(0)

        outputs.append({
            "filename": f"page_{i + 1}.pdf",
            "file": output
        })

    return outputs


def split_by_range(file, ranges: str):
    reader = PdfReader(file)
    total_pages = len(reader.pages)
    outputs = []

    for part in ranges.split(","):
        writer = PdfWriter()

        if "-" in part:
            start, end = map(int, part.split("-"))
            for i in range(start - 1, min(end, total_pages)):
                writer.add_page(reader.pages[i])
            name = f"pages_{start}_to_{end}.pdf"
        else:
            page = int(part)
            writer.add_page(reader.pages[page - 1])
            name = f"page_{page}.pdf"

        output = SpooledTemporaryFile()
        writer.write(output)
        output.seek(0)

        outputs.append({
            "filename": name,
            "file": output
        })

    return outputs

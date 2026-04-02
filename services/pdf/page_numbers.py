import tempfile
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def add_page_numbers(input_pdf, position="bottom", format_type="number"):
    '''Position:
top
bottom
center
Format:
number → 1
page → Page 1
total → 1/10

'''
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    for i, page in enumerate(reader.pages):
        packet = tempfile.NamedTemporaryFile(delete=False)
        c = canvas.Canvas(packet.name, pagesize=letter)

        page_number = i + 1

        # format
        if format_type == "page":
            text = f"Page {page_number}"
        elif format_type == "total":
            text = f"{page_number}/{total_pages}"
        else:
            text = str(page_number)

        # position
        x = 300
        y = 20

        if position == "top":
            y = 800
        elif position == "bottom":
            y = 20
        elif position == "center":
            y = 400

        c.drawString(x, y, text)
        c.save()

        overlay = PdfReader(packet.name)
        page.merge_page(overlay.pages[0])
        writer.add_page(page)

    output_path = tempfile.mktemp(suffix="_numbered.pdf")

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path
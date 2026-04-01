from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO


def create_watermark_page(
    width,
    height,
    text=None,
    image_path=None,
    opacity=0.3,
    rotation=45,
    position="center",
    font_size=40,
    tile=False
):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))

    can.setFont("Helvetica", font_size)
    can.setFillGray(0, opacity)

    def get_position():
        return {
            "center": (width / 2, height / 2),
            "top-left": (50, height - 50),
            "top-right": (width - 50, height - 50),
            "bottom-left": (50, 50),
            "bottom-right": (width - 50, 50),
        }.get(position, (width / 2, height / 2))

    x, y = get_position()

    can.saveState()

    # Apply rotation
    if rotation:
        can.translate(x, y)
        can.rotate(rotation)
        x, y = 0, 0

    # Tile mode
    if tile and text:
        for i in range(0, int(width), 200):
            for j in range(0, int(height), 150):
                can.drawString(i, j, text)
    else:
        if text:
            can.drawCentredString(x, y, text)

        if image_path:
            can.drawImage(
                image_path,
                x - 100,
                y - 100,
                width=200,
                height=200,
                mask='auto'
            )

    can.restoreState()
    can.save()

    packet.seek(0)
    return PdfReader(packet)


def add_watermark(
    input_pdf,
    output_pdf,
    text=None,
    image_path=None,
    opacity=0.3,
    rotation=45,
    position="center",
    font_size=40,
    tile=False,
    pages="all"
):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    # Page selection
    if pages == "all":
        target_pages = range(total_pages)
    else:
        target_pages = [int(p.strip()) - 1 for p in pages.split(",")]

    for i, page in enumerate(reader.pages):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        if i in target_pages:
            watermark_pdf = create_watermark_page(
                width,
                height,
                text,
                image_path,
                opacity,
                rotation,
                position,
                font_size,
                tile
            )
            watermark_page = watermark_pdf.pages[0]
            page.merge_page(watermark_page)

        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    return output_pdf
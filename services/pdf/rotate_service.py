from PyPDF2 import PdfReader, PdfWriter


def rotate_pdf(
    input_pdf: str,
    output_pdf: str,
    rotation: int = 90,
    pages: str = "all"
):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    # Normalize rotation (only 90, 180, 270)
    rotation = rotation % 360
    if rotation not in [90, 180, 270]:
        rotation = 90

    # Page selection
    if pages == "all":
        target_pages = range(total_pages)
    else:
        target_pages = [int(p.strip()) - 1 for p in pages.split(",")]

    for i, page in enumerate(reader.pages):
        if i in target_pages:
            page.rotate(rotation)

        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    return output_pdf
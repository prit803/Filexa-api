from xhtml2pdf import pisa
from io import BytesIO


def html_to_pdf(html_content: str, output_path: str):
    """
    Cross-platform HTML to PDF
    """

    with open(output_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(
            src=html_content,
            dest=pdf_file
        )

    if pisa_status.err:
        raise Exception("Error while converting HTML to PDF")

    return output_path
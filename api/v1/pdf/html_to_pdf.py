import os
import uuid
import tempfile
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Optional

from services.pdf.html_to_pdf_service import html_to_pdf
from core.logging import get_logger


router = APIRouter()
logger = get_logger("htmlToPDF")


@router.post("/html-to-pdf")
async def convert_html_to_pdf(
    html: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    logger.info("HTML to PDF API called")

    temp_dir = tempfile.gettempdir()

    input_path = None
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")

    try:
        # Case 1: Raw HTML
        if html:
            html_to_pdf(html, output_path)

        # Case 2: HTML file
        elif file:
            content = (await file.read()).decode("utf-8")
            html_to_pdf(content, output_path)

        else:
            return {"error": "Provide HTML content or file"}

        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename="converted.pdf"
        )

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": "Something went wrong"}

    finally:
        if input_path and os.path.exists(input_path):
            os.remove(input_path)
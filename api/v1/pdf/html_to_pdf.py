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


@router.post(
    "/html-to-pdf",
    response_class=FileResponse,
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "PDF file download"
        }
    }
)
async def convert_html_to_pdf(
    html: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    logger.info("HTML to PDF API called")

    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")

    try:
        # ✅ Case 1: Raw HTML
        if html:
            await html_to_pdf(html, output_path)

        # ✅ Case 2: HTML file
        elif file:
            content = (await file.read()).decode("utf-8")
            await html_to_pdf(content, output_path)

        else:
            return {"error": "Provide HTML or file"}

        logger.info("PDF generated successfully")

        # ✅ IMPORTANT → Swagger download works
        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename="converted.pdf"  # 👈 REQUIRED for download button
        )

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": "Something went wrong"}

    finally:
        # 🔥 Cleanup (optional but recommended)
        if os.path.exists(output_path):
            pass  # keep file for download (or delete later via cron)
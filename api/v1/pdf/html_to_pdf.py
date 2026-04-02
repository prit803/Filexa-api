from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Optional

from services.pdf.html_to_pdf_service import html_to_pdf_stream
from core.logging import get_logger


router = APIRouter()
logger = get_logger("htmlToPDF")


@router.post("/html-to-pdf")
async def convert_html_to_pdf(
    html: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    try:
        # ✅ Validate input
        if not html and not file:
            return JSONResponse(
                content={
                    "success": False,
                    "errorMessage": "Provide HTML or file",
                    "statusCode": "400"
                },
                status_code=400
            )

        # ✅ Case 1: raw HTML
        if html:
            content = html

        # ✅ Case 2: HTML file
        else:
            if file.content_type not in ["text/html"]:
                return JSONResponse(
                    content={
                        "success": False,
                        "errorMessage": "Only HTML file allowed",
                        "statusCode": "400"
                    },
                    status_code=400
                )
            content = (await file.read()).decode("utf-8")

        # 🔥 Generate PDF
        result = await html_to_pdf_stream(content)

        logger.info("HTML converted to PDF successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=converted.pdf"
            }
        )

    except Exception as e:
        logger.error(str(e))
        return JSONResponse(
            content={
                "success": False,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )
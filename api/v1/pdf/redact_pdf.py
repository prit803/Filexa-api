from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.redact_pdf_service import redact_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("REDACTPDF")


@router.post("/redact-pdf")
async def redact_pdf_api(
    file: UploadFile = File(...),
    text: str = Form(...)   # text to redact
):
    try:
        if file.content_type != "application/pdf":
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Only PDF files are allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = redact_pdf(file.file, text)

        logger.info("PDF redacted successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=redacted.pdf"
            }
        )

    except Exception as e:
        logger.error(str(e))

        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )
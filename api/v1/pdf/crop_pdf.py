from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.crop_pdf_service import crop_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("CROPPDF")


@router.post("/crop-pdf")
async def crop_pdf_api(
    file: UploadFile = File(...),
    left: float = Form(...),
    top: float = Form(...),
    right: float = Form(...),
    bottom: float = Form(...)
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

        result = crop_pdf(file.file, left, top, right, bottom)

        logger.info("PDF cropped successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=cropped.pdf"
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
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.jpg_to_pdf_service import jpg_to_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("JPGtoPDF")


@router.post("/jpg-to-pdf")
async def convert_jpg_to_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Only JPG/PNG images are allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = jpg_to_pdf(file.file)

        logger.info("Image converted to PDF successfully")

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
                "successMessage": None,
                "data": None,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )
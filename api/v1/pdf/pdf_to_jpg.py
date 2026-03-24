from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.pdf_to_jpg_service import pdf_to_jpg
from core.logging import get_logger

router = APIRouter()
logger = get_logger("PDFtoJPG")


@router.post("/pdf-to-jpg")
async def convert_pdf_to_jpg(file: UploadFile = File(...)):
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

        result, media_type = pdf_to_jpg(file.file)

        logger.info("PDF converted to JPG successfully")

        filename = "converted.jpg" if media_type == "image/jpeg" else "converted.zip"

        return StreamingResponse(
            result,
            media_type=media_type,
            headers={
                "Content-Disposition": f"attachment; filename={filename}"
            }
        )

    except FileNotFoundError:
        logger.error("Poppler not installed")
        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": "Poppler (pdftoppm) is not installed on server",
                "statusCode": "500"
            },
            status_code=500
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
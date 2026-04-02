from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.ocr_pdf_service import ocr_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("OCRPDF")


@router.post("/ocr-pdf")
async def convert_ocr_pdf(file: UploadFile = File(...)):
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

        result = ocr_pdf(file.file)

        logger.info("OCR PDF processed successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=ocr_output.pdf"
            }
        )

    except FileNotFoundError:
        logger.error("Tesseract or Poppler not installed")

        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": "Tesseract or Poppler is not installed on server",
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
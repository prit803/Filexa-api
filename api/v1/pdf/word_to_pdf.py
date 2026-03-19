from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.word_to_pdf_service import word_to_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("WordToPDF")


@router.post("/word-to-pdf")
async def convert_word_to_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type not in [
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/msword"
        ]:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Only Word files (DOCX/DOC) are allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = word_to_pdf(file.file)

        logger.info("Word converted to PDF successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=converted.pdf"
            }
        )

    except FileNotFoundError:
        logger.error("LibreOffice not installed")
        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": "LibreOffice is not installed on server",
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
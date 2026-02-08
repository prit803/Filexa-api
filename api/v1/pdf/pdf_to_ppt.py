from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.pdf_to_ppt_service import pdf_to_ppt
from core.logging import get_logger

router = APIRouter()
logger = get_logger("PDFtoPPT")


@router.post("/pdf-to-ppt")
async def convert_pdf_to_ppt(file: UploadFile = File(...)):
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

        result = pdf_to_ppt(file.file)
        logger.info("PDF converted to PowerPoint successfully")

        return StreamingResponse(
            result,
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            headers={
                "Content-Disposition": "attachment; filename=converted.pptx"
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

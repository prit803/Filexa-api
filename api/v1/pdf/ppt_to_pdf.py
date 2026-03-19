from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.ppt_to_pdf_service import ppt_to_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("PPTtoPDF")


@router.post("/ppt-to-pdf")
async def convert_ppt_to_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type not in [
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.ms-powerpoint"
        ]:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Only PowerPoint files (PPT/PPTX) are allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = ppt_to_pdf(file.file)

        logger.info("PowerPoint converted to PDF successfully")

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
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.compare_pdf_service import compare_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("COMPAREPDF")


@router.post("/compare-pdf")
async def compare_pdf_api(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):
    try:
        if file1.content_type != "application/pdf" or file2.content_type != "application/pdf":
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Both files must be PDFs",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = compare_pdf(file1.file, file2.file)

        logger.info("PDF comparison completed successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=compared.pdf"
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
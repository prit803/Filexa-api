from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import JSONResponse, StreamingResponse
from services.pdf.compress_service import compress_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("CompressPDF")


@router.post("/compress")
async def compress_pdf_api(
    file: UploadFile = File(...),
    level: str = Query("medium", enum=["low", "medium", "high"])
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

        compressed = compress_pdf(file.file, level)

        logger.info(f"PDF compressed successfully | level={level}")

        return StreamingResponse(
            compressed,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=compressed.pdf"
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

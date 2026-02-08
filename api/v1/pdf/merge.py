from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.merge_service import merge_pdfs
from core.logging import get_logger

router = APIRouter()
logger = get_logger("MergePDF")

@router.post("/merge")
async def merge_pdf(files: list[UploadFile] = File(...)):
    try:
        merged_file = merge_pdfs(files)

        logger.info("PDF merged successfully")

        return StreamingResponse(
            merged_file,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=merged.pdf"
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

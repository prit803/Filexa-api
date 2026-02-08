from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import JSONResponse, StreamingResponse
from services.pdf.split_service import split_by_page, split_by_range
from core.logging import get_logger
import zipfile
from tempfile import SpooledTemporaryFile

router = APIRouter()
logger = get_logger("SplitPDF")


@router.post("/split")
async def split_pdf(
    file: UploadFile = File(...),
    mode: str = Query("split", enum=["split", "range"]),
    ranges: str | None = Query(None)
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

        if mode == "split":
            result_files = split_by_page(file.file)

        elif mode == "range":
            if not ranges:
                raise ValueError("ranges parameter is required for range mode")
            result_files = split_by_range(file.file, ranges)

        zip_buffer = SpooledTemporaryFile()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for item in result_files:
                zipf.writestr(item["filename"], item["file"].read())

        zip_buffer.seek(0)

        logger.info("PDF split successfully")

        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={
                "Content-Disposition": "attachment; filename=split_pdf.zip"
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

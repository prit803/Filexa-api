from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import tempfile
import shutil

from services.pdf.scan_to_pdf import scan_to_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("ScanToPDF")


def error_response(message, status_code):
    return JSONResponse(
        content={
            "success": False,
            "successMessage": None,
            "data": None,
            "errorMessage": message,
            "statusCode": str(status_code)
        },
        status_code=status_code
    )


@router.post("/scan-to-pdf")
async def scan_to_pdf_api(files: list[UploadFile] = File(...)):
    try:
        temp_files = []

        for file in files:
            if not file.content_type.startswith("image/"):
                logger.warning("Invalid file type in scan-to-pdf")
                return error_response("Only image files are allowed", 400)

            temp = tempfile.NamedTemporaryFile(delete=False)
            shutil.copyfileobj(file.file, temp)
            temp_files.append(temp.name)

        output_path = scan_to_pdf(temp_files)

        logger.info("Images converted to PDF successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=scanned.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error in scan to PDF")
        return error_response(str(e), 500)
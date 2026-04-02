from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import tempfile
import shutil

from services.pdf.repair_pdf import repair_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("RepairPDF")


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


@router.post("/repair-pdf")
async def repair_pdf_api(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for repair")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        output_path = repair_pdf(temp.name)

        logger.info("PDF repaired successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=repaired.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error repairing PDF")
        return error_response(str(e), 500)
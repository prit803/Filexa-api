from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import tempfile
import shutil

from services.pdf.pdf_to_pdfa import convert_to_pdfa
from core.logging import get_logger

router = APIRouter()
logger = get_logger("PDFtoPDFA")


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


@router.post("/pdf-to-pdfa")
async def pdf_to_pdfa(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for PDF/A")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        output_path = convert_to_pdfa(temp.name)

        logger.info("PDF converted to PDF/A successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=converted_pdfa.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error converting PDF to PDF/A")
        return error_response(str(e), 500)
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
import tempfile
import shutil

from services.pdf.page_numbers import add_page_numbers
from core.logging import get_logger

router = APIRouter()
logger = get_logger("PageNumbers")


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


@router.post("/page-numbers")
async def page_numbers(
    file: UploadFile = File(...),
    position: str = Form("bottom"),
    format_type: str = Form("number")
):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for page numbers")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        output_path = add_page_numbers(temp.name, position, format_type)

        logger.info("Page numbers added successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=numbered.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error adding page numbers")
        return error_response(str(e), 500)
import os
import uuid
import tempfile
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Optional

from services.pdf.rotate_service import rotate_pdf

from core.logging import get_logger 
router = APIRouter()
logger = get_logger("rotatePDF")


@router.post("/rotate-pdf")
async def rotate_pdf_api(
    file: UploadFile = File(...),
    rotation: int = Form(90),
    pages: str = Form("all")
):
    logger.info("Rotate PDF API called")

    temp_dir = tempfile.gettempdir()

    input_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}_rotated.pdf")

    try:
        # Save file
        with open(input_path, "wb") as f:
            f.write(await file.read())

        logger.info(f"File saved: {input_path}")

        # Process rotation
        rotate_pdf(
            input_pdf=input_path,
            output_pdf=output_path,
            rotation=rotation,
            pages=pages
        )

        logger.info("PDF rotated successfully")

        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename="rotated.pdf"
        )

    except Exception as e:
        logger.error(f"Error in rotate API: {str(e)}")
        return {"error": "Something went wrong"}

    finally:
        # Cleanup
        if os.path.exists(input_path):
            os.remove(input_path)
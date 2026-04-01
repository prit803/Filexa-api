import os
import uuid
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Optional

from services.pdf.watermark_service import add_watermark
from core.logging import get_logger

import tempfile
import os
 
router = APIRouter()
logger = get_logger("watermarkPDF")


@router.post("/watermark-pdf")
async def watermark_pdf(
    file: UploadFile = File(...),

    text: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),

    opacity: float = Form(0.3),
    rotation: int = Form(45),
    position: str = Form("center"),
    font_size: int = Form(40),
    tile: bool = Form(False),
    pages: str = Form("all")
):
    logger.info("Watermark PDF API called")

    temp_dir = tempfile.gettempdir()

    input_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}_watermarked.pdf")
    image_path = None

    try:
        # Save input PDF
        with open(input_path, "wb") as f:
            f.write(await file.read())

        logger.info(f"Input file saved: {input_path}")

        # Save image if provided
        if image:
            image_path = f"/tmp/{uuid.uuid4()}_{image.filename}"
            with open(image_path, "wb") as f:
                f.write(await image.read())

            logger.info(f"Image file saved: {image_path}")

        # Validation
        if not text and not image:
            logger.error("No watermark input provided")
            return {"error": "Provide text or image watermark"}

        # Process watermark
        add_watermark(
            input_pdf=input_path,
            output_pdf=output_path,
            text=text,
            image_path=image_path,
            opacity=opacity,
            rotation=rotation,
            position=position,
            font_size=font_size,
            tile=tile,
            pages=pages
        )

        logger.info("Watermark applied successfully")

        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename="watermarked.pdf"
        )

    except Exception as e:
        logger.error(f"Error in watermark API: {str(e)}")
        return {"error": "Something went wrong"}

    finally:
        # Cleanup
        if os.path.exists(input_path):
            os.remove(input_path)

        if image_path and os.path.exists(image_path):
            os.remove(image_path)
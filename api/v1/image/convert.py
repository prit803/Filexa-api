from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.image.convert_service import convert_image
from core.logging import get_logger

router = APIRouter()
logger = get_logger("convertToimage")

@router.post("/convert")
async def image_convert(
    file: UploadFile = File(...),
    format: str = Form(...)
):
    try:
        allowed = ["jpg", "jpeg", "png", "webp"]

        if format.lower() not in allowed:
            return JSONResponse(
                content={"error": "Invalid format"},
                status_code=400
            )

        result = convert_image(file.file, format.lower())

        return StreamingResponse(
            result,
            media_type=f"image/{format}",
            headers={
                "Content-Disposition": f"attachment; filename=converted.{format}"
            }
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
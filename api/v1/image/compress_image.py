from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.image.compress_image_service import compress_image
from core.logging import get_logger

router = APIRouter()
logger = get_logger("COMPRESSIMAGE")


@router.post("/compress-image")
async def compress_image_api(
    file: UploadFile = File(...),
    quality: int = Form(70)   # default compression
):
    try:
        if file.content_type not in [
            "image/jpeg",
            "image/png",
            "image/webp"
        ]:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Only JPG, PNG, WEBP images are allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = compress_image(file.file, file.content_type, quality)

        logger.info("Image compressed successfully")

        return StreamingResponse(
            result,
            media_type=file.content_type,
            headers={
                "Content-Disposition": "attachment; filename=compressed_image"
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
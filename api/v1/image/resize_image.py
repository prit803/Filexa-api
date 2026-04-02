from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.image.resize_image_service import resize_image
from core.logging import get_logger

router = APIRouter()
logger = get_logger("RESIZEIMAGE")


@router.post("/resize-image")
async def resize_image_api(
    file: UploadFile = File(...),
    width: int = Form(...),
    height: int = Form(...),
    keep_aspect_ratio: bool = Form(True)
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

        result = resize_image(
            file.file,
            file.content_type,
            width,
            height,
            keep_aspect_ratio
        )

        logger.info("Image resized successfully")

        return StreamingResponse(
            result,
            media_type=file.content_type,
            headers={
                "Content-Disposition": "attachment; filename=resized_image"
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
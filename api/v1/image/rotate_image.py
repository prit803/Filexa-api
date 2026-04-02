from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.image.rotate_image_service import rotate_image
from core.logging import get_logger

router = APIRouter()
logger = get_logger("ROTATEIMAGE")


@router.post("/rotate-image")
async def rotate_image_api(
    file: UploadFile = File(...),
    angle: int = Form(...)   # 90, 180, 270
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

        result = rotate_image(file.file, file.content_type, angle)

        logger.info(f"Image rotated successfully by {angle} degrees")

        return StreamingResponse(
            result,
            media_type=file.content_type,
            headers={
                "Content-Disposition": "attachment; filename=rotated_image"
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
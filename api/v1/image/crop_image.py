from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.image.crop_image_service import crop_image
from core.logging import get_logger

router = APIRouter()
logger = get_logger("CROPIMAGE")


@router.post("/crop-image")
async def crop_image_api(
    file: UploadFile = File(...),
    left: int = Form(...),
    top: int = Form(...),
    right: int = Form(...),
    bottom: int = Form(...)
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

        result = crop_image(
            file.file,
            file.content_type,
            left,
            top,
            right,
            bottom
        )

        logger.info("Image cropped successfully")

        return StreamingResponse(
            result,
            media_type=file.content_type,
            headers={
                "Content-Disposition": "attachment; filename=cropped_image"
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
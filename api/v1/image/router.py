from fastapi import APIRouter
from core.logging import setup_logging
from api.v1.image.convert import router as convert_router
from api.v1.image.compress_image import router as compress_image_router
from api.v1.image.resize_image import router as resize_image_router
from api.v1.image.crop_image import router as crop_image_router
from api.v1.image.rotate_image import router as rotate_image_router




setup_logging()

router = APIRouter(prefix="/image", tags=["IMAGE"])

router.include_router(convert_router)
router.include_router(compress_image_router)
router.include_router(resize_image_router)
router.include_router(rotate_image_router)

from fastapi import APIRouter
from core.logging import setup_logging
from api.v1.image.convert import router as convert_router




setup_logging()

router = APIRouter(prefix="/image", tags=["IMAGE"])

router.include_router(convert_router)

from fastapi import APIRouter
from core.logging import setup_logging
from api.v1.pdf.merge import router as merge_router
from api.v1.pdf.split import router as split_router
from api.v1.pdf.compress import router as compress_router
from api.v1.pdf.pdf_to_word import router as pdf_to_word_router
from api.v1.pdf.pdf_to_ppt import router as pdf_to_ppt_router
from api.v1.pdf.pdf_to_excel import router as pdf_to_excel_router


setup_logging()
router = APIRouter(prefix="/pdf", tags=["PDF"])

router.include_router(merge_router)
router.include_router(split_router)
router.include_router(compress_router)

router.include_router(pdf_to_word_router)



router.include_router(pdf_to_ppt_router)




router.include_router(pdf_to_excel_router)

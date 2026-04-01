from fastapi import APIRouter
from core.logging import setup_logging
from api.v1.pdf.merge import router as merge_router
from api.v1.pdf.split import router as split_router
from api.v1.pdf.compress import router as compress_router
from api.v1.pdf.pdf_to_word import router as pdf_to_word_router
from api.v1.pdf.pdf_to_ppt import router as pdf_to_ppt_router
from api.v1.pdf.pdf_to_excel import router as pdf_to_excel_router
from api.v1.pdf.word_to_pdf import router as word_to_pdf_router
from api.v1.pdf.ppt_to_pdf import router as ppt_to_pdf_router

from api.v1.pdf.excel_to_pdf import router as excel_to_pdf_router
from api.v1.pdf.jpg_to_pdf import router as jpg_to_pdf_router
from api.v1.pdf.pdf_to_jpg import router as pdf_to_jpg_router
from api.v1.pdf.sign_pdf import router as sign_pdf_router
from api.v1.pdf.unlock_pdf import router as unlock_pdf_router
from api.v1.pdf.protect_pdf import router as protect_pdf_router
from api.v1.pdf.watermark import router as watermark_pdf_router
from api.v1.pdf.rotate import router as router_pdf_router
from api.v1.pdf.html_to_pdf import router as html_to_pdf_router

setup_logging()

router = APIRouter(prefix="/pdf", tags=["PDF"])

router.include_router(merge_router)

router.include_router(split_router)

router.include_router(compress_router)

router.include_router(pdf_to_word_router)

router.include_router(pdf_to_ppt_router)

router.include_router(pdf_to_excel_router)

router.include_router(word_to_pdf_router)

router.include_router(ppt_to_pdf_router)



router.include_router(excel_to_pdf_router)
router.include_router(jpg_to_pdf_router)
router.include_router(pdf_to_jpg_router)
router.include_router(sign_pdf_router)
router.include_router(unlock_pdf_router)
router.include_router(protect_pdf_router)
router.include_router(watermark_pdf_router)
router.include_router(router_pdf_router)
router.include_router(html_to_pdf_router)

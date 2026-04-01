import sys
import asyncio

# ✅ FIX for Windows + Playwright (TOP MOST)
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from middleware.feature_guard import feature_guard
from api.v1.pdf.router import router as pdf_router
from api.v1.image.router import router as image_router
from api.v1.admin.feature_toggle import router as admin_router

app = FastAPI()

app.middleware("http")(feature_guard)

app.include_router(pdf_router)
app.include_router(image_router)
app.include_router(admin_router)
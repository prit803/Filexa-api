from fastapi import FastAPI
from middleware.feature_guard import feature_guard
from api.v1.pdf.router import router as pdf_router
from api.v1.admin.feature_toggle import router as admin_router

app = FastAPI()

app.middleware("http")(feature_guard)

app.include_router(pdf_router)
app.include_router(admin_router)

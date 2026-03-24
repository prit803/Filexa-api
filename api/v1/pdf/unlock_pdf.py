from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.unlock_pdf_service import unlock_pdf
from core.logging import get_logger 

router = APIRouter()
logger = get_logger("unlockPDF")

@router.post("/unlock-pdf")
async def unlock_pdf_api(
    file: UploadFile = File(...),
    password: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            return JSONResponse(
                content={"error": "Only PDF allowed"},
                status_code=400
            )

        result = unlock_pdf(file.file, password)

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=unlocked.pdf"}
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
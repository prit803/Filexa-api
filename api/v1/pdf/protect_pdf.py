from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.protect_pdf_service import protect_pdf

router = APIRouter()


@router.post("/protect-pdf")
async def protect_pdf_api(
    file: UploadFile = File(...),
    password: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            return JSONResponse(
                content={"error": "Only PDF allowed"},
                status_code=400
            )

        result = protect_pdf(file.file, password)

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=protected.pdf"}
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
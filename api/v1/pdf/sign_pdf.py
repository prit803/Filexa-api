from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from services.pdf.sign_pdf_service import sign_pdf
from core.logging import get_logger

router = APIRouter()
logger = get_logger("SignPDF")


@router.post("/sign-pdf")
async def sign_pdf_api(
    pdf: UploadFile = File(...),
    signature: UploadFile = File(...),
    page: int = Form(0),
    x: int = Form(100),
    y: int = Form(100)
):
    try:
        if pdf.content_type != "application/pdf":
            return JSONResponse(
                content={
                    "success": False,
                    "errorMessage": "Only PDF file allowed",
                    "statusCode": "400"
                },
                status_code=400
            )

        if signature.content_type not in ["image/png", "image/jpeg"]:
            return JSONResponse(
                content={
                    "success": False,
                    "errorMessage": "Signature must be PNG/JPG",
                    "statusCode": "400"
                },
                status_code=400
            )

        result = sign_pdf(pdf.file, signature.file, page, x, y)

        logger.info("PDF signed successfully")

        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=signed.pdf"}
        )

    except Exception as e:
        logger.error(str(e))
        return JSONResponse(
            content={
                "success": False,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )
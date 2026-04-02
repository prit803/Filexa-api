from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
import shutil
import tempfile
import json
import os

from services.pdf.organize_pdf import PDFOrganizer
from core.logging import get_logger


router = APIRouter()
logger = get_logger("PDFOrganizer")


def error_response(message, status_code):
    return JSONResponse(
        content={
            "success": False,
            "successMessage": None,
            "data": None,
            "errorMessage": message,
            "statusCode": str(status_code)
        },
        status_code=status_code
    )

@router.post("/organize/reorder")
async def reorder_pdf(
    file: UploadFile = File(...),
    order: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for reorder")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        # ✅ 👇 AHI ADD KARVU (replace json.loads line)
        try:
            page_order = json.loads(order)
        except json.JSONDecodeError:
            try:
                page_order = [int(x.strip()) for x in order.split(",")]
            except Exception:
                logger.warning(f"Invalid order format: {order}")
                return error_response(
                    "Invalid format for 'order'. Use [2,1] or 2,1",
                    400
                )

        output_path = PDFOrganizer.reorder_pages(temp.name, page_order)

        logger.info("PDF reordered successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=reordered.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error in reorder PDF")
        return error_response(str(e), 500)
    
# ✅ DELETE
@router.post("/organize/delete")
async def delete_pages(
    file: UploadFile = File(...),
    pages: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for delete")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        # ✅ FIXED PARSING
        try:
            pages_to_delete = json.loads(pages)
        except json.JSONDecodeError:
            try:
                pages_to_delete = [int(x.strip()) for x in pages.split(",")]
            except Exception:
                logger.warning(f"Invalid pages format: {pages}")
                return error_response(
                    "Invalid format for 'pages'. Use [0,2] or 0,2",
                    400
                )

        output_path = PDFOrganizer.delete_pages(temp.name, pages_to_delete)

        logger.info("PDF pages deleted successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=deleted_pages.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error in delete PDF pages")
        return error_response(str(e), 500)


# ✅ ROTATE
@router.post("/organize/rotate")
async def rotate_pdf(
    file: UploadFile = File(...),
    rotations: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            logger.warning("Invalid file type for rotate")
            return error_response("Only PDF files are allowed", 400)

        temp = tempfile.NamedTemporaryFile(delete=False)
        shutil.copyfileobj(file.file, temp)

        # ✅ FIXED PARSING
        try:
            rotation_dict = json.loads(rotations)
        except json.JSONDecodeError:
            try:
                rotation_dict = {}
                for item in rotations.split(","):
                    key, value = item.split(":")
                    rotation_dict[int(key.strip())] = int(value.strip())
            except Exception:
                logger.warning(f"Invalid rotations format: {rotations}")
                return error_response(
                    "Invalid format for 'rotations'. Use {\"0\":90} or 0:90",
                    400
                )

        output_path = PDFOrganizer.rotate_pages(temp.name, rotation_dict)

        logger.info("PDF rotated successfully")

        return StreamingResponse(
            open(output_path, "rb"),
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=rotated.pdf"
            }
        )

    except Exception as e:
        logger.exception("Error in rotate PDF")
        return error_response(str(e), 500)
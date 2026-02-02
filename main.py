import os
import logging
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# --------------------------------------------------
# Logging Configuration (Production Ready)
# --------------------------------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/converter.log"),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger("FileConverter")

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="File Converter API",
    version="1.0.0",
    description="Excel ↔ CSV | Excel → PDF | CSV → PDF"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --------------------------------------------------
# Utilities
# --------------------------------------------------
def save_upload_file(upload: UploadFile) -> str:
    path = os.path.join(UPLOAD_DIR, upload.filename)
    with open(path, "wb") as f:
        f.write(upload.file.read())
    logger.info(f"Uploaded file saved: {path}")
    return path


def get_output_path(input_path: str, ext: str) -> str:
    base = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join(OUTPUT_DIR, f"{base}.{ext}")


# --------------------------------------------------
# PDF Generator
# --------------------------------------------------
def dataframe_to_pdf(df: pd.DataFrame, pdf_path: str, title: str):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    x, y = 40, height - 40
    row_height = 18

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, title)
    y -= 30

    c.setFont("Helvetica", 9)

    for col in df.columns:
        c.drawString(x, y, str(col))
        x += 120

    x = 40
    y -= row_height

    for _, row in df.iterrows():
        for value in row:
            c.drawString(x, y, str(value))
            x += 120

        x = 40
        y -= row_height

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    logger.info(f"PDF generated: {pdf_path}")


# --------------------------------------------------
# API Endpoints
# --------------------------------------------------
@app.post("/excel-to-csv")
async def excel_to_csv(file: UploadFile = File(...)):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Invalid Excel file")

    input_path = save_upload_file(file)
    output_path = get_output_path(input_path, "csv")

    pd.read_excel(input_path).to_csv(output_path, index=False)
    logger.info("Excel → CSV completed")

    return FileResponse(output_path, filename=os.path.basename(output_path))


@app.post("/csv-to-excel")
async def csv_to_excel(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    input_path = save_upload_file(file)
    output_path = get_output_path(input_path, "xlsx")

    pd.read_csv(input_path).to_excel(output_path, index=False, engine="xlsxwriter")
    logger.info("CSV → Excel completed")

    return FileResponse(output_path, filename=os.path.basename(output_path))


@app.post("/excel-to-pdf")
async def excel_to_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Invalid Excel file")

    input_path = save_upload_file(file)
    output_path = get_output_path(input_path, "pdf")

    df = pd.read_excel(input_path)
    dataframe_to_pdf(df, output_path, "Excel to PDF")

    return FileResponse(output_path, filename=os.path.basename(output_path))


@app.post("/csv-to-pdf")
async def csv_to_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    input_path = save_upload_file(file)
    output_path = get_output_path(input_path, "pdf")

    df = pd.read_csv(input_path)
    dataframe_to_pdf(df, output_path, "CSV to PDF")

    return FileResponse(output_path, filename=os.path.basename(output_path))


# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

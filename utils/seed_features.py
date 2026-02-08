from core.database import SessionLocal
from models.feature import Feature

db = SessionLocal()

merge_pdf = Feature(
    feature_key="pdf_merge",
    slug="merge-pdf",
    name="Merge PDF",
    desc="Combine multiple PDFs into one.",
    icon="bi-layers",
    category="pdf",
    keywords=["combine", "join", "merge", "pdf"],
    is_active=True,
    seo_title="Merge PDF Online Free – Combine PDFs Securely | Filexa",
    seo_desc="Merge multiple PDF files into one document instantly. Fast, secure, and privacy-first PDF merger."
)

db.add(merge_pdf)
db.commit()
db.close()

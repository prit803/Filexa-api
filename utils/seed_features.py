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
split_pdf = Feature(
    feature_key="pdf_split",
    slug="split-pdf",
    name="Split PDF",
    desc="Extract pages or split a PDF into multiple files.",
    icon="bi-scissors",
    category="pdf",
    keywords=["split", "extract", "separate", "pages", "pdf"],
    is_active=True,
    seo_title="Split PDF Online Free – Extract Pages Instantly | Filexa",
    seo_desc="Split PDF files into multiple documents or extract selected pages easily. Fast, secure, and privacy-first PDF splitter."
)



compress_pdf = Feature(
    feature_key="pdf_compress",
    slug="compress-pdf",
    name="Compress PDF",
    desc="Reduce PDF file size while maintaining quality.",
    icon="bi-file-zip",
    category="pdf",
    keywords=["compress", "reduce size", "optimize", "pdf"],
    is_active=True,
    seo_title="Compress PDF Online Free – Reduce PDF File Size | Filexa",
    seo_desc="Compress PDF files quickly and reduce their size without losing quality. Fast, secure, and privacy-first PDF compression."
)
pdf_to_word = Feature(
    feature_key="pdf_to_word",
    slug="pdf-to-word",
    name="PDF to Word",
    desc="Convert PDF files into editable Word documents.",
    icon="bi-file-earmark-word",
    category="pdf",
    keywords=["pdf to word", "convert pdf", "docx", "word", "pdf"],
    is_active=True,
    seo_title="PDF to Word Converter Online Free – Convert PDF to DOCX | Filexa",
    seo_desc="Convert PDF files into fully editable Word documents (DOCX) instantly. Fast, secure, and privacy-first PDF to Word converter."
)


pdf_to_ppt = Feature(
    feature_key="pdf_to_ppt",
    slug="pdf-to-ppt",
    name="PDF to PowerPoint",
    desc="Convert PDF files into editable PowerPoint presentations.",
    icon="bi-file-earmark-slides",
    category="pdf",
    keywords=["pdf to ppt", "pdf to powerpoint", "convert pdf", "ppt", "presentation"],
    is_active=True,
    seo_title="PDF to PowerPoint Converter Online Free – Convert PDF to PPT | Filexa",
    seo_desc="Convert PDF files into editable PowerPoint presentations instantly. Fast, secure, and privacy-first PDF to PPT converter."
)


pdf_to_excel = Feature(
    feature_key="pdf_to_excel",
    slug="pdf-to-excel",
    name="PDF to Excel",
    desc="Convert PDF files into editable Excel spreadsheets.",
    icon="bi-file-earmark-excel",
    category="pdf",
    keywords=["pdf to excel", "convert pdf", "xlsx", "spreadsheet", "pdf"],
    is_active=True,
    seo_title="PDF to Excel Converter Online Free – Convert PDF to XLSX | Filexa",
    seo_desc="Convert PDF files into editable Excel spreadsheets instantly. Fast, secure, and privacy-first PDF to Excel converter."
)


# db.add(merge_pdf)
# db.add(split_pdf)
# db.add(compress_pdf)

# db.add(pdf_to_word)
# db.add(pdf_to_ppt)
# db.add(pdf_to_excel)
db.commit()
db.close()

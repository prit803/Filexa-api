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


word_to_pdf = Feature(
    feature_key="word_to_pdf",
    slug="word-to-pdf",
    name="Word to PDF",
    desc="Convert Word documents into PDF files.",
    icon="bi-file-earmark-pdf",
    category="pdf",
    keywords=["word to pdf", "docx to pdf", "convert word", "pdf", "document"],
    is_active=True,
    seo_title="Word to PDF Converter Online Free – Convert DOCX to PDF | Filexa",
    seo_desc="Convert Word documents (DOCX) into high-quality PDF files instantly. Fast, secure, and privacy-first Word to PDF converter."
)

ppt_to_pdf = Feature(
    feature_key="ppt_to_pdf",
    slug="ppt-to-pdf",
    name="PowerPoint to PDF",
    desc="Convert PowerPoint presentations into PDF files.",
    icon="bi-file-earmark-pdf",
    category="pdf",
    keywords=["ppt to pdf", "powerpoint to pdf", "convert ppt", "pdf"],
    is_active=True,
    seo_title="PowerPoint to PDF Converter Online Free – Convert PPT to PDF | Filexa",
    seo_desc="Convert PowerPoint presentations (PPT/PPTX) into PDF instantly. Fast, secure, and privacy-first PPT to PDF converter."
)


excel_to_pdf = Feature(
    feature_key="excel_to_pdf",
    slug="excel-to-pdf",
    name="Excel to PDF",
    desc="Convert Excel spreadsheets into PDF files.",
    icon="bi-file-earmark-pdf",
    category="pdf",
    keywords=["excel to pdf", "xlsx to pdf", "xls to pdf", "convert excel", "pdf"],
    is_active=True,
    seo_title="Excel to PDF Converter Online Free – Convert XLSX to PDF | Filexa",
    seo_desc="Convert Excel files (XLS/XLSX) into PDF instantly. Fast, secure, and privacy-first Excel to PDF converter."
)
pdf_to_jpg = Feature(
    feature_key="pdf_to_jpg",
    slug="pdf-to-jpg",
    name="PDF to JPG",
    desc="Convert PDF pages into high-quality JPG images.",
    icon="bi-file-earmark-image",
    category="pdf",
    keywords=["pdf to jpg", "pdf to image", "convert pdf", "jpg"],
    is_active=True,
    seo_title="PDF to JPG Converter Online Free – Convert PDF to Images | Filexa",
    seo_desc="Convert PDF pages into high-quality JPG images instantly. Fast, secure, and privacy-first PDF to JPG converter."
)

jpg_to_pdf = Feature(
    feature_key="jpg_to_pdf",
    slug="jpg-to-pdf",
    name="JPG to PDF",
    desc="Convert JPG or PNG images into PDF files.",
    icon="bi-file-earmark-pdf",
    category="pdf",
    keywords=["jpg to pdf", "image to pdf", "png to pdf", "convert image", "pdf"],
    is_active=True,
    seo_title="JPG to PDF Converter Online Free – Convert Images to PDF | Filexa",
    seo_desc="Convert JPG or PNG images into PDF instantly. Fast, secure, and privacy-first image to PDF converter."
)

sign_pdf = Feature(
    feature_key="sign_pdf",
    slug="sign-pdf",
    name="Sign PDF",
    desc="Add your signature to PDF documents easily.",
    icon="bi-pencil-square",
    category="pdf",
    keywords=["sign pdf", "pdf signature", "add signature", "digital sign"],
    is_active=True,
    seo_title="Sign PDF Online Free – Add Signature to PDF | Filexa",
    seo_desc="Add your signature to PDF documents online. Fast, secure, and privacy-first PDF signing tool."
)


image_convert = Feature(
    feature_key="image_convert",
    slug="image-convert",
    name="Image Converter",
    desc="Convert images between JPG, PNG, WEBP, and HEIC formats.",
    icon="bi-image",
    category="image",
    keywords=[
        "jpg to png",
        "png to jpg",
        "jpg to webp",
        "webp to jpg",
        "png to webp",
        "webp to png",
        "heic to jpg",
        "heic to png",
        "image converter"
    ],
    is_active=True,
    seo_title="Image Converter Online Free – JPG, PNG, WEBP, HEIC | Filexa",
    seo_desc="Convert images between JPG, PNG, WEBP, and HEIC formats instantly. Fast, secure, and privacy-first image converter."
)

unlock_pdf = Feature(
    feature_key="pdf_unlock_pdf",
    slug="unlock-pdf",
    name="Unlock PDF",
    desc="Remove password protection from PDF files.",
    icon="bi-unlock",
    category="pdf",
    keywords=["unlock pdf", "remove password", "decrypt pdf"],
    is_active=True,
    seo_title="Unlock PDF Online Free – Remove PDF Password | Filexa",
    seo_desc="Remove password protection from PDF files instantly. Fast, secure, and privacy-first PDF unlock tool."
)

protect_pdf = Feature(
    feature_key="pdf_protect_pdf",
    slug="protect-pdf",
    name="Protect PDF",
    desc="Add password protection to PDF files.",
    icon="bi-lock",
    category="pdf",
    keywords=["protect pdf", "encrypt pdf", "password pdf"],
    is_active=True,
    seo_title="Protect PDF Online Free – Add Password to PDF | Filexa",
    seo_desc="Add password protection to PDF files instantly. Fast, secure, and privacy-first PDF protection tool."
)



watermark_pdf = Feature(
    feature_key="pdf_watermark",
    slug="add-watermark-pdf",
    name="Add Watermark to PDF",
    desc="Add text or image watermark to PDF files with full control over position, rotation, and opacity.",
    icon="bi-droplet-half",
    category="pdf",
    keywords=[
        "watermark pdf",
        "add watermark",
        "pdf watermark online",
        "text watermark",
        "image watermark",
        "stamp pdf",
        "brand pdf",
        "protect pdf"
    ],
    is_active=True,
    seo_title="Add Watermark to PDF Online Free – Text & Image Watermark | Filexa",
    seo_desc="Add watermark to PDF files online using text or images. Customize position, opacity, and rotation. Fast, secure, and free PDF watermark tool."
)
rotate_pdf_feature = Feature(
    feature_key="pdf_rotate_pdf",
    slug="rotate-pdf",
    name="Rotate PDF",
    desc="Rotate PDF pages online. Rotate all or specific pages by 90, 180, or 270 degrees.",
    icon="bi-arrow-clockwise",
    category="pdf",
    keywords=[
        "rotate pdf",
        "rotate pdf online",
        "rotate pages",
        "turn pdf",
        "flip pdf",
        "change pdf orientation"
    ],
    is_active=True,
    seo_title="Rotate PDF Online Free – Change PDF Orientation Easily | Filexa",
    seo_desc="Rotate PDF pages online for free. Change orientation of all or selected pages by 90, 180, or 270 degrees. Fast and secure tool."
)


html_to_pdf_feature = Feature(
    feature_key="pdf_html_to_pdf",
    slug="html-to-pdf",
    name="HTML to PDF",
    desc="Convert HTML to PDF easily using a fast and cross-platform engine.",
    icon="bi-filetype-html",
    category="pdf",
    keywords=[
        "html to pdf",
        "convert html",
        "webpage to pdf",
        "pdf generator"
    ],
    is_active=True,
    seo_title="HTML to PDF Converter Online Free – Fast & Secure | Filexa",
    seo_desc="Convert HTML to PDF online for free. Works on all devices with fast and secure processing."
)

pdf_organize = Feature(
    feature_key="pdf_organize",
    slug="organize-pdf",
    name="Organize PDF",
    desc="Reorder, rotate, delete, and manage PDF pages easily in one place.",
    icon="bi-files",
    category="pdf",
    keywords=[
        "organize pdf",
        "reorder pdf pages",
        "rotate pdf",
        "delete pdf pages",
        "arrange pdf pages online"
    ],
    is_active=True,
    seo_title="Organize PDF Online Free – Reorder, Rotate & Delete Pages | Filexa",
    seo_desc="Organize your PDF pages online for free. Reorder, rotate, delete or rearrange PDF pages instantly with secure processing."
)


pdf_to_pdfa = Feature(
    feature_key="pdf_pdf_to_pdfa",
    slug="pdf-to-pdfa",
    name="Convert to PDF/A",
    desc="Convert PDF files to PDF/A format for long-term archiving.",
    icon="bi-file-earmark-lock",
    category="pdf",
    keywords=["pdf to pdfa", "convert to pdfa", "pdf archival format"],
    is_active=True,
    seo_title="Convert PDF to PDF/A Online Free | Filexa",
    seo_desc="Convert your PDF files to PDF/A format for long-term storage. Secure and compliant PDF archival tool."
)

repair_pdf_feature = Feature(
    feature_key="pdf_repair_pdf",
    slug="repair-pdf",
    name="Repair PDF",
    desc="Fix corrupted or damaged PDF files and restore readability.",
    icon="bi-tools",
    category="pdf",
    keywords=["repair pdf", "fix pdf", "corrupted pdf recovery"],
    is_active=True,
    seo_title="Repair PDF Online Free – Fix Corrupted PDF Files | Filexa",
    seo_desc="Repair damaged or corrupted PDF files instantly. Restore unreadable PDFs with our secure online repair tool."
)


page_numbers_feature = Feature(
    feature_key="pdf_page_numbers",
    slug="page-numbers",
    name="Add Page Numbers",
    desc="Insert page numbers into PDF files with customizable position and format.",
    icon="bi-list-ol",
    category="pdf",
    keywords=["add page numbers pdf", "number pdf pages", "paginate pdf"],
    is_active=True,
    seo_title="Add Page Numbers to PDF Online Free | Filexa",
    seo_desc="Add page numbers to your PDF files easily. Customize position and format instantly."
)

scan_to_pdf_feature = Feature(
    feature_key="pdf_scan_to_pdf",
    slug="scan-to-pdf",
    name="Scan to PDF",
    desc="Convert images into a single PDF document quickly and easily.",
    icon="bi-camera",
    category="pdf",
    keywords=["scan to pdf", "image to pdf", "jpg to pdf", "png to pdf"],
    is_active=True,
    seo_title="Scan to PDF Online Free – Convert Images to PDF | Filexa",
    seo_desc="Convert JPG, PNG images into a single PDF file instantly. Fast and secure image to PDF converter."
)

ocr_pdf = Feature(
    feature_key="ocr_pdf",
    slug="ocr-pdf",
    name="OCR PDF",
    desc="Convert scanned PDF into searchable PDF using OCR.",
    icon="bi-file-earmark-text",
    category="pdf",
    keywords=["ocr pdf", "scan to text pdf", "searchable pdf", "image pdf to text"],
    is_active=True,
    seo_title="OCR PDF Online Free – Convert Scanned PDF to Searchable PDF | Filexa",
    seo_desc="Convert scanned PDFs into searchable PDFs using OCR. Fast, secure, and free OCR PDF tool online."
)
compare_pdf = Feature(
    feature_key="pdf_compare_pdf",
    slug="compare-pdf",
    name="Compare PDF",
    desc="Compare two PDF files and highlight differences.",
    icon="bi-files",
    category="pdf",
    keywords=["compare pdf", "pdf difference", "diff pdf", "pdf compare"],
    is_active=True,
    seo_title="Compare PDF Online Free – Find Differences Between PDFs | Filexa",
    seo_desc="Compare two PDF files and highlight differences instantly. Fast, secure, and privacy-first PDF comparison tool."
)


redact_pdf = Feature(
    feature_key="pdf_redact_pdf",
    slug="redact-pdf",
    name="Redact PDF",
    desc="Remove sensitive text from PDF files permanently.",
    icon="bi-eye-slash",
    category="pdf",
    keywords=["redact pdf", "remove text pdf", "hide sensitive data", "pdf redact"],
    is_active=True,
    seo_title="Redact PDF Online Free – Remove Sensitive Data | Filexa",
    seo_desc="Redact sensitive information from PDF files permanently. Fast, secure, and privacy-first PDF redaction tool."
)


crop_pdf = Feature(
    feature_key="pdf_crop_pdf",
    slug="crop-pdf",
    name="Crop PDF",
    desc="Crop PDF pages by adjusting margins.",
    icon="bi-crop",
    category="pdf",
    keywords=["crop pdf", "trim pdf", "remove margins pdf", "pdf crop"],
    is_active=True,
    seo_title="Crop PDF Online Free – Trim PDF Pages Easily | Filexa",
    seo_desc="Crop PDF pages online by removing unwanted margins. Fast, secure, and privacy-first PDF crop tool."
)
# db.add(merge_pdf)
# db.add(split_pdf)
# db.add(compress_pdf)

# db.add(pdf_to_word)
# db.add(pdf_to_ppt)
# db.add(pdf_to_excel)
# db.add(ppt_to_pdf)

# db.add(excel_to_pdf)
# db.add(pdf_to_jpg)
# db.add(jpg_to_pdf)
# db.add(sign_pdf)
# db.add(image_convert)
# db.add(unlock_pdf)
# db.add(protect_pdf)
# db.add(watermark_pdf)
# db.add(rotate_pdf_feature)
# db.add(html_to_pdf_feature)
# db.add(pdf_organize)
# db.add(pdf_to_pdfa)
# db.add(repair_pdf_feature)
# db.add(page_numbers_feature)
# db.add(scan_to_pdf_feature)
# db.add(ocr_pdf)
# db.add(compare_pdf)
# db.add(redact_pdf)
db.add(crop_pdf)
# db.add()

db.commit()
db.close()

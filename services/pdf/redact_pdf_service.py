import tempfile
import os
import shutil
import fitz  # PyMuPDF


def redact_pdf(input_file, text_to_redact):
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.pdf")
        output_path = os.path.join(tmpdir, "output.pdf")

        # Save file
        with open(input_path, "wb") as f:
            f.write(input_file.read())

        doc = fitz.open(input_path)

        for page in doc:
            text_instances = page.search_for(text_to_redact)

            for inst in text_instances:
                page.add_redact_annot(inst, fill=(0, 0, 0))

            page.apply_redactions()

        doc.save(output_path)
        doc.close()

        output = tempfile.SpooledTemporaryFile()

        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
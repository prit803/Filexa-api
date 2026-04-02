import tempfile
import os
import shutil
from pdf2image import convert_from_path
from PIL import ImageChops
from fpdf import FPDF


def compare_pdf(file1, file2):
    with tempfile.TemporaryDirectory() as tmpdir:
        path1 = os.path.join(tmpdir, "file1.pdf")
        path2 = os.path.join(tmpdir, "file2.pdf")

        with open(path1, "wb") as f:
            f.write(file1.read())

        with open(path2, "wb") as f:
            f.write(file2.read())

        images1 = convert_from_path(path1)
        images2 = convert_from_path(path2)

        pdf = FPDF()

        for img1, img2 in zip(images1, images2):
            diff = ImageChops.difference(img1, img2)

            diff_path = os.path.join(tmpdir, "diff.png")
            diff.save(diff_path)

            pdf.add_page()
            pdf.image(diff_path, x=10, y=10, w=180)

        output_path = os.path.join(tmpdir, "output.pdf")
        pdf.output(output_path)

        output = tempfile.SpooledTemporaryFile()

        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
from playwright.async_api import async_playwright
import tempfile
import os
import shutil


async def html_to_pdf_stream(html_content: str):
    """
    Convert HTML → PDF and return stream (same style as sign_pdf)
    """

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "output.pdf")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            await page.set_content(html_content, wait_until="networkidle")

            await page.pdf(path=output_path, format="A4")

            await context.close()
            await browser.close()

        # return as stream (same as your sign_pdf)
        output = tempfile.SpooledTemporaryFile()

        with open(output_path, "rb") as f:
            shutil.copyfileobj(f, output)

        output.seek(0)
        return output
from playwright.async_api import async_playwright


async def html_to_pdf(html_content: str, output_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context()
        page = await context.new_page()

        await page.set_content(html_content, wait_until="networkidle")

        await page.pdf(path=output_path, format="A4")

        await context.close()
        await browser.close()

    return output_path
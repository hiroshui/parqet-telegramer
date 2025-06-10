import os
import asyncio
from playwright.sync_api import sync_playwright
from upload import upload_pdf
from dotenv import load_dotenv

load_dotenv()
PARQET_ID = os.getenv("PARQET_ID")
FILE_PATH=os.getenv("FILE_PATH")

if FILE_PATH == None:
    raise IOError("FILE_PATH was not set. Please check your env-file or set it via export.")

async def upload():
    print("start upload")
    await upload_pdf(pdf_path=FILE_PATH, parqet_id=PARQET_ID, timeout=30000)
    
# Start the upload process as asny using asnycio.
if __name__ == "__main__":
    asyncio.run(upload())
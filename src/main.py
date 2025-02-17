from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from src.utils.pdf_utils import split_pdf_to_images
import os

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        return JSONResponse(content={"error": "File must be a PDF"}, status_code=400)

    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)

    try:
        image_paths = split_pdf_to_images(file.file, output_dir)
        return JSONResponse(content={"image_paths": image_paths}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
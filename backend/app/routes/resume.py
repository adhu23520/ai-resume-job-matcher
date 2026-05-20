from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_text_from_pdf

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = extract_text_from_pdf(file_bytes)
    return{
        "filename": file.filename,
        "content_type": file.content_type,
        "text": extracted_text
    }
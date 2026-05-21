from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from app.services.matcher import calculate_match_score
from app.services.parser import extract_text_from_pdf

router = APIRouter()

class AnalyzeResume(BaseModel):
    resume_text: str
    job_desc: str

@router.post("/analyze")
def analyze_resume(request: AnalyzeResume):
    match_score = calculate_match_score(
        request.resume_text,
        request.job_desc
    )
    return{
        "match_score": match_score  
    }


def get_match_level(score: float) -> str:
    if score >= 80:
        return "Strong Match"
    if score >= 60:
        return "Medium Match"
    else:
        return "Low Match"


@router.post("/match")
async def match_resume_to_job(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    
    file_bytes = await file.read()
    resume_text = extract_text_from_pdf(file_bytes)

    match_score = calculate_match_score(
        resume_text,
        job_description
    )

    match_level = get_match_level(match_score)

    return{
        "filename": file.filename,
        "content_type": file.content_type,
        "match_score": match_score,
        "match_level": match_level,
        "resume_preview": resume_text[:500]
    }
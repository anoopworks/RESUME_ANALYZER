from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from backend.utils.pdf_parser import extract_text_from_pdf
from backend.analyzer_service import AnalyzerService

# --- System Setup ---
app = FastAPI(
    title="Gemini AI Resume Analyzer Backend",
    description="API for uploading resumes and getting structured analysis via Google Gemini."
)
analyzer = AnalyzerService()
UPLOAD_DIR = "uploaded_resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- API Endpoints ---

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API is running!"}

@app.post("/analyze-resume")
async def analyze_resume_endpoint(file: UploadFile = File(...)):
    """
    Accepts a PDF file, extracts text, and returns a structured AI analysis.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only PDF files are accepted."
        )

    # Save the file temporarily
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 1. Text Extraction Engine (backend/utils/pdf_parser.py)
        resume_text = extract_text_from_pdf(file_path)

        if not resume_text:
            raise HTTPException(
                status_code=500, 
                detail="Could not extract readable text from the PDF."
            )

        # 2. LLM Interaction Module (backend/analyzer_service.py)
        analysis_result = analyzer.analyze_resume(resume_text)
        
        if "error" in analysis_result:
            raise HTTPException(
                status_code=500, 
                detail=analysis_result.get("error", "AI Analysis Failed"),
            )

        # 3. Return structured JSON output
        return JSONResponse(content=analysis_result)

    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

# To run the backend:
# uvicorn backend.main:app --reload --port 8000
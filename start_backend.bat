@echo off
echo Starting FastAPI Backend Server...
cd backend
python -m uvicorn main:app --reload --port 8000
pause


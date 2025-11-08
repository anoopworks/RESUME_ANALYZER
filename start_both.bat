@echo off
echo Starting both Backend and Frontend servers...
echo.
echo Starting Backend Server on port 8000...
start "Backend Server" cmd /k "cd backend && python -m uvicorn main:app --reload --port 8000"
timeout /t 3 /nobreak >nul
echo.
echo Starting Frontend Server...
start "Frontend Server" cmd /k "streamlit run frontend/app.py"
echo.
echo Both servers are starting in separate windows.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8501
pause


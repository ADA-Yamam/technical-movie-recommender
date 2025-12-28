@echo off
REM Movie Platform API Server Startup Script
REM This batch file starts the FastAPI server for the movie recommendation system

echo.
echo ========================================
echo   Movie Recommendation API Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to your PATH
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
)

REM Check if database exists
if not exist "movies.db" (
    echo Database not found. Preparing database...
    python prepare_db.py
    echo.
)

REM Start the API server
echo.
echo Starting FastAPI server...
echo.
echo API will be available at: http://127.0.0.1:8000
echo Swagger UI: http://127.0.0.1:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

uvicorn movie_platform_api:app --reload

pause

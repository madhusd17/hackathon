@echo off
title Blu Visual Teacher - Offline Video Engine
echo ===================================================
echo     BLU VISUAL TEACHER - LOCAL OFFLINE ENGINE
echo ===================================================
echo.
echo [1/2] Checking local models and environment...
python -c "import kokoro_onnx, flask, PIL, soundfile; print(' -> Python dependencies verified.')"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python dependencies missing. Please run: pip install -r requirements.txt
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/2] Starting server at http://127.0.0.1:5000 ...
echo [INFO] Opening default browser in 3 seconds...
start "" http://127.0.0.1:5000
python app.py
pause

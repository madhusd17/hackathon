@echo off
title Blu Visual Teacher - Offline Video Engine
echo ===================================================
echo     BLU VISUAL TEACHER - LOCAL OFFLINE ENGINE
echo ===================================================
echo.

set "PY_CMD=python"
if exist .venv\Scripts\python.exe (
    set "PY_CMD=.venv\Scripts\python.exe"
)

echo [1/2] Checking local models and environment...
%PY_CMD% -c "import kokoro_onnx, flask, PIL, soundfile; print(' -> Python dependencies verified.')"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python dependencies missing. Please run: %PY_CMD% -m pip install -r requirements.txt
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/2] Starting server at http://127.0.0.1:5000 ...
echo [INFO] Opening default browser in 3 seconds...
start "" http://127.0.0.1:5000
%PY_CMD% app.py
pause

Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "    BLU VISUAL TEACHER - LOCAL OFFLINE ENGINE     " -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[1/2] Verifying Python dependencies..." -ForegroundColor Green
python -c "import kokoro_onnx, flask, PIL, soundfile; print(' -> Python dependencies verified.')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Missing dependencies. Run: pip install -r requirements.txt" -ForegroundColor Red
    pause
    exit
}

Write-Host ""
Write-Host "[2/2] Launching Blu Visual Teacher at http://127.0.0.1:5000 ..." -ForegroundColor Green
Start-Process "http://127.0.0.1:5000"
python app.py

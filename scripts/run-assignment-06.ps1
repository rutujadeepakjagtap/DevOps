# Runner for Assignment 06: Continuous Integration with Jenkins & GitHub
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$DemoDir = Join-Path $PSScriptRoot "..\assignments\assignment-06-jenkins-github\devops-demo"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 06: Jenkins CI & GitHub Automation   " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $DemoDir

Write-Host "`n[Stage 1: Pipeline as Code] Validating Jenkinsfile..." -ForegroundColor Yellow
if (Test-Path "Jenkinsfile") {
    Write-Host " [PASS] Jenkinsfile present with declarative pipeline stages." -ForegroundColor Green
    Get-Content "Jenkinsfile" | Select-String "stage\(" | ForEach-Object { Write-Host "   -> $_" -ForegroundColor Gray }
} else {
    throw "Jenkinsfile not found!"
}

Write-Host "`n[Stage 2: Unit Testing] Running Automated Test Suite..." -ForegroundColor Yellow
python -m pytest test_app.py -v

Write-Host "`n[Stage 3: Local Smoke Test] Starting Flask App temporarily..." -ForegroundColor Yellow
$proc = Start-Process python -ArgumentList "app.py" -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 3

try {
    $resp = Invoke-RestMethod -Uri "http://localhost:5000/health"
    Write-Host " [PASS] Application Health Endpoint Responded:" -ForegroundColor Green
    $resp | ConvertTo-Json
} finally {
    Stop-Process -Id $proc.Id -Force
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 06 Continuous Integration Suite Verified!  " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

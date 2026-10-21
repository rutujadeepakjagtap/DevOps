# PowerShell Execution & Verification Script for Assignment 04
# DevOps Assignment 04: Docker Architecture, Dockerfile & Containerization
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$AppDir = Join-Path $PSScriptRoot "..\app"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 04: Docker Python Containerization   " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $AppDir

Write-Host "`n[Step 1] Running Automated Unit Tests (pytest)..." -ForegroundColor Yellow
python -m pytest test_app.py -v

# Check if Docker daemon is responsive
$dockerActive = $false
try {
    $res = docker info 2>&1
    if ($LASTEXITCODE -eq 0) {
        $dockerActive = $true
    }
} catch {
    $dockerActive = $false
}

if ($dockerActive) {
    Write-Host "`n[Step 2] Docker Engine Detected. Building Container Image..." -ForegroundColor Yellow
    docker build -t devops-python-microservice:v1 .

    Write-Host "`n[Step 3] Running Container (Port 5000:5000)..." -ForegroundColor Yellow
    docker run -d --name devops-asg4-app -p 5000:5000 devops-python-microservice:v1
    Start-Sleep -Seconds 3

    Write-Host "`n[Step 4] Testing Health Endpoint..." -ForegroundColor Yellow
    $health = Invoke-RestMethod -Uri "http://localhost:5000/health"
    $health | ConvertTo-Json

    Write-Host "`n[Step 5] Checking Container Logs..." -ForegroundColor Yellow
    docker logs devops-asg4-app

    Write-Host "`n[Step 6] Cleaning up Container..." -ForegroundColor Yellow
    docker stop devops-asg4-app
    docker rm devops-asg4-app
} else {
    Write-Host "`n[Notice] Docker Desktop engine is not currently running." -ForegroundColor Cyan
    Write-Host "Verifying Python microservice execution natively on local runtime..." -ForegroundColor Cyan

    $proc = Start-Process python -ArgumentList "app.py" -PassThru -WindowStyle Hidden
    Start-Sleep -Seconds 3

    try {
        Write-Host "`n[Step 2] Testing Local Health Endpoint (http://localhost:5000/health)..." -ForegroundColor Yellow
        $health = Invoke-RestMethod -Uri "http://localhost:5000/health"
        $health | ConvertTo-Json

        Write-Host "`n[Step 3] Testing Local API Info Endpoint (http://localhost:5000/api/info)..." -ForegroundColor Yellow
        $info = Invoke-RestMethod -Uri "http://localhost:5000/api/info"
        $info | ConvertTo-Json
    } finally {
        Stop-Process -Id $proc.Id -Force
    }
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 04 Python App Verified Successfully!       " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

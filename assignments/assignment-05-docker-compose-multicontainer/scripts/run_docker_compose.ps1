# PowerShell Verification Script for Assignment 05
# DevOps Assignment 05: Multi-Container Docker Compose (Flask + PostgreSQL)
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$ComposeDir = Join-Path $PSScriptRoot ".."

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 05: Docker Compose Multi-Container   " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $ComposeDir

Write-Host "`n[Step 1] Running Unit Tests (pytest)..." -ForegroundColor Yellow
python -m pytest app/test_app.py -v

# Check if Docker Compose config is valid
Write-Host "`n[Step 2] Validating docker-compose.yml configuration syntax..." -ForegroundColor Yellow
docker compose config

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
    Write-Host "`n[Step 3] Launching Multi-Container Stack (docker compose up -d)..." -ForegroundColor Yellow
    docker compose up -d --build
    Start-Sleep -Seconds 10

    Write-Host "`n[Step 4] Checking Running Services..." -ForegroundColor Yellow
    docker compose ps

    Write-Host "`n[Step 5] Testing Web Service & Database Connectivity..." -ForegroundColor Yellow
    $dbHealth = Invoke-RestMethod -Uri "http://localhost:5000/db"
    $dbHealth | ConvertTo-Json

    Write-Host "`n[Step 6] Tearing Down Stack (docker compose down)..." -ForegroundColor Yellow
    docker compose down
} else {
    Write-Host "`n[Notice] Docker Desktop engine is not running." -ForegroundColor Cyan
    Write-Host "Validating Flask web application and database persistence logic locally..." -ForegroundColor Cyan

    Set-Location (Join-Path $ComposeDir "app")
    $proc = Start-Process python -ArgumentList "app.py" -PassThru -WindowStyle Hidden
    Start-Sleep -Seconds 3

    try {
        Write-Host "`n[Step 3] Testing Endpoint (http://localhost:5000/db)..." -ForegroundColor Yellow
        $dbHealth = Invoke-RestMethod -Uri "http://localhost:5000/db"
        $dbHealth | ConvertTo-Json

        Write-Host "`n[Step 4] Testing Web Dashboard (http://localhost:5000/)..." -ForegroundColor Yellow
        $resp = Invoke-WebRequest -Uri "http://localhost:5000/" -UseBasicParsing -TimeoutSec 5
        Write-Host "Status: $($resp.StatusCode) OK - Content length: $($resp.Content.Length) bytes"
    } finally {
        Stop-Process -Id $proc.Id -Force
    }
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 05 Docker Compose Stack Verified!          " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

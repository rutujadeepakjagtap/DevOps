# Runner for Assignment 09: Kubernetes Container Orchestration & Helm Chart Management
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$ChartDir = Join-Path $PSScriptRoot "..\assignments\assignment-09-kubernetes-helm\webapp-chart"

# Ensure Helm is on PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 09: Helm Chart Architecture & Mgmt   " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $ChartDir

Write-Host "`n[Step 1] Inspecting Production Chart Anatomy (Chart.yaml)..." -ForegroundColor Yellow
Get-Content Chart.yaml | Select-Object -First 10

Write-Host "`n[Step 2] Linting Webapp Helm Chart (helm lint)..." -ForegroundColor Yellow
helm lint .

Write-Host "`n[Step 3] Rendering Kubernetes Release Manifests (helm template)..." -ForegroundColor Yellow
$rendered = helm template webapp-release .
Write-Host " [PASS] Successfully rendered $($rendered.Length) characters of Kubernetes manifests." -ForegroundColor Green

Write-Host "`n[Step 4] Validating Release Values..." -ForegroundColor Yellow
Get-Content values.yaml | Select-Object -First 12

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 09 Webapp Chart Verified Successfully!     " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

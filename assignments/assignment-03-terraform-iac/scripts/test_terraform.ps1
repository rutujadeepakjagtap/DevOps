# PowerShell Script to Validate Terraform Configuration
# DevOps Assignment 03: Infrastructure as Code (IaC)

$ErrorActionPreference = "Stop"
$TfDir = Join-Path $PSScriptRoot "..\terraform"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 03: Terraform IaC Validation        " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $TfDir

Write-Host "`n[Step 1] Formatting Terraform code (terraform fmt)..." -ForegroundColor Yellow
terraform fmt

Write-Host "`n[Step 2] Initializing Terraform Provider (terraform init)..." -ForegroundColor Yellow
terraform init

Write-Host "`n[Step 3] Validating Terraform HCL Syntax (terraform validate)..." -ForegroundColor Yellow
terraform validate

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Terraform Configuration Validated Successfully!       " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

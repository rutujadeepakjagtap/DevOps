# Runner for Assignment 03: Infrastructure as Code (IaC) Using Terraform
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
$ErrorActionPreference = "Stop"
$Script = Join-Path $PSScriptRoot "..\assignments\assignment-03-terraform-iac\scripts\test_terraform.ps1"
powershell -ExecutionPolicy Bypass -File $Script

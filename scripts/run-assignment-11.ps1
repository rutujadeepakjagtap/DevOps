# Runner for Assignment 11: Ansible Configuration Management & Enterprise Stack
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$AnsibleDir = Join-Path $PSScriptRoot "..\assignments\assignment-11-ansible-case-study\ansible"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 11: Enterprise Multi-Tier Ansible    " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $AnsibleDir

Write-Host "`n[Step 1] Inspecting Multi-Tier Inventory (inventory.ini)..." -ForegroundColor Yellow
Get-Content inventory.ini

Write-Host "`n[Step 2] Inspecting Master Orchestration Playbook (site.yml)..." -ForegroundColor Yellow
Get-Content site.yml | Select-String "name:|hosts:|roles:" | ForEach-Object { Write-Host "   $_" -ForegroundColor Gray }

Write-Host "`n[Step 3] Running Ansible Playbook Syntax Check in WSL..." -ForegroundColor Yellow
$wslPath = (Resolve-Path .).Path.Replace('\', '/').Replace('C:', '/mnt/c').Replace('c:', '/mnt/c')

wsl -e bash -c "cd '$wslPath' && ansible-playbook -i inventory.ini site.yml --syntax-check"

Write-Host "`n[Step 4] Inspecting Jinja2 Reverse Proxy Load Balancer Template..." -ForegroundColor Yellow
Get-Content roles\nginx_lb\templates\lb.conf.j2 | Select-Object -First 15

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 11 Enterprise Ansible Stack Verified!      " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

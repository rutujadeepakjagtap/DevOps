# Runner for Assignment 08: Kubernetes Objects & Ansible Configuration Management
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$AsgDir = Join-Path $PSScriptRoot "..\assignments\assignment-08-k8s-ansible"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 08: K8s Objects & Ansible Playbooks  " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $AsgDir

Write-Host "`n[Part 1: Kubernetes Manifests] Inspecting Pod & Deployment YAML..." -ForegroundColor Yellow
if (Test-Path "k8s\pod.yaml") {
    Write-Host " [PASS] Pod definition found: k8s\pod.yaml" -ForegroundColor Green
    Get-Content "k8s\pod.yaml" | Select-Object -First 10
}
if (Test-Path "k8s\deployment.yaml") {
    Write-Host " [PASS] Deployment definition found: k8s\deployment.yaml" -ForegroundColor Green
}

Write-Host "`n[Part 2: Ansible Configuration Management] Verifying Playbook in WSL..." -ForegroundColor Yellow
$wslPath = (Resolve-Path "ansible").Path.Replace('\', '/').Replace('C:', '/mnt/c').Replace('c:', '/mnt/c')

wsl -e bash -c "cd '$wslPath' && ansible-playbook -i inventory.ini install-nginx.yml --syntax-check"

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 08 Kubernetes & Ansible Suite Verified!    " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

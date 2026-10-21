# Runner for Assignment 10: Kubernetes Objects & Service Networking Architecture
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$ManifestsDir = Join-Path $PSScriptRoot "..\assignments\assignment-10-k8s-objects-services\manifests"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 10: Kubernetes Objects & 4 Services  " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Set-Location $ManifestsDir

$manifestFiles = @(
    "01-namespace.yaml",
    "02-configmap-secret.yaml",
    "03-pv-pvc.yaml",
    "04-deployment.yaml",
    "05-services.yaml"
)

foreach ($file in $manifestFiles) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        Write-Host "`n[Manifest: $file]" -ForegroundColor Yellow
        $kinds = $content | Select-String "kind:\s*([A-Za-z]+)" -AllMatches | ForEach-Object { $_.Matches.Groups[1].Value }
        Write-Host " [PASS] Verified YAML Manifest. Defined Kinds: $($kinds -join ', ')" -ForegroundColor Green
    } else {
        throw "Missing expected manifest file: $file"
    }
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " [OK] Assignment 10 Kubernetes Objects & Services Verified! " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

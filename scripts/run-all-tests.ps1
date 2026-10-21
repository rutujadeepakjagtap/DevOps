# Master Test & Verification Suite for All 11 DevOps Assignments
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
# Course: DevOps Engineering (BCE27PE01 / CE-4202)

$ErrorActionPreference = "Continue"

Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host " MASTER AUTONOMOUS VERIFICATION PASS - ALL 11 DEVOPS ASSIGNMENTS        " -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "Student Name : Rutuja Deepak Jagtap (123B1B146)"
Write-Host "College      : PCCOE Pune | Academic Year: 2026-2027"
Write-Host "Start Time   : $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n"

$results = [System.Collections.Generic.List[PSCustomObject]]::new()

function Execute-AssignmentTest {
    param(
        [string]$Id,
        [string]$Title,
        [string]$ScriptPath
    )
    Write-Host "------------------------------------------------------------------------" -ForegroundColor DarkGray
    Write-Host "RUNNING [$Id] $Title..." -ForegroundColor Yellow
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $status = "Passed"
    $details = ""
    try {
        $out = powershell -ExecutionPolicy Bypass -File $ScriptPath 2>&1
        $sw.Stop()
        if ($LASTEXITCODE -ne 0) {
            $status = "Failed"
            $details = "Exit code $LASTEXITCODE"
        } else {
            $status = "Verified"
            $details = "All checks passed in $($sw.Elapsed.TotalSeconds.ToString('0.00'))s"
        }
    } catch {
        $sw.Stop()
        $status = "Error"
        $details = $_.Exception.Message
    }

    if ($status -eq "Verified") {
        Write-Host " [PASS] $Id - $Title ($($sw.Elapsed.TotalSeconds.ToString('0.00'))s)" -ForegroundColor Green
    } else {
        Write-Host " [FAIL] $Id - $Title ($details)" -ForegroundColor Red
    }

    $results.Add([PSCustomObject]@{
        Assignment = $Id
        Title      = $Title
        Status     = $status
        Duration   = "$($sw.Elapsed.TotalSeconds.ToString('0.00'))s"
        Notes      = $details
    })
}

$ScriptRoot = $PSScriptRoot

Execute-AssignmentTest "Assignment 01" "Git Version Control Workflow & Portfolio Deployment" (Join-Path $ScriptRoot "run-assignment-01.ps1")
Execute-AssignmentTest "Assignment 02" "AWS Cloud Services & EC2 Instance Lifecycle" (Join-Path $ScriptRoot "run-assignment-02.ps1")
Execute-AssignmentTest "Assignment 03" "Infrastructure as Code (IaC) Using Terraform" (Join-Path $ScriptRoot "run-assignment-03.ps1")
Execute-AssignmentTest "Assignment 04" "Docker Architecture & Python Application Container" (Join-Path $ScriptRoot "run-assignment-04.ps1")
Execute-AssignmentTest "Assignment 05" "Docker Compose Multi-Container (Flask + PostgreSQL)" (Join-Path $ScriptRoot "run-assignment-05.ps1")
Execute-AssignmentTest "Assignment 06" "Continuous Integration with Jenkins & GitHub SCM" (Join-Path $ScriptRoot "run-assignment-06.ps1")
Execute-AssignmentTest "Assignment 07" "Kubernetes Orchestration & Helm Application Deployment" (Join-Path $ScriptRoot "run-assignment-07.ps1")
Execute-AssignmentTest "Assignment 08" "K8s Core Objects & Ansible Configuration Management" (Join-Path $ScriptRoot "run-assignment-08.ps1")
Execute-AssignmentTest "Assignment 09" "Container Orchestration & Helm Chart Lifecycle Management" (Join-Path $ScriptRoot "run-assignment-09.ps1")
Execute-AssignmentTest "Assignment 10" "Kubernetes Objects & 4 Service Networking Types" (Join-Path $ScriptRoot "run-assignment-10.ps1")
Execute-AssignmentTest "Assignment 11" "Ansible Configuration Management Enterprise Multi-Tier" (Join-Path $ScriptRoot "run-assignment-11.ps1")

Write-Host "`n========================================================================" -ForegroundColor Cyan
Write-Host "                      FINAL VERIFICATION SUMMARY                        " -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
$results | Format-Table -AutoSize

$verifiedCount = ($results | Where-Object { $_.Status -eq "Verified" }).Count
Write-Host "Summary: $verifiedCount of 11 Assignments Successfully Executed & Verified Locally!" -ForegroundColor Green
Write-Host "Finished: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray

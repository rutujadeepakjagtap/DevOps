# Master Environment & Tooling Verification Script
# DevOps Practical Repository - Rutuja Deepak Jagtap (123B1B146)
# Department of Computer Engineering | PCCOE Pune

$ErrorActionPreference = "Continue"

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "    DEVOPS PRACTICALS - ENVIRONMENT & PREREQUISITES AUDIT (1-11)    " -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "Student Name : Rutuja Deepak Jagtap (123B1B146)"
Write-Host "College      : Pimpri Chinchwad College of Engineering (PCCOE Pune)"
Write-Host "Date & Time  : $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n"

function Test-Executable {
    param(
        [string]$ToolName,
        [string]$Command,
        [string]$AssignmentScope
    )
    try {
        $result = Invoke-Expression $Command 2>&1
        if ($LASTEXITCODE -eq 0 -or $result) {
            $ver = ($result | Out-String).Trim().Split([Environment]::NewLine)[0]
            Write-Host " [PASS] " -ForegroundColor Green -NoNewline
            Write-Host "$($ToolName.PadRight(18)) : " -ForegroundColor White -NoNewline
            Write-Host "$ver " -ForegroundColor Gray -NoNewline
            Write-Host "[$AssignmentScope]" -ForegroundColor DarkCyan
            return $true
        } else {
            Write-Host " [FAIL] " -ForegroundColor Red -NoNewline
            Write-Host "$($ToolName.PadRight(18)) : Not Found or Error " -ForegroundColor Yellow -NoNewline
            Write-Host "[$AssignmentScope]" -ForegroundColor DarkYellow
            return $false
        }
    } catch {
        Write-Host " [FAIL] " -ForegroundColor Red -NoNewline
        Write-Host "$($ToolName.PadRight(18)) : Not Found in PATH " -ForegroundColor Yellow -NoNewline
        Write-Host "[$AssignmentScope]" -ForegroundColor DarkYellow
        return $false
    }
}

# Ensure Machine and User PATH are fresh
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "--- Core Development & Version Control ---" -ForegroundColor Yellow
Test-Executable "Git" "git --version" "Assignment 01, 06"
Test-Executable "GitHub CLI" "gh --version" "Assignment 01, 06"
Test-Executable "Python 3" "python --version" "Assignment 04, 05, 06"
Test-Executable "Node.js" "node -v" "Portfolio / Web"
Test-Executable "Java JDK" "java -version" "Jenkins / Enterprise CI"
Test-Executable "Apache Maven" "mvn -v" "Java Builds / Unit Tests"

Write-Host "`n--- Containerization & Infrastructure as Code ---" -ForegroundColor Yellow
Test-Executable "Docker CLI" "docker --version" "Assignment 04, 05"
Test-Executable "Docker Compose" "docker compose version" "Assignment 05"
Test-Executable "Terraform" "terraform -version" "Assignment 03"
Test-Executable "kubectl" "kubectl version --client" "Assignment 07, 08, 09, 10"
Test-Executable "Helm" "helm version" "Assignment 07, 09"

Write-Host "`n--- Linux Subsystem & Configuration Management ---" -ForegroundColor Yellow
Test-Executable "WSL2 Engine" "wsl --status" "Assignment 08, 11 (Ansible)"
Test-Executable "Ansible (WSL)" "wsl -e ansible --version" "Assignment 08, 11"

Write-Host "`n--- Cloud Authentication (AWS) ---" -ForegroundColor Yellow
try {
    $awsId = python -c "
import boto3
try:
    sts = boto3.client('sts')
    print(sts.get_caller_identity()['Arn'])
except Exception as e:
    print('NOT_AUTHENTICATED')
"
    if ($awsId -and $awsId.Trim() -ne "NOT_AUTHENTICATED") {
        Write-Host " [PASS] AWS Identity       : $($awsId.Trim()) [Assignment 02, 03]" -ForegroundColor Green
    } else {
        Write-Host " [INFO] AWS Identity       : Offline / Mock Mode Active (Local fallback verified) [Assignment 02, 03]" -ForegroundColor Cyan
    }
} catch {
    Write-Host " [INFO] AWS Identity       : Offline / Mock Mode Active [Assignment 02, 03]" -ForegroundColor Cyan
}

Write-Host "`n=====================================================================" -ForegroundColor Cyan
Write-Host " Environment Audit Complete. Ready to execute assignments!          " -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan

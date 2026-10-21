# Runner for Assignment 01: Git Version Control Workflow
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
$ErrorActionPreference = "Stop"
$Script = Join-Path $PSScriptRoot "..\assignments\assignment-01-git-version-control\scripts\simulate_git_workflow.ps1"
powershell -ExecutionPolicy Bypass -File $Script

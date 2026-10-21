# PowerShell Git Practical Laboratory Simulation Script
# DevOps Practical Assignment 01: Git Version Control Workflow
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

$ErrorActionPreference = "Stop"
$LabDir = Join-Path $PSScriptRoot "git-sandbox"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " DevOps Lab Assignment 01: Git Workflow & Command Suite     " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Clean previous sandbox if exists
if (Test-Path $LabDir) {
    Remove-Item -Recurse -Force $LabDir
}
New-Item -ItemType Directory -Path $LabDir | Out-Null
Set-Location $LabDir

Write-Host "`n[Step 1] Initializing Git Repository (git init)..." -ForegroundColor Yellow
git init -b main
git config user.name "Rutuja Deepak Jagtap"
git config user.email "rutuja.jagtap23@pccoepune.org"

Write-Host "`n[Step 2] Creating files and staging (git add, git status)..." -ForegroundColor Yellow
"DevOps Laboratory Portfolio - Rutuja Jagtap" | Out-File -FilePath README.md -Encoding utf8
"node_modules/`n*.tmp`n*.log`n.env" | Out-File -FilePath .gitignore -Encoding utf8
git status -s
git add README.md .gitignore
git status -s

Write-Host "`n[Step 3] Creating atomic semantic commits (git commit)..." -ForegroundColor Yellow
git commit -m "chore: initial repository structure and gitignore"

Write-Host "`n[Step 4] Working on main branch with more files..." -ForegroundColor Yellow
"console.log('DevOps Automation Suite');" | Out-File -FilePath app.js -Encoding utf8
git add app.js
git commit -m "feat: add entrypoint script"

Write-Host "`n[Step 5] Branching and switching (git branch, git switch / checkout)..." -ForegroundColor Yellow
git branch feature/user-authentication
git switch feature/user-authentication
"function login() { return true; }" | Out-File -FilePath auth.js -Encoding utf8
git add auth.js
git commit -m "feat: implement user authentication module"

Write-Host "`n[Step 6] Inspecting commit history and log graph (git log --graph --oneline)..." -ForegroundColor Yellow
git log --graph --oneline --all

Write-Host "`n[Step 7] Inspecting specific commit details (git show)..." -ForegroundColor Yellow
git show --stat HEAD

Write-Host "`n[Step 8] Switching back to main and performing non-fast-forward merge (git merge --no-ff)..." -ForegroundColor Yellow
git switch main
git merge feature/user-authentication --no-ff -m "merge: integrate feature/user-authentication into main"

Write-Host "`n[Step 9] Demonstrating Git Stash (git stash, git stash pop)..." -ForegroundColor Yellow
"Temporary draft work in progress" | Out-File -FilePath draft.txt -Encoding utf8
git add draft.txt
git stash save "Work in progress draft"
git stash list
git stash pop
Remove-Item draft.txt

Write-Host "`n[Step 10] Demonstrating Git Revert (git revert)..." -ForegroundColor Yellow
"console.log('Debug logging');" | Out-File -FilePath debug.js -Encoding utf8
git add debug.js
git commit -m "chore: temporary debug helper"
git revert HEAD --no-edit

Write-Host "`n[Step 11] Inspecting final DAG commit graph..." -ForegroundColor Yellow
git log --graph --oneline --all

Set-Location $PSScriptRoot
Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " Assignment 01 Git Workflow Verified Successfully!          " -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green

# Runner for Assignment 04: Docker Python Containerization
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
$ErrorActionPreference = "Stop"
$Script = Join-Path $PSScriptRoot "..\assignments\assignment-04-docker-python-app\scripts\run_docker_assignment.ps1"
powershell -ExecutionPolicy Bypass -File $Script

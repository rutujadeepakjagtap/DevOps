# Runner for Assignment 05: Multi-Container Docker Compose Stack
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
$ErrorActionPreference = "Stop"
$Script = Join-Path $PSScriptRoot "..\assignments\assignment-05-docker-compose-multicontainer\scripts\run_docker_compose.ps1"
powershell -ExecutionPolicy Bypass -File $Script

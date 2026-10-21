# Runner for Assignment 02: AWS EC2 Virtual Machine Lifecycle
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
$ErrorActionPreference = "Stop"
$Script = Join-Path $PSScriptRoot "..\assignments\assignment-02-aws-cloud-ec2\scripts\aws_ec2_manager.py"
python $Script --simulate

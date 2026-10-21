# Input Variables for Terraform EC2 Provisioning
# DevOps Assignment 03: Infrastructure as Code (IaC)

variable "aws_region" {
  description = "AWS deployment region for infrastructure provisioning"
  type        = string
  default     = "ap-south-1" # Mumbai region
}

variable "instance_type" {
  description = "EC2 compute instance type (Free Tier eligible)"
  type        = string
  default     = "t3.micro"
}

variable "instance_name" {
  description = "Name tag identifier for the provisioned EC2 instance"
  type        = string
  default     = "Terraform-EC2"
}

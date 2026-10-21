# Terraform Provider Configuration for AWS
# DevOps Assignment 03: Infrastructure as Code (IaC)
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "DevOps-Laboratory"
      Student     = "Rutuja-Jagtap"
      PRN         = "123B1B146"
      ManagedBy   = "Terraform"
      Environment = "Academic-Lab"
    }
  }
}

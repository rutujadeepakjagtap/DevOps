# DevOps Practical Assignment 03: Infrastructure as Code (IaC) Using Terraform

**Student Name:** Rutuja Deepak Jagtap  
**PRN:** `123B1B146` | **Batch:** `C1`  
**Department:** Computer Engineering, PCCOE Pune  
**Academic Year:** 2026–2027  
**Official Curriculum Code:** `BCE27PE01` / `CE-4202`  

---

## 1. Aim
To study the concepts and workflow of Infrastructure as Code (IaC), install and configure Terraform, and develop a declarative Terraform configuration in HashiCorp Configuration Language (HCL) to provision, validate, plan, inspect, and destroy an Amazon EC2 virtual machine instance, custom security group, input variables, output attributes, and state tracking.

---

## 2. Learning Objectives
1. **IaC Principles:** Contrast imperative manual cloud provisioning with declarative Infrastructure as Code.
2. **Terraform Architecture:** Understand Core Engine, State (`terraform.tfstate`), Provider Plugins (`hashicorp/aws`), and Resource Graphs.
3. **Configuration Structure:** Author modular HCL files:
   - `provider.tf`: Provider version constraints and region parameters.
   - `variables.tf`: Parameterized inputs for flexibility and reusability.
   - `main.tf`: Data sources, security groups, and compute resources.
   - `outputs.tf`: Exported attributes (Public IP, DNS, Resource IDs).
4. **Terraform Workflow Execution:** Master the 5-stage lifecycle:
   - `terraform fmt`: Canonical HCL code formatting.
   - `terraform init`: Provider download and backend initialization.
   - `terraform validate`: Syntax and internal configuration consistency checking.
   - `terraform plan`: Dry-run execution planning and diff analysis.
   - `terraform apply`: Idempotent infrastructure reconciliation against AWS APIs.
   - `terraform destroy`: Safe resource teardown to eliminate recurring costs.
5. **State Management & State Drift:** Analyze how `.terraform.lock.hcl` and `terraform.tfstate` protect against configuration drift.

---

## 3. Terraform Architecture & Workflow

```
       +-------------------------------------------------------+
       |             Terraform Configuration Files             |
       |  (main.tf, variables.tf, provider.tf, outputs.tf)     |
       +-------------------------------------------------------+
                                  |
                                  v
+------------------+     +------------------+     +------------------+
|  terraform fmt   | --> |  terraform init  | --> |terraform validate|
| (Format HCL)     |     | (Fetch AWS Prov) |     |  (Syntax Check)  |
+------------------+     +------------------+     +------------------+
                                                           |
                                                           v
       +-------------------------------------------------------+
       |                    terraform plan                     |
       |  (Compares desired HCL state with real AWS state)     |
       +-------------------------------------------------------+
                                  |
                                  v
       +-------------------------------------------------------+
       |                    terraform apply                    |
       |  (Provisions AWS EC2, Security Group & User Data)     |
       +-------------------------------------------------------+
                                  |
                 +----------------+----------------+
                 |                                 |
                 v                                 v
       +--------------------+            +--------------------+
       |  terraform.tfstate |            | terraform destroy  |
       | (State Tracking)   |            | (Zero-Cost Teardown|
       +--------------------+            +--------------------+
```

---

## 4. Configuration Manifests Reference

### 4.1 Provider (`provider.tf`)
Configures the HashiCorp AWS provider with region `ap-south-1` (Mumbai) and automated default tags for student traceability.

### 4.2 Variables (`variables.tf`)
Declares `aws_region`, `instance_type` (`t3.micro`), and `instance_name` (`Terraform-EC2`).

### 4.3 Main Resources (`main.tf`)
- **Data Source:** Dynamically retrieves the latest Amazon Linux 2023 x86_64 AMI ID from AWS SSM Parameter Store.
- **Security Group:** Inbound rules for Port 22 (SSH) and Port 80 (HTTP), egress all.
- **EC2 Instance:** Associates the AMI, instance type, security group, and automated Nginx bootstrap script via `user_data`.

### 4.4 Outputs (`outputs.tf`)
Exports `instance_id`, `instance_public_ip`, `instance_public_dns`, and `security_group_id`.

---

## 5. Local Execution & Validation Guide

### Step 1: Run Automated Verification Script
Execute the bundled PowerShell validation script:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/test_terraform.ps1
```

### Step 2: Step-by-Step Manual Commands
```powershell
cd assignments/assignment-03-terraform-iac/terraform

# Format all HCL manifests
terraform fmt

# Initialize AWS provider plugin
terraform init

# Validate syntax and arguments
terraform validate
# Output: Success! The configuration is valid.
```

### Step 3: Deploying to AWS (When Authenticated)
```powershell
# Review proposed infrastructure changes
terraform plan

# Apply infrastructure changes
terraform apply -auto-approve

# Inspect created resources
terraform show
terraform output

# Clean up all AWS resources to avoid billing
terraform destroy -auto-approve
```

---

## 6. Viva Voce Questions & Answers

**Q1: What is the purpose of the `terraform.tfstate` file?**  
*Answer:* The `terraform.tfstate` file maps declarative resource declarations in code to physical resource IDs in the cloud provider. It tracks resource attributes, metadata, and dependencies, enabling Terraform to calculate incremental diffs during `terraform plan` rather than recreating resources.

**Q2: How does Terraform achieve idempotency?**  
*Answer:* Terraform continuously evaluates the current state of infrastructure against the desired state declared in HCL manifests. If the real-world infrastructure already matches the desired configuration, running `terraform apply` performs zero modifications.

**Q3: Why is `.terraform.lock.hcl` committed to version control, while `.env` and `terraform.tfstate` are excluded?**  
*Answer:* `.terraform.lock.hcl` guarantees reproducible builds by locking the exact cryptographic hashes and versions of provider plugins across team members. `.env` and `terraform.tfstate` must be excluded via `.gitignore` because they can contain unencrypted database passwords, private IP addresses, and sensitive cloud credentials.

**Q4: What is the benefit of fetching AMIs via `data "aws_ssm_parameter"` instead of hardcoding AMI IDs?**  
*Answer:* Hardcoded AMI IDs vary across AWS regions and are periodically deprecated by AWS. Querying AWS SSM Parameter Store dynamically guarantees that the deployment always deploys the latest patched, secure Amazon Linux AMI in whatever region is chosen.

---

## 7. Conclusion
Infrastructure as Code was successfully demonstrated using HashiCorp Terraform. Modular declarative HCL manifests were authored for AWS EC2 and Security Group provisioning, and the entire workflow (`fmt`, `init`, `validate`, `plan`) was verified on Windows.

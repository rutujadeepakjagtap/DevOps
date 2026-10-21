# Pimpri Chinchwad Education Trust's
# Pimpri Chinchwad College of Engineering (PCCOE), Pune
### (An Autonomous Institute Affiliated to Savitribai Phule Pune University)
### Department of Computer Engineering | Academic Year 2026–2027

---

# DevOps Laboratory Assignment Report — Assignment 02
## Course: DevOps Engineering (Course Code: `BCE27PE01` / `CE-4202`)
### Semester: VII | Final Year B.Tech Computer Engineering

- **Student Name:** Rutuja Deepak Jagtap
- **PRN:** `123B1B146`
- **Batch:** `C1`
- **Department:** Department of Computer Engineering
- **Academic Year:** 2026–2027
- **AWS Account:** `Rutuja Jagtap (545432115022)`
- **AWS Deployment Region:** Asia Pacific (Mumbai) `ap-south-1`
- **Public GitHub Repository:** [https://github.com/rutujadeepakjagtap/DevOps](https://github.com/rutujadeepakjagtap/DevOps)

---

## 1. Title
**Exploration of AWS Cloud Computing Services and Complete Virtual Machine Lifecycle Management using Amazon Elastic Compute Cloud (EC2)**

---

## 2. Aim
To study the architectural fundamentals of cloud computing and Amazon Web Services (AWS core services: EC2, S3, RDS, Lambda, ELB, ECS), and systematically create, configure security groups and key pairs, launch, connect to, monitor telemetry via Amazon CloudWatch, and safely terminate an Amazon EC2 Virtual Machine instance (`t3.micro`) under the AWS Free Tier.

---

## 3. Objectives
1. To understand cloud computing models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
2. To explore Amazon Web Services core ecosystem: Amazon EC2, Amazon S3, AWS Lambda, Amazon RDS, Elastic Load Balancing (ELB), and Amazon ECS.
3. To study virtualization principles, hypervisors (Type 1 Bare-Metal vs Type 2 Hosted, and the AWS Nitro Hypervisor system).
4. To configure network firewall policies using AWS Security Groups (SSH Port 22 and HTTP Port 80).
5. To launch and verify a live running Linux virtual server (`My-DevOps-EC2`) in the Mumbai region (`ap-south-1b`).
6. To monitor compute telemetry (CPU utilization, network traffic, system and instance health checks) using Amazon CloudWatch.
7. To execute zero-cost termination and resource cleanup adhering to the AWS Free Tier.

---

## 4. Software & Hardware Specifications
- **Cloud Service Provider:** Amazon Web Services (AWS)
- **Deployment Region:** Asia Pacific (Mumbai) `ap-south-1` (Availability Zone `ap-south-1b`)
- **Virtual Machine Instance Type:** `t3.micro` (2 vCPUs, 1.0 GiB RAM - AWS Free Tier Eligible)
- **Base Operating System:** Amazon Linux 2023 (AL2023) 64-bit (x86_64) Kernel
- **Storage:** 8 GiB General Purpose SSD (gp3)
- **Management Interfaces:** AWS Management Console, AWS CLI `v2.38.3`, Windows PowerShell
- **Client System:** Windows 11 64-bit, AMD64 Architecture

---

## 5. Theoretical Background

### 5.1 Cloud Computing & Service Delivery Models
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. It replaces traditional on-premises capital expenditure (CapEx) with flexible operational expenditure (OpEx).

| Service Model | Management Scope (User vs Provider) | AWS Service Examples |
| :--- | :--- | :--- |
| **IaaS (Infrastructure as a Service)** | User manages OS, runtime, middleware, data, and applications. AWS manages physical servers, storage, virtualization, and physical networking. | **Amazon EC2**, Amazon VPC, Amazon EBS |
| **PaaS (Platform as a Service)** | User manages only code and data. AWS manages OS patching, runtime environments, scaling, and hardware. | AWS Elastic Beanstalk, AWS App Runner |
| **SaaS (Software as a Service)** | Provider manages entire software stack; users consume via browser. | AWS WorkMail, QuickSight |

### 5.2 Overview of Core AWS Services
1. **Amazon EC2 (Elastic Compute Cloud):** Resizable virtual compute capacity in the cloud.
2. **Amazon S3 (Simple Storage Service):** Highly scalable object storage with 99.999999999% (11 9's) durability.
3. **AWS Lambda:** Serverless event-driven compute engine executing code in response to events without provisioning servers.
4. **Amazon RDS (Relational Database Service):** Managed database service supporting PostgreSQL, MySQL, MariaDB, and Oracle.
5. **Elastic Load Balancing (ELB):** Automatically distributes incoming application traffic across multiple EC2 targets.
6. **Amazon ECS (Elastic Container Service):** Scalable container management service running Docker containers.

### 5.3 Amazon EC2 Virtualization Architecture (AWS Nitro System)
Modern Amazon EC2 instances (such as the `t3` family) run on the **AWS Nitro System**, an architecture that offloads virtualization functions (storage, networking, security, and management) from the CPU onto dedicated Nitro ASIC hardware cards. This leaves practically 100% of host CPU and memory available for user workloads.

```
+-------------------------------------------------------------------------------+
| AWS Cloud (Region: ap-south-1 / Mumbai)                                            |
|                                                                               |
|  +-------------------------------------------------------------------------+  |
|  | Virtual Private Cloud (VPC: 172.31.0.0/16)                              |  |
|  |                                                                         |  |
|  |   +-------------------------------------------------------------------+ |  |
|  |   | Public Subnet (ap-south-1b)                                       | |  |
|  |   |                                                                   | |  |
|  |   |   +------------------- Security Group ------------------------+   | |  |
|  |   |   | Inbound Rules:                                            |   | |  |
|  |   |   |   - Port 22 (SSH)  <- 0.0.0.0/0 (Admin Workstation)        |   | |  |
|  |   |   |   - Port 80 (HTTP) <- 0.0.0.0/0 (Web Clients)             |   | |  |
|  |   |   +-----------------------------------------------------------+   | |  |
|  |   |                               |                                   | |  |
|  |   |                               v                                   | |  |
|  |   |              +----------------------------------+                 | |  |
|  |   |              | Instance: My-DevOps-EC2          |                 | |  |
|  |   |              | ID: i-0e2921adb9d8abd4b          |                 | |  |
|  |   |              | Type: t3.micro (Free Tier)       |                 | |  |
|  |   |              | IP: 3.109.154.173                |                 | |  |
|  |   |              | State: Running                   |                 | |  |
|  |   |              +----------------------------------+                 | |  |
|  |   |                               |                                   | |  |
|  |   |                               v                                   | |  |
|  |   |              +----------------------------------+                 | |  |
|  |   |              | Elastic Block Store (EBS)        |                 | |  |
|  |   |              | Root Volume: 8 GiB gp3           |                 | |  |
|  |   |              +----------------------------------+                 | |  |
|  |   +-------------------------------------------------------------------+ |  |
|  +-------------------------------------------------------------------------+  |
|                                                                               |
|  Telemetry: Amazon CloudWatch (CPUUtilization, NetworkIn/Out, Status Checks)  |
+-------------------------------------------------------------------------------+
```

---

## 6. Step-by-Step Practical Implementation Procedure

### Step 1: AWS Management Console Sign-In & Region Selection
1. Navigate to the AWS Console at `https://ap-south-1.console.aws.amazon.com/`.
2. Confirm identity as student user: `Rutuja Jagtap` (Account ID: `545432115022`).
3. Select region: **Asia Pacific (Mumbai) `ap-south-1`**.

### Step 2: Configure and Launch EC2 Virtual Machine
1. Open the Amazon EC2 Console &rarr; click **Launch Instance**.
2. **Name:** `My-DevOps-EC2`.
3. **Application and OS Images (AMI):** Amazon Linux 2023 AMI (Free tier eligible).
4. **Instance Type:** `t3.micro` (2 vCPUs, 1 GiB RAM - Free Tier eligible).
5. **Key Pair:** Configure RSA key pair or proceed without key pair for web demonstration.
6. **Network Settings & Firewall (Security Group):**
   - Create security group allowing **SSH (Port 22)**.
   - Enable checkbox **Allow HTTP traffic from the internet (Port 80)**.
7. **Storage:** 8 GiB gp3 root volume.
8. Click **Launch Instance**.

---

## 7. Practical Verification Evidence & Real AWS Screenshots

### Evidence 1: Successful Launch Initiation Log
The instance request was successfully initialized, creating the security group, authorization rules, and launching instance `i-0e2921adb9d8abd4b`:

![AWS Launch Success](./screenshots/aws_01_launch_success.png)

*Figure 1: AWS Management Console confirmation showing "Successfully initiated launch of instance (i-0e2921adb9d8abd4b)" with all launch log steps succeeded.*

---

### Evidence 2: Live Running EC2 Virtual Machines in Mumbai Region
The AWS EC2 Instances Dashboard showing `My-DevOps-EC2` active and running in `ap-south-1b`:

![AWS Instances Running](./screenshots/aws_02_instances_running.png)

*Figure 2: Real-time AWS EC2 instances console in region ap-south-1 (Mumbai) showing instance `My-DevOps-EC2` (`i-0e2921adb9d8abd4b`) in `Running` state alongside assigned DNS `ec2-3-109-154-173.ap-south-1.compute.amazonaws.com`.*

---

## 8. Real Instance Observation Table

| Parameter | Observed Live Value | Academic Specification |
| :--- | :--- | :--- |
| **AWS Account Owner** | Rutuja Jagtap (`545432115022`) | Verified Student Identity |
| **Instance Name Tag** | `My-DevOps-EC2` | Configured Instance Name |
| **Instance ID** | `i-0e2921adb9d8abd4b` | Unique AWS Resource Identifier |
| **Instance State** | **`Running`** | Healthy active workload |
| **Instance Type** | **`t3.micro`** | 2 vCPUs, 1 GiB RAM (AWS Free Tier) |
| **AWS Deployment Region** | Asia Pacific (Mumbai) `ap-south-1` | Local Low-Latency Region |
| **Availability Zone** | `ap-south-1b` | Redundant Datacenter Zone |
| **Public IPv4 DNS** | `ec2-3-109-154-173.ap-south-1.compute.amazonaws.com` | Resolved AWS Public DNS |
| **Public IPv4 Address** | `3.109.154.173` | Accessible Internet Endpoint |
| **Security Group Ports** | Port 22 (SSH), Port 80 (HTTP) | Least-Privilege Inbound Firewall |
| **Storage Architecture** | 8 GiB gp3 (EBS Block Storage) | Free Tier Allocation (<30 GiB) |
| **Billing & Cost** | **$0.00** | 100% Free Tier Eligible |

---

## 9. Telemetry Monitoring & Safe Resource Termination

### 9.1 Amazon CloudWatch Telemetry Metrics
1. **CPUUtilization (%):** Tracks compute load across evaluation periods (baseline < 5%).
2. **NetworkIn & NetworkOut (Bytes):** Quantifies inbound requests and outbound HTTP responses.
3. **StatusCheckFailed_System:** Verifies AWS physical host infrastructure.
4. **StatusCheckFailed_Instance:** Verifies guest OS reachability.

### 9.2 Safe Termination Procedure (Zero-Cost Guarantee)
To ensure zero ongoing charges:
1. In the EC2 Instances table, select `My-DevOps-EC2` (`i-0e2921adb9d8abd4b`).
2. Click **Instance State** dropdown &rarr; select **Terminate instance**.
3. AWS transitions the instance from `Running` &rarr; `Shutting-down` &rarr; `Terminated`.
4. The attached 8 GiB root EBS volume is automatically detached and deleted, eliminating recurring storage and compute expenses.

---

## 10. Viva Voce Examination Questions & Answers

### Q1: What is the difference between AWS Security Groups and Network ACLs?
**Answer:** Security Groups operate at the virtual network interface (ENI) level, are **stateful** (return traffic is automatically allowed), and evaluate allow rules only. Network ACLs operate at the subnet boundary, are **stateless** (return traffic must be explicitly allowed), and evaluate both allow and deny rules in numbered order.

### Q2: Why did we select the `t3.micro` instance type for this practical?
**Answer:** The `t3.micro` instance provides 2 vCPUs and 1 GiB of burstable memory and is included under the **AWS Free Tier** (750 hours per month). It delivers high baseline performance using the AWS Nitro System without incurring charges.

### Q3: What is an Amazon Machine Image (AMI)?
**Answer:** An AMI is a pre-packaged template containing the operating system, architecture, volume mapping, and pre-installed software packages necessary to launch an EC2 instance.

### Q4: What is the difference between Stopping and Terminating an EC2 instance?
**Answer:** **Stopping** shuts down the virtual server OS and halts compute charges, but the allocated EBS storage volume persists and incurs minor storage fees. **Terminating** permanently destroys the virtual instance and deletes the attached root EBS volume, guaranteeing zero ongoing cloud costs.

### Q5: What is the AWS Nitro System?
**Answer:** The AWS Nitro System is the underlying virtualization architecture for modern EC2 instances. It offloads hypervisor storage, networking, and security management tasks onto dedicated hardware cards, leaving almost 100% of host CPU and memory available to the virtual machine.

---

## 11. Result
An Amazon EC2 virtual machine instance named `My-DevOps-EC2` (`i-0e2921adb9d8abd4b`) was successfully created, configured with security group firewall rules, launched in the Mumbai region (`ap-south-1b`), verified in the `Running` state with public DNS `ec2-3-109-154-173.ap-south-1.compute.amazonaws.com`, and monitored under the AWS Free Tier.

---

## 12. Conclusion
Through this practical assignment, comprehensive practical knowledge of cloud computing service models (IaaS/PaaS/SaaS), AWS core infrastructure services (EC2, S3, RDS, Lambda, ELB), virtualization with the AWS Nitro hypervisor, and virtual server lifecycle operations was acquired. The entire procedure was performed adhering to cloud cost-safety best practices.

# DevOps Practical Assignment 02: AWS Cloud Services Exploration & EC2 Virtual Machine Lifecycle

**Student Name:** Rutuja Deepak Jagtap  
**PRN:** `123B1B146` | **Batch:** `C1`  
**Department:** Computer Engineering, PCCOE Pune  
**Academic Year:** 2026–2027  
**Official Curriculum Code:** `BCE27PE01` / `CE-4202`  

### Quick Download Links for Faculty Submission:
- 📄 **Download PDF Report:** [123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf](./123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf)
- 📝 **Download Word Document (.docx):** [123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx](./123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx)
- 📖 **Read Full Markdown Report:** [DevOps_Assignment_02_AWS_EC2_Report_Rutuja_Jagtap.md](./DevOps_Assignment_02_AWS_EC2_Report_Rutuja_Jagtap.md)

---

## 1. Aim
To explore the core computing and cloud infrastructure services offered by Amazon Web Services (AWS) — including Amazon EC2, Amazon S3, AWS Lambda, Amazon RDS, Elastic Load Balancing (ELB), and Amazon ECS — and systematically create, configure security groups and key pairs, connect to via SSH, monitor telemetry using Amazon CloudWatch, and safely terminate an Amazon EC2 Virtual Machine instance.

---

## 2. Learning Objectives
1. **Cloud Service Models:** Understand Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
2. **AWS Core Architecture:** Survey essential AWS building blocks:
   - Compute: EC2, Lambda, ECS, Fargate.
   - Storage: S3 object storage, EBS block storage, EFS network storage.
   - Database: RDS relational database, DynamoDB NoSQL database.
   - Networking: Virtual Private Cloud (VPC), Subnets, Route Tables, Internet Gateway, Security Groups.
3. **Virtualization & Hypervisors:** Distinguish Type 1 (Bare Metal / Nitro Hypervisor) and Type 2 (Hosted) virtualization.
4. **EC2 Instance Provisioning:** Configure Amazon Machine Image (AMI), instance sizing (`t2.micro` / `t3.micro`), VPC subnets, and EBS root volumes.
5. **Network Security:** Author least-privilege Security Group inbound rules for SSH (port 22) and HTTP (port 80).
6. **Telemetry & Monitoring:** Inspect Amazon CloudWatch alarms and metrics (`CPUUtilization`, `NetworkIn`, `StatusCheckFailed`).
7. **Resource Lifecycle & Cost Management:** Prevent unwanted billing through timely instance stopping and termination.

---

## 3. Theoretical Architecture & AWS Nitro Hypervisor

```
+-----------------------------------------------------------------------------------+
| AWS Cloud (Region: ap-south-1 / Mumbai)                                            |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | Virtual Private Cloud (VPC: 172.31.0.0/16)                                  |  |
|  |                                                                             |  |
|  |   +-----------------------------------------------------------------------+ |  |
|  |   | Public Subnet (172.31.32.0/20)                                         | |  |
|  |   |                                                                       | |  |
|  |   |   +----------------------- Security Group ------------------------+   | |  |
|  |   |   | Inbound Rules:                                                |   | |  |
|  |   |   |   - Port 22 (SSH)   <- Admin Workstation IP                       |   | |  |
|  |   |   |   - Port 80 (HTTP)  <- 0.0.0.0/0 (Internet)                       |   | |  |
|  |   |   +---------------------------------------------------------------+   | |  |
|  |   |                               |                                       | |  |
|  |   |                               v                                       | |  |
|  |   |              +----------------------------------+                     | |  |
|  |   |              | Amazon EC2 Instance (t2.micro)   |                     | |  |
|  |   |              | OS: Amazon Linux 2023 / Ubuntu   |                     | |  |
|  |   |              | Public IPv4: 13.233.104.55       |                     | |  |
|  |   |              +----------------------------------+                     | |  |
|  |   |                               |                                       | |  |
|  |   |                               v                                       | |  |
|  |   |              +----------------------------------+                     | |  |
|  |   |              | Elastic Block Store (EBS)        |                     | |  |
|  |   |              | Root Volume: 8 GiB gp3 (IOPS 3k) |                     | |  |
|  |   |              +----------------------------------+                     | |  |
|  |   +-----------------------------------------------------------------------+ |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  Amazon CloudWatch (Metrics: CPU, Disk I/O, Network, System / Instance Status)    |
+-----------------------------------------------------------------------------------+
```

---

## 4. Step-by-Step Practical Procedure

### Step 1: AWS Management Console Login
1. Navigate to [https://aws.amazon.com/console/](https://aws.amazon.com/console/) and sign in.
2. Select Region: **Asia Pacific (Mumbai) `ap-south-1`**.

### Step 2: Key Pair Creation
1. In the EC2 console under **Network & Security**, click **Key Pairs** &rarr; **Create Key Pair**.
2. Name: `devops-lab-key`, Key pair type: `RSA`, Private key format: `.pem`.
3. Store the downloaded `devops-lab-key.pem` safely. Set permissions in Linux/WSL: `chmod 400 devops-lab-key.pem`.

### Step 3: Launch Instance
1. Click **Launch Instances**.
2. Name: `PCCOE-DevOps-EC2-Server`.
3. AMI: **Amazon Linux 2023 AMI** (Free Tier eligible).
4. Instance type: **t2.micro** (1 vCPU, 1 GiB RAM).
5. Key pair: Select `devops-lab-key`.
6. Network Settings & Security Group:
   - Allow SSH traffic from My IP (or `0.0.0.0/0` for academic lab).
   - Allow HTTP traffic from the internet (`0.0.0.0/0`).
7. Storage: Default 8 GiB gp3.
8. Click **Launch Instance**.

### Step 4: Connect to the Instance
Connect using SSH from terminal / PowerShell:
```bash
ssh -i devops-lab-key.pem ec2-user@<EC2-PUBLIC-IP>
```
Or use the browser-based **EC2 Instance Connect**.

### Step 5: Install & Start Web Server (User Data / Terminal)
```bash
sudo dnf update -y
sudo dnf install -y nginx
sudo systemctl enable --now nginx
echo "<h1>Welcome to Rutuja Jagtap's AWS EC2 DevOps Server</h1>" | sudo tee /usr/share/nginx/html/index.html
```

### Step 6: Monitor with Amazon CloudWatch
1. In EC2 Dashboard, select instance &rarr; **Monitoring** tab.
2. Observe real-time graphs for:
   - `CPU Utilization (%)`
   - `Status Check Failed (Any)`
   - `Network In (Bytes)` & `Network Out (Bytes)`

### Step 7: Clean Termination
1. Select instance &rarr; **Instance State** &rarr; **Terminate Instance**.
2. Confirm termination to release the allocated EBS volume and elastic IP, ensuring zero ongoing cloud cost.

---

## 5. Local Python Automation & Demonstration

Execute the bundled offline/mock verification script locally on Windows without incurring cloud charges:
```powershell
python scripts/aws_ec2_manager.py --simulate
```
To verify active AWS credentials (if configured):
```powershell
python scripts/aws_ec2_manager.py --check-auth
```

---

## 6. Viva Voce Questions & Answers

**Q1: What is the difference between AWS Security Groups and Network ACLs?**  
*Answer:* Security Groups operate at the virtual network interface (ENI) level, are **stateful** (return traffic is automatically allowed), and evaluate allow rules only. Network ACLs operate at the subnet boundary, are **stateless** (return traffic must be explicitly allowed), and evaluate both allow and deny rules in numbered order.

**Q2: What is an Amazon Machine Image (AMI)?**  
*Answer:* An AMI is a pre-configured template containing the operating system, architecture, volume mapping, and pre-installed software packages necessary to launch an EC2 instance.

**Q3: What are the two types of EC2 Status Checks in CloudWatch?**  
*Answer:* 
1. **System Status Checks:** Monitors the underlying AWS physical host hardware and power systems.
2. **Instance Status Checks:** Monitors the guest operating system reachability, filesystem corruption, or network stack failures.

**Q4: What is the difference between Stopping and Terminating an EC2 instance?**  
*Answer:* **Stopping** an EBS-backed instance shuts down the OS and halts compute charges, but EBS root storage remains allocated and incur minor storage fees. **Terminating** permanently destroys the virtual instance and automatically deletes the attached root EBS volume, ending all associated charges.

---

## 7. Conclusion
The comprehensive AWS cloud computing model was analyzed, and the end-to-end lifecycle of an Amazon EC2 instance—from provisioning, security group firewall authoring, SSH connectivity, CloudWatch monitoring, to safe termination—was verified.

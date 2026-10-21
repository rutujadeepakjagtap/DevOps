import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class AssignmentPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'B', 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 5, 'PCCOE Pune | Dept of Computer Engineering | DevOps Lab (BCE27PE01) | Assignment 02', 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.set_draw_color(220, 220, 220)
            self.line(12, 12, 198, 12)
            self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(130, 130, 130)
        self.cell(0, 8, f'Page {self.page_no()} of {{nb}}  |  Rutuja Deepak Jagtap  |  PRN: 123B1B146  |  Batch C1', 0, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')

    def chapter_title(self, num_and_title):
        self.set_x(12)
        self.set_font('Helvetica', 'B', 10.5)
        self.set_text_color(20, 45, 85)
        self.set_fill_color(238, 244, 255)
        self.set_draw_color(180, 205, 245)
        self.cell(186, 7, f'  {num_and_title}', 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln(2)

    def body_text(self, text):
        self.set_x(12)
        self.set_font('Helvetica', '', 9)
        self.set_text_color(40, 40, 40)
        self.multi_cell(186, 4.5, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def add_image_figure(self, img_path, caption, width=160):
        if os.path.exists(img_path):
            if self.get_y() > 195:
                self.add_page()
            x_pos = (210 - width) / 2
            self.image(img_path, x=x_pos, w=width)
            self.ln(2)
            self.set_x(12)
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(70, 70, 70)
            self.multi_cell(186, 4, caption, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.ln(3)

def build_pdf():
    pdf = AssignmentPDF(format='A4')
    pdf.alias_nb_pages()
    pdf.set_margins(12, 12, 12)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # ---------------- PAGE 1 ----------------
    pdf.add_page()
    
    # College Header
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(18, 38, 76)
    pdf.cell(0, 7, "PIMPRI CHINCHWAD COLLEGE OF ENGINEERING", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, "An Autonomous Institute Affiliated to Savitribai Phule Pune University", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.cell(0, 5, "Department of Computer Engineering | Academic Year 2026-2027", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(1)
    
    # Assignment Banner
    pdf.set_fill_color(13, 110, 253)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 11.5)
    pdf.cell(0, 8, "DEVOPS ENGINEERING LABORATORY - ASSIGNMENT 02", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C', fill=True)
    pdf.ln(2)

    # Student Metadata Card
    pdf.set_fill_color(248, 249, 250)
    pdf.set_draw_color(210, 215, 222)
    y_card = pdf.get_y()
    pdf.rect(12, y_card, 186, 24, 'DF')
    pdf.set_text_color(30, 30, 30)
    pdf.set_font('Helvetica', '', 8.5)
    
    pdf.set_xy(16, y_card + 2)
    pdf.cell(90, 4.5, "Student Name: Rutuja Deepak Jagtap", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 4.5, "AWS Account: Rutuja Jagtap (545432115022)", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(16)
    pdf.cell(90, 4.5, "PRN: 123B1B146 | Batch: C1", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 4.5, "Region: Asia Pacific (Mumbai) ap-south-1b", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(16)
    pdf.cell(90, 4.5, "Course: DevOps Engineering (BCE27PE01)", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 4.5, "Instance Name: My-DevOps-EC2", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.cell(90, 4.5, "Repository: github.com/rutujadeepakjagtap/DevOps", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.cell(90, 4.5, "Cost Profile: 100% Free Tier ($0.00)", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_y(y_card + 27)

    # Title
    pdf.chapter_title("1. Title")
    pdf.body_text("Exploration of AWS Cloud Computing Services and Complete Virtual Machine Lifecycle Management using Amazon Elastic Compute Cloud (EC2).")

    # Aim
    pdf.chapter_title("2. Aim")
    pdf.body_text("To study the architectural fundamentals of cloud computing (IaaS, PaaS, SaaS) and AWS core services (EC2, S3, RDS, Lambda, ELB), and systematically configure, launch, monitor via Amazon CloudWatch, and safely terminate an Amazon EC2 Virtual Machine instance (t3.micro) under the AWS Free Tier.")

    # Objectives
    pdf.chapter_title("3. Objectives")
    pdf.body_text(
        "1. Understand Cloud Service Models (IaaS, PaaS, SaaS) and virtualization hypervisors.\n"
        "2. Configure network firewall boundaries using AWS Security Groups (Port 22 SSH & Port 443 HTTPS).\n"
        "3. Launch and manage an Amazon Linux 2023 EC2 virtual machine (My-DevOps-EC2) in ap-south-1b.\n"
        "4. Verify instance attributes (Public IP, Private IP, VPC ID, Public DNS).\n"
        "5. Analyze real-time performance telemetry with Amazon CloudWatch and execute zero-cost termination."
    )

    # ---------------- PAGE 2: Procedure & Screenshots 1 & 2 ----------------
    pdf.add_page()
    pdf.chapter_title("4. Practical Implementation Procedure")
    pdf.body_text(
        "1. Sign in to AWS Management Console with student account 'Rutuja Jagtap' (ID: 545432115022).\n"
        "2. Select Region 'Asia Pacific (Mumbai) ap-south-1'.\n"
        "3. Navigate to EC2 Console -> Launch Instances.\n"
        "4. Set Instance Name tag to 'My-DevOps-EC2', AMI to Amazon Linux 2023 (AL2023), and Type to 't3.micro'.\n"
        "5. Create Security Group 'launch-wizard-1' opening Port 22 (SSH) and Port 443 (HTTPS).\n"
        "6. Configure 8 GiB gp3 Root EBS Volume and launch the instance.\n"
        "7. Inspect the running state, verify IP endpoints, and track CloudWatch telemetry."
    )

    pdf.chapter_title("5. Practical Verification Evidence - Real AWS Console Screenshots")
    
    img_dir = "assignments/assignment-02-aws-cloud-ec2/screenshots"
    
    # Figure 1: Launch success
    pdf.add_image_figure(
        os.path.join(img_dir, "aws_01_launch_success.png"),
        "Figure 1: AWS Console - Successfully initiated launch of EC2 instance (i-0e2921adb9d8abd4b) with all launch steps succeeded.",
        width=155
    )

    # Figure 2: Instances Running Table
    pdf.add_image_figure(
        os.path.join(img_dir, "aws_02_instances_running.png"),
        "Figure 2: AWS EC2 Dashboard showing instance 'My-DevOps-EC2' in Running state in Mumbai (ap-south-1b) with IP 3.109.154.173.",
        width=155
    )

    # ---------------- PAGE 3: Screenshots 3 & 4 ----------------
    pdf.add_page()
    
    # Figure 3: Details View
    pdf.add_image_figure(
        os.path.join(img_dir, "aws_03_instance_details.png"),
        "Figure 3: Detailed Instance View for 'i-0e2921adb9d8abd4b' verifying Public IP (3.109.154.173), Private IP (172.31.1.101), and VPC DNS.",
        width=155
    )

    # Figure 4: Security Group Rules
    pdf.add_image_figure(
        os.path.join(img_dir, "aws_04_security_group_rules.png"),
        "Figure 4: AWS Security Group 'launch-wizard-1' (sg-0671e3672a564981f) inbound firewall rules: HTTPS (443) and SSH (22).",
        width=155
    )

    # ---------------- PAGE 4: Screenshot 5 & Observation Table ----------------
    pdf.add_page()

    # Figure 5: CloudWatch Monitoring
    pdf.add_image_figure(
        os.path.join(img_dir, "aws_05_cloudwatch_monitoring.png"),
        "Figure 5: Live Amazon CloudWatch Telemetry - Real-time CPU Utilization (0.18%), Network Packets (24 in/21 out), and CPU Credit Balance (1.18).",
        width=155
    )

    pdf.chapter_title("6. Real Instance Observation & Verification Table")
    
    # Table Header
    pdf.set_x(12)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(225, 235, 250)
    pdf.set_draw_color(180, 195, 215)
    pdf.cell(50, 5.5, " Parameter", 1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True)
    pdf.cell(75, 5.5, " Observed Live Console Value", 1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True)
    pdf.cell(61, 5.5, " Academic Specification", 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)

    obs_data = [
        ("AWS Account User", "Rutuja Jagtap (545432115022)", "Verified Student Owner"),
        ("Instance Name", "My-DevOps-EC2", "Configured Name Tag"),
        ("Instance ID", "i-0e2921adb9d8abd4b", "Unique AWS Resource Identifier"),
        ("Instance State", "Running (Healthy)", "Active Virtual Machine"),
        ("Instance Type", "t3.micro (2 vCPU, 1 GiB RAM)", "AWS Free Tier Eligible"),
        ("Region & Zone", "ap-south-1 / ap-south-1b (Mumbai)", "Asia Pacific Region"),
        ("Public IPv4 Address", "3.109.154.173", "Internet Accessible IP"),
        ("Private IPv4 Address", "172.31.1.101", "Internal VPC Network IP"),
        ("Public IPv4 DNS", "ec2-3-109-154-173.ap-south-1...", "AWS Generated DNS Hostname"),
        ("Virtual Private Cloud", "vpc-0e0a04b1273818ad2", "Isolated VPC Boundary"),
        ("Security Group", "launch-wizard-1 (sg-0671e3672a564981f)", "Stateful Firewall"),
        ("Inbound Rules", "Port 22 (SSH) + Port 443 (HTTPS)", "Administrative & Web Access"),
        ("CPU Utilization", "0.18% (Baseline Idle)", "CloudWatch Telemetry"),
        ("CPU Credit Balance", "1.18 (Accumulating)", "Nitro Burstable Capacity"),
        ("EBS Volume", "8 GiB gp3 (Root Volume)", "General Purpose SSD"),
        ("Total Billed Cost", "$0.00 (Zero USD)", "100% Free Tier Compliance")
    ]

    pdf.set_font('Helvetica', '', 7.5)
    for i, (param, val, spec) in enumerate(obs_data):
        fill = (i % 2 == 1)
        pdf.set_fill_color(248, 250, 252) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.set_x(12)
        pdf.cell(50, 4.4, f" {param}", 1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=fill)
        pdf.cell(75, 4.4, f" {val}", 1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=fill)
        pdf.cell(61, 4.4, f" {spec}", 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=fill)

    # ---------------- PAGE 5: Viva Voce & Result & Conclusion ----------------
    pdf.add_page()
    pdf.chapter_title("7. Viva-Voce Examination Questions & Answers")
    
    qas = [
        ("Q1: What is the difference between AWS Security Groups and Network ACLs?",
         "Answer: Security Groups operate at the virtual network interface (ENI) level, are stateful (inbound return traffic automatically allowed), and evaluate permit rules only. Network ACLs operate at the subnet boundary, are stateless (inbound and outbound must be explicitly allowed), and evaluate ordered allow/deny rules."),
        ("Q2: Why is the t3.micro instance type recommended for this DevOps laboratory?",
         "Answer: t3.micro offers 2 vCPUs and 1 GiB memory on the AWS Nitro hypervisor architecture, qualifying for 750 free hours per month under the AWS Free Tier, providing high burstable performance at zero financial cost."),
        ("Q3: What happens when an EC2 instance is Stopped vs Terminated?",
         "Answer: Stopping halts the compute instance and its per-second compute bill, but attached EBS storage volumes persist and accrue nominal storage charges. Terminating permanently deletes the virtual server and its root EBS volume, ensuring $0.00 ongoing charges."),
        ("Q4: What is the AWS Nitro System?",
         "Answer: AWS Nitro is a lightweight hypervisor architecture that offloads virtualization management (storage, network, security) to dedicated PCIe hardware cards, maximizing virtual machine CPU and memory performance."),
        ("Q5: How does Amazon CloudWatch assist in infrastructure reliability?",
         "Answer: CloudWatch automatically collects hypervisor metrics (CPU utilization, disk I/O, network traffic) every 5 minutes (or 1 minute in detailed monitoring) without requiring guest agent installation, enabling proactive alarming and autoscaling.")
    ]

    for q, a in qas:
        pdf.set_x(12)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(20, 50, 100)
        pdf.multi_cell(186, 4.2, q, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_x(12)
        pdf.set_font('Helvetica', '', 8)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(186, 3.8, a, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1.5)

    pdf.ln(1)
    pdf.chapter_title("8. Result & Conclusion")
    pdf.set_x(12)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(20, 80, 40)
    pdf.cell(186, 4.5, "Result:", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.body_text("Amazon EC2 instance 'My-DevOps-EC2' (i-0e2921adb9d8abd4b) was successfully provisioned, secured with Security Group 'launch-wizard-1', launched in Mumbai (ap-south-1b), verified with Public IP 3.109.154.173 and Private IP 172.31.1.101, and monitored via CloudWatch with $0.00 spend.")

    pdf.set_x(12)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(20, 80, 40)
    pdf.cell(186, 4.5, "Conclusion:", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.body_text("Through this practical, core cloud computing architectures (IaaS/PaaS/SaaS), virtualization fundamentals, virtual network firewalls, and cloud instance lifecycle operations were thoroughly understood and demonstrated according to industrial DevOps best practices.")

    # Save PDF
    out_pdf_asg2 = "assignments/assignment-02-aws-cloud-ec2/123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf"
    out_pdf_assets = "assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf"
    
    pdf.output(out_pdf_asg2)
    pdf.output(out_pdf_assets)
    print(f"SUCCESS: Generated {out_pdf_asg2}")
    print(f"SUCCESS: Generated {out_pdf_assets}")

if __name__ == '__main__':
    build_pdf()

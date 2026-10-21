import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_heading_with_bottom_border(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    for run in h.runs:
        run.font.name = 'Calibri'
        run.font.color.rgb = RGBColor(16, 44, 87)
    return h

def build_docx():
    doc = docx.Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("PCCOE Pune | Dept of Computer Engineering | DevOps Lab (BCE27PE01)")
        hrun.font.name = 'Calibri'
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(128, 128, 128)
        
        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Rutuja Deepak Jagtap | PRN: 123B1B146 | Batch: C1 | DevOps Assignment 02 Report")
        frun.font.name = 'Calibri'
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(128, 128, 128)

    # College Header
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r1 = p_inst.add_run("PIMPRI CHINCHWAD EDUCATION TRUST'S\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(100, 100, 100)
    
    r2 = p_inst.add_run("PIMPRI CHINCHWAD COLLEGE OF ENGINEERING, PUNE\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(16)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(16, 44, 87)
    
    r3 = p_inst.add_run("An Autonomous Institute Affiliated to Savitribai Phule Pune University\nDepartment of Computer Engineering | Academic Year 2026–2027")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(10)
    r3.font.color.rgb = RGBColor(70, 70, 70)

    # Title Banner
    p_ban = doc.add_paragraph()
    p_ban.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ban.paragraph_format.space_before = Pt(8)
    p_ban.paragraph_format.space_after = Pt(10)
    r_ban = p_ban.add_run("LABORATORY PRACTICAL REPORT — ASSIGNMENT 02\n")
    r_ban.font.name = 'Calibri'
    r_ban.font.size = Pt(13)
    r_ban.font.bold = True
    r_ban.font.color.rgb = RGBColor(13, 110, 253)
    
    r_ban2 = p_ban.add_run("Course: DevOps Engineering (BCE27PE01 / CE-4202)")
    r_ban2.font.name = 'Calibri'
    r_ban2.font.size = Pt(11)
    r_ban2.font.bold = True
    r_ban2.font.color.rgb = RGBColor(40, 40, 40)

    # Student Metadata Table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    metadata = [
        ("Student Name: Rutuja Deepak Jagtap", "AWS Account: Rutuja Jagtap (545432115022)"),
        ("PRN: 123B1B146 | Batch: C1", "Region & Zone: Asia Pacific (Mumbai) ap-south-1b"),
        ("Class: Final Year B.Tech Computer Engineering", "Instance: My-DevOps-EC2 (i-0e2921adb9d8abd4b)"),
        ("Public Repo: github.com/rutujadeepakjagtap/DevOps", "Billing & Cost Status: 100% Free Tier ($0.00)")
    ]
    
    for row_idx, (left_text, right_text) in enumerate(metadata):
        row = meta_table.rows[row_idx]
        cell_l, cell_r = row.cells[0], row.cells[1]
        cell_l.width = Inches(3.4)
        cell_r.width = Inches(3.4)
        set_cell_background(cell_l, "F0F4F8")
        set_cell_background(cell_r, "F0F4F8")
        set_cell_margins(cell_l, top=60, bottom=60, left=120, right=120)
        set_cell_margins(cell_r, top=60, bottom=60, left=120, right=120)
        
        pl = cell_l.paragraphs[0]
        pl.paragraph_format.space_after = Pt(0)
        run_l = pl.add_run(left_text)
        run_l.font.name = 'Calibri'
        run_l.font.size = Pt(9.5)
        run_l.font.bold = True
        
        pr = cell_r.paragraphs[0]
        pr.paragraph_format.space_after = Pt(0)
        run_r = pr.add_run(right_text)
        run_r.font.name = 'Calibri'
        run_r.font.size = Pt(9.5)
        run_r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # 1. Title
    add_heading_with_bottom_border(doc, "1. Title", level=2)
    p = doc.add_paragraph()
    r = p.add_run("Exploration of AWS Cloud Computing Services and Complete Virtual Machine Lifecycle Management using Amazon Elastic Compute Cloud (EC2).")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.5)

    # 2. Aim
    add_heading_with_bottom_border(doc, "2. Aim", level=2)
    p = doc.add_paragraph()
    r = p.add_run("To study the architectural fundamentals of cloud computing (IaaS, PaaS, SaaS) and AWS core infrastructure services (EC2, S3, RDS, Lambda, ELB), and systematically configure, launch, monitor via Amazon CloudWatch, and safely terminate an Amazon EC2 Virtual Machine instance (t3.micro) under the AWS Free Tier.")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.5)

    # 3. Objectives
    add_heading_with_bottom_border(doc, "3. Objectives", level=2)
    objectives = [
        "To understand cloud computing models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).",
        "To explore Amazon Web Services core ecosystem: Amazon EC2, Amazon S3, AWS Lambda, Amazon RDS, Elastic Load Balancing (ELB), and Amazon ECS.",
        "To study virtualization principles, hypervisors (Type 1 Bare-Metal vs Type 2 Hosted, and the AWS Nitro Hypervisor system).",
        "To configure network firewall boundaries using AWS Security Groups (Port 22 SSH & Port 443 HTTPS).",
        "To launch and verify a live running Linux virtual server (My-DevOps-EC2) in the Mumbai region (ap-south-1b).",
        "To monitor compute telemetry (CPU utilization, network traffic, system and instance health checks) using Amazon CloudWatch.",
        "To execute zero-cost termination and resource cleanup adhering strictly to the AWS Free Tier ($0.00 guarantee)."
    ]
    for obj in objectives:
        doc.add_paragraph(obj, style='List Bullet')

    # 4. Software & Hardware Specifications
    add_heading_with_bottom_border(doc, "4. Software & Hardware Specifications", level=2)
    specs = [
        ("Cloud Service Provider", "Amazon Web Services (AWS)"),
        ("Deployment Region", "Asia Pacific (Mumbai) ap-south-1 (Availability Zone: ap-south-1b)"),
        ("Virtual Machine Instance Type", "t3.micro (2 vCPUs, 1.0 GiB RAM - AWS Free Tier Eligible)"),
        ("Operating System Image (AMI)", "Amazon Linux 2023 (AL2023) 64-bit (x86_64) Kernel"),
        ("Storage Volume", "8 GiB General Purpose SSD (gp3 Root Volume)"),
        ("Virtual Private Cloud (VPC)", "vpc-0e0a04b1273818ad2 (Default Subnet CIDR 172.31.0.0/16)"),
        ("Security Group", "launch-wizard-1 (sg-0671e3672a564981f)"),
        ("Management Interfaces", "AWS Management Console, AWS CLI v2.38.3, Windows PowerShell 7")
    ]
    spec_table = doc.add_table(rows=len(specs)+1, cols=2)
    spec_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    spec_table.rows[0].cells[0].paragraphs[0].add_run("Specification Component").font.bold = True
    spec_table.rows[0].cells[1].paragraphs[0].add_run("Configured Academic Value").font.bold = True
    set_cell_background(spec_table.rows[0].cells[0], "0D6EFD")
    set_cell_background(spec_table.rows[0].cells[1], "0D6EFD")
    spec_table.rows[0].cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    spec_table.rows[0].cells[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    for i, (k, v) in enumerate(specs):
        row = spec_table.rows[i+1]
        row.cells[0].width = Inches(2.5)
        row.cells[1].width = Inches(4.3)
        row.cells[0].paragraphs[0].add_run(k).font.bold = True
        row.cells[1].paragraphs[0].add_run(v)
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        set_cell_background(row.cells[0], bg)
        set_cell_background(row.cells[1], bg)

    # 5. Implementation Procedure
    doc.add_page_break()
    add_heading_with_bottom_border(doc, "5. Step-by-Step Practical Implementation Procedure", level=2)
    steps = [
        ("Step 1: Sign-In and Identity Verification", "Sign in to the AWS Management Console at https://ap-south-1.console.aws.amazon.com/ with verified student credentials under account 'Rutuja Jagtap' (Account ID: 545432115022). Set the geographical deployment region to Asia Pacific (Mumbai) [ap-south-1]."),
        ("Step 2: Virtual Machine Provisioning", "Navigate to EC2 -> Instances -> Launch Instances. Assign the Name tag 'My-DevOps-EC2'. Choose the Amazon Linux 2023 AMI (HVM kernel 6.1) and select the 't3.micro' Free-Tier instance type offering 2 vCPUs and 1 GiB memory on the AWS Nitro hypervisor architecture."),
        ("Step 3: Security Group & Firewall Configuration", "Configure inbound firewall rules in Security Group 'launch-wizard-1' (sg-0671e3672a564981f): Authorize SSH (Port 22, TCP) for secure remote shell access and HTTPS (Port 443, TCP) for encrypted web traffic from all internet endpoints (0.0.0.0/0)."),
        ("Step 4: Storage Allocation & Launch Execution", "Allocate an 8 GiB gp3 General Purpose SSD root volume with 3,000 baseline IOPS. Click 'Launch Instance' and verify initiation confirmation."),
        ("Step 5: Telemetry Monitoring & Health Verification", "Select the running instance in the EC2 Management Console. Verify the public IPv4 address (3.109.154.173) and private IPv4 address (172.31.1.101). Open the CloudWatch 'Monitoring' tab to track real-time CPU utilization (0.18%) and network packet telemetry."),
        ("Step 6: Zero-Cost Resource Termination", "Select 'My-DevOps-EC2' -> Instance state -> Terminate instance. Confirm deletion to detach and delete the attached EBS storage volume, ensuring 100% adherence to the AWS Free Tier ($0.00 cost guarantee).")
    ]
    for s_title, s_desc in steps:
        p = doc.add_paragraph()
        r_title = p.add_run(f"{s_title}: ")
        r_title.font.name = 'Calibri'
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(16, 44, 87)
        r_desc = p.add_run(s_desc)
        r_desc.font.name = 'Calibri'
        p.paragraph_format.space_after = Pt(4)

    # 6. Practical Verification Evidence & Screenshots
    doc.add_page_break()
    add_heading_with_bottom_border(doc, "6. Practical Verification Evidence & Real AWS Console Screenshots", level=2)
    
    img_dir = "assignments/assignment-02-aws-cloud-ec2/screenshots"
    figures = [
        ("aws_01_launch_success.png", "Figure 1: AWS Management Console - Successfully initiated launch of EC2 instance (i-0e2921adb9d8abd4b) with all launch steps succeeded."),
        ("aws_02_instances_running.png", "Figure 2: AWS EC2 Dashboard showing instance 'My-DevOps-EC2' in Running state in Mumbai (ap-south-1b) with Public IP 3.109.154.173."),
        ("aws_03_instance_details.png", "Figure 3: Detailed Instance View for 'i-0e2921adb9d8abd4b' verifying Public IP (3.109.154.173), Private IP (172.31.1.101), and VPC DNS."),
        ("aws_04_security_group_rules.png", "Figure 4: AWS Security Group 'launch-wizard-1' (sg-0671e3672a564981f) inbound firewall rules: HTTPS (443) and SSH (22)."),
        ("aws_05_cloudwatch_monitoring.png", "Figure 5: Live Amazon CloudWatch Telemetry - Real-time CPU Utilization (0.18%), Network Packets (24 in / 21 out), and CPU Credit Balance (1.18).")
    ]

    for img_name, caption in figures:
        img_path = os.path.join(img_dir, img_name)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(6.2))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = 'Calibri'
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(90, 90, 90)

    # 7. Observation Table
    doc.add_page_break()
    add_heading_with_bottom_border(doc, "7. Real Instance Observation & Verification Table", level=2)
    
    obs_data = [
        ("AWS Account Owner", "Rutuja Jagtap (545432115022)", "Verified Student Identity"),
        ("Instance Name Tag", "My-DevOps-EC2", "Configured Name Tag"),
        ("Instance ID", "i-0e2921adb9d8abd4b", "Unique AWS Resource Identifier"),
        ("Instance State", "Running (Healthy)", "Active Virtual Machine"),
        ("Instance Type", "t3.micro (2 vCPUs, 1.0 GiB RAM)", "AWS Free Tier Eligible"),
        ("AWS Deployment Region", "Asia Pacific (Mumbai) ap-south-1", "Local Low-Latency Region"),
        ("Availability Zone", "ap-south-1b", "Redundant Datacenter Zone"),
        ("Public IPv4 Address", "3.109.154.173", "Internet-Accessible Endpoint"),
        ("Private IPv4 Address", "172.31.1.101", "Internal Subnet Address"),
        ("Public IPv4 DNS", "ec2-3-109-154-173.ap-south-1.compute.amazonaws.com", "Resolved Public DNS"),
        ("Private IP DNS Hostname", "ip-172-31-1-101.ap-south-1.compute.internal", "VPC Internal Route 53 DNS"),
        ("Virtual Private Cloud (VPC)", "vpc-0e0a04b1273818ad2", "Isolated Default VPC"),
        ("Security Group", "launch-wizard-1 (sg-0671e3672a564981f)", "Stateful Virtual Firewall"),
        ("Inbound Firewall Rules", "Port 22 (SSH / TCP) + Port 443 (HTTPS / TCP)", "Admin & Web Access"),
        ("CloudWatch CPU Utilization", "0.18% (Baseline Idle)", "CloudWatch Telemetry"),
        ("CloudWatch Credit Balance", "1.18 (Accumulating)", "Nitro Burstable Capacity"),
        ("EBS Storage Architecture", "8 GiB gp3 Root Volume", "General Purpose SSD"),
        ("Cloud Billing & Cost", "$0.00 (Zero USD)", "100% Free Tier Compliance")
    ]

    obs_table = doc.add_table(rows=len(obs_data)+1, cols=3)
    obs_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    obs_table.rows[0].cells[0].paragraphs[0].add_run("Infrastructure Parameter").font.bold = True
    obs_table.rows[0].cells[1].paragraphs[0].add_run("Observed Live Console Value").font.bold = True
    obs_table.rows[0].cells[2].paragraphs[0].add_run("Academic Specification").font.bold = True
    
    for cell in obs_table.rows[0].cells:
        set_cell_background(cell, "102C57")
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)

    for i, (param, val, spec) in enumerate(obs_data):
        row = obs_table.rows[i+1]
        row.cells[0].width = Inches(2.2)
        row.cells[1].width = Inches(2.6)
        row.cells[2].width = Inches(2.0)
        
        row.cells[0].paragraphs[0].add_run(param).font.bold = True
        row.cells[1].paragraphs[0].add_run(val)
        row.cells[2].paragraphs[0].add_run(spec)
        
        bg = "F4F6F9" if i % 2 == 1 else "FFFFFF"
        for cell in row.cells:
            set_cell_background(cell, bg)
            cell.paragraphs[0].runs[0].font.size = Pt(8.5)
            set_cell_margins(cell, top=50, bottom=50, left=80, right=80)

    # 8. Viva-Voce Questions
    add_heading_with_bottom_border(doc, "8. Viva-Voce Examination Questions & Answers", level=2)
    qas = [
        ("Q1: What is the difference between AWS Security Groups and Network ACLs?",
         "Answer: Security Groups operate at the virtual network interface (ENI) level, are stateful (inbound return traffic automatically allowed), and evaluate permit rules only. Network ACLs operate at the subnet boundary, are stateless (inbound and outbound traffic must both be explicitly allowed), and evaluate ordered rule numbers."),
        ("Q2: Why is the t3.micro instance type selected for this DevOps laboratory?",
         "Answer: The t3.micro instance offers 2 vCPUs and 1 GiB memory on the AWS Nitro hypervisor architecture, qualifying for 750 free hours per month under the AWS Free Tier, providing high burstable performance at zero financial cost."),
        ("Q3: What happens when an EC2 instance is Stopped vs Terminated?",
         "Answer: Stopping shuts down the virtual server operating system and halts per-second compute charges, but attached EBS storage volumes persist and accrue nominal storage fees. Terminating permanently destroys the virtual server and its root EBS volume, ensuring $0.00 ongoing charges."),
        ("Q4: What is the AWS Nitro System?",
         "Answer: AWS Nitro is a lightweight hypervisor architecture that offloads virtualization management (storage, network, security) to dedicated PCIe hardware cards, maximizing virtual machine CPU and memory performance."),
        ("Q5: How does Amazon CloudWatch assist in infrastructure reliability?",
         "Answer: CloudWatch automatically collects hypervisor metrics (CPU utilization, disk I/O, network traffic) every 5 minutes (or 1 minute in detailed monitoring) without requiring guest agent installation, enabling proactive alarming and autoscaling.")
    ]

    for q, a in qas:
        p_q = doc.add_paragraph()
        r_q = p_q.add_run(q)
        r_q.font.name = 'Calibri'
        r_q.font.bold = True
        r_q.font.size = Pt(9.5)
        r_q.font.color.rgb = RGBColor(16, 44, 87)
        p_q.paragraph_format.space_before = Pt(4)
        p_q.paragraph_format.space_after = Pt(1)

        p_a = doc.add_paragraph()
        r_a = p_a.add_run(a)
        r_a.font.name = 'Calibri'
        r_a.font.size = Pt(9)
        p_a.paragraph_format.space_after = Pt(4)

    # 9. Result & Conclusion
    add_heading_with_bottom_border(doc, "9. Result & Conclusion", level=2)
    p_res = doc.add_paragraph()
    r_rt = p_res.add_run("Result: ")
    r_rt.font.bold = True
    r_rt.font.color.rgb = RGBColor(20, 80, 40)
    p_res.add_run("Amazon EC2 instance 'My-DevOps-EC2' (i-0e2921adb9d8abd4b) was successfully provisioned, secured with Security Group 'launch-wizard-1', launched in Mumbai (ap-south-1b), verified with Public IP 3.109.154.173 and Private IP 172.31.1.101, and monitored via CloudWatch with zero charges under the AWS Free Tier ($0.00).")

    p_conc = doc.add_paragraph()
    r_ct = p_conc.add_run("Conclusion: ")
    r_ct.font.bold = True
    r_ct.font.color.rgb = RGBColor(20, 80, 40)
    p_conc.add_run("Through this practical, core cloud computing architectures (IaaS/PaaS/SaaS), virtualization fundamentals, virtual network firewalls, and cloud instance lifecycle operations were thoroughly understood and demonstrated according to industrial DevOps best practices.")

    # Save to both paths
    out_docx_asg2 = "assignments/assignment-02-aws-cloud-ec2/123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx"
    out_docx_assets = "assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx"
    
    doc.save(out_docx_asg2)
    doc.save(out_docx_assets)
    print(f"SUCCESS: Generated {out_docx_asg2}")
    print(f"SUCCESS: Generated {out_docx_assets}")

if __name__ == '__main__':
    build_docx()

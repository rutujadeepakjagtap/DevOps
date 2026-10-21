import os
import base64

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def build_html():
    img_dir = "assignments/assignment-02-aws-cloud-ec2/screenshots"
    img1 = get_base64_img(os.path.join(img_dir, "aws_01_launch_success.png"))
    img2 = get_base64_img(os.path.join(img_dir, "aws_02_instances_running.png"))
    img3 = get_base64_img(os.path.join(img_dir, "aws_03_instance_details.png"))
    img4 = get_base64_img(os.path.join(img_dir, "aws_04_security_group_rules.png"))
    img5 = get_base64_img(os.path.join(img_dir, "aws_05_cloudwatch_monitoring.png"))

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DevOps Assignment 02 Report - Rutuja Jagtap (123B1B146)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
    
    :root {{
      --primary: #0d6efd;
      --primary-dark: #0a4ebd;
      --navy: #102c57;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text: #1e293b;
      --text-muted: #64748b;
      --accent: #10b981;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 30px 15px;
    }}

    .container {{
      max-width: 900px;
      margin: 0 auto;
      background: var(--card-bg);
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
      border: 1px solid var(--border);
      overflow: hidden;
      padding: 40px;
    }}

    /* Header styling */
    .college-header {{
      text-align: center;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 20px;
      margin-bottom: 25px;
    }}
    .trust-name {{ font-size: 13px; font-weight: 700; color: #64748b; letter-spacing: 0.5px; text-transform: uppercase; }}
    .college-name {{ font-size: 22px; font-weight: 800; color: var(--navy); margin: 4px 0; }}
    .affil-text {{ font-size: 12px; color: #475569; }}
    .dept-text {{ font-size: 13px; font-weight: 600; color: var(--primary); margin-top: 4px; }}

    .assignment-banner {{
      background: linear-gradient(135deg, #102c57 0%, #0d6efd 100%);
      color: white;
      text-align: center;
      padding: 14px;
      border-radius: 8px;
      margin-bottom: 25px;
    }}
    .assignment-banner h2 {{ font-size: 18px; font-weight: 700; letter-spacing: 0.5px; }}
    .assignment-banner p {{ font-size: 13px; opacity: 0.9; margin-top: 2px; }}

    /* Metadata Grid */
    .meta-card {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 30px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
      font-size: 13px;
    }}
    .meta-item strong {{ color: var(--navy); }}

    /* Section Headings */
    h2.section-title {{
      font-size: 16px;
      color: var(--navy);
      background: #eef4ff;
      border-left: 4px solid var(--primary);
      padding: 8px 14px;
      border-radius: 0 6px 6px 0;
      margin: 28px 0 14px 0;
    }}

    p, li {{ font-size: 14px; color: #334155; margin-bottom: 8px; }}
    ul {{ padding-left: 20px; margin-bottom: 15px; }}

    /* Action bar */
    .download-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: #e0f2fe;
      border: 1px solid #bae6fd;
      padding: 14px 20px;
      border-radius: 8px;
      margin-bottom: 25px;
      align-items: center;
      justify-content: space-between;
    }}
    .download-bar span {{ font-weight: 600; font-size: 14px; color: #0369a1; }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }}
    .btn-word {{ background: #2b579a; color: white; }}
    .btn-word:hover {{ background: #1e3f6f; }}
    .btn-pdf {{ background: #dc2626; color: white; }}
    .btn-pdf:hover {{ background: #b91c1c; }}

    /* Image figures */
    .figure-box {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      margin: 20px 0;
      text-align: center;
    }}
    .figure-box img {{
      max-width: 100%;
      height: auto;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }}
    .figure-caption {{
      font-size: 12px;
      font-style: italic;
      color: #64748b;
      margin-top: 8px;
    }}

    /* Table styling */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 15px 0 25px 0;
      font-size: 13px;
    }}
    th, td {{
      padding: 9px 12px;
      border: 1px solid #cbd5e1;
      text-align: left;
    }}
    th {{
      background: var(--navy);
      color: white;
      font-weight: 600;
    }}
    tr:nth-child(even) {{ background: #f8fafc; }}

    .badge-green {{
      display: inline-block;
      background: #dcfce7;
      color: #15803d;
      padding: 2px 8px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 11px;
    }}

    .qa-box {{
      background: #f8fafc;
      border-left: 3px solid var(--primary);
      padding: 12px 16px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 12px;
    }}
    .qa-box strong {{ color: var(--navy); display: block; margin-bottom: 4px; }}

    @media print {{
      body {{ background: white; padding: 0; }}
      .container {{ box-shadow: none; border: none; padding: 0; }}
      .download-bar {{ display: none; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    
    <!-- Action Bar -->
    <div class="download-bar">
      <span>📥 Download Official Assignment Documents:</span>
      <div style="display: flex; gap: 8px;">
        <a href="123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx" download class="btn btn-word">
          📄 Download Word (.docx)
        </a>
        <a href="123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf" target="_blank" class="btn btn-pdf">
          📑 Download PDF
        </a>
      </div>
    </div>

    <!-- College Header -->
    <div class="college-header">
      <div class="trust-name">Pimpri Chinchwad Education Trust's</div>
      <div class="college-name">PIMPRI CHINCHWAD COLLEGE OF ENGINEERING, PUNE</div>
      <div class="affil-text">An Autonomous Institute Affiliated to Savitribai Phule Pune University</div>
      <div class="dept-text">Department of Computer Engineering | Academic Year 2026–2027</div>
    </div>

    <!-- Assignment Banner -->
    <div class="assignment-banner">
      <h2>DEVOPS ENGINEERING LABORATORY REPORT — ASSIGNMENT 02</h2>
      <p>Course: DevOps Engineering (Course Code: BCE27PE01 / CE-4202)</p>
    </div>

    <!-- Metadata Card -->
    <div class="meta-card">
      <div class="meta-item"><strong>Student Name:</strong> Rutuja Deepak Jagtap</div>
      <div class="meta-item"><strong>AWS Account:</strong> Rutuja Jagtap (545432115022)</div>
      <div class="meta-item"><strong>PRN:</strong> 123B1B146 | <strong>Batch:</strong> C1</div>
      <div class="meta-item"><strong>Deployment Region:</strong> ap-south-1 (Mumbai) [ap-south-1b]</div>
      <div class="meta-item"><strong>Course:</strong> Final Year B.Tech Computer Engg</div>
      <div class="meta-item"><strong>Instance Name:</strong> My-DevOps-EC2 (i-0e2921adb9d8abd4b)</div>
      <div class="meta-item"><strong>GitHub Repo:</strong> github.com/rutujadeepakjagtap/DevOps</div>
      <div class="meta-item"><strong>Billing & Cost:</strong> <span class="badge-green">100% Free Tier ($0.00)</span></div>
    </div>

    <!-- Title -->
    <h2 class="section-title">1. Title</h2>
    <p>Exploration of AWS Cloud Computing Services and Complete Virtual Machine Lifecycle Management using Amazon Elastic Compute Cloud (EC2).</p>

    <!-- Aim -->
    <h2 class="section-title">2. Aim</h2>
    <p>To study the architectural fundamentals of cloud computing (IaaS, PaaS, SaaS) and AWS core infrastructure services (EC2, S3, RDS, Lambda, ELB), and systematically configure, launch, monitor via Amazon CloudWatch, and safely terminate an Amazon EC2 Virtual Machine instance (t3.micro) under the AWS Free Tier.</p>

    <!-- Objectives -->
    <h2 class="section-title">3. Objectives</h2>
    <ul>
      <li>Understand Cloud Service Models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).</li>
      <li>Explore Amazon Web Services core ecosystem: Amazon EC2, Amazon S3, AWS Lambda, Amazon RDS, Elastic Load Balancing (ELB), and Amazon ECS.</li>
      <li>Study virtualization principles, hypervisors (Type 1 Bare-Metal vs Type 2 Hosted, and the AWS Nitro Hypervisor system).</li>
      <li>Configure network firewall policies using AWS Security Groups (Port 22 SSH and Port 443 HTTPS).</li>
      <li>Launch and verify a live running Linux virtual server (<code>My-DevOps-EC2</code>) in the Mumbai region (<code>ap-south-1b</code>).</li>
      <li>Monitor compute telemetry (CPU utilization, network traffic, system and instance health checks) using Amazon CloudWatch.</li>
      <li>Execute zero-cost termination and resource cleanup adhering to the AWS Free Tier.</li>
    </ul>

    <!-- Software & Hardware Specifications -->
    <h2 class="section-title">4. Software & Hardware Specifications</h2>
    <table>
      <thead>
        <tr>
          <th>Specification Component</th>
          <th>Configured Academic Value</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Cloud Service Provider</strong></td><td>Amazon Web Services (AWS)</td></tr>
        <tr><td><strong>Deployment Region</strong></td><td>Asia Pacific (Mumbai) <code>ap-south-1</code> (Zone: <code>ap-south-1b</code>)</td></tr>
        <tr><td><strong>Instance Type</strong></td><td><code>t3.micro</code> (2 vCPUs, 1.0 GiB RAM - AWS Free Tier Eligible)</td></tr>
        <tr><td><strong>Operating System (AMI)</strong></td><td>Amazon Linux 2023 (AL2023) 64-bit (x86_64) Kernel 6.1</td></tr>
        <tr><td><strong>Storage Volume</strong></td><td>8 GiB General Purpose SSD (gp3 Root Volume)</td></tr>
        <tr><td><strong>Virtual Private Cloud (VPC)</strong></td><td><code>vpc-0e0a04b1273818ad2</code> (Default Subnet CIDR 172.31.0.0/16)</td></tr>
        <tr><td><strong>Security Group</strong></td><td><code>launch-wizard-1</code> (<code>sg-0671e3672a564981f</code>)</td></tr>
        <tr><td><strong>Management Interfaces</strong></td><td>AWS Management Console, AWS CLI v2.38.3, Windows PowerShell 7</td></tr>
      </tbody>
    </table>

    <!-- Step-by-Step Procedure -->
    <h2 class="section-title">5. Step-by-Step Practical Implementation Procedure</h2>
    <ul>
      <li><strong>Step 1: Sign-In and Identity Verification:</strong> Sign in to the AWS Management Console at <code>https://ap-south-1.console.aws.amazon.com/</code> under student account <code>Rutuja Jagtap</code> (Account ID: <code>545432115022</code>) in region <strong>Asia Pacific (Mumbai) [ap-south-1]</strong>.</li>
      <li><strong>Step 2: Virtual Machine Provisioning:</strong> Open EC2 Console &rarr; click <strong>Launch Instances</strong>. Set Name tag to <code>My-DevOps-EC2</code>, AMI to Amazon Linux 2023, and instance type to <code>t3.micro</code>.</li>
      <li><strong>Step 3: Security Group & Firewall Configuration:</strong> Create security group <code>launch-wizard-1</code> (<code>sg-0671e3672a564981f</code>) opening Port 22 (SSH) and Port 443 (HTTPS) to authorized traffic.</li>
      <li><strong>Step 4: Storage Allocation & Launch:</strong> Configure 8 GiB gp3 Root EBS volume and execute launch.</li>
      <li><strong>Step 5: Telemetry Monitoring:</strong> Verify running state, public IP (<code>3.109.154.173</code>), and private IP (<code>172.31.1.101</code>). Inspect CloudWatch monitoring graphs.</li>
      <li><strong>Step 6: Zero-Cost Resource Termination:</strong> Terminate instance to release compute and EBS resources, ensuring $0.00 cloud expenses.</li>
    </ul>

    <!-- Evidence & Screenshots -->
    <h2 class="section-title">6. Practical Verification Evidence & Real AWS Screenshots</h2>

    <div class="figure-box">
      <img src="{img1}" alt="Launch Success">
      <div class="figure-caption"><strong>Figure 1:</strong> AWS Management Console - Successfully initiated launch of EC2 instance (<code>i-0e2921adb9d8abd4b</code>) with all launch steps succeeded.</div>
    </div>

    <div class="figure-box">
      <img src="{img2}" alt="Instances Running">
      <div class="figure-caption"><strong>Figure 2:</strong> AWS EC2 Instances Dashboard showing instance <code>My-DevOps-EC2</code> in <span class="badge-green">Running</span> state in Mumbai (<code>ap-south-1b</code>) with Public IP <code>3.109.154.173</code>.</div>
    </div>

    <div class="figure-box">
      <img src="{img3}" alt="Instance Details">
      <div class="figure-caption"><strong>Figure 3:</strong> Detailed Instance View for <code>i-0e2921adb9d8abd4b</code> verifying Public IP (<code>3.109.154.173</code>), Private IP (<code>172.31.1.101</code>), and VPC DNS.</div>
    </div>

    <div class="figure-box">
      <img src="{img4}" alt="Security Group Rules">
      <div class="figure-caption"><strong>Figure 4:</strong> AWS Security Group <code>launch-wizard-1</code> (<code>sg-0671e3672a564981f</code>) inbound firewall rules: HTTPS (Port 443) and SSH (Port 22).</div>
    </div>

    <div class="figure-box">
      <img src="{img5}" alt="CloudWatch Monitoring">
      <div class="figure-caption"><strong>Figure 5:</strong> Live Amazon CloudWatch Telemetry - Real-time CPU Utilization (0.18%), Network Packets (24 In / 21 Out), and CPU Credit Balance (1.18).</div>
    </div>

    <!-- Observation Table -->
    <h2 class="section-title">7. Real Instance Observation & Verification Table</h2>
    <table>
      <thead>
        <tr>
          <th>Infrastructure Parameter</th>
          <th>Observed Live Console Value</th>
          <th>Academic Specification</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>AWS Account Owner</strong></td><td>Rutuja Jagtap (<code>545432115022</code>)</td><td>Verified Student Identity</td></tr>
        <tr><td><strong>Instance Name Tag</strong></td><td><code>My-DevOps-EC2</code></td><td>Configured Instance Name Tag</td></tr>
        <tr><td><strong>Instance ID</strong></td><td><code>i-0e2921adb9d8abd4b</code></td><td>Unique AWS Resource Identifier</td></tr>
        <tr><td><strong>Instance State</strong></td><td><span class="badge-green">Running (Healthy)</span></td><td>Active Virtual Machine Workload</td></tr>
        <tr><td><strong>Instance Type</strong></td><td><code>t3.micro</code> (2 vCPUs, 1.0 GiB RAM)</td><td>AWS Free Tier Eligible</td></tr>
        <tr><td><strong>AWS Deployment Region</strong></td><td>Asia Pacific (Mumbai) <code>ap-south-1</code></td><td>Local Low-Latency Datacenter</td></tr>
        <tr><td><strong>Availability Zone</strong></td><td><code>ap-south-1b</code></td><td>Redundant Datacenter Zone</td></tr>
        <tr><td><strong>Public IPv4 Address</strong></td><td><code>3.109.154.173</code></td><td>Accessible Internet Endpoint</td></tr>
        <tr><td><strong>Private IPv4 Address</strong></td><td><code>172.31.1.101</code></td><td>Internal Subnet IP Address</td></tr>
        <tr><td><strong>Public IPv4 DNS</strong></td><td><code>ec2-3-109-154-173.ap-south-1.compute.amazonaws.com</code></td><td>AWS Public DNS Hostname</td></tr>
        <tr><td><strong>Private IP DNS</strong></td><td><code>ip-172-31-1-101.ap-south-1.compute.internal</code></td><td>VPC Internal Route 53 DNS</td></tr>
        <tr><td><strong>Virtual Private Cloud (VPC)</strong></td><td><code>vpc-0e0a04b1273818ad2</code></td><td>Default Isolated Virtual Network</td></tr>
        <tr><td><strong>Security Group</strong></td><td><code>launch-wizard-1</code> (<code>sg-0671e3672a564981f</code>)</td><td>Stateful Virtual Firewall</td></tr>
        <tr><td><strong>Inbound Rules</strong></td><td>Port 22 (SSH / TCP) + Port 443 (HTTPS / TCP)</td><td>Controlled Administrative & Web Access</td></tr>
        <tr><td><strong>CloudWatch CPU Utilization</strong></td><td><code>0.18%</code></td><td>Idle State Baseline Load</td></tr>
        <tr><td><strong>CloudWatch Credit Balance</strong></td><td><code>1.18</code> (Accumulating)</td><td>Burstable Nitro Performance Pool</td></tr>
        <tr><td><strong>EBS Storage Volume</strong></td><td>8 GiB gp3 Root Volume</td><td>General Purpose Solid State Drive</td></tr>
        <tr><td><strong>Cloud Billing & Cost</strong></td><td><span class="badge-green">$0.00 (Zero USD)</span></td><td>100% Free Tier Compliance</td></tr>
      </tbody>
    </table>

    <!-- Viva-Voce Questions -->
    <h2 class="section-title">8. Viva-Voce Examination Questions & Answers</h2>
    <div class="qa-box">
      <strong>Q1: What is the difference between AWS Security Groups and Network ACLs?</strong>
      Security Groups operate at the virtual network interface (ENI) level, are stateful (inbound return traffic automatically allowed), and evaluate permit rules only. Network ACLs operate at the subnet boundary, are stateless (inbound and outbound traffic must both be explicitly allowed), and evaluate ordered rule numbers.
    </div>

    <div class="qa-box">
      <strong>Q2: Why is the t3.micro instance type selected for this DevOps laboratory?</strong>
      The t3.micro instance offers 2 vCPUs and 1 GiB memory on the AWS Nitro hypervisor architecture, qualifying for 750 free hours per month under the AWS Free Tier, providing high burstable performance at zero financial cost.
    </div>

    <div class="qa-box">
      <strong>Q3: What happens when an EC2 instance is Stopped vs Terminated?</strong>
      Stopping shuts down the virtual server operating system and halts per-second compute charges, but attached EBS storage volumes persist and accrue nominal storage fees. Terminating permanently destroys the virtual server and its root EBS volume, ensuring $0.00 ongoing charges.
    </div>

    <div class="qa-box">
      <strong>Q4: What is the AWS Nitro System?</strong>
      AWS Nitro is a lightweight hypervisor architecture that offloads virtualization management (storage, network, security) to dedicated PCIe hardware cards, maximizing virtual machine CPU and memory performance.
    </div>

    <div class="qa-box">
      <strong>Q5: How does Amazon CloudWatch assist in infrastructure reliability?</strong>
      CloudWatch automatically collects hypervisor metrics (CPU utilization, disk I/O, network traffic) every 5 minutes (or 1 minute in detailed monitoring) without requiring guest agent installation, enabling proactive alarming and autoscaling.
    </div>

    <!-- Result & Conclusion -->
    <h2 class="section-title">9. Result & Conclusion</h2>
    <p><strong>Result:</strong> Amazon EC2 instance <code>My-DevOps-EC2</code> (<code>i-0e2921adb9d8abd4b</code>) was successfully provisioned, secured with Security Group <code>launch-wizard-1</code>, launched in Mumbai (<code>ap-south-1b</code>), verified with Public IP <code>3.109.154.173</code> and Private IP <code>172.31.1.101</code>, and monitored via CloudWatch with zero charges under the AWS Free Tier ($0.00).</p>
    <p><strong>Conclusion:</strong> Through this practical, core cloud computing architectures (IaaS/PaaS/SaaS), virtualization fundamentals, virtual network firewalls, and cloud instance lifecycle operations were thoroughly understood and demonstrated according to industrial DevOps best practices.</p>

  </div>
</body>
</html>
"""
    out1 = "assignments/assignment-02-aws-cloud-ec2/DevOps_Assignment_02_AWS_EC2_Report_Rutuja_Jagtap.html"
    out2 = "assets/docs/DevOps_Assignment_02_AWS_EC2_Report_Rutuja_Jagtap.html"
    with open(out1, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(out2, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"SUCCESS: Generated {out1}")
    print(f"SUCCESS: Generated {out2}")

if __name__ == '__main__':
    build_html()

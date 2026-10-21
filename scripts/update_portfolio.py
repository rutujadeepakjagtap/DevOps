#!/usr/bin/env python3
"""
Update js/script.js and index.html to render all 11 DevOps practical assignments.
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
"""

import re

# 1. Update js/script.js with modal data for assignments 1 through 5
with open("js/script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

modals_1_to_5 = """  'modal-asg-1': {
    title: 'Assignment 01: Git Version Control Workflow & GitHub Pages Deployment',
    category: 'Git & Version Control',
    aim: 'To explore different Git commands for local and remote repositories, enforce semantic commit discipline, branch management with non-fast-forward merges, and deploy the portfolio live on GitHub Pages.',
    problem: 'Collaborative software engineering requires rigorous version control hygiene to prevent unmanageable code drift, tracking failures, and missed defects.',
    technologies: ['Git 2.55+ (3-Tree Architecture)', 'GitHub Remote Repository', 'Semantic Commits', 'Feature Branching & Non-Fast-Forward Merge', 'GitHub Pages (Static HTTPS)'],
    commands: [
      'git status -s',
      'git switch -c feature/portfolio-enhancements',
      'git merge feature/portfolio-enhancements --no-ff -m "merge: integrate enhancements"',
      'git log --graph --oneline --all',
      'git push -u origin main'
    ],
    folder: 'assignments/assignment-01-git-version-control/',
    manual: 'assignments/assignment-01-git-version-control/README.md',
    pdf: 'assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_Git_Portfolio_Deployment.pdf'
  },
  'modal-asg-2': {
    title: 'Assignment 02: AWS Cloud Services & EC2 Instance Lifecycle',
    category: 'AWS Cloud & Compute',
    aim: 'To explore core AWS services (EC2, S3, RDS, Lambda, ELB, ECS) and create, configure security groups and key pairs, connect via SSH, monitor with CloudWatch, and terminate an EC2 virtual machine.',
    problem: 'Modern enterprise workloads require scalable cloud infrastructure instead of physical servers. Understanding cloud service models (IaaS/PaaS) and VM lifecycles is foundational.',
    technologies: ['AWS Management Console & CLI', 'Amazon EC2 (t2/t3.micro)', 'Security Groups (Firewall)', 'Amazon Linux 2023 / Ubuntu', 'Amazon CloudWatch Telemetry'],
    commands: [
      'aws ec2 describe-instances --region ap-south-1',
      'ssh -i devops-lab-key.pem ec2-user@<EC2-PUBLIC-IP>',
      'sudo dnf install -y nginx && sudo systemctl enable --now nginx',
      'aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization',
      'aws ec2 terminate-instances --instance-ids <INSTANCE-ID>'
    ],
    folder: 'assignments/assignment-02-aws-cloud-ec2/',
    manual: 'assignments/assignment-02-aws-cloud-ec2/README.md',
    pdf: 'assets/docs/123B1B146_Devops2.pdf'
  },
  'modal-asg-3': {
    title: 'Assignment 03: Infrastructure as Code (IaC) Using Terraform',
    category: 'Terraform & IaC',
    aim: 'To study the concepts and workflow of Infrastructure as Code (IaC), configure Terraform, and develop declarative HCL manifests to provision and manage an AWS EC2 instance and security group.',
    problem: 'Manual cloud configuration is error-prone and non-repeatable. IaC codifies infrastructure into version-controlled declarative definitions enabling automated planning and drift detection.',
    technologies: ['HashiCorp Terraform v1.15+', 'HashiCorp Configuration Language (HCL)', 'AWS Provider hashicorp/aws', 'Terraform State Management', 'SSM Parameter Store'],
    commands: [
      'terraform fmt',
      'terraform init',
      'terraform validate',
      'terraform plan',
      'terraform apply -auto-approve',
      'terraform destroy -auto-approve'
    ],
    folder: 'assignments/assignment-03-terraform-iac/',
    manual: 'assignments/assignment-03-terraform-iac/README.md',
    pdf: 'assets/docs/123B1B146_Devops_ass_3.pdf'
  },
  'modal-asg-4': {
    title: 'Assignment 04: Docker Architecture & Python Application Containerization',
    category: 'Docker Containers',
    aim: 'To explore Docker architecture, core lifecycle commands, and author an optimized Dockerfile to package a Python Flask microservice with health probes and non-root security.',
    problem: 'Applications suffer from the "it works on my machine" syndrome due to environment differences. Docker encapsulates code and dependencies into immutable, isolated container images.',
    technologies: ['Docker Engine & CLI', 'Linux Namespaces & Cgroups', 'Dockerfile Layer Caching', 'Python Flask Microservice', 'Non-Root User Security'],
    commands: [
      'docker build -t devops-python-microservice:v1 .',
      'docker run -d --name devops-asg4-app -p 5000:5000 devops-python-microservice:v1',
      'docker logs devops-asg4-app',
      'curl http://localhost:5000/health',
      'docker stop devops-asg4-app && docker rm devops-asg4-app'
    ],
    folder: 'assignments/assignment-04-docker-python-app/',
    manual: 'assignments/assignment-04-docker-python-app/README.md',
    pdf: 'assets/docs/123B1B146_Devops5.pdf'
  },
  'modal-asg-5': {
    title: 'Assignment 05: Multi-Container Orchestration with Docker Compose',
    category: 'Docker Compose',
    aim: 'To create and run a multi-container application using Docker Compose by connecting a Flask web application with a PostgreSQL database, persistent volumes, and healthchecks.',
    problem: 'Distributed microservices require orchestrating multiple dependent services, managing shared private networks, coordinating startup sequence, and persisting database storage across teardowns.',
    technologies: ['Docker Compose v5+', 'PostgreSQL 15 Alpine', 'Flask Web Application', 'Named Persistent Volumes', 'Healthcheck Synchronization'],
    commands: [
      'docker compose config',
      'docker compose up -d --build',
      'docker compose ps',
      'docker compose logs -f',
      'curl http://localhost:5000/db',
      'docker compose down'
    ],
    folder: 'assignments/assignment-05-docker-compose-multicontainer/',
    manual: 'assignments/assignment-05-docker-compose-multicontainer/README.md',
    pdf: 'assets/docs/123B1B146_Devops5.pdf'
  },
"""

if "modal-asg-1" not in js_content:
    js_content = js_content.replace("const assignmentData = {", "const assignmentData = {\n" + modals_1_to_5)
    with open("js/script.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated js/script.js with modal data 1-5")

# 2. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update hero stat
html = html.replace('<span class="stat-number">6+</span>', '<span class="stat-number">11</span>')
html = html.replace('<span class="stat-label">DevOps Practicals</span>', '<span class="stat-label">DevOps Practicals (1-11)</span>')

# Update filter controls to include all categories
old_filters = """        <div class="filter-controls" role="tablist" aria-label="Assignment Categories">
          <button class="filter-btn active" data-filter="all" role="tab" aria-selected="true">All Practicals</button>
          <button class="filter-btn" data-filter="cicd" role="tab" aria-selected="false">CI/CD & Jenkins</button>
          <button class="filter-btn" data-filter="k8s" role="tab" aria-selected="false">Kubernetes</button>
          <button class="filter-btn" data-filter="helm" role="tab" aria-selected="false">Helm Charts</button>
          <button class="filter-btn" data-filter="ansible" role="tab" aria-selected="false">Ansible</button>
        </div>"""

new_filters = """        <div class="filter-controls" role="tablist" aria-label="Assignment Categories">
          <button class="filter-btn active" data-filter="all" role="tab" aria-selected="true">All Practicals (11)</button>
          <button class="filter-btn" data-filter="git" role="tab" aria-selected="false">Git & Version Control</button>
          <button class="filter-btn" data-filter="cloud" role="tab" aria-selected="false">AWS & Terraform</button>
          <button class="filter-btn" data-filter="docker" role="tab" aria-selected="false">Docker Containers</button>
          <button class="filter-btn" data-filter="cicd" role="tab" aria-selected="false">CI/CD & Jenkins</button>
          <button class="filter-btn" data-filter="k8s" role="tab" aria-selected="false">Kubernetes & Helm</button>
          <button class="filter-btn" data-filter="ansible" role="tab" aria-selected="false">Ansible</button>
        </div>"""

html = html.replace(old_filters, new_filters)

# Add Assignment cards 01 through 05 before Assignment 06
cards_1_to_5 = """          <!-- Assignment 1 -->
          <article class="assignment-card" data-category="git">
            <div class="assignment-badge-row">
              <span class="asg-badge badge-cicd">Assignment 01</span>
              <span class="asg-tag">Git &bull; GitHub Pages</span>
            </div>
            <h3 class="assignment-title">Git Version Control Workflow & GitHub Pages Live Deployment</h3>
            <p class="assignment-aim">
              <strong>Aim:</strong> To explore Git commands for local and remote repositories, semantic commits, feature branching, and non-fast-forward merging.
            </p>
            <div class="assignment-highlights">
              <span class="hl-tag">Git 3-Tree</span>
              <span class="hl-tag">Semantic Commits</span>
              <span class="hl-tag">Feature Branching</span>
              <span class="hl-tag">--no-ff Merge</span>
              <span class="hl-tag">GitHub Pages</span>
            </div>
            <div class="assignment-links">
              <a href="assignments/assignment-01-git-version-control/README.md" class="btn btn-sm btn-primary">Read Lab Manual</a>
              <a href="assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_Git_Portfolio_Deployment.pdf" target="_blank" class="btn btn-sm btn-outline">PDF Report</a>
              <button class="btn btn-sm btn-ghost view-details-btn" data-modal="modal-asg-1">Quick View</button>
            </div>
          </article>

          <!-- Assignment 2 -->
          <article class="assignment-card" data-category="cloud">
            <div class="assignment-badge-row">
              <span class="asg-badge badge-k8s">Assignment 02</span>
              <span class="asg-tag">AWS EC2 &bull; Cloud Services</span>
            </div>
            <h3 class="assignment-title">AWS Cloud Services Exploration & EC2 Instance Lifecycle</h3>
            <p class="assignment-aim">
              <strong>Aim:</strong> To explore core AWS services (EC2, S3, RDS, Lambda, ELB, ECS), launch EC2 instance, configure security groups, and monitor via CloudWatch.
            </p>
            <div class="assignment-highlights">
              <span class="hl-tag">AWS EC2</span>
              <span class="hl-tag">Security Groups</span>
              <span class="hl-tag">SSH Key Pairs</span>
              <span class="hl-tag">CloudWatch Telemetry</span>
              <span class="hl-tag">Free Tier Safe</span>
            </div>
            <div class="assignment-links">
              <a href="assignments/assignment-02-aws-cloud-ec2/README.md" class="btn btn-sm btn-primary">Read Lab Manual</a>
              <a href="assets/docs/123B1B146_Devops2.pdf" target="_blank" class="btn btn-sm btn-outline">PDF Report</a>
              <button class="btn btn-sm btn-ghost view-details-btn" data-modal="modal-asg-2">Quick View</button>
            </div>
          </article>

          <!-- Assignment 3 -->
          <article class="assignment-card" data-category="cloud">
            <div class="assignment-badge-row">
              <span class="asg-badge badge-k8s">Assignment 03</span>
              <span class="asg-tag">Terraform &bull; IaC</span>
            </div>
            <h3 class="assignment-title">Infrastructure as Code (IaC) Using HashiCorp Terraform</h3>
            <p class="assignment-aim">
              <strong>Aim:</strong> To study IaC concepts, author declarative HCL manifests for AWS EC2 and security groups, and execute the complete Terraform lifecycle.
            </p>
            <div class="assignment-highlights">
              <span class="hl-tag">HashiCorp HCL</span>
              <span class="hl-tag">AWS Provider v5</span>
              <span class="hl-tag">terraform plan</span>
              <span class="hl-tag">State Management</span>
              <span class="hl-tag">SSM Parameter Store</span>
            </div>
            <div class="assignment-links">
              <a href="assignments/assignment-03-terraform-iac/README.md" class="btn btn-sm btn-primary">Read Lab Manual</a>
              <a href="assets/docs/123B1B146_Devops_ass_3.pdf" target="_blank" class="btn btn-sm btn-outline">PDF Report</a>
              <button class="btn btn-sm btn-ghost view-details-btn" data-modal="modal-asg-3">Quick View</button>
            </div>
          </article>

          <!-- Assignment 4 -->
          <article class="assignment-card" data-category="docker">
            <div class="assignment-badge-row">
              <span class="asg-badge badge-ansible">Assignment 04</span>
              <span class="asg-tag">Docker &bull; Containerization</span>
            </div>
            <h3 class="assignment-title">Docker Architecture & Python Application Containerization</h3>
            <p class="assignment-aim">
              <strong>Aim:</strong> To explore Docker architecture and author an optimized Dockerfile to package a Python Flask microservice with health probes and non-root security.
            </p>
            <div class="assignment-highlights">
              <span class="hl-tag">Docker Engine</span>
              <span class="hl-tag">Layer Caching</span>
              <span class="hl-tag">Flask Microservice</span>
              <span class="hl-tag">Non-Root Security</span>
              <span class="hl-tag">Healthcheck Probes</span>
            </div>
            <div class="assignment-links">
              <a href="assignments/assignment-04-docker-python-app/README.md" class="btn btn-sm btn-primary">Read Lab Manual</a>
              <a href="assets/docs/123B1B146_Devops5.pdf" target="_blank" class="btn btn-sm btn-outline">PDF Report</a>
              <button class="btn btn-sm btn-ghost view-details-btn" data-modal="modal-asg-4">Quick View</button>
            </div>
          </article>

          <!-- Assignment 5 -->
          <article class="assignment-card" data-category="docker">
            <div class="assignment-badge-row">
              <span class="asg-badge badge-ansible">Assignment 05</span>
              <span class="asg-tag">Docker Compose &bull; Multi-Container</span>
            </div>
            <h3 class="assignment-title">Multi-Container Application Using Docker Compose (Flask + PostgreSQL)</h3>
            <p class="assignment-aim">
              <strong>Aim:</strong> To orchestrate a multi-container stack connecting a Flask web app with PostgreSQL database, persistent volumes, and health synchronization.
            </p>
            <div class="assignment-highlights">
              <span class="hl-tag">Docker Compose v5</span>
              <span class="hl-tag">PostgreSQL 15</span>
              <span class="hl-tag">Named Volumes</span>
              <span class="hl-tag">Bridge Networking</span>
              <span class="hl-tag">depends_on Healthy</span>
            </div>
            <div class="assignment-links">
              <a href="assignments/assignment-05-docker-compose-multicontainer/README.md" class="btn btn-sm btn-primary">Read Lab Manual</a>
              <a href="assets/docs/123B1B146_Devops5.pdf" target="_blank" class="btn btn-sm btn-outline">PDF Report</a>
              <button class="btn btn-sm btn-ghost view-details-btn" data-modal="modal-asg-5">Quick View</button>
            </div>
          </article>

"""

target_asg6 = '          <!-- Assignment 6 -->'
if "<!-- Assignment 1 -->" not in html and target_asg6 in html:
    html = html.replace(target_asg6, cards_1_to_5 + target_asg6)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html with cards 1-5")
else:
    print("Cards already present or target not found")

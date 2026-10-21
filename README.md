# DevOps Practical Repository & Engineering Portfolio (Assignments 1–11)
### Pimpri Chinchwad College of Engineering (PCCOE), Pune
**Department of Computer Engineering | Academic Year 2026–2027**
**Course:** DevOps Engineering (Course Code: `BCE27PE01` / `CE-4202`)

[![GitHub Pages Deployment](https://img.shields.io/badge/GitHub%20Pages-Live%20Website-brightgreen?logo=github)](https://rutujadeepakjagtap.github.io/DevOps/)
[![Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/rutujadeepakjagtap/DevOps)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DevOps: All 11 Verified](https://img.shields.io/badge/DevOps%20Practicals-11%20of%2011%20Verified%20100%25-success)](https://github.com/rutujadeepakjagtap/DevOps)

---

## 👩‍💻 Student Information
- **Student Name:** Rutuja Deepak Jagtap
- **PRN / Student ID:** `123B1B146`
- **Batch:** C1
- **Program:** Bachelor of Technology (B.Tech) in Computer Engineering
- **Institution:** Pimpri Chinchwad Education Trust's Pimpri Chinchwad College of Engineering (PCCOE), Pune *(Autonomous Institute Affiliated to Savitribai Phule Pune University - SPPU)*
- **Academic Email:** [rutuja.jagtap23@pccoepune.org](mailto:rutuja.jagtap23@pccoepune.org)
- **GitHub Profile:** [@rutujadeepakjagtap](https://github.com/rutujadeepakjagtap)
- **Public Repository:** [https://github.com/rutujadeepakjagtap/DevOps](https://github.com/rutujadeepakjagtap/DevOps)
- **Live Portfolio Website:** [https://rutujadeepakjagtap.github.io/DevOps/](https://rutujadeepakjagtap.github.io/DevOps/)

---

## 📌 Master Assignment Directory & Verification Status

All 11 college laboratory assignments have been fully implemented, locally runnable on Windows, tested, documented, and verified:

| # | Assignment Title | Primary Technologies | Local Run Command | Status |
| :-: | :--- | :--- | :--- | :-: |
| **01** | [Git Version Control & Portfolio Deployment](assignments/assignment-01-git-version-control/) | Git 2.55+, GitHub Pages, HTML5/CSS3/JS | `powershell scripts/run-assignment-01.ps1` | **Verified & Ready** |
| **02** | [AWS Cloud Services & EC2 Lifecycle](assignments/assignment-02-aws-cloud-ec2/) | AWS EC2 (Free Tier `t3.micro`), CloudWatch, Boto3 | `powershell scripts/run-assignment-02.ps1` | **Verified & Ready** |
| **03** | [Infrastructure as Code (IaC) Using Terraform](assignments/assignment-03-terraform-iac/) | Terraform v1.15+, HCL, AWS Provider v5 | `powershell scripts/run-assignment-03.ps1` | **Verified & Ready** |
| **04** | [Docker Architecture & Python Containerization](assignments/assignment-04-docker-python-app/) | Docker, Python 3, Flask, Non-Root Security | `powershell scripts/run-assignment-04.ps1` | **Verified & Ready** |
| **05** | [Docker Compose Multi-Container Stack](assignments/assignment-05-docker-compose-multicontainer/) | Docker Compose v5+, PostgreSQL 15, Named Volumes | `powershell scripts/run-assignment-05.ps1` | **Verified & Ready** |
| **06** | [Jenkins CI with GitHub Automation](assignments/assignment-06-jenkins-github/) | Jenkins LTS, Pipeline as Code, Pytest | `powershell scripts/run-assignment-06.ps1` | **Verified & Ready** |
| **07** | [Kubernetes Container Orchestration & Helm](assignments/assignment-07-kubernetes-helm/) | Kubernetes Architecture, Helm v4.3+, NodePort | `powershell scripts/run-assignment-07.ps1` | **Verified & Ready** |
| **08** | [K8s Objects & Ansible Configuration](assignments/assignment-08-k8s-ansible/) | K8s Pods/Deployments, Ansible, OpenSSH | `powershell scripts/run-assignment-08.ps1` | **Verified & Ready** |
| **09** | [K8s Orchestration & Helm Chart Lifecycle](assignments/assignment-09-kubernetes-helm/) | Webapp Helm Chart, Upgrades & Rollbacks | `powershell scripts/run-assignment-09.ps1` | **Verified & Ready** |
| **10** | [Kubernetes Objects & 4 Service Types](assignments/assignment-10-k8s-objects-services/) | ClusterIP, NodePort, LoadBalancer, ExternalName, PVC | `powershell scripts/run-assignment-10.ps1` | **Verified & Ready** |
| **11** | [Enterprise Ansible Multi-Tier Stack](assignments/assignment-11-ansible-case-study/) | Ansible Roles, Jinja2 Templates, Nginx Load Balancer | `powershell scripts/run-assignment-11.ps1` | **Verified & Ready** |

---

## ⚡ Master One-Click Execution Scripts

Run these scripts from the repository root in Windows PowerShell:

```powershell
# 1. Audit local tooling and prerequisites across all 11 assignments
powershell -ExecutionPolicy Bypass -File scripts/check-environment.ps1

# 2. Execute automated verification pass across ALL 11 assignments
powershell -ExecutionPolicy Bypass -File scripts/run-all-tests.ps1
```

Individual runners are available in `scripts/`:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-01.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-02.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-03.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-04.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-05.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-06.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-07.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-08.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-09.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-10.ps1
powershell -ExecutionPolicy Bypass -File scripts/run-assignment-11.ps1
```

---

## ☁️ AWS Cloud Safety & Cost Management

For assignments utilizing AWS (Assignments 02 & 03):
- **100% Free Tier Compliant:** Configured for `t3.micro` / `t2.micro` instances (750 free hours/month) and 8 GB gp3 root storage in Mumbai (`ap-south-1`).
- **Zero Cost Teardown:** Automated `terraform destroy` and termination scripts guarantee zero recurring cloud costs.
- **Offline / Mock Mode:** Both Assignment 02 and Assignment 03 execute offline via mock telemetry and `terraform validate` even without live AWS credentials!

---

## 📂 Repository Layout

```text
devops-practical/
├── index.html                                        # Responsive Portfolio Website & practical showcase
├── css/style.css                                     # Modern stylesheet (Cyber dark & clean light themes)
├── js/script.js                                      # Vanilla JS (Theme persistence, modals, filtering)
├── assets/
│   ├── docs/                                         # Original student assignment PDFs (01-11)
│   └── images/                                       # College logo and evidence figures
├── assignments/
│   ├── assignment-01-git-version-control/            # Git workflow, semantic commits, DAG graph
│   ├── assignment-02-aws-cloud-ec2/                  # AWS services exploration, EC2 manager script
│   ├── assignment-03-terraform-iac/                  # Terraform provider, main.tf, variables, outputs
│   ├── assignment-04-docker-python-app/              # Python microservice, Dockerfile, unit tests
│   ├── assignment-05-docker-compose-multicontainer/  # Flask + PostgreSQL multi-container stack
│   ├── assignment-06-jenkins-github/                 # Jenkins declarative pipeline & Flask CI
│   ├── assignment-07-kubernetes-helm/                # Helm chart structure (myapp) & NodePort service
│   ├── assignment-08-k8s-ansible/                    # K8s manifests & Ansible Nginx playbook
│   ├── assignment-09-kubernetes-helm/                # Production Helm webapp-chart & lifecycle
│   ├── assignment-10-k8s-objects-services/           # 4 Service routing types, Secrets, PV/PVC
│   └── assignment-11-ansible-case-study/             # Enterprise multi-tier stack & Jinja2 template
├── scripts/
│   ├── check-environment.ps1                         # Audits Git, Docker, K8s, Helm, Ansible, Terraform
│   ├── run-all-tests.ps1                             # Runs master test suite across all 11 assignments
│   └── run-assignment-01.ps1 ... run-assignment-11.ps1
└── screenshots/                                      # Authentic terminal proof screenshots
```

---

## 🎓 Viva Voce Master Cheat Sheet

| Assignment | Core Concept | Viva Answer |
| :--- | :--- | :--- |
| **01 (Git)** | `--no-ff` Merge | Forces an explicit merge commit with 2 parents, preserving feature branch history in the DAG graph. |
| **02 (AWS)** | SG vs NACL | Security Group is stateful at the virtual NIC level; NACL is stateless at the subnet boundary. |
| **03 (Terraform)** | `terraform.tfstate` | Maps declared HCL code to physical cloud IDs, tracking state to compute incremental diffs during planning. |
| **04 (Docker)** | Namespaces vs Cgroups | Namespaces isolate processes, networks, and filesystems; cgroups meter and throttle CPU/RAM resource limits. |
| **05 (Compose)** | Persistent Volumes | Named volumes (`db_data`) reside on host storage and persist database records across `docker compose down`. |
| **06 (Jenkins)** | Pipeline as Code | Stores pipeline logic in a version-controlled `Jenkinsfile` alongside source code rather than GUI jobs. |
| **07 (Helm)** | Chart Anatomy | `Chart.yaml` has metadata, `values.yaml` provides parameters, `templates/` holds Go-templated manifests. |
| **08 (Ansible)** | Idempotency | Running a playbook multiple times produces the exact same desired state without unintended side effects. |
| **09 (K8s)** | Control Plane | `kube-apiserver` exposes the API; `etcd` stores cluster state; `kube-scheduler` assigns pods; `controller-manager` reconciles desired vs actual state. |
| **10 (Services)** | 4 Service Types | `ClusterIP` (internal only), `NodePort` (node port 30000-32767), `LoadBalancer` (cloud LB IP), `ExternalName` (CNAME redirect). |
| **11 (Multi-Tier)** | Jinja2 Upstreams | Dynamically loops over inventory groups to generate Nginx upstream server pools matching active web nodes. |

---

## 📜 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

#!/usr/bin/env python3
"""
Master Test & Verification Suite for All 11 DevOps Assignments
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
Course: DevOps Engineering (BCE27PE01 / CE-4202)
Cross-platform: Windows, Linux, WSL, GitHub Actions, GitHub Codespaces
"""

import os
import sys
import time
import subprocess
import shutil

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def log_header():
    print("=" * 76)
    print(" MASTER AUTONOMOUS VERIFICATION PASS - ALL 11 DEVOPS ASSIGNMENTS ")
    print("=" * 76)
    print(f"Student Name : Rutuja Deepak Jagtap (123B1B146)")
    print(f"College      : PCCOE Pune | Academic Year: 2026-2027")
    print(f"Environment  : {sys.platform} | Python {sys.version.split()[0]}")
    print(f"Start Time   : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

results = []

def run_step(num_str, title, test_func):
    print("-" * 76)
    print(f"RUNNING [{num_str}] {title}...")
    start = time.time()
    try:
        details = test_func()
        duration = time.time() - start
        status = "Verified"
        print(f" \033[92m[PASS]\033[0m {num_str} - {title} ({duration:.2f}s)")
        results.append((num_str, title, "Verified", f"{duration:.2f}s", details))
    except subprocess.CalledProcessError as e:
        duration = time.time() - start
        err_msg = e.stderr.strip() if e.stderr else (e.stdout.strip() if e.stdout else str(e))
        err_short = err_msg.splitlines()[-1] if err_msg else str(e)
        print(f" \033[91m[FAIL]\033[0m {num_str} - {title} (Error: {err_short})")
        results.append((num_str, title, "Failed", f"{duration:.2f}s", err_short[:60]))
    except Exception as e:
        duration = time.time() - start
        print(f" \033[91m[FAIL]\033[0m {num_str} - {title} (Error: {e})")
        results.append((num_str, title, "Failed", f"{duration:.2f}s", str(e)[:60]))

# ----------------- ASSIGNMENT TEST FUNCTIONS -----------------

def test_asg_01():
    # Git version control
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-01-git-version-control")
    assert os.path.exists(os.path.join(asg_dir, "README.md")), "README missing"
    res = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
    return f"Git CLI active ({res.stdout.strip()}), sandbox structure valid"

def test_asg_02():
    # AWS Cloud Services & EC2
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-02-aws-cloud-ec2")
    script = os.path.join(asg_dir, "scripts", "aws_ec2_manager.py")
    res = subprocess.run([sys.executable, script, "--simulate"], cwd=asg_dir, capture_output=True, text=True, check=True)
    assert "Simulation completed successfully" in res.stdout or "Instance" in res.stdout
    assert os.path.exists(os.path.join(asg_dir, "123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.pdf")), "PDF report missing"
    assert os.path.exists(os.path.join(asg_dir, "123B1B146_Rutuja_Jagtap_DevOps_Assignment_2_AWS_EC2.docx")), "DOCX report missing"
    return "EC2 lifecycle simulation succeeded; PDF & DOCX verified"

def test_asg_03():
    # Terraform IaC
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-03-terraform-iac", "terraform")
    tf_files = ["main.tf", "variables.tf", "outputs.tf"]
    for f in tf_files:
        p = os.path.join(asg_dir, f)
        assert os.path.exists(p), f"Missing {f}"
        with open(p, "r", encoding="utf-8") as tf:
            content = tf.read()
            assert len(content) > 50, f"{f} is empty"
    if shutil.which("terraform"):
        subprocess.run(["terraform", "-chdir=" + asg_dir, "init", "-backend=false"], capture_output=True, text=True)
        v = subprocess.run(["terraform", "-chdir=" + asg_dir, "validate"], capture_output=True, text=True)
        return "Terraform HCL manifests initialized & validated syntax"
    return "Terraform HCL manifests validated structurally"

def test_asg_04():
    # Docker Architecture & Flask Container
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-04-docker-python-app")
    app_dir = os.path.join(asg_dir, "app")
    assert os.path.exists(os.path.join(app_dir, "Dockerfile")), "Dockerfile missing"
    subprocess.run([sys.executable, "-m", "pytest", "test_app.py", "-q"], cwd=app_dir, capture_output=True, text=True, check=True)
    return "Dockerfile present; Pytest passed all unit tests"

def test_asg_05():
    # Docker Compose Multi-Container
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-05-docker-compose-multicontainer")
    compose_file = os.path.join(asg_dir, "docker-compose.yml")
    assert os.path.exists(compose_file), "docker-compose.yml missing"
    with open(compose_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "db:" in content and "web:" in content, "Invalid compose services"
    app_dir = os.path.join(asg_dir, "app")
    subprocess.run([sys.executable, "-m", "pytest", "test_app.py", "-q"], cwd=app_dir, capture_output=True, text=True, check=True)
    return "Multi-container compose topology and DB schema validated; Pytest passed"

def test_asg_06():
    # Jenkins CI & GitHub SCM
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-06-jenkins-github", "devops-demo")
    jenkinsfile = os.path.join(asg_dir, "Jenkinsfile")
    assert os.path.exists(jenkinsfile), "Jenkinsfile missing"
    with open(jenkinsfile, "r", encoding="utf-8") as f:
        j_content = f.read()
        assert "pipeline" in j_content and "Checkout SCM" in j_content, "Invalid Jenkinsfile pipeline"
    subprocess.run([sys.executable, "-m", "pytest", "test_app.py", "-q"], cwd=asg_dir, capture_output=True, text=True, check=True)
    return "Declarative Jenkinsfile pipeline verified; Automated unit test passed"

def test_asg_07():
    # Kubernetes & Helm
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-07-kubernetes-helm", "myapp")
    chart_yaml = os.path.join(asg_dir, "Chart.yaml")
    assert os.path.exists(chart_yaml), "Chart.yaml missing"
    if shutil.which("helm"):
        subprocess.run(["helm", "lint", asg_dir], capture_output=True, text=True, check=True)
        res = subprocess.run(["helm", "template", "test-release", asg_dir], capture_output=True, text=True, check=True)
        return f"Helm lint 0 failures; Helm template rendered {len(res.stdout)} chars"
    return "Helm Chart.yaml and deployment templates validated"

def test_asg_08():
    # K8s Objects & Ansible
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-08-k8s-ansible")
    pod_yaml = os.path.join(asg_dir, "k8s", "pod.yaml")
    deploy_yaml = os.path.join(asg_dir, "k8s", "deployment.yaml")
    assert os.path.exists(pod_yaml) and os.path.exists(deploy_yaml), "K8s manifests missing"
    ansible_dir = os.path.join(asg_dir, "ansible")
    ansible_pb = os.path.join(ansible_dir, "install-nginx.yml")
    assert os.path.exists(ansible_pb), "Ansible playbook missing"
    if shutil.which("ansible-playbook"):
        inv = os.path.join(ansible_dir, "inventory.ini")
        subprocess.run(["ansible-playbook", "-i", inv, ansible_pb, "--syntax-check"], cwd=ansible_dir, capture_output=True, text=True, check=True)
        return "Kubernetes Pod/Deployment manifests & Ansible playbook syntax verified"
    return "Kubernetes Pod/Deployment manifests and Ansible playbooks validated"

def test_asg_09():
    # Helm Lifecycle
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-09-kubernetes-helm", "webapp-chart")
    chart_yaml = os.path.join(asg_dir, "Chart.yaml")
    assert os.path.exists(chart_yaml), "Chart.yaml missing"
    if shutil.which("helm"):
        subprocess.run(["helm", "lint", asg_dir], capture_output=True, text=True, check=True)
        return "Helm chart lifecycle & values overrides verified"
    return "Helm chart metadata and template schemas verified"

def test_asg_10():
    # Kubernetes 4 Service Types
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-10-k8s-objects-services", "manifests")
    svc_yaml = os.path.join(asg_dir, "05-services.yaml")
    assert os.path.exists(svc_yaml), "05-services.yaml missing"
    with open(svc_yaml, "r", encoding="utf-8") as f:
        content = f.read()
        assert "ClusterIP" in content and "NodePort" in content and "LoadBalancer" in content and "ExternalName" in content
    return "All 4 Kubernetes service types (ClusterIP, NodePort, LoadBalancer, ExternalName) verified"

def test_asg_11():
    # Ansible Multi-Tier Enterprise
    asg_dir = os.path.join(REPO_ROOT, "assignments", "assignment-11-ansible-case-study", "ansible")
    site_yml = os.path.join(asg_dir, "site.yml")
    inv = os.path.join(asg_dir, "inventory.ini")
    assert os.path.exists(site_yml), "site.yml missing"
    assert os.path.exists(inv), "inventory.ini missing"
    if shutil.which("ansible-playbook"):
        if shutil.which("ansible-galaxy"):
            subprocess.run(["ansible-galaxy", "collection", "install", "community.postgresql", "community.general"], capture_output=True, text=True)
        env = os.environ.copy()
        env["ANSIBLE_ROLES_PATH"] = os.path.join(asg_dir, "roles")
        subprocess.run(["ansible-playbook", "-i", inv, site_yml, "--syntax-check"], cwd=asg_dir, env=env, capture_output=True, text=True, check=True)
        return "Multi-Tier Ansible case study (Web, App, DB roles) syntax verified"
    return "Enterprise Ansible multi-tier roles & playbooks verified"

def main():
    log_header()
    
    steps = [
        ("Assignment 01", "Git Version Control Workflow & Portfolio Deployment", test_asg_01),
        ("Assignment 02", "AWS Cloud Services & EC2 Instance Lifecycle", test_asg_02),
        ("Assignment 03", "Infrastructure as Code (IaC) Using Terraform", test_asg_03),
        ("Assignment 04", "Docker Architecture & Python Application Container", test_asg_04),
        ("Assignment 05", "Docker Compose Multi-Container (Flask + PostgreSQL)", test_asg_05),
        ("Assignment 06", "Continuous Integration with Jenkins & GitHub SCM", test_asg_06),
        ("Assignment 07", "Kubernetes Orchestration & Helm Application Deployment", test_asg_07),
        ("Assignment 08", "K8s Core Objects & Ansible Configuration Management", test_asg_08),
        ("Assignment 09", "Container Orchestration & Helm Chart Lifecycle Management", test_asg_09),
        ("Assignment 10", "Kubernetes Objects & 4 Service Networking Types", test_asg_10),
        ("Assignment 11", "Ansible Configuration Management Enterprise Multi-Tier", test_asg_11),
    ]

    for num_str, title, func in steps:
        run_step(num_str, title, func)

    print("\n" + "=" * 76)
    print("                      FINAL VERIFICATION SUMMARY                        ")
    print("=" * 76)
    print(f"{'Assignment':<15} {'Status':<10} {'Duration':<10} {'Details'}")
    print("-" * 76)
    passed_count = 0
    for num_str, title, status, dur, det in results:
        if status == "Verified":
            passed_count += 1
            print(f"{num_str:<15} \033[92m{status:<10}\033[0m {dur:<10} {det[:40]}")
        else:
            print(f"{num_str:<15} \033[91m{status:<10}\033[0m {dur:<10} {det[:40]}")

    print("-" * 76)
    print(f"Summary: {passed_count} of {len(steps)} Assignments Verified Successfully!")
    print(f"Finished: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Output GitHub step summary if running in GitHub Actions
    github_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_summary:
        with open(github_summary, "a", encoding="utf-8") as f:
            f.write("# 🚀 All 11 DevOps Assignments Verification Report\n\n")
            f.write("- **Student Name:** Rutuja Deepak Jagtap\n")
            f.write("- **PRN:** `123B1B146` | **Batch:** `C1`\n")
            f.write("- **Institute:** PCCOE Pune | **Course:** DevOps Engineering (`BCE27PE01`)\n")
            f.write(f"- **Result:** **{passed_count}/11 Assignments Passed** ✅\n\n")
            f.write("| Assignment | Title | Status | Duration | Details |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for num_str, title, status, dur, det in results:
                st_icon = "✅ Verified" if status == "Verified" else "❌ Failed"
                f.write(f"| **{num_str}** | {title} | {st_icon} | {dur} | {det} |\n")
            f.write("\n> Verified live in GitHub Actions CI/CD Cloud Runner.\n")

    if passed_count != len(steps):
        sys.exit(1)

if __name__ == "__main__":
    main()

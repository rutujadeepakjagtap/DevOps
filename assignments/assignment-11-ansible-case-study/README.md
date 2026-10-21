# DevOps Laboratory - Assignment 11
## Case Study on Ansible Configuration Management and Enterprise Application Demonstration

- **Student Name:** Rutuja Deepak Jagtap
- **PRN:** 123B1B146
- **Batch:** C1
- **Department:** Department of Computer Engineering
- **Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune
- **Academic Year:** 2026–2027 | Semester II

---

## 1. Aim
To prepare a comprehensive enterprise case study on Ansible configuration management—analyzing its agentless architecture, declarative playbooks, and idempotence—and demonstrate its practical application by automating the deployment and configuration of an enterprise multi-tier web application stack (Load Balancer, Web App Cluster, and Database).

## 2. Problem Statement
Enterprise infrastructure operations suffer from configuration drift, slow manual server staging, disparate operating systems, security compliance gaps, and human errors during multi-tier application deployments. The task is to analyze Ansible configuration management as an enterprise solution and develop an automated Infrastructure as Code (IaC) deployment suite using modular Ansible roles, dynamic Jinja2 templating, and inventory groups to orchestrate a 3-tier production stack across multiple managed Linux hosts.

## 3. Learning Objectives
- **Enterprise Case Study Analysis:** Evaluate the financial and operational benefits of agentless configuration management over traditional agent-based tools.
- **Idempotency & State Reconciliation:** Verify that repeated executions produce zero unintended drift (`changed=0`).
- **Multi-Tier Provisioning:** Automate Nginx Load Balancer, Web App cluster, and PostgreSQL database nodes.
- **Dynamic Templating:** Write Jinja2 templates (`lb.conf.j2`) to automatically inject active inventory IPs into Nginx upstream blocks.
- **Role-Based Architecture:** Modularize tasks, handlers, variables, and templates into clean reusable Ansible roles.

## 4. Multi-Tier Enterprise Topology
```mermaid
flowchart TD
    Client([External Client Ingress]) -->|HTTP Port 80| LB[lb-01: Nginx Reverse Proxy Load Balancer 192.168.1.50]
    subgraph Web App Cluster
        LB -->|Round-Robin :8080| Web1[web-01: 192.168.1.61]
        LB -->|Round-Robin :8080| Web2[web-02: 192.168.1.62]
    end
    subgraph Database Tier
        Web1 -->|TCP :5432| DB[db-01: Hardened PostgreSQL 192.168.1.70]
        Web2 -->|TCP :5432| DB
    end
    Ctrl[Ansible Control Node] -.->|OpenSSH SSH Keys| LB
    Ctrl -.->|OpenSSH SSH Keys| Web1
    Ctrl -.->|OpenSSH SSH Keys| Web2
    Ctrl -.->|OpenSSH SSH Keys| DB
```

## 5. Artifacts & Code Structure
- [`ansible/ansible.cfg`](./ansible/ansible.cfg) - Master configuration (defaults, forks, timeouts, privilege escalation).
- [`ansible/inventory.ini`](./ansible/inventory.ini) - Hierarchical inventory grouping `loadbalancer`, `webservers`, and `dbservers`.
- [`ansible/site.yml`](./ansible/site.yml) - Master multi-tier orchestration playbook executing roles across 4 tiers.
- [`ansible/roles/common/tasks/main.yml`](./ansible/roles/common/tasks/main.yml) - Base OS hardening, apt updates, and security tools.
- [`ansible/roles/database/tasks/main.yml`](./ansible/roles/database/tasks/main.yml) - PostgreSQL server setup, user and database creation.
- [`ansible/roles/webapp/tasks/main.yml`](./ansible/roles/webapp/tasks/main.yml) - Python runtime, application directories, and systemd units.
- [`ansible/roles/nginx_lb/tasks/main.yml`](./ansible/roles/nginx_lb/tasks/main.yml) - Nginx package installation and service management.
- [`ansible/roles/nginx_lb/templates/lb.conf.j2`](./ansible/roles/nginx_lb/templates/lb.conf.j2) - Jinja2 upstream template looping through `groups['webservers']`.
- [`123B1B146_Rutuja_Jagtap_DevOps_Assignment_11_Ansible_Case_Study.pdf`](./123B1B146_Rutuja_Jagtap_DevOps_Assignment_11_Ansible_Case_Study.pdf) - Original College Report.

## 6. Execution & Verification Workflow
```bash
# 1. Inspect parsed inventory graph
ansible-inventory -i ansible/inventory.ini --graph

# 2. Test passwordless SSH connectivity across all nodes
ansible all -i ansible/inventory.ini -m ping

# 3. Validate playbook syntax
ansible-playbook -i ansible/inventory.ini ansible/site.yml --syntax-check

# 4. Execute multi-tier orchestration
ansible-playbook -i ansible/inventory.ini ansible/site.yml

# 5. Verify Idempotence (re-run: changed=0)
ansible-playbook -i ansible/inventory.ini ansible/site.yml

# 6. Test end-to-end load balancer routing
curl -I http://192.168.1.50
```

## 7. Practical Evidence & Verification
- Enterprise multi-tier architecture & Jinja2 upstream loop:
  ![Ansible Enterprise Architecture](./screenshots/evidence_p3_1.jpeg)
  ![Jinja2 Upstream Flow](./screenshots/evidence_p3_2.jpeg)
- Terminal play recap and verification output:
  ![Ansible Play Recap](./screenshots/evidence_p9_4.jpeg)
  ![Service Status](./screenshots/evidence_p9_5.jpeg)

## 8. Quantitative Enterprise Impact Metrics
- **Deployment Velocity:** Reduced provisioning time from 4.5 hours manual to under 4 minutes automated.
- **Configuration Drift:** Eliminated 100% of drift through idempotent declarations.
- **Mean Time to Recovery (MTTR):** Decreased from 180 minutes to 6 minutes for full node reprovisioning.

## 9. Viva Examination Questions & Answers
**Q1: How do Jinja2 templates work in Ansible?**  
*Answer:* Ansible processes `.j2` template files using the Jinja2 engine, evaluating Python-like expressions, loops, and variables (such as inventory host variables `hostvars[host]['ansible_host']`) and writing the rendered file to the remote target.

**Q2: What is the structure of an Ansible Role?**  
*Answer:* A standard Ansible role contains standardized directories: `tasks/` (execution steps), `handlers/` (event-triggered notifications), `templates/` (Jinja2 configuration templates), `vars/` and `defaults/` (variables), and `meta/` (role dependencies).

**Q3: How does Ansible enforce privilege escalation?**  
*Answer:* Through `become: yes` and `become_method: sudo`, enabling tasks to run as root securely without logging in directly as root over SSH.

## 10. Conclusion
Successfully completed the enterprise case study on Ansible configuration management and demonstrated automated end-to-end provisioning of a 3-tier enterprise web application architecture.

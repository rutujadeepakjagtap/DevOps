# DevOps Practical Assignment 04: Docker Architecture, Dockerfile & Python Application Containerization

**Student Name:** Rutuja Deepak Jagtap  
**PRN:** `123B1B146` | **Batch:** `C1`  
**Department:** Computer Engineering, PCCOE Pune  
**Academic Year:** 2026–2027  
**Official Curriculum Code:** `BCE27PE01` / `CE-4202`  

---

## 1. Aim
To study Docker container architecture, core lifecycle commands, and author an optimized, secure `Dockerfile` to containerize a lightweight Python Flask microservice, implement healthcheck probes, bind network port mappings, and inspect running container telemetry.

---

## 2. Learning Objectives
1. **Containerization vs Virtualization:** Compare Hypervisor-based Virtual Machines (hardware virtualization, separate guest OS kernel) with OS-level Containerization (shared host Linux kernel, namespaces, cgroups).
2. **Docker Architecture:** Master the client-server topology:
   - **Docker Client (`docker` CLI):** Command-line interface communicating over REST API/named pipe.
   - **Docker Daemon (`dockerd`):** Background process managing images, containers, networks, and storage volumes.
   - **Docker Images:** Read-only layered templates defined by a `Dockerfile`.
   - **Docker Containers:** Isolated, lightweight runnable runtime instances of images.
   - **Docker Registry:** Central repository (Docker Hub) for sharing images.
3. **Optimized Dockerfile Authoring:**
   - Multi-stage/minimal slim base image selection (`python:3.11-slim`).
   - Dependency caching layer separation (`COPY requirements.txt` before code).
   - Least-privilege security practice: Creating and switching to a non-root user (`appuser`).
   - Native container health checking via `HEALTHCHECK`.
4. **Lifecycle Commands:** Build, tag, run in detached mode (`-d`), port forwarding (`-p`), log inspection (`logs`), interactive debugging (`exec`), resource stats (`stats`), and clean teardown (`stop`, `rm`).

---

## 3. Docker Architecture & Layered Filesystem

```
+-------------------------------------------------------------------------------+
|                            Docker Engine Host                                 |
|                                                                               |
|  +--------------------+     REST API / Named Pipe     +--------------------+  |
|  |   Docker Client    | ============================> |   Docker Daemon    |  |
|  |   (docker CLI)     |                               |     (dockerd)      |  |
|  +--------------------+                               +--------------------+  |
|                                                                 |             |
|                                   +-----------------------------+             |
|                                   |                             |             |
|                                   v                             v             |
|                        +--------------------+        +---------------------+  |
|                        |   Images (Layers)  |        | Running Containers  |  |
|                        |                    |        |                     |  |
|                        | +----------------+ |        | +-----------------+ |  |
|                        | | App Code Layer | |        | | Read/Write Layer| |  |
|                        | +----------------+ |        | +-----------------+ |  |
|                        | | Py Dependencies| |        | | Flask App:5000  | |  |
|                        | +----------------+ |        | | Non-root User   | |  |
|                        | | python:slim OS | |        | | Health Probe OK | |  |
|                        | +----------------+ |        | +-----------------+ |  |
|                        +--------------------+        +---------------------+  |
+-------------------------------------------------------------------------------+
```

---

## 4. Docker Commands Reference

| Command | Category | Functionality |
| :--- | :--- | :--- |
| `docker build -t <img:tag> .` | Build | Compiles Dockerfile into an immutable layered image. |
| `docker images` | Inspection | Lists local images with tags, Image IDs, and sizes. |
| `docker run -d -p 5000:5000 --name <app> <img:tag>` | Execution | Runs container in detached background mode with port forwarding. |
| `docker ps -a` | Inspection | Lists all active and stopped containers. |
| `docker logs -f <app>` | Observability | Streams standard output and error logs from the container. |
| `docker inspect <app>` | Observability | Displays low-level JSON configuration (IP, network, mounts, health). |
| `docker exec -it <app> bash` | Debugging | Spawns an interactive shell inside a running container. |
| `docker stop <app>` | Teardown | Sends `SIGTERM` followed by `SIGKILL` to gracefully halt the container. |
| `docker rm <app>` | Teardown | Deletes a stopped container instance. |
| `docker rmi <img:tag>` | Teardown | Deletes an image from local storage. |

---

## 5. Execution & Verification Guide

### Step 1: Automated Test Script
Execute the PowerShell script to run unit tests and verify the microservice:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_docker_assignment.ps1
```

### Step 2: Step-by-Step Commands
```powershell
cd assignments/assignment-04-docker-python-app/app

# Run pytest unit tests
python -m pytest test_app.py -v

# Build Docker image
docker build -t devops-python-microservice:v1 .

# Run Docker container
docker run -d --name devops-asg4-app -p 5000:5000 devops-python-microservice:v1

# Test health probe
curl http://localhost:5000/health

# View logs
docker logs devops-asg4-app

# Clean up
docker stop devops-asg4-app
docker rm devops-asg4-app
```

---

## 6. Viva Voce Questions & Answers

**Q1: How do Linux Namespaces and Control Groups (cgroups) enable Docker containers?**  
*Answer:* **Namespaces** provide workspace isolation (PID for process trees, NET for network routing/ports, MNT for filesystem mount points, IPC for shared memory, and UTS for hostnames). **Control Groups (cgroups)** allocate, throttle, and monitor physical hardware resources (CPU shares, memory limits, and disk I/O) allocated to a container.

**Q2: What is the benefit of placing `COPY requirements.txt` before `COPY . .` in a Dockerfile?**  
*Answer:* Docker utilizes an aggressive layer caching mechanism. Installing dependencies takes significantly longer than copying application code. By placing `requirements.txt` and `pip install` earlier, Docker reuses the cached dependency layer on subsequent builds as long as `requirements.txt` hasn't changed, reducing build times from minutes to seconds.

**Q3: Why should containers run as a non-root user?**  
*Answer:* By default, processes in a container run as the `root` user (UID 0). In the event of a container breakout vulnerability, an attacker would inherit root privileges on the underlying host operating system. Creating a dedicated non-root user (`appuser` UID 1001) enforces defense-in-depth security.

**Q4: What is the difference between `CMD` and `ENTRYPOINT` in a Dockerfile?**  
*Answer:* `ENTRYPOINT` defines the permanent executable command that will always run when the container starts. `CMD` provides default arguments or instructions that can easily be overridden by command-line arguments during `docker run`.

---

## 7. Conclusion
The Docker client-server architecture, container isolation primitives, and layered filesystem model were explored. A Python Flask microservice was containerized using an optimized Dockerfile featuring layer caching, non-root user privileges, and automated health checking, verified locally with 100% test pass rates.

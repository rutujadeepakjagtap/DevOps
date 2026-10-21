# DevOps Practical Assignment 05: Multi-Container Application Using Docker Compose

**Student Name:** Rutuja Deepak Jagtap  
**PRN:** `123B1B146` | **Batch:** `C1`  
**Department:** Computer Engineering, PCCOE Pune  
**Academic Year:** 2026–2027  
**Official Curriculum Code:** `BCE27PE01` / `CE-4202`  

---

## 1. Aim
To create, configure, network, and orchestrate a multi-container web application stack using **Docker Compose** by connecting a Python Flask web application with a PostgreSQL database, demonstrating service discovery, port mapping, environment variable injection, named volume storage persistence across container teardown, and container health dependencies.

---

## 2. Learning Objectives
1. **Multi-Container Architecture:** Understand separation of concerns between stateless compute (Flask web tier) and stateful persistence (PostgreSQL database tier).
2. **Declarative Compose Manifests (`docker-compose.yml`):** Author service definitions, build contexts, port mappings, environment variables, and startup dependencies.
3. **Data Persistence with Named Volumes:** Differentiate ephemeral container writable layers from durable host-managed Docker named volumes (`db_data:/var/lib/postgresql/data`).
4. **Service Discovery & Software-Defined Networking:** Leverage user-defined bridge networks (`devops-network`) where containers resolve peers by service name (`db`, `web`) via internal DNS.
5. **Startup Synchronization & Health Checks:** Use `healthcheck` with `depends_on: condition: service_healthy` to prevent premature web server initialization before PostgreSQL is ready to accept socket connections.
6. **Compose Lifecycle Management:** Master commands: `up -d --build`, `ps`, `logs -f`, `exec`, `stop`, `down`, and `down -v`.

---

## 3. Multi-Container Stack Topology

```
+-------------------------------------------------------------------------------+
| User / Web Browser (Host: http://localhost:5000)                              |
+-------------------------------------------------------------------------------+
                                  |
                      Port Forward: 5000:5000
                                  |
                                  v
+-------------------------------------------------------------------------------+
| User-Defined Docker Bridge Network: devops-network                            |
|                                                                               |
|  +-------------------------------------------------------------------------+  |
|  | Web Service Container: devops-asg5-web                                  |  |
|  | - Image: Built from ./app/Dockerfile                                   |  |
|  | - Runtime: Python 3.11-slim + Flask + psycopg2                          |  |
|  | - Environment: POSTGRES_HOST=db, PORT=5000                             |  |
|  | - Healthcheck: curl http://localhost:5000/health                       |  |
|  +-------------------------------------------------------------------------+  |
|                                  |                                            |
|                  Internal TCP: db:5432 (PostgreSQL Protocol)                  |
|                                  |                                            |
|                                  v                                            |
|  +-------------------------------------------------------------------------+  |
|  | Database Service Container: devops-asg5-db                              |  |
|  | - Image: postgres:15-alpine                                             |  |
|  | - Environment: POSTGRES_DB=devopsdb, POSTGRES_USER=devops               |  |
|  | - Schema: init.sql (Creates table `visits` on first startup)           |  |
|  | - Healthcheck: pg_isready -U devops -d devopsdb                         |  |
|  +-------------------------------------------------------------------------+  |
|                                  |                                            |
|                  Storage Mount: /var/lib/postgresql/data                      |
|                                  v                                            |
|  +-------------------------------------------------------------------------+  |
|  | Named Persistent Volume: db_data (Survives container removal)           |  |
|  +-------------------------------------------------------------------------+  |
+-------------------------------------------------------------------------------+
```

---

## 4. Compose Service Configuration Reference

### 4.1 Database Service (`db`)
- **Image:** `postgres:15-alpine` (lightweight, minimal attack surface).
- **Volumes:**
  - `db_data:/var/lib/postgresql/data` (persistent database cluster storage).
  - `./init.sql:/docker-entrypoint-initdb.d/init.sql:ro` (seeds initial tables).
- **Healthcheck:** Uses native PostgreSQL utility `pg_isready` polling every 10 seconds.

### 4.2 Web Service (`web`)
- **Build Context:** `./app` targeting custom Dockerfile.
- **Port Mapping:** Host `5000` &rarr; Container `5000`.
- **Dependency Guard:**
  ```yaml
  depends_on:
    db:
      condition: service_healthy
  ```
  Guarantees web server will NOT boot until the PostgreSQL engine passes health verification.

---

## 5. Execution & Verification Guide

### Step 1: Run Automated Verification Script
Run the automated test and lifecycle verification script:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_docker_compose.ps1
```

### Step 2: Step-by-Step Commands
```powershell
cd assignments/assignment-05-docker-compose-multicontainer

# 1. Validate configuration syntax
docker compose config

# 2. Build and launch services in background
docker compose up -d --build

# 3. Check status of running services
docker compose ps

# 4. View container logs
docker compose logs -f

# 5. Test web application & database connection
curl http://localhost:5000/
curl http://localhost:5000/db

# 6. Stop and remove containers (preserving persistent database volume)
docker compose down

# 7. Complete cleanup (including volumes)
docker compose down -v
```

---

## 6. Viva Voce Questions & Answers

**Q1: What is the difference between Docker Compose and Dockerfile?**  
*Answer:* A `Dockerfile` defines instructions for building a single, immutable container image. `Docker Compose` is a higher-level orchestration tool defined in YAML to configure, run, and link multiple related containers, networks, and persistent storage volumes simultaneously.

**Q2: What happens to PostgreSQL data when `docker compose down` is executed?**  
*Answer:* `docker compose down` halts and removes containers and internal networks, but **preserves named volumes** (such as `db_data`). When `docker compose up -d` is subsequently run, the database container remounts `db_data` without any data loss. To permanently erase the storage volume, the explicit `-v` flag (`docker compose down -v`) must be provided.

**Q3: Why is `depends_on: condition: service_healthy` preferred over simple `depends_on`?**  
*Answer:* Standard `depends_on` only waits until the dependent container is started (process spawned), NOT until the application inside is actually ready to handle client connections. PostgreSQL requires several seconds to initialize database clusters and listen on port 5432. Using `condition: service_healthy` ensures the web application container boots only after `pg_isready` succeeds.

**Q4: How do containers communicate with each other inside a Compose network?**  
*Answer:* Docker creates an embedded DNS server on user-defined bridge networks. When the Flask container queries `db:5432`, the Docker DNS server automatically resolves the service hostname `db` to the private IP address of the database container within the subnet.

---

## 7. Conclusion
Multi-container microservice orchestration was successfully implemented using Docker Compose. A resilient two-tier architecture linking a Python Flask web frontend with a PostgreSQL database was verified with automated healthcheck synchronization and named volume persistence.

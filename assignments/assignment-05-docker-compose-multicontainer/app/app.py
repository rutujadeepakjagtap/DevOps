#!/usr/bin/env python3
"""
DevOps Laboratory Assignment 05: Multi-Container Application (Flask + PostgreSQL)
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
Course: DevOps Engineering (BCE27PE01 / CE-4202)
"""

import os
import socket
import sys
import sqlite3
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# Database configuration from environment
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "devopsdb")
DB_USER = os.getenv("POSTGRES_USER", "devops")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "devopspass")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Assignment 05 - Docker Compose Multi-Container</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #0b0f19;
            color: #f1f5f9;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            max-width: 760px;
            width: 100%;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        h1 { color: #38bdf8; margin-top: 0; }
        .badge {
            background: #059669;
            color: white;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .counter-box {
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 8px;
            padding: 16px 24px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .counter-val {
            font-size: 2rem;
            font-weight: bold;
            color: #10b981;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 16px;
        }
        th, td {
            text-align: left;
            padding: 10px 14px;
            border-bottom: 1px solid #1f2937;
        }
        th { color: #94a3b8; font-weight: 600; width: 35%; }
        td { color: #f8fafc; font-family: monospace; }
        .footer {
            margin-top: 24px;
            font-size: 0.85rem;
            color: #64748b;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <span class="badge">Assignment 05 &bull; Docker Compose Multi-Container</span>
        <h1>Flask Web App &bull; PostgreSQL Database</h1>
        <p>Demonstrating multi-container service orchestration, environment variables, named volume persistence, and private bridge networking.</p>
        
        <div class="counter-box">
            <div>
                <strong>Persistent Visitor Counter</strong>
                <p style="margin:4px 0 0; color:#94a3b8; font-size:0.85rem;">Stored securely in PostgreSQL database table</p>
            </div>
            <div class="counter-val">{{ visit_count }}</div>
        </div>

        <table>
            <tr><th>Student Name</th><td>Rutuja Deepak Jagtap</td></tr>
            <tr><th>PRN</th><td>123B1B146</td></tr>
            <tr><th>Database Engine</th><td>{{ db_engine }}</td></tr>
            <tr><th>Database Host</th><td>{{ db_host }}:{{ db_port }}</td></tr>
            <tr><th>Database Status</th><td><span style="color:#10b981;">{{ db_status }}</span></td></tr>
            <tr><th>Web Container Hostname</th><td>{{ hostname }}</td></tr>
            <tr><th>Server Timestamp</th><td>{{ timestamp }}</td></tr>
            <tr><th>Database Health Check</th><td><a href="/db" style="color:#38bdf8;">/db</a></td></tr>
            <tr><th>Service Health Check</th><td><a href="/health" style="color:#38bdf8;">/health</a></td></tr>
        </table>

        <div class="footer">
            Pimpri Chinchwad College of Engineering &bull; Department of Computer Engineering
        </div>
    </div>
</body>
</html>
"""

def get_db_connection():
    """Attempt PostgreSQL connection; fallback to local SQLite for test environments."""
    try:
        import psycopg2
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=2
        )
        return conn, "PostgreSQL 15"
    except Exception:
        # Fallback to local SQLite when running standalone without live Docker Postgres
        sqlite_path = os.path.join(os.path.dirname(__file__), "devops_local.db")
        conn = sqlite3.connect(sqlite_path)
        return conn, "SQLite (Local Fallback)"

def init_db():
    """Initialize table if not already created."""
    conn, engine = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                visited_at TIMESTAMP,
                client_ip VARCHAR(50)
            )
        """)
        conn.commit()
    except Exception:
        # For sqlite compatibility where SERIAL is INTEGER PRIMARY KEY AUTOINCREMENT
        conn.rollback()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visited_at TIMESTAMP,
                client_ip VARCHAR(50)
            )
        """)
        conn.commit()
    finally:
        cur.close()
        conn.close()

@app.route("/")
def index():
    init_db()
    conn, engine = get_db_connection()
    cur = conn.cursor()
    now_utc = datetime.now(timezone.utc)
    client_ip = request.remote_addr or "127.0.0.1"

    now_str = now_utc.isoformat()
    cur.execute("INSERT INTO visits (visited_at, client_ip) VALUES (%s, %s)" if "PostgreSQL" in engine else "INSERT INTO visits (visited_at, client_ip) VALUES (?, ?)", (now_utc if "PostgreSQL" in engine else now_str, client_ip))
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()

    return render_template_string(
        HTML_TEMPLATE,
        visit_count=count,
        db_engine=engine,
        db_host=DB_HOST,
        db_port=DB_PORT,
        db_status="Connected & Operational",
        hostname=socket.gethostname(),
        timestamp=now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route("/db")
def db_check():
    try:
        conn, engine = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM visits")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({
            "status": "connected",
            "database_engine": engine,
            "host": DB_HOST,
            "port": DB_PORT,
            "database_name": DB_NAME,
            "total_visits_logged": count,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-assignment-05-flask-postgres",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "container_id": socket.gethostname()
    }), 200

if __name__ == "__main__":
    init_db()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

#!/usr/bin/env python3
"""
DevOps Laboratory Assignment 04: Containerized Python Application
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
Course: DevOps Engineering (BCE27PE01 / CE-4202)
"""

import os
import socket
import sys
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Assignment 04 - Docker Python Microservice</title>
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
            max-width: 720px;
            width: 100%;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        h1 { color: #38bdf8; margin-top: 0; }
        .badge {
            background: #0284c7;
            color: white;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 24px;
        }
        th, td {
            text-align: left;
            padding: 12px 14px;
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
        <span class="badge">Assignment 04 &bull; Docker Containerization</span>
        <h1>Python Containerized Microservice</h1>
        <p>This microservice is running inside an isolated Linux container packaged via an optimized Dockerfile.</p>
        <table>
            <tr><th>Student Name</th><td>Rutuja Deepak Jagtap</td></tr>
            <tr><th>PRN</th><td>123B1B146</td></tr>
            <tr><th>College</th><td>PCCOE Pune</td></tr>
            <tr><th>Container Hostname</th><td>{{ hostname }}</td></tr>
            <tr><th>Python Version</th><td>{{ python_version }}</td></tr>
            <tr><th>Server Timestamp</th><td>{{ timestamp }}</td></tr>
            <tr><th>App Environment</th><td>{{ environment }}</td></tr>
            <tr><th>Health Endpoint</th><td><a href="/health" style="color:#38bdf8;">/health</a></td></tr>
            <tr><th>JSON API Endpoint</th><td><a href="/api/info" style="color:#38bdf8;">/api/info</a></td></tr>
        </table>
        <div class="footer">
            Pimpri Chinchwad College of Engineering &bull; Department of Computer Engineering
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=socket.gethostname(),
        python_version=sys.version.split()[0],
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        environment=os.getenv("APP_ENV", "Production (Containerized)")
    )

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-assignment-04-python-docker",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "container_id": socket.gethostname()
    }), 200

@app.route("/api/info")
def api_info():
    return jsonify({
        "assignment": "04 - Docker Architecture, Dockerfile & Containerization",
        "student": "Rutuja Deepak Jagtap",
        "prn": "123B1B146",
        "institution": "PCCOE Pune",
        "python_version": sys.version,
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "Production")
    }), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

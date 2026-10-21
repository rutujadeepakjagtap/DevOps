# Dockerfile for Flask Web Service
# DevOps Assignment 05: Multi-Container Docker Compose
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

FROM python:3.11-slim

WORKDIR /app

# Install system build dependencies for psycopg2 if compiling
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

HEALTHCHECK --interval=20s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]

# Production Multi-Stage / Lightweight Dockerfile for Python Flask Application
# DevOps Laboratory Assignment 04
# Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

FROM python:3.11-slim

# Set environment variables for Python optimization
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000 \
    APP_ENV="Production (Docker Container)"

# Set working directory
WORKDIR /app

# Install dependencies separately to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Create a non-privileged system user for container security
RUN useradd -u 1001 -m appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose internal listening port
EXPOSE 5000

# Container healthcheck for orchestrators / Docker daemon
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; sys.exit(0 if urllib.request.urlopen('http://localhost:5000/health').getcode() == 200 else 1)" || exit 1

# Start Flask application
CMD ["python", "app.py"]

# ---- Base image ----
FROM python:3.11-slim

# ---- Set environment variables ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_VERSION=v2

# ---- Create non-root user ----
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# ---- Set work directory ----
WORKDIR /app

# ---- Install dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY app.py .

# ---- Change ownership ----
RUN chown -R appuser:appgroup /app

# ---- Switch to non-root user ----
USER appuser

# ---- Expose port ----
EXPOSE 5000

# ---- Health check ----
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

# ---- Run application ----
CMD ["python", "app.py"]

# 🚀 Self-Healing DevOps Platform

A **production-grade DevOps project** demonstrating **CI/CD, GitOps, Kubernetes self-healing, auto-scaling, observability, and alerting** using modern DevOps and SRE best practices.

This project is built to **stand out in DevOps interviews** and reflects **real-world production workflows**, not tutorials.

---

## 📌 Overview

The **Self-Healing DevOps Platform** automates the entire application lifecycle:

- Code → Build → Deploy → Scale → Monitor → Alert
- Fully automated with **zero manual deployment**
- Designed with **GitOps and SRE principles**

---

## ✨ Key Features

### 🔄 CI/CD Automation
- GitHub Actions for Continuous Integration
- Automated Docker image build and push
- Secure secret handling using GitHub Secrets

### 🔁 GitOps-Based Deployment
- Argo CD for Continuous Delivery
- Separate GitOps repository for Kubernetes manifests
- Auto-sync, prune, and self-heal enabled
- Declarative and auditable deployments

### ♻️ Kubernetes Self-Healing
- Automatic pod recovery on failure
- Liveness and readiness probes
- Zero-downtime restarts

### 📈 Horizontal Pod Auto-Scaling (HPA)
- CPU-based auto-scaling
- Automatically scales under load
- No manual intervention

### 📊 Observability (SRE)
- **Prometheus** for metrics
- **Grafana** for dashboards
- **Loki** for centralized logging

### 🔔 Alerting
- Pod crash loop detection
- High CPU usage alerts
- Deployment availability monitoring
- Managed via Prometheus + Alertmanager

---

## 🏗️ Architecture
Developer
|
v
GitHub (App Repo)
|
v
GitHub Actions (CI)
|
v
Docker Hub
|
v
GitHub (GitOps Repo)
|
v
Argo CD (CD)
|
v
Kubernetes Cluster
├── Self-Healing
├── Auto-Scaling
├── Monitoring
└── Alerting


---

## 🛠️ Technology Stack

| Category | Tools |
|-------|------|
| CI | GitHub Actions |
| CD | Argo CD (GitOps) |
| Containers | Docker |
| Orchestration | Kubernetes |
| Auto Scaling | HPA |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| Logging | Loki |
| Alerting | Alertmanager |
| Local Cluster | Minikube |

---

## 📂 Repository Structure

### Application Repository (`self-healing-app`)

self-healing-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── .github/workflows/
│ └── ci.yml
└── README.md

---

### GitOps Repository (`self-healing-gitops`)

self-healing-gitops/
└── k8s/
├── deployment.yaml
└── service.yaml


---

## 🔄 CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Actions builds Docker image
3. Image is pushed to Docker Hub
4. Kubernetes manifests are tracked in GitOps repo
5. Argo CD auto-syncs cluster state
6. Application is deployed automatically

---

## ♻️ Self-Healing Demo

```bash
kubectl delete pod -l app=self-healing-app


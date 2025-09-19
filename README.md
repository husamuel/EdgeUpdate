# EdgeUpdate – Simulated IoT DevOps Lab
<img width="1190" height="611" alt="image" src="https://github.com/user-attachments/assets/153ddbb7-861f-4aa8-a29b-cf52965930ae" />

## Table of Contents
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)

---

## About The Project

EdgeUpdate is a **simulated IoT environment** using Docker containers to emulate devices managed by a Flask backend. The system supports **Over-The-Air (OTA) updates**, exposes **Prometheus metrics**, and integrates with a **CI/CD pipeline** including **vulnerability scans** (Trivy) and **SBOM generation** (Syft).

The project is designed to demonstrate **DevOps skills**, including containerization, monitoring, security, and automation, in a realistic IoT scenario. It's still in its initial phase, but the project is evolving as new features are added.

---

## Built With

- **Python** – Backend and device simulation  
- **Flask** – REST API for device control  
- **Docker** – Containerized devices  
- **Docker Compose** – Orchestration of multiple containers  
- **Prometheus** – Metrics collection  
- **Grafana** – Metrics visualization  
- **GitHub Actions** – CI/CD automation and **artifact storage**  
- **Trivy** – Vulnerability scanning  
- **Syft** – SBOM generation  

---
## Getting Started

### Prerequisites

- Docker  
- Docker Compose  
- Python 3.11+  
- Git  

### Installation

1. Clone the repository:  
   `git clone https://github.com/your_username/EdgeUpdate.git`  
2. Navigate to the project folder:  
   `cd EdgeUpdate`  
3. Build the Docker containers:  
   `docker-compose build`  
4. Run the containers in detached mode:  
   `docker-compose up -d`  

---

## Usage

1. Check backend API status:  
   `curl http://localhost:5000/status`  
2. Trigger OTA update for a device:  
   `curl -X POST http://localhost:5000/update -H "Content-Type: application/json" -d '{"version": "1.1.0"}'`  
3. Access Prometheus metrics via browser:  
   `http://localhost:9090`  
4. Access Grafana dashboard via browser:  
   `http://localhost:3000`  

> The CI/CD pipeline automatically builds, tests, scans for vulnerabilities, generates SBOMs, and uploads **artifacts** on each push to the main branch.

---

## Roadmap

### ✅ Phase 1 – Device Simulation
- Simular dispositivos IoT com **containers Docker** que representam câmeras e sensores  
- Cada container roda um script Python que gera vídeos ou snapshots  
- Backend central recebe dados e armazena, expondo **API e métricas**  

### ⏳ Phase 2 – Centralized Video Processing
- Containers enviam vídeos para o backend  
- Backend processa vídeos e envia para **AWS Rekognition** para análise  
- Backend gera alertas com base nos resultados da análise  

### ⚡ Phase 3 – Real Devices
- Substituir containers simulados por **câmeras reais**  
- Backend recebe vídeos ou snapshots das câmeras físicas  
- Backend processa e gera alertas, integrando métricas e logs


---

## Acknowledgments

- [Docker Documentation](https://docs.docker.com/)  
- [Flask Documentation](https://flask.palletsprojects.com/)  
- [Prometheus Docs](https://prometheus.io/docs/)  
- [Grafana Docs](https://grafana.com/docs/)  
- [Trivy](https://aquasecurity.github.io/trivy/)  
- [Syft](https://github.com/anchore/syft)  
- [GitHub Actions](https://github.com/features/actions)


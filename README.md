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

To run this project locally, you will need:  

- **Docker** & **Docker Compose** installed  
- **Python 3.11+**  
- **Git**  

### Installation

1. Clone the repository and navigate to the project folder.  
2. Build and run the simulated IoT devices using Docker Compose.  
3. The backend API will start and be ready to manage devices and expose metrics.  

Once running, the system allows you to check device status, trigger OTA updates, and monitor metrics via Prometheus and Grafana. The CI/CD pipeline automatically handles building, testing, scanning, generating SBOMs, and storing artifacts on each push to the main branch.

---

## Usage

- Check device status via the backend API.  
- Trigger OTA updates for simulated devices.  
- View Prometheus metrics on Grafana dashboards.  
- CI/CD pipeline automatically builds, tests, scans for vulnerabilities, generates SBOMs, and uploads **artifacts** on each push to the main branch.  

---

## Roadmap

- Integrate real cameras and edge AI processing  
- Add automatic alerts for unauthorized activity  
- Migrate to Kubernetes for scalable device orchestration  
- Integrate AWS S3 and Rekognition for image analysis  

---

## Acknowledgments

- Docker Documentation  
- Flask Documentation  
- Prometheus Docs  
- Grafana Docs  
- Trivy  
- Syft  

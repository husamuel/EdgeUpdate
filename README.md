# EdgeUpdate – Simulated IoT DevOps Lab

Table of Contents
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

EdgeUpdate is a **simulated IoT environment** using Docker containers to emulate devices managed by a Flask backend. The system supports **Over-The-Air (OTA) updates**, exposes **Prometheus metrics**, and integrates with a **CI/CD pipeline** including vulnerability scans (Trivy) and SBOM generation (Syft).  

The project is designed to demonstrate **DevOps skills**, including containerization, monitoring, security, and automation, in a realistic IoT scenario.

---

## Built With

- [Python](https://www.python.org/) – Backend and device simulation
- [Flask](https://flask.palletsprojects.com/) – REST API for device control
- [Docker](https://www.docker.com/) – Containerized devices
- [Docker Compose](https://docs.docker.com/compose/) – Orchestration of multiple containers
- [Prometheus](https://prometheus.io/) – Metrics collection
- [Grafana](https://grafana.com/) – Metrics visualization
- [GitHub Actions](https://github.com/features/actions) – CI/CD automation and artifact storage
- [Trivy](https://aquasecurity.github.io/trivy/) – Vulnerability scanning
- [Syft](https://github.com/anchore/syft) – SBOM generation

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Git

### Installation

1. Clone the repository:
git clone https://github.com/your_username/EdgeUpdate.git
cd EdgeUpdate

2. Build and run the containers:
docker-compose up -d --build

Usage

Check device status:
curl http://localhost:5000/status


Trigger OTA update:
curl -X POST http://localhost:5000/update -H "Content-Type: application/json" -d '{"version": "1.1.0"}'

View Prometheus metrics by Grafana:
http://localhost:3000

CI/CD pipeline automatically builds, tests, scans for vulnerabilities, generates SBOMs, and uploads artifacts on each push to main.


Roadmap

Integrate real cameras and edge AI processing

Add automatic alerts for unauthorized activity

Migrate to Kubernetes for scalable device orchestration

Integrate AWS S3 and Rekognition for image analysis


Acknowledgments

Docker Documentation

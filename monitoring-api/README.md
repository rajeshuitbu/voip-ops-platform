# VoIP Ops Platform - Monitoring API

## Overview

The Monitoring API is the first module of the **VoIP Ops Platform**. It provides REST APIs to monitor the health and runtime status of a Kamailio SIP Server.

The project is designed for VoIP Operations, NOC teams, Support Engineers, and Telecom DevOps engineers who need a simple API to monitor SIP infrastructure.

---

## Features

- Monitor Kamailio service status
- Retrieve Kamailio version
- Get process details
- Monitor CPU utilization
- Monitor Memory utilization
- Retrieve Process ID (PID)
- Monitor Thread Count
- Display Hostname
- Display Operating System information
- Display System Timestamp
- REST APIs built using FastAPI
- JSON-based API responses

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend Programming |
| FastAPI | REST API Framework |
| Kamailio | SIP Server |
| Linux (Ubuntu) | Operating System |
| systemctl | Service Management |
| psutil | Process Monitoring |
| Uvicorn | ASGI Server |

---

## Project Structure

```
monitoring-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   └── service.py
│
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Root

```
GET /
```

Response

```json
{
    "application": "VoIP Ops Platform",
    "status": "running"
}
```

---

### Health Check

```
GET /health
```

Response

```json
{
    "status": "healthy"
}
```

---

### Kamailio Status

```
GET /kamailio/status
```

Example Response

```json
{
    "service": "kamailio",
    "status": "active"
}
```

---

### Kamailio Version

```
GET /kamailio/version
```

Example Response

```json
{
    "service": "kamailio",
    "version": "version: kamailio 6.0.5"
}
```

---

### Kamailio Details

```
GET /kamailio/details
```

Example Response

```json
{
    "service": "kamailio",
    "status": "active",
    "version": "version: kamailio 6.0.5",
    "pid": 4234,
    "cpu_percent": 0.2,
    "memory_mb": 24.5,
    "threads": 41,
    "hostname": "ip-172-31-13-152",
    "operating_system": "Ubuntu 24.04",
    "timestamp": "2026-07-05 18:15:21"
}
```

---

## Running the Project

Clone the repository

```bash
git clone https://github.com/rajeshuitbu/voip-ops-platform.git
```

Go to the project directory

```bash
cd monitoring-api
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://localhost:8000/docs
```

---

## Sample Architecture

```
                REST Client
                     │
                     ▼
                FastAPI API
                     │
                     ▼
                service.py
                     │
      ┌──────────────┴──────────────┐
      ▼                             ▼
 systemctl                     psutil
      │                             │
      └──────────────┬──────────────┘
                     ▼
                 Kamailio
```

---

## Future Enhancements

- Self-Healing Engine
- SIP OPTIONS Monitoring
- Log Analyzer
- Dashboard
- Alerting
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- Prometheus Metrics
- Grafana Dashboard

---

## Author

**Rajesh Kumar**

VoIP | Telecom | SIP | Kamailio | Python | FastAPI | AWS

GitHub:
https://github.com/rajeshuitbu

---

## License

This project is released under the MIT License.

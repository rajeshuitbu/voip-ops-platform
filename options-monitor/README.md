# VoIP OPTIONS Monitor

A carrier-grade SIP OPTIONS monitoring service built using **Python** and **FastAPI** to continuously monitor the health and availability of SIP servers such as **Kamailio**, **OpenSIPS**, and SIP SBCs.

---

# Project Overview

The OPTIONS Monitor periodically sends SIP OPTIONS requests to a SIP server and measures its availability, response time, and health status.

This project simulates the functionality commonly used by telecom operators and enterprise VoIP platforms to monitor SIP infrastructure.

---

# Features

- Real SIP OPTIONS request using UDP sockets
- Kamailio health monitoring
- SIP response code detection
- Response time measurement
- Latency classification
- Health status calculation
- Statistics engine
- Availability calculation
- REST APIs
- JSON responses

---

# Project Structure

```
options-monitor/

│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── service.py
│   ├── monitor.py
│   ├── health.py
│   ├── stats.py
│   ├── logger.py
│   └── watchdog.py
│
├── logs/
│
├── README.md
├── requirements.txt
└── venv/
```

---

# Architecture

```
                OPTIONS Monitor

                      │

                      ▼

          Build SIP OPTIONS Request

                      │

                      ▼

         UDP Socket Communication

                      │

                      ▼

             Kamailio SIP Server

                      │

          SIP/2.0 200 Keepalive

                      │

                      ▼

           Measure Response Time

                      │

                      ▼

          Health Classification

                      │

                      ▼

         Statistics Collection

                      │

                      ▼

             REST API Response
```

---

# REST APIs

## Application Status

```
GET /
```

Response

```json
{
    "application":"VoIP OPTIONS Monitor",
    "status":"running"
}
```

---

## Health Check

```
GET /health
```

Response

```json
{
    "status":"healthy"
}
```

---

## Check SIP Server

```
GET /options/status
```

Example

```bash
curl http://localhost:8003/options/status
```

Example Response

```json
{
    "server":"kamailio",
    "ip":"127.0.0.1",
    "port":5060,
    "method":"OPTIONS",
    "response_code":200,
    "status":"UP",
    "response_time_ms":0.58,
    "latency_status":"Excellent",
    "health":"Healthy",
    "recommendation":"No action required."
}
```

---

## Trigger Manual OPTIONS Check

```
POST /options/check
```

---

## Statistics

```
GET /options/statistics
```

Example

```json
{
    "total_checks":10,
    "successful_checks":10,
    "failed_checks":0,
    "consecutive_failures":0,
    "average_latency_ms":0.61,
    "minimum_latency_ms":0.52,
    "maximum_latency_ms":0.82,
    "availability_percent":100.0
}
```

---

# Health Classification

| Latency | Status |
|----------|---------|
| < 5 ms | Excellent |
| 5–20 ms | Good |
| 20–50 ms | Warning |
| > 50 ms | Critical |

---

# Technology Stack

- Python 3
- FastAPI
- Linux
- UDP Socket Programming
- SIP Protocol
- Kamailio
- REST API
- JSON

---

# Tested Environment

- Ubuntu Linux
- Python 3.14
- FastAPI
- Uvicorn
- Kamailio 6.x

---

# Current Capabilities

- SIP OPTIONS Monitoring
- Response Time Measurement
- SIP Response Code Parsing
- Health Evaluation
- Statistics Collection
- Availability Calculation

---

# Planned Enhancements

- Automatic background monitoring
- Email / Slack alerts
- Historical latency graphs
- Self-Healing integration
- Dashboard integration
- Prometheus metrics
- Grafana dashboards
- Docker deployment
- Kubernetes deployment

---

# Sample Workflow

```
OPTIONS Request

      │

      ▼

Kamailio

      │

      ▼

200 Keepalive

      │

      ▼

Measure Latency

      │

      ▼

Health Classification

      │

      ▼

Statistics Update

      │

      ▼

REST API Response
```

---

# Author

Rajesh Kumar

Senior VoIP / Telecom Engineer

Python • SIP • Kamailio • FastAPI • Linux • VoIP Monitoring • Telecom Automation

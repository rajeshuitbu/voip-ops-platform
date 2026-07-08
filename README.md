
![Python](https://img.shields.io/badge/Python-3.14-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)

![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)

![VoIP](https://img.shields.io/badge/VoIP-SIP-red)


# VoIP Operations Automation Platform

An end-to-end VoIP Operations Platform built using Python and FastAPI for monitoring, troubleshooting and self-healing of SIP infrastructure.

---

## Project Overview

This repository demonstrates practical telecom automation using Python.

It includes:

- SIP Monitoring
- Automated Self-Healing
- SIP Log Analysis
- REST APIs
- Linux Automation

---

## Components

### Monitoring API

Monitors Kamailio SIP server.

Features

- Health API
- Status API
- Version API
- PID Information

---

### Self-Healing Engine

Automatically recovers failed SIP services.

Features

- Watchdog
- Auto Restart
- Retry Logic
- Logging

---

### SIP Log Analyzer

Parses SIP traces.

Features

- Call Flow Reconstruction
- SIP Method Parsing
- Response Analysis
- Root Cause Detection

---

## Architecture

```text
                    VoIP Ops Platform

                    +------------------+
                    | Monitoring API   |
                    +---------+--------+
                              |
                              |
                    +---------v--------+
                    | Self-Healing API |
                    +---------+--------+
                              |
                     Restart Kamailio
                              |
                    +---------v--------+
                    | Kamailio Server  |
                    +---------+--------+
                              |
                              |
                    +---------v--------+
                    | SIP Log Analyzer |
                    +---------+--------+
                              |
                              |
                    JSON Reports
```

---

## Technology Stack

- Python
- FastAPI
- Linux
- SIP
- Kamailio
- REST API
- Uvicorn
- Systemd
- JSON

---

## Future Roadmap

- OPTIONS Monitor
- Dashboard
- Docker
- Kubernetes
- Prometheus
- Grafana
- ELK Stack

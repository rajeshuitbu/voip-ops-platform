# VoIP Self-Healing Engine

An automated self-healing service for VoIP infrastructure that continuously monitors the Kamailio SIP server and automatically restarts the service if it becomes unavailable.

---

## Features

- REST API built using FastAPI
- Manual Kamailio restart endpoint
- Continuous health monitoring
- Automatic recovery using watchdog
- Retry mechanism before restart
- Logging of all monitoring activities
- Timestamped restart information

---

## Project Structure

```
self-healing/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── service.py
│   ├── watchdog.py
│   ├── logger.py
│   └── __init__.py
│
├── run_watchdog.py
├── healing.log
├── requirements.txt
└── README.md
```

---

## Architecture

```
                +----------------------+
                | FastAPI REST API     |
                +----------+-----------+
                           |
                           |
          +----------------v----------------+
          | Manual Restart API              |
          +----------------+----------------+
                           |
                           |
                     systemctl restart
                           |
                           v
                  +------------------+
                  | Kamailio SIP     |
                  +------------------+

------------------------------------------------

            Background Watchdog Process

        Every 30 Seconds
                |
                v
        Check Kamailio Status
                |
        +-------+--------+
        |                |
      Active           Down
        |                |
        |          Retry 3 Times
        |                |
        |         Still Down?
        |                |
        +------No--------+
                |
               Yes
                |
        Restart Kamailio
                |
        Write Recovery Log
```

---

## REST APIs

### Application Status

```
GET /
```

Response

```json
{
    "application": "VoIP Self-Healing Engine",
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

### Restart Kamailio

```
POST /kamailio/restart
```

Example

```bash
curl -X POST http://localhost:8001/kamailio/restart
```

Response

```json
{
    "service":"kamailio",
    "action":"restart",
    "status":"active",
    "timestamp":"2026-07-05 15:01:18"
}
```

---

## Watchdog

Start monitoring

```bash
python run_watchdog.py
```

The watchdog checks Kamailio every 30 seconds.

If Kamailio is unavailable

- Retry three times
- Restart Kamailio
- Log the recovery activity

---

## Log Output

Example

```
2026-07-05 16:50:13 INFO Watchdog Started
2026-07-05 16:50:13 INFO Kamailio is healthy
2026-07-05 16:50:43 INFO Kamailio is healthy
2026-07-05 16:51:13 INFO Kamailio is healthy
```

---

## Technology Stack

- Python 3.14
- FastAPI
- Uvicorn
- Linux Systemd
- Kamailio SIP Server
- Logging
- Subprocess
- REST API

---

## Future Enhancements

- Restart Counter
- Recovery Statistics
- Email Notifications
- Slack Notifications
- Prometheus Metrics
- Grafana Dashboard
- Docker Support
- Kubernetes Deployment
- Multi-service Monitoring

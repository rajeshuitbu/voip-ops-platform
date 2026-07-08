# SIP Log Analyzer

A carrier-grade SIP Log Analyzer built using **Python** and **FastAPI** for analyzing SIP call traces. The application parses SIP logs, reconstructs call flows, classifies SIP responses, and provides troubleshooting recommendations.

---

# Overview

SIP Log Analyzer helps VoIP engineers quickly troubleshoot SIP signaling issues by parsing SIP messages and grouping them by **Call-ID**.

The analyzer supports:

- SIP Method Detection
- SIP Response Analysis
- Call Flow Reconstruction
- Call Classification
- Root Cause Analysis
- Troubleshooting Recommendations

---

# Features

- Parse SIP log files
- Extract SIP Methods
  - INVITE
  - REGISTER
  - ACK
  - BYE
  - OPTIONS
  - CANCEL
- Extract SIP Headers
  - Call-ID
  - From
  - To
  - CSeq
  - User-Agent
- Detect SIP Response Codes
  - 100 Trying
  - 180 Ringing
  - 183 Session Progress
  - 200 OK
  - 401 Unauthorized
  - 403 Forbidden
  - 404 Not Found
  - 408 Request Timeout
  - 480 Temporarily Unavailable
  - 486 Busy Here
  - 487 Request Terminated
  - 500 Internal Server Error
  - 503 Service Unavailable
- Reconstruct complete SIP Call Flow
- Call Success / Failure Classification
- Intelligent Troubleshooting Recommendation
- REST API Interface

---

# Project Structure

```
sip-log-analyzer/

│
├── app/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── diagnosis.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   ├── routes.py
│   └── service.py
│
├── logs/
│   └── sample_sip.log
│
├── README.md
├── requirements.txt
└── venv/
```

---

# Architecture

```
                 SIP Log File
                       │
                       ▼
               Read SIP Messages
                       │
                       ▼
               Parse SIP Headers
                       │
                       ▼
               Group by Call-ID
                       │
                       ▼
           Reconstruct Call Flow
                       │
                       ▼
           Analyze SIP Response Codes
                       │
                       ▼
          Diagnose Call Failure Cause
                       │
                       ▼
             Generate JSON Report
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
    "application":"VoIP SIP Log Analyzer",
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

## Analyze SIP Log

```
GET /analyze
```

Example

```bash
curl http://localhost:8002/analyze
```

Example Response

```json
{
    "total_calls": 2,
    "calls": [
        {
            "call_id": "call001@test",
            "from": "<sip:1000@test.com>",
            "to": "<sip:1001@test.com>",
            "user_agent": "Zoiper",
            "call_flow": [
                "INVITE",
                "100",
                "180",
                "200",
                "ACK",
                "BYE"
            ],
            "result": "Successful Call",
            "diagnosis": {
                "status": "Successful",
                "root_cause": "Call established successfully.",
                "recommendation": "No action required.",
                "severity": "Info"
            }
        }
    ]
}
```

---

# Supported SIP Methods

| Method | Description |
|----------|-------------|
| INVITE | Establish a SIP session |
| REGISTER | Register endpoint |
| ACK | Acknowledge final response |
| BYE | Terminate call |
| CANCEL | Cancel pending INVITE |
| OPTIONS | Capability query |

---

# Supported SIP Response Codes

| Code | Meaning |
|------|---------|
|100|Trying|
|180|Ringing|
|183|Session Progress|
|200|OK|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|408|Request Timeout|
|480|Temporarily Unavailable|
|486|Busy Here|
|487|Request Terminated|
|500|Internal Server Error|
|503|Service Unavailable|

---

# Technology Stack

- Python 3
- FastAPI
- Uvicorn
- REST APIs
- SIP Protocol
- VoIP Signaling
- JSON
- Linux

---

# Use Cases

- SIP Call Troubleshooting
- VoIP Network Analysis
- SIP Trace Validation
- Call Flow Reconstruction
- Root Cause Analysis
- Telecom Support Automation
- Carrier VoIP Operations
- SIP Debugging

---

# Future Enhancements

- Upload SIP Log File using REST API
- Parse PCAP Files
- SIP Ladder Diagram Generation
- RTP Statistics
- MOS Score Estimation
- Multiple Concurrent Call Analysis
- Dashboard Integration
- Elasticsearch Integration
- Prometheus Metrics
- Grafana Visualization

---

# Sample Workflow

```
SIP Log
    │
    ▼
Read File
    │
    ▼
Parse SIP Messages
    │
    ▼
Extract Headers
    │
    ▼
Group by Call-ID
    │
    ▼
Analyze Responses
    │
    ▼
Identify Failure Cause
    │
    ▼
Generate JSON Report
```

---

# Author

Rajesh Kumar

Senior VoIP / Telecom Engineer

Python • SIP • Kamailio • OpenSIPS • Asterisk • FastAPI • Linux • VoIP Automation

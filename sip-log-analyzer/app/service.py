from app.parser import parse_sip_log
from app.analyzer import classify_call
from app.diagnosis import diagnose_call


def analyze_log():

    logfile = "logs/sample_sip.log"

    calls = parse_sip_log(logfile)

    report = []

    for call_id, data in calls.items():

        flow = data["call_flow"]

        report.append({

            "call_id": call_id,

            "from": data["headers"].get("from"),

            "to": data["headers"].get("to"),

            "user_agent": data["headers"].get("user_agent"),

            "call_flow": flow,

            "result": classify_call(flow),

            "diagnosis": diagnose_call(flow)

        })

    return {

        "total_calls": len(report),

        "calls": report

    }

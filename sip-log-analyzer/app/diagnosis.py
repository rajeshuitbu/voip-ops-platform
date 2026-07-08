def diagnose_call(call_flow):

    diagnosis = {
        "status": "Unknown",
        "root_cause": "",
        "recommendation": "",
        "severity": "Low"
    }

    if "200" in call_flow:

        diagnosis["status"] = "Successful"

        diagnosis["root_cause"] = "Call established successfully."

        diagnosis["recommendation"] = "No action required."

        diagnosis["severity"] = "Info"

    elif "486" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Destination user is busy."

        diagnosis["recommendation"] = "Retry the call later."

        diagnosis["severity"] = "Low"

    elif "480" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Destination temporarily unavailable."

        diagnosis["recommendation"] = "Verify registration and endpoint connectivity."

        diagnosis["severity"] = "Medium"

    elif "408" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Request timeout."

        diagnosis["recommendation"] = "Check network latency, firewall and SBC."

        diagnosis["severity"] = "High"

    elif "401" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Authentication challenge."

        diagnosis["recommendation"] = "Verify SIP username and password."

        diagnosis["severity"] = "Medium"

    elif "403" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Authentication rejected."

        diagnosis["recommendation"] = "Check authentication policy."

        diagnosis["severity"] = "High"

    elif "404" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Destination user not found."

        diagnosis["recommendation"] = "Verify dial plan and SIP routing."

        diagnosis["severity"] = "Medium"

    elif "487" in call_flow:

        diagnosis["status"] = "Cancelled"

        diagnosis["root_cause"] = "Call cancelled before answer."

        diagnosis["recommendation"] = "Verify CANCEL message source."

        diagnosis["severity"] = "Low"

    elif "500" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Internal SIP server error."

        diagnosis["recommendation"] = "Check Kamailio/OpenSIPS logs."

        diagnosis["severity"] = "Critical"

    elif "503" in call_flow:

        diagnosis["status"] = "Failed"

        diagnosis["root_cause"] = "Service unavailable."

        diagnosis["recommendation"] = "Verify SIP server availability."

        diagnosis["severity"] = "Critical"

    return diagnosis

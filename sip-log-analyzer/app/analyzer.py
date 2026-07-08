def classify_call(call_flow):

    if "200" in call_flow:
        return "Successful Call"

    if "486" in call_flow:
        return "Busy"

    if "480" in call_flow:
        return "User Unavailable"

    if "408" in call_flow:
        return "Timeout"

    if "401" in call_flow:
        return "Authentication Required"

    if "403" in call_flow:
        return "Forbidden"

    if "404" in call_flow:
        return "Not Found"

    if "487" in call_flow:
        return "Cancelled"

    if "500" in call_flow:
        return "Server Error"

    if "503" in call_flow:
        return "Service Unavailable"

    return "Unknown"

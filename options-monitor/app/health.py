def classify_latency(latency):

    if latency is None:
        return "Unavailable"

    if latency < 5:
        return "Excellent"

    elif latency < 20:
        return "Good"

    elif latency < 50:
        return "Warning"

    return "Critical"


def overall_health(status, latency):

    if status != "UP":
        return "Critical"

    if latency < 5:
        return "Healthy"

    elif latency < 20:
        return "Healthy"

    elif latency < 50:
        return "Warning"

    return "Critical"

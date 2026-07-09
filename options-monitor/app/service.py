from app.monitor import send_options
from app.health import classify_latency, overall_health
from app.stats import update_statistics


def check_options():

    data = send_options()

    latency = data.get("response_time_ms")

    # Add latency classification
    data["latency_status"] = classify_latency(latency)

    # Calculate overall health
    data["health"] = overall_health(
        data["status"],
        latency
    )

    # Recommendation
    if data["health"] == "Healthy":

        data["recommendation"] = "No action required."

    elif data["health"] == "Warning":

        data["recommendation"] = "Monitor response latency."

    else:

        data["recommendation"] = (
            "Investigate SIP server or trigger Self-Healing."
        )

    # Update statistics
    update_statistics(data)

    return data

from datetime import datetime

stats = {

    "total_checks": 0,

    "successful_checks": 0,

    "failed_checks": 0,

    "consecutive_failures": 0,

    "average_latency_ms": 0,

    "minimum_latency_ms": None,

    "maximum_latency_ms": 0,

    "last_success": None,

    "latency_history": []
}


def update_statistics(result):

    stats["total_checks"] += 1

    latency = result.get("response_time_ms")

    if result["status"] == "UP":

        stats["successful_checks"] += 1

        stats["consecutive_failures"] = 0

        stats["last_success"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if latency is not None:

            stats["latency_history"].append(latency)

            if len(stats["latency_history"]) > 100:

                stats["latency_history"].pop(0)

            stats["average_latency_ms"] = round(

                sum(stats["latency_history"])

                / len(stats["latency_history"]),

                2

            )

            if stats["minimum_latency_ms"] is None:

                stats["minimum_latency_ms"] = latency

            else:

                stats["minimum_latency_ms"] = min(

                    stats["minimum_latency_ms"],

                    latency

                )

            stats["maximum_latency_ms"] = max(

                stats["maximum_latency_ms"],

                latency

            )

    else:

        stats["failed_checks"] += 1

        stats["consecutive_failures"] += 1


def get_statistics():

    if stats["total_checks"] == 0:

        availability = 100

    else:

        availability = round(

            stats["successful_checks"]

            / stats["total_checks"]

            * 100,

            2

        )

    return {

        **stats,

        "availability_percent": availability

    }

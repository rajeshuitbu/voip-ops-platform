import subprocess
from datetime import datetime


def restart_kamailio():
    """
    Restart the Kamailio service.
    """

    try:
        # Restart Kamailio
        subprocess.run(
            ["systemctl", "restart", "kamailio"],
            check=True
        )

        # Verify service status
        result = subprocess.run(
            ["systemctl", "is-active", "kamailio"],
            capture_output=True,
            text=True
        )

        return {
            "service": "kamailio",
            "action": "restart",
            "status": result.stdout.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except subprocess.CalledProcessError as e:
        return {
            "service": "kamailio",
            "action": "restart",
            "status": "failed",
            "error": str(e),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

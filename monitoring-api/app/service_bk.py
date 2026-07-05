import subprocess
import psutil


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)


def get_kamailio_status():
    status = run_command(
        ["systemctl", "is-active", "kamailio"]
    )

    return {
        "service": "kamailio",
        "status": status
    }


def get_kamailio_version():
    version = run_command(
        ["kamailio", "-v"]
    )

    lines = version.splitlines()
    first_line = lines[0] if lines else "Unknown"

    return {
        "service": "kamailio",
        "version": first_line
    }


def get_kamailio_details():

    for process in psutil.process_iter(['pid', 'name']):

        if process.info['name'] == "kamailio":

            return {
                "service": "kamailio",
                "status": "running",
                "pid": process.info['pid']
            }

    return {
        "service": "kamailio",
        "status": "not running"
    }

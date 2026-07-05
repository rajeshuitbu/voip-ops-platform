import subprocess
import psutil
import socket
import platform
from datetime import datetime


def run_command(command):
    """
    Execute a Linux command and return stdout.
    """
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


def get_kamailio_process():
    """
    Find the running Kamailio process.
    """
    for process in psutil.process_iter(['pid', 'name']):

        if process.info['name'] == "kamailio":
            return process

    return None


def get_kamailio_details():

    process = get_kamailio_process()

    hostname = socket.gethostname()
    os_name = platform.system()
    os_version = platform.release()
    last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if process:

        # Prime CPU measurement
        process.cpu_percent(interval=0.1)

        cpu = process.cpu_percent(interval=0.1)

        memory = round(
            process.memory_info().rss / 1024 / 1024,
            2
        )

        threads = process.num_threads()

        start_time = datetime.fromtimestamp(
            process.create_time()
        )

        uptime = datetime.now() - start_time
        uptime = str(uptime).split(".")[0]

        pid = process.pid

    else:

        cpu = None
        memory = None
        threads = None
        uptime = None
        pid = None

    return {

        "service": "kamailio",

        "hostname": hostname,

        "os": os_name,

        "os_version": os_version,

        "status": get_kamailio_status()["status"],

        "version": get_kamailio_version()["version"],

        "pid": pid,

        "cpu_percent": cpu,

        "memory_mb": memory,

        "threads": threads,

        "uptime": uptime,

        "last_checked": last_checked
    }

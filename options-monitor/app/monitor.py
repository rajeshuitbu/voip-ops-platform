import socket
import time
from datetime import datetime


SERVER = "127.0.0.1"
PORT = 5060


def build_options():

    return (
        "OPTIONS sip:127.0.0.1 SIP/2.0\r\n"
        "Via: SIP/2.0/UDP 127.0.0.1:5065;branch=z9hG4bK123456\r\n"
        "Max-Forwards: 70\r\n"
        "From: <sip:monitor@localhost>;tag=12345\r\n"
        "To: <sip:kamailio@localhost>\r\n"
        "Call-ID: options-monitor-001\r\n"
        "CSeq: 1 OPTIONS\r\n"
        "Contact: <sip:monitor@127.0.0.1>\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    )


def send_options():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.settimeout(3)

    request = build_options()

    start = time.time()

    try:

        sock.sendto(request.encode(), (SERVER, PORT))

        data, _ = sock.recvfrom(4096)

        latency = round((time.time() - start) * 1000, 2)

        response = data.decode(errors="ignore")

        status_line = response.split("\r\n")[0]

        response_code = int(status_line.split()[1])

        return {

            "server": "kamailio",

            "ip": SERVER,

            "port": PORT,

            "method": "OPTIONS",

            "response_code": response_code,

            "status": "UP",

            "response_time_ms": latency,

            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "status_line": status_line

        }

    except socket.timeout:

        return {

            "server": "kamailio",

            "ip": SERVER,

            "port": PORT,

            "method": "OPTIONS",

            "response_code": None,

            "status": "DOWN",

            "response_time_ms": None,

            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "error": "Timeout"

        }

    finally:

        sock.close()

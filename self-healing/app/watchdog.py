import time
import subprocess

from app.service import restart_kamailio
from app.logger import logger


def get_kamailio_status():
    result = subprocess.run(
        ["systemctl", "is-active", "kamailio"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def start_watchdog():

    logger.info("===== Self-Healing Watchdog Started =====")

    while True:

        status = get_kamailio_status()

        if status == "active":

            logger.info("Kamailio is healthy.")

        else:

            logger.warning("Kamailio is DOWN. Starting verification...")

            recovered = False

            # Retry 3 times before restart
            for attempt in range(1, 4):

                logger.info(f"Retry {attempt}/3")

                time.sleep(5)

                status = get_kamailio_status()

                if status == "active":

                    logger.info("Kamailio recovered automatically.")

                    recovered = True
                    break

            if not recovered:

                logger.warning("Restarting Kamailio...")

                result = restart_kamailio()

                logger.info(f"Restart Result: {result}")

        time.sleep(30)

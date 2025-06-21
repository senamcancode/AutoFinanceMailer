from pathlib import Path

import watchdog.events
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from src.utils.email_utils import send_email_w_report_attachment
from src.utils.email_config import receiver, user, subject, message
import logging 
import time

class MyHandler(RegexMatchingEventHandler):
    def __init__(self):
        watchdog.events.RegexMatchingEventHandler.__init__(self, regexes=[r'.*\/Downloads\/MonthlyStatement.*-\d{4}\-\d{2}\.pdf$'], ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        if ".download" in event.src_path:
            logging.info(f"Ignored temporary download file: {event.src_path}")
            return 
        
        logging.info(f"Watchdog received Created Event: {event.src_path}")
        
        file_path = Path(event.src_path)
        wait_time = 0
        max_wait = 30
        last_size = -1 

        while wait_time < max_wait:
            if not file_path.exists():
                time.sleep(1)
                wait_time += 1
                continue

            current_size = file_path.stat().st_size
            if current_size == last_size:
                break
            last_size = current_size
            time.sleep(1)
            wait_time += 1

        try:
            trading_report = send_email_w_report_attachment(receiver, user, subject, message, event.src_path)
            logging.info(f"Email attachment {trading_report} successfully sent to {receiver}")

        except Exception as e:
            logging.error(f"Failed to send email report for {event.src_path}: {e}")

        return

def monitor():
    path = Path.home() / "Downloads" 
    logging.info(f"Montioring path: {path}")

    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    observer.start()

    while True:
        cmd = input("> ")
        if cmd == "q": break

    observer.stop()
    observer.join()
    logging.info("Observer shut down cleanly")

from pathlib import Path

import watchdog.events
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from email_utils import send_email_w_report_attachment
from email_config import receiver, user, subject, message
import logging 

class MyHandler(RegexMatchingEventHandler):
    def __init__(self):
        watchdog.events.RegexMatchingEventHandler.__init__(self, regexes=[r'.*\/Downloads\/MonthlyStatement.*-\d{4}\-\d{2}\.pdf$'], ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        logging.info("Watchdog received Created Event", event.src_path)
        trading_report = send_email_w_report_attachment(receiver, user, subject, message, event.src_path)
        logging.info(f"Email attachment {trading_report} successfully sent to {receiver}")

        return super().on_created(event)

def monitor():
    path = Path.home()
    
    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    observer.start()

    while True:
        cmd = input("> ")
        if cmd == "q": break

    observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor()


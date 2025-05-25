from pathlib import Path

import watchdog.events
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

class MyHandler(RegexMatchingEventHandler):
    def __init__(self):
        watchdog.events.RegexMatchingEventHandler.__init__(self, regexes=[r'.*\/Downloads\/MonthlyStatement.*-\d{4}\-\d{2}\.pdf$'], ignore_directories=True, case_sensitive=False)


    def on_created(self, event):
        print("Watchdog received Created Event", event.src_path)
        return super().on_created(event)

    def on_modified(selfself, event):
        print("Watchdog received Modified Event", event.src_path)
        return super().on_modified(event)


def main():
    path = Path("test_folder")
    #the above path will eventually be changed to Path.home()
    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    observer.start()

    while True:
        cmd = input("> ")
        if cmd == "q": break

    observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

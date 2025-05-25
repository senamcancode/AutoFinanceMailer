from pathlib import Path

import watchdog.events
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.pdf'], ignore_directories=True, case_sensitive=False)


    def on_created(self, event):
        print("Watchdog received Created Event", event.src_path)
        return super().on_created(event)

    def on_modified(selfself, event):
        print("Watchdog received Modified Event", event.src_path)
        return super().on_modified(event)


def main():
    path = Path("test_folder")
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

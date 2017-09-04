import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer

    def on_any_event(self, event):
        print(event)
        print(type(event))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    event_handler = MyEventHandler(observer)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

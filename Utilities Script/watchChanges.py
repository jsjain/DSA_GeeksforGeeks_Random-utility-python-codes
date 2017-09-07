import sys
import time
import distutils
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        print(event)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.\\src\\'
    event_handler = MyEventHandler(regexes=['*.js', '*.less'], 
                                    ignore_regexes=['*.git'], 
                                    ignore_directories=False, 
                                    case_sensitive=False)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

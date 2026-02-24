from __future__ import annotations

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class _Handler(FileSystemEventHandler):
    def __init__(self, on_new_file):
        self.on_new_file = on_new_file

    def on_created(self, event):
        if not event.is_directory:
            self.on_new_file(event.src_path)


class DownloadsWatcher:
    def __init__(self, folder_path: str, on_new_file):
        self.folder_path = folder_path
        self.on_new_file = on_new_file
        self._observer: Observer | None = None

    def start(self):
        if self._observer:
            return
        handler = _Handler(self.on_new_file)
        obs = Observer()
        obs.schedule(handler, self.folder_path, recursive=False)
        obs.start()
        self._observer = obs

    def stop(self):
        if not self._observer:
            return
        self._observer.stop()
        self._observer.join()
        self._observer = None

    @property
    def running(self) -> bool:
        return self._observer is not None

import os
import tkinter as tk
from tkinter import filedialog

from scanpro.scanner import scan_file, format_result
from scanpro.watcher import DownloadsWatcher


def default_downloads_folder() -> str:
    return os.path.expanduser("~/Downloads")


class ScanProApp:
    def __init__(self):
        self.downloads_folder = default_downloads_folder()
        self.watcher = DownloadsWatcher(self.downloads_folder, self._on_new_file)

        self.window = tk.Tk()
        self.window.title("ScanPro File Scanner — Samuel Zizzo")
        self.window.geometry("520x420")

        title = tk.Label(self.window, text="ScanPro File Scanner", font=("Helvetica", 18, "bold"))
        title.pack(pady=8)

        top_frame = tk.Frame(self.window)
        top_frame.pack(fill="x", padx=10, pady=5)

        self.toggle_button = tk.Button(top_frame, text="Enable File Watcher", command=self.enable_watcher)
        self.toggle_button.pack(side="left")

        clear_button = tk.Button(top_frame, text="Clear Output", command=self.clear_output)
        clear_button.pack(side="right")

        scan_button = tk.Button(self.window, text="Choose File to Scan", command=self.manual_scan)
        scan_button.pack(pady=5)

        self.output_box = tk.Text(self.window, height=12, wrap="word", state="disabled")
        self.output_box.pack(padx=10, pady=10, fill="both", expand=True)

        self.log_output("ScanPro initialized — Created by Samuel Zizzo")

        # stop watchdog cleanly on close
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def log_output(self, text: str):
        self.output_box.config(state="normal")
        self.output_box.insert(tk.END, text + "\n")
        self.output_box.see(tk.END)
        self.output_box.config(state="disabled")

    def clear_output(self):
        self.output_box.config(state="normal")
        self.output_box.delete(1.0, tk.END)
        self.output_box.config(state="disabled")

    def _scan_and_log(self, path: str):
        result = scan_file(path)
        self.log_output(format_result(result))

    def _on_new_file(self, path: str):
        self.log_output(f"[NEW FILE] {path}")
        self._scan_and_log(path)

    def manual_scan(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.log_output(f"Manual scan: {filepath}")
            self._scan_and_log(filepath)

    def enable_watcher(self):
        self.watcher.start()
        self.log_output("File watcher enabled.")
        self.toggle_button.config(text="Disable File Watcher", command=self.disable_watcher)

    def disable_watcher(self):
        self.watcher.stop()
        self.log_output("File watcher disabled.")
        self.toggle_button.config(text="Enable File Watcher", command=self.enable_watcher)

    def on_close(self):
        try:
            self.watcher.stop()
        finally:
            self.window.destroy()

    def run(self):
        self.window.mainloop()


def start_gui():
    ScanProApp().run()

# ScanPro File Scanner
# Created by Samuel Zizzo — 2025
# MIT License

import os
import mimetypes
import tkinter as tk
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

observer = None


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            log_output(f"[NEW FILE] {event.src_path}")
            scan_file(event.src_path)


def log_output(text):
    output_box.config(state="normal")
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)
    output_box.config(state="disabled")


def format_size(size_bytes):
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes} Bytes"


def scan_file(filepath):
    filename = os.path.basename(filepath)

    try:
        size_bytes = os.path.getsize(filepath)
        size_str = format_size(size_bytes)
    except Exception:
        size_str = "Unknown"

    filetype, _ = mimetypes.guess_type(filepath)
    ext = os.path.splitext(filename)[1].lower()

    risky_exts = [
        ".exe", ".bat", ".cmd", ".js", ".vbs",
        ".scr", ".ps1", ".msi", ".jar"
    ]

    risk_level = "HIGH" if ext in risky_exts else "LOW"
    risk_message = (
        "Potentially dangerous executable file."
        if risk_level == "HIGH"
        else "Common file type."
    )

    result = [
        "-----------------------------",
        "FILE SCAN RESULT",
        f"Name: {filename}",
        f"Type: {filetype or 'Unknown'}",
        f"Size: {size_str}",
        f"Risk Level: {risk_level}",
        f"Note: {risk_message}",
        "-----------------------------"
    ]

    log_output("\n".join(result))


def start_watcher():
    global observer

    if observer:
        return

    handler = DownloadHandler()
    observer = Observer()
    observer.schedule(handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()

    log_output("File watcher enabled.")


def stop_watcher():
    global observer

    if observer:
        observer.stop()
        observer.join()
        observer = None
        log_output("File watcher disabled.")


def manual_scan():
    filepath = filedialog.askopenfilename()
    if filepath:
        log_output(f"Manual scan: {filepath}")
        scan_file(filepath)


def clear_output():
    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)
    output_box.config(state="disabled")


def enable_watcher():
    start_watcher()
    toggle_button.config(text="Disable File Watcher", command=disable_watcher)


def disable_watcher():
    stop_watcher()
    toggle_button.config(text="Enable File Watcher", command=enable_watcher)


# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("ScanPro File Scanner — Samuel Zizzo")
window.geometry("520x420")

title = tk.Label(
    window,
    text="ScanPro File Scanner",
    font=("Helvetica", 18, "bold")
)
title.pack(pady=8)

top_frame = tk.Frame(window)
top_frame.pack(fill="x", padx=10, pady=5)

toggle_button = tk.Button(
    top_frame,
    text="Enable File Watcher",
    command=enable_watcher
)
toggle_button.pack(side="left")

clear_button = tk.Button(
    top_frame,
    text="Clear Output",
    command=clear_output
)
clear_button.pack(side="right")

scan_button = tk.Button(
    window,
    text="Choose File to Scan",
    command=manual_scan
)
scan_button.pack(pady=5)

output_box = tk.Text(window, height=12, wrap="word", state="disabled")
output_box.pack(padx=10, pady=10, fill="both", expand=True)

log_output("ScanPro initialized — Created by Samuel Zizzo")

window.mainloop()

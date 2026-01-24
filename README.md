# ScanPro File Scanner

ScanPro is a Python-based GUI application developed by **Samuel Zizzo** that monitors your **Downloads** folder for newly created files and performs a basic risk assessment.

The application detects file system changes using the **Watchdog** library and scans files by analyzing:
- File name
- File size
- File type (via Python’s `mimetypes`)
- File extension (to identify potentially risky executable formats)

If a file matches a known high-risk extension such as `.exe`, `.bat`, `.ps1`, or `.js`, ScanPro flags it as **HIGH risk**. Otherwise, it is marked **LOW risk**. This provides a simple first-pass security awareness tool.

> ScanPro does **not** analyze internal file contents or behavior. It is not an antivirus — it is a lightweight educational and early-warning utility.

---

## Features
- Monitors the Downloads folder for new files
- Scans files for size, type, and extension risk
- Allows manual file scanning
- Displays scan results in a simple Tkinter GUI

---

## Requirements (Running From Source)
- Python 3.8+
- watchdog

Install dependency:
```bash
pip install watchdog

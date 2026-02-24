# File Risk Engine (ScanPro)

ScanPro is a lightweight endpoint security tool that monitors newly created files and performs automated risk classification based on file metadata.

Developed by Samuel Zizzo as part of a cybersecurity-focused portfolio, this project demonstrates event-driven monitoring, endpoint visibility concepts, and basic risk scoring logic used in enterprise security environments.

---

##Demo




---

## Overview

The application continuously monitors a target directory (Downloads folder by default) and evaluates newly detected files using metadata-based analysis.

This simulates an early-stage endpoint detection workflow commonly used in enterprise environments before deeper behavioral or signature analysis occurs.

---

## Features

- Real-time filesystem monitoring using Watchdog
- Automatic file risk classification
- Metadata inspection:
  - File name
  - Extension
  - MIME type
  - File size
- High-risk executable detection
- Manual file scan capability
- Tkinter-based GUI dashboard

---

## Risk Classification Logic

Files are categorized based on extension risk:

| Risk Level | Example Extensions |
|------------|-------------------|
| HIGH | `.exe`, `.bat`, `.ps1`, `.js` |
| LOW | documents, media, archives |

⚠️ This tool does **not** perform malware analysis or behavioral inspection.

---

## Technology Stack

- Python 3
- Tkinter GUI
- Watchdog (filesystem monitoring)
- Mimetypes library

---

## Installation

Clone repository:

```bash
git clone https://github.com/szizzo522/file-risk-engine.git
cd file-risk-engine

Install dependencies:

pip install -r requirements.txt

Run application:

python main.py

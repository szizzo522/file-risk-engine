# File Risk Engine (ScanPro)

ScanPro is an endpoint security tool that monitors newly downloaded and created files. It performs automated risk classification based on file metadata.

---

## Demo

**Check out my other projects on [YouTube](https://www.youtube.com/@Research-Farm/videos)**

[![Watch the Demo](https://img.youtube.com/vi/eSiTjAktJIQ/0.jpg)](https://www.youtube.com/watch?v=BQvOrIgLj3g)


---

## Features
- Continuously monitors a target directory (Downloads folder by default) and evaluates newly detected files using metadata-based analysis
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

---

## Installation

Clone repository:

```bash
git clone https://github.com/szizzo522/file-risk-engine.git
```bash
cd file-risk-engine

Install dependencies:
```bash
pip install -r requirements.txt

Run application:
```bash
python main.py

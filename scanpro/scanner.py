import mimetypes
from dataclasses import dataclass
from pathlib import Path

RISKY_EXTS = {
    ".exe", ".bat", ".cmd", ".js", ".vbs",
    ".scr", ".ps1", ".msi", ".jar"
}


@dataclass
class ScanResult:
    name: str
    filetype: str
    size_str: str
    risk_level: str
    note: str
    path: str


def format_size(size_bytes: int) -> str:
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    if size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes} Bytes"


def scan_file(filepath: str) -> ScanResult:
    p = Path(filepath)
    filename = p.name
    ext = p.suffix.lower()

    try:
        size_bytes = p.stat().st_size
        size_str = format_size(size_bytes)
    except Exception:
        size_str = "Unknown"

    filetype, _ = mimetypes.guess_type(str(p))
    filetype = filetype or "Unknown"

    risk_level = "HIGH" if ext in RISKY_EXTS else "LOW"
    note = "Potentially dangerous executable file." if risk_level == "HIGH" else "Common file type."

    return ScanResult(
        name=filename,
        filetype=filetype,
        size_str=size_str,
        risk_level=risk_level,
        note=note,
        path=str(p)
    )


def format_result(result: ScanResult) -> str:
    lines = [
        "-----------------------------",
        "FILE SCAN RESULT",
        f"Name: {result.name}",
        f"Type: {result.filetype}",
        f"Size: {result.size_str}",
        f"Risk Level: {result.risk_level}",
        f"Note: {result.note}",
        "-----------------------------",
    ]
    return "\n".join(lines)

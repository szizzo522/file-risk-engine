# ScanPro File Scanner:
ScanPro is a Python-based GUI application that monitors your Downloads folder for new files and scans them for potential risks. Watchdog is a Python library that monitors file system events. It allows programs to detect when files and directories are created, modified, moved, or deleted. The app compares the file’s extension (for example, .exe, .js, .bat) against a list of extensions known to be associated with executable or potentially dangerous files. If it finds a match, it flags the file as high risk. It also uses Python’s mimetypes module to guess the file’s type. While this doesn’t tell you everything about the file’s content, it helps verify if the file’s nature (like being an application or script) aligns with its extension. Based on these checks, the app then outputs a risk level (“HIGH” for risky extensions, “LOW” otherwise) along with a recommendation on whether it’s safe to open the file.

## Features:
- Monitors the Downloads folder for new files.
- Scans files for size, type, and potentially risky extensions.
- Allows manual file scanning.
- Displays results in a user-friendly GUI.

## Requirements (for Developers / Running from Source)
If you want to run ScanPro directly from the Python source code:

- Python 3.8 or later
- watchdog
 ```bash
pip install watchdog
```

## Installation
### 1. Download the Executable
1. Go to the [Releases](https://github.com/szizzo522/ScanPro/releases) page of this repository.
2. Download the latest version of the executable:
   - On **Windows**, download `ScanPro.exe`.
   - On **macOS**, download `ScanPro.app`.

### 2. Run the Application
#### On Windows:
1. Locate the downloaded `ScanPro.exe` file.
2. Double-click the `ScanPro.exe` file to launch the application.

#### On macOS:
1. Locate the downloaded `ScanPro.app` file.
2. Double-click the `ScanPro.app` file to launch the application.
3. If you see a security warning, go to **System Preferences > Security & Privacy > General** and click **Open Anyway**.
4. If you see an error like **“The application can’t be opened”**, run the following in Terminal to fix it:

```bash
xattr -rd com.apple.quarantine ~/Downloads/ScanPro\ 2.app
chmod +x ~/Downloads/ScanPro\ 2.app/Contents/MacOS/*
```
**Then**, right-click the app and choose **Open** again. This bypasses macOS Gatekeeper restrictions for new/unverified apps.

**No additional setup is required on either platform.**

## Licnse

This project is licensed under the MIT License. See the [LICENSE](./LICENCE) file for details.

## Comments
***This was created using python version 3.12.2***

***This is a basic scanner—it doesn’t actually analyze the file’s internal code or behavior. More advanced scanners use signature-based or heuristic analysis, sometimes even running files in a sandbox. This version is meant as a learning tool and a simple first line of defense.***

***I don’t expect or recommend anyone to download and run this app blindly — that’s just not good security practice in general.
That said, ScanPro is 100% malware-free and built with transparency in mind.
You can always review the source code in this repo to verify what it does.***

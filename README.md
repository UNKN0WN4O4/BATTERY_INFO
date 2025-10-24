# BATTERY_INFO

Lightweight Python utilities for reading battery information from Windows systems. This repository contains source code and utilities to read battery attributes exposed on Windows (WMI/Win32, or via psutil when available). This project is not published to PyPI. And also attached a file which has ready exe file in it just click and run:)

Badges
- build: [![CI](https://img.shields.io/badge/ci-none-lightgrey)](https://github.com/UNKN0WN4O4/BATTERY_INFO/actions)
- pypi: [![PyPI](https://img.shields.io/badge/pypi-not%20published-lightgrey)](https://pypi.org/project/)
- license: [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

Table of contents
- What this repo is
- Installation (from source)
- How to use
- Supported platforms
- Requirements
- Development
- Contributing
- Troubleshooting
- License
- Contact

What this repo is
- A simple, Windows-focused implementation for reading battery details (percentage, charging state, and additional properties when the platform exposes them).
- Not a published PyPI package; install from the repository or clone and install locally.
- There is no official CLI or stable public API documented here unless you add/define one in the code. Use the code directly or request a documented API and I will add examples.

Installation (from source)
- Recommended: install into a virtual environment
```bash
git clone https://github.com/UNKN0WN4O4/BATTERY_INFO.git
cd BATTERY_INFO
python -m venv .venv
# activate the venv:
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -e .
```

How to use
- This repository contains the implementation code. Check the package/module files (look for the main package folder or top-level Python modules) to see available functions and classes.
- If you want a short usage snippet or a CLI wrapper added, tell me which function(s) in the code should be exposed and I will add examples and a small CLI entrypoint.

Supported platforms
- Windows only — this code is written to read battery data from Windows APIs (WMI, Win32Battery or psutil on Windows).
- It does not provide macOS or Linux support at this time. If you want cross-platform support, I can add Linux/macOS adapters (e.g., read /sys/class/power_supply or use upower/IOKit) — say the word and I’ll sketch an implementation plan.

Requirements
- Python 3.8+
- Optional: psutil (used if present to simplify cross-platform calls on Windows)
- Optional (for additional Windows info): pywin32 or wmi

Development

Setup dev environment
```bash
git clone https://github.com/UNKN0WN4O4/BATTERY_INFO.git
cd BATTERY_INFO
python -m venv .venv
.venv\Scripts\activate   # Windows
python -m pip install -e ".[dev]"   # if extras/dev dependencies are defined
```

Run tests
```bash
pytest
```

Lint & formatting
```bash
flake8
black .
```

Contributing
- Fork the repo, create a branch, add your feature or fix, include tests, and open a pull request.
- If you plan to add Linux or macOS adapters or a CLI/JSON interface, open an issue with the proposed interface (fields and names) so we can agree on the contract before implementation.

Troubleshooting
- If the Windows machine shows no battery:
  - Ensure the system exposes battery devices and WMI is available.
  - Check Device Manager for batteries and verify permissions for WMI queries.
  - psutil may provide battery details on some Windows installations — install psutil and retry if supported.

License
- MIT — see the LICENSE file.

Contact
- Author: UNKN0WN4O4
- GitHub: https://github.com/UNKN0WN4O4/BATTERY_INFO
- Issues: https://github.com/UNKN0WN4O4/BATTERY_INFO/issues

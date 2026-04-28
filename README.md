# LogHound 🛡️

**LogHound** is a lightweight, efficient Python-based utility designed to analyze system authentication logs (`auth.log`) and identify potential brute-force attacks by monitoring failed login attempts.

---

## 🚀 Overview

LogHound scans specified log directories, parses authentication events using optimized regular expressions, and aggregates failed attempts by source IP address. If an IP exceeds a configurable threshold, it is flagged as a potential threat.

### Key Features
- **Brute Force Detection:** Automatically identifies high-frequency failed attempts.
- **Cross-Platform CLI:** Compatible with Linux (system logs) and Windows (for testing/archived logs).
- **Intelligent Parsing:** Filters out legitimate noise (Cron jobs, session events) to focus on security-relevant data.
- **Sortable Reporting:** Displays suspicious IPs ranked by attempt frequency.

---

## 🏗️ Architecture & Workflow

LogHound follows a simple but robust pipeline to ensure accuracy and performance.

```text
[ Log File ] --> [ Regex Engine ] --> [ IP Aggregator ] --> [ Threshold Validator ] --> [ Security Report ]
      ^                |                    |                       |                       |
   auth.log      Filters "Failed"      Counter/Map           Check against          CLI Visualization
                 password lines        by Source IP          Config (default: 5)
```

---

## 🛠️ Usage

### Installation
Clone the repository and ensure you have Python 3.6+ installed.
```bash
git clone https://github.com/youruser/LogHound.git
cd LogHound
```

### Running the Scanner
To scan the default system directory (`/var/log`):
```bash
python cli.py
```

To scan a custom directory or archived logs:
```bash
python cli.py ./path/to/logs
```

> **Note:** On Linux systems, reading `/var/log/auth.log` typically requires elevated privileges. Use `sudo python cli.py`.

---

## 📊 Sample Output

```text
Scanning test_logs/auth.log for unauthorized access attempts (Threshold: 5)...

--- Brute Force Detection Report ---
[!] POSSIBLE BRUTE FORCE: 192.168.1.50  - 35 failed attempts
[!] POSSIBLE BRUTE FORCE: 45.12.33.101  - 35 failed attempts

Scan complete.
```

---

## 🛡️ Security Disclaimer
LogHound is an analysis tool meant for log auditing. For active prevention, consider integrating with tools like `fail2ban` or system firewall rules.

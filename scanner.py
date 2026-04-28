import os
import sys
import re
from collections import Counter

def scan_directory(directory, threshold=5):
    log_file = os.path.join(directory, "auth.log")
    
    if not os.path.isfile(log_file):
        print(f"Error: {log_file} does not exist.")
        return

    print(f"Scanning {log_file} for unauthorized access attempts (Threshold: {threshold})...")

    # Regex to capture IP addresses in "Failed password" lines
    # Example: "Failed password for root from 192.168.1.1 port 12345 ssh2"
    failed_pattern = re.compile(r"Failed password for .* from ([\d\.]+) port")
    ip_counts = Counter()

    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                match = failed_pattern.search(line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] += 1
    except PermissionError:
        print(f"Error: Permission denied reading {log_file}. Try running with elevated privileges.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    print("\n--- Brute Force Detection Report ---")
    detected = False
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        if count >= threshold:
            print(f"[!] POSSIBLE BRUTE FORCE: {ip} - {count} failed attempts")
            detected = True
    
    if not detected:
        print("No suspicious activity detected based on the current threshold.")
    
    print("\nScan complete.")

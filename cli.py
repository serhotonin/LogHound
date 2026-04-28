import os
import sys  
from scanner import scan_directory

def main():
    # os.geteuid() is not available on Windows
    if sys.platform != "win32":
        try:
            if os.getuid() != 0:
                print("Warning: This script usually requires root privileges to read system logs.")
        except AttributeError:
            pass
    
    # Default log directory
    log_directory = "/var/log"
    
    # Allow user to specify a path as an argument
    if len(sys.argv) > 1:
        log_directory = sys.argv[1]
        
    if not os.path.exists(log_directory):
        print(f"Error: Directory '{log_directory}' not found.")
        print(f"Usage: python cli.py [log_directory_path]")
        sys.exit(1)

    scan_directory(log_directory)

if __name__ == "__main__":
    main()

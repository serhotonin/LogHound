## Executable cli tool for LogHound
## Usage: LogHound.sh [options] <log_file>
## Options:
##   -h, --help          Show this help message and exit
##   -v, --version       Show version information and exit
##   -f, --filter <pattern>  Filter log entries by pattern
##   -o, --output <file>     Output results to a file   

#!/bin/bash 
VERSION="1.0.0"
print_help() {
    echo "Usage: LogHound.sh [options] <log_file>"
    echo "Options:"
    echo "  -h, --help          Show this help message and exit"
    echo "  -v, --version       Show version information and exit"
    echo "  -f, --filter <pattern>  Filter log entries by pattern"
    echo "  -o, --output <file>     Output results to a file"
}
print_version() {
    echo "LogHound version $VERSION"
}
filter_pattern=""
output_file=""
while [[ "$1" == -* ]]; do
    case "$1" in
        -h|--help)
            print_help
            exit 0
            ;;
        -v|--version)
            print_version
            exit 0
            ;;
        -f|--filter)
            shift
            filter_pattern="$1"
            ;;
        -o|--output)
            shift
            output_file="$1"
            ;;
        *)            echo "Unknown option: $1"
            print_help
            exit 1
            ;;
    esac
    shift
done
if [[ -z "$1" ]]; then      
    echo "Error: No log file specified."
    print_help
    exit 1
fi
log_file="$1"
if [[ ! -f "$log_file" ]]; then
    echo "Error: Log file '$log_file' not found."
    exit 1
fi
if [[ -n "$filter_pattern" ]]; then
    filtered_logs=$(grep "$filter_pattern" "$log_file")
else
    filtered_logs=$(cat "$log_file")
fi
if [[ -n "$output_file" ]]; then
    echo "$filtered_logs" > "$output_file"
    echo "Filtered logs written to '$output_file'"  
else
    echo "$filtered_logs"
fi

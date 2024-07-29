#!/usr/bin/python3
"""
Script to parse log lines from stdin and compute metrics.

Metrics:
- Total file size: sum of all file sizes
- Number of lines by status code: count of occurrences of each status code

Usage:
    cat log_file |./0-stats.py

Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example:
    192.168.1.1 - [2022-01-01 12:00:00] "GET /projects/260 HTTP/1.1" 200 1024
"""

import sys
import re

def parse_log_line(line):
    """
    Parse a log line and extract file size and status code.

    Args:
        line (str): log line to parse

    Returns:
        tuple: (file size, status code) or None if line is invalid
    """
    pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')
    match = pattern.match(line)
    if match:
        file_size = int(match.group(3))
        status_code = int(match.group(2))
        return file_size, status_code
    return None

def main():
    """
    Main function to parse log lines and compute metrics.
    """
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    for i, line in enumerate(sys.stdin):
        result = parse_log_line(line)
        if result:
            file_size, status_code = result
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        if (i + 1) % 10 == 0 or (i + 1) == 10000:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
        try:
            pass
        except KeyboardInterrupt:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            sys.exit(0)

if __name__ == "__main__":
    main()

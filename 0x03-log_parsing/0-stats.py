#!/usr/bin/python3
"""log parsing script"""
import sys


def show_stats(total_size, code_counts):
    """Show the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(code_counts):
        if code_counts[code] > 0:
            print(f"{code}: {code_counts[code]}")


total_size = 0
code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_num = 0

try:
    for log in sys.stdin:
        fields = log.split()

        if len(fields) >= 2:
            try:
                status = int(fields[-2])
                if status in code_counts:
                    code_counts[status] += 1
            except ValueError:
                pass

            try:
                size = int(fields[-1])
                total_size += size
            except ValueError:
                pass

        line_num += 1
        if line_num % 10 == 0:
            show_stats(total_size, code_counts)

finally:
    show_stats(total_size, code_counts)

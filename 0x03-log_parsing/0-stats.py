#!/usr/bin/env python3
""" function that reads stdin line by line and computes metrics """

import sys


def process_line(line):
    # Split the line into components
    parts = line.split()

    # Check if the line matches the expected format
    if len(parts) >= 9 and parts[5].isdigit() and parts[8].isdigit():
        return int(parts[8]), int(parts[5])

    return None, None


def print_statistics(total_size, status_counts):
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')


def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            # Process each line
            file_size, status_code = process_line(line)

            if file_size is not None and status_code is not None:
                # Update total file size
                total_size += file_size

                # Update status code counts
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1

            # Print statistics every 10 lines
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass
    finally:
        # Print final statistics
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()

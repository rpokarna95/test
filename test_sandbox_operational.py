"""
Sandbox Operational Test
========================
Verifies the sandbox is operational by printing and logging the current timestamp.
Requested by rpokarna95 in PR comment 3820121095.
"""

import os
from datetime import datetime

LOG_FILE = "sandbox_operational.log"


def get_current_timestamp():
    """Get the current timestamp in ISO format."""
    return datetime.now().isoformat()


def print_timestamp(timestamp):
    """Print the timestamp to demonstrate sandbox is running."""
    print(f"Sandbox Execution Timestamp: {timestamp}")


def log_timestamp_to_file(timestamp, log_file=LOG_FILE):
    """Write the timestamp to a log file in text format for verification."""
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    with open(log_file, 'a') as f:
        f.write(f"Sandbox Operational Test - Timestamp: {timestamp}\n")


def run_sandbox_test():
    """Run the sandbox operational test."""
    timestamp = get_current_timestamp()
    
    # Print timestamp to stdout
    print_timestamp(timestamp)
    
    # Log timestamp to file
    log_timestamp_to_file(timestamp)
    
    print(f"Timestamp logged to: {LOG_FILE}")
    return timestamp


if __name__ == '__main__':
    run_sandbox_test()

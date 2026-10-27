"""
Utility functions and constants for the Robotics Micro-Profiler.

This module provides utility functions and constants that are used throughout the library.
"""

# Constants
MAX_STACK_SIZE = 1000  # Maximum number of stack frames to display in a report
REPORT_WIDTH = 80  # Width of each line in a flame-style text report

def format_time_ns(time_ns: int) -> str:
    """
    Format time in nanoseconds as a string.

    Args:
        time_ns (int): Time in nanoseconds.

    Returns:
        str: Formatted time string.
    """
    return f"{time_ns:.2f} ns"

def format_time_s(time_s: float) -> str:
    """
    Format time in seconds as a string.

    Args:
        time_s (float): Time in seconds.

    Returns:
        str: Formatted time string.
    """
    return f"{time_s:.2f} s"

def format_memory_bytes(memory_bytes: int) -> str:
    """
    Format memory usage in bytes as a string.

    Args:
        memory_bytes (int): Memory usage in bytes.

    Returns:
        str: Formatted memory string.
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if memory_bytes < 1024:
            return f"{memory_bytes} {unit}"
        memory_bytes //= 1024

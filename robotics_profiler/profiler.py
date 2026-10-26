"""
Core instrumentation logic and API.

Provides a simple way to measure execution time of code blocks in a flame-style text report.
"""

class Profiler:
    def __init__(self):
        """Initialize the profiler."""
        self._start_times = {}

    def _get_elapsed_time(self, name):
        """Get elapsed time for a given function or block."""
        return self._start_times.get(name, 0)

    def start_block(self, name):
        """Start measuring execution time of a code block."""
        self._start_times[name] = time.time()

    def end_block(self, name):
        """End measuring execution time of a code block and print report."""
        elapsed_time = time.time() - self._get_elapsed_time(name)
        print(f"{name}: {elapsed_time:.6f} seconds")

def profile(func):
    """
    Decorator to measure execution time of a function.

    Args:
        func: Function to be measured.

    Returns:
        Wrapper function with profiling enabled.
    """
    def wrapper(*args, **kwargs):
        profiler = Profiler()
        profiler.start_block(func.__name__)
        result = func(*args, **kwargs)
        profiler.end_block(func.__name__)
        return result
    return wrapper

import time

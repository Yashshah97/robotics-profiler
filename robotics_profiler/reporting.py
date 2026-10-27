"""
Flame-style text reporting functionality for the Robotics Micro-Profiler.

This module provides functions to generate flame-style reports in plain text format.
"""

def format_report(report_data):
    """
    Format report data into a string with a flame-style layout.

    Args:
        report_data (dict): Dictionary containing report data. Each key is a function name,
            and each value is a dictionary with 'time' and 'calls' keys.

    Returns:
        str: Formatted report as a plain text string.
    """
    max_time = 0
    for func_name, func_data in report_data.items():
        if func_data['time'] > max_time:
            max_time = func_data['time']

    formatted_report = ""
    for func_name, func_data in sorted(report_data.items(), key=lambda x: x[1]['time'], reverse=True):
        time_ratio = func_data['time'] / max_time
        formatted_report += f"{func_name}: {time_ratio:.2f} ({func_data['calls']} calls)\n"

    return formatted_report

def generate_report(report_data, title="Flame Report"):
    """
    Generate a flame-style report from report data.

    Args:
        report_data (dict): Dictionary containing report data. Each key is a function name,
            and each value is a dictionary with 'time' and 'calls' keys.
        title (str, optional): Title of the report. Defaults to "Flame Report".

    Returns:
        str: Formatted report as a plain text string.
    """
    formatted_report = f"{title}\n"
    for func_name, func_data in report_data.items():
        time_ratio = func_data['time'] / sum(x['time'] for x in report_data.values())
        formatted_report += f"  {func_name}: {time_ratio:.2f} ({func_data['calls']} calls)\n"

    return formatted_report

# Example usage:
report_data = {
    'function1': {'time': 10, 'calls': 5},
    'function2': {'time': 20, 'calls': 3},
    'function3': {'time': 15, 'calls': 7}
}

print(format_report(report_data))
print(generate_report(report_data))

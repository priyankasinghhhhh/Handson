import os
import platform
import subprocess

def get_system_uptime():
    """
    Returns the system uptime as a string.
    Works on Linux, macOS, and Windows.
    """
    system = platform.system()
    try:
        if system == "Linux":
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours, remainder = divmod(int(uptime_seconds), 3600)
                minutes, seconds = divmod(remainder, 60)
                return f"Uptime: {hours}h {minutes}m {seconds}s"
        elif system == "Darwin":
            output = subprocess.check_output(['uptime']).decode()
            # The uptime output format on macOS is slightly different.
            # Example: 14:36  up 1 day,  4:03, 2 users, load averages: 1.84 1.98 2.04
            up_part = output.split(' up ')[1].split(',')[0:2]
            return f"Uptime: {', '.join(up_part)}"
        elif system == "Windows":
            output = subprocess.check_output(['net', 'stats', 'srv'], shell=True).decode()
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"Uptime since: {line.split('since')[1].strip()}"
            return "Could not determine uptime on Windows."
        else:
            return "Unsupported operating system for uptime check."
    except Exception as ex:
        return f"Error retrieving uptime: {ex}"

if __name__ == "__main__":
    print(get_system_uptime())

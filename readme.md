Using GitHub Copilot to Generate a System Uptime Script
Experience Using Copilot
I asked GitHub Copilot to create a Python script (copilot_test.py) that prints the system's uptime. Copilot generated the following script:

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
Modifications
I reviewed the generated code and found that it already covered Linux, macOS, and Windows, and handled exceptions gracefully. No modifications were necessary.

Testing
To test the script:

I ran it on my local machine with:
python copilot_test.py
The script output the system uptime in a human-readable format, confirming it worked as intended.
How to Run the Script
Make sure you have Python 3 installed.
Save the script as copilot_test.py in your project directory.
Open a terminal and navigate to the directory containing the script.
Run the script with:
python copilot_test.py
You should see the system's uptime printed in the terminal.

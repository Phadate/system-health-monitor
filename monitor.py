#! /usr/bin/env python3
import subprocess
from datetime import datetime

current_time = datetime.now().strftime('%d-%m-%Y %X')

# create a header that shows the welcome message
def header():
    print("=" * 50)
    print("SYSTEM HEALTH MONITOR")
    print(f"Report Time: {current_time}")
    print("=" * 50)
    print()

def get_cpu_usage():
    try:
        result = subprocess.run(
            args=['top', '-bn1'],
            capture_output=True,
            text=True
        )
        # Loop through the result to get each line 
        for line in result.stdout.split('\n'):
            if "Cpu(s)" in line:
                cpu_properties = line.split(',')
                # split the cpu_properties and pick the 1st value
                idle = cpu_properties[3].split()[0]
                cpu_usage = 100 - float(idle)
                return cpu_usage
            
        return None
    except Exception as e:
        print(f"Error getting Cpu usage : {e}")
        return None

def display_cpu_usage():
    # save the return value from the get_cpu_usage() function in the cpu variable
    cpu = get_cpu_usage()
    # Check the logic
    if cpu is not None:
        print(f"CPU Usage: {round(cpu,2)}%")
        if cpu > 90:
            print("🔥 CPU usage is Critical")
        elif 75< cpu <= 90:
            print("⚠️ CPU usage is High!")
        elif 50 < cpu <= 75:
            print("🚀 CPU usage is Busy!")
        elif 20 < cpu <= 50:
            print("🙂 CPU usage is Normal!")
        else:
            print(f"😴 CPU usage is Idle!")
    else:
        print("CPU Usage is Not Available")
    print()

def main():
    header()
    print("Starting system check...")
    display_cpu_usage()
    
 
if __name__ == '__main__':
    main()

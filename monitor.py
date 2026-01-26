#! /usr/bin/env python3
import subprocess
import sys
from datetime import datetime

current_time = datetime.now().strftime('%d-%m-%Y %X')

# create a header that shows the welcome message
def header():
    print("=" * 50)
    print("SYSTEM HEALTH MONITOR")
    print(f"Report Time: {current_time}")
    print("=" * 50)

def get_cpu_usage():

    result = subprocess.run(
        args=['top', '-bn1'], 
        capture_output=True, 
        text=True
        )
    
    for line in result.stdout.split("\n"):
        if "Cpu(s)" in line:
            # Treat the comma "," in the string, most time, 
            cpu_parts = line.split(',')
            idle = cpu_parts[3].split()[0]
            print(100 -float(idle))
            

    # print(result.stdout

def main():
    header()
    get_cpu_usage()


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
import subprocess
from datetime import datetime
import time

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

# TODO Get the memory usage data from the system
def get_memory_usage():
    try:
        result = subprocess.run(
            args=['free', '-m'],
            capture_output=True,
            text=True
        ).stdout

        rows = result.split("\n")
        mem_line = rows[1].split()
        total = int(mem_line[1])
        used = int(mem_line[2])
        percentage = (used / total) * 100

        return {
            'total': total,
            'used': used,
            'percentage': int(percentage)
        }
    except Exception as e:
        print(f"Error getting memory usage : {e}")
        return None


# Todo Display and format the usage

def display_memory_usage():
    memory = get_memory_usage()
    if memory is not None:
        print(f"Memory Usage: {memory['used']} MB / {memory['total']} MB ({memory['percentage']}%)")
        usage_percentage = memory['percentage']
        if usage_percentage > 85:
            print("⚠️ High memory usage! ")
        elif usage_percentage >= 60:
            print("⚡ Memory usage is moderate")
        else:
            print("👍 Memory usage is normal")
    else:
        print("Memory Usage is Not Available")
    print()

# Todo Get and display the disk usage 

def get_disk_usage():
    try:
        result = subprocess.run(
            # Add the / to return the root
            args=['df', '-h','/'],
            capture_output=True,
            text=True
        ).stdout

        rows = result.split('\n')
        filesystem = rows[1].split()
        size = filesystem[1]
        used = filesystem[2]
        available = filesystem[3]
        percentage = int(filesystem[-2].split('%')[0])

        disk = {
            'size' : size,
            'used' : used,
            'available' : available,
            'percentage' : percentage
        }

        return disk

    except Exception as e:
        print(f'Disk usage is not available due to {e}')
        return None

def display_disk_usage():
    disk = get_disk_usage()
    if disk is not None:
        print(f"Disk usage: {disk['used']} / {disk['size']} ({disk['percentage']}%)")
        print(f"Disk Available: {disk['available']}")
        percentage = disk['percentage']
        if percentage >= 90:
            print("⚠️ Disk space is low!")
        elif percentage >= 75:
            print("⚡ Disk space is moderate!")
        else:
            print("👍 Disk space is low!")

    else:
        print("😥 Unable to retrieve disk storage")
    print()

def main():
    header()
    print("Starting system check...")
    time.sleep(2)
    display_cpu_usage()
    display_memory_usage()
    display_disk_usage()
    print('=' * 50)
    
 
if __name__ == '__main__':
    main()

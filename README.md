# System Health Monitor

A Python script that monitors Linux system health metric including CPU, disk, and memory usage.

## Features
- ✅ CPU usage monitoring with alerts
- ✅ Memory usage monitoring with alerts
- ✅ Disk space monitoring with alerts
- ✅ Color-coded warnings
- 🔄 (Coming soon) Logging to file
- 🔄 (Coming soon) Process monitoring

## Requirements
- Python 3.6+
- Linux operating system
- Basic system utilities (top, free, df)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/system-health-monitor.git
cd system-health-monitor
```

2. Make the script executable:
```bash
chmod +x monitor.py
```

3. Run the script directly:
```bash
./monitor.py
```

## Example Output

<img width="416" height="291" alt="Image" src="https://github.com/user-attachments/assets/b8dee05c-7762-4d7e-b08b-696fc1af89fa" />

## What I Learned
- Git workflow and version control
- How to change the locale from Numeric= Poland to Numeric = C in linux
- Using Python's subprocess module to run Linux commands
- Parsing command output and extracting data(Interating with the Dictionary)
- String manipulation and formatting
- Error handling with try/except

## Next Steps

- Add logging functionality
- Create configuration file
- Add command-line arguments
- Schedule automatic checks with cron
- Add more monitoring metrics

## Author

Dunsin Fayode

## License

MIT
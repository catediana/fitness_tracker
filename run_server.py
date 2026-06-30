
import os
import subprocess
import time

# Set correct working directory
os.chdir(r"c:\Users\admin\Desktop\fitness tracker\fitness_tracker")

# Log file
log_file = r"c:\Users\admin\Desktop\fitness tracker\fitness_tracker\server_log.txt"

# Clear log and start fresh
with open(log_file, 'w', encoding='utf-8') as f:
    f.write(f"Starting server...\n")

# Start server
python_exe = os.path.join(os.getcwd(), "env", "Scripts", "python.exe")
cmd = [python_exe, "manage.py", "runserver"]

with open(log_file, 'a', encoding='utf-8') as log:
    process = subprocess.Popen(
        cmd,
        stdout=log,
        stderr=subprocess.STDOUT,
        text=True
    )

print(f"Server started with PID: {process.pid}")
print(f"Logs are being written to: {log_file}")
time.sleep(3)  # Wait a few seconds for server to initialize

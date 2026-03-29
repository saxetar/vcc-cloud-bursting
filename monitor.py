import psutil
import subprocess
import time
import os

# Configuration
THRESHOLD = 75       # CPU percentage to trigger burst
CHECK_INTERVAL = 5   # Seconds between checks

SCRIPT_PATH = os.path.expanduser("~/vcc-cloud-bursting/scale_out.sh")

print(f"Monitoring CPU... Threshold: {THRESHOLD}%")

try:
    while True:
        # Get CPU usage over the last interval
        cpu_usage = psutil.cpu_percent(interval=CHECK_INTERVAL)
        print(f"Current CPU Usage: {cpu_usage}%")
        
        if cpu_usage > THRESHOLD:
            print("Threshold exceeded! Triggering scale_out.sh...")
            try:
                # Run the bash script to resize the GCP Instance Group
                subprocess.run(["bash", SCRIPT_PATH], check=True)
                print("Scale out command sent successfully.")
                
                break 
            except Exception as e:
                print(f"Error running scale_out script: {e}")
                break
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

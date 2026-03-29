import psutil
import time
import subprocess

# Configured for 8GB local VM environment
THRESHOLD = 75.0
CHECK_INTERVAL = 5 # Check every 5 seconds
CONSECUTIVE_CHECKS = 4 # Wait for 20 seconds of sustained high CPU before bursting

def scale_to_cloud():
    print("CRITICAL: Local CPU > 75%. Triggering GCP Managed Instance Group scale-out...")
    subprocess.call(['./scale_out.sh'])

def monitor():
    high_cpu_count = 0
    print("Starting lightweight VCC resource monitor...")
    
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(f"Local CPU Usage: {cpu}%")
        
        if cpu > THRESHOLD:
            high_cpu_count += 1
            if high_cpu_count >= CONSECUTIVE_CHECKS:
                scale_to_cloud()
                high_cpu_count = 0 # Reset after triggering
                print("Sleeping monitor for 60s to allow GCP provisioning...")
                time.sleep(60) 
        else:
            high_cpu_count = 0
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()

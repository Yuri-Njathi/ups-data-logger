import json
import os
from datetime import datetime

# Path to your Eaton JSON log file
LOG_FILE = os.path.expanduser("~/ups_metrics_all.json")

def analyze_ups_logs():
    if not os.path.exists(LOG_FILE):
        print(f"Error: Log file not found at {LOG_FILE}")
        return

    print(f"--- Analyzing Eaton 9E3000i Log Data ---")
    
    total_entries = 0
    with open(LOG_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            try:
                # Parse the line-delimited JSON string into a Python dictionary
                data = json.loads(line)
                total_entries += 1
                
                # Extract and format specific metrics dynamically
                timestamp = data.get("timestamp", "Unknown Time")
                status = data.get("ups.status", "N/A")
                load = data.get("ups.load", "0")
                power = data.get("ups.realpower", "0")
                charge = data.get("battery.charge", "0")
                temp = data.get("ups.temperature", "N/A")
                
                # Example condition: Print out stats if the UPS load climbs high or drops off battery
                print(f"[{timestamp}] Status: {status} | Load: {load}% ({power}W) | Battery: {charge}% | Temp: {temp}°C")
                
            except json.JSONDecodeError:
                print(f"Skipping malformed data row...")

    print(f"----------------------------------------")
    print(f"Successfully processed {total_entries} total historical logs.")

if __name__ == "__main__":
    analyze_ups_logs()

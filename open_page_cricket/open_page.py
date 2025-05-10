import webbrowser
import time
from datetime import datetime

# 🔗 Set your URL
url = "https://queue.district.in/gstataipl2025cskm63rr8725368"
target_time = "2025-05-08 10:15:01"  # yyyy-mm-dd HH:MM:SS

# ⏳ Wait until the target time
target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")

print(f"Waiting to open {url} at {target}...")

while True:
    now = datetime.now()
    if now >= target:
        print("Opening URL...")
        webbrowser.open(url)
        break
    time.sleep(0.1)
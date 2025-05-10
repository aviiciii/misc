import webbrowser
import time
from datetime import datetime


url = "https://queue.district.in/gstataipl2025cskm63rr8725368"
target_time = "2025-05-08 10:15:00"
target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")

# For macOS
chrome_path = "open -a /Applications/Google\\ Chrome.app %s"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

print(f"Waiting to open {url} in Chrome at {target}...")

while True:
    now = datetime.now()
    if now >= target:
        print("Opening in Chrome...")
        import subprocess
        subprocess.Popen(["open", "-g", "-a", "Google Chrome", url])
        break
    time.sleep(0.1)
import requests

URL = "https://air-quality-monitor-3t55.onrender.com/"

try:
    response = requests.get(URL)
    print(f"Pinged {URL} with status: {response.status_code}")
except Exception as e:
    print(f"Failed to ping: {e}")

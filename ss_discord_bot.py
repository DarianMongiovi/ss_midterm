import requests
import json
from ss_haiku import haiku_formatter


with open("webhook.txt", "r") as f:
    webhook_url = f.read().strip()

haiku_list = haiku_formatter()

full_haiku = "\n".join(haiku_list)

payload = {
    "content": full_haiku
}

response = requests.post(
    webhook_url, 
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)

if response.ok:
    print("Successfully posted the haiku:")
    print(full_haiku)
else:
    print(f"Error {response.status_code}: {response.text}")
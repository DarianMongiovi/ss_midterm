import requests
import json
from ss_haiku import haiku_formatter


try:
    with open("webhook.txt", "r") as f:
        webhook_data = json.load(f)
        webhook_url = webhook_data['url']
except FileNotFoundError:
    print("Error: FileNotFound")
    exit()
except json.JSONDecodeError:
    print("Error: JSON")
    exit()

haiku_list = haiku_formatter()

full_haiku = "\n".join(haiku_list)

payload = {
    "content": full_haiku 
}

try:
    response = requests.post(
        webhook_url,
        json=payload,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    if response.status_code in [200, 204]:
        print("Success!")
        print(full_haiku)
    else:
        print(f"Failed! {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"connection error: {e}")

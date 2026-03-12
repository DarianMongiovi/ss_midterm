import requests
import json
from ss_haiku import haiku_formatter

# 1. Pull the Webhook URL (The "Address")
try:
    with open("webhook.txt", "r") as f:
        # .strip() is vital to remove the hidden '\n' Linux adds to files
        webhook_url = f.read().strip()
except FileNotFoundError:
    print("Error: Could not find webhook.txt in this folder.")
    exit()

# 2. Get your list from the other file
# Expected: ["line 1", "line 2", "line 3"]
haiku_list = haiku_formatter()

# 3. Join them with newlines
full_haiku = "\n".join(haiku_list)

# 4. Create the "Payload" (The "Letter" inside the "Envelope")
# Use "content" for Discord or "text" for Slack
payload = {
    "content": full_haiku 
}

# 5. Send it! 
# We use json=payload here so 'requests' handles the headers for us automatically
try:
    response = requests.post(
        webhook_url, 
        json=payload,
        headers={'User-Agent': 'Mozilla/5.0'} # Helps prevent Linux 'Forbidden' errors
    )

    # 6. Check results
    if response.status_code in [200, 204]:
        print("Success! Haiku posted:")
        print("-" * 20)
        print(full_haiku)
        print("-" * 20)
    else:
        print(f"Failed! Server said: {response.status_code}")
        print(f"Response text: {response.text}")

except Exception as e:
    print(f"A connection error occurred: {e}")text}")

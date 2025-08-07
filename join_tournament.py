import os
import requests

# Get environment variables
token = os.getenv("TOKEN")
tournament_id = os.getenv("TOURNAMENT_ID")

# Validate
if not token or not tournament_id:
    raise ValueError("TOKEN or TOURNAMENT_ID missing!")

# Join tournament
url = f"https://lichess.org/api/tournament/{tournament_id}/join"
headers = {"Authorization": f"Bearer {token}"}

response = requests.post(url, headers=headers)

# Output result
if response.status_code == 200:
    print(f"✅ Successfully joined tournament {tournament_id}")
else:
    print(f"❌ Failed to join tournament {tournament_id}")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

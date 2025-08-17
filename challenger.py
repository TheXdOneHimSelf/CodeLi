import os
import requests
import time

TOKEN = os.getenv("TOKEN")  # Read from GitHub Actions secrets securely

BOT_NAMES = [
    "ToromBot",
    "NimsiluBot",
    "MaggiChess16",
    "Exogenetic-Bot",
    "Endogenetic-Bot",
    "VEER-OMEGA-BOT",
    "Yuki_1324",
    "InvinxibleFlxsh",
    "strain-on-veins"
]  

TOTAL_GAMES = 200
SLEEP_BETWEEN = 60  # Delay between challenges (in seconds)

if not TOKEN:
    raise ValueError("TOKEN environment variable not set!")

def send_challenges():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "clock.limit": 30,        # 30 seconds
        "clock.increment": 0,
        "rated": False,
        "color": "random",
        "variant": "standard"
    }

    for bot in BOT_NAMES:
        print(f"\n--- Challenging {bot} ---\n")
        url = f"https://lichess.org/api/challenge/{bot}"

        for i in range(1, TOTAL_GAMES + 1):
            print(f"Sending challenge {i}/{TOTAL_GAMES} to {bot}...")
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                print(f"  ✅ Challenge {i} sent to {bot}.")
            else:
                print(f"  ❌ Challenge {i} failed for {bot}! Status: {response.status_code} | {response.text}")

            time.sleep(SLEEP_BETWEEN)

if __name__ == "__main__":
    send_challenges()

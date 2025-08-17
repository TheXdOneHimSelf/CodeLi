import os
import requests
import time
import itertools

TOKEN = os.getenv("TOKEN")  # Read from GitHub Actions secrets securely

BOT_NAMES = [
    "NimsiluBot",
    "Exogenetic-Bot",
    "Endogenetic-Bot"
]  

TOTAL_GAMES = 200   # Total number of games overall (not per bot)
SLEEP_BETWEEN = 60  # Delay between accepted challenges (seconds)
WAIT_FOR_ACCEPT = 15 # Seconds to wait if bot might accept

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

    bot_cycle = itertools.cycle(BOT_NAMES)
    sent_games = 0

    while sent_games < TOTAL_GAMES:
        bot = next(bot_cycle)
        url = f"https://lichess.org/api/challenge/{bot}"

        print(f"Sending challenge {sent_games+1}/{TOTAL_GAMES} to {bot}...")
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print(f"  ✅ Challenge sent to {bot}, waiting {WAIT_FOR_ACCEPT}s for acceptance...")
            time.sleep(WAIT_FOR_ACCEPT)
            # Assume accepted if no immediate failure (API won't update instantly)
            sent_games += 1
            time.sleep(SLEEP_BETWEEN)
        else:
            print(f"  ❌ {bot} did not accept / failed! Skipping... Status: {response.status_code} | {response.text}")
            time.sleep(1)  # tiny pause before next bot

if __name__ == "__main__":
    send_challenges()

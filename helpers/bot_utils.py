from pyrogram import Client
from config import BOT_TOKEN  # Keeping BOT_TOKEN from config.py
import time
# Get API_ID and API_HASH from user input
API_ID = int(23605467)
API_HASH = "be7f635e4d9526239beeabbbd0bbd877"

# Initialize bot client
bot = Client(
    "VideoPlayer",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)

# print("API_ID:", API_ID, "API_HASH:", API_HASH, "BOT_TOKEN:", BOT_TOKEN)
# time.sleep(2)

# Start bot and get bot info
with bot:
    ok = bot.get_me()
    print(ok)
    USERNAME = ok.username
    BOT_NAME = ok.first_name

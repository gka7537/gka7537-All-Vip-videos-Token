import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "")
BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", 0))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
# Agar ek se zyada admin hain, to comma lagayein (e.g., 12345,67890)
ADMINS = [int(x) for x in os.environ.get("ADMINS", "0").split(",")]
PORT = int(os.environ.get("PORT", 10000))


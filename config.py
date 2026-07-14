import os

# Render se variable read karne ka code
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "")
# Agar ek se zyada admin hain, to comma lagayein (e.g., 12345,67890)
ADMINS = [int(x) for x in os.environ.get("ADMINS", "0").split(",")]
PORT = int(os.environ.get("PORT", 10000))


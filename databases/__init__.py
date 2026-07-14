
from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URI, DATABASE_NAME

# MongoDB Client
client = AsyncIOMotorClient(DATABASE_URI)

# Database
db = client[DATABASE_NAME]

# Collections
users = db["users"]
admins = db["admins"]
files = db["files"]
albums = db["albums"]
verify = db["verify"]
settings = db["settings"]

# Export
__all__ = [
    "client",
    "db",
    "users",
    "admins",
    "files",
    "albums",
    "verify",
    "settings",
]

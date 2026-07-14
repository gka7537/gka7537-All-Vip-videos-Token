from motor.motor_asyncio import AsyncIOMotorClient
import datetime

# MongoDB connection (Isse config.py se load karna behtar hota hai)
client = AsyncIOMotorClient("YOUR_MONGODB_URI") 
db = client["bot_database"]
users = db["users"]

async def add_user(user_id):
    user = await users.find_one({"user_id": user_id})
    if not user:
        await users.insert_one({
            "user_id": user_id,
            "verified_at": None
        })

async def set_verify(user_id):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"verified_at": datetime.datetime.now()}}
    )

async def is_verified(user_id):
    user = await users.find_one({"user_id": user_id})
    if user and user.get("verified_at"):
        # Check if 24 hours have passed
        if datetime.datetime.now() - user["verified_at"] < datetime.timedelta(hours=24):
            return True
    return False
    

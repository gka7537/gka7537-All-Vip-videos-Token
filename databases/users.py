from database import db
import time # Ise upar import mein add karein

async def get_user_data(user_id):
    return await db.users.find_one({"user_id": user_id})

async def update_user_verification(user_id, timestamp):
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"verify_time": timestamp}},
        upsert=True
    )

# --- Yahan se naya code add karein ---
async def set_access_expiry(user_id):
    # 1 ghanta = 3600 seconds
    expiry = time.time() + 3600
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"access_expiry": expiry}},
        upsert=True
    )

async def has_access(user_id):
    user = await get_user_data(user_id)
    if user and user.get("access_expiry", 0) > time.time():
        return True
    return False

    

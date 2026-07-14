from database import db

async def get_user_data(user_id):
    return await db.users.find_one({"user_id": user_id})

async def update_user_verification(user_id, timestamp):
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"verify_time": timestamp}},
        upsert=True
    )
    

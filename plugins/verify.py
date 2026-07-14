import time
from pyrogram import Client, filters
from database.users import get_user_data, update_user_verification, set_access_expiry

# Verification ka samay (24 ghante = 86400 seconds)
VERIFY_TIME = 86400 

async def check_verification(user_id):
    user = await get_user_data(user_id)
    if not user:
        return False
    
    last_verify = user.get("verify_time", 0)
    if (time.time() - last_verify) < VERIFY_TIME:
        return True # Verified hai
    return False # Dobara verify karna hoga

# Jab user link par click kare (Callback)
@Client.on_callback_query(filters.regex("verify_now"))
async def verify_callback(client, callback_query):
    user_id = callback_query.from_user.id
    
    # 1. 24-ghante ka verification update karein
    await update_user_verification(user_id, time.time())
    
    # 2. 1-ghante ka file access bhi set karein (Naya add kiya)
    await set_access_expiry(user_id)
    
    await callback_query.answer("Verification successful! Aapko 24 ghante ka access mil gaya hai.", show_alert=True)
    

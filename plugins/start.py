from pyrogram import Client, filters, types
from plugins.verify import check_verification
from database.users import has_access # Yeh import zaroor add karein

@Client.on_message(filters.command("start") & filters.regex("file_"))
async def start_handler(client, message):
    user_id = message.from_user.id
    
    # 1. Pehle 24-ghante ka verification check karein
    is_verified = await check_verification(user_id)
    
    # 2. Phir 1-ghante ka access check karein
    has_active_access = await has_access(user_id)
    
    if is_verified and has_active_access:
        # Access valid hai - file bhej do
        await message.reply("Aap verified hain! Ye rahi aapki file...")
    else:
        # Ya to verify nahi hain, ya 1 ghanta khatam ho gaya
        await message.reply(
            "File dekhne ke liye pehle verify karein.",
            reply_markup=types.InlineKeyboardMarkup([
                [types.InlineKeyboardButton("Verify Now", callback_data="verify_now")]
            ])
        )
        

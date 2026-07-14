from pyrogram import Client, filters
from plugins.verify import check_verification

@Client.on_message(filters.command("start") & filters.regex("file_"))
async def start_handler(client, message):
    user_id = message.from_user.id
    
    # 24-hour verification check
    is_verified = await check_verification(user_id)
    
    if is_verified:
        # File send karein
        await message.reply("Aap verified hain! Ye rahi aapki file...")
    else:
        # User ko Shortlink verification par bhejein
        await message.reply("File dekhne ke liye pehle 24-hour verification complete karein.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Verify Now", callback_data="verify_now")]
            ]))
      

from pyrogram import Client, filters, types

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply(
        "Bot chal raha hai! Verification ke liye click karein...",
        reply_markup=types.InlineKeyboardMarkup([[
            types.InlineKeyboardButton("Verify Now", callback_data="verify_now")
        ]])
    )
    

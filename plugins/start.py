from pyrogram import Client, filters, types

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply(
        "Welcome to my bot!",
        reply_markup=types.InlineKeyboardMarkup([[
            types.InlineKeyboardButton("Verify Now", callback_data="verify_now")
        ]])
    )
    

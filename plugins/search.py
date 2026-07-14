from pyrogram import Client, filters
from database.files import get_files_by_name # Aapke database function ka naam
from config import ADMINS # config.py mein admins ki list define honi chahiye

@Client.on_message(filters.command("search") & filters.user(ADMINS))
async def search_file(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /search <file_name>")
        return

    query = message.command[1]
    files = await get_files_by_name(query)
    
    if not files:
        await message.reply("File nahi mili.")
        return

    # Link generation logic
    for file in files:
        # File ka metadata: Name + Size
        file_name = file.get("name", "Unknown")
        file_size = file.get("size", "0 MB")
        
        # Link generator (Apne bot ka username ya shortener link add karein)
        # Agar album_id hai to pura album link, varna single file
        link = f"https://t.me/{client.me.username}?start=file_{file['_id']}"
        
        response = f"**Name:** {file_name}\n**Size:** {file_size}\n\n[Link Click Here]({link})"
        
        # File ka thumbnail agar store kiya hai
        if file.get("thumbnail_id"):
            await message.reply_photo(photo=file["thumbnail_id"], caption=response)
        else:
            await message.reply(response)



from pyrogram import Client, filters
from database.files import save_file 
from utils.thumbnail import get_thumbnail

@Client.on_message(filters.document | filters.video)
async def upload_file(client, message):
    # File details extract karein
    file = message.document or message.video
    file_name = file.file_name
    file_size = round(file.file_size / (1024 * 1024), 2) # MB mein
    
    # Database mein save karein
    file_id = await save_file(file_name, file.file_id, file_size)
    
    # Auto link generate karein
    link = f"https://t.me/{client.me.username}?start=file_{file_id}"
    
    # Notice: File ke niche message
    caption = f"**File Name:** {file_name}\n**Size:** {file_size} MB\n\n[Click here for link]({link})\n\n*(Note: Is file ka access sirf 1 ghante tak rahega.)*"
    
    await message.reply(caption)
  

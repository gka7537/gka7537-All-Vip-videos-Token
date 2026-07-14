from database import db

async def save_file(file_data, media_group_id=None):
    # Agar media_group_id hai, to ek hi album mein save karein
    data = {
        "file_id": file_data.file_id,
        "name": file_data.file_name,
        "size": file_data.file_size,
        "media_group_id": media_group_id  # Ye album ke liye hai
    }
    await db.files.insert_one(data)
  

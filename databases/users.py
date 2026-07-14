from datetime import datetime

from . import users


async def add_user(user_id: int, first_name: str = "", username: str = ""):

    user = await users.find_one({"_id": user_id})

    if user:
        return False

    data = {
        "_id": user_id,
        "first_name": first_name,
        "username": username,
        "joined_date": datetime.utcnow(),
        "verified": False,
        "verify_expire": 0
    }

    await users.insert_one(data)

    return True


async def get_user(user_id: int):

    return await users.find_one({"_id": user_id})


async def is_user_exist(user_id: int):

    user = await users.find_one({"_id": user_id})

    return bool(user)


async def delete_user(user_id: int):

    await users.delete_one({"_id": user_id})


async def total_users():

    return await users.count_documents({})


async def get_all_users():

    async for user in users.find({}):

        yield user


async def update_verify(user_id: int, expire_time: int):

    await users.update_one(
        {"_id": user_id},
        {
            "$set": {
                "verified": True,
                "verify_expire": expire_time
            }
        }
    )


async def remove_verify(user_id: int):

    await users.update_one(
        {"_id": user_id},
        {
            "$set": {
                "verified": False,
                "verify_expire": 0
            }
        }
    )

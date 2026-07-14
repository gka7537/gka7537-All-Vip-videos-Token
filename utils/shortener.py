import aiohttp

async def get_shortlink(url):
    api_url = "YOUR_SHORTLINK_API_URL" # Jaise Ouo.io, Exe.io etc.
    api_key = "YOUR_API_KEY"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}?api={api_key}&url={url}") as resp:
            data = await resp.json()
            return data.get("shortenedUrl", url) # Error par original url return hoga
          

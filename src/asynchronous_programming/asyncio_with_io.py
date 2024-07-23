import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def main():
    urls=["https://www.google.com","https://www.facebook.com","https://www.x.com",]
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result[:100])

asyncio.run(main())
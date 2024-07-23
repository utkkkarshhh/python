import asyncio
import aiohttp

async def fetch_user(session, user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    async with session.get(url) as response:
        return await response.json()
    
async def fetch_users():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for user_id in range(1, 11):
            tasks.append(fetch_user(session, user_id))
            
        users = await asyncio.gather(*tasks)
        return users
    
async def main():
    users = await fetch_users()
    for user in users:
        print(user)
        
asyncio.run(main())


    

    
# import requests
# from bs4 import BeautifulSoup

# def fetch_webpage_title(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         title = soup.title.string
#         return title
#     else:
#         return None

# if __name__ == "__main__":
#     url = "https://www.google.com"
#     title = fetch_webpage_title(url)
#     if title:
#         print(f"Title of the web page is: {title}")
#     else:
#         print("Failed to retrieve the web page.")


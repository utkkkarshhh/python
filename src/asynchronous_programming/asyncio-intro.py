import asyncio

async def sayHello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    
async def main():
    await asyncio.gather(sayHello())
    
asyncio.run(main())
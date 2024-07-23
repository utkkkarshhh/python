import asyncio

async def hello(name):
    print("Hello")
    await asyncio.sleep(1)
    print(f"World to {name}")
    
async def main():
    task1 = asyncio.create_task(hello("Utkarsh"))
    task2 = asyncio.create_task(hello("Ram"))
    
    await task1
    await task2
    
asyncio.run(main())
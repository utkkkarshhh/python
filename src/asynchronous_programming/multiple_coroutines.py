import asyncio

async def greet(name):
    print("Hello")
    await asyncio.sleep(1)
    print(f"World to {name}")
    
async def bye(name):
    print("Goodbye")
    await asyncio.sleep(2)
    print(f"World to {name}")
    
async def main():
    await asyncio.gather(greet("Utkarsh"), bye("Utkarsh"))
    
asyncio.run(main())
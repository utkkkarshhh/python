import asyncio

async def may_fail():
    await asyncio.sleep(5)
    raise ValueError("An Error Occurred")

async def main():
    try:
        await may_fail()
    except ValueError as e:
        print(f"Error Occured: {e}")
        
asyncio.run(main())
import asyncio

async def main():
    print('Tim')
    task = asyncio
    await foo('text')

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    # await only inside async funciton, 

asyncio.run(main())
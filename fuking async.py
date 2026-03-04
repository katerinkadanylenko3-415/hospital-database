#1
import asyncio

async def async_counter(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)

async def main():
    await async_counter(5)

asyncio.run(main())

#2
import asyncio

async def download_file_1():
    await asyncio.sleep(3)
    print("File 1 downloaded")

async def download_file_2():
    await asyncio.sleep(2)
    print("File 2 downloaded")

async def download_file_3():
    await asyncio.sleep(1)
    print("File 3 downloaded")

async def main():
    await asyncio.gather(
        download_file_1(),
        download_file_2(),
        download_file_3()
    )

asyncio.run(main())

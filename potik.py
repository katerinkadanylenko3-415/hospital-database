'''
import os
import threading
import time
from queue import Queue

class FileWorker(threading.Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        time.sleep(0.1)
        results = len(self.name)
        self.queue.put((self.name, results))

result = {}
threads = []

files = ['a', 'b', 'c', 'd']
queue = Queue()

for f in files:
    t = FileWorker(f, queue)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

while not queue.empty():
    key, value = queue.get()
    result[key] = value

print(result)

counter = 0
'''

import asyncio
import random
import time


async def task(name):
    print(f"{name} starts")
    await asyncio.sleep(2)
    print(f"{name} ends")


async def hello(name):
    print(f"{name} starts")
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    print(f"Hllo , {name}, wait {delay}")

import requests
import aiohttp


urls = ['https://mystat.itstep.org/homework/done', 'https://music.youtube.com/watch?v=s0ig07MRW4A&list=PLQ6XAbcjjt_e6VD5MjGGbzkuDsI81iNUf']
start = time.time()
for url in urls:
    r = requests.get(url)
    print(f"get {len(r.text)} symbols")

print("time: ", time.time()-start)

async def getUrl(session, url):
    async with session.get(url) as response:
        text = await response.text()
        print(f"get {len(text)} symbols")
        return text


async def main():
    # names = ['Bill', 'Pop', 'Nik']
    # tasks = [hello(n) for n in names]
    # await asyncio.gather(*tasks)
    global urls
    async with aiohttp.ClientSession() as session:
        task = [getUrl(session, url) for url in urls]
        await asyncio.gather(*task)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f"time: {time.time()-start}")


import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp

local_hash = "your_local_hash"


def hash_and_compare(s):
    # Replace with your hash function
    import hashlib

    return hashlib.sha256(s.encode()).hexdigest() == local_hash


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        with ProcessPoolExecutor() as pool:
            while True:
                s = await fetch(session, url)
                match = await asyncio.get_event_loop().run_in_executor(
                    pool, hash_and_compare, s
                )
                if match:
                    print(f"Match found: {s}")
                    break


asyncio.run(main("https://your-api-endpoint"))

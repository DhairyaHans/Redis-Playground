from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

data = {
    "model": "Deimos",
    "brand": "Ergonom",
    "type": "Enduro bikes",
    "price": 4972,
}

def hashSet_functions():
    client.hset("bikes:2", mapping=data)
    print(client.hget("bikes:2", "model"))
    print(client.hgetall("bikes:2"))
    client.hincrby("bikes:2", "price", 200)
    print(client.hmget("bikes:2", ["model", "price"]))
    
async def main():
    await loop.run_in_executor(_executor, hashSet_functions)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
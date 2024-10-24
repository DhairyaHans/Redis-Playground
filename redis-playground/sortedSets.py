from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

def sortedSet_add():
    client.zadd("score", {"Dhairya": 10})
    client.zadd("score", {"ABC": 1})
    client.zadd("score", {"XVT": 2})
    client.zadd("score", {"oioi": 7})
    print(client.zrange("score", 0, -1))
    print(client.zrevrange("score", 0, -1))
    print(client.zrank("score", "oioi"))
        
async def main():
    await loop.run_in_executor(_executor, sortedSet_add)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
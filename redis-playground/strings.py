from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(2)

def redis_get():
    data = client.get("msg:6")
    return data

def redis_set():
    client.set("msg:6", "Hll from XXX")
    
def redis_expire():
    client.expire("msg:6", 10)
    
async def main():
    # await loop.run_in_executor(_executor, redis_set)
    # await loop.run_in_executor(_executor, redis_expire)
    data = await loop.run_in_executor(_executor, redis_get)
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
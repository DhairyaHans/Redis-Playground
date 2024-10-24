from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

def redis_functions():
    # client.lpush("messages", 1)
    # client.lpush("messages", 2)
    # client.lpush("messages", 3)
    # client.lpush("messages", 4)
    print(client.lpop("messages"))
    
async def main():
    await loop.run_in_executor(_executor, redis_functions)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
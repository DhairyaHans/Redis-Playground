from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

def setAdd():
    client.sadd("ips", 1)
    client.sadd("ips", 2)
    client.sadd("ips", 3)
    client.sadd("ips", 4)

def setRemove():
    client.srem("ips", 2)
        
async def main():
    await loop.run_in_executor(_executor, setAdd)
    # await loop.run_in_executor(_executor, setRemove)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
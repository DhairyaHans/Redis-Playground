from ClientCode.client_code import client
import asyncio

from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

def redis_stream():
    # time_id = client.xadd("race:france", 
    #                         {"rider": "Prickett", "speed": 29.7, "position": 2, "location_id": 1}
    #                     )
    # print(time_id)
    print(client.xrange("race:france", '-', '+', count=10))
    print(client.xlen("race:france"))
    # print(client.xread(streams={"race:france": '1729429863533-0'}, count=10, block=10000))


async def main():
    await loop.run_in_executor(_executor, redis_stream)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

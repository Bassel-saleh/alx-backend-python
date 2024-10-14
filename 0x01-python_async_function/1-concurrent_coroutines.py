#!/usr/bin/env python3
''' module for task#1 '''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    '''
        return random wait_time n times
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)

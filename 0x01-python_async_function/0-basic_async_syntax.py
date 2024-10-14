#!/usr/bin/env python3
''' module for task#0 '''
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    '''
        wait and then return a random number between 0 and max_delay
    '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

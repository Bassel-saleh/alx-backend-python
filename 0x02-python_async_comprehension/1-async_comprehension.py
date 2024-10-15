#!/usr/bin/env python3
''' module for task#1 '''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        The coroutine will collect 10 random numbers
        using an async comprehensing over async_generator
    '''
    return [number async for number in async_generator()]

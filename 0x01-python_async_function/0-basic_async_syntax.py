#!/usr/bin/env python3
"""
waits for a random delay between 0 and max_delay
seconds and eventually returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i

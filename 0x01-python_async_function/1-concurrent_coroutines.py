#!/usr/bin/env python3
"""
pawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    pawn wait_random n times with the specified max_delay.
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays

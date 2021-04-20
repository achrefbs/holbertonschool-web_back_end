#!/usr/bin/env python3
"""
collect 10 random numbers using an async comprehensing over async_generator
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async comprehensing over async_generator
    """
    return [x async for x in async_generator()]

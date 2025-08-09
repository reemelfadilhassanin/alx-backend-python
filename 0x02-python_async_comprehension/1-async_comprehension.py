#!/usr/bin/env python3
"""This module contains a coroutine"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension.

    This coroutine uses async comprehension to gather values yielded from
    async_generator and returns a list of these values.
    """
    return [number async for number in async_generator()]

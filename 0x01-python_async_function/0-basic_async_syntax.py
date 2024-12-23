#!/usr/bin/env python3
"""This modules for async
    """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time waited.
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number

#!/usr/bin/env python3
"""This wait_n and alter it into a
 new function task_wait_n
    """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay,
    and returns a list of all the delays in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the delays sorted in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

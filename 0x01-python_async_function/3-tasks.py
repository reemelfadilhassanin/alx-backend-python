#!/usr/bin/env python3
"""this for tasks
    """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio Task object for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

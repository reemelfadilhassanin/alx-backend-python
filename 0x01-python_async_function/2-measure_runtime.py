#!/usr/bin/env python3
"""This measure _runtime
    """
import asyncio
import time
from typing import Any
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time taken for each call to wait_n.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    total_time = time.time() - start_time  # Calculate total elapsed time

    return total_time / n  # Return average time per call

#!/usr/bin/env python3
"""This module measures the runtime
of async_comprehension executed in parallel."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of executing
    async_comprehension four times in parallel.

    This coroutine uses asyncio.gather to
    run async_comprehension four times concurrently
    and returns the total runtime.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time

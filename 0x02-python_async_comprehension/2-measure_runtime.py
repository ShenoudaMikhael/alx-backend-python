#!/usr/bin/env python3
"""measure_runtime Module"""

import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """measure_runtime function"""
    start = time()
    await asyncio.gather(
        *[
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
        ]
    )
    delta = time() - start
    return delta

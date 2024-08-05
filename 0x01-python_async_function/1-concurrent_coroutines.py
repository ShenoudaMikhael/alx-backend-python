#!/usr/bin/env python3
"""concurrent Module"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n function"""
    q = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(q)

#!/usr/bin/env python3
"""concurrent Module"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait n function"""
    q = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    return sorted(q)

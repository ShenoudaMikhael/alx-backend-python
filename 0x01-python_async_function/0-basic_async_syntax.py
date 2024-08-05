#!/usr/bin/env python3
"""Basic Module"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """COUNT"""
    q: float = random.uniform(0, max_delay)
    await asyncio.sleep(q)
    return q

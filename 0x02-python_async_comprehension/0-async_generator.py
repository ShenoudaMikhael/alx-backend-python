#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """async_generator function"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10

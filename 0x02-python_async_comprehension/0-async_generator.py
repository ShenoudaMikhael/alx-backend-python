#!/usr/bin/env python3
"""Async Generator"""
import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, typing.Any, typing.Any]:
    """async_generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""Async Generator"""
import random
import typing


async def async_generator() -> typing.Any:
    """async_generator function"""
    for _ in range(10):
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""Tasks Module"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task wait function"""
    return asyncio.create_task(wait_random(max_delay))

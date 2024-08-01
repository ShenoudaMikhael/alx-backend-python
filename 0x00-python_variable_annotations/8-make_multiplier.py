#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""
    return lambda x: x * multiplier

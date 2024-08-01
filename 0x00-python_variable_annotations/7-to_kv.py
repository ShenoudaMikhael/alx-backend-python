#!/usr/bin/env python3
"""to_kv List module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv function"""
    return k, v * v

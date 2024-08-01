#!/usr/bin/env python3
"""SUM Mixed List module"""
from typing import List, Union


def mxd_lst(mxd_lst: List[Union[int, float]]) -> float:
    """mxd_lst function"""
    q: float = 0.0
    for a in mxd_lst:
        q += a
    return q

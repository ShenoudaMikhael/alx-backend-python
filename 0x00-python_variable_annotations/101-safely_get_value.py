#!/usr/bin/env python3
"""Module"""

from typing import TypeVar, Mapping, Union, Any

T = TypeVar("T")


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None):
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default

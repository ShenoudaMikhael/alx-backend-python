#!/usr/bin/env python3
"""Defines duck typed function"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[any]) -> Union[Any, None]:
    """safe_first_element function
    The types of the elements of the input are not know
    """
    if lst:
        return lst[0]
    else:
        return None

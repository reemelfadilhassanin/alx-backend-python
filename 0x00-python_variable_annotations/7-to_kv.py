#!/usr/bin/env python3
"""
This module to create a tuple from a string and a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string and the square of the number.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of
        the number.
    """
    return (k, float(v ** 2))

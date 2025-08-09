#!/usr/bin/env python3
"""
This module to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the multiplier.
    """

    def multiply(x: float) -> float:
        """Multiply x by the multiplier."""
        return x * multiplier

    return multiply

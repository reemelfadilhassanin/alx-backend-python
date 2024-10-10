#!/usr/bin/env python3
"""
This module to zoom in on an array
"""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zoom into a list by a specified factor.

    Args:
        lst (List[int]): The list of integers to zoom in on.
        factor (int, optional): The factor by which to zoom. Defaults to 2.

    Returns:
        List[int]: A new list containing the zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

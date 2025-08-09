#!/usr/bin/env python3
"""
This module to sum a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all the integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))

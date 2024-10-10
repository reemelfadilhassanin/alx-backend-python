#!/usr/bin/env python3
"""
This module to safely get the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence or None if is empty.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: The first element of the sequence or None if it
        is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

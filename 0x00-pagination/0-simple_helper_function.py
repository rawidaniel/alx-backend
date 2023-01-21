#!/usr/bin/env python3
"""
Module 0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Parameters
    ---------
    page: int
        the start of pagination
    page_size: int
        the maximum number of object returned

    Returns
    -------
    Tuple
        tuple holding the beginning and ending page numbers
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)

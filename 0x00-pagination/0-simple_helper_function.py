#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""


def index_range(page, page_size):
    """
    function named index_range that takes
    two integer arguments page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index

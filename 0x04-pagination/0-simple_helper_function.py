#!/usr/bin/env python3
"""
0x04-pagination
"""


def index_range(page, page_size):
    """ Simple helper function mandatory
    """
    currentIndex = (page - 1) * page_size
    return(currentIndex, currentIndex + page_size)

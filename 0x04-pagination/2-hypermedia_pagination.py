#!/usr/bin/env python3
"""
0x04-pagination
"""

import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page
        """

        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        if page_size * page > len(self.dataset()):
            return []

        indexRange = index_range(page, page_size)
        DataSet = self.dataset()
        return(DataSet[indexRange[0]:indexRange[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get_hyper
        """
        data = self.dataset()

        maxPages = math.ceil(len(data) / page_size)

        return ({
            'page_size': page_size if maxPages >= page else 0,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if maxPages >= page + 1 else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': maxPages
        })

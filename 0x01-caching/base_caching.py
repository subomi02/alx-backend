#!/usr/bin/env python3
"""Adetunji Olasubomi
"""


class BaseCaching():
    """
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        """
        self.cache_data = {}

    def print_cache(self):
        """
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)

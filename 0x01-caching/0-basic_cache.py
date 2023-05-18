#!/usr/bin/python3
"""Adetunji Olasubomi
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    """
    def put(self, key, item):
        """
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        """
        return self.cache_data.get(key, None)

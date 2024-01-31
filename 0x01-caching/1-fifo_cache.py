#!/usr/bin/env python3
"""
1-fifo_cache.py
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from,
    BaseCaching and is a caching system
    """

    def __init__(self):
        """
        the FIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an items from the cache
        """
        if key is not None:
            return self.cache_data.get(key, None)

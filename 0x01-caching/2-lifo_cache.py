#!/usr/bin/env python3
"""
2-lifo_cache.py
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from,
    BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        the LIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key, None)

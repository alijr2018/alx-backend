#!/usr/bin/env python3
"""
4-mru_cache.py
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching,
    and is a caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
                self.access_order.insert(0, key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    mru_key = self.access_order.pop(0)
                    del self.cache_data[mru_key]
                    print("DISCARD:", mru_key)

                self.cache_data[key] = item
                self.access_order.insert(0, key)

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.insert(0, key)
            return self.cache_data[key]
        return None

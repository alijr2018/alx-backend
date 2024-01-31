#!/usr/bin/env python3
"""
3-lru_cache.py
"""

from datetime import datetime
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching,
    and is a caching system
    """

    def __init__(self):
        """
        the LRUCache instance
        """
        super().__init__()
        self.lru_tracker = OrderedDict()

    def put(self, key, item):
        """
        Add an items to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.lru_tracker.popitem(last=False)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.lru_tracker[key] = datetime.now()

    def get(self, key):
        """
        Get an items from the cache
        """
        if key is not None and key in self.cache_data:
            self.lru_tracker[key] = datetime.now()
            return self.cache_data[key]
        return None

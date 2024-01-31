#!/usr/bin/env python3
"""
4-mru_cache.py
"""

from datetime import datetime
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from,
    BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        the MRUCache instance
        """
        super().__init__()
        self.mru_tracker = OrderedDict()

    def put(self, key, item):
        """
        Add item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru_tracker.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key, _ = self.mru_tracker.popitem(last=False)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.mru_tracker[key] = datetime.now()

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.mru_tracker.move_to_end(key)
            return self.cache_data[key]
        return None

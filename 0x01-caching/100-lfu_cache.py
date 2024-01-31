#!/usr/bin/env python3
"""
100-lfu_cache.py
"""

from datetime import datetime
from collections import OrderedDict
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from BaseCaching,
    and is a caching system.
    """

    def __init__(self):
        """
        the LFUCache instance
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.timestamp = {}

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [
                    k for k, v in self.frequency.items() if v == min(
                        self.frequency.values())]

                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.timestamp[k])
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    del self.timestamp[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    lfu_key = lfu_keys[0]
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    del self.timestamp[lfu_key]
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.frequency[key] += 1
            self.timestamp[key] = datetime.now()

    def get(self, key):
        """ Get an item from the cache """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.timestamp[key] = datetime.now()
            return self.cache_data[key]
        return None

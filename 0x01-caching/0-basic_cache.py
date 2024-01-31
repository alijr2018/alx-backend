#!/usr/bin/env python3
"""
0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from,
    BaseCaching and is a caching system.
    """

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key, None)

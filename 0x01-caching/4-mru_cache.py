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
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """
        Add item to the cache
        """
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """ MRU algorithm, remove element """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def add_to(self, key, item):
        """
        add
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            self._remove(self.prev[self.tail])
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

    def put_to(self, key, item):
        """
        put to dictionary
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self.add_to(key, item)

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self.add_to(key, value)
            return value

#!/usr/bin/env python3
"""
 LFU Caching module which inherits from
 BaseCaching and is a caching system
 """

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFU Caching system
    """
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.lfu_count = {}

    def put(self, key, item):
        """ Add an item in the cache
        args:
            key - key of the item in the cache
            item - value of the item in the cache
        return:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_items = []
            for k, v in self.frequency.items():
                if v == min(self.frequency.values()):
                    lfu_items.append(k)
            lru_item = min(lfu_items, key=lambda k: self.lfu_count.get(k, 0))
            del self.cache_data[lru_item]
            del self.frequency[lru_item]
            print("DISCARD:", lru_item)

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.lfu_count[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.lfu_count[key] += 1
        return self.cache_data[key]

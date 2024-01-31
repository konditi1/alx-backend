#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching
and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.pop(key)
                else:
                    print("DISCARD: {}".format(list(self.cache_data.keys())[0])
                          )
                    self.cache_data.pop(list(self.cache_data.keys())[0])
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key, None)

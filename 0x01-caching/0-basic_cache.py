#!/usr/bin/env python3
"""
BasicCache which inherits from BaseCaching
and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        arg:
            key - key of the item in the cache
            item - value of the item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        arg:
            key - key of the item in the cache
        return:
          - the value in the cache linked to the key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key, None)

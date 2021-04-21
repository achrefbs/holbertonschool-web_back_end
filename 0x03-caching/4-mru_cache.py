#!/usr/bin/python3
"""
class MRUCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching and is a caching system
    """

    QUEUE = []

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def updateQueue(self, KeyToRemove, KeyToAppend):
        """ update queue
        """
        self.__class__.QUEUE.remove(KeyToRemove)
        self.__class__.QUEUE.append(KeyToAppend)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (not key or not item):
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.updateQueue(key, key)
            else:
                last = len(self.__class__.QUEUE) - 1
                print("DISCARD: {}".format(self.__class__.QUEUE[last]))
                keyToDelete = self.__class__.QUEUE[last]
                del self.cache_data[keyToDelete]
                self.cache_data[key] = item
                self.updateQueue(keyToDelete, key)

        else:

            self.cache_data[key] = item
            self.__class__.QUEUE.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        self.updateQueue(key, key)
        return self.cache_data[key]

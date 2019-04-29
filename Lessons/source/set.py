#!python
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """ Initialize this set """

        self.size = 0
        self.items = HashTable()
        # Adding elements to the hashtable if elements is not none
        if elements is not None:
            for element in elements:
                self.items.set(element, element)

    def __iter__(self):
        for item in self.items.keys():
            yield item

    def contains(self, element):
        """ Return true if the element is in the set or false if is not """
        return self.items.contains(element)
    
    def add(self, element):
        """ Add an element to the set """
        self.items.set(element, element)
        self.size += 1

    def remove(self, element):
        """ Delete an element from the set """
        self.items.delete(element)
        self.size -= 1

    def length(self):
        """ Return the size of the set """
        return self.items.length()

    def union(self, other_set):
        """ Return the combination of elements in both sets """
        return list(dict.fromkeys(self.items.keys() + other_set.items.keys()))

    def intersection(self, other_set):
        """ Return the intersection between two sets """ 
        intersection = list()

        for key in self.items.keys():
            if key in other_set.items.keys():
                intersection.append(key)
        return intersection

    def difference(self, other_set):
        """ Return elements that are not in other_set """
        result = Set()
        intersection = self.intersection(other_set)

        for key in self.items.keys():
            if key not in intersection:
                result.add(key)
        return result

    def is_subset(self, other_set):
        """ return true if other set is a subset of this set and false if it isn't """
        for key in other_set.items.keys():
            if not self.contains(key):
                return False
        return True

    
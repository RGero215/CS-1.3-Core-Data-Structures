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
        for item in self.items:
            yield item
    
    def get_items(self):
        """returns a list of all items in the set"""
        all_items = []
        for item in self.items:
            all_items.append(item.data[0])
        return all_items

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
        new_set = Set()
        for item in self.items:
            new_set.add(item.data[0])
        for item in other_set.items:
            new_set.add(item.data[0])
        return new_set

    def intersection(self, other_set):
        """ Return the intersection between two sets """ 
        new_set = Set()
        for item in self.items.values():
            if other_set.contains(item):
                new_set.add(item)
        print("Intersection", new_set.items)
        return new_set

    def difference(self, other_set):
        """ Return elements that are not in other_set """
        new_set = Set()
        intersection = self.intersection(other_set)
        for item in self.items:
            if not intersection.contains(item.data[0]):
                new_set.add(item.data[0])
        return new_set

    def is_subset(self, other_set):
        """ return true if other set is a subset of this set and false if it isn't """
        for item in other_set:
            if not self.contains(item.data[0]):
                return False
        return True

if __name__ == "__main__":
    test_set = Set(['A','B','C','D','E'])
    other_set = Set(['C','D','E','F','G'])
    intersection = test_set.intersection(other_set)
    (intersection, ['C', 'D', 'E'])

    
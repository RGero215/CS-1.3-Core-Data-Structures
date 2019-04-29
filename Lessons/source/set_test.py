from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['A','B','C','D','E'])
        assert test_set.length() == 5
        assert test_set.contains('A') == True
        assert test_set.contains('C') == True
        assert test_set.contains('E') == True

    def test_contains(self):
        test_set = Set(['A','B','C','D','E'])
        assert test_set.length() == 5
        assert test_set.contains('A') == True
        assert test_set.contains('B') == True
        assert test_set.contains('C') == True
        assert test_set.contains('D') == True
        assert test_set.contains('E') == True
        assert test_set.contains('F') == False
        assert test_set.contains('Z') == False

    def test_add(self):
        test_set = Set()
        assert test_set.length() == 0
        test_set.add('A')
        assert test_set.contains('A') == True
        test_set.add('B')
        assert test_set.contains('B') == True
        test_set.add('C')
        assert test_set.contains('C') == True
    
    def test_remove(self):
        test_set = Set(['A','B','C'])
        assert test_set.length() == 3
        test_set.remove('A')
        assert test_set.length() == 2
        assert test_set.contains('A') == False 
        test_set.remove('B')
        assert test_set.length() == 1
        assert test_set.contains('B') == False
        test_set.remove('C')
        assert test_set.length() == 0
        assert test_set.contains('C') == False

    def test_union(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        unions = test_set.union(other_set)
        self.assertCountEqual(unions, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_intersection(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        intersection = test_set.intersection(other_set)
        self.assertCountEqual(intersection, ['C', 'D', 'E'])

    def test_difference(self):
        test_set = Set(['A','B','C','D','E'])
        other_set = Set(['C','D','E','F','G'])
        difference = test_set.difference(other_set)
        self.assertCountEqual(difference, ['A','B'])

    def test_is_subset(self):
        test_set = Set(['A','B','C','D','E'])
        subset = Set(['B','C'])
        assert test_set.is_subset(subset) == True
        subset = Set([1,2,3])
        assert test_set.is_subset(subset) == False
        subset = Set(['D', 'E'])
        assert test_set.is_subset(subset) == True
        

if __name__ == '__main__':
    unittest.main()

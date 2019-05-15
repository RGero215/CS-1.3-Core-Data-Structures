from numbers_prefix_cost import *
import timeit

CHILDREN_SIZE = 10

class Node:
    def __init__(self, data):
        self.data = data
        self.children = [None for _ in range(CHILDREN_SIZE)]
        self.leaf = False

class Trie:
    def __init__(self):
        # The root node is an empty node we are using +
        self.root = Node('+')

    def insert(self, numbers, cost):
        path = []
        # Start at the root node
        current = self.root
        # Numbers is a string of numbers and number is a char number
        for number in numbers:
            # We use ascii representation to get the index and transfer within the range
            # [0, CHILDREN_SIZE - 1]
            ascii_index = ord(number)-ord('0')
            # Check if theres a child with given number
            if current.children[ascii_index]:
                # Keep going
                current = current.children[ascii_index]
                path.append(current.data)
            else:
                # Insert a new node
                node = Node(number)
                current.children[ascii_index] = node
                current = node
                path.append(current.data)

        # leaf nodes represent the end of the words in the tree
        current.data = (''.join(path), cost)
        current.leaf = True
        # print("Current Data", current.data)

        

    def search(self, numbers):
        # if the tree is empty
        if not self.root.children:
            return False
        # start with the root node
        current = self.root
        # consider all the root node
        for number in numbers:
            ascii_index = ord(number)-ord('0')
            # check if number is present in the tree
            if current.children[ascii_index]:
                # Keep going
                current = current.children[ascii_index]
            else:
                if isinstance(current.data, tuple) and current.data[0] in numbers:
                    # Not leaf but contain prefixd
                    # print(current.data)
                    print("Data: ", current.data)
                    return current.data
                else:
                    # Number is not present
                    return False
        # if we consider all numbers and the node is a leaf we found the number
        if current.leaf and current.data[0] in numbers:
            print("Current Data:", current.data)
            return True
        # number is not present in the tree
        return False


    def insert_file(self, route_costs):
        index = 0
        while index < len(route_costs):
            # Start at the root node
            current = self.root
            # Numbers is a string of numbers and number is a char number
            for number in route_costs[index][0]:
                # We use ascii representation to get the index and transfer within the range
                # [0, CHILDREN_SIZE - 1]
                ascii_index = ord(number)-ord('0')
                # Check if theres a child with given number
                if current.children[ascii_index]:
                    # Keep going
                    current = current.children[ascii_index]
                else:
                    # Insert a new node
                    node = Node(number)
                    current.children[ascii_index] = node
                    current = node

            # leaf nodes represent the end of the words in the tree
            current.data = (route_costs[index][0], route_costs[index][1])
            current.leaf = True
            # print("Current Data", current.data)
            index += 1

        

    def search_file(self, numbers_file):
        # if the tree is empty
        if not self.root.children:
            return False
        index = 0
        while index < len(numbers_file):
            # start with the root node
            current = self.root
            # consider all the root node
            for number in numbers_file[index]:
                # print("Number: ", numbers_file)
                ascii_index = ord(number)-ord('0')
                # check if number is present in the tree
                if current.children[ascii_index]:
                    # Keep going
                    current = current.children[ascii_index]
                else:
                    
                    if isinstance(current.data, tuple) and current.data[0] in numbers_file[index]:
                        # Not leaf but contain prefixd
                        # print(current.data)
                        # print(current.data)
                        print("Current Data: ", current.data)
                        return current.data
                    else:
                        # Number is not present
                        continue
            index += 1
            # if we consider all numbers and the node is a leaf we found the number
            if current.leaf and current.data[0] in numbers_file:
                print("Current Data:", current.data)
                return True
            # number is not present in the tree
            return False

            


    
if __name__ == "__main__":
    
    trie = Trie()
    trie.insert_file(prefix_cost_dict('route-costs-100.txt'))
    # trie.insert('1213', '0.05')
    # print(trie.search('12138881907'))
    # print(trie.search('1888417'))
    # print(trie.search_file(number_list('phone-numbers-1000.txt')))
    print(timeit.timeit("trie.search_file(number_list('phone-numbers-1000.txt'))", globals=globals(), number=1))


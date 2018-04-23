import random
from collections import deque
    
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numMap = {}
        self.numElems = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.numMap:
            return False

        self.numMap[val] = 1
        self.numElems += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.numMap:
            return False
        
        del self.numMap[val]
        self.numElems -= 1
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.numElems > 0:
            return random.choice(list(self.numMap.keys()))
        else:
            return False


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

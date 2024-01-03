"""
Type: Medium
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
"""

import random
from random import randint


class RandomizedSetSolution2:
    def __init__(self):
        self.dictionary = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dictionary:
            return False
        else:
            self.dictionary[val] = val
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dictionary:
            self.dictionary.pop(val)
            self.list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        key = random.choice(self.list)
        return self.dictionary[key]


class RandomizedSetSolution1:
    def __init__(self):
        self.dictionary = {}

    def insert(self, val: int) -> bool:
        if self.dictionary.get(val) is None:
            self.dictionary[val] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.dictionary.get(val) is not None:
            self.dictionary.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        numKey = randint(0, len(self.dictionary) - 1)
        key = list(self.dictionary.keys())[numKey]
        return self.dictionary[key]


# Your RandomizedSet object will be instantiated and called as such:
val1 = 10
val2 = 15
val3 = 20

randomSet = RandomizedSetSolution2()
print(randomSet.insert(-1))
print(randomSet.remove(-2))
print(randomSet.insert(-2))
print(randomSet.getRandom())
print(randomSet.remove(-1))
print(randomSet.insert(-2))
print(randomSet.getRandom())



# print(randomSet.insert(val1))
# print(randomSet.insert(val1))
# print(randomSet.insert(val2))
# print(randomSet.insert(val3))
# print(randomSet.insert(13))
# print(randomSet.insert(11))
# print("------")
# print(randomSet.remove(val2))
# print(randomSet.remove(val1))
# print(randomSet.remove(40))
# print(randomSet.remove(-10))
# print("------")
# print(randomSet.getRandom())
# print(randomSet.getRandom())
# print(randomSet.getRandom())

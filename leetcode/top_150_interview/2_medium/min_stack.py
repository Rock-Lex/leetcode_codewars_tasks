"""
Type: Medium
155. Min Stack
https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List
from icecream import ic


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_element = self.getMin()
        if min_element is None or val < min_element:
            min_element = val
        self.stack.append([val, min_element])

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
ic(minStack.getMin())  # return -3
minStack.pop()
ic(minStack.top())  # return 0
ic(minStack.getMin())  # return -2

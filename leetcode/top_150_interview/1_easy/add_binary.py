"""
Type: Easy
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List, Optional
from icecream import ic


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        memory = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or memory:
            if i >= 0:
                memory += int(a[i])
                i -= 1
            if j >= 0:
                memory += int(b[j])
                j -= 1
            answer.append(str(memory % 2))
            memory //= 2

        return ''.join(reversed(answer))


a = "0"
b = "0"
sol = Solution()
ic(sol.addBinary(a, b))
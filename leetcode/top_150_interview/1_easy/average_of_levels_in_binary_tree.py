"""
Type: Easy
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        answ = []
        d = deque([root])

        while d:
            level_size = len(d)
            level_sum = 0

            for _ in range(level_size):
                node = d.popleft()
                level_sum += node.val

                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)

            answ.append(level_sum / level_size)
        return answ
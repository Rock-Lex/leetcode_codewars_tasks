"""
Type: Easy
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
"""

from copy import copy
from typing import List, Optional

from icecream import ic


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deep_first_search(root):
    if root is None:
        return root
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        root.left = deep_first_search(root.left)
        root.right = deep_first_search(root.right)
        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deep_first_search(root)


root = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
ic(sol.invertTree(root))
